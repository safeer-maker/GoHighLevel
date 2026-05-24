# Shared Foundation — Booking Setup

> Complete build guide for a GHL funnel that captures leads, shows a calendar booking widget, and triggers the booking workflow.

---

## Goal

Build a self-contained booking funnel for a business with no website.

- Funnel title: `7-Day Free Trial`
- Primary flow: lead lands on the funnel, enters details into the calendar booking step, and submits the scheduler form.
- Workflow: captures lead data, tags the lead, creates the opportunity, sends instant response, and follows up.
- Booking URL: publish the funnel and set `{{custom_values.business.booking_url}}` to that URL.

---

## What to build first

### 1. Required foundation assets

Before the funnel and workflow, confirm these exist in GHL and in shared foundation:

- Custom Fields:
  - `lead_source`, `lead_source_detail`, `lead_campaign`, `lead_captured_at`, `lead_first_response_at`, `lead_status`
  - `fitness_goal_primary`, `preferred_workout_time`
  - `sms_opt_in`, `email_opt_in`
- Custom Values:
  - `business.booking_url`
  - `business.short_name`
  - `team.owner_first`
  - `offer.free_trial`
  - `voice.greeting_warm`
  - `voice.signature_short`
- Tags:
  - `lead-new`, `lead-contacted`, `lead-responded`, `trial-booked`, `lead-cold`
  - `source-instagram`, `source-facebook`, `source-google`, `source-walkin`, `source-referral`, `source-web`
- Pipeline:
  - `Membership Sales` with stage `New Lead`
- Product / Service:
  - `Free 7-Day All-Access Pass` ($0, SKU `TRIAL-7DAY`) or appointment type `7-Day Free Trial`

---

## Recommended architecture

Use a single GHL funnel that includes:

1. Landing page (hero + benefits)
2. Calendar booking page with form fields attached
3. Thank-you page

Because the business has no website, this funnel is the business’s public booking presence.

- Publish the funnel and use the published URL as `business.booking_url`.
- The calendar step is the first booking touchpoint, not a separate website.

---

## Funnel build

### Funnel name

`Sunrise — 7-Day Free Trial Booking`

### Funnel steps

#### 1. Landing page

- Step name: `01 — Free Trial`
- Headline: `7-Day Free Trial`
- Copy: short benefit statements, social proof, low friction CTA.
- Primary CTA button: `Book Your Free Trial`.
- Button action: navigate to the booking page step.

#### 2. Calendar booking page

- Step name: `02 — Book Your Trial`
- Page title: `7-Day Free Trial`
- Explanation: “Choose your first session and claim your free 7-day pass.”
- Embed the GHL calendar booking widget on this page.
- Use the scheduling widget’s built-in form fields so the lead enters contact info while also selecting a time.

#### 3. Thank-you page

- Step name: `03 — Welcome`
- Message: `You're in! Check your phone.`
- Subtext: `We sent your 7-Day Free Trial booking confirmation and next steps.`
- Optional: show contact options and what to expect next.

---

## Calendar / service setup

### Calendar item

Create a booking service or appointment type named exactly:

- `7-Day Free Trial`

If your GHL version supports calendars and appointment types, configure it like this:

- Duration: `30 minutes` or `45 minutes` (use the first session/orientation time)
- Buffer: 10–15 minutes before/after if needed
- Location: studio or virtual, whichever applies
- Availability: business hours and any trainer availability
- Visibility: public booking allowed

### Form fields on the calendar widget

Use the scheduler form to capture these contact fields:

- First Name → Contact first name
- Last Name → Contact last name
- Phone → Contact phone
- Email → Contact email
- Primary Goal → `fitness_goal_primary`
- Preferred Workout Time → `preferred_workout_time`
- SMS Opt-In → `sms_opt_in`
- Email Opt-In → `email_opt_in`

### Hidden / tracking fields

Add hidden fields to the scheduler form if possible:

- `lead_source` → source name (from URL parameter or funnel)
- `lead_source_detail` → campaign or ad details
- `lead_campaign` → campaign name or UTM campaign

If the calendar widget cannot capture hidden fields directly, add them to the funnel landing page form or use URL parameters on the booking page.

---

## Form and booking flow

### Preferred flow

1. Lead clicks CTA on landing page
2. Lead lands on calendar booking page
3. Lead selects a slot and fills the calendar form
4. Lead submits booking
5. Lead is redirected to the thank-you page
6. Workflow fires on the booking form submission or appointment created event

### Recommended user journey copy

- Landing page CTA: `Book Your Free Trial`
- Calendar step title: `7-Day Free Trial`
- Calendar step instructions: `Choose the time that works best for your first session. We'll reserve your spot and send details.`
- Thank-you page text: `You're in! Check your phone for confirmation and next steps.`

---

## Workflow setup

### Workflow name

`01 — Free Trial Booking — Instant Response`

