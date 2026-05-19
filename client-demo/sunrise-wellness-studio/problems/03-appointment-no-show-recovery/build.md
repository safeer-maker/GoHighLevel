# #03 — Build Playbook: Appointment No-Show Recovery

> Step-by-step GHL build. Estimated time: **2 hours** for a competent operator. Two workflows + calendar wiring + 6 messages.

---

## Prerequisites (from shared-foundation/)

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Engagement fields (`last_pt_session_date`, `total_pt_sessions`, `noshow_count_90d`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Tracking no-show patterns |
| Membership fields (`membership_tier`, `assigned_trainer`) | Same | Personalization |
| Tags: `apt-confirmed`, `apt-completed`, `apt-noshow`, `apt-noshow-repeat`, `apt-rescheduled` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Appointment state |
| Custom values: `business.short_name`, `business.booking_url`, `business.address_short`, `team.owner_first`, `voice.greeting_warm`, `voice.cta_book` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| At least one Calendar in GHL (PT, Intro Consult, Nutrition) | (GHL Calendars feature) | Source of appointment events |

---

## Step 1 — Configure GHL Calendars (20 min)

Skip if calendars are already in place. Otherwise:

Navigate to **Calendars > + New Calendar**.

Build at minimum these calendars (each is a separate calendar in GHL so the workflow can branch on type):

| Calendar Name | Duration | Hosted by | Capacity |
|---|---|---|---|
| `Personal Training — 60min` | 60 min | All 3 trainers (round-robin) | 1 |
| `Intro Consult — Free` | 30 min | Lead trainer | 1 |
| `Nutrition Starter Consult` | 45 min | Sam Rivera | 1 |
| `Group Class — HIIT` | 45 min | Trainer-of-record | 12 |
| `Group Class — Yoga` | 60 min | Trainer-of-record | 25 |
| `Group Class — Pilates Reformer` | 50 min | Trainer-of-record | 8 |
| `Group Class — Strength Lab` | 60 min | Trainer-of-record | 10 |

Configure each calendar:
- **Auto-mark no-show:** ON, 15 minutes after start time (if no check-in registered).
- **Allow reschedule:** ON, up to 4 hours before start.
- **Allow cancel:** ON, up to 4 hours before start.
- **Default status flow:** Booked → Confirmed → Showed | Cancelled | No-Show.

These statuses are the trigger fuel for the workflows below.

---

## Step 2 — Build Reminder Email Template (10 min)

Navigate to **Marketing > Emails > Templates > + New Template**.

Build: `03 — 48hr Appointment Reminder` from [assets/emails.md](assets/emails.md).

Confirm merge fields resolve: `{{appointment.start_time}}`, `{{appointment.trainer_name}}`, `{{appointment.calendar_name}}`, `{{appointment.reschedule_url}}`.

---

## Step 3 — Build All SMS Templates (15 min)

Navigate to **Marketing > Templates > SMS > + New Template**.

| Template Name | When Used | From [sms.md](assets/sms.md) |
|---|---|---|
| `03 — 24hr Confirm SMS` | Reminder workflow, T-24hr | Message A |
| `03 — 2hr Reminder SMS` | Reminder workflow, T-2hr | Message B |
| `03 — Post No-Show — 2hr` | Recovery workflow, T+2hr after no-show | Message C |
| `03 — Post No-Show — 72hr Final` | Recovery workflow, T+72hr after no-show | Message D |
| `03 — Rebook Confirmation` | Reply handler, when member rebooks | Message E |

---

## Step 4 — Build Reminder Cadence Workflow (30 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `03 — Appointment Reminder Cadence`
- **Folder:** Create `03 - Appointments`

Full spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 4.1 Trigger

- **Trigger:** Appointment Booked
- **Filter:** Calendar is one of: PT-60, Intro Consult, Nutrition Starter, all Group Class calendars
- **Filter:** Appointment status is `Booked` or `Confirmed`

### 4.2 Action: Set initial state

- **Add Tag:** `apt-pending`
- **Update Contact Field:** (no field update at booking — we wait until showed/no-show)

### 4.3 Action: Wait until 48 hours before start

- **Wait Until:** `appointment.start_time - 48 hours`

### 4.4 Action: Send 48hr reminder email

- **Skip if:** Appointment status is `Cancelled` OR contact has `do-not-email`
- **Send Email:** Template `03 — 48hr Appointment Reminder`

### 4.5 Action: Wait until 24 hours before start

- **Wait Until:** `appointment.start_time - 24 hours`

### 4.6 Action: Send 24hr SMS (the confirm/reschedule message)

- **Skip if:** Appointment status is `Cancelled` OR contact has `do-not-sms`
- **Send SMS:** Template `03 — 24hr Confirm SMS`

The SMS asks them to reply **C** to confirm or **R** to reschedule. See companion workflow Step 6 for handling.

### 4.7 Action: Wait until 2 hours before start

- **Wait Until:** `appointment.start_time - 2 hours`

### 4.8 Action: Send 2hr SMS

- **Skip if:** Appointment status is `Cancelled` OR contact has `do-not-sms`
- **Skip if:** Contact has tag `apt-rescheduled` for *this* appointment (they already moved it)
- **Send SMS:** Template `03 — 2hr Reminder SMS`

### 4.9 Action: Exit Workflow

The reminders are done. The appointment-status-change trigger picks up next (Workflow 2).

### 4.10 Publish

Click **Save** then **Publish**. Toggle ON.

---

## Step 5 — Build No-Show Recovery Workflow (35 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `03 — No-Show Recovery`
- **Folder:** `03 - Appointments`

### 5.1 Trigger

- **Trigger:** Appointment Status Changed
- **Filter:** New status is `No-Show`

### 5.2 Action: Stamp + tag

- **Add Tag:** `apt-noshow`
- **Update Contact Field:** `noshow_count_90d` = `noshow_count_90d + 1`

### 5.3 Action: Check for repeat no-show

- **If/Else:** `noshow_count_90d >= 2`
  - **Yes:** Add Tag `apt-noshow-repeat`, Internal Notification to Morgan ("repeat no-show: {{contact.first_name}}").
  - **No:** Continue.

### 5.4 Action: Wait 2 hours

- **Wait:** 2 hours (gives the member time to settle — sending instantly reads guilt-trippy)

### 5.5 Action: Send "we missed you" SMS

- **Skip if:** Contact has `do-not-sms` OR `apt-rescheduled` already set on this appointment.
- **Send SMS:** Template `03 — Post No-Show — 2hr` (Message C from [sms.md](assets/sms.md))

This SMS includes a **one-click rebook link** (`{{appointment.reschedule_url}}` if GHL supports per-appointment, else `{{custom_values.business.booking_url}}`).

### 5.6 Action: Wait 22 hours (= T+24hr from noshow)

- **Wait:** 22 hours

### 5.7 Action: Send rebook email (if not already rebooked)

- **If/Else:** Contact has tag `apt-rescheduled` (set by reply handler)?
  - **Yes:** Exit workflow
  - **No:** Send Email `03 — Rebook Email` from [assets/emails.md](assets/emails.md)

### 5.8 Action: Wait 48 hours (= T+72hr total)

- **Wait:** 48 hours

### 5.9 Action: Final personal SMS from Morgan

- **If/Else:** Contact has tag `apt-rescheduled`?
  - **Yes:** Exit workflow
  - **No:** Send SMS `03 — Post No-Show — 72hr Final` (Message D — written as personal SMS from Morgan)

### 5.10 Action: Exit

- Remove tag `apt-noshow` after 14 days (handled by a separate cleanup workflow) OR leave permanently as historical record. Recommend: leave the per-appointment tag, but `noshow_count_90d` is the rolling stat that matters.

### 5.11 Publish

Click **Save** then **Publish**.

---

## Step 6 — Build SMS Reply Handler Workflow (15 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `03 — Appointment Reply Handler`
- **Trigger:** Inbound SMS Received
- **Filter:** Contact has any of: `apt-pending`, `apt-noshow`

### 6.1 Action: Parse message body

- **If/Else:** Body matches "C" / "Confirm" / "yes" / "y" (case-insensitive)
  - **Yes:** Add Tag `apt-confirmed`. Send auto-reply: *"Confirmed, {{first_name}}! See you {{appointment.start_time_short}} ☀️"*
- **Else If:** Body matches "R" / "Reschedule" / "move" / "change time"
  - **Yes:** Send SMS `03 — Rebook Confirmation` (Message E — includes the rebook link). Add Tag `apt-needs-reschedule`.
- **Else If:** Body matches "cancel" / "can't make it" / "X"
  - **Yes:** Mark appointment Cancelled (via API or front-desk notification). Send reply: *"Got it — cancelled. Reply BOOK when you want to set up the next one."*
- **Else (general question):**
  - Internal notification to Morgan or front desk: *"{{contact.first_name}} replied about their appointment — check Conversations."*

### 6.2 Publish

---

## Step 7 — Build Post-Show "Thank You" Micro-Workflow (10 min) — optional but recommended

When an appointment status flips to `Showed`, fire a quick thank-you SMS (especially after PT). This builds momentum and creates the natural rebook moment.

- **Workflow Name:** `03 — Post-Appointment Thank You`
- **Trigger:** Appointment Status Changed → `Showed`
- **Filter:** Calendar is `Personal Training — 60min` OR `Intro Consult — Free`

**Actions:**

1. Add Tag `apt-completed`.
2. Update contact field: `last_pt_session_date` = today (only for PT calendar); `total_pt_sessions` += 1.
3. Wait 1 hour (let them shower, get a coffee).
4. Send SMS: *"Hey {{first_name}}, great work today 👏 {{contact.assigned_trainer}} said you crushed it. Want to lock in next week's slot? Tap here: {{custom_values.business.booking_url}}"*

This is the highest-rebook-rate touchpoint in the whole system. Members are still in the endorphin high.

---

## Test Plan

### Test 1 — Reminder cadence (full path)

1. Book a test appointment on the PT-60 calendar for 50 hours from now.
2. **Expected at T-48hr:** 48hr reminder email arrives.
3. **Expected at T-24hr:** 24hr confirm SMS arrives.
4. **Expected at T-2hr:** 2hr reminder SMS arrives.
5. (For testing, manually shift wait durations to minutes.)

### Test 2 — Confirm via reply

1. Book a test appointment. At T-24hr SMS reply with "C".
2. **Expected:** Tag `apt-confirmed` applied. Auto-reply received.

### Test 3 — Reschedule via reply

1. Book test appt. At T-24hr SMS reply with "R".
2. **Expected:** Rebook SMS with link arrives. Tag `apt-needs-reschedule` applied.

### Test 4 — No-show recovery (single)

1. Book a test appt. Let the time pass without checking in.
2. After 15 min, auto-no-show fires (or manually mark).
3. **Expected at T+2hr:** Post-noshow SMS arrives ("we missed you").
4. **Expected at T+24hr:** Rebook email arrives.
5. **Expected at T+72hr:** Final personal SMS from Morgan arrives.
6. `noshow_count_90d` = 1.

### Test 5 — Repeat no-show

1. Create a test contact, manually set `noshow_count_90d` = 1.
2. Book + no-show another appointment.
3. **Expected:** `noshow_count_90d` = 2. Tag `apt-noshow-repeat` applied. Internal notification to Morgan fires.

### Test 6 — Rebook stops recovery cadence

1. Book + no-show. At T+2hr SMS, click the rebook link, book a new appt.
2. **Expected:** Tag `apt-rescheduled` applied. T+24hr email does NOT fire. T+72hr SMS does NOT fire.

### Test 7 — Post-show thank you

1. Book PT-60 appt. Mark `Showed`.
2. **Expected at T+1hr:** Thank-you SMS arrives with rebook link.

---

## Common Build Mistakes

1. **Reminder fires for cancelled appointments.** Forgot the "Appointment status is not Cancelled" filter on each reminder send. Add it.
2. **`noshow_count_90d` keeps growing forever.** Field doesn't auto-reset. Build a nightly cleanup workflow: for any contact, decrement `noshow_count_90d` by 1 each time a no-show is > 90 days old. (Or run a weekly recompute from appointment history.)
3. **24hr SMS goes out at 3 AM.** GHL doesn't auto-respect quiet hours for appointment-time-relative sends. Add a check: if T-24hr falls between 9 PM and 8 AM contact-local, send at 8 AM instead.
4. **Rebook link doesn't pre-fill member info.** Use `{{appointment.reschedule_url}}` if GHL exposes it; otherwise use the contact's deep-link booking URL.
5. **Group-class no-shows trigger PT-style recovery.** Build the no-show recovery filter to either include or exclude group classes deliberately — over-messaging on group classes is more annoying than valuable; PT/consult messaging is the high-value version. Recommend: exclude group classes from full T+24hr/T+72hr cadence, send only the T+2hr soft note.
6. **Trainer notified twice.** If the auto-no-show fires AND the trainer manually marks, the workflow may double-fire. Use the "Status changed to No-Show" trigger with a debounce: skip if `apt-noshow` tag was added in last 30 min.

---

## What's Next

Once this is live:

- No-show data feeds **[#05 Retention](../05-retention-and-churn-prevention/build.md)** — 2+ no-shows in 30 days is an at-risk signal.
- Appointment volume and no-show rate appear on **[#10 Owner Dashboard](../10-owner-reporting-and-visibility/build.md)**.
- Onboarding workflow ([#04](../04-new-member-onboarding/build.md)) checks for no-shows on the Day-7 first PT session and adjusts its Day-14 messaging accordingly.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
