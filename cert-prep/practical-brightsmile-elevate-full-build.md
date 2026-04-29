# Phase 1 Practical (Full Build) — Part B Exam Prep
## Two Separate Sub-Accounts: BrightSmile Dental + Elevate Digital Agency

> **You have passed Part A.** This entire practical targets **Part B only** — the 1-hour live proctored session where you build a sub-account from scratch on screen.
>
> Telephony (A2P 10DLC, LC Phone, Twilio) is in the **A2P Compliance badge** — not tested in Part B. Ignore those topics here.

---

## How to Use This Practical

Build each section like a timed exam simulation. Do **BrightSmile first** — it builds the muscle memory. Elevate will go 30–40% faster because the navigation patterns are the same.

- **Section A:** BrightSmile Dental Clinic (build in the BrightSmile sub-account)
- **Section B:** Elevate Digital Agency (build in the Elevate sub-account)

### Time Estimates

| Build | First Time | After Drilling |
|---|---|---|
| BrightSmile full (Days 1–10) | 8–10 hrs | 3–4 hrs |
| Elevate full (Days 1–10) | 5–7 hrs | 2–3 hrs |
| Part B Drill (end of each section) | Target < 25 min | Must hit < 25 min to be exam-ready |

---

## Global Naming + Hygiene Rules (Do this first)

### Naming conventions
Use consistent prefixes so you can find things fast:
- **BrightSmile assets:** `BrightSmile - ...`
- **Elevate assets:** `Elevate - ...`
- **Tags:** lowercase + hyphens, e.g. `new-patient-inquiry`, `new-agency-lead`

### Test data rules
- Keep at least 1 permanent test contact per sub-account: `TEST - Do Not Delete`
- Use realistic E.164 phone numbers for testing
- Sample CSV data is in `cert-prep/sample-data/` — import during Day 2 of each build

---

## Section 0 — Agency Account: Full Walkthrough

> **Do this entire section before touching Section A or B.** Everything in GHL starts at the agency level. You have only worked in sub-accounts before — this section teaches you the agency layer that wraps around them.
>
> Part B tests BOTH agency-level AND sub-account-level navigation. Mixing them up under pressure is the #4 reason people fail.

---

### 0.1 Understanding the Two Levels

GHL has two completely separate levels. They have different left-nav menus, different settings panels, and different purposes:

| | Agency Level | Sub-Account Level |
|---|---|---|
| **What it is** | Your management dashboard | One client's workspace |
| **Who works here** | You (the agency admin) | The client's staff |
| **Left nav shows** | Accounts, Snapshots, SaaS tools | Contacts, Workflows, Calendars, etc. |
| **Settings icon opens** | Agency-wide config | That client's business settings |
| **URL pattern** | `.../agency/...` | `.../location/...` |
| **How to get here** | Log in → you land here | Click your agency name → pick a sub-account |

**The critical habit:** Always glance at the top-left corner before clicking anything. It shows which level you are in. If it shows your agency name, you are at agency level. If it shows a client name, you are inside that sub-account.

---

### 0.2 Agency Dashboard Tour — Do This First

Log in now and explore the **Agency view** left sidebar:

| Left Nav Item | What It Is |
|---|---|
| **Dashboard** | Summary stats across all sub-accounts (conversations, leads, revenue) |
| **Accounts** (or Sub-Accounts) | List of all client sub-accounts — this is where you create and manage them |
| **Snapshots** | Saved configuration packages you can deploy to sub-accounts |
| **Templates** | Agency-level shared templates (optional; sub-accounts have their own too) |
| **Media** | Agency-level media library |
| **Marketplace** | GHL apps and integrations |
| **Settings** (gear icon) | Agency-wide settings — company info, team, billing |
| **SaaS Configurator** | Pricing plans and rebilling (SaaS plans only — not relevant for Part B) |

**Do this now:**
- [ ] Find the Accounts list — count your existing sub-accounts
- [ ] Find Snapshots — note if any exist already
- [ ] Open Agency Settings (gear icon) → find Company Info — verify your agency name

---

### 0.3 Agency Settings — What's Inside

Click the **gear icon (Settings)** while in Agency view. This is the AGENCY settings panel, not a sub-account's settings:

| Section | What You'll Find |
|---|---|
| **Company** | Agency name, address, logo, timezone |
| **Team** | Agency-level staff members (your employees, not client staff) |
| **Email Services** | Default email sending setup for the agency |
| **Integrations** | Stripe, PayPal, Facebook, etc. at agency level |
| **API Keys** | Developer access |
| **White Label** | Custom domain/branding for your agency |
| **Billing** | Your GHL subscription |

**Agency Team vs Sub-Account Team — this confuses everyone:**

- **Agency Team** (here in Agency Settings): Your employees who manage the agency. They can access all sub-accounts. Example: your VA, account manager, yourself.
- **Sub-Account Team** (inside a sub-account → Settings → Team): The client's staff. They can ONLY see that one sub-account. Example: dental receptionist, front desk.

When you create a Dentist or Front Desk user in Day 1, you do that **inside the sub-account**, not here.

**Checklist:**
- [ ] Agency Company Info complete (name, address, timezone)
- [ ] 2FA enabled for your agency admin account
- [ ] You understand the difference between Agency Team and Sub-Account Team

---

### 0.4 Creating Sub-Accounts — Step by Step

From **Agency view** (confirm you are NOT inside a sub-account):

**Step 1:** Click **"Accounts"** in the left sidebar. You see a list of existing sub-accounts.

**Step 2:** Click **"+ New Sub-Account"** or **"+ Create Sub-Account"** (button in top-right area).

**Step 3:** Fill in the sub-account details:
- **Business Name:** `BrightSmile Dental Clinic`
- **Address / City / State / Zip**
- **Timezone:** Your local timezone
- **Phone:** Optional — can be added later inside the sub-account
- **Email:** Optional — can be added later
- **Snapshot to Load:** Leave blank for now (we will set this up fresh)

**Step 4:** Click **Save** (or Create / Continue).

**Step 5:** Verify the sub-account appears in your Accounts list.

**Step 6:** Click into the new sub-account. You should now see the **sub-account dashboard** — the left nav completely changes (shows Contacts, Conversations, Calendars, etc.). This is the client's workspace.

**Step 7:** Return to Agency view (click the sub-account name top-left → pick your agency).

**Repeat for Elevate Digital Agency.**

**Checklist:**
- [ ] "BrightSmile Dental Clinic" sub-account created
- [ ] "Elevate Digital Agency" sub-account created
- [ ] Both appear in the Accounts list
- [ ] You entered each one and confirmed the sub-account dashboard loaded
- [ ] You successfully returned to Agency view from each one

---

### 0.5 Snapshots — Create + Load (Step by Step)

Snapshots let you save the entire configuration of a sub-account and replicate it. This is confirmed Part B content. Practice until it takes under 3 minutes.