### Trigger

Use one of these triggers depending on your GHL setup:

- `Form Submitted` on the booking/calendar form
- OR `Appointment Created` where appointment type = `7-Day Free Trial`

If possible, use `Form Submitted` from the scheduling page form. If not, use `Appointment Created`.

### Workflow entry filters

- Form is `Lead Capture — Free 7-Day Trial` OR calendar form attached to `7-Day Free Trial`
- Contact does NOT have tag `member-active`
- Contact does NOT have tag `lead-contacted`

### Workflow actions

#### 1. Update contact fields

- `lead_captured_at` → `{{date_added}}`
- `lead_first_response_at` → `{{now}}` when sending first reply
- `lead_status` → `Contacted`

#### 2. Add tags

- Add `lead-new`
- Add `lead-contacted`

#### 3. Add source tags

Use an If/Else branch based on `lead_source`:

- Instagram → `source-instagram`
- Facebook → `source-facebook`
- Google → `source-google`
- Walk-in → `source-walkin`
- Referral → `source-referral`
- Default → `source-web`

#### 4. Create opportunity

- Pipeline: `Membership Sales`
- Stage: `New Lead`
- Opportunity name: `{{contact.first_name}} {{contact.last_name}} — Free Trial Lead`
- Value: projected membership value, e.g. `948`
- Status: `Open`
- Owner: front desk or owner round-robin
- Skip if contact already has an open Membership Sales opportunity

#### 5. Send instant SMS

- From: `{{custom_values.business.sms_number}}`
- Message: use instant response copy that includes `{{custom_values.business.booking_url}}`
- Skip if contact has tag `do-not-sms` or `sms_opt_in` ≠ `Yes`

#### 6. Send welcome email

- Wait 2 minutes
- Send if `email_opt_in` = `Yes` and no `do-not-email`
- From name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- From email: `{{custom_values.business.email}}`
- Reply-to: `{{custom_values.business.owner_email}}`

#### 7. Add internal notification

- Send notification to `{{custom_values.business.owner_email}}`
- Subject: `New trial booking lead: {{contact.first_name}} {{contact.last_name}}`
- Body includes lead info, source, phone, email, goal, link to contact

#### 8. Follow-up sequence

- Wait 2 hours (respect contact-local 8 AM–9 PM)
  - If contact has tag `lead-responded` OR `trial-booked`, exit
  - Else send SMS `01 — 2hr Nudge`
- Wait until 72 hours after capture (respect contact-local 8 AM–9 PM)
  - If contact has tag `lead-responded` OR `trial-booked`, exit
  - Else send SMS `01 — Day 3 Last Touch`
  - Add tag `lead-cold`
  - Add to workflow `Lead Nurture — 30-Day Drip`

---

## Booking completion and downstream tags

### When a trial is actually booked

If the scheduler creates an appointment for `7-Day Free Trial`, use a second workflow or a workflow branch to set:

- Add tag `trial-booked`
- Update `lead_status` → `Trial Booked`
- Remove `lead-new` if present
- Add `lead-responded` if reply is required

This ensures the follow-up path stops once the lead has booked.

### If you want to tag immediately

Yes, tag users directly in the workflow. Do not rely on manual tagging.

- `lead-new` → first entry
- `lead-contacted` → instant response path
- source tag → attribution
- `trial-booked` → appointment booked
- `lead-cold` → no response after day 3

---

## What to set `business.booking_url` to

Because this business has no website, set `business.booking_url` to the published funnel or scheduling page URL.

- Example: `https://book.sunrisewellness.com`
- If you publish the funnel at a different branded domain, update the custom value accordingly.

---

## Notes for the `7-Day Free Trial` title

- Use `7-Day Free Trial` as the calendar service/appointment type name.
- Use the same wording on the funnel landing page, booking page title, calendar widget heading, and thank-you page.
- If you want a second line, use: `Reserve your starter session and unlock your free 7-day pass.`

---

## Minimal object list for build

- Funnel: `Sunrise — 7-Day Free Trial Booking`
- Landing page: `01 — Free Trial`
- Booking page: `02 — Book Your Trial`
- Thank you page: `03 — Welcome`
- Scheduler service: `7-Day Free Trial`
- Form fields: first name, last name, phone, email, primary goal, preferred workout time, SMS opt-in, email opt-in
- Workflow: `01 — Free Trial Booking — Instant Response`
- Opportunity pipeline: `Membership Sales`
- Tags: `lead-new`, `lead-contacted`, `source-*`, `trial-booked`, `lead-cold`

---

## Quick build checklist

1. Create or verify custom fields.
2. Add `business.booking_url` and other custom values.
3. Create the booking service / calendar item.
4. Build the funnel pages.
5. Publish the funnel and set the booking URL.
6. Create the workflow and map the form trigger.
7. Test the full flow end-to-end.
