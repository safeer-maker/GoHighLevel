# GHL Extended Practical — Real-World Business Builds

> **Purpose:** practice building full, realistic GHL sub-accounts after you've passed Part B.
> **Not exam prep.** For the 30-minute Part B drill, use [practical-part-b-core.md](practical-part-b-core.md).

---

## How this file differs from the core file

| Topic | Core file | This file |
|---|---|---|
| Time per build | 30 min target | 4-6 hours per scenario |
| Asset count | ~12 named assets | 30-50 per scenario |
| SMS sending | Skipped (A2P-dependent) | Templates created, sending optional |
| Payments / Webchat / Campaigns | Skipped | Included as real-world skills |
| Workflows | 1 form-triggered | 5 covering full lifecycle |
| Goal | Pass the exam | Run a real client build |

This file fixes the bugs that were in the original `practical-brightsmile-elevate-full-build.md` — see the bug list at the bottom.

---

## Two Scenarios

- **Section A — BrightSmile Dental Clinic** (healthcare, individual customers)
- **Section B — Elevate Digital Agency** (B2B services, recurring retainers)

Build them in order. Section B re-uses the same disciplines but in a B2B context, which forces you to adapt rather than copy.

---

## Global Rules

- **BrightSmile assets prefix:** `BrightSmile - <name>`
- **Elevate assets prefix:** `Elevate - <name>`
- **Tags:** lowercase + hyphens (`new-patient-inquiry`)
- **Custom field keys:** lowercase + underscores (`patient_type`)
- **Custom value keys:** lowercase + underscores (`business_name`)
- **Merge syntax:** `{{custom_values.<key>}}` for custom values, `{{contact.<field_key>}}` for contact custom fields, `{{appointment.start_time}}` etc. for appointments. The editor's merge-tag dropdown inserts the right syntax — use it instead of typing.
- **Test contact:** keep one `TEST - Do Not Delete` per sub-account with your real email + phone, used to receive every workflow's output during testing.

---

# Section A — BrightSmile Dental Clinic

## A0 — Data Dictionary

### A0.1 Custom Values (8)

| Name | Value | Created | Consumed By |
|---|---|---|---|
| `business_name` | BrightSmile Dental Clinic | A1 | All templates, funnel, calendar confirmations |
| `business_phone` | +14085550100 | A1 | Email footers, webchat after-hours |
| `business_email` | smile@brightsmile.com | A1 | Email footers |
| `business_address` | 456 Smile Avenue, Springfield | A1 | Welcome Email body, Confirmation Email |
| `business_hours` | Mon-Thu 8AM-5PM, Fri 8AM-2PM | A1 | Welcome Email, webchat after-hours, funnel |
| `book_link` | (calendar URL after A4 — placeholder Day 1) | A1 → A4 | Welcome Email CTA, Recall Email |
| `review_link` | https://g.page/r/brightsmile/review | A1 | Post-Visit Email |
| `offer_new_patient` | Free Dental Exam & X-Rays for new patients | A1 | Funnel hero, Welcome Email subject |

> **Build order note:** `book_link` is created Day 1 with a placeholder URL because templates in Day 3 reference it. The real URL gets pasted in Day 4 after the calendar is created. This is expected — don't try to "fix" the order.

### A0.2 Custom Fields (14)

The CSV at `cert-prep/sample-data/brightsmile-patients.csv` populates these. Each field has at least one downstream consumer.

**Folder: Patient Info**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `patient_type` | Dropdown: New Patient, Returning, Referred, Emergency | Form (A8) / CSV / manual | Workflow 1 if/else (A9) |
| `last_visit_date` | Date | CSV / Workflow 4 sets to today on Showed | Smart List "Overdue for Cleaning", Workflow 5 trigger |
| `next_appointment_type` | Dropdown: Cleaning, Filling, Crown, Whitening, Veneer, Ortho Check, Emergency | CSV / manual | Workflow 2 internal notification |
| `preferred_dentist` | Dropdown: Dr. Sarah Kim, Dr. James Okafor | Form / CSV | Smart List, Workflow 1 routing |
| `visit_frequency` | Dropdown: Every 6 Months, Quarterly, As Needed | CSV / manual | Smart List filter |

**Folder: Insurance & Billing**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `insurance_provider` | Dropdown: Aetna, BlueCross, Cigna, Delta Dental, MetLife, United, Self-Pay, Other | Form / CSV | Smart List, Workflow 1 notification |
| `insurance_id` | Text | CSV / manual | Reference, Workflow 2 notification |
| `coverage_level` | Dropdown: Basic, Standard, Premium, None | CSV / manual | Reference (front-desk authorization) |
| `payment_plan_active` | Checkbox | CSV / manual | Smart List "Payment Plans Active" |
| `outstanding_balance` | Number | CSV / manual | Smart List, Workflow 2 flags > $100 |

**Folder: Treatment Plan**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `active_treatment` | Dropdown: None, Whitening Series, Invisalign, Crown Prep, Implant Process | CSV / manual | Smart List "Active Treatment Follow-Up" |
| `treatment_stage` | Dropdown: Consultation, In Progress, Follow-Up, Completed | CSV / manual | Smart List, Workflow 4 if/else |
| `treatment_value` | Number | CSV / manual | Workflow 2 flags > $1000 |
| `medical_alerts` | Textarea | CSV / manual | **Reference field — must appear in Workflow 2 internal notification body so staff sees alerts before visit** |

> **Folder organization is optional** — Part B doesn't test it. Folders are included here because in real use the front desk needs to find fields fast.

### A0.3 Tags

**Lifecycle (mutually informative — describe state):**
| Tag | Applied By | Read By |
|---|---|---|
| `new-patient-inquiry` | Form submit, CSV | Workflow 1 trigger, Smart List |
| `returning-patient` | CSV | Smart List |
| `referred-patient` | CSV / manual | Smart List |
| `emergency-visit` | CSV / Emergency calendar booking | Workflow 1 conditional branch |
| `appointment-scheduled` | Workflow 2 on calendar booking | Workflow 3 removes; Workflow 4 removes |
| `appointment-completed` | Workflow 4 on Showed | Smart List "Completed Visits This Month" |
| `no-show` | Workflow 3 on No Show | Smart List "Recent No-Shows" |
| `recall-due` | Workflow 5 (Recall) | Recall Campaign filter |

**Interest (additive, marketing segmentation):**
| Tag | Applied By | Read By |
|---|---|---|
| `interested-whitening` | Trigger link in Recall Email, CSV | Marketing campaign filter |
| `interested-orthodontics` | Trigger link in Welcome Email, CSV | Marketing campaign filter |
| `interested-cleaning` | Trigger link in Recall Email | Recall Campaign filter |