**What a snapshot can contain:**
- Workflows
- Funnels and websites
- Calendars
- Email and SMS templates
- Custom values
- Forms and surveys
- Pipelines
- Tags

**Creating a Snapshot from a Sub-Account:**

1. Switch to **Agency view** (click sub-account name top-left → pick agency)
2. Click **"Snapshots"** in the left sidebar
3. Click **"+ New Snapshot"** or **"Create Snapshot"**
4. **Select the source sub-account** from the dropdown (e.g. BrightSmile)
5. **Select what to include** — check all boxes for a full snapshot, or be selective
6. **Name it:** `Snapshot - BrightSmile - v1 Foundation (Day 3)`
7. Click **Save / Create**
8. Snapshot appears in your Snapshots list

Alternative path (from inside the sub-account, if available in your GHL version):
- Settings → Snapshots → Create Snapshot → name it → Save

**Loading a Snapshot into a Sub-Account:**

1. Switch to **Agency view**
2. Click **"Snapshots"** in the left sidebar
3. Find the snapshot → click the **three-dot menu (⋮)** → **"Push to Account"** or **"Load"**
4. **Select the target sub-account** from the dropdown
5. Choose merge behavior:
   - **"Add / Merge"** — adds assets without deleting what's already there ✓ (use this)
   - **"Replace"** — overwrites everything (use with caution)
6. Click **Load** (or Push / Apply)
7. Enter the target sub-account and verify the assets appeared (check Workflows, Funnels, etc.)

**Practice drill — do this before starting Section A:**
- [ ] Create a snapshot from ANY sub-account (even an empty one) — just to practice the flow
- [ ] Load it into a DIFFERENT sub-account (create a temp "practice" sub-account if needed)
- [ ] Verify it loaded
- [ ] Time yourself: target < 3 minutes total for both steps combined

**Rule:** Never overwrite a snapshot. Always create a new version number.

---

### 0.6 Agency-Level Navigation Speed Drill

Do this 5 times before starting Section A. Time yourself — target < 30 seconds per step:

1. Start at Agency view → open Agency Settings → click Company
2. Enter BrightSmile sub-account → open Sub-Account Settings → click Business Info
3. Return to Agency view → click Snapshots
4. Enter Elevate sub-account → click Workflows in left nav
5. Return to Agency view → click Accounts list

If any of those steps took you more than 10 seconds to find, that is your drilling target.

---

### 0.7 Agency Context: What You Do at Each Level

Use this as your reference throughout Sections A and B:

| Task | Level | Where |
|---|---|---|
| Create sub-account | Agency | Accounts → + New |
| Create/load snapshot | Agency | Snapshots |
| Agency billing/settings | Agency | Settings (gear) |
| Add agency team member | Agency | Settings → Team |
| Sub-account business profile | Sub-account | Settings → Business Info |
| Custom values | Sub-account | Settings → Custom Values |
| Sub-account team/users | Sub-account | Settings → Team |
| Contacts, CRM | Sub-account | Contacts menu |
| Workflows | Sub-account | Automation → Workflows |
| Calendars | Sub-account | Calendars menu |
| Funnels/Sites | Sub-account | Sites menu |
| Templates | Sub-account | Marketing → Templates |
| Pipelines | Sub-account | Opportunities menu |
| Payments | Sub-account | Payments menu |

**Bottom line:** You are in Agency view only to create/manage sub-accounts and snapshots. Everything else is inside the sub-account.

---

---

# Section A — BrightSmile Dental Clinic

Build everything below inside the **BrightSmile Dental Clinic** sub-account.

---

## A1 — Day 1: Dashboard & Settings

### A1.1 Business Profile
- Business Name: BrightSmile Dental Clinic
- Address: 456 Smile Avenue, Springfield
- Hours: Mon-Thu 8AM-5PM, Fri 8AM-2PM, Sat-Sun Closed
- Category: Healthcare / Dental
- Timezone: set correctly for your region

**Custom Values (create all of these):**
- `{{business.name}}` = BrightSmile Dental Clinic
- `{{business.phone}}` = (placeholder)
- `{{business.email}}` = smile@brightsmile.com
- `{{business.address}}` = 456 Smile Avenue, Springfield
- `{{business.hours}}` = Mon-Thu 8AM-5PM, Fri 8AM-2PM
- `{{offer.new_patient}}` = Free Dental Exam & X-Rays for New Patients
- `{{offer.whitening}}` = 50% Off Professional Whitening - Limited Time
- `{{offer.referral}}` = Refer a Friend, Both Get $50 Off Next Visit

> Custom values are how you avoid hardcoded text in templates and workflows. On the exam you may be asked to use them inside a workflow or template — know where to create and reference them.

### A1.2 Users + Permissions

| Role | Contacts | Conversations | Appointments | Pipeline | Payments | Settings |
|------|----------|--------------|--------------|----------|----------|----------|
| Dentist | Assigned | Assigned | Own schedule | View only | No | No |
| Hygienist | Assigned | No | Own schedule | No | No | No |
| Front Desk | All | All | All schedules | View only | View only | No |
| Admin/Owner | All | All | All | Full | Full | Full |

Create at least: Admin + Front Desk (minimum 2 users).

**Definition of Done (Day 1):**
- [ ] Business Profile complete with correct hours and timezone
- [ ] All custom values created
- [ ] At least 2 users created with correct permission levels
- [ ] "Only Assigned Data" setting matches the table above

> **Agency Context — Day 1:** The BrightSmile sub-account exists because you created it from Agency view (Section 0.4). Everything you just did (business profile, custom values, users) was done INSIDE the sub-account. If you accidentally ended up in Agency Settings instead of Sub-Account Settings at any point, that's the #4 Part B failure mode — notice it now so you catch it under pressure.

---

## A2 — Day 2: Contacts & CRM

### A2.1 Custom Fields

**Folder: Patient Info**
- Patient Type (Dropdown: New Patient, Returning, Referred, Emergency)
- Last Visit Date (Date)
- Next Appointment Type (Dropdown: Cleaning, Filling, Crown, Root Canal, Whitening, Veneer Consultation, Orthodontic Check, Emergency)
- Preferred Dentist (Dropdown: Dr. Sarah Kim, Dr. James Okafor)
- Visit Frequency (Dropdown: Every 6 Months, Quarterly, As Needed)

**Folder: Insurance & Billing**
- Insurance Provider (Dropdown: Aetna, BlueCross, Cigna, Delta Dental, MetLife, United, Self-Pay, Other)
- Insurance ID (Text)
- Coverage Level (Dropdown: Basic, Standard, Premium, None)
- Payment Plan Active (Checkbox)
- Outstanding Balance (Number)

**Folder: Treatment Plan**
- Active Treatment (Dropdown: None, Whitening Series, Invisalign, Crown Prep, Implant Process)
- Treatment Stage (Dropdown: Consultation, In Progress, Follow-Up, Completed)
- Treatment Value (Number)
- Medical Alerts (Textarea)

