# Phase 1 Practical (Full Build)
## Exam Preparation: Two Separate Sub-Accounts

This practical consolidates **all Phase 1 case-scenario work (Days 1–10)** into **two independent builds** inside your GHL Agency account:

1. **BrightSmile Dental Clinic** sub-account (local healthcare-style business)
2. **Elevate Digital Agency** sub-account (B2B marketing agency)

Treat each section like a timed exam simulation: build the sub-account from Day 1 → Day 10, then self-grade.

---

## How to Use This Practical

You said you’ll use **two different sub-accounts**. Use these sections separately:

- Section A: BrightSmile Dental Clinic (build in the BrightSmile sub-account)
- Section B: Elevate Digital Agency (build in the Elevate sub-account)

---

## Global Naming + Hygiene Rules (Do this first)

### Naming conventions
Use consistent prefixes so you can find things fast:
- **BrightSmile assets:** `BrightSmile - ...`
- **Elevate assets:** `Elevate - ...`
- **Tags:** lowercase + hyphens, e.g. `new-patient-inquiry`, `new-agency-lead`

### Test data rules
- Keep at least 1 permanent test contact per sub-account:
  - `TEST - Do Not Delete`
- Use realistic E.164 phone numbers for testing (avoid fictitious `555` ranges).

---

## Section 0 — Agency Account Setup (Admin)

> Goal: Make your agency environment “ready to deploy” before creating client sub-accounts.

### 0.1 Agency “foundation” checklist
- [ ] Agency business info is accurate (name, address, timezone)
- [ ] Default notification preferences configured for agency admins
- [ ] 2FA enabled for agency admins

### 0.2 Domains + email + phone (agency-level best practice)
This practical expects you to set these up per sub-account, but decide your agency strategy now:
- **Funnel/website domain strategy:**
  - Option A: each client has their own domain/subdomain
  - Option B: agency-owned subdomains for training (fine for exam practice)
- **Email sending domain:** plan a dedicated sending domain per brand when possible
- **Phone/SMS:** plan for one main number per sub-account

---

---

# Section A — BrightSmile Dental Clinic (Sub-Account Practical)

Build everything below inside the **BrightSmile Dental Clinic** sub-account.

## A1 — Day 1: Dashboard & Settings

### A1.1 Business Profile
- Business Name: BrightSmile Dental Clinic
- Address: 456 Smile Avenue, Springfield
- Hours: Mon-Thu 8AM-5PM, Fri 8AM-2PM, Sat-Sun Closed
- Category: Healthcare / Dental
- Phone: main line + separate emergency after-hours number

**Custom Values (create these):**
- `{{business.name}}` = BrightSmile Dental Clinic
- `{{business.phone}}` = (placeholder)
- `{{business.email}}` = smile@brightsmile.com (placeholder)
- `{{business.address}}` = 456 Smile Avenue, Springfield
- `{{business.hours}}` = Mon-Thu 8AM-5PM, Fri 8AM-2PM
- `{{emergency.phone}}` = (placeholder)
- `{{offer.new_patient}}` = Free Dental Exam & X-Rays for New Patients
- `{{offer.whitening}}` = 50% Off Professional Whitening - Limited Time
- `{{offer.referral}}` = Refer a Friend, Both Get $50 Off Next Visit

### A1.2 Users + permissions (create a minimal set)
Create users (or document them if you can’t create all). Use “Only Assigned Data” intentionally.

| Role | Contacts | Conversations | Appointments | Pipeline | Payments | Settings |
|------|----------|--------------|--------------|----------|----------|----------|
| Dentist | Assigned | Assigned | Own schedule | View only | No | No |
| Hygienist | Assigned | No | Own schedule | No | No | No |
| Front Desk | All | All | All schedules | View only | View only | No |
| Admin/Owner | All | All | All | Full | Full | Full |

**Definition of Done (Day 1):**
- [ ] Business Profile complete
- [ ] Custom Values created
- [ ] At least 2 users created (Admin + Front Desk)
- [ ] “Only Assigned Data” decisions match the table

---

## A2 — Day 2: Contacts & CRM
### A2.1 Custom Fields
Create the custom field folders + fields.

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

### A2.2 Sample CSV + import (or manual create)
- Design a 15-patient dataset (or create 15 contacts manually)

### A2.3 Smart Lists
- Overdue for Cleaning
- Active Treatment - Follow-Up Needed
- Self-Pay Patients
- Dr. Kim’s Patients
- Outstanding Balance

**Definition of Done (Day 2):**
- [ ] Custom fields created in folders
- [ ] 15+ patient contacts created/imported
- [ ] Smart Lists return correct records

