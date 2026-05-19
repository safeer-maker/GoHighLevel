# #09 — Build Playbook: Win-Back Lapsed Members

> Step-by-step GHL build. Estimated time: **180 minutes** for a competent operator. Two workflows, one checkout funnel, three coupons (already in shared-foundation), Stripe webhook configuration. Prerequisites listed first.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting. If anything is missing, build it first.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Membership Info fields: `membership_status`, `membership_cancel_date`, `cancel_reason`, `monthly_rate`, `ltv_to_date`, `days_as_member`, `membership_tier` | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Routing logic, value math |
| Tags: `member-cancelled`, `member-lapsed`, `member-reactivated`, `campaign-winback-d30`, `campaign-winback-d60`, `campaign-winback-d90` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Sequence stage markers |
| Pipeline: **Retention** with Win-Back D30 / D60 / D90 / Reactivated / Permanent Loss stages | [../../shared-foundation/pipelines.md](../../shared-foundation/pipelines.md) | Owner-visible kanban |
| Custom values: `business.short_name`, `team.owner_first`, `offer.winback_d30`, `offer.winback_d60`, `offer.winback_d90`, `business.booking_url` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| Coupons: `WB30`, `WB60`, `WB90LAST` | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Auto-applied at checkout |
| Products: Basic ($79), Premium ($149), VIP ($249) memberships | Same | Re-purchase targets |
| Stripe integration in GHL Payments | GHL Settings > Payments | Source of failed-payment events |

---

## Step 1 — Configure Cancellation Capture (20 min)

Before win-back can run, the studio needs a clean way to register cancellations with a reason. This drives all downstream routing.

### 1.1 Build the Cancellation Form (if not already in place)

Navigate to **Sites > Forms > + Build Form**.

- **Form Name:** `Membership Cancellation Request`
- **Used on:** A page accessible from the member portal AND from a "Cancel Membership" link in renewal-warning emails.

Fields:

| # | Field | Type | Required | Maps to |
|---|---|---|---|---|
| 1 | First name | Text | ✅ | `contact.first_name` |
| 2 | Email | Email | ✅ | `contact.email` |
| 3 | Why are you cancelling? | Dropdown | ✅ | `cancel_reason` |
| 4 | Anything else you want to share? | Multi-line text | ❌ | `cancel_notes` (new field — Multi-line, Engagement folder) |
| 5 | Confirm cancellation | Checkbox | ✅ | (form validation only) |

**Field 3 dropdown options** (matches `cancel_reason` field options in shared-foundation):

- Cost
- Time / schedule
- Moved away
- Injury
- Switched to another studio
- Not using it enough
- Failed Payment (hidden — only set programmatically via Stripe webhook, not user-selectable)
- Other

**On submit:** Workflow trigger fires (Step 2 below).

### 1.2 Configure Stripe Failed-Payment Webhook

Navigate to **Settings > Integrations > Payments > Stripe > Webhooks**.

Add webhook event: `invoice.payment_failed`

GHL workflow trigger configuration:
- Listen for: Payment failed event
- On fire: Update contact field `cancel_reason` = `Failed Payment`, add tag `payment-failed-pending`

This tag is the gate for the Failed-Payment Intervention workflow (Step 4). It is *not* the same as `member-cancelled` — we don't cancel the member yet; we try to recover.

---

## Step 2 — Build the Cancellation-Processing Workflow (15 min)

This is the "cancellation handler" — a thin workflow that fires on cancellation-form submit, records the event, and routes to the right downstream workflow.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `09a — Cancellation Handler`
- **Folder:** Create folder `09 - Win-Back` and put it there

### 2.1 Trigger

- **Trigger:** Form Submitted
- **Filter:** Form is `Membership Cancellation Request`

### 2.2 Actions