### A2.2 Import Sample Data
- Import `cert-prep/sample-data/brightsmile-patients.csv`
- During import, map each column to the matching GHL field
- Verify 15 contacts appear with correct tags and field values after import

### A2.3 Smart Lists (create all 5)
- **Overdue for Cleaning** — Last Visit Date > 6 months ago + Visit Frequency = Every 6 Months
- **Active Treatment - Follow-Up Needed** — Active Treatment ≠ None + Treatment Stage = In Progress
- **Self-Pay Patients** — Insurance Provider = Self-Pay
- **Dr. Kim's Patients** — Preferred Dentist = Dr. Sarah Kim
- **Outstanding Balance** — Outstanding Balance > 0

**Definition of Done (Day 2):**
- [ ] Custom fields created in correct folders
- [ ] 15+ patient contacts imported with correct field mapping
- [ ] All 5 Smart Lists return expected records
- [ ] `TEST - Do Not Delete` contact created manually

---

## A3 — Day 3: Conversations & Templates

### A3.1 Templates

**SMS Templates (create all 5)**
- `BrightSmile - Appointment Reminder 48hr` — includes `{{appointment.title}}`, `{{appointment.start_time}}`
- `BrightSmile - Appointment Reminder 24hr` — shorter version, day-before tone
- `BrightSmile - Post-Procedure Care` — includes `{{contact.first_name}}`, `{{business.phone}}`
- `BrightSmile - 6-Month Recall Notice` — uses `{{offer.new_patient}}` custom value
- `BrightSmile - Insurance Follow-Up` — requests insurance info before upcoming visit

**Email Templates (create all 3)**
- `BrightSmile - Welcome to BrightSmile` — onboarding email with office hours and what to bring
- `BrightSmile - Post-Visit Summary` — follow-up after appointment
- `BrightSmile - Referral Request` — uses `{{offer.referral}}` custom value

### A3.2 Webchat Widget
- Greeting: "Welcome to BrightSmile! How can we help?"
- After-hours message: "We're currently closed. Leave your info and we'll call you back."
- Pre-chat form includes: Name, Email, Phone, Reason for inquiry (dropdown)
- Dental disclaimer: "This chat is for scheduling and general inquiries only. Do not share medical information here."

> **Note on Telephony:** SMS template creation (above) is all you need for the base Admin cert. A2P 10DLC registration, LC Phone provisioning, and Twilio setup are in the **A2P Compliance Badge** — not tested in Part B.

**Definition of Done (Day 3):**
- [ ] 5 SMS templates created and use correct merge fields
- [ ] 3 email templates created
- [ ] Webchat widget configured and embedded
- [ ] Snapshot: `Snapshot - BrightSmile - v1 Foundation (Day 3)`

> **Agency Step — Create Snapshot v1:**
> 1. Click the sub-account name (top-left) → select your agency to return to Agency view
> 2. Click **Snapshots** in the left sidebar
> 3. Click **+ New Snapshot**
> 4. Source sub-account: **BrightSmile Dental Clinic**
> 5. Select all assets (custom values, templates, settings)
> 6. Name: `Snapshot - BrightSmile - v1 Foundation (Day 3)`
> 7. Click Save
> 8. Return to BrightSmile sub-account (Accounts → BrightSmile)
>
> Target time: < 3 minutes. If it takes longer, re-read Section 0.5.

---

## A4 — Day 4: Calendars + Integrations

> **Calendar + Zoom/Google Meet integration is the #1 confirmed Part B task and the most common failure point.** Practice this until you can do it in under 5 minutes.

### A4.1 Calendars (create all 4)

**General Checkup (Basic Calendar)**
- Duration: 60 min
- Buffer: 10 min after
- Availability: Mon-Thu 8AM-5PM, Fri 8AM-2PM
- Booking form fields: Name, Email, Phone, Insurance Provider, Reason for Visit
- Confirmation message: uses `{{business.name}}` custom value

**Cosmetic Consultation (Basic Calendar)**
- Duration: 45 min
- Buffer: 15 min after
- Availability: Mon-Thu 9AM-4PM
- Booking form: Name, Email, Phone, Area of Interest (Whitening/Veneers/Orthodontics)

**Emergency Dental (Basic Calendar)**
- Duration: 30 min
- Buffer: 5 min after
- Availability: Mon-Fri 8AM-5PM, same-day only (set advance booking to 0 days)
- Booking form: Name, Email, Phone, Brief Description of Emergency

**Hygienist Cleaning (Round Robin)**
- Duration: 45 min
- Assign to: Front Desk user (simulate 2 hygienists for round-robin)
- Availability: Mon-Fri 8AM-5PM

### A4.2 Zoom / Google Meet Integration (DRILL THIS)

For the **General Checkup** calendar:
1. Go to Calendar Settings → Connections
2. Connect your Zoom account (or Google Calendar → Google Meet)
3. Set meeting location to: **Zoom** (or Google Meet)
4. Test: book an appointment through the calendar link
5. Verify: the booking confirmation email contains a Zoom/Meet link

**Drill checklist — do this until it takes < 5 minutes:**
- [ ] Connect Zoom (or Google Meet) to the calendar
- [ ] Book a test appointment
- [ ] Open the confirmation — meeting link is present
- [ ] Check the calendar event — link is visible

**Definition of Done (Day 4):**
- [ ] All 4 calendars created with correct durations and buffers
- [ ] At least 1 calendar connected to Zoom or Google Meet
- [ ] Test booking confirmed with meeting link in email
- [ ] Booking forms contain the described fields
- [ ] Snapshot: `Snapshot - BrightSmile - v2 Calendars (Day 4)`

---

## A5 — Day 5: Opportunities & Pipelines

### A5.1 Patient Treatment Pipeline (8 stages)
1. New Patient Inquiry
2. Consultation Scheduled
3. Consultation Completed
4. Treatment Proposed
5. Treatment Accepted
6. Treatment In Progress
7. Treatment Completed
8. Follow-Up / Recall Scheduled

### A5.2 Insurance Claims Tracking Pipeline (5 stages)
1. Claim Submitted
2. Claim Under Review
3. Additional Info Required
4. Approved / Partially Approved
5. Claim Closed

Create 5 sample opportunities across the Patient Treatment Pipeline with realistic values and notes. Use the imported contacts.

**Definition of Done (Day 5):**
- [ ] Both pipelines created with all stages
- [ ] 5+ opportunities created with values and notes
- [ ] Snapshot: `Snapshot - BrightSmile - v3 Pipelines (Day 5)`

> **Agency Step — Create Snapshot v3:**
> Agency view → Snapshots → + New Snapshot → source: BrightSmile → name: `Snapshot - BrightSmile - v3 Pipelines (Day 5)` → Save → return to BrightSmile sub-account.
>
> You should now be doing this in under 2 minutes. If not, you need more snapshot reps.

