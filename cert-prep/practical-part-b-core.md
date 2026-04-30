# GHL Admin Cert — Part B Core Practical

> **Purpose:** drill the 13 confirmed Part B tasks until you can build them in under 30 minutes on camera.
> **Not in scope:** SMS sending, A2P/telephony, payments, webchat, marketing campaigns, reputation management, round-robin calendars. Those live in [practical-business-extended.md](practical-business-extended.md) for post-cert practice.

---

## Why this file exists

Part B is a 60-minute live proctored build. The proctor watches you create a sub-account from scratch and complete a sequence of small tasks. They are checking that you can **navigate the platform fast** and that **each piece you build connects to the next** — not that you can build a whole business.

This file gives you:
- One **building-block contract** where every asset is consumed by the next step (no orphans)
- Two scenarios so you drill the build twice with different names — second one tests memory, not muscle
- A 30-minute timed drill at the end of each scenario

Read [exam-research-findings.md](exam-research-findings.md) for the confirmed task list and pitfalls before starting.

---

## The 13 Confirmed Part B Tasks

Every section in this file maps to one or more of these. If a task isn't on this list, it's not in this file.

| # | Task | Where it appears |
|---|---|---|
| 1 | Create a sub-account from Agency dashboard | Step 0 |
| 2 | Switch between Agency and Sub-Account views | Throughout |
| 3 | Set up business profile + custom values | Step 1 |
| 4 | Create custom fields | Step 2 |
| 5 | Add a contact + apply a tag | Step 3 |
| 6 | Create a Smart List | Step 3 |
| 7 | Create an email template with a merge field | Step 4 |
| 8 | Create a calendar + connect Zoom/Google Meet | Step 5 ← #1 failure point |
| 9 | Create a pipeline + add an opportunity | Step 6 |
| 10 | Create a trigger link + apply a tag | Step 7 |
| 11 | Build a form + embed in a 2-step funnel | Step 8 |
| 12 | Build + **Publish** a workflow | Step 9 ← #1 failure point |
| 13 | Create a snapshot + load it | Step 10 |

---

## Scenario 1 — Doctor Bob Family Dental

> Single sub-account build. ~60 minutes first time. Target: under 30 minutes by the third repetition.

### S1.0 Data Dictionary (the contract)

Every asset below has a **producer** (where it gets created) and a **consumer** (where it gets used). Nothing in this build is decorative.

**Custom Values (3):**
| Name | Value | Created In | Consumed By |
|---|---|---|---|
| `business_name` | Doctor Bob Family Dental | Step 1 | Email template (Step 4), Funnel hero (Step 8) |
| `business_phone` | +14085550100 | Step 1 | Email template footer (Step 4) |
| `book_link` | (paste calendar URL after Step 5) | Step 1 placeholder → Step 5 real value | Email template CTA (Step 4) |

**Custom Fields (3):**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `patient_type` | Dropdown: New Patient, Returning, Emergency | Form (Step 8) sets to "New Patient" | Workflow if/else (Step 9) |
| `last_visit_date` | Date | Manual / CSV later | Smart List filter (Step 3) |
| `preferred_dentist` | Dropdown: Dr. Bob, Dr. Sarah | Form (Step 8) | Workflow internal notification (Step 9) |

**Tags (3):**
| Tag | Applied By | Read By |
|---|---|---|
| `new-patient-inquiry` | Form submit (Step 8) | Workflow trigger (Step 9) |
| `interested-whitening` | Trigger link click (Step 7) | Smart List filter |
| `appointment-scheduled` | Workflow on calendar booking (post-cert add) | (workflow if/else — optional) |

**Email Template (1):** `Bob - New Patient Welcome`
- Subject uses `business_name`
- Body uses `contact.first_name`, `book_link` (CTA), `business_phone` (footer)
- Embeds 1 trigger link: `interested-whitening`

**Trigger Link (1):** `interested-whitening` → applies tag `interested-whitening`

**Calendar (1):** `Bob - General Checkup` — Basic, 30min, Mon-Fri 9AM-5PM, **Zoom connected**

**Pipeline (1):** `Bob - Patient Pipeline` — 3 stages: New Inquiry → Consultation Scheduled → Treatment Completed

**Form (1):** `Bob - New Patient Inquiry`
- Fields: First Name, Last Name, Email, Phone, Preferred Dentist (custom field), Reason for Visit (dropdown — drives tag logic)
- Submit actions: apply tag `new-patient-inquiry`, set `patient_type` = "New Patient"
- (Opportunity is created by the workflow, NOT by the form — see fix note below)