1. **Update Contact Field** — `membership_status` = `Cancelled`
2. **Update Contact Field** — `membership_cancel_date` = `{{now}}`
3. **Add Tag** — `member-cancelled`
4. **Remove Tag** — `member-active`
5. **Move Retention pipeline opportunity** — to stage "Lost — Cancelled"
6. **Send Internal Notification** to owner — "Member cancelled: {{contact.first_name}} {{contact.last_name}}, reason: {{contact.cancel_reason}}. {{contact.cancel_notes}}"
7. **Branch on cancel_reason:**
   - If `Moved` OR `Injury` → enroll in **Quiet Track** (Day-1 goodbye only)
   - Else → enroll in **Workflow `09b — Win-Back Sequence (Voluntary)`** (Step 3 below)

### 2.3 Publish

---

## Step 3 — Build the Win-Back Sequence (Voluntary) Workflow (60 min)

This is the centerpiece — the 90-day reactivation campaign.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `09b — Win-Back Sequence (Voluntary)`
- **Folder:** `09 - Win-Back`

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 3.1 Trigger

- **Trigger:** Workflow enrollment (called by `09a` Cancellation Handler) — OR — Contact Tag Added: `member-cancelled` (with cancel_reason filter)
- **Filter:** `cancel_reason` is NOT `Moved` AND NOT `Injury` AND NOT `Failed Payment`

### 3.2 Action: Day 1 — Gentle Goodbye Email

- **Action:** Send Email
- **Template:** Email 1 "Day-1 Gentle Goodbye" from [assets/emails.md](assets/emails.md)
- **Wait before:** None — fires immediately on enrollment

No SMS on Day 1. Voluntary cancels need a *quiet* day-1, not a notification cascade.

### 3.3 Wait: 30 days (the silent period)

- **Action:** Wait — 30 days
- **Respect contact-local time:** Yes — release at 10 AM contact-local

### 3.4 Day 30 — Branch Check Before Re-Engagement

- **Action:** If/Else — has contact tag `member-reactivated`?
  - **Yes:** Exit workflow (they came back on their own)
  - **No:** Continue

### 3.5 Day 30 — Apply Sequence Tag

- **Action:** Add Tag — `member-lapsed` (the 30-day-past-cancel marker)
- **Action:** Add Tag — `campaign-winback-d30`
- **Action:** Move Retention pipeline opportunity — to stage "Win-Back D30"

### 3.6 Day 30 — Send Check-In SMS

- **Action:** Send SMS
- **Template:** SMS A "Day-30 Light Check-In" from [assets/sms.md](assets/sms.md)
- **Skip if:** Contact has `do-not-sms`

### 3.7 Day 30 — Wait 30 min, Send Check-In Email

- **Action:** Wait — 30 minutes
- **Action:** Send Email
- **Template:** Email 2 "Day-30 We Miss You" from [assets/emails.md](assets/emails.md)

### 3.8 Wait: 30 days (to Day 60)

- **Action:** Wait — 30 days
- **Respect contact-local time:** Yes

### 3.9 Day 60 — Branch Check + Sequence Tag

- **Action:** If/Else — has contact tag `member-reactivated`?
  - **Yes:** Exit workflow
  - **No:** Continue
- **Action:** Remove Tag — `campaign-winback-d30`
- **Action:** Add Tag — `campaign-winback-d60`
- **Action:** Move Retention pipeline opportunity — to stage "Win-Back D60"

### 3.10 Day 60 — Send Comeback Offer

- **Action:** Send SMS — SMS B "Day-60 Comeback Offer" from [assets/sms.md](assets/sms.md)
- **Action:** Wait — 30 minutes
- **Action:** Send Email — Email 3 "Day-60 Comeback Offer" from [assets/emails.md](assets/emails.md)

Both messages include a link to the Comeback Offer Funnel with `?wb=60` parameter (auto-applies WB60 coupon).

### 3.11 Wait: 30 days (to Day 90)

- **Action:** Wait — 30 days
- **Respect contact-local time:** Yes

### 3.12 Day 90 — Branch Check + Sequence Tag

- **Action:** If/Else — has contact tag `member-reactivated`?
  - **Yes:** Exit workflow
  - **No:** Continue
- **Action:** Remove Tag — `campaign-winback-d60`
- **Action:** Add Tag — `campaign-winback-d90`
- **Action:** Move Retention pipeline opportunity — to stage "Win-Back D90"