---

## A6 — Day 6: Payments

### A6.1 Products

| Product | Price | Type |
|---|---|---|
| Dental Exam | $200 | One-time |
| Professional Cleaning | $150 | One-time |
| Teeth Whitening Package | $450 | One-time |
| Crown / Cap | $1,200 | One-time |
| Emergency Visit | $300 | One-time |

### A6.2 Invoices
- **Whitening Invoice:** Teeth Whitening Package ($450) + insurance adjustment line item (negative amount)
- **Payment Plan Concept:** Orthodontics $375/mo × 12 — create as a recurring invoice or document the setup approach

**Definition of Done (Day 6):**
- [ ] 5 products created with correct billing types
- [ ] Whitening invoice created with negative line item for insurance adjustment
- [ ] Payment plan approach documented or built

---

## A7 — Day 7: Marketing (Email + Trigger Links)

### A7.1 Email Templates for Campaigns (create 4)
- `BrightSmile - New Patient Welcome` — full onboarding sequence email
- `BrightSmile - Cleaning Recall Reminder` — includes trigger link `clicked-book-cleaning`
- `BrightSmile - Post-Procedure Care Instructions` — detailed aftercare
- `BrightSmile - Referral Request` — uses `{{offer.referral}}`

### A7.2 Trigger Links (create 2)
- `interested-whitening` — clicking applies tag `interested-whitening`
- `interested-orthodontics` — clicking applies tag `interested-orthodontics`

### A7.3 Campaign
- Create a campaign: "BrightSmile - Cleaning Recall"
- Target list: "Overdue for Cleaning" Smart List
- First email: `BrightSmile - Cleaning Recall Reminder`

**Definition of Done (Day 7):**
- [ ] 4 email templates created
- [ ] 2 trigger links created and tested (click → verify tag applied)
- [ ] 1 campaign drafted targeting the Smart List
- [ ] Snapshot: `Snapshot - BrightSmile - v4 Marketing (Day 7)`

> **Agency Step — Create Snapshot v4:**
> Agency view → Snapshots → + New Snapshot → source: BrightSmile → name: `Snapshot - BrightSmile - v4 Marketing (Day 7)` → Save → return to sub-account.

---

## A8 — Day 8: Sites (Funnels), Forms, Surveys

### A8.1 Funnel: Free Dental Exam (2 steps)
**Step 1 — Landing Page:**
- Headline: "Claim Your Free Dental Exam & X-Rays"
- Sub-headline uses `{{offer.new_patient}}`
- Intake form embedded (see A8.2)
- CTA button: "Book My Free Exam"

**Step 2 — Thank You Page:**
- Confirmation message + next steps
- Calendar widget: General Checkup calendar embedded
- "What to Bring" section

### A8.2 Intake Form
Required fields:
- First Name (required)
- Last Name (required)
- Email (required)
- Phone (required)
- Date of Birth (required)
- Insurance Provider (maps to custom field)
- Reason for Visit (text)
- How did you hear about us? (dropdown)

Field mapping: each form field maps to the correct contact field or custom field.

### A8.3 Survey: Patient Needs Assessment (conditional)
- Page 1: "What brings you in today?" (options: Routine Check, Cosmetic, Orthodontics, Pain/Emergency, Other)
- Page 2A (if Cosmetic selected): Whitening interest, Veneers interest
- Page 2B (if Orthodontics selected): Age range, previous ortho work
- Page 2C (if Pain/Emergency): Symptom description, urgency

On submit → Workflow applies tags:
- `needs-cosmetic`, `needs-orthodontics`, `needs-emergency` (based on answers)
- Creates opportunity in Patient Treatment Pipeline at "New Patient Inquiry"

**Definition of Done (Day 8):**
- [ ] 2-step funnel built and published
- [ ] Intake form embedded on landing page and field mapping verified
- [ ] Survey built with conditional pages
- [ ] Submit survey with test contact → verify tags applied + opportunity created

---

## A9 — Day 9: Automation & Workflows

> More workflows = more Part B reps. Build all 4. The exam may ask you to build any combination of these.

### Workflow 1: BrightSmile - New Patient Inquiry
**Trigger:** Form submitted (BrightSmile intake form) OR tag added: `new-patient-inquiry`
**Actions:**
1. Add tag: `new-patient-inquiry`
2. Send SMS: `BrightSmile - Appointment Reminder 48hr` (as immediate confirmation)
3. Send Email: `BrightSmile - Welcome to BrightSmile`
4. Create opportunity in Patient Treatment Pipeline → Stage: "New Patient Inquiry"
5. Wait: 24 hours
6. Internal notification to Front Desk: "New patient inquiry from {{contact.first_name}} — no appointment booked yet"
7. If no appointment booked (IF/ELSE): Send SMS follow-up

**Test checklist:**
- [ ] Trigger fires on form submit
- [ ] Tags applied correctly
- [ ] SMS and email sent
- [ ] Opportunity created in correct pipeline stage
- [ ] Internal notification received
- [ ] Workflow status shows "Published"

### Workflow 2: BrightSmile - Appointment Reminder
**Trigger:** Appointment booked (any calendar)
**Actions:**
1. Add tag: `appointment-scheduled`
2. Wait until: 48 hours before appointment
3. Send SMS: `BrightSmile - Appointment Reminder 48hr`
4. Wait until: 24 hours before appointment
5. Send SMS: `BrightSmile - Appointment Reminder 24hr`
6. Send Email: appointment summary with location and what to bring

**Test checklist:**
- [ ] Triggers on calendar booking
- [ ] Both SMS reminders queued at correct intervals
- [ ] Email confirmation sent
- [ ] Workflow status shows "Published"

### Workflow 3: BrightSmile - No-Show Recovery
**Trigger:** Appointment status changed to "No Show"
**Actions:**
1. Add tag: `no-show`
2. Remove tag: `appointment-scheduled`
3. Wait: 2 hours
4. Send SMS: "Hi {{contact.first_name}}, we missed you today! Reply to reschedule."
5. Wait: 3 days (if no reply/booking)
6. Send Email: reschedule offer
7. Internal notification to Front Desk: "No-show recovery — {{contact.first_name}}"
8. Move opportunity to "Follow-Up / Recall Scheduled" stage

**Test checklist:**
- [ ] Trigger fires when appointment marked No Show
- [ ] Tags updated correctly
- [ ] SMS and email sent in sequence
- [ ] Internal notification received
- [ ] Workflow status shows "Published"

### Workflow 4: BrightSmile - Post-Visit Review Request
**Trigger:** Appointment status changed to "Showed" / Completed
**Actions:**
1. Add tag: `visit-completed`
2. Remove tag: `appointment-scheduled`
3. Wait: 3 hours
4. Send SMS: "Thank you for visiting BrightSmile! How was your experience? Leave us a review: [review link]"
5. Wait: 48 hours (if no review)
6. Send Email: `BrightSmile - Post-Visit Summary` + review request
7. Move opportunity to next stage (Treatment Completed or Follow-Up)

