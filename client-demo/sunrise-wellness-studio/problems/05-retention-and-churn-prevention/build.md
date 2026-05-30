# #05 — Build Playbook: Retention & Churn Prevention

> Step-by-step GHL build. Estimated time: **2.5 hours** for a competent operator. This is a flagship problem — the engagement scoring formula needs careful testing, and the intervention workflow has branches per risk level. Build the scoring engine first, then the interventions, then connect them.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Engagement & Activity fields (`last_visit_date`, `visits_last_30_days`, `visits_last_90_days`, `noshow_count_90d`, `engagement_score`, `at_risk_flag`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Score inputs and outputs |
| Membership fields (`membership_status`, `membership_tier`, `monthly_rate`, `days_as_member`) | Same | Gate scoring to active members only |
| Tags: `member-active`, `member-paused`, `risk-healthy`, `risk-watching`, `risk-at-risk`, `risk-critical`, `do-not-email`, `do-not-email`, `vip-do-not-disturb` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Risk segmentation and suppression |
| Pipeline: **Retention** with stages Healthy / Watching / At-Risk / Critical / Save In Progress / Saved / Lost-Cancelled | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Owner-facing kanban |
| Custom values: `team.owner_first`, `business.short_name`, `business.sms_number`, `business.booking_url`, `offer.first_pt_session`, `voice.signature_owner` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| Product: **Personal Training — Single Session** (SKU `PT-SINGLE`) — referenced in save offer | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Free PT redemption credit |
| Workflow from [#04 New Member Onboarding](../04-new-member-onboarding/) graduating members into Retention at Day 30 | [#04](../04-new-member-onboarding/) | Inbound source of new active members |
| Attendance ingestion already populating `last_visit_date` and `visits_last_30_days` (via class check-in or PT completion) | [#03 Appointment No-Show Recovery](../03-appointment-no-show-recovery/build.md) | Score input data |

If any field is empty for existing members, the score will be 0 and they'll all flag as `risk-critical` on first run. **Backfill attendance data before turning the scoring workflow ON.** See Step 6.

---

## Step 1 — Verify Retention Pipeline Exists (5 min)

Navigate to **Opportunities > Pipelines**.

Confirm a pipeline named **Retention** exists with these stages in this order:

1. Healthy
2. Watching
3. At-Risk
4. Critical
5. Save In Progress
6. Saved
7. Lost-Cancelled
8. Win-Back D30
9. Win-Back D60
10. Win-Back D90
11. Reactivated
12. Permanent Loss

Stages 8–12 are owned by [#09 Win-Back](../09-win-back-lapsed-members/) — they exist but #05 only writes to stages 1–7.

If the pipeline doesn't exist, build it per the spec in [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) before continuing.

---

## Step 2 — Build the Engagement Scoring Workflow (60 min)

This is the heart of the retention system. It runs every night, recomputes every active member's score, and triggers downstream interventions when scores drop.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `05a — Engagement Scoring (Nightly)`
- **Folder:** Create folder `05 - Retention` and put it there
- **Re-entry:** Enabled (this re-runs on the same contact every night)

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)** under "Workflow A". Build order:

### 2.1 Trigger

Click **+ Add New Workflow Trigger**.

- **Trigger:** Schedule (Time-Based / Cron)
- **Schedule:** Daily at 2:00 AM `{{custom_values.business.timezone}}`
- **Filter — Contact has tag:** `member-active`
- **Filter — Contact does NOT have tag:** `member-paused` (paused members don't count against engagement)
- **Filter — Contact does NOT have tag:** `member-onboarding` (onboarding members are scored by [#04](../04-new-member-onboarding/), not here)

> **Note on the schedule trigger:** Some GHL plans don't expose a pure cron trigger; the workaround is a "Loop Through Contacts" trigger fired by a parent meta-workflow that runs nightly. Both end up at the same place. Use whichever your plan supports. The downstream actions are identical.

### 2.2 Action — Compute the Engagement Score

GHL's workflow builder doesn't have a "math" action. The score is computed by a chain of If/Else branches that *add to* a running total stored in `engagement_score`.

**Reset the score** first:

- **Action:** Update Contact Field → `engagement_score` = `0`

Then add the visit-frequency component:

- **Action:** If/Else on `visits_last_30_days`
  - `>= 12` → Update `engagement_score` = `100`
  - `>= 8 AND < 12` → Update `engagement_score` = `85`
  - `>= 4 AND < 8` → Update `engagement_score` = `60`
  - `>= 1 AND < 4` → Update `engagement_score` = `30`
  - `= 0` → leave at `0`

After branches reconverge, apply **recency decay**:

- **Action:** If/Else on days since `last_visit_date`
  - `> 14 days` → Update `engagement_score` = `engagement_score - 20`
  - `> 21 days` → Update `engagement_score` = `engagement_score - 35` (replaces the −20)
  - `> 30 days` → Update `engagement_score` = `engagement_score - 50` (replaces the −35)

Apply **no-show decay**:

- **Action:** If/Else on `noshow_count_90d`
  - `>= 3` → Update `engagement_score` = `engagement_score - 15`
  - `>= 5` → Update `engagement_score` = `engagement_score - 30`

Apply **engagement boost** (responded to last marketing touch):

- **Action:** If/Else on contact tag `email-engaged-30d` OR `sms-engaged-30d`
  - True → Update `engagement_score` = `engagement_score + 10`

Apply **floor and ceiling**:

- **Action:** If/Else: `engagement_score > 100` → set to `100`
- **Action:** If/Else: `engagement_score < 0` → set to `0`

> **Important:** GHL's "Update Field" using a math expression (`engagement_score - 20`) is supported in newer GHL versions only. On older plans, you must compute the final value per branch. The expanded If/Else tree gets long but works. See the full expansion in [assets/workflow.md](assets/workflow.md).

### 2.3 Action — Capture the Previous Risk Flag (for transition detection)

Before we update `at_risk_flag`, stash the previous value so we can detect downward crossings.

- **Action:** Update Contact Field → `at_risk_flag_previous` = `{{contact.at_risk_flag}}`

> If `at_risk_flag_previous` doesn't exist as a custom field, add it now to the Engagement & Activity folder. Type: Single Line.

### 2.4 Action — Set the New Risk Flag

Based on the new `engagement_score`, update `at_risk_flag` and the corresponding tag.

- **Action:** If/Else on `engagement_score`
  - `>= 70` → Update `at_risk_flag` = `No`, Add tag `risk-healthy`, Remove tags `risk-watching` / `risk-at-risk` / `risk-critical`
  - `>= 50 AND < 70` → Update `at_risk_flag` = `Watching`, Add tag `risk-watching`, Remove others
  - `>= 30 AND < 50` → Update `at_risk_flag` = `At-Risk`, Add tag `risk-at-risk`, Remove others
  - `< 30` → Update `at_risk_flag` = `Critical`, Add tag `risk-critical`, Remove others

### 2.5 Action — Move the Retention Pipeline Stage

- **Action:** If/Else on new `at_risk_flag`
  - `No` → Move Retention opportunity to **Healthy** stage
  - `Watching` → Move to **Watching** stage
  - `At-Risk` → Move to **At-Risk** stage
  - `Critical` → Move to **Critical** stage

If no Retention opportunity exists for this contact, create one first:

- **Action:** Create Opportunity
- **Pipeline:** Retention
- **Stage:** (matches new flag)
- **Opportunity Name:** `{{contact.first_name}} {{contact.last_name}} — Retention`
- **Value:** `{{contact.monthly_rate}} * 12`
- **Skip if:** Contact already has Open opportunity in Retention pipeline (just move the existing one)

### 2.6 Action — Detect Downward Crossing & Trigger Intervention

This is the key behavior. We don't want to spam interventions every night a member is at-risk — only fire when their risk **level** transitions downward.

- **Action:** If/Else
  - Condition: `at_risk_flag` changed from `No` to `Watching` → Add tag `transition-to-watching`
  - Condition: `at_risk_flag` changed from `No`/`Watching` to `At-Risk` → Add tag `transition-to-at-risk`
  - Condition: `at_risk_flag` changed from any to `Critical` → Add tag `transition-to-critical`
  - No downward transition → Skip (exit workflow)

The tags `transition-to-*` are the trigger fuel for Workflow B. They're applied here, consumed there, removed by that workflow at end.

### 2.7 Publish

Click **Save** then **Publish**. **Do not toggle ON yet** — we need the intervention workflow built first.

---

## Step 3 — Build the At-Risk Intervention Workflow (60 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `05b — At-Risk Intervention`
- **Folder:** `05 - Retention`
- **Re-entry:** Disabled per risk level (use tag-based re-entry blocks — see below)

Full spec in [assets/workflow.md](assets/workflow.md) under "Workflow B".

### 3.1 Trigger

- **Trigger:** Tag Added
- **Filter — Tag is:** `transition-to-watching` OR `transition-to-at-risk` OR `transition-to-critical`
- **Filter — Contact has tag:** `member-active`
- **Filter — Contact does NOT have tag:** `do-not-email` AND `do-not-email` (if both blocked, owner-call task is the only option — handled in Critical branch)

### 3.2 Action — Branch by Severity

- **Action:** If/Else
  - Has tag `transition-to-critical` → go to **Branch C (Critical)**
  - Has tag `transition-to-at-risk` → go to **Branch B (At-Risk)**
  - Has tag `transition-to-watching` → go to **Branch A (Watching)**

### 3.3 Branch A — Watching (lightweight nudge)

The lightest touch. We're letting them know we noticed.

1. **Wait:** 0 (immediate)
2. **Send Email:** Template `05 — Watching Soft Check-In` from [assets](assets). Skip if `do-not-email` or `sms_opt_in` ≠ Yes.
3. **Add tag:** `campaign-retention-watching`
4. **Remove tag:** `transition-to-watching`
5. **Wait:** 7 days
6. **If/Else:** `last_visit_date` within last 7 days?
   - Yes → Add tag `save-watching-success`. Exit.
   - No → Workflow B's behavior cascades because the next nightly score run will likely move them to At-Risk and re-trigger. Exit cleanly here.

### 3.4 Branch B — At-Risk (active intervention)

This is the real save attempt.

1. **Wait:** 0
2. **Create opportunity / move existing:** Retention pipeline → **Save In Progress** stage.
3. **Send Email:** Template `05 — At-Risk Warm Hello` from [assets](assets). Skip if `do-not-email`.
4. **Wait:** 4 hours
5. **Send Email:** Template `05 — At-Risk Personal from Morgan` from [assets/emails.md](assets/emails.md). Skip if `do-not-email`.
6. **Wait:** 2 days
7. **If/Else:** Has contact replied to Email OR visited in last 48 hours?
   - Yes → Add tag `save-at-risk-engaged`, notify owner ("Good news — Sarah just replied / showed up"), proceed to step 10.
   - No → Continue.
8. **Send Email:** Template `05 — Win-Them-Back Free PT Offer` from [assets/emails.md](assets/emails.md). The offer in `{{custom_values.offer.first_pt_session}}` is the lever. Skip if `do-not-email`.
9. **Wait:** 5 days
10. **If/Else:** `last_visit_date` within last 7 days OR booked PT session?
    - Yes → Move Retention opportunity to **Save In Progress** (still). Add tag `save-at-risk-success-pending`. Wait until next nightly run promotes them to Healthy → workflow will move to **Saved** stage.
    - No → Add tag `save-at-risk-failed`. Exit. Member will continue under nightly monitoring; if score keeps falling, Critical branch fires next.
11. **Remove tag:** `transition-to-at-risk` (consume the trigger fuel)
12. Exit.

### 3.5 Branch C — Critical (owner-personal save attempt)

The member is hours-to-days from cancelling. Owner gets involved.

1. **Wait:** 0
2. **Move Retention opportunity:** to **Critical** stage (if not already there).
3. **Send Internal Notification (owner):** High-priority alert. Subject: `URGENT — {{contact.first_name}} {{contact.last_name}} is Critical retention risk`. Body includes: name, phone, last visit date, total months as member, monthly rate, recent attendance pattern. CTA: "Call within 48 hours."
4. **Create Task:** Assigned to Owner. Title: `Call {{contact.first_name}} {{contact.last_name}} — Critical retention`. Due: 48 hours.
5. **Wait:** 2 hours (let the owner see the alert before the auto-Email goes)
6. **If/Else:** Contact has tag `vip-do-not-disturb`?
   - Yes → Skip auto-Email. Owner handles 100%. Proceed to step 9.
   - No → Continue.
7. **Send Email:** Template `05 — Critical Owner-Personal Email` from [assets](assets). Sent **from the owner's number**, not the general Email number. This is a "I'm reaching out personally" moment.
8. **Wait:** 5 days
9. **If/Else:** Contact replied OR visited in last 5 days?
   - Yes → Notify owner: "Saved — {{contact.first_name}} re-engaged after Critical." Add tag `save-critical-success-pending`. Move Retention opp to **Save In Progress**.
   - No → Notify owner: "{{contact.first_name}} did not respond to Critical sequence. May cancel imminently. Personal call recommended."
10. **Remove tag:** `transition-to-critical`
11. Exit.

### 3.6 Publish

Click **Save** then **Publish**. Toggle ON.

---

## Step 4 — Add the "Save Success" Watcher (15 min)

A small helper workflow that watches for members in the Save In Progress stage who climb back to Healthy, and moves them to the Saved (Won) stage with a celebration notification.

Navigate to **Automation > Workflows > + Create Workflow**.

- **Workflow Name:** `05c — Save Success Detector`
- **Folder:** `05 - Retention`

### 4.1 Trigger

- **Trigger:** Tag Added
- **Tag:** `risk-healthy`
- **Filter — Contact has tag:** `save-at-risk-success-pending` OR `save-critical-success-pending`

### 4.2 Actions

1. **Move Retention opportunity:** to **Saved** stage (mark Won, value = `monthly_rate × 12`)
2. **Notify owner:** "Win! {{contact.first_name}} {{contact.last_name}} just moved from at-risk back to healthy. That's a ${{contact.monthly_rate}}/mo save."
3. **Remove tags:** `save-at-risk-success-pending`, `save-critical-success-pending`, `campaign-retention-watching`
4. **Add tag:** `member-saved` (permanent badge — feeds [#06 upsell readiness](../06-upsell-and-cross-sell/) at day 30)
5. **Wait:** 30 days
6. **Add tag:** `save-mature-30d` — this is the signal to [#06 Upsell & Cross-Sell](../06-upsell-and-cross-sell/) that the relationship rebuild is solid and an upsell can be offered.

### 4.3 Publish & toggle ON.

---

## Step 5 — Add the "Save Failure → Cancel" Detector (10 min)

When a Critical-stage member submits a cancellation, route them to [#09 Win-Back](../09-win-back-lapsed-members/) immediately.

- **Workflow Name:** `05d — Save Failure → Cancel Handoff`
- **Folder:** `05 - Retention`

### 5.1 Trigger

- **Trigger:** Tag Added → `member-cancelled`
- **Filter:** Contact has tag `save-at-risk-failed` OR `save-critical-success-pending` OR `risk-at-risk` OR `risk-critical`

### 5.2 Actions

1. **Move Retention opportunity:** to **Lost-Cancelled** stage (mark Lost)
2. **Remove tags:** `risk-at-risk`, `risk-critical`, `save-*-success-pending`
3. **Notify owner:** "Lost — {{contact.first_name}} cancelled despite save attempt. Reason: {{contact.cancel_reason}}. Routing to win-back."
4. **Add to Workflow:** `09a — Win-Back D30` (defined in [#09 build](../09-win-back-lapsed-members/build.md))
5. Exit.

### 5.3 Publish & toggle ON.

---

## Step 6 — Backfill Existing Members (30 min) — CRITICAL

If you turn on `05a — Engagement Scoring` now without backfilling, every existing member with empty `visits_last_30_days` will score 0 and flag as `risk-critical`. The owner will get 250 critical alerts overnight. **Don't do that.**

### 6.1 Bulk-update active members' attendance data

If you have attendance history in another system (a class-booking tool, a spreadsheet), import it:

1. Export attendance data: `contact_email, visit_count_30d, last_visit_date`.
2. In GHL: **Contacts > Import > CSV**. Match columns to `visits_last_30_days` and `last_visit_date`.
3. Run the import. Confirm at least 90% of `member-active` contacts now have non-zero `visits_last_30_days`.

If you don't have history, set a default:

1. **Bulk Action:** Smart list = `member-active`. Action = "Update Field" → `visits_last_30_days` = `4` (places everyone in the 60-pt "Watching" buffer to start, avoids false critical alerts).
2. Set `last_visit_date` = today minus 7 days for the same group (so recency decay doesn't fire on day 1).

### 6.2 Test the scoring engine on yourself first

1. Set your own test contact: `visits_last_30_days` = 12, `last_visit_date` = today, `noshow_count_90d` = 0.
2. Manually trigger Workflow 05a on yourself (right-click contact → Add to Workflow).
3. Confirm `engagement_score` = 100, `at_risk_flag` = `No`, tag `risk-healthy` applied.
4. Now change `visits_last_30_days` to 1 and re-run. Expect score = 30, flag = `At-Risk`, tag updated.
5. Confirm Workflow 05b fires (look for Email in your inbox if your number is on the contact).

### 6.3 Turn ON the scoring workflow

Now you can toggle `05a — Engagement Scoring` ON.

Check the workflow execution history the next morning. Expect ~250 successful runs (one per active member) with a distribution that matches your business reality (~70% Healthy, 20% Watching, 8% At-Risk, 2% Critical for a healthy studio).

If the distribution looks off (e.g., 60% Critical), the input data is bad. Pause the workflow, fix the input data, restart.

---

## Step 7 — Build Owner Smart Lists (10 min)

Smart lists let the owner see the kanban at-a-glance in any view.

Navigate to **Contacts > Smart Lists > + Create**.

### List 1: At-Risk + Critical (the daily glance)

- Name: `Retention — Needs Owner Attention`
- Filters: Has tag `risk-at-risk` OR `risk-critical`. Has tag `member-active`. Sort by `engagement_score` ascending.

### List 2: Saves in progress

- Name: `Retention — Save in Progress`
- Filters: Has tag `save-at-risk-success-pending` OR `save-critical-success-pending`.

### List 3: Recent wins

- Name: `Retention — Recent Saves (30d)`
- Filters: Has tag `member-saved`. Save event in last 30 days. (Use a date-added-to-tag filter if your GHL supports it; otherwise, manual.)

### List 4: Watching members (lower urgency)

- Name: `Retention — Watching`
- Filters: Has tag `risk-watching`. Has tag `member-active`. Sort by `last_visit_date` ascending.

These four lists feed the [#10 Owner Reporting](../10-owner-reporting-and-visibility/) Retention widget.

---

## Test Plan

Run this test sequence after publishing all workflows. **Do not declare done until all pass.**

### Test 1 — Healthy scoring

1. Create test contact `test-healthy@example.com` with `member-active` tag, `visits_last_30_days` = 14, `last_visit_date` = today, `noshow_count_90d` = 0.
2. Add to workflow `05a — Engagement Scoring` manually.
3. **Expected:** `engagement_score` = 100, `at_risk_flag` = No, tag `risk-healthy` applied. No Email sent. Retention opportunity in **Healthy** stage.

### Test 2 — Watching transition

1. Same contact. Change `visits_last_30_days` to 5, `last_visit_date` to 5 days ago.
2. Re-run workflow 05a.
3. **Expected:** Score = 60. Flag = Watching. Tag swapped to `risk-watching`. Tag `transition-to-watching` applied.
4. **Within 60 sec:** Workflow 05b fires Branch A. Email arrives at test phone. `campaign-retention-watching` tag applied.

### Test 3 — At-Risk transition

1. Same contact. Change `visits_last_30_days` to 2, `last_visit_date` to 16 days ago, `noshow_count_90d` to 3.
2. Re-run.
3. **Expected:** Score = 30 − 20 − 15 = −5 → floored to 0… wait, let me recompute: visits 2 = 30, − 20 recency = 10, − 15 noshow = −5 → floor 0. Actually that scores too low — verify the score calc. The expected is **At-Risk band (30–49)** OR Critical depending on exact numbers; design intent is that 2 visits + 16d gap + 3 noshows is solidly at-risk-or-worse. Adjust the test inputs to land cleanly in 30–49 if needed (try visits=2, last_visit=10d ago, noshow=2 → score = 30 − 0 − 0 = 30 → At-Risk).
4. **Expected workflow:** Branch B fires. Email in 0 min, email in 4 hours, follow-up offer email in 2 days.

### Test 4 — Critical transition + owner notification

1. Same contact. Set `visits_last_30_days` = 0, `last_visit_date` = 25 days ago.
2. Re-run.
3. **Expected:** Score = 0 − 35 = floored to 0. Flag = Critical. Owner gets alert email. Owner task created. After 2-hour wait, Email goes out from owner number.

### Test 5 — Save success path

1. After Test 3 (At-Risk), simulate a visit: update `visits_last_30_days` = 8, `last_visit_date` = today.
2. Re-run workflow 05a.
3. **Expected:** Score climbs to ~85, flag returns to Healthy, tag swaps to `risk-healthy`. Workflow 05c fires. Retention opportunity moves to **Saved**. Owner gets "win" notification.

### Test 6 — Suppression respected

1. Create contact with `do-not-email` tag. Trigger At-Risk transition.
2. **Expected:** Email sends, Email skipped. No errors.

### Test 7 — VIP do-not-disturb

1. Create contact with `vip-do-not-disturb` AND trigger Critical.
2. **Expected:** Owner alert + task fires. Auto-Email to member skipped. Owner is the sole contact channel.

### Test 8 — Paused member ignored

1. Set test contact to `member-paused`.
2. Run nightly trigger.
3. **Expected:** Contact filter blocks workflow entry. No score change.

---

## Common Build Mistakes (avoid these)

1. **Math operations not supported.** If your GHL plan doesn't support `field = field - 20`-style math in Update Contact Field, you must expand every branch into explicit final-value computations. Tedious but works. The full expanded version is in [assets/workflow.md](assets/workflow.md) appendix.
2. **Forgot to backfill `visits_last_30_days`.** First night fires, every member flags Critical, owner gets 250 alerts, owner cancels you. Backfill first.
3. **Re-entry settings wrong on 05a.** Must be **enabled** — the workflow needs to re-run nightly on the same contact. If disabled, it fires once and never again.
4. **Re-entry settings wrong on 05b.** Must use tag-based re-entry blocks — otherwise a member who transitions from Watching → At-Risk same week gets the Watching Email, then the At-Risk Email, in close succession. Solution: each branch removes its trigger tag at start; transition tags should never both be present.
5. **Recency decay double-counts.** If you use cumulative If/Else (`> 14` then separately `> 21`), a member 22 days idle gets −20 AND −35 = −55. Decay should be a single branch: use mutually exclusive conditions (else-if chain), not separate ifs.
6. **Owner gets 250 nightly emails.** The Owner alert in Branch C should fire **only on transition** to Critical, not every night a member stays Critical. The `transition-to-critical` tag-based trigger guards this — confirm it's working.
7. **Stage moves create duplicate opportunities.** If you "Create" instead of "Move," you get a new opportunity every night. Always use "Move existing opportunity if present; create only if absent."
8. **Score lookup vs storage drift.** `engagement_score` and `at_risk_flag` are stored values, computed nightly. Smart lists that filter on these are accurate as of last night, not real-time. Acceptable — the cadence is nightly by design.

---

## What's Next

Once this is live and producing data:

- Members who get a `member-saved` tag and graduate to `save-mature-30d` are surfaced to **[#06 Upsell & Cross-Sell](../06-upsell-and-cross-sell/build.md)** as upsell-ready candidates.
- Members who cancel despite saves are picked up by **[#09 Win-Back Lapsed Members](../09-win-back-lapsed-members/build.md)** via the handoff in Step 5.
- All retention metrics flow into the **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)** dashboard, including save rate, churn rate, and at-risk distribution.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