---

## A3 — Day 3: Conversations, Templates, Webchat
### A3.1 Templates
**SMS**
- Appointment Reminder - 48hr
- Post-Procedure Care
- Insurance Follow-Up
- 6-Month Recall Notice

**Email (at least 2)**
- Welcome to BrightSmile
- Post-Visit Summary

**Webchat widget**
- Greeting + after-hours message
- Include dental disclaimer: chat is for scheduling/general inquiries
- Pre-chat form includes “Reason for inquiry” dropdown

### A3.2 Phone/SMS best practice (US)
- Register A2P 10DLC for production-scale messaging
- Don’t send sensitive details over SMS

**Definition of Done (Day 3):**
- [ ] 4 SMS templates created
- [ ] 2 email templates created
- [ ] Webchat widget configured

---

## A4 — Day 4: Calendars

### A4.1 Calendars (design + build)
- General Checkup (Basic)
- Cosmetic Consultation (Basic)
- Emergency Dental (Basic, same-day)
- Hygienist Cleaning (Round Robin if multiple hygienists)

**Definition of Done (Day 4):**
- [ ] Calendars created with correct durations
- [ ] Availability + buffers configured
- [ ] Booking forms contain the described fields

---

## A5 — Day 5: Opportunities & Pipelines

### A5.1 Pipelines
- Patient Treatment Pipeline (8 stages)
- Insurance Claims Tracking pipeline (5 stages)

Create 5 sample opportunities with realistic values and notes.

**Definition of Done (Day 5):**
- [ ] All pipelines + stages created
- [ ] 5+ opportunities created

---

## A6 — Day 6: Payments

### A6.1 Products + invoices
Create products:
- Dental Exam ($200)
- Professional Cleaning ($150)
- Teeth Whitening Package ($450)
- Crown / Cap ($1,200)
- Emergency Visit ($300)

Create:
- Whitening invoice for insurance adjustment (negative line item)
- Orthodontics payment plan concept: $375/mo x 12

**Definition of Done (Day 6):**
- [ ] Products created with correct billing types
- [ ] Whitening invoice created with insurance adjustment
- [ ] Payment plan approach documented

---

## A7 — Day 7: Marketing (Email + Trigger Links)

### A7.1 Email templates + campaign + trigger links
Build 4 email templates:
- New Patient Welcome
- Cleaning Recall Reminder (with trigger link `clicked-book-cleaning`)
- Post-Procedure Care Instructions
- Referral Request

Create a campaign sending Cleaning Recall Reminder to a “Patients Due for Cleaning” list.

Create trigger links:
- `interested-whitening` → tag `interested-whitening`
- `interested-orthodontics` → tag `interested-orthodontics`

**Definition of Done (Day 7):**
- [ ] Templates created
- [ ] Trigger links created + tested
- [ ] 1 campaign drafted (or scheduled)

---

## A8 — Day 8: Sites (Funnels), Forms, Surveys

### A8.1 Funnel + form + survey
Build a 2-step funnel:
- Free Dental Exam (Landing Page + Thank You)

Build intake form with required fields (including DOB), embed on landing page.

Build conditional survey “Patient Needs” and set a workflow to:
- tag needs (e.g., `needs-cosmetic`, `needs-orthodontics`)
- create an opportunity in the dental pipeline

**Definition of Done (Day 8):**
- [ ] 2-step funnel built
- [ ] Form embedded + maps to fields
- [ ] Survey built with conditional pages

---

## A9 — Day 9: Automation & Workflows

Build these 3 workflows:
- BrightSmile - New Patient Inquiry
- BrightSmile - Appointment Reminder
- BrightSmile - No-Show Recovery

**Definition of Done (Day 9):**
- [ ] All workflows published
- [ ] Each workflow has at least one internal notification
- [ ] Each workflow tested with the `TEST - Do Not Delete` contact

---

## A10 — Day 10: Reputation, Community, Reporting

### A10.1 Reputation + community + reporting
- Reputation workflow: post-appointment review request (wait 3 hours)
- Review response templates for 5-star, 3–4 star, 1–2 star
- Community: “Dental Health Hub” with groups + 2 sample posts
- Weekly report checklist for BrightSmile

**Definition of Done (Day 10):**
- [ ] Review request system built
- [ ] Community created with groups
- [ ] Weekly reporting checklist documented

---

## A-Snapshots — Snapshot Versioning (BrightSmile)

Use snapshots as “save points” so you can restore or compare versions.

