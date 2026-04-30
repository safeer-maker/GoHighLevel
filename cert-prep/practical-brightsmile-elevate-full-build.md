# GHL Admin Cert — Part B Practical
## BrightSmile Dental + Elevate Digital Agency — Coherent Build

> **You have passed Part A.** This practical targets **Part B only** — the 1-hour live proctored session where you build a sub-account from scratch on screen.
>
> Telephony (A2P 10DLC, LC Phone, Twilio) is in the **A2P Compliance badge** — not tested in Part B.

---

## How This Practical Is Designed (read first)

Previous versions of this file defined custom values, custom fields, templates, and tags in isolation — many were never consumed by anything downstream. The result was a checklist of orphan assets, not a system. This rewrite fixes that.

**The contract:**
1. Each business section opens with a **Data Dictionary** (A0 / B0) listing every named asset
2. Each Day section ONLY uses assets from the dictionary
3. Every asset documents what creates it AND what consumes it
4. There are no orphans — if you find one, it's a bug

**Why this matters for Part B:** the proctored exam evaluates whether your build *works as a system*. A form that populates a custom field that's read by a workflow that fires a template — that integration is exactly what the proctor checks. A pile of disconnected assets fails even if every individual asset looks correct.

---

## Part B Task Coverage Map

| Confirmed Part B Task | Where Drilled |
|---|---|
| Create sub-account from Agency dashboard | Section 0.4 |
| Switch between Agency and Sub-Account views | Section 0 + every Agency Step |
| Set up business profile + custom values | A1 / B1 |
| Create custom fields with folders | A2 / B2 |
| Add a contact + apply tag | A2 / B2 (CSV import) + Part B drill |
| Build a Smart List | A2 / B2 |
| Create SMS + Email templates with merge fields | A3 / B3 |
| Create a calendar + connect Zoom/Google Meet | A4 / B4 (drilled twice) |
| Create a pipeline + add an opportunity | A5 / B5 |
| Create trigger links + apply tags | A7 / B7 |
| Build a form mapped to custom fields | A8 / B8 |
| Build a 2-step funnel embedding form + calendar | A8 / B8 |
| Build + **Publish** a workflow | A9 / B9 (5 workflows each) |
| Create a snapshot from Agency view | After A3, A5, A7, A9, A10 (same for B) |
| Load a snapshot into a sub-account | After A9 + B9 |

Sections marked **Lower Part B priority** can be skimmed during cram time.

---

## Time Estimates

| Build | First Time | After Drilling |
|---|---|---|
| BrightSmile full (Days 1–10) | 6–8 hrs | 2.5–3.5 hrs |
| Elevate full (Days 1–10) | 4–6 hrs | 2–3 hrs |
| Part B Drill (end of each section) | < 25 min target | < 25 min must hit |

---

## Global Naming + Hygiene Rules

- **BrightSmile assets:** `BrightSmile - <name>`
- **Elevate assets:** `Elevate - <name>`
- **Tags:** lowercase + hyphens, lifecycle convention (see A0/B0 tag tables)
- Keep one permanent test contact per sub-account: `TEST - Do Not Delete`
- Sample CSVs are in `cert-prep/sample-data/` — imported during Day 2

---

## Section 0 — Agency Account: Full Walkthrough

> **Do this entire section before touching Section A or B.** Everything in GHL starts at the agency level. Part B tests BOTH agency-level AND sub-account-level navigation. Mixing them up under pressure is the #4 reason people fail.

### 0.1 Understanding the Two Levels

| | Agency Level | Sub-Account Level |
|---|---|---|
| **What it is** | Your management dashboard | One client's workspace |
| **Who works here** | You (the agency admin) | The client's staff |
| **Left nav shows** | Accounts, Snapshots, SaaS tools | Contacts, Workflows, Calendars, etc. |
| **Settings icon opens** | Agency-wide config | That client's business settings |
| **URL pattern** | `.../agency/...` | `.../location/...` |

**The critical habit:** glance at the top-left corner before clicking. It shows which level you are in.

### 0.2 Agency Dashboard Tour

| Left Nav Item | What It Is |
|---|---|
| **Dashboard** | Summary stats across all sub-accounts |
| **Accounts** | List of all sub-accounts — create / manage them here |
| **Snapshots** | Saved configuration packages |
| **Templates** | Agency-level shared templates (optional) |
| **Media** | Agency-level media library |
| **Settings** (gear) | Agency-wide settings |
| **SaaS Configurator** | SaaS pricing/rebilling (not Part B relevant) |

**Do this now:** Find Accounts list → find Snapshots → open Agency Settings → Company Info.

### 0.3 Agency Settings — What's Inside

| Section | What You'll Find |
|---|---|
| **Company** | Agency name, address, logo, timezone |
| **Team** | Agency-level staff (your employees) |
| **Email Services** | Default email sending |
| **Integrations** | Stripe, Facebook, etc. at agency level |
| **API Keys** | Developer access |
| **White Label** | Custom domain/branding |

**Agency Team vs Sub-Account Team:** Agency Team = your staff (access all sub-accounts); Sub-Account Team = client staff (one sub-account only). When you create a Dentist or Front Desk user in A1, you do that **inside the sub-account**, not here.

### 0.4 Creating Sub-Accounts

From **Agency view**:
1. Click **Accounts** in left sidebar
2. Click **+ New Sub-Account** (top-right)
3. Fill in: Business Name, Address, Timezone, Phone, Email
4. Leave "Snapshot to Load" blank
5. Click **Save**
6. Sub-account appears in list

**Do this for both:**
- [ ] BrightSmile Dental Clinic created
- [ ] Elevate Digital Agency created
- [ ] Both appear in Accounts list

### 0.5 Snapshots — Create + Load

**Create:**
1. Agency view → **Snapshots** → **+ New Snapshot**
2. Source: select sub-account
3. Select assets to include (all = full snapshot)
4. Name: `Snapshot - <Business> - v<N> <Description>`
5. Save

**Load:**
1. Agency view → **Snapshots** → find snapshot → **⋮ menu → Push to Account**
2. Target: select sub-account
3. Merge: choose **Add/Merge** (preserves existing) or **Replace**
4. Click Load
5. Enter target sub-account → verify assets appeared

**Practice drill before starting Section A:** create a snapshot from any sub-account → load it into a different one → verify. Target: < 3 minutes total.

### 0.6 Navigation Speed Drill

Time yourself, < 30 seconds per step, do 5 reps:
1. Agency Settings → Company
2. Enter BrightSmile → Sub-Account Settings → Business Info
3. Return to Agency view → Snapshots
4. Enter Elevate → Workflows
5. Return to Agency view → Accounts list

### 0.7 What Happens at Each Level (reference)

| Task | Level | Where |
|---|---|---|
| Create sub-account | Agency | Accounts → + New |
| Create/load snapshot | Agency | Snapshots |
| Sub-account business profile | Sub-account | Settings → Business Info |
| Custom values | Sub-account | Settings → Custom Values |
| Sub-account team/users | Sub-account | Settings → Team |
| Contacts, Workflows, Calendars, Funnels, Pipelines | Sub-account | corresponding left-nav |

---
---

# Section A — BrightSmile Dental Clinic

> Build everything inside the **BrightSmile Dental Clinic** sub-account.
> Section A0 below is the contract — Days A1–A10 only use assets defined in A0.

---

## A0 — Data Dictionary (the contract)

### A0.1 Custom Values (8 — all consumed)

| Name | Value | Created In | Consumed By |
|---|---|---|---|
| `business_name` | BrightSmile Dental Clinic | A1 | All templates (A3), Funnel headline (A8), Calendar confirmations (A4), Webchat (A3) |
| `business_phone` | +14085550100 | A1 | Post-Procedure SMS (A3), Welcome Email (A3), Webchat after-hours (A3) |
| `business_email` | smile@brightsmile.com | A1 | All email footers (A3, A7), Welcome Email signature (A3) |
| `business_address` | 456 Smile Avenue, Springfield | A1 | Welcome Email body (A3), Appointment Confirmation Email (A3) |
| `business_hours` | Mon-Thu 8AM-5PM, Fri 8AM-2PM | A1 | Welcome Email (A3), Webchat after-hours (A3), Funnel landing (A8) |
| `book_link` | (paste General Checkup calendar URL after A4) | A4 | Recall SMS (A3), No-Show Recovery SMS (A3), Welcome Email CTA (A3) |
| `review_link` | https://g.page/r/brightsmile/review | A1 | Post-Visit Summary Email (A3), Post-Procedure SMS (A3) |
| `offer_new_patient` | Free Dental Exam & X-Rays for new patients | A1 | Funnel landing hero (A8), Welcome Email subject (A3) |

### A0.2 Custom Fields (14 — every CSV column wired to a consumer)

The CSV at `cert-prep/sample-data/brightsmile-patients.csv` populates these. Each field has at least one downstream consumer.