### A0.4 Templates

**SMS Templates (3 — created so you know where the SMS template editor lives, but workflows do NOT send them by default. Toggle the SMS actions ON in Workflow 2 and 4 only if your A2P 10DLC is approved on this sub-account):**

| Template Name | Used By | Uses |
|---|---|---|
| `BrightSmile - Appointment Reminder 24hr` | Workflow 2 (optional Send SMS action) | `business_name`, `appointment.start_time`, `appointment.title` |
| `BrightSmile - No-Show Recovery SMS` | Workflow 3 (optional) | `contact.first_name`, `book_link` |
| `BrightSmile - Recall Notice SMS` | Workflow 5 (optional) | `contact.first_name`, `business_name`, `book_link` |

> **Why SMS is "optional":** sending an SMS in GHL requires A2P 10DLC carrier approval, which takes 1-3 weeks and isn't relevant to base admin cert. The templates are included so you know the screen exists. In a real client build, you flip these on after A2P clears.

**Email Templates (4):**
| Template Name | Used By | Uses |
|---|---|---|
| `BrightSmile - New Patient Welcome Email` | Workflow 1 | `offer_new_patient` (subject), `business_name`, `business_address`, `business_hours`, `business_phone`, `book_link`. Embeds trigger link `interested-orthodontics`. |
| `BrightSmile - Appointment Confirmation Email` | Workflow 2 | `business_name`, `business_address`, `appointment.start_time`, `appointment.title`, `medical_alerts` |
| `BrightSmile - Post-Visit Summary Email` | Workflow 4 | `contact.first_name`, `next_appointment_type`, `review_link`, `business_phone` |
| `BrightSmile - Cleaning Recall Email` | Recall Campaign (A7) | `contact.first_name`, `business_name`, `book_link`. Embeds trigger links `interested-cleaning`, `interested-whitening`, `interested-orthodontics`. |

> **Templates location matters:** create these under Marketing → Templates → Email (the **shared** template library). When a workflow's "Send Email" action asks for a template, it reads from this library. If you build the email **inline** inside the workflow instead, it works but isn't reusable — and the workflow won't see "missing" if you delete a shared template later.

### A0.5 Trigger Links (3)

| Trigger Link | Embed Location | Tag On Click |
|---|---|---|
| `interested-orthodontics` | Welcome Email — text "Curious about Invisalign?" | `interested-orthodontics` |
| `interested-whitening` | Cleaning Recall Email | `interested-whitening` |
| `interested-cleaning` | Cleaning Recall Email | `interested-cleaning` |

### A0.6 Calendars (3)

| Calendar | Type | Used By |
|---|---|---|
| `BrightSmile - General Checkup` | Basic, 60min, Mon-Thu 8-5, Fri 8-2, **Zoom connected** | Funnel Thank You embed, `book_link` points here, Workflow 2 trigger |
| `BrightSmile - Emergency Dental` | Basic, 30min, same-day, Mon-Fri 8-5 | Emergency form path → applies `emergency-visit` |
| `BrightSmile - Cosmetic Consultation` | Basic, 45min, Mon-Thu 9-4 | Booked manually for whitening/ortho prospects |

### A0.7 Pipeline (1, 5 stages)

`BrightSmile - Patient Treatment Pipeline`:
1. **New Inquiry** — opportunity created here by **Workflow 1** (NOT by the form — see fix note A0.8)
2. **Consultation Scheduled** — moved by Workflow 2 on calendar booking
3. **Treatment In Progress** — moved manually or by Workflow 4 when `treatment_stage` = In Progress
4. **Treatment Completed** — moved by Workflow 4 on Showed + `treatment_stage` = Completed
5. **Recall Scheduled** — moved by Workflow 5

### A0.8 Form (1)

`BrightSmile - New Patient Inquiry Form` — embedded on funnel landing.

| Form Field | Required | Maps To |
|---|---|---|
| First Name | yes | `contact.first_name` |
| Last Name | yes | `contact.last_name` |
| Email | yes | `contact.email` |
| Phone | yes | `contact.phone` |
| Insurance Provider | yes | `insurance_provider` |
| Preferred Dentist | no | `preferred_dentist` |
| Reason for Visit | yes | (drives conditional tag — see below) |

**Form submit actions:**
1. Apply tag: `new-patient-inquiry`
2. Set custom field `patient_type` = "New Patient"
3. Conditional tag from Reason for Visit:
   - "Routine Check" → no extra tag
   - "Cosmetic" → `interested-whitening`
   - "Orthodontics" → `interested-orthodontics`
   - "Emergency" → `emergency-visit`

> **Bug fix from previous version:** the form does **NOT** create an opportunity. GHL forms don't have a "create opportunity" action. **Workflow 1 creates the opportunity** when triggered by the `new-patient-inquiry` tag (or by Form Submitted directly — both work). This eliminates the duplicate-opportunity confusion in the previous file.

### A0.9 Funnel (1)

`BrightSmile - Free Dental Exam Funnel` — 2 steps:
1. **Landing page** — embeds the form, hero uses `offer_new_patient`, sub-headline uses `business_hours`
2. **Thank You page** — embeds `BrightSmile - General Checkup` calendar, "What to bring" uses `business_address`

### A0.10 Workflows (5)

| # | Name | Trigger | Templates | Pipeline | Tags |
|---|---|---|---|---|---|
| 1 | `BrightSmile - New Patient Inquiry` | Tag added: `new-patient-inquiry` | New Patient Welcome Email | **Creates opportunity** at "New Inquiry" | reads `new-patient-inquiry` |
| 2 | `BrightSmile - Appointment Booked` | Calendar booking (any) | Appointment Confirmation Email + (optional) 24hr Reminder SMS | Move opp → "Consultation Scheduled" | adds `appointment-scheduled` |
| 3 | `BrightSmile - No-Show Recovery` | Appointment status = No Show | (optional) No-Show Recovery SMS | (no move) | adds `no-show`, removes `appointment-scheduled` |
| 4 | `BrightSmile - Post-Visit Care + Review` | Appointment status = Showed | Post-Visit Summary Email | Move opp → "Treatment Completed" if `treatment_stage` = Completed | adds `appointment-completed`, removes `appointment-scheduled` |
| 5 | `BrightSmile - Recall (6-Month)` | Date trigger: `last_visit_date` + 6 months | (optional) Recall Notice SMS | Move opp → "Recall Scheduled" | adds `recall-due` |

