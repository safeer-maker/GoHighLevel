# #01 — Build Playbook: Lead Capture & Instant Response

> Step-by-step GHL build. Estimated time: **90 minutes** for a competent operator. Prerequisites listed first — do not skip them.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting. If anything is missing, build it first.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Lead Info custom fields (`lead_source`, `lead_source_detail`, `lead_captured_at`, `lead_first_response_at`, `lead_status`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Stamping lead data |
| Fitness Profile fields (`fitness_goal_primary`, `fitness_experience`, `preferred_workout_time`) | Same | Form captures goal data |
| Communication Preferences (`sms_opt_in`, `email_opt_in`) | Same | Consent capture |
| Tags: `lead-new`, `lead-contacted`, `source-instagram`, `source-facebook`, `source-google`, `source-walkin`, `source-referral`, `source-web` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Source attribution |
| Pipeline: **Membership Sales**, Stage: "New Lead" | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Opportunity creation |
| Custom values: `business.short_name`, `business.booking_url`, `team.owner_first`, `offer.free_trial`, `voice.greeting_warm`, `voice.signature_short` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| Product: **Free 7-Day All-Access Pass** ($0, SKU `TRIAL-7DAY`) | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Funnel CTA |

---

## Step 1 — Build the Lead Capture Funnel (30 min)

### 1.1 Create the funnel

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Free 7-Day Pass — Lead Capture`
- **Type:** Lead Generation
- **Template:** Start blank

### 1.2 Build Page 1 — Landing Page

Click **+ Add Step > Landing Page**. Name it `01 — Hero`.

Build in the page editor following the page-by-page copy in **[assets/funnel.md](assets/funnel.md)**. Page 1 structure:

- **Section 1: Hero** — Large background image (sunrise studio shot), H1 headline, subheadline, primary CTA button.
- **Section 2: Social proof bar** — "Trusted by 240+ Springfield wellness lovers" + star strip + 3 small member photos.
- **Section 3: What's included** — 3-column layout (Classes / Open Gym / Intro Consult).
- **Section 4: 3 quick testimonials** — name, photo, 1-line quote, member-since date.
- **Section 5: Repeat primary CTA**.

The primary CTA button label and link target are in [assets/funnel.md](assets/funnel.md). Button action: scroll to Step 2 (form page) or navigate to `/claim`.

### 1.3 Build Page 2 — Form / Claim Page

Click **+ Add Step > Form Page**. Name it `02 — Claim`.

Build:

- **Section 1: Mini-hero** — short H2 "You're one step away" + body line.
- **Section 2: The Form** — drag in a Form element and select the form you'll build in Step 2 below.
- **Section 3: Trust strip** — small icons: "No credit card · Cancel anytime · Real humans reply"

### 1.4 Build Page 3 — Thank-You Page

Click **+ Add Step > Thank-You Page**. Name it `03 — Welcome`.

Build:

- **Section 1: Confirmation** — H1 "You're in! Check your phone." subhead "We just texted you a booking link."
- **Section 2: While you're here** — embed Instagram feed widget (their @sunrisewellnessstudio handle).
- **Section 3: Soft secondary CTA** — "Follow us so you don't miss class drops" with Instagram/Facebook icons.

Full copy for all three pages in [assets/funnel.md](assets/funnel.md).

### 1.5 Publish & note the URL

Click **Publish**. Copy the published URL — this becomes the destination for all paid traffic.

Update `business.booking_url` in **Settings > Custom Values** if the URL changed.

---

## Step 2 — Build the Lead Capture Form (15 min)

Navigate to **Sites > Forms > + Build Form**.

- **Form Name:** `Lead Capture — Free 7-Day Pass`

Form fields (drag from the form builder sidebar). Full spec including labels, placeholders, validation in **[assets/forms.md](assets/forms.md)**.

| Order | Field | Type | Required | Maps to Custom Field |
|---|---|---|---|---|
| 1 | First Name | Text | Yes | (standard contact field) |
| 2 | Last Name | Text | Yes | (standard contact field) |
| 3 | Phone | Phone | Yes | (standard contact field) |
| 4 | Email | Email | Yes | (standard contact field) |
| 5 | What's your primary goal? | Dropdown | Yes | `fitness_goal_primary` |
| 6 | Best time to work out? | Dropdown | No | `preferred_workout_time` |
| 7 | Hidden: source | Hidden text | — | `lead_source` (populated from URL param) |
| 8 | Hidden: source detail | Hidden text | — | `lead_source_detail` (UTM campaign) |
| 9 | Consent checkbox | Checkbox | Yes | `sms_opt_in` AND `email_opt_in` |

**Form settings:**

- **On Submit:** Redirect to `03 — Welcome` thank-you page.
- **Send notification email:** No (the workflow handles this — avoid duplicate notifications).
- **Add to workflow:** Leave blank (the workflow trigger picks it up).

### Walk-in tablet variant

Duplicate the form, name it `Lead Capture — Walk-In Tablet`. Set hidden `lead_source` = `Walk-in` directly. Mount on a tablet at the front desk.

---

## Step 3 — Build the Walk-In Quick Form Page (10 min)

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Walk-In Quick Capture`
- **Type:** Lead Generation
- **Template:** Start blank, one page only.

Add one form page; embed the `Lead Capture — Walk-In Tablet` form. Simple layout:

- Large logo header
- H1: "Welcome to Sunrise — let's get you set up"
- Form (4 fields visible: name, phone, email, goal)
- Submit button text: "Get My Pass"
- Thank-you redirect: a simple page that says "You're in! We'll grab your tablet back."

Bookmark the URL on the front-desk tablet's home screen.

---

## Step 4 — Build the Instant Response Workflow (30 min)

This is the heart of the system. Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `01 — Instant Response — Lead Capture`
- **Folder:** Create folder `01 - Lead Capture` and put it there

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 4.1 Trigger

Click **+ Add New Workflow Trigger**.

- **Trigger:** Form Submitted
- **Filter:** Form is `Lead Capture — Free 7-Day Pass` OR `Lead Capture — Walk-In Tablet`
- **Filter:** Contact does NOT have tag `member-active` (avoid re-triggering for existing members re-filling form)

### 4.2 Action: Stamp lead capture timestamp

- **Action:** Update Contact Field
- **Field:** `lead_captured_at`
- **Value:** `{{contact.date_added}}` (or `{{now}}`)

### 4.3 Action: Tag by source

- **Action:** If / Else
- **Condition:** Custom field `lead_source` equals "Instagram" → branch A: Add tag `source-instagram`
- Repeat for Facebook, Google, Walk-in, Referral, Web Search → respective tags

Easier alternative if your GHL plan supports it: a single "Workflow Variable Mapping" action that maps `lead_source` value directly to the corresponding `source-*` tag via a lookup. Use this if available; the If/Else chain is the fallback.

### 4.4 Action: Add `lead-new` tag

- **Action:** Add Tag
- **Tag:** `lead-new`

### 4.5 Action: Create Opportunity

- **Action:** Create Opportunity
- **Pipeline:** Membership Sales
- **Stage:** New Lead
- **Opportunity Name:** `{{contact.first_name}} {{contact.last_name}} — Trial Lead`
- **Value:** $948 (Basic LTV projection — overwritten on conversion)
- **Status:** Open

### 4.6 Action: Send Email (the critical 5-minute response)

- **Action:** Send Email
- **From:** `{{custom_values.business.sms_number}}`
- **To:** Contact phone
- **Body:** Email body in [assets](assets) — message **A — Instant Response**
- **Wait condition:** None (fires immediately on workflow entry)

Set quiet-hours **bypass = OFF** for this message — transactional/responsive, not marketing. (For *marketing* messages later, quiet-hours respect is on.)

### 4.7 Action: Send Welcome Email

- **Action:** Send Email
- **Template:** Email "Welcome — Free 7-Day Pass" from [assets/emails.md](assets/emails.md)
- **Send via:** Business email
- **Wait before:** 2 minutes (let the Email land first, so they check their phone, then the email is waiting)

### 4.8 Action: Stamp first-response timestamp

- **Action:** Update Contact Field
- **Field:** `lead_first_response_at`
- **Value:** `{{now}}`

### 4.9 Action: Add `lead-contacted` tag, remove `lead-new`

- **Action:** Add Tag → `lead-contacted`
- **Action:** Remove Tag → `lead-new`

### 4.10 Action: Owner notification

- **Action:** Send Internal Notification
- **To:** `{{custom_values.business.owner_email}}`
- **Subject:** `New lead: {{contact.first_name}} {{contact.last_name}} from {{contact.lead_source}}`
- **Body:** Brief — name, phone, email, goal, source. With a clickable contact link.

Quiet hours for owner: send email only between 7AM–10PM owner-local time. If outside, queue for 7AM. (Use a Wait action with conditional release if your GHL supports it; otherwise, accept that the owner may get an off-hours email — they can choose to silence.)

### 4.11 Action: Wait 5 minutes → check reply

- **Action:** Wait — 5 minutes
- **Action:** If/Else — has contact replied to Email?
  - **Yes branch:** Add tag `lead-responded`, exit workflow (the trial-booking workflow takes over)
  - **No branch:** Continue to next action

### 4.12 Action: Wait 2 hours → second Email nudge

- **Action:** Wait — 2 hours
- **Action:** If/Else — does contact have tag `trial-claimed` OR `lead-responded`?
  - **Yes branch:** Exit workflow
  - **No branch:** Send Email — message **B — 2hr Nudge** from [assets](assets)

### 4.13 Action: Wait 24 hours → final email + handoff to long nurture

- **Action:** Wait — 24 hours
- **Action:** If/Else — does contact have tag `trial-claimed` OR `lead-responded`?
  - **Yes branch:** Exit
  - **No branch:** Send email "24hr Soft Follow-Up" from [assets/emails.md](assets/emails.md), then exit (handed off to a longer drip nurture — out of scope for #01)

### 4.14 Publish

Click **Save** then **Publish**. Toggle the workflow ON.

---

## Step 5 — Verify Source Attribution (10 min)

Lead source needs to populate correctly from URL parameters. Configure:

### 5.1 UTM-to-field mapping

For paid ad URLs, append:

- Instagram: `?lead_source=Instagram&lead_source_detail={{campaign_id}}`
- Facebook: `?lead_source=Facebook&lead_source_detail={{campaign_id}}`
- Google: `?lead_source=Google&lead_source_detail={{keyword}}`

In the form builder, hidden fields `lead_source` and `lead_source_detail` should be configured to **read from URL parameter** of the same name.

### 5.2 Default fallbacks

For organic web traffic (no UTM):

- Hidden field `lead_source` default value = `Web Search`

For referral links (built in #08):

- Append `?lead_source=Referral&lead_source_detail={{referrer_code}}`

---

## Test Plan

Run this test sequence after publishing. **Do not declare done until all five pass.**

### Test 1 — Funnel form submission, generic source

1. Open the funnel URL in an incognito browser.
2. Fill the form with test data (use your own real phone number).
3. Submit.
4. **Expected within 5 minutes:**
   - Email arrives on your phone (message A from [assets](assets)).
   - Welcome email arrives (2 minutes after Email).
   - Owner email lands in `{{custom_values.business.owner_email}}` inbox.
5. **Expected in GHL:**
   - Contact created.
   - Tags applied: `source-web` (default), `lead-contacted`.
   - Custom fields populated: `lead_source`, `lead_captured_at`, `lead_first_response_at`.
   - Opportunity created in Membership Sales pipeline, stage "New Lead".

### Test 2 — UTM source attribution

1. Open funnel URL with `?lead_source=Instagram&lead_source_detail=spring_launch` appended.
2. Submit form.
3. **Expected:** Contact gets `source-instagram` tag (not `source-web`). `lead_source_detail` field = `spring_launch`.

### Test 3 — Walk-in tablet form

1. Open the walk-in funnel URL.
2. Submit.
3. **Expected:** Contact gets `source-walkin` tag automatically (hidden field default).

### Test 4 — No-reply nudge sequence

1. Submit a fresh test lead. Do NOT reply to the Email.
2. Wait 2 hours.
3. **Expected:** Email message B (2hr nudge) arrives.
4. Wait 24 hours from original submission (test variant: use a 24-minute delay temporarily for testing).
5. **Expected:** 24hr soft follow-up email arrives.

### Test 5 — Reply detection

1. Submit a fresh test lead.
2. Reply to the Email within 5 minutes.
3. **Expected:** No 2hr nudge Email fires. Contact gets `lead-responded` tag.

---

## Common Build Mistakes (avoid these)

1. **Form not publishing.** If submissions don't trigger the workflow, confirm: the form is *published* (not draft), the workflow's trigger filter exactly matches the form name, and the workflow is *toggled on*.
2. **Source tags not applying.** Hidden form fields default to `Web Search`, not blank. If you see `source-web` on Instagram traffic, your UTM isn't reaching the form — check the URL parameter name matches the hidden field name exactly.
3. **Email not firing.** Confirm the GHL phone number is provisioned and the contact's phone is in valid format. Test by sending a manual Email first.
4. **Owner getting flooded.** Confirm the owner notification fires only ONCE per lead (not once per workflow re-entry). Use the "Contact does not have tag `lead-contacted`" filter on the trigger.
5. **Duplicate opportunities.** If a lead fills the form twice, you get two opportunities. Add a workflow filter: "If contact already has an open opportunity in Membership Sales, skip the Create Opportunity step."

---

## What's Next

Once this is live and verified:

- Leads that book a trial are picked up by **[#02 Trial-to-Paid Conversion](../02-trial-to-paid-conversion/build.md)**.
- Source attribution data flows into **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)**.
- Referred leads (with `source-referral` and `referred_by_contact_id` populated) trigger reward credits via **[#08 Referral Engine](../08-referral-engine/build.md)**.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
