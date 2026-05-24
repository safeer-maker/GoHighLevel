# Shared Foundation — Booking Setup

> Single-page build guide for a funnel-first booking system with a separate lead capture form, calendar booking step, and lean automations.

---

## Goal

Build a self-contained booking system for a business with no website.

- Funnel title: `7-Day Free Trial`
- Build order: form first, calendar second, funnel third, workflow last
- Booking URL: publish the funnel and point `{{custom_values.business.booking_url}}` at the public funnel URL
- Key rule: do not re-ask lead source or fitness goals in the booking step if those were already captured in the lead form

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
- Tags from [tags.md](tags.md):
  - `lead-new`, `lead-contacted`, `lead-responded`, `lead-cold`, `lead-lost`
  - `trial-claimed`, `trial-active`, `trial-converted`, `trial-expired`, `trial-not-now`
  - `member-active`
  - `source-instagram`, `source-facebook`, `source-google`, `source-walkin`, `source-referral`, `source-web`, `source-event`
  - `do-not-sms`, `do-not-email`, `do-not-market`
- Pipeline:
  - `Membership Sales` with stage `New Lead`
- Product / Service:
  - `Free 7-Day All-Access Pass` ($0, SKU `TRIAL-7DAY`) or appointment type `7-Day Free Trial`

---

## Recommended architecture

Use one GHL funnel and split the automation into smaller parts.

1. Lead capture form collects the real intake data.
2. Calendar booking step collects the booking time.
3. Funnel hosts both steps and becomes the public booking presence.
4. Workflow is split so source tagging stays isolated from booking confirmation.

- The lead capture form should handle `lead_source`, `lead_source_detail`, `fitness_goal_primary`, `preferred_workout_time`, and consent.
- The calendar step should only book the slot and capture the minimum contact details needed to schedule.
- Publish the funnel and use the published URL as `business.booking_url`.
- If you later want a deep link directly to the calendar page, add a separate custom value for that; keep `business.booking_url` as the primary public entry.

---

## Build order

### 1. Lead capture form

Use the form from #01, not a second copy of the same questions.

- Form Name: `Lead Capture — Free 7-Day Pass`
- Fields:
  - First name
  - Last name
  - Phone
  - Email
  - Main goal → `fitness_goal_primary`
  - Preferred workout time → `preferred_workout_time`
  - Hidden lead source → `lead_source`
  - Hidden source detail → `lead_source_detail`
  - Consent checkbox → `sms_opt_in` and `email_opt_in`
- Submit behavior: redirect to the booking page in the funnel

Important:
- Do not repeat lead source or fitness goal questions on the booking page.
- That data belongs to the intake form and the intake workflow.

Booking page rule:
- The calendar step should only collect scheduling details needed to reserve the slot.
- If the scheduler needs a contact field, keep it to name, phone, and email.
- Do not ask for `fitness_goal_primary`, `preferred_workout_time`, `lead_source`, `lead_source_detail`, or consent again on the booking step.

### 2. Calendar / service setup

Create a booking service or appointment type named exactly:

- `7-Day Free Trial`

If your GHL version supports calendars and appointment types, configure it like this:

- Duration: `30 minutes` or `45 minutes`
- Buffer: 10–15 minutes before/after if needed
- Location: studio or virtual, whichever applies
- Availability: business hours and any trainer availability
- Visibility: public booking allowed

Calendar form fields:
- First name → contact first name
- Last name → contact last name
- Phone → contact phone
- Email → contact email

Do not require the goal or source fields here unless there is a hard operational need. If a field already exists from the intake form, prefill it or leave it out.

### 3. Funnel build

Funnel name:

- `Sunrise — 7-Day Free Trial Booking`

Funnel steps:

#### Step 1 — Landing page

- Step name: `01 — Free Trial`
- Headline: `7-Day Free Trial`
- Copy: short benefit statements, social proof, low friction CTA
- Primary CTA button: `Book Your Free Trial`
- Button action: go to the form step or the booking page step, depending on your layout

#### Step 2 — Form page

- Step name: `02 — Claim`
- Embed the `Lead Capture — Free 7-Day Pass` form
- This page is where the intake form captures source, consent, and lead details

#### Step 3 — Calendar booking page