**Test checklist:**
- [ ] Trigger fires on appointment marked Showed
- [ ] 3-hour wait observed before SMS
- [ ] Email sent 48 hours later
- [ ] Opportunity moves to correct stage
- [ ] Workflow status shows "Published"

**Definition of Done (Day 9):**
- [ ] All 4 workflows created and **Published** (verify the toggle, not just saved)
- [ ] Each workflow tested with `TEST - Do Not Delete` contact
- [ ] Each test checklist above completed
- [ ] Snapshot: `Snapshot - BrightSmile - v5 Workflows (Day 9)`

> **Agency Step — Create Snapshot v5:**
> Agency view → Snapshots → + New Snapshot → source: BrightSmile → name: `Snapshot - BrightSmile - v5 Workflows (Day 9)` → Save → return to sub-account.
>
> **Extra practice:** After saving, load this snapshot into a blank test sub-account and verify the workflows appear there. This is the exact Part B snapshot task. (Delete the test sub-account or leave it for drilling.)

---

## A10 — Day 10: Reputation, Community, Reporting

### A10.1 Reputation
- Workflow 4 (above) handles the post-visit review request — verify it's set up
- Review response templates:
  - 5-star: enthusiastic thank-you + share request
  - 3–4 star: thank-you + invitation to discuss
  - 1–2 star: apology + direct contact offer

### A10.2 Community: "Dental Health Hub"
- Create the community
- Groups: General Discussion, Oral Health Tips, Treatment Questions, Patient Success Stories
- 2 sample posts in the General Discussion group

### A10.3 Weekly Reporting Checklist (BrightSmile)
- [ ] New contacts this week vs last week
- [ ] Appointments booked vs completed vs no-show rate
- [ ] Outstanding balances > $100
- [ ] Review rating average
- [ ] Smart List: Outstanding Balance — any new entries?

**Definition of Done (Day 10):**
- [ ] Review response templates created (all 3 tiers)
- [ ] Community created with groups + 2 sample posts
- [ ] Weekly reporting checklist documented
- [ ] Snapshot: `Snapshot - BrightSmile - v6 Complete (Day 10)`

> **Agency Step — Final Snapshot + Agency-Level Review:**
>
> **Create the final snapshot:**
> Agency view → Snapshots → + New Snapshot → source: BrightSmile → name: `Snapshot - BrightSmile - v6 Complete (Day 10)` → include ALL assets → Save.
>
> **Agency-level reporting review (do this once per build):**
> While in Agency view, explore what visibility you have across sub-accounts:
> 1. **Agency Dashboard** — check the overview stats (conversations, leads, appointments, revenue across all sub-accounts)
> 2. **Accounts list** — find BrightSmile → click the three-dot menu (⋮) → explore: Edit, Pause, View Reports
> 3. **Sub-account reporting** — enter BrightSmile → Reporting menu (left nav) → explore Attribution Report, Call Reporting, Appointment Report
> 4. Return to Agency view
>
> Understanding this switch (agency-level overview vs sub-account-level detail) is often tested in Part B.

---

## A-Scorecard — Self-Grade BrightSmile (0–5 each)

| Category | Score |
|---|---:|
| Day 1 — Settings + custom values + users | |
| Day 2 — CRM (fields, import, smart lists) | |
| Day 3 — Templates + webchat | |
| Day 4 — Calendars + Zoom/Meet integration | |
| Day 5 — Pipelines + opportunities | |
| Day 6 — Payments + invoices | |
| Day 7 — Marketing + trigger links | |
| Day 8 — Funnels + forms + surveys | |
| Day 9 — Workflows (4 built, tested, published) | |
| Day 10 — Reputation + community + reporting | |
| **Part B Speed** — Can complete core tasks in < 25 min? | |

**Target: 40+/50 on content + "Yes" on speed.**

---

## A — Part B Timed Drill (30 minutes)

> This replaces "study" — do it repeatedly until you hit the target time.

**Setup:** Use a fresh/blank sub-account (not the BrightSmile build — a separate test sub-account). Set a 30-minute timer.

**Build the following from scratch:**
1. Business profile + 3 custom values (target: < 5 min)
2. 1 contact added manually with tags (target: < 2 min)
3. 1 pipeline with 3 stages + 1 opportunity for the contact (target: < 5 min)
4. 1 calendar connected to Zoom or Google Meet + test booking (target: < 7 min)
5. 1 workflow: "New Inquiry" trigger → SMS → internal notification → Published (target: < 8 min)
6. 1 snapshot from the Agency view (target: < 3 min)

**Scoring:**
| Time | Result |
|---|---|
| < 25 minutes | Exam-ready |
| 25–40 minutes | Borderline — drill the slowest step |
| > 40 minutes | Not ready — identify what slowed you and drill it 5× in isolation |

**After each drill:** Note which step took longest. That's your next drill target.

---

---

# Section B — Elevate Digital Agency

Build everything below inside the **Elevate Digital Agency** sub-account.

---

## B1 — Day 1: Dashboard & Settings

### B1.1 Business Profile
- Business Name: Elevate Digital Agency
- Address: 789 Marketing Blvd, Suite 300, Springfield
- Hours: Mon-Fri 9AM-6PM
- Category: Professional Services / Marketing
- Timezone: set correctly for your region

**Custom Values (create all of these):**
- `{{business.name}}` = Elevate Digital Agency
- `{{business.phone}}` = (placeholder)
- `{{business.email}}` = hello@elevateagency.com
- `{{business.address}}` = 789 Marketing Blvd, Suite 300, Springfield
- `{{business.hours}}` = Mon-Fri 9AM-6PM
- `{{offer.audit}}` = Free Website & SEO Audit
- `{{offer.consultation}}` = Free 30-Minute Strategy Session
- `{{onboarding.link}}` = (placeholder)
- `{{offer.retainer_discount}}` = 15% Off First 3 Months for Annual Contracts

### B1.2 Users + Permissions

| Role | Contacts | Conversations | Appointments | Pipeline | Reporting | Settings |
|------|----------|--------------|--------------|----------|-----------|----------|
| Account Manager | Assigned clients | Assigned | Own | Assigned | Assigned clients | No |
| Specialist | Assigned tasks only | No | No | No | No | No |
| Project Manager | All | All | All | All | All | No |
| Agency Owner | All | All | All | All | All | Full |

Create at least: Agency Owner + Account Manager.

**Definition of Done (Day 1):**
- [ ] Business Profile complete with correct hours and timezone
- [ ] All custom values created
- [ ] At least 2 users created with correct permission levels

