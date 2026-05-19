# #04 — Build Playbook: New Member Onboarding

> Step-by-step GHL build. Estimated time: **3 hours** for a competent operator. One main workflow (long, 30 days) + pipeline configuration + 11 messages.

---

## Prerequisites (from shared-foundation/)

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Membership fields (`membership_tier`, `membership_status`, `membership_start_date`, `monthly_rate`, `days_as_member`, `onboarding_completed`, `onboarding_completed_date`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Member state |
| Fitness Profile fields (`fitness_goal_primary`, `fitness_experience`, `preferred_workout_time`, `assigned_trainer`, `nutrition_interest`) | Same | Personalization |
| Engagement fields (`last_visit_date`, `visits_last_30_days`, `total_visits_lifetime`, `last_class_attended`, `last_pt_session_date`) | Same | Attendance branching |
| Tags: `member-active`, `member-onboarding`, `campaign-onboarding`, `tier-basic`/`tier-premium`/`tier-vip`, `risk-healthy`/`risk-watching`/`risk-at-risk`/`risk-critical` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | State machine |
| Pipeline: **Onboarding** with all 8 stages | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Owner visibility |
| Custom values: `business.short_name`, `business.booking_url`, `team.owner_first`, `team.owner_name`, `voice.greeting_warm`, `offer.first_pt_session`, `offer.nutrition_starter`, `class.hiit`, `class.yoga`, etc. | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |

---

## Step 1 — Verify Onboarding Pipeline (10 min)

Confirm the Onboarding pipeline from [shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) is built with these stages:

1. Welcome Sent (Day 0)
2. First Visit Confirmed
3. Week 1 Check-In
4. Two-Week Milestone
5. Goal Review (Day 21)
6. Onboarded (Day 30) — Won
7. Onboarding At-Risk
8. Early Churn Risk

If not built, build it now. Navigate to **Opportunities > Pipelines > + Create Pipeline > "Onboarding"** and create stages exactly as named.

---

## Step 2 — Build Email Templates (45 min)

Navigate to **Marketing > Emails > Templates > + New Template**.

Build each template from [assets/emails.md](assets/emails.md):

| Template Name | Send Day | Used in workflow step |
|---|---|---|
| `04 — Day 0 — Welcome to the Studio` | Day 0 | Step 4.2 |
| `04 — Day 7 — Week 1 Check-In` | Day 7 | Step 4.7 |
| `04 — Day 14 — Two-Week Milestone` | Day 14 | Step 4.10 |
| `04 — Day 14 — At-Risk (zero visits)` | Day 14 (branched) | Step 4.10b |
| `04 — Day 21 — Goal Review Invite` | Day 21 | Step 4.13 |
| `04 — Day 30 — Graduation` | Day 30 | Step 4.16 |

Each template has tier-conditional sections and goal-conditional sections — see [assets/emails.md](assets/emails.md) for full copy.

---

## Step 3 — Build SMS Templates (15 min)

Navigate to **Marketing > Templates > SMS > + New Template**.

| Template Name | Send Day | Used in workflow step |
|---|---|---|
| `04 — Day 1 — Personal Welcome SMS` | Day 1 | Step 4.4 |
| `04 — Day 3 — No Visit Yet (gentle)` | Day 3 (conditional) | Step 4.6 |
| `04 — Day 14 — Milestone Celebrate` | Day 14 | Step 4.10 |
| `04 — Day 21 — Goal Review Reminder` | Day 21 | Step 4.13 |
| `04 — Day 30 — Graduation` | Day 30 | Step 4.16 |

---

## Step 4 — Build the 30-Day Onboarding Workflow (90 min)

This is the longest workflow in the build. Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `04 — New Member Onboarding — 30 Day`
- **Folder:** Create `04 - Onboarding`

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 4.1 Trigger

- **Trigger:** Tag Added
- **Filter:** Tag is `member-onboarding`
- **Filter:** Contact has `member-active`
- **Filter:** Contact does NOT have `campaign-onboarding` (prevents re-entry)

### 4.2 Action: Day 0 Setup

- **Add Tag:** `campaign-onboarding`
- **Update Contact Field:** `membership_status` = `Active`
- **Create Opportunity:** Pipeline `Onboarding`, Stage `Welcome Sent (Day 0)`, Value = `monthly_rate × 12`
- **Send Email:** `04 — Day 0 — Welcome to the Studio`

(No Day 0 SMS — they just got the conversion-confirmation SMS from #02. Don't double-send within the hour.)

### 4.3 Action: Wait until Day 1, 10 AM contact-local

- **Wait Until:** `membership_start_date + 1 day` at 10:00 AM contact-local

### 4.4 Action: Day 1 Personal SMS

- **Send SMS:** `04 — Day 1 — Personal Welcome SMS` (from Morgan, personal-tone)

### 4.5 Action: Wait until Day 3, 11 AM

- **Wait Until:** `membership_start_date + 3 days` at 11:00 AM contact-local

### 4.6 Action: Day 3 Visit Check

- **If/Else:** `last_visit_date` >= `membership_start_date` (have they visited since signup?)
  - **Yes:** Add tag `onboarding-attended-week1`. Continue.
  - **No:** Send SMS `04 — Day 3 — No Visit Yet (gentle)`. Add tag `onboarding-needs-nudge`.

### 4.7 Action: Wait until Day 7, 9 AM → Week 1 Check-In Email

- **Wait Until:** `membership_start_date + 7 days` at 9:00 AM contact-local
- **Update Opportunity Stage:** `Week 1 Check-In`
- **Send Email:** `04 — Day 7 — Week 1 Check-In`

### 4.8 Action: Wait until Day 8, 6 PM → Trainer/PT booking nudge (tier-specific)

- **Wait Until:** `membership_start_date + 8 days` at 6:00 PM contact-local
- **If/Else:** `membership_tier` =
  - **Basic:** No automated PT nudge (Basic doesn't include PT). Skip.
  - **Premium / VIP:** Send SMS: *"Hey {{first_name}} — your membership includes PT sessions. Want me to set up your first one with {{contact.assigned_trainer}}? Just reply with a day/time."*

### 4.9 Action: Wait until Day 14, 8 AM

- **Wait Until:** `membership_start_date + 14 days` at 8:00 AM contact-local

### 4.10 Action: Day 14 Milestone + Branching

- **If/Else:** `visits_last_30_days` (since membership_start_date) — how many?
  - **3+ visits → Healthy path:**
    - Add Tag `risk-healthy`
    - Update Opportunity Stage `Two-Week Milestone`
    - Send Email `04 — Day 14 — Two-Week Milestone`
    - Send SMS `04 — Day 14 — Milestone Celebrate`
  - **1-2 visits → Watching path:**
    - Add Tag `risk-watching`
    - Update Opportunity Stage `Two-Week Milestone`
    - Send Email `04 — Day 14 — Two-Week Milestone` (slightly different version — encouraging more frequency)
  - **0 visits → Early Churn Risk path:**
    - Add Tag `risk-critical`
    - Update Opportunity Stage `Early Churn Risk`
    - Send Email `04 — Day 14 — At-Risk (zero visits)`
    - Send Internal Notification to Morgan ("CRITICAL: {{contact.first_name}} has zero visits — please call this week")

### 4.11 Action: Wait until Day 17 → if still zero visits, escalate

- **Wait Until:** `membership_start_date + 17 days`
- **If/Else:** still zero visits AND `risk-critical`?
  - **Yes:** Send personal SMS from Morgan: *"Hey {{first_name}}, Morgan here. Wanted to check in — you joined 17 days ago and haven't been able to come in yet. Totally happens. Anything I can do? Even a 10-min phone call works."*
  - **No:** Skip.

### 4.12 Action: Wait until Day 21, 9 AM

- **Wait Until:** `membership_start_date + 21 days` at 9:00 AM contact-local

### 4.13 Action: Day 21 Goal Review Invite

- **Update Opportunity Stage:** `Goal Review (Day 21)`
- **Send Email:** `04 — Day 21 — Goal Review Invite`
- **Wait 6 hours**
- **Send SMS:** `04 — Day 21 — Goal Review Reminder`

The email includes a direct calendar link to book a 30-min goal review with the assigned trainer (or Morgan, if no assignment).

### 4.14 Action: Wait until Day 25 → check if booked

- **Wait Until:** `membership_start_date + 25 days`
- **If/Else:** Has the member booked the goal review? (Check: any appointment on `Goal Review Calendar` between days 21-30 for this contact)
  - **Yes:** No further nudge.
  - **No:** Send SMS: *"{{first_name}}, your goal review with {{contact.assigned_trainer}} is still open — grab 30 min: {{custom_values.business.booking_url}}"*

### 4.15 Action: Wait until Day 30, 10 AM

- **Wait Until:** `membership_start_date + 30 days` at 10:00 AM contact-local

### 4.16 Action: Day 30 Graduation + Handoff

- **Send Email:** `04 — Day 30 — Graduation`
- **Send SMS:** `04 — Day 30 — Graduation`
- **Update Contact Field:** `onboarding_completed` = `Yes`
- **Update Contact Field:** `onboarding_completed_date` = today
- **Update Contact Field:** `days_as_member` = 30
- **Remove Tag:** `member-onboarding`
- **Remove Tag:** `campaign-onboarding`

### 4.17 Action: Pipeline outcome routing

- **If/Else:** Total visits since signup —
  - **3+ visits AND tag `risk-healthy`:**
    - Update Opportunity → `Onboarded (Day 30)`, Status `Won`
    - Create new Opportunity in `Retention` pipeline at stage `Healthy`
    - Add Tag `risk-healthy`
  - **1-2 visits AND `risk-watching`:**
    - Update Opportunity → `Onboarded (Day 30)`, Status `Won` (still won — they're paying)
    - Create new Opportunity in `Retention` at `Watching`
    - Add Tag `risk-watching`
  - **0 visits → Early Churn Risk persists:**
    - Update Opportunity stays at `Early Churn Risk`
    - Status `Open` (not yet Lost — give #05 Retention a chance to save)
    - Create new Opportunity in `Retention` at `Critical`
    - Add Tag `risk-critical`

### 4.18 Action: Add to #05 Retention workflow

- **Add to Workflow:** `05 — Retention & Churn Prevention`
- **Exit Workflow**

### 4.19 Publish

Click **Save** then **Publish**. Toggle ON.

---

## Step 5 — Build "Owner Quick Save" Companion (15 min)

When a member hits `risk-critical` during onboarding, Morgan needs a one-button way to fire the save SMS without manually typing.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `04 — Onboarding Save SMS (Owner-Triggered)`
- **Trigger:** Tag Added → `owner-save-sms` (Morgan manually adds this tag from the contact card when ready to send)
- **Filter:** Contact has `member-onboarding` AND `risk-critical`

**Actions:**

1. Send SMS from Morgan: *"Hey {{first_name}}, Morgan here personally — I noticed you joined 2 weeks ago and haven't been able to make it in. Totally happens; life is a thing. If schedule is the problem, just text me back with what time of day works for you and I'll find you a class. If something else is in the way, I'd love to know — I read every reply. — Morgan"*
2. Remove tag `owner-save-sms` (so it can be re-fired later).
3. Add tag `onboarding-save-attempted`.
4. Exit.

---

## Step 6 — Wire Visit-Update Triggers (10 min)

The workflow's Day-14 attendance branch relies on `visits_last_30_days` being current. Build a small companion workflow that updates this field every time the member checks in.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `04 — Visit Counter Update`
- **Trigger:** Appointment Status Changed → `Showed`
- **Filter:** Contact has tag `member-active`

**Actions:**

1. Update Contact Field: `last_visit_date` = today
2. Update Contact Field: `total_visits_lifetime` += 1
3. Update Contact Field: `visits_last_30_days` = (recompute — count Showed appointments in last 30 days)
4. Update Contact Field: `last_class_attended` = `{{appointment.calendar_name}} on {{today_short}}`

(If GHL exposes a check-in event separate from "appointment showed," wire to that instead.)

---

## Test Plan

### Test 1 — Workflow entry on member-onboarding tag

1. Test contact: manually add tags `member-active` + `member-onboarding`.
2. **Expected:** Day 0 welcome email arrives within 60 seconds. Opportunity created in Onboarding pipeline at "Welcome Sent (Day 0)". Tag `campaign-onboarding` applied.

### Test 2 — Day 1 SMS

1. Fast-forward workflow to Day 1, 10 AM.
2. **Expected:** Day 1 personal welcome SMS arrives.

### Test 3 — Day 3 visit branch

1. Test contact A: simulate a visit (set `last_visit_date` = today, after `membership_start_date`).
2. Fast-forward to Day 3.
3. **Expected:** No Day 3 SMS fires (they've attended). Tag `onboarding-attended-week1`.
4. Test contact B: no visits.
5. Fast-forward to Day 3.
6. **Expected:** Day 3 "no visit yet" SMS fires. Tag `onboarding-needs-nudge` applied.

### Test 4 — Day 14 three-way branch

1. Test contact A: simulate 3 visits since signup.
2. Fast-forward to Day 14.
3. **Expected:** Healthy path — Day 14 milestone email + SMS, tag `risk-healthy`.

4. Test contact B: simulate 1 visit.
5. Fast-forward to Day 14.
6. **Expected:** Watching path — Day 14 milestone email (different copy), tag `risk-watching`.

7. Test contact C: zero visits.
8. Fast-forward to Day 14.
9. **Expected:** At-Risk path — Day 14 at-risk email, tag `risk-critical`, opportunity moved to "Early Churn Risk", Morgan internal notification fires.

### Test 5 — Day 17 escalation

1. Test contact C from Test 4 (zero visits, `risk-critical`).
2. Fast-forward to Day 17.
3. **Expected:** Personal SMS from Morgan fires.

### Test 6 — Day 21 goal review

1. Fast-forward any test contact to Day 21.
2. **Expected:** Goal review invite email + SMS arrive. Opportunity stage → "Goal Review (Day 21)".

### Test 7 — Day 30 graduation + handoff

1. Test contact: 3+ visits, fast-forward to Day 30.
2. **Expected:**
   - Day 30 graduation email + SMS arrive.
   - `onboarding_completed` = Yes.
   - Onboarding opportunity moved to "Onboarded — Won".
   - New Retention opportunity created at "Healthy".
   - Tags `member-onboarding` and `campaign-onboarding` removed.
   - Tag `risk-healthy` applied.
   - Contact enrolled in workflow `05 — Retention & Churn Prevention`.

### Test 8 — Day 30 with zero visits (failed onboarding)

1. Test contact: zero visits through day 30.
2. **Expected:**
   - Day 30 graduation messages still send (or substitute with at-risk variant).
   - Onboarding opportunity stays at "Early Churn Risk", status Open.
   - New Retention opportunity created at "Critical".
   - Tag `risk-critical` persists.

### Test 9 — Owner save SMS

1. On a `risk-critical` test contact, manually add tag `owner-save-sms`.
2. **Expected:** Save SMS from Morgan fires immediately. Tag `onboarding-save-attempted` applied.

---

## Common Build Mistakes

1. **Workflow fires on existing members.** If a long-time member somehow gets `member-onboarding` re-applied (manual tag, import error), the whole 30-day machine restarts. Use the trigger filter "Contact does NOT have `campaign-onboarding`".
2. **Day-14 branch reads wrong visit count.** If the visit-counter workflow (Step 6) isn't built, `visits_last_30_days` may stay at 0 forever, and every member gets routed to At-Risk. Build Step 6 *before* publishing the main workflow.
3. **Quiet hours violated on Day 1 SMS.** A member who converts at 9 PM will get a Day 1 SMS the next morning at 10 AM — good. But if the workflow fires the Day 1 SMS *immediately* on the day-after wait, check that 10 AM contact-local is honored, not server time.
4. **Pipeline opportunity created but never moved.** Each Day's actions must include the opportunity stage update. Easy to forget — the kanban won't show progress.
5. **Goal review email sends but no calendar exists.** Step 4.13 requires a calendar named "Goal Review" or similar with the trainer's availability. Build the calendar in [#03 Step 1](../03-appointment-no-show-recovery/build.md) *or* set up a dedicated one for onboarding goal reviews.
6. **Day 30 handoff fires twice.** If contact lingers in workflow due to a wait-step bug, the handoff to #05 may double-enroll. Use the trigger filter on #05 — "Contact does NOT have tag `campaign-retention`" — to defend.

---

## What's Next

Once this is live and verified:

- Successful onboardings flow into **[#05 Retention](../05-retention-and-churn-prevention/build.md)** at the Healthy or Watching stage.
- Day-30 retention rate appears on the **[#10 Owner Dashboard](../10-owner-reporting-and-visibility/build.md)**.
- Basic members hitting 12+ visits in their first 30 days trigger early **[#06 Upsell](../06-upsell-and-cross-sell/build.md)** offers ("you'd love Premium").
- Members who book the Day-21 goal review and discuss nutrition get tagged `interest-nutrition`, which feeds the [#06 Upsell](../06-upsell-and-cross-sell/build.md) nutrition consult offer at a later point.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