Create these snapshots:
- `Snapshot - BrightSmile - v1 Foundation (Day 1)`
- `Snapshot - BrightSmile - v2 CRM + Comms (Day 3)`
- `Snapshot - BrightSmile - v3 Calendars + Pipelines (Day 5)`
- `Snapshot - BrightSmile - v4 Payments + Marketing (Day 7)`
- `Snapshot - BrightSmile - v5 Funnels + Automation (Day 9)`
- `Snapshot - BrightSmile - v6 Reputation + Reporting (Day 10)`

Rule: never overwrite a snapshot—create a new version.

---

## A-Scorecard — Self-Grade BrightSmile (0–5 each)

Score each sub-account from 0–5.

| Category | Score |
|---|---:|
| Day 1 Settings + users |  |
| Day 2 CRM (fields, import, lists) |  |
| Day 3 Conversations + templates + webchat |  |
| Day 4 Calendars |  |
| Day 5 Pipelines + opportunities |  |
| Day 6 Payments |  |
| Day 7 Marketing + trigger links |  |
| Day 8 Funnels + forms + surveys |  |
| Day 9 Workflows |  |
| Day 10 Reputation + community + reporting |  |

Target: **40+/50** total.

## A-Exam Run-Through (15 minutes)

Run these quick checks in the BrightSmile sub-account:
- [ ] Submit the BrightSmile funnel form → contact created + tags applied
- [ ] Book an appointment from the Thank You page → confirmation email/SMS queued
- [ ] Mark appointment as No-Show → no-show recovery workflow runs
- [ ] Mark appointment as Showed → review request workflow queues (Day 10)
- [ ] Verify opportunity exists in the Patient Treatment Pipeline
- [ ] Verify 1 Smart List (e.g. Outstanding Balance) returns expected records

---

# Section B — Elevate Digital Agency (Sub-Account Practical)

Build everything below inside the **Elevate Digital Agency** sub-account.

## B1 — Day 1: Dashboard & Settings

### B1.1 Business Profile
- Business Name: Elevate Digital Agency
- Address: 789 Marketing Blvd, Suite 300, Springfield
- Hours: Mon-Fri 9AM-6PM
- Category: Professional Services / Marketing
- Website: elevateagency.com (placeholder)

**Custom Values (create these):**
- `{{business.name}}` = Elevate Digital Agency
- `{{business.phone}}` = (placeholder)
- `{{business.email}}` = hello@elevateagency.com (placeholder)
- `{{business.address}}` = 789 Marketing Blvd, Suite 300, Springfield
- `{{business.hours}}` = Mon-Fri 9AM-6PM
- `{{offer.audit}}` = Free Website & SEO Audit
- `{{offer.consultation}}` = Free 30-Minute Strategy Session
- `{{onboarding.link}}` = (placeholder)
- `{{offer.retainer_discount}}` = 15% Off First 3 Months for Annual Contracts

### B1.2 Users + permissions (create a minimal set)
| Role | Contacts | Conversations | Appointments | Pipeline | Reporting | Settings |
|------|----------|--------------|--------------|----------|-----------|----------|
| Account Manager | Assigned clients | Assigned | Own | Assigned | Assigned clients | No |
| Specialist | Assigned tasks only | No | No | No | No | No |
| Project Manager | All | All | All | All | All | No |
| Agency Owner | All | All | All | All | All | Full |

**Definition of Done (Day 1):**
- [ ] Business Profile complete
- [ ] Custom Values created
- [ ] At least 2 users created (Agency Owner + Account Manager)
- [ ] “Only Assigned Data” decisions match the table

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

### B2.2 Sample CSV + import (or manual create)
- Design a 15-client/prospect dataset (or create 15 contacts manually)

### B2.3 Smart Lists
- Contracts Expiring in 60 Days
- Upsell Opportunities
- Rachel’s Book of Business
- High-Value Prospects
- Churned - Win-Back Targets

**Definition of Done (Day 2):**
- [ ] Custom fields created in folders
- [ ] 15+ contacts created/imported
- [ ] Smart Lists return correct records

## B3 — Day 3: Conversations, Templates, Webchat

### B3.1 Templates
**SMS**
- Onboarding Welcome
- Monthly Report Ready
- Strategy Call Reminder
- Contract Renewal Notice

**Email (at least 2)**
- Client Onboarding Kit
- Monthly Performance Report

**Webchat widget**
- B2B tone
- Pre-chat: name, email, company name, service interest

**Definition of Done (Day 3):**
- [ ] 4 SMS templates created
- [ ] 2 email templates created
- [ ] Webchat widget configured

## B4 — Day 4: Calendars

Create these calendars:
- Strategy Call (Round Robin)
- Onboarding Kickoff (Basic)
- Monthly Review Call (Round Robin)