- Step name: `03 — Book Your Trial`
- Page title: `7-Day Free Trial`
- Explanation: `Choose the time that works best for your first session. We'll reserve your spot and send details.`
- Embed the GHL calendar booking widget on this page
- Keep this page focused on booking, not intake

#### Step 4 — Thank-you page

- Step name: `04 — Welcome`
- Message: `You're in! Check your phone.`
- Subtext: `We sent your 7-Day Free Trial confirmation and next steps.`

---

## Workflow setup

### Split the automation

Use two or three small workflows instead of one large one.

#### Workflow A — Lead Capture Intake

- Workflow Name: `01 — Lead Capture — Intake`
- Trigger: `Form Submitted` on `Lead Capture — Free 7-Day Pass`
- Purpose: create the lead record, send the instant response, and notify staff
- Actions:
  - Stamp `lead_captured_at`
  - Update `lead_status` to `Contacted`
  - Add `lead-new`
  - Add `lead-contacted`
  - Create Membership Sales opportunity
  - Send instant SMS using `{{custom_values.business.booking_url}}`
  - Send welcome email if opted in
  - Send internal notification

Source tagging should live in a separate workflow unless it is truly trivial. Keep the intake workflow focused on lead creation and immediate follow-up.

#### Workflow B — Booking Confirmation

- Workflow Name: `01 — Lead Capture — Booking Confirmation`
- Trigger: `Appointment Created` for `7-Day Free Trial`
- Purpose: mark the booking as claimed and stop lead follow-up branches
- Actions:
  - Add tag `trial-claimed`
  - Update `lead_status` to `Trial Booked`
  - Add `lead-responded` if the booking should end the lead sequence immediately
  - Remove `lead-new` if present
  - Send booking confirmation SMS or email

#### Workflow C — Source Tag Normalization

Use this when you want source logic isolated from the rest of the intake and booking logic.

- Trigger: `Form Submitted` on `Lead Capture — Free 7-Day Pass` or a custom field update on `lead_source`
- Purpose: translate `lead_source` into the correct `source-*` tag
- Actions:
  - If `lead_source` = Instagram, add `source-instagram`
  - If `lead_source` = Facebook, add `source-facebook`
  - If `lead_source` = Google, add `source-google`
  - If `lead_source` = Walk-in, add `source-walkin`
  - If `lead_source` = Referral, add `source-referral`
  - If `lead_source` = Event, add `source-event`
  - Else, add `source-web`

---

## Workflow behavior rules

- Do not ask for `lead_source` or `fitness_goal_primary` inside the booking confirmation workflow.
- Keep lead capture data entry in the intake form.
- Keep appointment booking in the calendar workflow.
- Use tags for state changes and custom fields for stored values.
- Use `trial-claimed`, not `trial-booked`, because that is the tag in `tags.md`.

---

## What to set `business.booking_url` to

Because this business has no website, set `business.booking_url` to the public funnel URL.

- Example: `https://book.sunrisewellness.com`
- If the funnel publishes on a different branded domain, update the custom value accordingly

---

## Notes for the `7-Day Free Trial` title

- Use `7-Day Free Trial` as the calendar service/appointment type name
- Use the same wording on the funnel landing page, booking page title, calendar widget heading, and thank-you page
- If you want a second line, use: `Reserve your starter session and unlock your free 7-day pass.`

---

## Minimal object list for build

- Funnel: `Sunrise — 7-Day Free Trial Booking`
- Landing page: `01 — Free Trial`
- Form page: `02 — Claim`
- Booking page: `03 — Book Your Trial`
- Thank you page: `04 — Welcome`
- Scheduler service: `7-Day Free Trial`
- Lead capture form: `Lead Capture — Free 7-Day Pass`
- Workflow A: `01 — Lead Capture — Intake`
- Workflow B: `01 — Lead Capture — Booking Confirmation`
- Pipeline: `Membership Sales`
- Tags: `lead-new`, `lead-contacted`, `lead-responded`, `trial-claimed`, `lead-cold`, `source-*`

---

## Quick build checklist

1. Create or verify custom fields.
2. Add `business.booking_url` and other custom values.
3. Build the lead capture form first.
4. Create the calendar / appointment type.
5. Build the funnel pages around form then booking.
6. Publish the funnel and set the booking URL.
7. Create the intake workflow and the booking confirmation workflow.
8. Test the full flow end-to-end.