> **Why the email replaces the SMS:** in the previous version, every workflow's primary action was Send SMS. SMS sending requires A2P approval; without it, every test fails silently and you blame the workflow. The default actions in this version are **Send Email + Internal Notification** — both work without any carrier setup. SMS sending is now an optional add-on you toggle ON when A2P clears.

### A0.11 Smart Lists (6)

| Smart List | Filter |
|---|---|
| Overdue for Cleaning | `last_visit_date` < today−6 months AND `visit_frequency` = "Every 6 Months" |
| Self-Pay Patients | `insurance_provider` = "Self-Pay" |
| Dr. Kim's Patients | `preferred_dentist` = "Dr. Sarah Kim" |
| Outstanding Balance | `outstanding_balance` > 0 |
| Active Treatment Follow-Up | `active_treatment` ≠ None AND `treatment_stage` = "In Progress" |
| Payment Plans Active | `payment_plan_active` = TRUE |

### A0.12 Marketing Campaign (1)

`BrightSmile - Cleaning Recall Campaign`:
- Target: Smart List "Overdue for Cleaning"
- Email: `BrightSmile - Cleaning Recall Email`
- Sending: scheduled or manual

---

> Everything in A1-A10 below uses ONLY assets from A0. If a name appears that isn't in A0, it's a bug — flag it.

---

## A1 — Day 1: Settings + Custom Values

### A1.1 Business Profile (sub-account → Settings → Business Info)
- Name: `BrightSmile Dental Clinic`
- Address: `456 Smile Avenue, Springfield`
- Phone: `+14085550100`
- Email: `smile@brightsmile.com`
- Hours: Mon-Thu 8AM-5PM, Fri 8AM-2PM, Sat-Sun Closed
- Category: Healthcare / Dental

### A1.2 Custom Values (Settings → Custom Values)
Create all 8 from A0.1. `book_link` gets a placeholder URL (e.g. `https://placeholder.com`) — real URL pasted in A4.

### A1.3 Sub-Account Users (Settings → Team)

| Role | Permissions |
|---|---|
| Admin (Owner) | All access |
| Front Desk | All Contacts, All Conversations, All Calendars, View Pipelines, View Payments, No Settings |
| Dentist | Assigned Contacts, Assigned Conversations, Own Schedule, View Pipelines, No Payments, No Settings |

**Done when:**
- [ ] Business Profile complete
- [ ] All 8 custom values created
- [ ] At least 2 users (Admin + Front Desk)

---

## A2 — Day 2: Custom Fields + CSV + Smart Lists

### A2.1 Custom Fields
Create all 14 from A0.2 in three folders. Use exact lowercase-underscore keys for clean CSV mapping.

### A2.2 CSV Import
- Source: `cert-prep/sample-data/brightsmile-patients.csv`
- Contacts → Import → map columns to fields (or standard fields for first_name, last_name, email, phone, tags)
- Verify 15 contacts imported
- Spot-check: Sarah Johnson has `patient_type = New Patient` and tag `new-patient-inquiry`; Robert Thompson has `medical_alerts` populated and visible on contact card

### A2.3 TEST Contact
- First name: `TEST`, Last name: `Do Not Delete`
- Email: `test+brightsmile@yopmail.com`
- Phone: your real phone (for any optional SMS testing)

### A2.4 Smart Lists
Create all 6 from A0.11. Verify counts match expectations:
- Overdue for Cleaning: ~2
- Self-Pay: ~2 (Robert Thompson, Mary Jackson)
- Dr. Kim's Patients: ~7
- Outstanding Balance: ~5
- Active Treatment Follow-Up: ~4
- Payment Plans Active: ~2

**Done when:**
- [ ] 14 custom fields in correct folders
- [ ] CSV imported, 15 contacts, fields populated
- [ ] TEST contact created
- [ ] All 6 Smart Lists return non-zero counts

---

## A3 — Day 3: Templates + Webchat

### A3.1 SMS Templates (Marketing → Templates → SMS)

Build the 3 from A0.4. Bodies:

**`BrightSmile - Appointment Reminder 24hr`**
```
{{contact.first_name}}, this is a reminder for your {{appointment.title}} with {{custom_values.business_name}} tomorrow at {{appointment.start_time}}. Reply CONFIRM or CALL to reschedule.
```

**`BrightSmile - No-Show Recovery SMS`**
```
Hi {{contact.first_name}}, we missed you today. Life happens — book a new time: {{custom_values.book_link}}
```

**`BrightSmile - Recall Notice SMS`**
```
{{contact.first_name}}, it's been ~6 months since your last visit at {{custom_values.business_name}}. Time for your cleaning: {{custom_values.book_link}}
```

> Templates exist regardless of A2P status. They only fail to *send* without A2P approval.

### A3.2 Email Templates (Marketing → Templates → Email)

Build all 4 from A0.4. Use the editor's merge-tag dropdown for custom values and contact fields — don't type the syntax.

**`BrightSmile - New Patient Welcome Email`**
- Subject: `Welcome — your {{custom_values.offer_new_patient}}`
- Body: greet using `{{contact.first_name}}`, mention `business_name`, list `business_hours` and `business_address`, CTA button to `book_link`, footer with `business_phone` and `business_email`
- Embed trigger link `interested-orthodontics` — text "Curious about Invisalign? Tell us"

**`BrightSmile - Appointment Confirmation Email`**
- Subject: `Confirmed — {{appointment.title}} at {{custom_values.business_name}}`
- Body: appointment date/time, location (`business_address`), what to bring
- Include "Notes for our team" line surfacing `{{contact.medical_alerts}}`

**`BrightSmile - Post-Visit Summary Email`**
- Subject: `Thanks for visiting — your visit summary`
- Body: summary placeholder using `{{contact.next_appointment_type}}`, review CTA → `review_link`, contact info `business_phone`

**`BrightSmile - Cleaning Recall Email`**
- Subject: `{{contact.first_name}}, time for your cleaning?`
- Body: `business_name`, CTA to `book_link`
- Embed 3 trigger links: `interested-cleaning`, `interested-whitening`, `interested-orthodontics`

### A3.3 Webchat Widget (Sites → Chat Widget)
- Greeting: `Welcome to {{custom_values.business_name}}! How can we help?`
- After-hours: `We're closed (hours: {{custom_values.business_hours}}). Call back: {{custom_values.business_phone}}`
- Pre-chat fields: Name, Email, Phone, Reason
- Disclaimer: "Chat is for scheduling and general inquiries only. Do not share medical information here."