### 3.13 Day 90 — Send Last-Call Offer

- **Action:** Send SMS — SMS C "Day-90 Last Call" from [assets/sms.md](assets/sms.md)
- **Action:** Wait — 30 minutes
- **Action:** Send Email — Email 4 "Day-90 Last Call" from [assets/emails.md](assets/emails.md)

Coupon: WB90LAST (auto-applied via `?wb=90`).

### 3.14 Wait: 30 days (to Day 120 — final)

- **Action:** Wait — 30 days
- **Action:** If/Else — has contact tag `member-reactivated`?
  - **Yes:** Exit workflow
  - **No:** Add Tag `member-permanent-loss`, Move Retention pipeline to "Permanent Loss" stage, exit to long-tail nurture

### 3.15 Publish

---

## Step 4 — Build the Failed-Payment Intervention Workflow (45 min)

This is the highest-leverage workflow in the system — recovering involuntary cancellations *before* they become voluntary ones.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `09c — Failed-Payment Intervention`
- **Folder:** `09 - Win-Back`

### 4.1 Trigger

- **Trigger:** Contact Tag Added: `payment-failed-pending` (applied by the Stripe webhook from Step 1.2)

### 4.2 Action: Stamp the Event

- **Action:** Update Contact Field — `cancel_reason` = `Failed Payment`
- **Action:** Update Contact Field — Custom field `payment_failed_at` (new field — Date & Time, Engagement folder) = `{{now}}`

### 4.3 Action: Send Intervention SMS Within 1 Hour

- **Action:** Wait — until 60 minutes elapsed (use 1-hour wait, respect 8 AM – 9 PM contact-local; if outside window, hold until 8 AM)
- **Action:** Send SMS
- **Template:** SMS D "Failed Payment Immediate Intervention" from [assets/sms.md](assets/sms.md)
- **Skip if:** `do-not-sms` (rare for an active member, but check)

### 4.4 Action: Send Intervention Email Same Time

- **Action:** Send Email
- **Template:** Email 5 "Failed Payment Intervention" from [assets/emails.md](assets/emails.md)

### 4.5 Action: Wait 24 Hours, Check Recovery

- **Action:** Wait — 24 hours
- **Action:** If/Else — has contact tag `payment-failed-pending` been removed (by successful Stripe retry)?
  - **Yes (recovered):** Add Tag `payment-recovered`, send "thanks for fixing that" SMS, exit workflow
  - **No:** Continue

### 4.6 Action: Day 2 Reminder

- **Action:** Send SMS — "Quick heads up — your card's still declining. One tap to fix: [funnel link with `?wb=update`]"
- **Action:** Send Email — same message, longer

### 4.7 Action: Wait 24 Hours, Final Check

- **Action:** Wait — 24 hours (total 48 hours)
- **Action:** If/Else — recovered?
  - **Yes:** Exit
  - **No:** Apply `member-cancelled` tag, set `cancel_reason` = `Failed Payment`, route to voluntary win-back at Day 30 stage (skip Days 1–29)

### 4.8 Publish

---

## Step 5 — Build the Comeback Offer Funnel (30 min)

This is the checkout page lapsed members land on from the win-back messages.

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Comeback Offer`
- **Type:** Checkout
- **Template:** Start blank

### 5.1 Build the Single Checkout Page

Click **+ Add Step > Checkout Page**. Name it `01 — Comeback Checkout`.

Build per **[assets/funnel.md](assets/funnel.md)**. Critical elements:

- Headline reads the URL parameter `?wb=30|60|90` and personalizes the offer ("First month back at 50% off" vs "$39 first month" vs "$29 first month — this week only")
- Embed the Basic Membership product checkout
- Auto-apply coupon based on URL param:
  - `?wb=30` → WB30 (50% off)
  - `?wb=60` → WB60 ($39 + waived enrollment)
  - `?wb=90` → WB90LAST ($29 + waived enrollment)

### 5.2 Coupon Auto-Application Mechanism

In GHL Checkout settings:
- **Discount code field:** Hidden by default (the URL param applies it programmatically)
- **Pre-applied coupon source:** URL parameter `wb` mapped via a lookup table (JS snippet on the page):

```javascript
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const wb = new URLSearchParams(window.location.search).get('wb');
    const couponMap = { '30': 'WB30', '60': 'WB60', '90': 'WB90LAST' };
    const code = couponMap[wb];
    if (code) {
      // Apply via GHL checkout API or hidden coupon input
      document.querySelector('input[name="coupon"]').value = code;
      document.querySelector('input[name="coupon"]').dispatchEvent(new Event('change'));
    }
  });
