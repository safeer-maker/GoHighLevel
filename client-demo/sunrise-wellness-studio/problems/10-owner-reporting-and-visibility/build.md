# #10 — Build Playbook: Owner Reporting & Visibility

> Step-by-step GHL build. Estimated time: **240 minutes** for a competent operator. Eight smart lists, seven dashboard widgets, three workflows, three email templates. Prerequisites listed first. Build #10 LAST — every other problem must be live and producing data first.

---

## Prerequisites (from shared-foundation/ + all other problems)

Confirm these exist before starting. If anything is missing, the dashboard widgets will display zeros or fail to load.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| All 48+ custom fields | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Field-based smart list filters |
| All tags (lead-, trial-, member-, risk-, source-, campaign-) | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Tag-based smart list filters |
| All 3 pipelines (Membership Sales, Onboarding, Retention) | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Stage-based queries |
| Custom values: `team.owner_first`, `business.owner_email`, `business.short_name`, `business.timezone` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Email personalization |
| Workflows from #01–#09 live and producing tag/field updates | Each respective `build.md` | Source data — dashboard reads what those workflows wrote |

---

## Step 1 — Build All 8 Source Smart Lists (45 min)

The dashboard and digest both pull from these smart lists. Build them in **Contacts > Smart Lists > + New Smart List**.

### 1.1 Smart List: All Hot Leads

- **Name:** `All Hot Leads`
- **Filters:**
  - Tag includes ANY of: `lead-new`, `lead-responded`
  - Tag does NOT include: `trial-active`, `member-active`, `lead-cold`, `lead-lost`
  - `lead_captured_at` is within last 14 days

**Used by:** Dashboard widget #1 (New Leads This Week)

### 1.2 Smart List: Active Trials Needing Attention

- **Name:** `Active Trials Needing Attention`
- **Filters:**
  - Tag includes: `trial-active`
  - Tag does NOT include: `trial-attended-3plus`, `trial-converted`
  - `lead_captured_at` is within last 10 days

**Used by:** Dashboard widget #2 (Active Trials)

### 1.3 Smart List: New Members in Onboarding

- **Name:** `New Members in Onboarding`
- **Filters:**
  - Tag includes: `member-active` AND `member-onboarding`
  - `membership_start_date` is within last 30 days

**Used by:** Onboarding pipeline widget

### 1.4 Smart List: All At-Risk Members

- **Name:** `All At-Risk Members`
- **Filters:**
  - Tag includes ANY of: `risk-at-risk`, `risk-critical`
  - Tag includes: `member-active`
  - Tag does NOT include: `member-cancelled`, `member-lapsed`

**Used by:** Dashboard widget #6 (At-Risk Members) + Alerts workflow

### 1.5 Smart List: Basic Members (Upsell Targets)

- **Name:** `Basic Members (Upsell Targets)`
- **Filters:**
  - Tag includes: `tier-basic` AND `member-active`
  - `visits_last_30_days` ≥ 12
  - Tag does NOT include: `tier-premium`, `tier-vip`

**Used by:** Upsell widget cluster

### 1.6 Smart List: Lapsed Members (Win-Back Targets)

- **Name:** `Lapsed Members (Win-Back Targets)`
- **Filters:**
  - Tag includes: `member-lapsed`
  - Tag does NOT include: `member-reactivated`, `member-permanent-loss`

**Used by:** Win-back widget cluster

### 1.7 Smart List: Top Referrers (Quarterly)

- **Name:** `Top Referrers (Quarterly)`
- **Filters:**
  - `referrals_converted_count` > 0
  - Most recent `trial-converted` tag on any referred contact within last 90 days
  - Sort: descending by `referrals_converted_count`

**Used by:** Referral widget

### 1.8 Smart List: VIP Veterans

- **Name:** `VIP Veterans`
- **Filters:**
  - Tag includes: `member-vip-veteran`
  - Tag includes: `member-active`

**Used by:** VIP-attention widget

---