**Folder: Patient Info**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `patient_type` | Dropdown: New Patient, Returning, Referred, Emergency | Form (A8) sets to "New Patient" / CSV / manual | Workflow 1 conditional branch (A9) |
| `last_visit_date` | Date | CSV / Workflow 4 sets to today on Showed | Smart List "Overdue for Cleaning" (A2), Workflow 5 Recall trigger (A9) |
| `next_appointment_type` | Dropdown: Cleaning, Filling, Crown, Whitening, Veneer Consultation, Orthodontic Check, Emergency | CSV / manual | Internal notification in Workflow 2 (A9) — staff sees what kind of visit |
| `preferred_dentist` | Dropdown: Dr. Sarah Kim, Dr. James Okafor | Form (A8) / CSV / manual | Smart List "Dr. Kim's Patients" (A2), Workflow 1 internal-notification routing (A9) |
| `visit_frequency` | Dropdown: Every 6 Months, Quarterly, As Needed | CSV / manual | Smart List "Overdue for Cleaning" filter combine with `last_visit_date` (A2) |

**Folder: Insurance & Billing**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `insurance_provider` | Dropdown: Aetna, BlueCross, Cigna, Delta Dental, MetLife, United, Self-Pay, Other | Form (A8) / CSV | Smart List "Self-Pay Patients" (A2), Workflow 1 internal-notification body (A9) |
| `insurance_id` | Text | CSV / manual | Reference field — appears on contact card during appointment, included in Workflow 2 internal notification (A9) |
| `coverage_level` | Dropdown: Basic, Standard, Premium, None | CSV / manual | Reference field on contact card (used by front desk for treatment authorization) |
| `payment_plan_active` | Checkbox | CSV / manual | Smart List "Payment Plans Active" (A2) |
| `outstanding_balance` | Number | CSV / manual update | Smart List "Outstanding Balance" (A2), Workflow 2 internal notification flags > $100 (A9) |

**Folder: Treatment Plan**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `active_treatment` | Dropdown: None, Whitening Series, Invisalign, Crown Prep, Implant Process | CSV / manual | Smart List "Active Treatment Follow-Up" (A2) |
| `treatment_stage` | Dropdown: Consultation, In Progress, Follow-Up, Completed | CSV / manual | Smart List "Active Treatment Follow-Up" filter combine with `active_treatment` (A2) |
| `treatment_value` | Number | CSV / manual | Internal notification "high-value patient" flag in Workflow 2 if > $1000 (A9) |
| `medical_alerts` | Textarea | CSV / manual | **Reference field** — displayed prominently on contact card. Must appear in Workflow 2 internal notification body so staff sees alerts (e.g. "Penicillin allergy") before the visit (A9) |

### A0.3 Tags (lifecycle + interest — 11 total, every tag has a producer and consumer)

**Lifecycle tags** (mutually informative — describe current state):
| Tag | Applied By | Read By |
|---|---|---|
| `new-patient-inquiry` | Form submit (A8), CSV | Workflow 1 trigger (A9), Smart List filter |
| `returning-patient` | CSV | Smart List filter |
| `referred-patient` | CSV / manual | Smart List filter |
| `emergency-visit` | CSV / Emergency Dental calendar booking | Workflow 1 conditional branch routes to emergency path |
| `appointment-scheduled` | Workflow 2 on calendar booking (A9) | Workflow 3 (No-Show) removes it; Workflow 4 (Showed) removes it |
| `appointment-completed` | Workflow 4 on Showed (A9) | Smart List "Completed Visits This Month" |
| `no-show` | Workflow 3 on No Show (A9) | Smart List "Recent No-Shows" |
| `recall-due` | Workflow 5 (Recall) when `last_visit_date` > 6 months (A9) | Day 7 Cleaning Recall campaign filter |

**Interest tags** (additive, marketing segmentation):
| Tag | Applied By | Read By |
|---|---|---|
| `interested-whitening` | Trigger link in Recall Email (A7), CSV | Marketing campaign filter, Smart List |
| `interested-orthodontics` | Trigger link in Welcome Email (A7), CSV | Marketing campaign filter, Smart List |
| `interested-cleaning` | Trigger link in Recall Email (A7) | Day 7 Cleaning Recall campaign filter |

### A0.4 Templates (Day 3 = single source of truth — workflows reference by exact name)

**SMS Templates (5):**
| Template Name | Used By | Uses |
|---|---|---|
| `BrightSmile - New Patient Welcome SMS` | Workflow 1 (A9) — sent immediately on form submit | `business_name`, `contact.first_name`, `business_phone` |
| `BrightSmile - Appointment Reminder 24hr` | Workflow 2 (A9) — 24hr before appointment | `business_name`, `appointment.start_time`, `appointment.title` |
| `BrightSmile - No-Show Recovery SMS` | Workflow 3 (A9) — 2hr after no-show | `contact.first_name`, `book_link` |
| `BrightSmile - Post-Procedure Care SMS` | Workflow 4 (A9) — 3hr after Showed | `contact.first_name`, `business_phone`, `review_link` |
| `BrightSmile - Recall Notice SMS` | Workflow 5 (A9) — 6 months after `last_visit_date` | `contact.first_name`, `business_name`, `book_link` |

**Email Templates (3):**
| Template Name | Used By | Uses |
|---|---|---|
| `BrightSmile - New Patient Welcome Email` | Workflow 1 (A9) — sent immediately on form submit | `offer_new_patient` (subject), `business_name`, `business_address`, `business_hours`, `business_phone`, `book_link`, embeds trigger link `interested-orthodontics` |
| `BrightSmile - Appointment Confirmation Email` | Workflow 2 (A9) — on booking | `business_name`, `business_address`, `appointment.start_time`, `appointment.title`, `medical_alerts` (visible in summary) |
| `BrightSmile - Post-Visit Summary Email` | Workflow 4 (A9) — 24hr after Showed | `contact.first_name`, `next_appointment_type`, `review_link`, `business_phone` |

### A0.5 Trigger Links (3 — embedded in emails)

| Trigger Link Name | Embed Location | Tag Applied On Click |
|---|---|---|
| `interested-orthodontics` | Welcome Email body ("Curious about Invisalign?") | `interested-orthodontics` |
| `interested-whitening` | Day 7 Cleaning Recall Email | `interested-whitening` |
| `interested-cleaning` | Day 7 Cleaning Recall Email | `interested-cleaning` |

### A0.6 Calendars (3)

| Calendar | Type | Used By |
|---|---|---|
| `BrightSmile - General Checkup` | Basic, 60min, Mon-Thu 8AM-5PM, Fri 8AM-2PM, **Zoom connected** | Funnel Thank You page embed (A8), `book_link` custom value points here, Workflow 2 trigger fires on booking |
| `BrightSmile - Emergency Dental` | Basic, 30min, same-day, Mon-Fri 8AM-5PM | Emergency Dental form path (A8) → applies `emergency-visit` tag |
| `BrightSmile - Cosmetic Consultation` | Basic, 45min, Mon-Thu 9AM-4PM | Booked manually for `interested-whitening` / `interested-orthodontics` contacts |

### A0.7 Pipeline (1 main — 5 stages)

`BrightSmile - Patient Treatment Pipeline`:
1. **New Inquiry** — opportunity created here by Form (A8) on submission
2. **Consultation Scheduled** — moved here by Workflow 2 when calendar booking happens
3. **Treatment In Progress** — moved manually or by Workflow 4 when treatment_stage = In Progress
4. **Treatment Completed** — moved by Workflow 4 when appointment status = Showed and treatment_stage = Completed
5. **Recall Scheduled** — moved by Workflow 5 when recall reminder is queued

> Single pipeline only. The previous "Insurance Claims" pipeline was orphaned (no workflow created or moved opportunities through it) — removed.

### A0.8 Form (1)

`BrightSmile - New Patient Inquiry Form` — embedded on funnel landing page.

| Form Field | Required | Maps To | Notes |
|---|---|---|---|
| First Name | yes | `contact.first_name` | standard |
| Last Name | yes | `contact.last_name` | standard |
| Email | yes | `contact.email` | standard |
| Phone | yes | `contact.phone` | standard |
| Insurance Provider | yes | custom field `insurance_provider` | dropdown matches custom field options |
| Preferred Dentist | no | custom field `preferred_dentist` | dropdown |
| Reason for Visit | yes | tag application logic (see below) | dropdown: Routine Check, Cosmetic, Orthodontics, Emergency |

**Form submission actions (configured in form settings, NOT in a workflow):**
1. Apply tag: `new-patient-inquiry`
2. Set custom field `patient_type` = "New Patient"
3. Map "Reason for Visit" → conditional tag:
   - "Routine Check" → no extra tag
   - "Cosmetic" → `interested-whitening`
   - "Orthodontics" → `interested-orthodontics`
   - "Emergency" → `emergency-visit`
4. Create opportunity in `BrightSmile - Patient Treatment Pipeline` at stage **New Inquiry** with value 0 (treatment value updated later)

> **The form creates the opportunity, not Workflow 1.** This eliminates the duplicate-opportunity bug from the previous version.

### A0.9 Funnel (1)

`BrightSmile - Free Dental Exam Funnel` — 2 steps:
1. **Landing page** — embeds `BrightSmile - New Patient Inquiry Form`, hero uses `offer_new_patient`, sub-headline references `business_hours`
2. **Thank You page** — embeds `BrightSmile - General Checkup` calendar widget, "What to bring" section uses `business_address`

### A0.10 Workflows (5 — every action references dictionary assets by exact name)