</script>
```

If GHL exposes native "Coupon from URL parameter" in checkout settings, use that instead — simpler and more reliable.

### 5.3 Confirmation Page

On successful purchase:
- Redirect to a "Welcome back!" thank-you page (built as Page 2 of the funnel)
- Page content: warm welcome, "We'll see you soon — book your first class now: [link]"

### 5.4 Publish & Note URLs

The three URLs sent in win-back messages:

- Day 30: `https://book.sunrisewellness.com/comeback?wb=30`
- Day 60: `https://book.sunrisewellness.com/comeback?wb=60`
- Day 90: `https://book.sunrisewellness.com/comeback?wb=90`

---

## Step 6 — Wire Reactivation Detection (15 min)

When a lapsed member completes checkout, the system must detect and react cleanly.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `09d — Reactivation Detection`
- **Folder:** `09 - Win-Back`

### 6.1 Trigger

- **Trigger:** Order Placed (Stripe payment succeeded)
- **Filter:** Contact has tag `member-cancelled` OR `member-lapsed`

### 6.2 Actions

1. **Add Tag** — `member-reactivated` (permanent badge)
2. **Add Tag** — `member-active`
3. **Remove Tags** — `member-cancelled`, `member-lapsed`, `campaign-winback-d30`, `campaign-winback-d60`, `campaign-winback-d90`
4. **Update Contact Field** — `membership_status` = `Active`, `membership_start_date` = `{{now}}` (fresh start)
5. **Move Retention pipeline** — to "Reactivated" (Won) stage
6. **Create new Onboarding pipeline opportunity** — at "Welcome Sent (Day 0)" stage
7. **Send celebration SMS** to member — "{{contact.first_name}} — welcome back ☀️ Book your first class: {{custom_values.business.booking_url}}"
8. **Send celebration email** — "Welcome back. Genuinely glad you're here."
9. **Owner internal notification** — "REACTIVATION: {{contact.first_name}} {{contact.last_name}} just came back. Tier: {{contact.membership_tier}}. Save them a personal hello next time they're in."

### 6.3 Publish

---

## Test Plan

Run this complete test sequence. **Do not declare done until all six pass.**

### Test 1 — Voluntary cancellation routes correctly

1. Create a test contact with `member-active` tag.
2. Submit the cancellation form with reason "Cost".
3. **Expected:**
   - `member-cancelled` tag applied
   - `cancel_reason` = `Cost`
   - Retention pipeline moves to "Lost — Cancelled"
   - Workflow `09b` triggers
   - Day-1 goodbye email arrives within 60 seconds
4. Fast-forward: in test mode, set the Day-30 wait to 1 minute. Verify SMS A + Email 2 arrive after the wait.

### Test 2 — Quiet track for "Moved" reason

1. Create another test contact, cancel with reason "Moved away".
2. **Expected:**
   - `member-cancelled` applied
   - Day-1 goodbye email arrives
   - NO subsequent messages at Day 30, 60, 90
   - Retention pipeline stays in "Lost — Cancelled" (no Win-Back stages applied)

### Test 3 — Failed-payment intervention fires within 1 hour

1. Simulate a Stripe `invoice.payment_failed` event for a test member (use Stripe test mode with a card that auto-declines, e.g., `4000000000000341`).
2. **Expected:**
   - `payment-failed-pending` tag applied
   - `cancel_reason` = `Failed Payment`
   - Within 60 minutes: SMS D + Email 5 arrive with one-tap card-update link
   - `member-cancelled` is NOT applied yet (member is still active, in recovery window)