### 1.9 Bonus Smart Lists (built but not on dashboard front page — used in digest details)

- **Reactivations This Month:** `member-reactivated` tag added in current calendar month
- **Cancellations This Month:** `member-cancelled` tag added in current calendar month
- **Failed Payments — Pending:** `payment-failed-pending` tag present
- **5-Star Reviews This Month:** `review_star_rating` = 5 AND `review_submitted_date` in current month

---

### Verification

After building all smart lists:
1. Each smart list should show a populated count (or 0 if data hasn't accumulated yet).
2. Click into each list and confirm the filter logic produces expected contacts.
3. Bookmark each list's URL — you'll reference these when building widgets.

---

## Step 2 — Build the Live GHL Dashboard (60 min)

Navigate to **Dashboards > + Create Dashboard**.

- **Dashboard Name:** `Sunrise — Owner Headlines`
- **Layout:** 4-column grid on desktop, single-column on mobile

Full widget specs in **[assets/dashboard-spec.md](assets/dashboard-spec.md)**. Build order:

### 2.1 Row 1: The Seven Headline Numbers (top of dashboard)

Add seven **KPI Card** widgets in this order:

| # | Widget | Type | Data Source | Calculation |
|---|---|---|---|---|
| 1 | New Leads This Week | KPI Card with trend arrow | `All Hot Leads` smart list | Count, compared to previous 7-day window |
| 2 | Active Trials | KPI Card with count + sub-text | `Active Trials Needing Attention` | Count + "X need attention this week" |
| 3 | Trial → Paid (30d) | KPI Card with percentage | Custom calc (see below) | (trial-converted last 30d ÷ trial-active last 30d) × 100 |
| 4 | Active Members | KPI Card | All contacts with `member-active` | Count |
| 5 | Current MRR | KPI Card formatted as currency | Sum of `monthly_rate` where `member-active` | Dollar total |
| 6 | At-Risk Members | KPI Card with color (yellow if >5, red if >10) | `All At-Risk Members` | Count |
| 7 | Net New This Month | KPI Card with delta | (new `member-active` − new `member-cancelled` in current month) | Integer with +/- |

**Trial → Paid calculation (Widget #3):**

GHL native dashboards don't always support custom math. Two implementation paths:

- **Native:** If GHL exposes a "Formula" or "Ratio" widget type, configure: numerator = count of contacts with `trial-converted` tag added in last 30d; denominator = count of contacts with `trial-active` tag added in last 30d. Display as percentage.
- **Webhook-backed:** A small custom widget that calls an endpoint returning the precomputed percentage. Endpoint queries the GHL API on a 1-hour cache.

### 2.2 Row 2: Funnel Health Widgets

| Widget | Type | Source |
|---|---|---|
| Trial Conversion Funnel | Funnel chart | Membership Sales pipeline stages |
| Onboarding Progress | Funnel chart | Onboarding pipeline stages |
| Retention Status | Funnel chart | Retention pipeline stages |

### 2.3 Row 3: Cross-System Widgets

| Widget | Type | Source |
|---|---|---|
| Top Referrers (this quarter) | Leaderboard table | `Top Referrers (Quarterly)` smart list, top 5 by count |
| Lapsed → Reactivation | KPI pair | Reactivations This Month / Cancellations This Month |
| Reviews This Month | KPI Card | `5-Star Reviews This Month` smart list |
| Failed Payments Pending | KPI Card with alert color | `Failed Payments — Pending` smart list |

### 2.4 Row 4: Channel & Source Attribution

| Widget | Type | Source |
|---|---|---|
| Leads by Source (last 30d) | Pie chart | All contacts with `source-*` tag, grouped by tag value |
| Conversion Rate by Source | Bar chart | trial-converted ÷ leads, broken by source-* tag |

### 2.5 Publish & Set as Default

Click **Save**, then **Set as Default Dashboard** for the owner user. Every login lands here.

---

## Step 3 — Build the Weekly Digest Workflow (60 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `10a — Weekly Digest`
- **Folder:** Create folder `10 - Reporting` and put it there

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 3.1 Trigger

- **Trigger:** Scheduled — recurring
- **Schedule:** Every Monday at 7:00 AM owner-local time (`America/Chicago`)
- **Target:** Single recipient — the owner's email `{{custom_values.business.owner_email}}`

This is a **non-contact-scoped** workflow — it doesn't enroll any specific contact; it runs once a week and sends one email.

### 3.2 Action: Calculate All Metrics

GHL workflows can't natively aggregate across smart lists in a single action. Use one of these patterns:

**Approach A — Webhook to a custom endpoint:**

- **Action:** Webhook
- **URL:** `https://hooks.sunrisewellness.com/weekly-digest-metrics`
- **Method:** GET
- **Expected response:**
```json
{
  "new_leads_week": 31,
  "new_leads_week_delta": "+8",
  "active_trials": 12,
  "trials_needing_attention": ["Lin H.", "James K."],
  "trial_to_paid_rate_30d": 52,
  "trial_to_paid_rate_delta": "+4",
  "active_members": 247,
  "active_members_delta": "+3",
  "mrr": 24180,
  "mrr_delta": "+240",
  "at_risk_count": 6,
  "at_risk_critical": ["Diane K. (flagged 14d)"],
  "net_new_month": 8,
  "reactivations_week": 2,
  "failed_payments_pending": 1,
  "top_referrer_week": "Sarah M. (1 conversion)",
  "reviews_week": 3
}
```
- **Store as workflow variables**

**Approach B — Hardcoded smart-list count merges:**

GHL may expose smart-list count as a merge field `{{smart_list.all_hot_leads.count}}` or similar. If so, no webhook needed — just reference directly in email template.

Use whichever your GHL plan supports.

### 3.3 Action: Send Weekly Digest Email

- **Action:** Send Email
- **To:** `{{custom_values.business.owner_email}}`
- **From:** `{{custom_values.business.short_name}} Dashboard <dashboard@sunrisewellness.com>`
- **Subject:** `Sunrise — Week of {{week_label}} (7 numbers + this week's actions)`
- **Template:** Email "Weekly Digest" from [assets/emails.md](assets/emails.md)

The email template uses the variables from Step 3.2 to render the 7-number grid + sparklines + action items.

### 3.4 Action: Log Sent Event

- **Action:** Update Custom Value
- **Custom value:** `reporting.last_weekly_digest_sent` (new custom value — add to shared-foundation)
- **Value:** `{{now}}`

(For monitoring: if this value is more than 8 days old, the workflow isn't firing.)

### 3.5 Publish

Save and publish. Toggle the workflow ON.

---

## Step 4 — Build the Daily Summary Workflow (45 min) — OPTIONAL

For owners who want daily visibility. Same pattern as the weekly digest, smaller scope.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `10b — Daily Lead Summary`
- **Folder:** `10 - Reporting`

### 4.1 Trigger

- **Trigger:** Scheduled — recurring
- **Schedule:** Daily at 6:00 PM owner-local time

### 4.2 Actions

1. **Webhook:** Get today's activity (`/hooks/sunrisewellness.com/daily-summary`):
   - Leads in today (count + names)
   - Trials booked today (count + names)
   - Members saved today (any at-risk → healthy transitions)
   - Failed payments today
   - Cancellations today
2. **Send Email** — Template "Daily Activity Summary" from [assets/emails.md](assets/emails.md)

### 4.3 Toggle Control

This workflow should be easy to turn off if the owner finds it noisy. Build a control:

- **Custom value:** `reporting.daily_digest_enabled` (Boolean: `Yes` / `No`)
- **Trigger filter:** Custom value `reporting.daily_digest_enabled` = `Yes`

Owner can flip the toggle without touching the workflow itself.

### 4.4 Publish (initially OFF; owner enables after 1 week of weekly digests)

---

## Step 5 — Build the Critical Alerts Workflow (60 min)

This workflow fires only on critical events. Designed to NOT be noisy — each alert is high-signal.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `10c — Critical Alerts`
- **Folder:** `10 - Reporting`

Full spec in **[assets/workflow.md](assets/workflow.md)**. Build is multi-trigger (one workflow handles multiple alert types via branching).

### 5.1 Triggers (each is a separate trigger added to the same workflow)

| # | Trigger | Filter | Alert Sent |
|---|---|---|---|
| A | Tag added: `trial-active` | Wait 6 days, then check: no `trial-attended-1` tag | "Trial day-6, no booking: {{name}}" |
| B | Tag added: `risk-at-risk` OR `risk-critical` | Contact has tag `tier-vip` OR `member-vip-veteran` | "VIP at-risk: {{name}}" |
| C | Scheduled weekly | Count of `risk-at-risk` + `risk-critical` added in last 7d > 3 | "3+ at-risk members this week — pattern check" |
| D | Tag added: `payment-failed-pending` | Wait 24h, check still pending | "Failed payment not recovered: {{name}}" |
| E | Tag added: `member-cancelled` | Contact has `tier-vip` OR `monthly_rate` ≥ 200 | "High-value cancellation: {{name}}, reason {{cancel_reason}}" |

### 5.2 Actions Per Trigger (each trigger branch ends in same action set)

For each alert:
1. **Send Internal Notification** → `{{custom_values.business.owner_email}}`
2. **Email template:** Use the matching alert template from [assets/emails.md](assets/emails.md)
3. **Subject prefix:** `[ALERT]` — so they filter cleanly in inbox
4. **Add Tag** (audit): `alert-fired-{type}-{date}` (e.g., `alert-fired-vip-at-risk-2026-05-18`)

### 5.3 Publish

Save and publish. Toggle ON.

### 5.4 Snooze Mechanism

Owner needs an escape hatch — if she's on vacation, she shouldn't get alerts piling up.

- **Custom value:** `reporting.alerts_snoozed_until` (Date)
- **Trigger filter on every alert:** Skip if `today` ≤ `reporting.alerts_snoozed_until`

Owner sets the snooze via a simple internal form ("Snooze alerts until: [date]"). Workflow respects it silently.

---

## Step 6 — (Optional) API/Webhook Integration for Custom Calcs

Some metrics (Trial → Paid Rate, week-over-week deltas, cross-list aggregations) are easier to compute outside GHL.

Recommended stack:
- **GHL API:** Pull contact and tag data via REST
- **Lightweight backend:** Python Flask, Node Express, or even a Google Apps Script
- **Cache layer:** Redis or in-memory 1-hour cache (the dashboard doesn't need real-time precision)

Endpoints to build:
1. `GET /weekly-digest-metrics` — returns all numbers for the Monday digest
2. `GET /daily-summary` — returns today's activity
3. `GET /trial-to-paid-rate?days=30` — returns the rolling rate as a percentage
4. `GET /top-referrers?days=90` — returns ordered list for Workflow 08c

**Build these only if** your GHL plan can't do the calculations natively. For most studios under 500 members, GHL's smart list counts + the digest webhook for one custom percentage is enough.

---

## Test Plan

Run this complete test sequence. **Do not declare done until all five pass.**

### Test 1 — Dashboard renders all 7 KPIs

1. Log in as the owner user.
2. **Expected:** Dashboard `Sunrise — Owner Headlines` loads as default.
3. Confirm all 7 KPI cards display numbers (not empty / loading state).
4. Confirm trend arrows render where expected (week-over-week comparisons).
5. Click through each KPI → confirm it opens the underlying smart list.

### Test 2 — Weekly digest fires Monday 7 AM

1. Set system date to a Sunday evening.
2. Wait for Monday 7 AM trigger (or fast-forward via GHL's workflow test mode).
3. **Expected:** Owner email arrives at 7:05 AM with:
   - All 7 headline numbers populated
   - Week-over-week deltas with up/down arrows + color
   - 2–3 action items pulled from the smart lists
   - Specific names for at-risk members and trials needing attention
   - Formatted HTML (renders cleanly in Gmail + Outlook + iOS Mail)

### Test 3 — Alerts fire on critical triggers

Test each alert type with a test contact:

| Test | Setup | Expected |
|---|---|---|
| 3a — Trial Day-6 no booking | Create contact with `trial-active`, fast-forward 6 days, no `trial-attended-1` | Alert email arrives within 1 hour |
| 3b — VIP at-risk | Apply `tier-vip` + `risk-at-risk` to same contact | Alert email arrives immediately |
| 3c — 3+ at-risk in 7d | Tag 3 contacts with `risk-at-risk` over 5 days | Weekly check fires, alert arrives |
| 3d — Failed payment unrecovered | Apply `payment-failed-pending`, fast-forward 24h, don't recover | Alert email arrives |
| 3e — High-value cancellation | Apply `member-cancelled` to a `tier-vip` contact | Alert email arrives immediately |

### Test 4 — Smart lists update in near-real-time

1. Create a new contact, tag with `lead-new`.
2. Refresh "All Hot Leads" smart list.
3. **Expected:** Contact appears within 60 seconds.
4. Tag the same contact with `trial-active`.
5. Refresh — contact should disappear from Hot Leads, appear in "Active Trials".

### Test 5 — Snooze mechanism works

1. Set `reporting.alerts_snoozed_until` = tomorrow's date.
2. Trigger any alert condition.
3. **Expected:** No alert email sent.
4. Set `reporting.alerts_snoozed_until` = yesterday's date.
5. Trigger again.
6. **Expected:** Alert fires.

---

## Common Build Mistakes

1. **Smart list counts are empty.** The dashboard widgets show 0 because the source smart list has no matching contacts. Root cause: usually a tag misspelling (`risk-atrisk` vs `risk-at-risk`) or a filter that excludes too aggressively. Audit each smart list manually before connecting to widgets.
2. **Weekly digest fires but the body is full of empty merge fields.** The webhook returned wrong field names, or the email template references variables that don't exist. Test the webhook in isolation first (Postman or curl), then verify each merge field renders in a preview.
3. **Owner email lands in spam.** Send-from address `dashboard@sunrisewellness.com` needs valid SPF/DKIM/DMARC. If it's a transactional-pattern domain (no marketing history), warm it up by sending a test email to a personal address first, marking as "Not Spam," then to the owner address.
4. **Alerts are too noisy in the first week.** When you first turn on the alerts workflow, *every* existing at-risk member will fire a "VIP at-risk" alert if they're VIP. Mitigation: add a "first run grace period" — alerts only fire for events that occur AFTER the workflow's enabled date. Use a custom value `reporting.alerts_enabled_at` and filter on it.
5. **Dashboard widget cache is stale.** GHL dashboards cache widget data — sometimes a smart list count is 30 minutes stale. Acceptable for most metrics; problematic for "At-Risk Count" which should be near-live. If precision matters, force a refresh by adding the widget to a "manual refresh" group.
6. **Owner stops opening the digest after week 3.** This is the killer failure mode. Mitigation: keep the digest under 200 lines, lead with the 7 numbers (not narrative), make action items specific (names, not "follow up on at-risk members"). If open rate drops, send a one-line survey: "What would make this more useful?"

---

## What's Next

Once this is live and verified:

- The owner should be opening the dashboard daily and the weekly digest 100% of the time within 30 days.
- After 60 days: review which widgets actually drive action vs which are just noise. Cut anything the owner ignores.
- After 90 days: consider building an **owner-facing mobile-PWA dashboard** that's even faster than the GHL native dashboard. Out of scope here but a natural v2.
- Optional: build **monthly board-style PDF report** (auto-generated, sent to the owner's accountant or partner on the 1st of each month) for non-GHL stakeholders.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
