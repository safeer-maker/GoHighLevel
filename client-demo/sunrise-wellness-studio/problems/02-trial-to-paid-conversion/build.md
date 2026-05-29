# #02 — Build Playbook: Trial-to-Paid Conversion

> Step-by-step GHL build. Estimated time: **2.5 hours** for a competent operator. Prerequisites listed first — do not skip them. This build assumes [#01 Lead Capture](../01-lead-capture-and-instant-response/build.md) is already live.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting. If anything is missing, build it first.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Lead Info fields (`lead_status`, `lead_source`, `lead_captured_at`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Carried over from #01 |
| Fitness Profile fields (`fitness_goal_primary`, `fitness_experience`, `assigned_trainer`) | Same | Personalized class recommendations |
| Membership Info (`membership_tier`, `membership_status`, `monthly_rate`, `membership_start_date`) | Same | Set on conversion |
| Engagement fields (`visits_last_30_days`, `total_visits_lifetime`, `last_visit_date`, `last_class_attended`) | Same | Drives attendance branching |
| Tags: `trial-claimed`, `trial-active`, `trial-attended-1`, `trial-attended-3plus`, `trial-converted`, `trial-expired`, `trial-not-now`, `campaign-trial-nurture` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Workflow gating + outcome routing |
| Pipeline: **Membership Sales**, Stages `Trial Booked`, `Trial Active`, `Conversion Offer Sent`, `Won — Paid Member`, `Lost — Trial Expired` | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Owner visibility |
| Products: **Basic Membership** ($79), **Premium Membership** ($149), **VIP Membership** ($249) | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Conversion checkout |
| Coupon: **TRIAL2PAID** (20% off first month + waive enrollment, 14-day window, single-use) | Same | Conversion offer |
| Custom values: `business.short_name`, `business.booking_url`, `team.owner_first`, `team.owner_name`, `offer.trial_conversion_discount`, `offer.first_pt_session`, `price.basic`, `price.premium`, `price.vip`, `voice.greeting_warm` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |

---

## Step 1 — Build the Conversion Offer Funnel (35 min)

### 1.1 Create the funnel

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Trial Conversion Offer`
- **Type:** 2-Step Order Form
- **Template:** Start blank

### 1.2 Build Page 1 — Offer / Sales Page

Click **+ Add Step > Landing Page**. Name it `01 — Offer`.

Full copy in **[assets/funnel.md](assets/funnel.md)**. Page structure:

- **Section 1: Hero** — Reframe headline ("Loved your trial? Lock in the studio rate.") + photo of brightly lit class
- **Section 2: What you get** — Side-by-side tier comparison (Basic / Premium / VIP) with the offer ($79 first month, $0 enrollment, 20% off)
- **Section 3: Member quotes** — 3 short testimonials from members who started on the same offer
- **Section 4: FAQ** — Cancel anytime · No long contract · Switch tiers anytime · Pause for vacations
- **Section 5: Primary CTA button** — "Lock In My Membership →" (scrolls to checkout step)

### 1.3 Build Page 2 — Checkout

Click **+ Add Step > Order Form**. Name it `02 — Checkout`.

Configure:

- **Product picker:** Show Basic, Premium, VIP as toggleable selections. Default to Basic.
- **Coupon:** Auto-apply `TRIAL2PAID`.
- **Order bump (optional):** "Add a 5-pack of PT sessions for $375 (save $50)" — small, unobtrusive checkbox.
- **Pre-fill contact:** Use URL parameter `?contact_id={{contact.id}}` so the funnel pre-fills name, email, phone from GHL.
- **Submit button:** "Complete My Membership →"

### 1.4 Build Page 3 — Confirmation

Click **+ Add Step > Thank-You Page**. Name it `03 — Welcome to Sunrise`.

Build:

- **Section 1: Confirmation** — "Welcome to the studio, {{contact.first_name}} ☀️" with member-since date
- **Section 2: What happens next** — Numbered list (your first as-a-member class, your onboarding call from Morgan, your member app login)
- **Section 3: One-click links** — Book first class · Download app · Join the member Facebook group

### 1.5 Publish & note the URL

Click **Publish**. Copy the URL.

Update custom value: `offer.conversion_funnel_url` = the published URL (add this custom value if not present).

---

## Step 2 — Build All Email Templates (40 min)

Navigate to **Marketing > Emails > Templates > + New Template**.

Build each template in **[assets/emails.md](assets/emails.md)** in order:

| Template Name | Send Day | Used in workflow step |
|---|---|---|
| `02 — Day 0 — Trial Welcome` | Day 0 | Step 4.2 |
| `02 — Day 2 — First Class Encouragement` | Day 2 | Step 4.5 |
| `02 — Day 4 — Testimonial / Social Proof` | Day 4 | Step 4.7 |
| `02 — Day 5 — Conversion Offer` | Day 5 | Step 4.9 |
| `02 — Day 7 — Last Call` | Day 7 | Step 4.12 |
| `02 — Recap — Trial Expired (Soft)` | Day 8 (handoff) | Step 4.14 |

For each: paste the subject, preview, body from `assets/emails.md`. Confirm all merge fields resolve in the preview (`{{contact.first_name}}`, `{{custom_values.offer.trial_conversion_discount}}`, etc.).

---

## Step 3 — Build All Email Templates (15 min)

Navigate to **Marketing > Templates > Email > + New Template**.

Build each template in **[assets](assets)**:

| Template Name | Send Day | Used in workflow step |
|---|---|---|
| `02 — Day 1 — Booking Check` | Day 1 | Step 4.4 |
| `02 — Day 4 — Class Nudge` | Day 4 | Step 4.7 |
| `02 — Day 6 — Personal from Morgan` | Day 6 | Step 4.10 |
| `02 — Day 7 — Last Call Email` | Day 7 | Step 4.12 |

---

## Step 4 — Build the 7-Day Trial Nurture Workflow (60 min)

The heart of this problem. Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `02 — Trial Nurture — 7 Day Conversion`
- **Folder:** Create folder `02 - Trial Conversion`

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 4.1 Trigger

Click **+ Add New Workflow Trigger**.

- **Trigger:** Tag Added
- **Filter:** Tag is `trial-claimed`
- **Filter:** Contact does NOT have tag `member-active`
- **Filter:** Contact does NOT have tag `campaign-trial-nurture` (prevents double-entry)

### 4.2 Action: Setup (tag + opportunity + Day 0 send)

- **Action:** Add Tag → `campaign-trial-nurture`
- **Action:** Update Contact Field → `lead_status` = `Trial Active`
- **Action:** Update Opportunity Stage → Pipeline `Membership Sales` → Stage `Trial Active`
- **Action:** Send Email → Template `02 — Day 0 — Trial Welcome`
- **Action:** Send Email → Day-0 short welcome (uses Template from #01 Email message A pattern, OR build a 02-Day-0 Email — see [assets](assets))

### 4.3 Action: Wait until Day 1, 10 AM contact-local

- **Action:** Wait — Until specific time
- **Wait until:** `lead_captured_at + 1 day` at 10:00 AM contact-local

### 4.4 Action: Day 1 Email check-in (with branch)

- **Action:** If/Else — has contact attended a class? (`last_visit_date` >= `lead_captured_at`)
  - **Yes branch:** Send Email `02 — Day 1 — Class Confirmation` ("loved having you in class!")
  - **No branch:** Send Email `02 — Day 1 — Booking Check` ("did you grab a class slot yet?")

### 4.5 Action: Wait until Day 2, 8 AM

- **Action:** Wait — Until specific time → Day 2 at 8 AM contact-local
- **Action:** Send Email → Template `02 — Day 2 — First Class Encouragement`

(Note: the email template itself has conditional sections — one block for "haven't been in yet" and one for "loved having you" — driven by an If/Else logic block in the email builder reading `total_visits_lifetime`.)

### 4.6 Action: Wait until Day 4, 9 AM

- **Action:** Wait — Until specific time → Day 4 at 9 AM contact-local

### 4.7 Action: Day 4 emails Nudge

- **Action:** Send Email → Template `02 — Day 4 — Testimonial / Social Proof`
- **Action:** Wait 4 hours
- **Action:** If/Else — does contact have `trial-attended-3plus`?
  - **Yes branch:** Skip the nudge Email (they're already in love)
  - **No branch:** Send Email `02 — Day 4 — Class Nudge`

### 4.8 Action: Wait until Day 5, 10 AM

- **Action:** Wait — Until specific time → Day 5 at 10 AM contact-local

### 4.9 Action: Day 5 Conversion Offer (the big one)

- **Action:** Update Opportunity Stage → `Conversion Offer Sent`
- **Action:** Send Email → Template `02 — Day 5 — Conversion Offer`

The email contains the coupon code `TRIAL2PAID` and a direct CTA to the conversion funnel built in Step 1.

### 4.10 Action: Wait until Day 6, 2 PM → Personal Email from Morgan

- **Action:** Wait — Until specific time → Day 6 at 2 PM contact-local
- **Action:** If/Else — does contact have `trial-converted`?
  - **Yes branch:** Exit workflow (success)
  - **No branch:** Send Email `02 — Day 6 — Personal from Morgan`

This Email is intentionally human-toned — "hey, just wanted to ask before your trial wraps — any questions or concerns I can answer?"

### 4.11 Action: Wait until Day 7, 9 AM

- **Action:** Wait — Until specific time → Day 7 at 9 AM contact-local

### 4.12 Action: Day 7 Last Call (emails)

- **Action:** If/Else — does contact have `trial-converted`?
  - **Yes branch:** Exit workflow
  - **No branch:**
    - Send Email → Template `02 — Day 7 — Last Call`
    - Wait 4 hours
    - Send Email `02 — Day 7 — Last Call Email`

### 4.13 Action: Wait 12 hours → Outcome Router

- **Action:** Wait — 12 hours
- **Action:** If/Else — `trial-converted` exists?
  - **Yes branch:** → Action 4.14a (Conversion Path)
  - **No branch:** check `trial-not-now`
    - **Yes:** → Action 4.14b (Not Now Path)
    - **No:** → Action 4.14c (Silent Expiration Path)

### 4.14 Action: Outcome Routing

**4.14a — Conversion Path:**
- Update Opportunity Stage → `Won — Paid Member`
- Opportunity Status → `Won`
- Update Contact Field → `membership_start_date` = today
- Update Contact Field → `membership_status` = `Active`
- Update Contact Field → `membership_tier` = (set by checkout product purchase trigger)
- Add Tag → `member-active`, `member-onboarding`
- Add to Workflow → `04 — New Member Onboarding`
- Remove Tag → `campaign-trial-nurture`
- Exit Workflow

**4.14b — Not Now Path:**
- Add Tag → `trial-not-now`
- Update Contact Field → `lead_status` = `Lost`
- Add to Workflow → `Long-Tail Nurture — 30 Day Drip` (separate)
- Remove Tag → `campaign-trial-nurture`
- Exit Workflow

**4.14c — Silent Expiration Path:**
- Add Tag → `trial-expired`
- Update Opportunity Stage → `Lost — Trial Expired`
- Opportunity Status → `Lost`
- Send Email → Template `02 — Recap — Trial Expired (Soft)` (a soft "your pass is over, here if you ever want to come back")
- Add to Workflow → `Long-Tail Nurture — 30 Day Drip`
- Remove Tag → `campaign-trial-nurture`
- Exit Workflow

### 4.15 Publish

Click **Save** then **Publish**. Toggle ON.

---

## Step 5 — Wire Reply Detection (10 min)

Build a small companion workflow to handle replies during the trial nurture.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `02 — Trial Reply Handler`
- **Trigger:** Inbound Email received
- **Filter:** Contact has tag `campaign-trial-nurture`

**Actions:**

1. **If/Else — message body contains "not now" / "no thanks" / "stop trying" / "later":**
   - **Yes:** Add Tag `trial-not-now`, send auto-reply: *"All good, {{first_name}} — no pressure. I'll stop the nudges. Your trial info stays in our system if you change your mind. — Morgan"*. Exit main nurture workflow.
2. **Else If — body contains "yes" / "interested" / "sign me up" / "i'm in":**
   - Send auto-reply: *"Amazing! Tap here to lock it in: {{custom_values.offer.conversion_funnel_url}}"*. Tag `trial-warm`.
3. **Else (general question):**
   - Internal notification to `{{custom_values.business.owner_email}}`: "Trial member {{contact.first_name}} replied — please respond personally."
   - Add Tag `trial-needs-personal-touch`.

---

## Step 6 — Wire Conversion Detection (10 min)

When a trial member completes purchase on the conversion funnel, fire the conversion path.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `02 — Trial Conversion Detected`
- **Trigger:** Order Submitted
- **Filter:** Product is `Basic Membership` OR `Premium Membership` OR `VIP Membership`
- **Filter:** Contact has tag `campaign-trial-nurture` (i.e., this purchase came from a trial, not a cold buyer)

**Actions:**

1. Add Tag `trial-converted`
2. Update Contact Field `membership_tier` based on product:
   - Basic → `Basic`, `monthly_rate` = $79
   - Premium → `Premium`, `monthly_rate` = $149
   - VIP → `VIP`, `monthly_rate` = $249
3. Add Tag `tier-basic` / `tier-premium` / `tier-vip` accordingly (If/Else chain)
4. The main nurture workflow's Day 7 outcome router (Action 4.13/4.14a) sees `trial-converted` and runs the conversion path.

---

## Test Plan

Run this sequence after publishing. **Do not declare done until all six pass.**

### Test 1 — Trial pass claimed, workflow enters correctly

1. On a test contact, manually add the tag `trial-claimed`.
2. **Expected within 60 seconds:**
   - Day 0 welcome email arrives.
   - Day 0 Email arrives.
   - Tag `campaign-trial-nurture` applied.
   - Contact field `lead_status` = `Trial Active`.
   - Opportunity moved to "Trial Active" stage in Membership Sales pipeline.

### Test 2 — Day 1 Email branch (attended vs not)

1. Test contact A: leave `last_visit_date` blank, fast-forward workflow to Day 1.
2. **Expected:** Email `02 — Day 1 — Booking Check` ("did you grab a class slot yet?")
3. Test contact B: set `last_visit_date` = today, increment `total_visits_lifetime` to 1, fast-forward.
4. **Expected:** Email `02 — Day 1 — Class Confirmation` ("loved having you in class!")

### Test 3 — Day 4 attendance-based skip

1. Test contact: simulate 3 class attendances; add tag `trial-attended-3plus`.
2. Fast-forward to Day 4.
3. **Expected:** Day 4 email arrives, but Day 4 nudge Email does NOT fire (skipped by branch).

### Test 4 — Conversion path (happy)

1. Test contact: fast-forward to Day 5.
2. Confirm conversion offer email arrives with `TRIAL2PAID` coupon.
3. Click the email CTA, complete checkout on conversion funnel with a Stripe test card.
4. **Expected:**
   - Tag `trial-converted`, `member-active`, `member-onboarding`, `tier-basic` (or matching tier) all applied.
   - `membership_start_date` set to today.
   - Opportunity moved to `Won — Paid Member`.
   - Contact enrolled in workflow `04 — New Member Onboarding`.
   - Tag `campaign-trial-nurture` removed.

### Test 5 — Not-now reply

1. Test contact: at Day 4 of the workflow, reply to any Email with the text "not now thanks."
2. **Expected:**
   - Auto-reply from Morgan-voice script fires.
   - Tag `trial-not-now` applied.
   - Main nurture workflow exits.
   - Contact enrolled in long-tail nurture.

### Test 6 — Silent expiration

1. Test contact: never reply, never attend, never convert. Fast-forward to Day 8.
2. **Expected:**
   - Tag `trial-expired` applied.
   - Opportunity moved to `Lost — Trial Expired`.
   - Recap "soft goodbye" email arrives.
   - Contact enrolled in long-tail nurture.

---

## Common Build Mistakes (avoid these)

1. **Double-entry into the workflow.** If a contact gets `trial-claimed` re-applied (front desk re-clicks it), the workflow restarts. Use the trigger filter "Contact does NOT have tag `campaign-trial-nurture`" to prevent.
2. **Conversion not firing.** If a trial buys via the funnel but the `trial-converted` tag never gets applied, check Step 6's wiring — the Order Submitted trigger must filter for the right products AND the `campaign-trial-nurture` tag.
3. **Quiet hours violated on Day 6 personal Email.** The Day 6 Email is the most "human" message — sending it at 11 PM destroys the effect. Set the wait at Step 4.10 to specifically 2 PM contact-local.
4. **Coupon already used.** If a contact attempts the conversion funnel twice, GHL rejects the coupon. Build the funnel with a fallback message: *"Coupon already redeemed — but you can still purchase at the regular price."*
5. **Owner notification spam on Day 6.** Day 6 fires the personal Email for every trial. If the owner wants to *approve* before send, change Step 4.10 to send an internal notification ("ready to send to {{first_name}} — approve in Conversations") instead of auto-firing.

---

## What's Next

Once this is live and verified:

- Trials that convert flow into **[#04 New Member Onboarding](../04-new-member-onboarding/build.md)** automatically.
- Trial-to-paid conversion rate appears on the **[#10 Owner Dashboard](../10-owner-reporting-and-visibility/build.md)**.
- Silent expirations feed the long-tail "Trial Expired — 30 Day Drip" workflow, which pings monthly with class highlights, success stories, and the next seasonal offer.
- For trials referred by an existing member (`source-referral`), the conversion event also fires the [#08 Referral Engine](../08-referral-engine/build.md) reward credit for the referrer.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