**Done when:**
- [ ] 3 SMS templates created with exact A0.4 names
- [ ] 4 email templates created with exact names; Welcome Email contains trigger link, Recall Email contains 3 trigger links (you'll insert these in A7 if you skip the link creation now)
- [ ] Webchat configured
- [ ] Snapshot: `Snapshot - BrightSmile - v1 Foundation (Day 3)`

> **Agency Step:** Switch to Agency view → Snapshots → + New → source: BrightSmile → name as above → Save.

---

## A4 — Day 4: Calendars + Zoom Integration

### A4.1 Calendars
Build all 3 from A0.6.

**`BrightSmile - General Checkup`** — Basic, 60 min, Buffer 10 min after, Mon-Thu 8-5 & Fri 8-2, booking form: Name, Email, Phone, Reason

**`BrightSmile - Emergency Dental`** — Basic, 30 min, same-day only ("Allow booking X days in advance" = 0), Mon-Fri 8-5

**`BrightSmile - Cosmetic Consultation`** — Basic, 45 min, Mon-Thu 9-4

### A4.2 Zoom/Meet Integration on General Checkup

1. Calendars → click `BrightSmile - General Checkup` → Edit
2. Connections (or Integrations) tab → Connect Zoom or Google Meet → authenticate
3. Set Meeting Location: Zoom or Meet
4. Save
5. **Test:** copy public booking URL → book a test slot using TEST contact email
6. **Verify:** confirmation email contains the meeting link

### A4.3 Update `book_link`
Settings → Custom Values → edit `book_link` → paste the General Checkup public URL → save. Templates that reference it now work.

**Done when:**
- [ ] All 3 calendars created
- [ ] General Checkup connected to Zoom or Meet
- [ ] Test booking confirmed with meeting link
- [ ] `book_link` custom value updated to real URL
- [ ] Snapshot: `Snapshot - BrightSmile - v2 Calendars (Day 4)`

---

## A5 — Day 5: Pipeline + Opportunities

### A5.1 Pipeline (Opportunities → Pipelines → + New)
Create `BrightSmile - Patient Treatment Pipeline` with 5 stages from A0.7.

### A5.2 Sample Opportunities

| Contact | Stage | Value |
|---|---|---|
| Sarah Johnson | New Inquiry | $0 |
| David Anderson | Treatment In Progress | $1,200 (Crown Prep) |
| Susan Lewis | Treatment In Progress | $5,500 (Invisalign) |
| Patricia Taylor | Treatment In Progress | $900 (Whitening) |
| Linda Martinez | Recall Scheduled | $150 |

**Done when:**
- [ ] Pipeline with 5 stages
- [ ] 5 opportunities at correct stages
- [ ] Snapshot: `Snapshot - BrightSmile - v3 Pipeline (Day 5)`

---

## A6 — Day 6: Payments [real-world only]

> Not Part B exam content. Skip if pressed for time.

### A6.1 Products
| Product | Price | Type |
|---|---|---|
| Dental Exam | $200 | One-time |
| Professional Cleaning | $150 | One-time |
| Whitening Package | $450 | One-time |
| Crown / Cap | $1,200 | One-time |
| Emergency Visit | $300 | One-time |

### A6.2 One Invoice
Patricia Taylor: Whitening $450 + insurance adjustment line item −$50 = $400.

---

## A7 — Day 7: Trigger Links + Marketing Campaign

### A7.1 Trigger Links (Marketing → Trigger Links → + New)
Create all 3 from A0.5: each redirects to a real URL and applies its named tag.

### A7.2 Verify Embedding
Open the email templates from A3 and confirm trigger links are embedded:
- Welcome Email: `interested-orthodontics`
- Cleaning Recall Email: `interested-cleaning`, `interested-whitening`, `interested-orthodontics`

### A7.3 Campaign (Marketing → Campaigns)
`BrightSmile - Cleaning Recall Campaign`:
- Target: Smart List `Overdue for Cleaning`
- Email: `BrightSmile - Cleaning Recall Email`
- Trigger: scheduled or manual

### A7.4 Test Trigger Links
Click each trigger link manually with the TEST contact → verify tag applied.

**Done when:**
- [ ] 3 trigger links created
- [ ] Welcome Email + Recall Email both contain their trigger links
- [ ] Campaign configured
- [ ] All 3 trigger links tested → tags applied
- [ ] Snapshot: `Snapshot - BrightSmile - v4 Marketing (Day 7)`

---

## A8 — Day 8: Form + Funnel

### A8.1 Form (Sites → Forms → + New)
Build `BrightSmile - New Patient Inquiry Form` per A0.8.

| Field | Type | Required | Maps To |
|---|---|---|---|
| First Name | Text | yes | `contact.first_name` |
| Last Name | Text | yes | `contact.last_name` |
| Email | Email | yes | `contact.email` |
| Phone | Phone | yes | `contact.phone` |
| Insurance Provider | Dropdown | yes | `insurance_provider` |
| Preferred Dentist | Dropdown (Dr. Sarah Kim, Dr. James Okafor) | no | `preferred_dentist` |
| Reason for Visit | Dropdown (Routine Check, Cosmetic, Orthodontics, Emergency) | yes | drives conditional tag |

**Form Settings → Actions on Submit:**
1. Apply tag: `new-patient-inquiry`
2. Set custom field: `patient_type` = "New Patient"
3. Conditional tag from Reason for Visit:
   - Cosmetic → `interested-whitening`
   - Orthodontics → `interested-orthodontics`
   - Emergency → `emergency-visit`
   - Routine Check → no extra tag

> **Do NOT add "Create Opportunity" here** — that action doesn't exist on forms. Workflow 1 creates the opportunity.

**Test:** submit form as TEST → contact card shows tag, custom field, and (after A9) opportunity created by workflow.

### A8.2 Funnel (Sites → Funnels → + New)

`BrightSmile - Free Dental Exam Funnel` — 2 steps:

**Step 1 — Landing:**
- Hero: `{{custom_values.offer_new_patient}}`
- Sub-headline: "Open {{custom_values.business_hours}}"
- Embed: `BrightSmile - New Patient Inquiry Form` (Form element → pick saved form)

**Step 2 — Thank You:**
- Headline: "You're booked — pick a time"
- Embed: `BrightSmile - General Checkup` calendar (Calendar element → pick saved calendar)
- Below: "What to bring" using `business_address`

Publish funnel.

**Test the full chain:** open landing URL → submit → land on Thank You → calendar widget present → book → after A9, Workflow 2 fires.

**Done when:**
- [ ] Form built with full A0.8 mapping + submit actions
- [ ] Form tested with TEST → tag and field set
- [ ] 2-step funnel published
- [ ] Calendar embedded on Thank You page

---

## A9 — Day 9: Workflows

> All 5 from A0.10. Verify **Published** toggle on every one.

### Workflow 1: `BrightSmile - New Patient Inquiry`

**Trigger:** Tag added: `new-patient-inquiry`
*(Alternative trigger: Form Submitted → New Patient Inquiry Form. Either works; tag-based decouples from form changes.)*

**Actions:**
1. **Create Opportunity** → Pipeline `BrightSmile - Patient Treatment Pipeline`, Stage "New Inquiry", Value 0, Name `{{contact.first_name}} {{contact.last_name}}`
2. Send Email: `BrightSmile - New Patient Welcome Email`
3. If/Else: `preferred_dentist` = "Dr. Sarah Kim"
   - True: Internal Notification → "New inquiry — assigned to Dr. Kim. {{contact.first_name}} {{contact.last_name}}, Insurance: {{contact.insurance_provider}}"
   - False: Internal Notification → "New inquiry — assigned to Dr. Okafor. {{contact.first_name}} {{contact.last_name}}"
4. Wait: 24 hours
5. If/Else: has tag `appointment-scheduled`?
   - True: end (goal achieved)
   - False: Send Email reminder (same template, OR custom inline message "Hi {{contact.first_name}}, ready to book? {{custom_values.book_link}}")

**Test:**
- [ ] Apply tag `new-patient-inquiry` to TEST → workflow fires
- [ ] Opportunity created in pipeline at "New Inquiry"
- [ ] Welcome email received
- [ ] Internal notification received (bell icon)
- [ ] **Published** toggle on

### Workflow 2: `BrightSmile - Appointment Booked`

**Trigger:** Calendar Booking → "Any Calendar" (or specifically General Checkup + Cosmetic)

**Actions:**
1. Add tag: `appointment-scheduled`
2. Move opportunity → "Consultation Scheduled" in Patient Treatment Pipeline
3. Send Email: `BrightSmile - Appointment Confirmation Email`
4. Wait until: 24 hours before appointment start
5. *(Optional, A2P-dependent)* Send SMS: `BrightSmile - Appointment Reminder 24hr` — leave as **disabled** until A2P clears
6. Internal Notification: "Appointment tomorrow — {{contact.first_name}} — alerts: {{contact.medical_alerts}} — balance: {{contact.outstanding_balance}}"

**Test:**
- [ ] Book test appointment via General Checkup
- [ ] Tag `appointment-scheduled` applied
- [ ] Opportunity moved to Consultation Scheduled
- [ ] Confirmation email arrives
- [ ] Internal notification body includes medical_alerts text
- [ ] **Published**

### Workflow 3: `BrightSmile - No-Show Recovery`

**Trigger:** Appointment Status = No Show

**Actions:**
1. Remove tag: `appointment-scheduled`
2. Add tag: `no-show`
3. Wait: 2 hours
4. *(Optional)* Send SMS: `BrightSmile - No-Show Recovery SMS`
5. Internal Notification: "No-show recovery initiated — {{contact.first_name}}"

**Test:**
- [ ] Mark test appointment as No Show
- [ ] Tags swap correctly
- [ ] Internal notification arrives
- [ ] **Published**

### Workflow 4: `BrightSmile - Post-Visit Care + Review`

**Trigger:** Appointment Status = Showed

**Actions:**
1. Remove tag: `appointment-scheduled`
2. Add tag: `appointment-completed`
3. Update Contact Field: `last_visit_date` = today
4. If/Else: `treatment_stage` = "Completed"
   - True: Move opportunity → "Treatment Completed"
   - False: leave in current stage
5. Wait: 24 hours
6. Send Email: `BrightSmile - Post-Visit Summary Email`

**Test:**
- [ ] Mark test appointment as Showed
- [ ] Tags swapped
- [ ] `last_visit_date` set to today
- [ ] After wait, summary email arrives
- [ ] **Published**

### Workflow 5: `BrightSmile - Recall (6-Month)`

**Trigger:** Date trigger on `last_visit_date` + 6 months
*(Alternative: Smart List entry on "Overdue for Cleaning" — use whichever your GHL version supports cleanly.)*

**Actions:**
1. Add tag: `recall-due`
2. Move opportunity → "Recall Scheduled"
3. *(Optional)* Send SMS: `BrightSmile - Recall Notice SMS`
4. Send Email: a recall version of the Welcome Email OR the Cleaning Recall Email
5. Wait: 7 days
6. If/Else: has tag `appointment-scheduled`?
   - True: end
   - False: Internal Notification: "Recall — {{contact.first_name}} hasn't booked yet"

**Test:**
- [ ] Set TEST `last_visit_date` to 6+ months ago
- [ ] Workflow fires
- [ ] Tag `recall-due` applied, opportunity moved
- [ ] **Published**

**Done when:**
- [ ] All 5 workflows built with exact A0.10 names
- [ ] Every action references only A0 assets
- [ ] All 5 toggles on **Published**
- [ ] All 5 test sequences complete
- [ ] Snapshot: `Snapshot - BrightSmile - v5 Workflows (Day 9)`

> **Agency Step — Snapshot v5 + Load Drill:** save snapshot, push to a blank test sub-account, verify workflows appeared. Target: < 4 minutes total.

---

## A10 — Day 10: Reputation + Reporting [real-world only]

### A10.1 Review Response Templates
Workflow 4 sends the post-visit review request via `review_link`. For staff response to incoming reviews, write 3 short templates: 5-star (thanks + share), 3-4 star (thanks + invite to discuss), 1-2 star (apology + direct phone outreach using `business_phone`).

### A10.2 Weekly Reporting Checklist
| Check | Where |
|---|---|
| New leads this week | Reporting → Source attribution / Smart List `new-patient-inquiry` |
| Appointments booked vs no-show rate | Reporting → Appointment Report |
| Outstanding balances > $100 | Smart List `Outstanding Balance` |
| Workflows still Published | Automation → Workflows status column |

**Done when:**
- [ ] 3 review response templates
- [ ] Weekly checklist documented
- [ ] Snapshot: `Snapshot - BrightSmile - v6 Complete (Day 10)`

---

# Section B — Elevate Digital Agency

## B0 — Data Dictionary

### B0.1 Custom Values (7)

| Name | Value | Created | Consumed By |
|---|---|---|---|
| `business_name` | Elevate Digital Agency | B1 | All templates, funnel, calendar |
| `business_phone` | +14085554000 | B1 | Webchat after-hours, Onboarding Email |
| `business_email` | hello@elevateagency.com | B1 | Email footers |
| `business_address` | 789 Marketing Blvd, Suite 300, Springfield | B1 | Onboarding Email |
| `business_hours` | Mon-Fri 9AM-6PM | B1 | Webchat, Funnel landing |
| `book_strategy_link` | (Strategy Call URL after B4) | B1 → B4 | Lead Nurture SMS, Welcome Email CTA |
| `offer_consultation` | Free 30-Minute Strategy Session | B1 | Funnel hero, Welcome Email subject |

### B0.2 Custom Fields (10)

CSV: `cert-prep/sample-data/elevate-clients.csv`

**Folder: Client Account**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `service_package` | Dropdown: SEO Only, PPC Only, Social Media, Full Stack, Email Marketing, Web Design | Form / CSV | Smart List, Workflow notification |
| `monthly_retainer` | Number | CSV / manual | Smart List "High-Retainer", high-value flag |
| `contract_end_date` | Date | CSV / manual | **Workflow 3 (Renewal) trigger**, Smart List "Contracts Expiring 60d" |
| `account_manager` | Dropdown: Rachel (AM), Derek (AM), Unassigned | Form / CSV | Smart List "Rachel's Book", routing |
| `client_status` | Dropdown: Prospect, Onboarding, Active, Paused, Churned | CSV / Workflow 2 | Smart List, conditional logic |

**Folder: Business Profile**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `industry` | Dropdown: Healthcare, Real Estate, Legal, E-Commerce, Restaurant, SaaS, Other | Form / CSV | Reference + segmentation |
| `website_url` | Text | Form / CSV | Reference (audit deliverables) |

**Folder: Performance & Pipeline**
| Field key | Type | Set By | Read By |
|---|---|---|---|
| `lead_source` | Dropdown: Inbound, Referral, Cold Outreach, Networking, LinkedIn | Form / CSV | Reporting, Smart List |
| `proposal_value` | Number | Manual | Smart List "High-Value Prospects", flag |
| `pipeline_stage` | Dropdown matches pipeline stages | CSV initial / pipeline auto-syncs | Reference |

### B0.3 Tags

**Lifecycle:**
| Tag | Applied By | Read By |
|---|---|---|
| `new-agency-lead` | Form submit, CSV | Workflow 1 trigger, Smart List |
| `onboarding-client` | Workflow 2 on Closed Won, CSV | Smart List, status check |
| `active-client` | Workflow 2 after 14d, CSV | Smart List "Active Book" |
| `paused-client` | CSV / manual | Smart List "Win-Back Targets" |
| `churned-client` | CSV / manual | Smart List "Win-Back Targets" |
| `renewal-approaching` | Workflow 3 (60d before contract_end_date) | Smart List, campaign |
| `strategy-call-booked` | Workflow 4 on Strategy Call booking | Workflow 1 if/else |

**Interest:**
| Tag | Applied By | Read By |
|---|---|---|
| `interested-seo` | Trigger link in Lead Nurture Email | Campaign filter |
| `interested-ppc` | Trigger link | Campaign filter |
| `interested-social` | Trigger link | Campaign filter |
| `download-case-study` | Trigger link | Workflow 1 if/else (engaged) |

**Modifier:**
| Tag | Applied By | Read By |
|---|---|---|
| `high-value` | CSV | Smart List "High-Value Active" |
| `high-value-prospect` | CSV (proposal_value > 50K) | Smart List |
| `win-back` | CSV | Smart List |

### B0.4 Templates

**SMS Templates (3 — A2P-optional, same convention as Section A):**
| Template Name | Used By | Uses |
|---|---|---|
| `Elevate - Lead Nurture SMS` | Workflow 1 (optional) | `contact.first_name`, `book_strategy_link` |
| `Elevate - Strategy Call Reminder 24hr` | Workflow 4 (optional) | `appointment.start_time`, `business_name` |
| `Elevate - Renewal Notice SMS` | Workflow 3 (optional) | `contact.company_name`, `book_strategy_link` |

**Email Templates (4):**
| Template Name | Used By | Uses |
|---|---|---|
| `Elevate - Lead Nurture Email` | Workflow 1 | `offer_consultation` (subject), `business_name`, `book_strategy_link`. Embeds 4 trigger links. |
| `Elevate - Strategy Call Confirmation Email` | Workflow 4 | `business_name`, `appointment.start_time`, `appointment.title` |
| `Elevate - Onboarding Kit Email` | Workflow 2 | `business_name`, `business_email`, `business_phone`, `business_address`, onboarding steps |
| `Elevate - Renewal Reminder Email` | Workflow 3 | `contact.company_name`, `contract_end_date`, `book_strategy_link` |

### B0.5 Trigger Links (4)

| Trigger Link | Embed | Tag |
|---|---|---|
| `interested-seo` | Lead Nurture Email | `interested-seo` |
| `interested-ppc` | Lead Nurture Email | `interested-ppc` |
| `interested-social` | Lead Nurture Email | `interested-social` |
| `download-case-study` | Lead Nurture Email (CTA button) | `download-case-study` |

### B0.6 Calendars (2)

| Calendar | Type | Used By |
|---|---|---|
| `Elevate - Strategy Call` | **Round Robin** (Rachel + Derek), 30min, **Zoom connected** | Funnel Thank You, `book_strategy_link`, Workflow 4 trigger |
| `Elevate - Onboarding Kickoff` | Basic, 90min | Booked manually post-Closed Won |

> **Round-robin is included for real-world practice** — it's not a Part B exam task. If round-robin isn't available in your GHL plan, build Strategy Call as Basic and assign to one user.

### B0.7 Pipeline (1, 5 stages)

`Elevate - Client Acquisition Pipeline`:
1. **New Lead** — opportunity created here by **Workflow 1** (NOT by the form)
2. **Discovery Call Scheduled** — moved by Workflow 4 on Strategy Call booking
3. **Audit Delivered** — manual move
4. **Proposal Sent** — manual
5. **Closed Won** — triggers Workflow 2

### B0.8 Form (1)

`Elevate - Strategy Session Form`:

| Field | Required | Maps To |
|---|---|---|
| First Name | yes | `contact.first_name` |
| Last Name | yes | `contact.last_name` |
| Email | yes | `contact.email` |
| Phone | yes | `contact.phone` |
| Company Name | yes | `contact.company_name` |
| Website URL | yes | `website_url` |
| Industry | yes | `industry` |
| Lead Source | no | `lead_source` |

**Submit actions:**
1. Apply tag: `new-agency-lead`
2. Set `client_status` = "Prospect"

> Same fix as A0.8: form does not create opportunity. Workflow 1 does.

### B0.9 Funnel (1)

`Elevate - Free Strategy Session Funnel`:
1. Landing — embeds form, hero uses `offer_consultation`
2. Thank You — embeds Strategy Call calendar, sub-text uses `business_hours`

### B0.10 Workflows (5)

| # | Name | Trigger | Templates | Pipeline | Tags |
|---|---|---|---|---|---|
| 1 | `Elevate - New Lead Nurture` | Tag added: `new-agency-lead` | Lead Nurture Email + (optional) Lead Nurture SMS | **Creates opportunity** at "New Lead" | reads `strategy-call-booked` |
| 2 | `Elevate - Onboarding Activation` | Opp stage → Closed Won | Onboarding Kit Email | Sets `client_status` Onboarding → Active after 14d | adds `onboarding-client`, then `active-client` |
| 3 | `Elevate - Renewal Reminder` | Date: `contract_end_date` − 60 days | Renewal Reminder Email + (optional) Renewal Notice SMS | (no move) | adds `renewal-approaching` |
| 4 | `Elevate - Strategy Call Booked` | Calendar booking on Strategy Call | Strategy Call Confirmation Email + (optional) 24hr Reminder SMS | Move opp → "Discovery Call Scheduled" | adds `strategy-call-booked` |
| 5 | `Elevate - Monthly Report Notification` | Tag added: `monthly-report-ready` (manual or via scheduled trigger) | Custom inline email | (no move) | (entry tag only) |

### B0.11 Smart Lists (5)

| Smart List | Filter |
|---|---|
| Contracts Expiring 60d | `contract_end_date` between today and today+60d AND `client_status` = Active |
| High-Value Active | tag `active-client` AND `monthly_retainer` > 5000 |
| Rachel's Book of Business | `account_manager` = "Rachel (AM)" |
| High-Value Prospects | tag `new-agency-lead` AND `proposal_value` > 50000 |
| Win-Back Targets | `client_status` IN (Paused, Churned) OR tag `win-back` |

---

## B1 — Day 1: Settings + Custom Values

- Business Profile: Elevate Digital Agency, +14085554000, hello@elevateagency.com, 789 Marketing Blvd Suite 300 Springfield, Mon-Fri 9-6
- Custom Values: all 7 from B0.1, `book_strategy_link` placeholder until B4
- Sub-Account Users: Owner + Account Manager

**Done when:** profile complete, 7 custom values created, 2 users created.

---

## B2 — Day 2: Custom Fields + CSV + Smart Lists

- 10 custom fields in 3 folders per B0.2
- CSV `cert-prep/sample-data/elevate-clients.csv` imported, 15 contacts
- Verify Stephanie Chen: `service_package` = Full Stack, `monthly_retainer` = 9000, tags `active-client`, `high-value`
- TEST contact (your real email + phone)
- 5 Smart Lists per B0.11

**Done when:** all of the above verified.

---

## B3 — Day 3: Templates + Webchat

### B3.1 SMS Templates

**`Elevate - Lead Nurture SMS`**
```
Hi {{contact.first_name}}, this is {{custom_values.business_name}}. Following up on your strategy session interest — book a time: {{custom_values.book_strategy_link}}
```

**`Elevate - Strategy Call Reminder 24hr`**
```
Reminder: your strategy call with {{custom_values.business_name}} is tomorrow at {{appointment.start_time}}.
```

**`Elevate - Renewal Notice SMS`**
```
Hi {{contact.company_name}} team — your contract renews in 60 days. Let's chat: {{custom_values.book_strategy_link}}
```

### B3.2 Email Templates

**`Elevate - Lead Nurture Email`**
- Subject: `{{custom_values.offer_consultation}} — let's talk strategy`
- Body: `business_name`, `book_strategy_link` CTA
- Embeds 4 trigger links (B7 will create them; reserve placeholder text now)

**`Elevate - Strategy Call Confirmation Email`**
- Subject: `Confirmed — {{appointment.title}} with {{custom_values.business_name}}`
- Body: appointment details, what to prepare

**`Elevate - Onboarding Kit Email`**
- Subject: `Welcome to {{custom_values.business_name}} — your onboarding kit`
- Body: onboarding steps, `business_email`, `business_phone`, `business_address`

**`Elevate - Renewal Reminder Email`**
- Subject: `Your contract is up in 60 days — let's plan`
- Body: `contract_end_date` reference, `book_strategy_link` CTA

### B3.3 Webchat
- Greeting: "Talk to a Growth Strategist at {{custom_values.business_name}}"
- After-hours: "We're closed. Hours: {{custom_values.business_hours}}. Email {{custom_values.business_email}}"
- Pre-chat: Name, Email, Company Name, Service Interest

**Done when:** 3 SMS + 4 email templates created, webchat configured. Snapshot v1.

---

## B4 — Day 4: Calendars + Zoom

**`Elevate - Strategy Call`** — Round Robin (Rachel + Derek), 30 min, Mon-Fri 9-5, Zoom connected, booking form: Name, Email, Company Name, Website, Primary Goal

**`Elevate - Onboarding Kickoff`** — Basic, 90 min, Mon-Thu 10-4

**Test:** book Strategy Call as TEST → confirmation email contains Zoom link.

**Update `book_strategy_link`** to Strategy Call public URL.

**Done when:** 2 calendars created, Strategy Call has Zoom + test booking, `book_strategy_link` populated. Snapshot v2.

---

## B5 — Day 5: Pipeline + Opportunities

`Elevate - Client Acquisition Pipeline` (5 stages from B0.7).

| Contact | Stage | Value |
|---|---|---|
| Brian Williams | New Lead | $48,000 |
| Olivia Nguyen | Audit Delivered | $18,000 |
| Jason Park | Proposal Sent | $36,000 |
| Amanda Foster | Proposal Sent | $96,000 |
| Stephanie Chen | Closed Won | $108,000 |

**Done when:** pipeline + 5 opportunities. Snapshot v3.

---

## B6 — Day 6: Payments [real-world only]

**Products:** SEO Retainer $3,000/mo (recurring), PPC Management $4,000/mo (recurring), Social Media $2,000/mo (recurring), Brand Audit $1,500 (one-time).

**One invoice + coupon:** Brand Audit $1,500 invoice for NexaVision Media; coupon `PARTNER15` 15% off one-time products.

---

## B7 — Day 7: Trigger Links + Marketing

Create 4 trigger links from B0.5. Embed all 4 in `Elevate - Lead Nurture Email`. Test each → tag applied.

**Done when:** 4 trigger links created, all embedded, all tested. Snapshot v4.

---

## B8 — Day 8: Form + Funnel

Build form per B0.8 (NO opportunity action — workflow handles it). Test as TEST → tag + custom field set.

Build funnel: Landing (form embedded, hero uses `offer_consultation`) + Thank You (Strategy Call calendar embedded). Publish.

**Done when:** form + funnel published, full flow tested.

---

## B9 — Day 9: Workflows

### Workflow 1: `Elevate - New Lead Nurture`

**Trigger:** Tag added: `new-agency-lead`

**Actions:**
1. **Create Opportunity** in Client Acquisition Pipeline at "New Lead", value 0, name `{{contact.company_name}}`
2. Send Email: Lead Nurture Email
3. Wait: 2 days
4. If/Else: tag `strategy-call-booked`?
   - True: end
   - False: *(optional)* Send SMS Lead Nurture SMS, OR send a follow-up email
5. Wait: 5 days
6. If/Else: tag `download-case-study` OR `interested-seo` OR `interested-ppc` OR `interested-social`?
   - True: Internal Notification: "Engaged lead — {{contact.company_name}} — review trigger-link tags"
   - False: end

**Test, Published.**

### Workflow 2: `Elevate - Onboarding Activation`

**Trigger:** Opp stage → "Closed Won"

**Actions:**
1. Add tag: `onboarding-client`
2. Set `client_status` = "Onboarding"
3. Send Email: Onboarding Kit Email
4. Internal Notification: "{{contact.company_name}} signed — start onboarding"
5. Wait: 14 days
6. Add tag: `active-client`, remove `onboarding-client`
7. Set `client_status` = "Active"
8. Internal Notification: "{{contact.company_name}} now Active — start monthly cadence"

**Test, Published.**

### Workflow 3: `Elevate - Renewal Reminder`

**Trigger:** Date: `contract_end_date` − 60 days

**Actions:**
1. Add tag: `renewal-approaching`
2. Send Email: Renewal Reminder Email
3. *(Optional)* Send SMS: Renewal Notice SMS
4. Wait: 21 days
5. If/Else: tag `renewal-booked` (manual)?
   - True: end
   - False: Internal Notification: "Renewal not booked — {{contact.company_name}}"

**Test:** set TEST `contract_end_date` to today+60 days → trigger fires.

### Workflow 4: `Elevate - Strategy Call Booked`

**Trigger:** Calendar Booking → Strategy Call calendar

**Actions:**
1. Add tag: `strategy-call-booked`
2. Move opp → "Discovery Call Scheduled"
3. Send Email: Strategy Call Confirmation Email
4. Wait until: 24h before appointment
5. *(Optional)* Send SMS: Strategy Call Reminder 24hr
6. Internal Notification: "Strategy call tomorrow — {{contact.company_name}}"

**Test, Published.**

### Workflow 5: `Elevate - Monthly Report Notification`

**Trigger:** Tag added: `monthly-report-ready`

**Actions:**
1. Send custom inline email: "Your {{contact.company_name}} monthly report is ready" + link
2. Wait: 3 days
3. If/Else: appointment booked on Strategy Call in last 3 days?
   - True: end
   - False: Internal Notification: "{{contact.company_name}} hasn't booked review"

**Test, Published.**

**Done when:** all 5 workflows built, published, tested. Snapshot v5 + load drill.

---

## B10 — Day 10: Reputation + Reporting [real-world only]

### B10.1 Testimonial Process
When opportunity reaches "Active" for 90+ days, AM applies tag `testimonial-eligible` and emails permission request manually.

### B10.2 Weekly Reporting
| Check | Where |
|---|---|
| New leads this week | Smart List `new-agency-lead` |
| Strategy calls booked vs completed | Calendar dashboard |
| Active clients with retainers | Smart List "High-Value Active" |
| Contracts expiring 60d | Smart List "Contracts Expiring 60d" |
| Workflows still Published | Automation → Workflows |

**Done when:** processes documented. Snapshot v6.

---

## Snapshots Reference

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

Rule: never overwrite — always increment the version.

---

## Coherence Audit Checklist

Run at the end of each section:

For each item in A0 (or B0), verify:
- [ ] It is created in the day section it claims to be created in
- [ ] At least one downstream consumer actually references it
- [ ] If a custom field: a workflow, smart list, form, OR template merges/reads it
- [ ] If a custom value: at least one template body or funnel page contains it
- [ ] If a tag: something applies it AND something reads it
- [ ] If a template: a workflow references it by exact name
- [ ] If a trigger link: it's embedded in a real email
- [ ] If a calendar: a workflow has a trigger pointing at it OR it's embedded in a funnel
- [ ] If a pipeline stage: a workflow either creates or moves opportunities into it
- [ ] If a form: it's embedded in a funnel AND its submit actions are configured

---

## Bugs Fixed From The Old File

If you're comparing this file to the original `practical-brightsmile-elevate-full-build.md`:

1. **Forms creating opportunities** — removed. GHL forms don't have a "Create Opportunity" submit action. Workflow 1 (in both A and B) creates the opportunity, triggered by either the `new-patient-inquiry`/`new-agency-lead` tag or the Form Submitted trigger.

2. **SMS as default workflow action** — replaced with Send Email + Internal Notification. SMS sending requires A2P 10DLC approval (1-3 weeks, separate badge) and silently fails without it. SMS templates still exist (so you know the screen) and SMS actions are documented as **optional / A2P-dependent** add-ons in workflows 2, 3, 4 (BrightSmile) and 1, 3, 4 (Elevate).

3. **Custom field merge syntax confusion** — clarified to `{{contact.<field_key>}}` for contact custom fields, no `custom_field` namespace. Always use the editor's merge-tag dropdown rather than typing.

4. **`book_link` circular dependency** — explicit. Created Day 1 with placeholder URL, real URL pasted Day 4 after the calendar exists. Templates in Day 3 reference the placeholder; first real-link test happens after Day 4.

5. **Templates inline vs Marketing library** — workflows reference templates from Marketing → Templates. Building inline inside a workflow works but breaks reuse. All named templates here live in the Marketing library.

6. **Orphan assets** — removed templates and pipeline stages that nothing referenced (old "Renewal Email," "Proposal Follow-Up," "Newsletter," "Insurance Claims" pipeline, "Project Delivery" pipeline, "Monthly Review Call" calendar).

7. **Lower-priority sections marked clearly** — Payments (A6/B6), Reputation/Reporting (A10/B10), Webchat, Round-Robin calendars are flagged "real-world only," not Part B exam content. Skip them under exam time pressure.