**Funnel (1):** `Bob - Free Exam Funnel`
- Step 1: Landing page — embeds form, hero uses `business_name`
- Step 2: Thank You — embeds calendar widget

**Workflow (1):** `Bob - New Patient Onboarding`
- **Trigger:** Form Submitted → `Bob - New Patient Inquiry`
- **Actions:**
  1. Create Opportunity in `Bob - Patient Pipeline` at stage "New Inquiry", value 0
  2. Send Email: `Bob - New Patient Welcome`
  3. If/Else: `preferred_dentist` = "Dr. Bob" → Internal Notification "Assigned to Dr. Bob"; else "Assigned to Dr. Sarah"
- **Status:** Published (this is the exam's #1 missed step)

**Smart List (1):** "New Patient Inquiries This Week" — filter: tag `new-patient-inquiry` AND date added in last 7 days

> **Fix note — why the workflow creates the opportunity, not the form:** GHL forms have submit actions for tags, custom fields, redirects, and notifications — but **not** "create opportunity." The workflow does it. This is the single most common build mistake.

---

### S1.1 Step 0 — Create the sub-account (Task 1)

**You are in Agency view.**
1. Left nav → **Accounts**
2. Top-right → **+ New Sub-Account**
3. Fill: Name = `Doctor Bob Family Dental`, Address = `123 Main St, Springfield`, Timezone = your local, Phone = `+14085550100`, Email = `bob@drbobdental.com`
4. Leave "Snapshot to Load" blank
5. Save
6. Click into the new sub-account — top-left should now show "Doctor Bob Family Dental"

✅ **Checkpoint:** top-left shows the sub-account name, not your agency name. If wrong, you'll do every later step in the wrong place.

---

### S1.2 Step 1 — Business Profile + Custom Values (Task 3)

**You are in the sub-account.**

**Business Profile:** Settings → Business Info — fill name, address, phone, email, hours (Mon-Fri 9AM-5PM), category (Healthcare/Dental), timezone.

**Custom Values:** Settings → Custom Values → + Add — create the 3 from the dictionary. Use **placeholder text** for `book_link` (e.g. `https://placeholder.com`) — you'll update it in Step 5 once the calendar exists.

✅ **Checkpoint:** 3 custom values listed.

---

### S1.3 Step 2 — Custom Fields (Task 4)

Settings → Custom Fields → + Add Field. Create the 3 from the dictionary. Use exact lowercase-underscore keys (`patient_type`, `last_visit_date`, `preferred_dentist`) — this matters for the form mapping in Step 8.

✅ **Checkpoint:** 3 custom fields listed under Contact object.

---

### S1.4 Step 3 — Contact + Tag + Smart List (Tasks 5, 6)

**Add a contact:**
1. Contacts → + New Contact
2. Name: `TEST Patient`, Email: `test@yopmail.com`, Phone: your real phone
3. Add tag `new-patient-inquiry`
4. Save

**Build the Smart List:**
1. Contacts → Smart Lists tab → + New
2. Name: `New Patient Inquiries This Week`
3. Filter: Tag = `new-patient-inquiry` AND Date Added in last 7 days
4. Save → verify TEST Patient appears

✅ **Checkpoint:** TEST Patient visible in Smart List.

---

### S1.5 Step 4 — Email Template (Task 7)

Marketing → Templates → Email → + New Email Template.

- Name: `Bob - New Patient Welcome`
- Subject: `Welcome to {{custom_values.business_name}}`
- Body: greeting using `{{contact.first_name}}`, button labelled "Book Your Visit" linked to `{{custom_values.book_link}}`, footer with `{{custom_values.business_phone}}`
- Save

> **Merge syntax:** custom values use `{{custom_values.<key>}}`. Custom fields use `{{contact.<field_key>}}`. The exam will not test obscure merge syntax — the dropdown picker in the editor inserts the right format.

✅ **Checkpoint:** template saved, you can re-open and see the merge tokens.

---

### S1.6 Step 5 — Calendar + Zoom (Task 8) ← drill this

> **This is the #1 confirmed Part B failure point.** Practice it standalone 5 times before moving on.

1. Calendars → + Create Calendar → **Service Calendar** type (sometimes labelled "Basic")
2. Name: `Bob - General Checkup`
3. Duration: 30 min, Buffer: 5 min after
4. Availability: Mon-Fri 9AM-5PM
5. **Connections** tab → Connect Zoom (or Google Meet) → authenticate in popup
6. Set Meeting Location: **Zoom** (or Google Meet)
7. Save

**Test it:**
1. Copy the public booking URL from the calendar's settings
2. Paste in browser → book a test slot using your TEST contact email
3. Verify confirmation email contains the Zoom/Meet link
4. Verify the calendar event in your dashboard shows the link

**Now update `book_link`:** Settings → Custom Values → edit `book_link` → paste the public booking URL → save.

✅ **Checkpoint:** test booking confirmed with meeting link, `book_link` custom value points at real URL.

---

### S1.7 Step 6 — Pipeline + Opportunity (Task 9)

1. Opportunities → Pipelines → + New Pipeline
2. Name: `Bob - Patient Pipeline`
3. Stages: New Inquiry, Consultation Scheduled, Treatment Completed
4. Save

**Add an opportunity:**
1. Opportunities → + Add Opportunity
2. Pipeline: Bob - Patient Pipeline, Stage: New Inquiry
3. Contact: TEST Patient, Value: $0
4. Save

✅ **Checkpoint:** opportunity visible in "New Inquiry" column.

---

### S1.8 Step 7 — Trigger Link (Task 10)

1. Marketing → Trigger Links → + New
2. Name: `interested-whitening`
3. Redirect URL: `https://drbobdental.com/whitening` (or any real URL)
4. **Action:** Apply Tag → `interested-whitening`
5. Save

**Embed in your email template:**
1. Open `Bob - New Patient Welcome` template
2. Add a line "Curious about teeth whitening? [Tell us]" — link the bracketed text to the trigger link
3. Save

✅ **Checkpoint:** trigger link exists, email template contains it. Click test: open trigger link URL → check TEST contact's tags → `interested-whitening` should appear.

---

### S1.9 Step 8 — Form + Funnel (Task 11)

**Form:**
1. Sites → Forms → + New Form
2. Name: `Bob - New Patient Inquiry`
3. Fields: First Name (req), Last Name (req), Email (req), Phone (req), Preferred Dentist (dropdown → map to custom field `preferred_dentist`), Reason for Visit (dropdown: Routine, Whitening, Emergency)
4. Form Settings → Actions on Submit:
   - Apply tag: `new-patient-inquiry`
   - Set custom field: `patient_type` = "New Patient"
5. Save

> **Do NOT** add "Create Opportunity" here — that's not a real form action. The workflow handles it.

**Funnel:**
1. Sites → Funnels → + New Funnel
2. Name: `Bob - Free Exam Funnel`
3. Step 1 — Landing Page:
   - Headline element using `{{custom_values.business_name}}`
   - Drag Form element → select `Bob - New Patient Inquiry`
   - Set "After Submit" = Go to next funnel step
4. Step 2 — Thank You Page:
   - Headline: "You're in — pick a time"
   - Drag Calendar element → select `Bob - General Checkup`
5. Publish funnel (toggle top-right)

**Test:** open landing page URL → submit form as TEST → land on Thank You → see calendar.

✅ **Checkpoint:** form submission visible on TEST contact, tag and custom field set, calendar embedded on Thank You.

---

### S1.10 Step 9 — Workflow (Task 12) ← drill the Publish toggle

Automation → Workflows → + Create Workflow → Start from scratch.

- Name: `Bob - New Patient Onboarding`
- **Trigger:** Form Submitted → `Bob - New Patient Inquiry`
- **Action 1:** Create Opportunity → Pipeline: `Bob - Patient Pipeline`, Stage: New Inquiry, Value: 0, Name: `{{contact.first_name}} {{contact.last_name}}`
- **Action 2:** Send Email → select template `Bob - New Patient Welcome`
- **Action 3:** If/Else condition → Custom Field `preferred_dentist` = "Dr. Bob"
  - True branch: Internal Notification → To: Assigned User → Subject "New patient — assigned to Dr. Bob" → Body `{{contact.first_name}} {{contact.last_name}} just signed up`
  - False branch: Internal Notification → "New patient — assigned to Dr. Sarah" with same body
- Save

**The critical step everyone forgets:** top-right toggle **Draft → Publish**. Confirm it shows "Published" not "Saved" or "Draft."

**Test:**
1. Submit the funnel form as a fresh test contact
2. Verify within 60 seconds:
   - Opportunity appears in pipeline
   - TEST contact receives email
   - Internal notification appears (bell icon top-right)

✅ **Checkpoint:** workflow status = **Published**, all 3 actions verified.

---

### S1.11 Step 10 — Snapshot Create + Load (Task 13)

**Switch to Agency view** (top-left dropdown or click your agency name).

**Create:**
1. Snapshots → + New Snapshot
2. Source: `Doctor Bob Family Dental`
3. Name: `Snapshot - Doctor Bob - v1`
4. Save → wait for "Snapshot Created" confirmation

**Load:**
1. Snapshots → find `Snapshot - Doctor Bob - v1` → ⋮ menu → Push to Account
2. Target: pick a different blank sub-account (create one with no data if needed)
3. Mode: Add/Merge
4. Click Load → wait for confirmation
5. Enter the target sub-account → verify pipeline, calendar, workflow, form all appeared

✅ **Checkpoint:** target sub-account contains the assets.

---

### S1.12 Scenario 1 — Definition of Done

- [ ] Sub-account created from Agency view
- [ ] 3 custom values, 3 custom fields, 3 tags
- [ ] TEST contact + Smart List
- [ ] 1 email template with merge fields + embedded trigger link
- [ ] 1 calendar with Zoom/Meet, test booking has meeting link
- [ ] `book_link` custom value updated to real URL
- [ ] 1 pipeline, 1 opportunity
- [ ] 1 trigger link, embedded + tested
- [ ] 1 form + 2-step funnel published
- [ ] 1 workflow with **Published** toggle on, all actions verified
- [ ] 1 snapshot created, loaded into another sub-account

---

## Scenario 2 — Apex Plumbing Services

> Different industry on purpose. If you only know dental field names, you'll fumble. Build this from scratch in a fresh sub-account using the same 13-task sequence.

### S2.0 Data Dictionary

**Custom Values (3):**
| Name | Value | Consumed By |
|---|---|---|
| `business_name` | Apex Plumbing Services | Email template, Funnel hero |
| `business_phone` | +14085550200 | Email footer |
| `book_link` | (calendar URL after Step 5) | Email CTA |

**Custom Fields (3):**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `service_type` | Dropdown: Emergency, Repair, Installation, Inspection | Form / manual | Workflow if/else routing |
| `property_type` | Dropdown: Residential, Commercial | Form / manual | Smart List filter |
| `urgency` | Dropdown: Same Day, Within 48h, Scheduled | Form | Workflow internal notification body |

**Tags (3):**
| Tag | Applied By | Read By |
|---|---|---|
| `new-service-request` | Form submit | Workflow trigger |
| `emergency-call` | Form (when `urgency` = Same Day) | Smart List, internal notification flag |
| `quote-requested` | Trigger link in email | Smart List |

**Email Template (1):** `Apex - Service Request Received`
- Subject: `{{custom_values.business_name}} — we got your request`
- Body: `{{contact.first_name}}` greeting, `{{custom_values.book_link}}` CTA, `{{custom_values.business_phone}}` footer
- Embeds trigger link: `quote-requested`

**Trigger Link (1):** `quote-requested` → applies `quote-requested`

**Calendar (1):** `Apex - Site Visit` — Basic, 60min, Mon-Sat 7AM-6PM, **Google Meet connected** (use Meet here so you've practiced both Zoom and Meet across the two scenarios)

**Pipeline (1):** `Apex - Service Pipeline` — 3 stages: Request Received → Quoted → Job Completed

**Form (1):** `Apex - Service Request`
- Fields: First Name, Last Name, Email, Phone, Service Type (→ `service_type`), Property Type (→ `property_type`), Urgency (→ `urgency`)
- Submit actions: tag `new-service-request`, conditional tag `emergency-call` if `urgency` = Same Day

**Funnel (1):** `Apex - Service Booking Funnel`
- Step 1: Landing — form embedded, hero uses `business_name`
- Step 2: Thank You — calendar embedded

**Workflow (1):** `Apex - Service Intake`
- Trigger: Form Submitted → `Apex - Service Request`
- Actions:
  1. Create Opportunity in `Apex - Service Pipeline` at "Request Received", value 0
  2. Send Email: `Apex - Service Request Received`
  3. If/Else: `urgency` = "Same Day" → Internal Notification "🚨 EMERGENCY — call back within 1 hour"; else "Standard request — respond within 24h"
- **Published**

**Smart List (1):** "Emergency Calls This Week" — tag `emergency-call` AND date added in last 7 days

---

### S2.1 Build Order (compressed — same 10 steps as Scenario 1)

Don't re-read the detailed steps. Use this checklist:

1. [ ] Agency view → create sub-account `Apex Plumbing Services`
2. [ ] Business profile + 3 custom values (`book_link` placeholder)
3. [ ] 3 custom fields with exact keys
4. [ ] TEST contact + Smart List "Emergency Calls This Week"
5. [ ] Email template `Apex - Service Request Received` with merge fields + trigger link slot
6. [ ] Calendar `Apex - Site Visit` + **Google Meet** connected + test booking has Meet link
7. [ ] Update `book_link` custom value to real calendar URL
8. [ ] Pipeline `Apex - Service Pipeline` + 1 opportunity
9. [ ] Trigger link `quote-requested` + embedded in email template + tested
10. [ ] Form `Apex - Service Request` (with conditional tag for emergency) + Funnel `Apex - Service Booking Funnel` (2 steps, published)
11. [ ] Workflow `Apex - Service Intake` (form trigger, 3 actions, **Published**)
12. [ ] Test full flow: submit form as Same Day urgency → opportunity created, email sent, emergency internal notification appears
13. [ ] Snapshot `Snapshot - Apex - v1` + load into a blank sub-account

If you have to look back at Scenario 1 details for any step, that step needs more reps before exam day.

---

## 30-Minute Timed Drill

> Use a **fresh blank sub-account** each time. Don't pre-create anything. Start the timer. Build a stripped Scenario 1 in 30 minutes.

| Step | Task | Target time |
|---|---|---|
| 1 | Create sub-account from Agency | 2 min |
| 2 | Business profile + 2 custom values | 3 min |
| 3 | 1 custom field | 1 min |
| 4 | 1 contact + apply 1 tag | 1 min |
| 5 | 1 Smart List | 2 min |
| 6 | 1 email template with 1 merge field | 3 min |
| 7 | 1 calendar + Zoom/Meet + test booking | 7 min |
| 8 | 1 trigger link → applies a tag | 2 min |
| 9 | 1 pipeline (3 stages) + 1 opportunity | 3 min |
| 10 | 1 form (4 fields) + 2-step funnel + publish | 4 min |
| 11 | 1 workflow: form-submit trigger → email → internal notification → **Published** | 3 min |
| 12 | Snapshot from Agency view | 2 min |
| | **Total** | **33 min** |

| Your time | Diagnosis |
|---|---|
| < 25 min | Exam-ready |
| 25-35 min | Borderline — drill the slowest step in isolation 5x |
| > 35 min | Not ready — go back to the navigation drills in [agency-navigation-guide.md](agency-navigation-guide.md) |

---

## The 5 Things That Fail Part B

From [exam-research-findings.md](exam-research-findings.md). If your build works but you fail, it's probably one of these.

1. **Workflow not Published** — built correctly, never toggled from Draft. Always check the toggle before saying "done."
2. **Calendar/Zoom integration broken** — connection fails silently, confirmation email has no meeting link. Always test with a real booking.
3. **Wrong account level** — building in Agency view what should be in the sub-account, or vice versa. Glance at the top-left before every action.
4. **Time pressure** — knew it cold in practice, took 3× longer on camera. Only fix is timed drilling, not more reading.
5. **Form trying to create an opportunity** — silently doesn't work, no error. Workflows create opportunities, not forms.

---

## What's Intentionally NOT Here

These are **real GHL skills** but **not Part B exam tasks** — practice them after you pass:

| Topic | Why excluded | Where to practice |
|---|---|---|
| SMS templates + sending | Requires A2P 10DLC approval; in A2P Compliance badge, not base cert | Extended file |
| Round-robin calendars | Real-world skill, not in confirmed task list | Extended file |
| Payments / invoices / coupons | Lower-priority; rarely in confirmed tasks | Extended file |
| Webchat widget | Not in confirmed task list | Extended file |
| Marketing campaigns | Not in confirmed task list | Extended file |
| Reputation / review responses | Not in confirmed task list | Extended file |
| 5+ workflows in one build | One workflow with form-trigger covers the task | Extended file |
| Custom field folders | Creating fields is tested; organizing them is decoration | Extended file |
| Sub-account user permission tables | "Add a user" might come up; full permissions matrix won't | Extended file |

If a real exam day task asks for any of these, the proctor will accept a basic version. Don't pre-build complexity that isn't asked for.

---

## How To Use This File

1. **First pass (60-90 min):** read Scenario 1 with the platform open, build along, don't time yourself
2. **Second pass (45 min):** rebuild Scenario 1 in a new sub-account, glance at the file only when stuck
3. **Third pass (timed):** Scenario 2 against the 30-minute drill table — different industry, different field names, no peeking
4. **Fourth pass (timed):** alternate Scenario 1 / Scenario 2 in fresh sub-accounts until both are under 30 min consistently
5. **Day before exam:** one timed Scenario 2 build, then sleep

You're ready when you can do Scenario 2 in under 30 minutes without consulting the dictionary.