| # | Workflow Name | Trigger | Templates Used | Pipelines Touched | Tags |
|---|---|---|---|---|---|
| 1 | `BrightSmile - New Patient Inquiry` | Tag added: `new-patient-inquiry` | New Patient Welcome SMS, New Patient Welcome Email | None (form already created opp) | `new-patient-inquiry` (entry) |
| 2 | `BrightSmile - Appointment Booked` | Calendar booking (any) | Appointment Reminder 24hr, Appointment Confirmation Email | Move opp to "Consultation Scheduled" | adds `appointment-scheduled` |
| 3 | `BrightSmile - No-Show Recovery` | Appointment status = No Show | No-Show Recovery SMS | (no move) | adds `no-show`, removes `appointment-scheduled` |
| 4 | `BrightSmile - Post-Visit Care + Review` | Appointment status = Showed | Post-Procedure Care SMS, Post-Visit Summary Email | Move opp to "Treatment Completed" if treatment_stage = Completed | adds `appointment-completed`, removes `appointment-scheduled` |
| 5 | `BrightSmile - Recall (6-Month)` | Date trigger: `last_visit_date` + 6 months | Recall Notice SMS | Move opp to "Recall Scheduled" | adds `recall-due` |

### A0.11 Smart Lists (5 — each filter uses fields from A0.2)

| Smart List | Filter |
|---|---|
| Overdue for Cleaning | `last_visit_date` < (today - 6 months) AND `visit_frequency` = "Every 6 Months" |
| Self-Pay Patients | `insurance_provider` = "Self-Pay" |
| Dr. Kim's Patients | `preferred_dentist` = "Dr. Sarah Kim" |
| Outstanding Balance | `outstanding_balance` > 0 |
| Active Treatment Follow-Up | `active_treatment` ≠ None AND `treatment_stage` = "In Progress" |
| Payment Plans Active | `payment_plan_active` = TRUE |

### A0.12 Day 7 Marketing Campaign (1)

`BrightSmile - Cleaning Recall Campaign`:
- Target: Smart List "Overdue for Cleaning"
- Email body: contains all 3 trigger links (interested-cleaning, interested-whitening, interested-orthodontics)
- Sending: scheduled or manual

---

> **Everything in A1–A10 below uses ONLY the assets in A0.** If an asset name appears in a Day section that isn't in A0, it's a bug — flag it.

---

## A1 — Day 1: Settings + Custom Values

### A1.1 Business Profile (sub-account → Settings → Business Info)
- Business Name: `BrightSmile Dental Clinic`
- Address: `456 Smile Avenue, Springfield`
- Phone: `+14085550100`
- Email: `smile@brightsmile.com`
- Hours: Mon-Thu 8AM-5PM, Fri 8AM-2PM, Sat-Sun Closed
- Category: Healthcare / Dental
- Timezone: your local timezone

### A1.2 Custom Values (sub-account → Settings → Custom Values)

Create all 8 from A0.1. The values for `business_phone`, `business_email`, `business_address`, `business_hours`, `business_name` should match Business Profile. `book_link` will be filled in after A4 (leave placeholder for now). `review_link` and `offer_new_patient` use the values in A0.1.

### A1.3 Sub-Account Users (sub-account → Settings → Team)

> Reminder from Section 0.3: these are sub-account users (client staff), NOT agency users.

| Role | Permissions |
|---|---|
| Admin (Owner) | All access |
| Front Desk | All Contacts, All Conversations, All Calendars, View Pipelines, View Payments, No Settings |
| Dentist | Assigned Contacts, Assigned Conversations, Own Schedule, View Pipelines, No Payments, No Settings |

Create at least Admin + Front Desk.

**Definition of Done (A1):**
- [ ] Business Profile complete
- [ ] All 8 custom values from A0.1 created (`book_link` can be placeholder until A4)
- [ ] At least 2 users (Admin + Front Desk) created with permissions matching the table

> **Agency Context:** This sub-account exists because you created it in Section 0.4. Everything above happens INSIDE the sub-account. If at any point the top-left shows your agency name, you're in the wrong place.

---

## A2 — Day 2: Custom Fields + CSV Import + Smart Lists

### A2.1 Custom Fields (sub-account → Settings → Custom Fields)

Create all 14 fields from A0.2 in three folders: Patient Info, Insurance & Billing, Treatment Plan. Use the exact field keys (lowercase + underscore) for clean CSV mapping.

### A2.2 CSV Import

- Source: `cert-prep/sample-data/brightsmile-patients.csv`
- Sub-account → Contacts → Import (top-right)
- Map every CSV column to its custom field (or standard field for first_name, last_name, email, phone, tags)
- Verify: 15 contacts imported, custom fields populated, tags applied
- Verify Sarah Johnson's contact card: `patient_type = New Patient`, no `last_visit_date`, tag `new-patient-inquiry`
- Verify Robert Thompson: `medical_alerts` = "Penicillin allergy..." (this field MUST display on the card — confirm)

### A2.3 `TEST - Do Not Delete` Contact

Create manually:
- First name: `TEST`, Last name: `Do Not Delete`
- Email: `test+brightsmile@yopmail.com`
- Phone: your real phone (so you can receive workflow SMS during testing)
- Used for testing every workflow in A9

### A2.4 Smart Lists (Contacts → Smart Lists tab → + New)