> **Agency Context — Day 1:** You created this sub-account from Agency view (Section 0.4) before starting. "Agency Owner" in this table refers to a sub-account-level user role (someone who owns this client's workspace), not your agency-level admin. They are created here inside the sub-account → Settings → Team, not in Agency Settings → Team.

---

## B2 — Day 2: Contacts & CRM

### B2.1 Custom Fields

**Folder: Client Account**
- Service Package (Dropdown: SEO Only, PPC Only, Social Media, Full Stack (SEO+PPC+Social), Email Marketing, Web Design)
- Monthly Retainer (Number)
- Contract Start Date (Date)
- Contract End Date (Date)
- Account Manager (Dropdown: Rachel (AM), Derek (AM), Unassigned)
- Client Status (Dropdown: Prospect, Onboarding, Active, Paused, Churned)

**Folder: Business Profile**
- Industry (Dropdown: Healthcare, Real Estate, Legal, E-Commerce, Restaurant, SaaS, Other)
- Company Size (Dropdown: 1-10, 11-50, 51-200, 200+)
- Annual Revenue (Dropdown: Under $500K, $500K-$1M, $1M-$5M, $5M+)
- Website URL (Text)
- Current Marketing Spend (Number)

**Folder: Performance & Pipeline**
- Lead Source (Dropdown: Inbound (Website), Referral, Cold Outreach, Networking Event, LinkedIn)
- Proposal Value (Number)
- Pipeline Stage (Dropdown: Discovery Call, Audit Delivered, Proposal Sent, Negotiation, Closed Won, Closed Lost)
- Upsell Opportunity (Multi-Select: Add SEO, Add PPC, Add Social, Increase Retainer, Add Email, Web Redesign)

### B2.2 Import Sample Data
- Import `cert-prep/sample-data/elevate-clients.csv`
- Map each column to the matching GHL field during import
- Verify 15 contacts appear with correct tags and company names

### B2.3 Smart Lists (create all 5)
- **Contracts Expiring in 60 Days** — Contract End Date within 60 days + Client Status = Active
- **Upsell Opportunities** — Upsell Opportunity field is not empty
- **Rachel's Book of Business** — Account Manager = Rachel (AM)
- **High-Value Prospects** — Client Status = Prospect + Proposal Value > $40,000
- **Churned - Win-Back Targets** — Client Status = Churned

**Definition of Done (Day 2):**
- [ ] Custom fields created in correct folders
- [ ] 15+ contacts imported with correct field mapping
- [ ] All 5 Smart Lists return expected records
- [ ] `TEST - Do Not Delete` contact created manually

---

## B3 — Day 3: Conversations & Templates

### B3.1 Templates

**SMS Templates (create all 5)**
- `Elevate - Onboarding Welcome` — includes `{{contact.first_name}}`, `{{onboarding.link}}`
- `Elevate - Strategy Call Reminder 24hr` — includes `{{appointment.start_time}}`
- `Elevate - Monthly Report Ready` — "Your [Month] report is live. Reply to book a review call."
- `Elevate - Contract Renewal Notice` — uses `{{offer.retainer_discount}}`
- `Elevate - Follow-Up After Audit` — audit delivered, next step is proposal call

**Email Templates (create all 3)**
- `Elevate - Client Onboarding Kit` — welcome email with onboarding steps, tools access, team intro
- `Elevate - Monthly Performance Report` — uses `{{contact.company_name}}`, placeholder for report link
- `Elevate - Proposal Follow-Up` — references `{{offer.retainer_discount}}`

### B3.2 Webchat Widget
- B2B tone: "Talk to a Growth Strategist"
- After-hours: "We're out of office. Leave your details and we'll connect within 1 business day."
- Pre-chat form: Name, Email, Company Name, Service Interest (dropdown), Monthly Budget (dropdown)

> **Note on Telephony:** SMS templates above are all you need for the base Admin cert. A2P 10DLC and LC Phone setup are in the **A2P Compliance Badge** — not tested in Part B.

**Definition of Done (Day 3):**
- [ ] 5 SMS templates created with correct merge fields
- [ ] 3 email templates created
- [ ] Webchat widget configured
- [ ] Snapshot: `Snapshot - Elevate - v1 Foundation (Day 3)`

> **Agency Step — Create Snapshot v1:**
> Agency view → Snapshots → + New Snapshot → source: **Elevate Digital Agency** → name: `Snapshot - Elevate - v1 Foundation (Day 3)` → Save → return to Elevate sub-account.
>
> This is your second snapshot of the day — you should be doing this in well under 2 minutes now.

---

## B4 — Day 4: Calendars + Integrations

> Same drill as BrightSmile — calendar + Zoom/Google Meet is the most-failed Part B task. Build it again here for reps.

### B4.1 Calendars (create all 3)

**Strategy Call (Round Robin)**
- Duration: 30 min
- Buffer: 10 min after
- Assign to: Rachel and Derek (round robin)
- Availability: Mon-Fri 9AM-5PM
- Booking form: Name, Email, Company Name, Website, Monthly Marketing Budget, Primary Goal

**Onboarding Kickoff (Basic)**
- Duration: 90 min
- Buffer: 15 min after
- Availability: Mon-Thu 10AM-4PM
- Booking form: Company Name, Key Stakeholders Attending, Top 3 Goals

**Monthly Review Call (Round Robin)**
- Duration: 45 min
- Buffer: 15 min after
- Assign to: Rachel and Derek
- Availability: Mon-Fri 9AM-5PM
- Booking form: Company Name, Report Period, Items to Discuss

### B4.2 Zoom / Google Meet Integration (DRILL AGAIN)

For the **Strategy Call** calendar:
1. Calendar Settings → Connections → Connect Zoom (or Google Meet)
2. Set meeting location to Zoom (or Google Meet)
3. Test booking via the calendar link
4. Verify: confirmation email contains the meeting link

**Drill checklist:**
- [ ] Zoom/Meet connected
- [ ] Test booking completed
- [ ] Meeting link visible in confirmation email
- [ ] Calendar event shows the link

**Definition of Done (Day 4):**
- [ ] All 3 calendars created with correct durations and buffers
- [ ] Strategy Call connected to Zoom or Google Meet
- [ ] Test booking confirmed with meeting link
- [ ] Booking forms contain the described fields
- [ ] Snapshot: `Snapshot - Elevate - v2 Calendars (Day 4)`

---

## B5 — Day 5: Opportunities & Pipelines

### B5.1 Client Acquisition Pipeline (7 stages)
1. New Lead / Initial Contact
2. Discovery Call Scheduled
3. Audit In Progress
4. Proposal Sent
5. Negotiation / Contract Review
6. Closed Won
7. Closed Lost

### B5.2 Project Delivery Pipeline (6 stages)
1. Onboarding
2. Strategy / Planning
3. Active Execution
4. Reporting
5. Renewal Discussion
6. Churned / Off-Boarded

Create 5 sample opportunities across the Client Acquisition Pipeline using the imported contacts.

**Definition of Done (Day 5):**
- [ ] Both pipelines created with all stages
- [ ] 5+ opportunities created with values and notes
- [ ] Snapshot: `Snapshot - Elevate - v3 Pipelines (Day 5)`

> **Agency Step — Create Snapshot v3:**
> Agency view → Snapshots → + New Snapshot → source: Elevate → name: `Snapshot - Elevate - v3 Pipelines (Day 5)` → Save → return to Elevate sub-account.

---

## B6 — Day 6: Payments

### B6.1 Products

| Product | Price | Type |
|---|---|---|
| SEO Retainer | $3,000/mo | Recurring |
| PPC Management | $4,000/mo | Recurring |
| Social Media Management | $2,000/mo | Recurring |
| Website Build | $8,000 | One-time |
| Brand Audit | $1,500 | One-time |

### B6.2 Invoices + Coupon
- **Onboarding Invoice:** Brand Audit ($1,500) + first month PPC Management ($4,000) = $5,500
- **Recurring Invoice:** PPC Management $4,000/month (set up as subscription)
- **Coupon:** Code `PARTNER` — 15% off one-time products

**Definition of Done (Day 6):**
- [ ] 5 products created with correct billing types (one-time vs recurring)
- [ ] Onboarding invoice created
- [ ] Recurring invoice/subscription created for PPC
- [ ] `PARTNER` coupon created with 15% discount

---

## B7 — Day 7: Marketing (Email + Trigger Links)

### B7.1 Email Templates for Campaigns (create 3)
- `Elevate - Prospect Nurture: Case Study` — includes trigger link `download-case-study`
- `Elevate - Monthly Client Report Notification` — "Your report for [Month] is ready"
- `Elevate - Agency Newsletter: Industry Tips` — general nurture

### B7.2 Trigger Links (create 4)
- `interested-seo` → applies tag `interested-seo`
- `interested-ppc` → applies tag `interested-ppc`
- `interested-social-media` → applies tag `interested-social-media`
- `download-case-study` → applies tag `downloaded-case-study`

### B7.3 Campaign
- Create a campaign: "Elevate - Prospect Nurture"
- Target list: "High-Value Prospects" Smart List
- First email: `Elevate - Prospect Nurture: Case Study`

**Definition of Done (Day 7):**
- [ ] 3 email templates created
- [ ] 4 trigger links created and tested (click → tag applied)
- [ ] 1 campaign drafted targeting the Smart List
- [ ] Snapshot: `Snapshot - Elevate - v4 Marketing (Day 7)`

> **Agency Step — Create Snapshot v4:**
> Agency view → Snapshots → + New Snapshot → source: Elevate → name: `Snapshot - Elevate - v4 Marketing (Day 7)` → Save → return to sub-account.

---

## B8 — Day 8: Sites (Funnels), Forms, Surveys

### B8.1 Funnel: Free Strategy Session (2 steps)
**Step 1 — Landing Page:**
- Headline: "Get a Free 30-Minute Growth Strategy Session"
- Sub-headline uses `{{offer.consultation}}`
- Lead capture form embedded (see B8.2)
- CTA: "Reserve My Free Strategy Call"

**Step 2 — Thank You Page:**
- Confirmation + next steps
- Strategy Call calendar embedded
- What to expect on the call

### B8.2 Lead Intake Form
Required fields:
- First Name, Last Name (required)
- Email, Phone (required)
- Company Name (required, maps to company_name)
- Website URL (maps to custom field)
- Industry (dropdown, maps to custom field)
- Monthly Marketing Budget (dropdown)
- Primary Goal (text)

### B8.3 Survey: Marketing Needs Assessment (conditional)
- Page 1: "What's your #1 marketing challenge?" (options: Not enough traffic, Poor lead quality, Low conversion rate, No time for marketing, Other)
- Page 2A (Traffic): Current SEO efforts, paid ad experience
- Page 2B (Lead Quality): Target audience description, current lead sources
- Page 2C (Conversion): Current funnel, CRM in use

On submit → Workflow applies tags:
- `goal-more-traffic`, `goal-more-leads`, `goal-better-conversion`
- Creates opportunity in Client Acquisition Pipeline at "New Lead / Initial Contact"

**Definition of Done (Day 8):**
- [ ] 2-step funnel built and published
- [ ] Lead form embedded with correct field mapping
- [ ] Survey built with conditional pages
- [ ] Submit survey with test contact → tags applied + opportunity created

---

## B9 — Day 9: Automation & Workflows

> Build all 4. Each one covers a different Part B scenario type.

### Workflow 1: Elevate - New Lead Nurture
**Trigger:** Form submitted (Elevate lead form) OR tag added: `new-agency-lead`
**Actions:**
1. Add tag: `new-agency-lead`
2. Send Email: `Elevate - Prospect Nurture: Case Study`
3. Create opportunity in Client Acquisition Pipeline → Stage: "New Lead / Initial Contact"
4. Wait: 2 days
5. Send SMS: "Hi {{contact.first_name}}, did you get a chance to review our case study? Happy to jump on a quick call."
6. Wait: 3 days (if no booking)
7. Internal notification to Account Manager: "Lead {{contact.first_name}} at {{contact.company_name}} — no call booked in 5 days"

**Test checklist:**
- [ ] Trigger fires on form submit
- [ ] Tags applied
- [ ] Email sent immediately
- [ ] Opportunity created in correct stage
- [ ] Internal notification received after delay
- [ ] Workflow status shows "Published"

### Workflow 2: Elevate - Client Onboarding
**Trigger:** Opportunity stage changed to "Closed Won" (in Client Acquisition Pipeline)
**Actions:**
1. Add tag: `active-client`, remove tag: `new-agency-lead`
2. Send Email: `Elevate - Client Onboarding Kit`
3. Send SMS: `Elevate - Onboarding Welcome`
4. Create opportunity in Project Delivery Pipeline → Stage: "Onboarding"
5. Wait: 1 day
6. Book onboarding kickoff call (send calendar link via email)
7. Internal notification to Project Manager: "New client {{contact.company_name}} closed — onboarding workflow active"

**Test checklist:**
- [ ] Trigger fires on stage change to Closed Won
- [ ] Tags updated
- [ ] Onboarding email and SMS sent
- [ ] Opportunity created in Project Delivery pipeline
- [ ] Internal notification received
- [ ] Workflow status shows "Published"

### Workflow 3: Elevate - Contract Renewal Reminder
**Trigger:** Contract End Date is 60 days away (date-based trigger)
**Actions:**
1. Add tag: `renewal-approaching`
2. Send Email: uses `{{offer.retainer_discount}}`
3. Wait: 14 days
4. If no renewal: Send SMS: `Elevate - Contract Renewal Notice`
5. Wait: 14 more days
6. If still no renewal: Internal notification to Account Manager + move opportunity to "Renewal Discussion"

**Test checklist:**
- [ ] Date trigger configured for 60 days before Contract End Date
- [ ] Tags applied
- [ ] Email sent at trigger point
- [ ] SMS sent 14 days later
- [ ] Internal notification fires if no action
- [ ] Workflow status shows "Published"

### Workflow 4: Elevate - Monthly Report Notification
**Trigger:** Tag added: `monthly-report-ready` (manually triggered by team or set to first of month)
**Actions:**
1. Send Email: `Elevate - Monthly Performance Report`
2. Send SMS: `Elevate - Monthly Report Ready`
3. Wait: 3 days
4. If no Monthly Review Call booked: Send follow-up SMS with calendar link
5. Internal notification: "{{contact.company_name}} has not booked their review call"

**Test checklist:**
- [ ] Trigger fires on tag added
- [ ] Email and SMS sent
- [ ] Follow-up fires after 3 days with no booking
- [ ] Internal notification received
- [ ] Workflow status shows "Published"

**Definition of Done (Day 9):**
- [ ] All 4 workflows created and **Published** (verify the toggle, not just saved)
- [ ] Each workflow tested with `TEST - Do Not Delete` contact
- [ ] Each test checklist above completed
- [ ] Snapshot: `Snapshot - Elevate - v5 Workflows (Day 9)`

> **Agency Step — Create Snapshot v5 + Load Drill:**
> Agency view → Snapshots → + New Snapshot → source: Elevate → name: `Snapshot - Elevate - v5 Workflows (Day 9)` → Save.
>
> **Then do the full load drill:**
> Snapshots list → find Elevate v5 → three-dot menu → Push to Account → select a blank test sub-account → Add/Merge → Load → enter the test sub-account → verify workflows appeared → return to Agency view.
>
> This is the exact sequence for Part B snapshot tasks. By this point you should complete both steps in under 4 minutes total.

---

## B10 — Day 10: Reputation, Community, Reporting

### B10.1 Testimonial + Case Study Permission Workflow
**Trigger:** Opportunity stage changed to "Active Execution" (at 90-day mark — use date trigger or manual tag)
**Actions:**
1. Send Email: "Can we feature you?" — asks permission to use results as a case study
2. Trigger link in email: `approved-case-study` → adds tag + notifies team
3. Wait: 7 days (if no response): Send follow-up

### B10.2 Community: "Client Portal"
- Create the community
- Groups: Agency Updates, Monthly Reports, Strategy Resources, Client Success Stories
- 2 sample posts in Agency Updates

### B10.3 Weekly Reporting Checklist (Elevate)
- [ ] New leads this week vs last week
- [ ] Strategy calls booked vs completed
- [ ] Active clients count + any status changes
- [ ] Contracts expiring in 60 days (Smart List check)
- [ ] Revenue from invoices this month

**Definition of Done (Day 10):**
- [ ] Testimonial workflow built
- [ ] Community created with groups + 2 sample posts
- [ ] Weekly reporting checklist documented
- [ ] Snapshot: `Snapshot - Elevate - v6 Complete (Day 10)`

> **Agency Step — Final Snapshot + Full Agency Review:**
>
> **Create final snapshot:**
> Agency view → Snapshots → + New Snapshot → source: Elevate → name: `Snapshot - Elevate - v6 Complete (Day 10)` → include ALL assets → Save.
>
> **Full agency-level review (both sub-accounts):**
> 1. Agency Dashboard — compare stats: BrightSmile vs Elevate (conversations, contacts added, appointments)
> 2. Accounts list → BrightSmile → three-dot menu → what options appear? (Edit, Pause, Reports)
> 3. Accounts list → Elevate → same
> 4. Snapshots list — you should now have 12 snapshots (6 per business). Confirm naming is consistent.
> 5. Agency Settings → Team — confirm your agency admin is the only person here
>
> **You have now practiced every agency-level task that could appear in Part B.** The Part B drill at the end of this section is the final exam simulation.

---

## B-Scorecard — Self-Grade Elevate (0–5 each)

| Category | Score |
|---|---:|
| Day 1 — Settings + custom values + users | |
| Day 2 — CRM (fields, import, smart lists) | |
| Day 3 — Templates + webchat | |
| Day 4 — Calendars + Zoom/Meet integration | |
| Day 5 — Pipelines + opportunities | |
| Day 6 — Payments + invoices + coupon | |
| Day 7 — Marketing + trigger links | |
| Day 8 — Funnels + forms + surveys | |
| Day 9 — Workflows (4 built, tested, published) | |
| Day 10 — Reputation + community + reporting | |
| **Part B Speed** — Can complete core tasks in < 25 min? | |

**Target: 40+/50 on content + "Yes" on speed.**

---

## B — Part B Timed Drill (30 minutes)

> Second run of the same drill. By now you should be faster than your first BrightSmile drill. Track your time improvement.

**Setup:** Use a fresh/blank sub-account. Set a 30-minute timer.

**Build the following from scratch:**
1. Business profile + 3 custom values (target: < 5 min)
2. 1 contact added manually with tags (target: < 2 min)
3. 1 pipeline with 3 stages + 1 opportunity for the contact (target: < 5 min)
4. 1 calendar connected to Zoom or Google Meet + test booking (target: < 7 min)
5. 1 workflow: "New Lead" trigger → email → internal notification → Published (target: < 8 min)
6. 1 snapshot from Agency view (target: < 3 min)

**Scoring:**
| Time | Result |
|---|---|
| < 25 minutes | Exam-ready |
| 25–40 minutes | Borderline — drill the slowest step |
| > 40 minutes | Not ready — back to isolated step drills |

**Improvement target:** Your Elevate drill time should be 5–10 minutes faster than your BrightSmile drill time. If it's not, you need more navigation reps — not more content study.

---

## Snapshots Summary

| Snapshot | Created After |
|---|---|
| `Snapshot - BrightSmile - v1 Foundation` | Day 3 |
| `Snapshot - BrightSmile - v2 Calendars` | Day 4 |
| `Snapshot - BrightSmile - v3 Pipelines` | Day 5 |
| `Snapshot - BrightSmile - v4 Marketing` | Day 7 |
| `Snapshot - BrightSmile - v5 Workflows` | Day 9 |
| `Snapshot - BrightSmile - v6 Complete` | Day 10 |
| `Snapshot - Elevate - v1 Foundation` | Day 3 |
| `Snapshot - Elevate - v2 Calendars` | Day 4 |
| `Snapshot - Elevate - v3 Pipelines` | Day 5 |
| `Snapshot - Elevate - v4 Marketing` | Day 7 |
| `Snapshot - Elevate - v5 Workflows` | Day 9 |
| `Snapshot - Elevate - v6 Complete` | Day 10 |

Rule: never overwrite a snapshot — always create a new version number.