### Test 4 — Failed-payment recovery exits workflow

1. From Test 3 state, simulate Stripe `invoice.payment_succeeded` (via Stripe dashboard "retry payment").
2. **Expected:**
   - `payment-failed-pending` tag removed
   - `payment-recovered` tag applied
   - "Thanks for fixing that" SMS arrives
   - Member stays `member-active`
   - No further win-back messages

### Test 5 — Failed-payment non-recovery transitions to voluntary track

1. From Test 3 state, don't recover. Wait 48 hours (or fast-forward in test mode).
2. **Expected:**
   - `member-cancelled` tag applied
   - `cancel_reason` stays `Failed Payment`
   - Workflow `09b` enrolls at Day 30 stage directly (skips Days 1–29 of voluntary track)
   - Day-30 messages arrive

### Test 6 — Comeback checkout reactivates cleanly

1. From any lapsed test contact (Test 1, 2, or 5 state, ideally past Day 30 with `campaign-winback-d30` tag).
2. Open the comeback URL with `?wb=30`.
3. **Expected:**
   - Coupon WB30 auto-applied at checkout (visible in price preview)
   - Headline reads "first month back at 50% off"
4. Complete checkout with Stripe test card.
5. **Expected:**
   - `member-reactivated` tag applied
   - `member-active` re-applied
   - All campaign-winback-* tags removed
   - Retention pipeline moves to "Reactivated" (Won)
   - New Onboarding pipeline opportunity created
   - Welcome-back SMS + email arrive
   - Owner internal notification fires
   - Workflow `09b` exits cleanly at next branch check

---

## Common Build Mistakes

1. **Day-1 message too aggressive.** Voluntary cancels get a *gentle* goodbye on Day 1 — no offer, no "we'd love to win you back" pitch. Just acknowledge they're leaving, wish them well. Pitching too early breeds resentment and damages reactivation odds at Day 30.
2. **Failed-payment SMS goes to `do-not-sms` contacts.** The SMS workflow skips them — but the email *must* still fire. Failed payment is operationally critical; the contact will be silently cancelled if neither channel works. Add a fallback: if both `do-not-sms` AND `do-not-email`, fire an owner-internal alert for manual phone call.
3. **`cancel_reason = Moved` still gets win-back offers.** Common bug: the workflow trigger filter is on tag presence (`member-cancelled`), not on `cancel_reason`. Result: someone who said "I moved away" gets a "first month back at 50% off!" message — disrespectful and tone-deaf. Always filter on `cancel_reason` at trigger time.
4. **Coupon auto-apply silently fails.** If the URL is `?wb=60` but coupon `WB60` isn't applied at checkout, member sees full price and bounces. Test every coupon URL after launch. Set up a smart list "Comeback Checkouts Without Coupon" to catch silent failures.
5. **Reactivation re-enrolls in voluntary win-back workflow.** When a member reactivates mid-sequence, the workflow's branch checks (Step 3.4, 3.9, 3.12, 3.14) catch it and exit. If those checks are missing, the reactivated member keeps getting "we miss you" messages until day 120. Always include the `member-reactivated` check at every wait-block exit point.
6. **Stripe webhook not configured.** The single biggest failure mode: failed-payment events fire in Stripe but never reach GHL because the webhook isn't subscribed or the secret is wrong. Test by triggering a manual decline in Stripe test mode and watching GHL's webhook log.

---

## What's Next

Once this is live and verified:

- Reactivated members flow into **[#04 New Member Onboarding](../04-new-member-onboarding/build.md)** for a fresh 30-day onboarding (treated as a new member, not a "welcome back drip").
- Reactivation revenue and lapsed-member counts flow into **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)** dashboard.
- Quarterly: review the "Permanent Loss" stage of the Retention pipeline. Members in that bucket get a final hand-written postcard from Morgan every January — out of automation scope, but a meaningful gesture that occasionally produces a reactivation 18 months later.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