Create all 6 from A0.11. After each, verify the count matches expectation:
- Overdue for Cleaning: 2 contacts (Susan Lewis, Nancy Garcia — depending on today's date relative to last visit)
- Self-Pay Patients: 2 contacts (Robert Thompson, Mary Jackson)
- Dr. Kim's Patients: ~7 contacts
- Outstanding Balance: 4 contacts (James Wilson $150, Robert Thompson $300, Patricia Taylor $75, Nancy Garcia $200, Mary Jackson $300)
- Active Treatment Follow-Up: 3 contacts (Emily Rodriguez Whitening Consultation, David Anderson Crown Prep In Progress, Patricia Taylor Whitening In Progress, Susan Lewis Invisalign In Progress)
- Payment Plans Active: 2 contacts (David Anderson, Susan Lewis)

**Definition of Done (A2):**
- [ ] All 14 custom fields created in correct folders
- [ ] CSV imported, 15 contacts present, fields populated
- [ ] `TEST - Do Not Delete` contact created
- [ ] All 6 Smart Lists created and return non-zero counts

---

## A3 — Day 3: Templates + Webchat

### A3.1 SMS Templates (sub-account → Marketing → Templates → SMS)

Build all 5 from A0.4 SMS table. Exact bodies:

**`BrightSmile - New Patient Welcome SMS`**
```
Hi {{contact.first_name}}, welcome to {{custom_values.business_name}}! We received your inquiry and will reach out within 1 business day. Questions? Call {{custom_values.business_phone}}.
```

**`BrightSmile - Appointment Reminder 24hr`**
```
{{contact.first_name}}, this is a reminder for your {{appointment.title}} appointment with {{custom_values.business_name}} tomorrow at {{appointment.start_time}}. Reply CONFIRM to confirm or CALL to reschedule.
```

**`BrightSmile - No-Show Recovery SMS`**
```
Hi {{contact.first_name}}, we missed you today. Life happens — book a new time here: {{custom_values.book_link}}. Reply if you'd like us to call.
```

**`BrightSmile - Post-Procedure Care SMS`**
```
Hi {{contact.first_name}}, thanks for visiting today! If you have any post-procedure questions, call {{custom_values.business_phone}}. We'd love a quick review: {{custom_values.review_link}}
```

**`BrightSmile - Recall Notice SMS`**
```
{{contact.first_name}}, it's been about 6 months since your last visit at {{custom_values.business_name}}. Time for your cleaning! Book here: {{custom_values.book_link}}
```

### A3.2 Email Templates (sub-account → Marketing → Templates → Email)

**`BrightSmile - New Patient Welcome Email`**
- Subject: `Welcome — your {{custom_values.offer_new_patient}}`
- Body includes: greeting using `contact.first_name`, mentions `business_name`, lists `business_hours`, lists `business_address`, includes a CTA button linked to `book_link`, footer includes `business_phone` and `business_email`
- **Embed trigger link:** `interested-orthodontics` — text "Curious about Invisalign? Tell us"

**`BrightSmile - Appointment Confirmation Email`**
- Subject: `Confirmed — {{appointment.title}} at {{custom_values.business_name}}`
- Body: appointment date/time, location (`business_address`), what to bring
- **Includes a "Notes for our team" line that surfaces `medical_alerts`** (so the patient can confirm we have current info)

**`BrightSmile - Post-Visit Summary Email`**
- Subject: `Thanks for visiting — your visit summary`
- Body: summary placeholder using `next_appointment_type` (for next-visit recommendation), review CTA linked to `review_link`, contact info `business_phone`

### A3.3 Webchat Widget (sub-account → Sites → Chat Widget)

- Greeting: `Welcome to {{custom_values.business_name}}! How can we help?`
- After-hours: `We're closed (hours: {{custom_values.business_hours}}). Leave your info and we'll call back: {{custom_values.business_phone}}`
- Pre-chat fields: Name, Email, Phone, Reason for inquiry (dropdown)
- Disclaimer: "This chat is for scheduling and general inquiries only. Do not share medical information here."

> **Note on Telephony:** SMS template creation is all you need for Part B. A2P 10DLC and LC Phone are in the A2P Compliance badge.

**Definition of Done (A3):**
- [ ] 5 SMS templates created with EXACT names from A0.4, bodies use only A0.1 custom values + standard merge fields
- [ ] 3 email templates created with EXACT names, embedding trigger link in Welcome Email
- [ ] Webchat widget configured and embedded
- [ ] Snapshot: `Snapshot - BrightSmile - v1 Foundation (Day 3)`

> **Agency Step — Snapshot v1:** Switch to Agency view → Snapshots → + New Snapshot → source: BrightSmile → name: `Snapshot - BrightSmile - v1 Foundation (Day 3)` → Save → return to BrightSmile sub-account. Target: < 3 minutes.

---

## A4 — Day 4: Calendars + Zoom Integration

> **The #1 confirmed Part B failure point.** Drill until you can do the integration in under 5 minutes.

### A4.1 Calendars (sub-account → Calendars → + New Calendar)

Build all 3 from A0.6:

**`BrightSmile - General Checkup`** (Basic)
- Duration: 60 min, Buffer: 10 min after
- Availability: Mon-Thu 8AM-5PM, Fri 8AM-2PM
- Booking form fields: Name, Email, Phone, Reason for Visit
- Confirmation message: uses `business_name`

**`BrightSmile - Emergency Dental`** (Basic)
- Duration: 30 min, Buffer: 5 min
- Availability: Mon-Fri 8AM-5PM, **same-day only** (set "Allow booking X days in advance" = 0)
- Booking form: Name, Phone, Brief Description

**`BrightSmile - Cosmetic Consultation`** (Basic)
- Duration: 45 min, Buffer: 15 min
- Availability: Mon-Thu 9AM-4PM
- Booking form: Name, Email, Phone, Area of Interest

### A4.2 Zoom / Google Meet Integration — `BrightSmile - General Checkup`

1. Calendars → click `BrightSmile - General Checkup` → **Edit**
2. Find **Connections** tab (or Integrations — varies by GHL version)
3. Connect Zoom (or Google Meet) → authenticate
4. Set Meeting Location: **Zoom** (or Google Meet)
5. Save
6. **Test:** open the calendar booking link → book a test appointment with your `TEST` contact's email
7. **Verify:** confirmation email contains the Zoom/Meet link
8. **Verify:** the calendar event in your dashboard shows the link

Drill checklist:
- [ ] Zoom/Meet connected
- [ ] Test booking placed
- [ ] Meeting link in confirmation email
- [ ] Link visible in calendar event

### A4.3 Update `book_link` Custom Value

Now that the calendar exists, copy its public booking URL and paste it into the `book_link` custom value (Settings → Custom Values → edit). This unblocks templates that reference it.

**Definition of Done (A4):**
- [ ] All 3 calendars created with names matching A0.6
- [ ] General Checkup connected to Zoom or Google Meet
- [ ] Test booking confirmed with meeting link
- [ ] `book_link` custom value updated to the General Checkup booking URL
- [ ] Snapshot: `Snapshot - BrightSmile - v2 Calendars (Day 4)`

> **Agency Step — Snapshot v2:** Agency view → Snapshots → + New → source: BrightSmile → name: `Snapshot - BrightSmile - v2 Calendars (Day 4)` → Save.

---

## A5 — Day 5: Pipeline + Opportunities

### A5.1 Pipeline (sub-account → Opportunities → Pipelines → + New)

Create `BrightSmile - Patient Treatment Pipeline` with 5 stages from A0.7:
1. New Inquiry
2. Consultation Scheduled
3. Treatment In Progress
4. Treatment Completed
5. Recall Scheduled

### A5.2 Sample Opportunities

Use imported contacts. Create 5:
| Contact | Stage | Value |
|---|---|---|
| Sarah Johnson | New Inquiry | $0 |
| David Anderson | Treatment In Progress | $1,200 (Crown Prep) |
| Susan Lewis | Treatment In Progress | $5,500 (Invisalign) |
| Patricia Taylor | Treatment In Progress | $900 (Whitening) |
| Linda Martinez | Recall Scheduled | $150 |

**Definition of Done (A5):**
- [ ] Pipeline created with all 5 stages from A0.7
- [ ] 5 opportunities created at correct stages with values
- [ ] Snapshot: `Snapshot - BrightSmile - v3 Pipeline (Day 5)`

> **Agency Step — Snapshot v3:** Agency view → Snapshots → + New → source: BrightSmile → name: `Snapshot - BrightSmile - v3 Pipeline (Day 5)` → Save.

---

## A6 — Day 6: Payments **[Lower Part B priority]**

> Payments rarely appear in Part B. Build this section quickly; don't drill it.

### A6.1 Products (sub-account → Payments → Products)
| Product | Price | Type |
|---|---|---|
| Dental Exam | $200 | One-time |
| Professional Cleaning | $150 | One-time |
| Teeth Whitening Package | $450 | One-time |
| Crown / Cap | $1,200 | One-time |
| Emergency Visit | $300 | One-time |

### A6.2 One Invoice (for the drill)
Create one invoice for Patricia Taylor: Teeth Whitening Package $450 + insurance adjustment line item −$50 = $400.

**Definition of Done (A6):**
- [ ] 5 products created
- [ ] 1 invoice created with negative line item

---

## A7 — Day 7: Trigger Links + Marketing Campaign

### A7.1 Trigger Links (sub-account → Marketing → Trigger Links)

Create all 3 from A0.5:
- `interested-orthodontics` → applies tag `interested-orthodontics`
- `interested-whitening` → applies tag `interested-whitening`
- `interested-cleaning` → applies tag `interested-cleaning`

### A7.2 Embed Trigger Links Into Existing Email Templates

Open `BrightSmile - New Patient Welcome Email` (created in A3) and verify the `interested-orthodontics` link is inserted (you did this in A3). If not, add it now: linked text "Curious about Invisalign? Tell us".

Create a NEW email template `BrightSmile - Cleaning Recall Email` for the campaign (this template lives only in A7's campaign — it's not in A0.4 because workflows don't reference it):
- Subject: `{{contact.first_name}}, time for your cleaning?`
- Body uses `business_name`, `book_link` button
- **Embeds 3 trigger links:** `interested-cleaning`, `interested-whitening`, `interested-orthodontics`

> Note: this is the only template not in A0.4 because it's used by a campaign, not a workflow. It's documented here so it isn't an orphan.

### A7.3 Campaign (sub-account → Marketing → Campaigns)

`BrightSmile - Cleaning Recall Campaign`:
- Target: Smart List `Overdue for Cleaning`
- Email: `BrightSmile - Cleaning Recall Email`
- Trigger: manual or scheduled

### A7.4 Test Trigger Links

Click each trigger link manually with the `TEST` contact → verify tag applied on contact card.

**Definition of Done (A7):**
- [ ] 3 trigger links created
- [ ] Welcome Email contains `interested-orthodontics` (verified)
- [ ] Cleaning Recall Email created with all 3 trigger links embedded
- [ ] Cleaning Recall Campaign created
- [ ] All 3 trigger links tested → tags applied
- [ ] Snapshot: `Snapshot - BrightSmile - v4 Marketing (Day 7)`

> **Agency Step — Snapshot v4:** Agency view → Snapshots → + New → source: BrightSmile → name: `Snapshot - BrightSmile - v4 Marketing (Day 7)` → Save.

---

## A8 — Day 8: Form + Funnel

### A8.1 Form (sub-account → Sites → Forms → + New)

Build `BrightSmile - New Patient Inquiry Form` exactly as defined in A0.8.

| Form Field | Type | Required | Maps To |
|---|---|---|---|
| First Name | Text | yes | `contact.first_name` |
| Last Name | Text | yes | `contact.last_name` |
| Email | Email | yes | `contact.email` |
| Phone | Phone | yes | `contact.phone` |
| Insurance Provider | Dropdown (matches custom field options) | yes | `insurance_provider` |
| Preferred Dentist | Dropdown (Dr. Sarah Kim, Dr. James Okafor) | no | `preferred_dentist` |
| Reason for Visit | Dropdown (Routine Check, Cosmetic, Orthodontics, Emergency) | yes | (drives conditional tag below) |

**Form Submit Actions** (Form Settings → Actions on Submit):
1. Apply tag: `new-patient-inquiry`
2. Set custom field `patient_type` = `New Patient`
3. Conditional tag based on Reason for Visit:
   - Cosmetic → tag `interested-whitening`
   - Orthodontics → tag `interested-orthodontics`
   - Emergency → tag `emergency-visit`
   - Routine Check → no extra tag
4. Create opportunity in pipeline `BrightSmile - Patient Treatment Pipeline` at stage `New Inquiry`, value 0

> **Test the form** before moving on. Submit it as the `TEST` contact → verify on contact card: tag applied, custom field set, opportunity created in pipeline.

### A8.2 Funnel (sub-account → Sites → Funnels → + New)

`BrightSmile - Free Dental Exam Funnel` — 2 steps:

**Step 1 — Landing Page:**
- Hero headline: uses `{{custom_values.offer_new_patient}}`
- Sub-headline: "Open {{custom_values.business_hours}}"
- Embed: `BrightSmile - New Patient Inquiry Form`
- CTA below form: same form's submit button

**Step 2 — Thank You Page:**
- Headline: "You're booked — let's get you scheduled"
- Embed: `BrightSmile - General Checkup` calendar widget
- Below calendar: "What to bring" using `business_address`

Publish the funnel. Test the full flow: submit form on landing page → see Thank You page → book on calendar → verify Workflow 2 fires (after A9 builds it).

**Definition of Done (A8):**
- [ ] Form built with exact name and field-to-custom-field mapping from A0.8
- [ ] Form submit actions configured (tag + custom field + conditional tag + opportunity creation)
- [ ] Form tested with `TEST` contact → tag, field, opportunity all verified
- [ ] 2-step funnel built and published
- [ ] General Checkup calendar embedded on Thank You page

---

## A9 — Day 9: Workflows (the centerpiece)

> Build all 5 workflows from A0.10. Each one ONLY uses templates, custom fields, tags, and pipeline stages from A0. Verify the **Published** toggle on every one before testing.

### Workflow 1: `BrightSmile - New Patient Inquiry`

**Trigger:** Tag added: `new-patient-inquiry`

**Actions:**
1. Send SMS: `BrightSmile - New Patient Welcome SMS`
2. Send Email: `BrightSmile - New Patient Welcome Email`
3. **If/Else:** custom field `preferred_dentist` = "Dr. Sarah Kim"
   - True: Internal notification to Front Desk: "New inquiry — assigned to Dr. Kim. Patient: {{contact.first_name}} {{contact.last_name}}, Insurance: {{custom_values.... wait}}"
   - Use field merge: `Insurance: {{contact.insurance_provider}}` (custom field merge syntax depends on GHL version — typically `{{contact.custom_field.insurance_provider}}` or via the field picker in the builder)
   - False: Internal notification to Front Desk: "New inquiry — assigned to Dr. Okafor. Patient: {{contact.first_name}} {{contact.last_name}}"
4. Wait: 24 hours
5. **If/Else:** has tag `appointment-scheduled`?
   - True: end (workflow goal achieved)
   - False: Send SMS: "Hi {{contact.first_name}}, just checking in — ready to book? {{custom_values.book_link}}"

**Test (with `TEST` contact):**
- [ ] Manually apply tag `new-patient-inquiry` → workflow fires
- [ ] SMS received on your real phone
- [ ] Welcome email received (check spam)
- [ ] Front Desk notification received (in-app)
- [ ] After 24h (or shortcut by manually adding `appointment-scheduled` tag during the wait), the if/else branch is taken
- [ ] Workflow status: **Published**

### Workflow 2: `BrightSmile - Appointment Booked`

**Trigger:** Appointment Booked (any calendar — or specifically `BrightSmile - General Checkup` and `BrightSmile - Cosmetic Consultation`; configure for "Any Calendar")

**Actions:**
1. Add tag: `appointment-scheduled`
2. Move opportunity in `BrightSmile - Patient Treatment Pipeline` → stage `Consultation Scheduled`
3. Send Email: `BrightSmile - Appointment Confirmation Email`
4. Wait until: 24 hours before appointment start time
5. Send SMS: `BrightSmile - Appointment Reminder 24hr`
6. Internal notification to Front Desk: "Appointment tomorrow — {{contact.first_name}} — alerts: [merge `medical_alerts`] — outstanding balance: [merge `outstanding_balance`]"

**Test:**
- [ ] Book a test appointment via the General Checkup calendar
- [ ] Tag `appointment-scheduled` applied
- [ ] Opportunity moved to Consultation Scheduled
- [ ] Confirmation email arrived
- [ ] (Wait or shortcut) — 24hr SMS arrives
- [ ] Internal notification body correctly includes medical_alerts text from contact card
- [ ] Workflow status: **Published**

### Workflow 3: `BrightSmile - No-Show Recovery`

**Trigger:** Appointment Status = No Show

**Actions:**
1. Remove tag: `appointment-scheduled`
2. Add tag: `no-show`
3. Wait: 2 hours
4. Send SMS: `BrightSmile - No-Show Recovery SMS`
5. Internal notification to Front Desk: "No-show recovery initiated — {{contact.first_name}}"

**Test:**
- [ ] Manually mark a test appointment as No Show
- [ ] Tag `appointment-scheduled` removed
- [ ] Tag `no-show` added
- [ ] After 2h (or shortcut), SMS sent
- [ ] Workflow status: **Published**

### Workflow 4: `BrightSmile - Post-Visit Care + Review`

**Trigger:** Appointment Status = Showed

**Actions:**
1. Remove tag: `appointment-scheduled`
2. Add tag: `appointment-completed`
3. Update Contact Field: `last_visit_date` = today
4. **If/Else:** custom field `treatment_stage` = "Completed"
   - True: Move opportunity → stage `Treatment Completed`
   - False: leave opportunity in current stage
5. Wait: 3 hours
6. Send SMS: `BrightSmile - Post-Procedure Care SMS`
7. Wait: 24 hours
8. Send Email: `BrightSmile - Post-Visit Summary Email`

**Test:**
- [ ] Mark a test appointment as Showed
- [ ] Tags swapped correctly
- [ ] `last_visit_date` updated to today on contact card
- [ ] After 3h, post-procedure SMS arrived
- [ ] After 24h, summary email arrived (with review link)
- [ ] Workflow status: **Published**

### Workflow 5: `BrightSmile - Recall (6-Month)`

**Trigger:** Date trigger on field `last_visit_date` + 6 months (configure as "Wait until field date + 6 months")

Alternative trigger: Smart List entry — when contact enters Smart List `Overdue for Cleaning`. Use whichever trigger your GHL version supports.

**Actions:**
1. Add tag: `recall-due`
2. Move opportunity → stage `Recall Scheduled`
3. Send SMS: `BrightSmile - Recall Notice SMS`
4. Wait: 7 days
5. **If/Else:** has tag `appointment-scheduled`?
   - True: end (goal achieved)
   - False: Internal notification to Front Desk: "Recall — {{contact.first_name}} hasn't booked yet"

**Test:**
- [ ] Manually set `last_visit_date` to 6+ months ago on `TEST` contact
- [ ] (Or for smart-list-trigger version) verify TEST appears in Overdue for Cleaning list
- [ ] Workflow fires
- [ ] Tag `recall-due` applied
- [ ] Opportunity moved
- [ ] Recall SMS received
- [ ] Workflow status: **Published**

**Definition of Done (A9):**
- [ ] All 5 workflows built with exact names from A0.10
- [ ] Every workflow uses ONLY templates / fields / tags / pipeline stages defined in A0
- [ ] All 5 toggles show **Published** (not just Saved)
- [ ] All 5 test checklists complete
- [ ] Snapshot: `Snapshot - BrightSmile - v5 Workflows (Day 9)`

> **Agency Step — Snapshot v5 + Load Drill:**
> 1. Agency view → Snapshots → + New → source: BrightSmile → name: `Snapshot - BrightSmile - v5 Workflows (Day 9)` → Save
> 2. Then drill the load: Snapshots → find v5 → ⋮ → Push to Account → select a blank test sub-account → Add/Merge → Load → enter target sub-account → verify workflows appeared
> 3. This is the exact Part B snapshot sequence. Target: under 4 minutes total.

---

## A10 — Day 10: Reputation + Reporting **[Lower Part B priority]**

> Reputation/community is rarely tested in Part B. Skim if pressed for time.

### A10.1 Review Response Templates

The post-visit review request is already handled by Workflow 4 (Post-Visit Summary Email contains `review_link`). For staff response to incoming reviews, write 3 short response templates:
- 5-star: thank-you + share request
- 3-4 star: thank-you + invitation to discuss directly
- 1-2 star: apology + direct phone outreach offer using `business_phone`

### A10.2 Weekly Reporting Checklist

| Check | Where |
|---|---|
| New leads this week | Reporting → Source attribution / Smart List `new-patient-inquiry` |
| Appointments booked vs no-show rate | Reporting → Appointment Report |
| Smart Lists updated | Contacts → Smart Lists tab |
| Outstanding balances over $100 | Smart List `Outstanding Balance` |
| Workflows still Published | Automation → Workflows status column |

**Definition of Done (A10):**
- [ ] 3 review response templates written
- [ ] Weekly checklist documented
- [ ] Snapshot: `Snapshot - BrightSmile - v6 Complete (Day 10)`

> **Agency Step — Final Snapshot + Agency-Level Review:**
> 1. Agency view → Snapshots → + New → source: BrightSmile → name: `Snapshot - BrightSmile - v6 Complete (Day 10)` → all assets → Save
> 2. Agency Dashboard — review BrightSmile's stats summary
> 3. Accounts list → BrightSmile → ⋮ menu → explore Edit / Pause / View Reports
> 4. Sub-account Reporting → check Attribution and Appointment reports

---

## A-Scorecard — BrightSmile Self-Grade

| Category | Score (0-5) |
|---|---:|
| A1 Settings + 8 custom values created | |
| A2 14 custom fields + CSV import + 6 Smart Lists | |
| A3 5 SMS + 3 email templates referencing A0.1 values | |
| A4 3 calendars + Zoom integration + book_link updated | |
| A5 Pipeline with 5 stages + 5 opportunities | |
| A6 Products + 1 invoice (light) | |
| A7 3 trigger links + Cleaning Recall Email + Campaign | |
| A8 Form with full field mapping + 2-step funnel + opportunity-creation logic | |
| A9 All 5 workflows built, **Published**, tested | |
| A10 Review templates + weekly checklist (light) | |
| **Coherence Check** — every asset in A0 has a producer AND consumer | |
| **Part B Speed** — < 25 min for the timed drill below | |

Target: **45+/55** with "Yes" on Coherence and Part B Speed.

---

## A — Part B Timed Drill (30 minutes)

> Use a fresh blank sub-account. Build from scratch under timer.

1. Business profile + 3 custom values (target: < 5 min)
2. Add 1 contact + apply tag (target: < 2 min)
3. Pipeline with 3 stages + 1 opportunity (target: < 5 min)
4. Calendar connected to Zoom + test booking (target: < 7 min)
5. Workflow: tag-triggered → SMS template → internal notification → **Published** (target: < 8 min)
6. Snapshot from Agency view (target: < 3 min)

| Time | Result |
|---|---|
| < 25 min | Exam-ready |
| 25-40 min | Borderline — drill the slowest step in isolation 5x |
| > 40 min | Not ready — back to navigation drills |

---
---

# Section B — Elevate Digital Agency

> Build inside the **Elevate Digital Agency** sub-account. Same data-dictionary discipline as Section A.

---

## B0 — Data Dictionary (the contract for Section B)

### B0.1 Custom Values (7 — all consumed)

| Name | Value | Created In | Consumed By |
|---|---|---|---|
| `business_name` | Elevate Digital Agency | B1 | All templates (B3), Funnel (B8), Calendar confirmations (B4), Webchat (B3) |
| `business_phone` | +14085554000 | B1 | Webchat after-hours, Onboarding Email |
| `business_email` | hello@elevateagency.com | B1 | All email footers |
| `business_address` | 789 Marketing Blvd, Suite 300, Springfield | B1 | Onboarding Email, Renewal Email |
| `business_hours` | Mon-Fri 9AM-6PM | B1 | Webchat after-hours, Funnel landing |
| `book_strategy_link` | (paste Strategy Call calendar URL after B4) | B4 | Lead Nurture SMS, Welcome Email CTA |
| `offer_consultation` | Free 30-Minute Strategy Session | B1 | Funnel landing hero, Welcome Email subject |

> Removed: `offer_audit`, `onboarding_link`, `offer_retainer_discount` (had no downstream consumer in the previous version).

### B0.2 Custom Fields (10 — wired to consumers)

The CSV at `cert-prep/sample-data/elevate-clients.csv` populates these.

**Folder: Client Account**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `service_package` | Dropdown: SEO Only, PPC Only, Social Media, Full Stack, Email Marketing, Web Design | Form (B8) / CSV | Smart List "Full Stack Clients" (B2), Workflow 2 internal notification |
| `monthly_retainer` | Number | CSV / manual | Smart List "High-Retainer Clients" (B2), internal notification high-value flag |
| `contract_end_date` | Date | CSV / manual | **Workflow 3 (Renewal) trigger** — date-based, Smart List "Contracts Expiring 60d" |
| `account_manager` | Dropdown: Rachel (AM), Derek (AM), Unassigned | Form / CSV | Smart List "Rachel's Book of Business" (B2), Workflow internal-notification routing |
| `client_status` | Dropdown: Prospect, Onboarding, Active, Paused, Churned | CSV / Workflow 2 sets to Onboarding then Active | Smart List "Win-Back Targets" (B2), Workflow conditional logic |

**Folder: Business Profile**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `industry` | Dropdown: Healthcare, Real Estate, Legal, E-Commerce, Restaurant, SaaS, Other | Form / CSV | Reference + segmentation |
| `website_url` | Text | Form / CSV | Reference (used in audit deliverables) |

**Folder: Performance & Pipeline**
| Field (key) | Type | Set By | Read By |
|---|---|---|---|
| `lead_source` | Dropdown: Inbound (Website), Referral, Cold Outreach, Networking Event, LinkedIn | Form / CSV | Reporting attribution, Smart List "Referral Pipeline" |
| `proposal_value` | Number | Manual | Smart List "High-Value Prospects" (B2), internal notification flag |
| `pipeline_stage` | Dropdown matches Client Acquisition Pipeline stages | CSV (initial) / pipeline auto-syncs | Reference (stages live in pipeline; this field mirrors for filtering) |

> Removed CSV columns kept as fields but not actively wired into workflows (`company_size`, `annual_revenue`, `current_marketing_spend`, `upsell_opportunity`) — these are reference fields the AM uses; documented as such.

### B0.3 Tags

**Lifecycle:**
| Tag | Applied By | Read By |
|---|---|---|
| `new-agency-lead` | Form submit (B8), CSV | Workflow 1 trigger, Smart List |
| `onboarding-client` | Workflow 2 on Closed Won, CSV | Smart List, status check |
| `active-client` | Workflow 2 after onboarding complete, CSV | Smart List "Active Book of Business" |
| `paused-client` | CSV / manual | Smart List "Win-Back Targets" |
| `churned-client` | CSV / manual | Smart List "Win-Back Targets" |
| `renewal-approaching` | Workflow 3 (Renewal trigger 60d before contract_end_date) | Smart List, marketing campaign target |
| `strategy-call-booked` | Workflow 4 on Strategy Call calendar booking | Workflow 1 if/else branch |

**Interest:**
| Tag | Applied By | Read By |
|---|---|---|
| `interested-seo` | Trigger link in Lead Nurture Email (B7) | Marketing campaign filter |
| `interested-ppc` | Trigger link | Marketing campaign filter |
| `interested-social` | Trigger link | Marketing campaign filter |
| `download-case-study` | Trigger link | Workflow 1 if/else (engaged lead) |

**Modifier:**
| Tag | Applied By | Read By |
|---|---|---|
| `high-value` | CSV (high-value clients) | Smart List "High-Value Active" |
| `high-value-prospect` | CSV (prospects with proposal_value > 50K) | Smart List "High-Value Prospects" |
| `win-back` | CSV (paused/churned win-back targets) | Smart List "Win-Back Targets" |

### B0.4 Templates

**SMS Templates (5):**
| Template Name | Used By | Uses |
|---|---|---|
| `Elevate - Lead Nurture SMS` | Workflow 1 (B9) — 2 days after form if no booking | `contact.first_name`, `book_strategy_link` |
| `Elevate - Strategy Call Reminder 24hr` | Workflow 4 (B9) | `appointment.start_time`, `business_name` |
| `Elevate - Onboarding Welcome SMS` | Workflow 2 (B9) — on Closed Won | `contact.first_name`, `business_name`, `business_email` |
| `Elevate - Renewal Notice SMS` | Workflow 3 (B9) — 30 days before contract end | `contact.company_name`, `book_strategy_link` |
| `Elevate - Monthly Report Ready SMS` | Workflow 5 (B9) — when tag added monthly | `contact.company_name`, `book_strategy_link` |

**Email Templates (3):**
| Template Name | Used By | Uses |
|---|---|---|
| `Elevate - Lead Nurture Email` | Workflow 1 — sent immediately on form submit | `offer_consultation` (subject), `business_name`, embeds 3 trigger links (interested-seo, interested-ppc, interested-social), and 1 download trigger link (download-case-study) |
| `Elevate - Onboarding Kit Email` | Workflow 2 — on Closed Won | `business_name`, `business_email`, `business_phone`, `business_address`, includes onboarding steps |
| `Elevate - Monthly Report Email` | Workflow 5 — when tag added monthly | `contact.company_name`, `service_package`, `book_strategy_link`, `monthly_retainer` |

> Removed: Renewal Email, Proposal Follow-Up Email, Newsletter — they were defined but never referenced. The Renewal flow uses just the SMS in Workflow 3.

### B0.5 Trigger Links (4)

| Trigger Link | Embed Location | Tag On Click |
|---|---|---|
| `interested-seo` | Lead Nurture Email body | `interested-seo` |
| `interested-ppc` | Lead Nurture Email body | `interested-ppc` |
| `interested-social` | Lead Nurture Email body | `interested-social` |
| `download-case-study` | Lead Nurture Email body (CTA button) | `download-case-study` |

### B0.6 Calendars (2)

| Calendar | Type | Used By |
|---|---|---|
| `Elevate - Strategy Call` | **Round Robin** (Rachel + Derek), 30min, **Zoom connected** | Funnel Thank You embed, `book_strategy_link`, Workflow 4 trigger |
| `Elevate - Onboarding Kickoff` | Basic, 90min | Booked manually post-Closed Won |

> Removed: "Monthly Review Call" — no workflow triggered off it.

### B0.7 Pipeline (1 main — 5 stages)

`Elevate - Client Acquisition Pipeline`:
1. **New Lead** — opportunity created here by Form (B8) on submission
2. **Discovery Call Scheduled** — moved by Workflow 4 on Strategy Call booking
3. **Audit Delivered** — moved manually after audit
4. **Proposal Sent** — moved manually
5. **Closed Won** — triggers Workflow 2

> Single pipeline. The previous "Project Delivery" pipeline had no workflow moving opps through it — removed.

### B0.8 Form (1)

`Elevate - Strategy Session Form`.

| Form Field | Required | Maps To |
|---|---|---|
| First Name | yes | `contact.first_name` |
| Last Name | yes | `contact.last_name` |
| Email | yes | `contact.email` |
| Phone | yes | `contact.phone` |
| Company Name | yes | `contact.company_name` |
| Website URL | yes | custom field `website_url` |
| Industry | yes | `industry` |
| Lead Source | no | `lead_source` |

**Form submit actions:**
1. Apply tag: `new-agency-lead`
2. Set custom field `client_status` = `Prospect`
3. Create opportunity in `Elevate - Client Acquisition Pipeline` at stage `New Lead`, value 0

### B0.9 Funnel (1)

`Elevate - Free Strategy Session Funnel`:
1. **Landing page** — embeds `Elevate - Strategy Session Form`, hero uses `offer_consultation`
2. **Thank You page** — embeds `Elevate - Strategy Call` calendar, sub-text uses `business_hours`

### B0.10 Workflows (5)

| # | Name | Trigger | Templates | Pipeline | Tags |
|---|---|---|---|---|---|
| 1 | `Elevate - New Lead Nurture` | Tag added: `new-agency-lead` | Lead Nurture Email, Lead Nurture SMS (delayed) | None (form created opp) | reads `strategy-call-booked` for branching |
| 2 | `Elevate - Onboarding Activation` | Opp stage = Closed Won | Onboarding Welcome SMS, Onboarding Kit Email | Sets `client_status` = Onboarding then later Active | adds `onboarding-client`, `active-client` |
| 3 | `Elevate - Renewal Reminder` | Date: `contract_end_date` − 60 days | Renewal Notice SMS | (no move) | adds `renewal-approaching` |
| 4 | `Elevate - Strategy Call Booked` | Calendar `Elevate - Strategy Call` booking | Strategy Call Reminder 24hr | Move opp to `Discovery Call Scheduled` | adds `strategy-call-booked` |
| 5 | `Elevate - Monthly Report Notification` | Tag added: `monthly-report-ready` (manual or scheduled) | Monthly Report Email, Monthly Report Ready SMS | (no move) | (entry tag only) |

### B0.11 Smart Lists (5)

| Smart List | Filter |
|---|---|
| Contracts Expiring 60d | `contract_end_date` between today and today+60d AND `client_status` = Active |
| High-Value Active | tag `active-client` AND `monthly_retainer` > 5000 |
| Rachel's Book of Business | `account_manager` = "Rachel (AM)" |
| High-Value Prospects | tag `new-agency-lead` AND `proposal_value` > 50000 |
| Win-Back Targets | `client_status` IN (Paused, Churned) OR tag `win-back` |

---

> **Everything in B1–B10 below uses ONLY the assets in B0.**

---

## B1 — Day 1: Settings + Custom Values

### B1.1 Business Profile
- Name: Elevate Digital Agency
- Address: 789 Marketing Blvd, Suite 300, Springfield
- Phone: +14085554000
- Email: hello@elevateagency.com
- Hours: Mon-Fri 9AM-6PM
- Category: Professional Services / Marketing

### B1.2 Custom Values
Create all 7 from B0.1. `book_strategy_link` placeholder until B4.

### B1.3 Sub-Account Users
Create at least: Agency Owner (sub-account level — different from your real agency admin) + Account Manager.

**Definition of Done (B1):**
- [ ] Business Profile complete
- [ ] All 7 custom values from B0.1 created
- [ ] At least 2 sub-account users created

---

## B2 — Day 2: Custom Fields + CSV Import + Smart Lists

### B2.1 Custom Fields
Create all 10 in three folders matching B0.2.

### B2.2 CSV Import
- Source: `cert-prep/sample-data/elevate-clients.csv`
- Map columns to fields (field keys match CSV columns)
- Verify: 15 contacts imported, custom fields populated, tags applied
- Verify Stephanie Chen: `service_package` = Full Stack, `monthly_retainer` = 9000, tag `active-client high-value`

### B2.3 `TEST - Do Not Delete` contact
Same as Section A — manual create, your real phone for SMS testing.

### B2.4 Smart Lists
Create all 5 from B0.11.

**Definition of Done (B2):**
- [ ] 10 custom fields in correct folders
- [ ] CSV imported, 15 contacts present
- [ ] `TEST` contact created
- [ ] All 5 Smart Lists return non-zero counts

---

## B3 — Day 3: Templates + Webchat

### B3.1 SMS Templates
Build all 5 from B0.4 SMS table:

**`Elevate - Lead Nurture SMS`**
```
Hi {{contact.first_name}}, this is {{custom_values.business_name}}. Following up on your strategy session interest — book a time here: {{custom_values.book_strategy_link}}
```

**`Elevate - Strategy Call Reminder 24hr`**
```
Reminder: your strategy call with {{custom_values.business_name}} is tomorrow at {{appointment.start_time}}.
```

**`Elevate - Onboarding Welcome SMS`**
```
Welcome to {{custom_values.business_name}}, {{contact.first_name}}! Your onboarding kit is in your inbox. Reply or email {{custom_values.business_email}} with questions.
```

**`Elevate - Renewal Notice SMS`**
```
Hi {{contact.company_name}} team — your contract renews in 60 days. Let's chat about next year: {{custom_values.book_strategy_link}}
```

**`Elevate - Monthly Report Ready SMS`**
```
Your {{contact.company_name}} monthly report is ready. Book a review call: {{custom_values.book_strategy_link}}
```

### B3.2 Email Templates
Build all 3 from B0.4 email table:

**`Elevate - Lead Nurture Email`**
- Subject: `{{custom_values.offer_consultation}} — let's talk strategy`
- Body uses `business_name`, `book_strategy_link` (CTA)
- **Embeds 4 trigger links:** `interested-seo`, `interested-ppc`, `interested-social`, `download-case-study`

**`Elevate - Onboarding Kit Email`**
- Subject: `Welcome to {{custom_values.business_name}} — your onboarding kit`
- Body: onboarding steps, `business_email`, `business_phone`, `business_address`

**`Elevate - Monthly Report Email`**
- Subject: `Your {{contact.company_name}} report is ready`
- Body: report summary placeholder, references `service_package`, `monthly_retainer`, CTA to `book_strategy_link`

### B3.3 Webchat
- Greeting: "Talk to a Growth Strategist at {{custom_values.business_name}}"
- After-hours: "We're closed. Hours: {{custom_values.business_hours}}. Email {{custom_values.business_email}}"
- Pre-chat: Name, Email, Company Name, Service Interest

**Definition of Done (B3):**
- [ ] 5 SMS templates with exact names from B0.4
- [ ] 3 email templates with exact names; Lead Nurture Email contains all 4 trigger link placements
- [ ] Webchat configured
- [ ] Snapshot: `Snapshot - Elevate - v1 Foundation (Day 3)`

> **Agency Step — Snapshot v1:** Agency view → Snapshots → + New → source: Elevate → name as above → Save.

---

## B4 — Day 4: Calendars + Zoom Integration

### B4.1 Calendars

**`Elevate - Strategy Call`** (Round Robin)
- 30 min, buffer 10 min after
- Assign to: Rachel + Derek
- Availability: Mon-Fri 9AM-5PM
- Booking form: Name, Email, Company Name, Website, Primary Goal

**`Elevate - Onboarding Kickoff`** (Basic)
- 90 min, buffer 15 min
- Mon-Thu 10AM-4PM
- Booking form: Company Name, Stakeholders, Top 3 Goals

### B4.2 Zoom / Google Meet Integration on Strategy Call

Same procedure as Section A:
1. Calendar → Edit → Connections → Connect Zoom (or Google Meet)
2. Set Meeting Location
3. Test: book a test call → verify meeting link in confirmation email

### B4.3 Update `book_strategy_link`

Copy Strategy Call public booking URL → Settings → Custom Values → update.

**Definition of Done (B4):**
- [ ] 2 calendars created (names match B0.6)
- [ ] Strategy Call connected to Zoom or Meet
- [ ] Test booking confirmed with meeting link
- [ ] `book_strategy_link` updated
- [ ] Snapshot: `Snapshot - Elevate - v2 Calendars (Day 4)`

> **Agency Step:** Snapshot as above.

---

## B5 — Day 5: Pipeline + Opportunities

### B5.1 Pipeline
Create `Elevate - Client Acquisition Pipeline` with 5 stages from B0.7.

### B5.2 Sample Opportunities
| Contact | Stage | Value |
|---|---|---|
| Brian Williams | New Lead | $48,000 |
| Olivia Nguyen | Audit Delivered | $18,000 |
| Jason Park | Proposal Sent | $36,000 |
| Amanda Foster | Proposal Sent | $96,000 |
| Stephanie Chen | Closed Won | $108,000 |

**Definition of Done (B5):**
- [ ] Pipeline with 5 stages
- [ ] 5 opportunities placed at correct stages with values
- [ ] Snapshot: `Snapshot - Elevate - v3 Pipeline (Day 5)`

> **Agency Step:** Snapshot.

---

## B6 — Day 6: Payments **[Lower Part B priority]**

### B6.1 Products
| Product | Price | Type |
|---|---|---|
| SEO Retainer | $3,000/mo | Recurring |
| PPC Management | $4,000/mo | Recurring |
| Social Media Management | $2,000/mo | Recurring |
| Brand Audit | $1,500 | One-time |

### B6.2 One Invoice + Coupon
- Onboarding invoice for NexaVision Media: Brand Audit $1,500
- Coupon `PARTNER15` — 15% off one-time products

**Definition of Done (B6):**
- [ ] 4 products created with correct billing types
- [ ] 1 invoice created
- [ ] 1 coupon created

---

## B7 — Day 7: Trigger Links + Marketing

### B7.1 Trigger Links
Create all 4 from B0.5: `interested-seo`, `interested-ppc`, `interested-social`, `download-case-study`.

### B7.2 Verify Embedding
Open `Elevate - Lead Nurture Email` (built in B3) → confirm all 4 trigger links present. Add if missing.

### B7.3 Test
Click each trigger link manually → verify tag applied to `TEST` contact.

**Definition of Done (B7):**
- [ ] 4 trigger links created
- [ ] All 4 embedded in Lead Nurture Email (verified)
- [ ] All 4 tested → tags applied
- [ ] Snapshot: `Snapshot - Elevate - v4 Marketing (Day 7)`

---

## B8 — Day 8: Form + Funnel

### B8.1 Form
Build `Elevate - Strategy Session Form` per B0.8 with all field mappings and submit actions (tag, custom field, opportunity creation).

Test: submit as `TEST` → verify tag, custom field, opportunity in pipeline.

### B8.2 Funnel
`Elevate - Free Strategy Session Funnel`:
- Landing: hero uses `offer_consultation`, embeds the form
- Thank You: embeds Strategy Call calendar, sub-text uses `business_hours`

Publish → submit form on landing → see Thank You → book on calendar → confirm Workflow 4 fires (after B9).

**Definition of Done (B8):**
- [ ] Form built with full B0.8 field mapping + submit actions
- [ ] Form tested with TEST → tag/field/opp verified
- [ ] 2-step funnel published
- [ ] Strategy Call embedded on Thank You

---

## B9 — Day 9: Workflows

> Build all 5 from B0.10. Verify **Published** on each.

### Workflow 1: `Elevate - New Lead Nurture`

**Trigger:** Tag added: `new-agency-lead`

**Actions:**
1. Send Email: `Elevate - Lead Nurture Email`
2. Wait: 2 days
3. **If/Else:** has tag `strategy-call-booked`?
   - True: end (lead is engaged)
   - False: Send SMS: `Elevate - Lead Nurture SMS`
4. Wait: 5 days
5. **If/Else:** has tag `download-case-study` OR `interested-seo` OR `interested-ppc` OR `interested-social`?
   - True: Internal notification to Account Manager: "Engaged lead — {{contact.company_name}} — review trigger-link tags"
   - False: end

**Test:** TEST contact → apply `new-agency-lead` → verify email → wait/skip → SMS branch → verify Published.

### Workflow 2: `Elevate - Onboarding Activation`

**Trigger:** Opp stage changed to "Closed Won" in `Elevate - Client Acquisition Pipeline`

**Actions:**
1. Add tag: `onboarding-client`
2. Set custom field `client_status` = "Onboarding"
3. Send SMS: `Elevate - Onboarding Welcome SMS`
4. Send Email: `Elevate - Onboarding Kit Email`
5. Wait: 14 days
6. Add tag: `active-client`, remove tag: `onboarding-client`
7. Set `client_status` = "Active"
8. Internal notification to Account Manager: "{{contact.company_name}} is now Active — start monthly cadence"

**Test:** Move TEST opp to Closed Won → verify all actions → Published.

### Workflow 3: `Elevate - Renewal Reminder`

**Trigger:** Date: `contract_end_date` - 60 days

**Actions:**
1. Add tag: `renewal-approaching`
2. Send SMS: `Elevate - Renewal Notice SMS`
3. Wait: 21 days (40 days before contract end)
4. **If/Else:** has tag `renewal-booked` (manual) OR opportunity moved to renewal stage?
   - True: end
   - False: Internal notification to Account Manager: "Renewal not booked — {{contact.company_name}}"

**Test:** Set TEST `contract_end_date` to 60 days from today → verify trigger fires → Published.

### Workflow 4: `Elevate - Strategy Call Booked`

**Trigger:** Appointment Booked on `Elevate - Strategy Call` calendar

**Actions:**
1. Add tag: `strategy-call-booked`
2. Move opportunity → stage `Discovery Call Scheduled`
3. Wait until: 24 hours before appointment
4. Send SMS: `Elevate - Strategy Call Reminder 24hr`
5. Internal notification to Account Manager: "Strategy call tomorrow — {{contact.company_name}}"

**Test:** Book test appointment → verify tag, opp move, reminder → Published.

### Workflow 5: `Elevate - Monthly Report Notification`

**Trigger:** Tag added: `monthly-report-ready` (manually applied when AM publishes the report, or via a recurring schedule)

**Actions:**
1. Send Email: `Elevate - Monthly Report Email`
2. Send SMS: `Elevate - Monthly Report Ready SMS`
3. Wait: 3 days
4. **If/Else:** has appointment booked on Strategy Call calendar in last 3 days?
   - True: end
   - False: Send SMS: "Hi — book your review here: {{custom_values.book_strategy_link}}"

**Test:** Apply tag manually → email + SMS → Published.

**Definition of Done (B9):**
- [ ] All 5 workflows built with exact names from B0.10
- [ ] Every action references only B0 assets
- [ ] All 5 toggles **Published**
- [ ] All 5 test sequences complete
- [ ] Snapshot: `Snapshot - Elevate - v5 Workflows (Day 9)`

> **Agency Step — Snapshot v5 + Load Drill:** save snapshot, then push to a blank test sub-account, verify workflows appeared. Target: < 4 minutes.

---

## B10 — Day 10: Reputation + Reporting **[Lower Part B priority]**

### B10.1 Testimonial Permission Workflow (light)
Manual process: when an opportunity reaches "Active" status for 90+ days, AM applies tag `testimonial-eligible` and emails permission request manually.

### B10.2 Weekly Reporting Checklist
| Check | Where |
|---|---|
| New leads this week | Smart List `new-agency-lead` |
| Strategy calls booked vs completed | Calendar dashboard / Reporting |
| Active clients with retainers | Smart List `High-Value Active` |
| Contracts expiring in 60 days | Smart List `Contracts Expiring 60d` |
| Workflows still Published | Automation → Workflows |

**Definition of Done (B10):**
- [ ] Testimonial process documented
- [ ] Weekly checklist documented
- [ ] Snapshot: `Snapshot - Elevate - v6 Complete (Day 10)`

> **Agency Step — Final Snapshot + Cross-Account Review:**
> 1. Save final snapshot
> 2. Agency Dashboard — compare BrightSmile vs Elevate stats
> 3. Snapshots list: confirm 12 snapshots (6 per business)
> 4. Accounts list — review both sub-accounts' status

---

## B-Scorecard — Elevate Self-Grade

| Category | Score (0-5) |
|---|---:|
| B1 Settings + 7 custom values | |
| B2 10 custom fields + CSV + 5 Smart Lists | |
| B3 5 SMS + 3 email templates referencing B0.1 values | |
| B4 2 calendars + Zoom + book_strategy_link updated | |
| B5 Pipeline + 5 opportunities | |
| B6 Products + invoice + coupon (light) | |
| B7 4 trigger links embedded + tested | |
| B8 Form mapped + funnel published + opp creation tested | |
| B9 All 5 workflows built, **Published**, tested | |
| B10 Reputation + reporting (light) | |
| **Coherence Check** — every B0 asset has producer + consumer | |
| **Part B Speed** — < 25 min on drill below | |

Target: **45+/55** with "Yes" on Coherence and Part B Speed.

---

## B — Part B Timed Drill (30 minutes)

Same drill as Section A — fresh blank sub-account, 30-min timer:
1. Business profile + 3 custom values
2. Add 1 contact + apply tag
3. Pipeline with 3 stages + 1 opportunity
4. Calendar + Zoom + test booking
5. Workflow: tag-triggered → email → internal notification → **Published**
6. Snapshot from Agency view

Your Elevate drill time should be 5-10 min faster than your BrightSmile drill time. If not, more navigation reps needed.

---
---

## Snapshots Summary

| Snapshot | After |
|---|---|
| `Snapshot - BrightSmile - v1 Foundation` | A3 |
| `Snapshot - BrightSmile - v2 Calendars` | A4 |
| `Snapshot - BrightSmile - v3 Pipeline` | A5 |
| `Snapshot - BrightSmile - v4 Marketing` | A7 |
| `Snapshot - BrightSmile - v5 Workflows` | A9 |
| `Snapshot - BrightSmile - v6 Complete` | A10 |
| `Snapshot - Elevate - v1 Foundation` | B3 |
| `Snapshot - Elevate - v2 Calendars` | B4 |
| `Snapshot - Elevate - v3 Pipeline` | B5 |
| `Snapshot - Elevate - v4 Marketing` | B7 |
| `Snapshot - Elevate - v5 Workflows` | B9 |
| `Snapshot - Elevate - v6 Complete` | B10 |

Rule: never overwrite — always create a new version number.

---

## Coherence Audit Checklist

Run this at the end of each section:

For each item in A0 (or B0), verify:
- [ ] It is created in the day section it claims to be created in
- [ ] At least one downstream consumer actually references it
- [ ] If it's a custom field: a workflow, smart list, form, OR template merges/reads it
- [ ] If it's a custom value: at least one template body or funnel page contains it
- [ ] If it's a tag: something applies it AND something reads it (a workflow trigger, a smart list filter, or a campaign target)
- [ ] If it's a template: a workflow references it by exact name
- [ ] If it's a trigger link: it's embedded in a real email
- [ ] If it's a calendar: a workflow has a trigger pointing at it OR it's embedded in a funnel
- [ ] If it's a pipeline stage: a workflow either creates or moves opportunities into it
- [ ] If it's a form: it's embedded in a funnel AND its submit actions are configured

Any "no" answer is a bug. Fix it before moving on.