**Definition of Done (Day 4):**
- [ ] Calendars created with correct durations
- [ ] Availability + buffers configured
- [ ] Booking forms contain the described fields

## B5 — Day 5: Opportunities & Pipelines

Create these pipelines:
- Client Acquisition Pipeline (7 stages)
- Project Delivery pipeline (6 stages)

Create 5 sample opportunities with realistic values and notes.

**Definition of Done (Day 5):**
- [ ] All pipelines + stages created
- [ ] 5+ opportunities created

## B6 — Day 6: Payments

Create products:
- SEO Retainer ($3,000/mo)
- PPC Management ($4,000/mo)
- Social Media Management ($2,000/mo)
- Website Build ($8,000 one-time)
- Brand Audit ($1,500 one-time)

Create:
- Onboarding invoice: Audit + first PPC month = $5,500
- Recurring invoice for PPC $4,000/mo
- Coupon: `PARTNER` (15% off one-time products)

**Definition of Done (Day 6):**
- [ ] Products created with correct billing types
- [ ] 1 invoice created
- [ ] 1 recurring subscription/invoice created
- [ ] 1 coupon created

## B7 — Day 7: Marketing (Email + Trigger Links)

Build 3 email templates:
- Prospect Nurture - Case Study (trigger link `download-case-study`)
- Monthly Client Report Notification
- Agency Newsletter - Industry Tips

Create trigger links:
- `interested-seo`
- `interested-ppc`
- `interested-social-media`
- `download-case-study`

**Definition of Done (Day 7):**
- [ ] Templates created
- [ ] Trigger links created + tested
- [ ] 1 campaign drafted (or scheduled)

## B8 — Day 8: Sites (Funnels), Forms, Surveys

Build a 2-step funnel:
- Free Strategy Session (Landing Page + Thank You)

Build client intake form with business fields.

Build conditional survey “Marketing Needs Assessment” and set a workflow to:
- tag goals (e.g., `goal-more-traffic`, `goal-more-leads`)
- create an opportunity in the agency pipeline

**Definition of Done (Day 8):**
- [ ] 2-step funnel built
- [ ] Form embedded + maps to fields
- [ ] Survey built with conditional pages

## B9 — Day 9: Automation & Workflows

Build these 3 workflows:
- Elevate - New Lead Nurture
- Elevate - Client Onboarding
- Elevate - Contract Renewal Reminder

**Definition of Done (Day 9):**
- [ ] All workflows published
- [ ] Each workflow has at least one internal notification
- [ ] Each workflow tested with the `TEST - Do Not Delete` contact

## B10 — Day 10: Reputation, Community, Reporting

- Testimonial + case study permission workflow (90-day trigger concept)
- Community: “Client Portal” with groups + 2 sample posts
- Weekly report checklist for Elevate

**Definition of Done (Day 10):**
- [ ] Testimonial system built
- [ ] Community created with groups
- [ ] Weekly reporting checklist documented

## B-Snapshots — Snapshot Versioning (Elevate)

Create these snapshots:
- `Snapshot - Elevate - v1 Foundation (Day 1)`
- `Snapshot - Elevate - v2 CRM + Comms (Day 3)`
- `Snapshot - Elevate - v3 Calendars + Pipelines (Day 5)`
- `Snapshot - Elevate - v4 Payments + Marketing (Day 7)`
- `Snapshot - Elevate - v5 Funnels + Automation (Day 9)`
- `Snapshot - Elevate - v6 Reputation + Reporting (Day 10)`

## B-Scorecard — Self-Grade Elevate (0–5 each)

| Category | Score |
|---|---:|
| Day 1 Settings + users |  |
| Day 2 CRM (fields, import, lists) |  |
| Day 3 Conversations + templates + webchat |  |
| Day 4 Calendars |  |
| Day 5 Pipelines + opportunities |  |
| Day 6 Payments |  |
| Day 7 Marketing + trigger links |  |
| Day 8 Funnels + forms + surveys |  |
| Day 9 Workflows |  |
| Day 10 Reputation + community + reporting |  |

Target: **40+/50** total.

## B-Exam Run-Through (15 minutes)

Run these quick checks in the Elevate sub-account:
- [ ] Submit the Elevate funnel form → contact created + tags applied
- [ ] Book a Strategy Call → confirmation + reminders queued
- [ ] Move a test opportunity to “Contract Signed” → onboarding workflow runs
- [ ] Confirm at least one marketing trigger link applies a tag
- [ ] Verify opportunity exists in the Client Acquisition Pipeline
- [ ] Verify 1 Smart List (e.g. High-Value Prospects) returns expected records
