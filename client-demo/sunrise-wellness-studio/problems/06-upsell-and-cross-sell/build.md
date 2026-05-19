# #06 — Build Playbook: Upsell & Cross-Sell

> Step-by-step GHL build. Estimated time: **3 hours** for a competent operator. The build has four offer paths in one workflow, plus a checkout funnel. Build the workflow first with one offer end-to-end, test it, then add the others in parallel branches.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Fitness Profile fields (`nutrition_interest`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Gating nutrition offers |
| Membership Info fields (`membership_tier`, `monthly_rate`, `days_as_member`) | Same | Tier check, day-21 gate |
| Engagement & Activity fields (`visits_last_30_days`, `total_pt_sessions`, `last_pt_session_date`) | Same | Behavioral triggers |
| Tags: `tier-basic`, `tier-premium`, `tier-vip`, `interest-pt`, `interest-nutrition`, `interest-vip`, `upsell-recent`, `upsell-converted-*`, `upsell-declined-*`, `do-not-market`, `save-mature-30d`, `risk-healthy` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Segmentation + gating |
| Custom values: `offer.upgrade_basic_to_premium`, `offer.first_pt_session`, `price.basic`, `price.premium`, `price.vip`, `service.nutrition_starter`, `team.nutritionist`, `team.owner_first`, `business.booking_url` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| Products: **Premium Membership** (SKU `MEM-PREMIUM`), **VIP Membership** (SKU `MEM-VIP`), **Nutrition Starter Consult** (SKU `NUT-STARTER`), **4-Week Custom Nutrition Plan** (SKU `NUT-PLAN-4WK`) | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Checkout targets |
| Coupons: optional `UPGRADE10` (10% off first month at upgrade) — create if not present | Same | Conversion incentive |
| Output of [#05 Retention](../05-retention-and-churn-prevention/) — `risk-*` tags populated nightly | [#05](../05-retention-and-churn-prevention/) | Excludes at-risk members from upsell |
| Output of [#04 Onboarding](../04-new-member-onboarding/) — `days_as_member` accurate | [#04](../04-new-member-onboarding/) | Day-21 trigger |

---

## Step 1 — Build the Premium Upgrade Checkout Funnel (40 min)

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Premium Upgrade Checkout`
- **Type:** Sales (Checkout)
- **Template:** Start blank

### 1.1 Page 1 — Upgrade Landing

Click **+ Add Step > Landing Page**. Name `01 — Why Premium`.

This is a one-page funnel — landing + form/checkout combined. Full copy in **[assets/funnel.md](assets/funnel.md)**. Structure:

- **Section 1: Personalized Hero** — H1 dynamically inserts the member's name and attendance stat ("Sarah, you attended 14 classes last month. Premium fits."). Uses contact merge fields rendered server-side via URL params.
- **Section 2: The Savings Calculator** — interactive widget that asks "How many PT sessions do you do per month?" and "Do you ever buy nutrition consults?" then shows the math: "You'd spend $X/mo if you stayed on Basic + add-ons. Premium is $149. You'd save $Y."
- **Section 3: What Premium Gets You** — 5-bullet list comparing Basic vs Premium side-by-side.
- **Section 4: Member Testimonials** — 2 quotes from members who upgraded.
- **Section 5: Checkout block** — direct Stripe checkout for **Premium Membership** with optional coupon `UPGRADE10` pre-filled.
- **Section 6: "Not Sure?" Reassurance** — small footer: "Downgrade back to Basic anytime. Pro-rated. No hassle."

### 1.2 Page 2 — Thank-You / Onboarding

Click **+ Add Step > Thank-You Page**. Name `02 — Welcome to Premium`.

Structure:

- **H1:** "Welcome to Premium, {{contact.first_name}} ☀️"
- **Body:** "Your new tier is active starting now. Here's what to do this week..."
- **3-card layout:** (1) Book your first PT session (calendar link); (2) Book your nutrition starter consult (calendar link); (3) Try one new class style this week.
- **CTA:** Book PT (primary), Book Nutrition (secondary).
- **Footer:** "Questions? Reply to your welcome SMS or text Morgan at {{custom_values.business.sms_number}}."

### 1.3 Publish

Click **Publish**. Note the URL — used as the destination for the Basic→Premium SMS and email CTA buttons. Save as `business.upgrade_url` in **Settings > Custom Values** if not already present (otherwise reference via the published funnel URL directly).

### 1.4 Build a similar funnel for VIP

Duplicate the Premium funnel: **Sunrise — VIP Upgrade Checkout**. Modify copy/calculator to compare Premium vs VIP (and Basic vs VIP for the rare direct skip-tier). Same structure.

> Nutrition consult and 4-Week Plan don't need a dedicated funnel — they book through the existing calendar/checkout flow, with the upsell email/SMS providing the booking link directly.

---

## Step 2 — Build the Behavior-Triggered Upsell Workflow (90 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `06 — Behavior-Triggered Upsell`
- **Folder:** Create folder `06 - Upsell` and put it there
- **Re-entry:** **Enabled** — runs weekly, may re-evaluate same contact

Full action-by-action spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 2.1 Trigger

Click **+ Add New Workflow Trigger**.

- **Trigger:** Schedule (Time-Based)
- **Schedule:** Weekly, Friday at 6:00 AM `{{custom_values.business.timezone}}` (the weekend is the natural decision window for membership changes)
- **Filter — Contact has tag:** `member-active`
- **Filter — Contact does NOT have tag:** `member-paused`, `member-cancelled`, `do-not-market`, `risk-at-risk`, `risk-critical`, `upsell-recent`
- **Filter — Contact has tag:** `risk-healthy` OR `save-mature-30d` (only healthy or recently-saved members get upsold)

### 2.2 Action — Offer Eligibility Branch

This is the central decision point. The workflow evaluates each offer in priority order — first match wins per cycle.

Use a master If/Else chain:

| Order | Offer | Eligibility Conditions |
|---|---|---|
| 1 | **Premium → VIP** (highest revenue lift, evaluate first) | Has tag `tier-premium` AND `total_pt_sessions` last 30d ≥ 4 (computed in 2.3) AND NOT tag `upsell-declined-premium-vip-30d` |
| 2 | **Basic → Premium** | Has tag `tier-basic` AND `visits_last_30_days` ≥ 12 AND NOT tag `upsell-declined-basic-premium-30d` |
| 3 | **4-Week Nutrition Plan** | Has tag `tier-premium` OR `tier-vip` AND `total_nutrition_consults_lifetime` ≥ 2 AND `nutrition_interest` IN (`Yes — High`, `Yes — Curious`) AND NOT tag `upsell-declined-nutrition-plan-30d` |
| 4 | **Nutrition Starter Consult** | `days_as_member` ≥ 21 AND `nutrition_interest` ≠ `No` AND NOT tag `upsell-declined-nutrition-starter-30d` |
| 5 | None of the above | Exit workflow (no offer this cycle) |

### 2.3 Helper Action — Compute "Total PT Sessions Last 30 Days"

GHL doesn't have a native "PT sessions in last 30 days" field. The workflow either:

- (Option A — preferred) reads `total_pt_sessions` and stores a snapshot, then on next run computes the delta. Requires a custom field `pt_sessions_snapshot_30d_ago` and a helper workflow that updates it nightly.
- (Option B — simpler) uses a proxy: `last_pt_session_date` within last 7 days AND `total_pt_sessions` ≥ 8 — implies someone using PT heavily.
- (Option C — most accurate) uses GHL's Appointments module: count appointments with calendar = "PT" in last 30 days. If your GHL version exposes this via workflow conditions, use it.

The build defaults to Option C, falls back to Option B if not supported.

### 2.4 Branch A — Basic → Premium

Steps for matched contact:

1. **Add tag:** `campaign-upsell-basic-premium` and `upsell-recent` (the latter prevents re-evaluation for 30 days)
2. **Set custom field:** `upsell_offer_active` = `Basic to Premium`
3. **Send SMS:** Template `06 — Basic to Premium Nudge` from [assets/sms.md](assets/sms.md). Skip if `do-not-sms`.
4. **Wait:** 1 day, respecting 9 AM – 7 PM contact-local
5. **Send Email:** Template `06 — Basic to Premium Pitch` from [assets/emails.md](assets/emails.md). Skip if `do-not-email`.
6. **Wait:** 4 days
7. **If/Else:** Did contact upgrade?
   - Check via tag `tier-premium` added in last 5 days OR purchase event for SKU `MEM-PREMIUM`.
   - YES → Branch to "Conversion" path (see 2.8).
   - NO → Continue to step 8.
8. **Send SMS:** Template `06 — Basic to Premium Last Nudge` from [assets/sms.md](assets/sms.md). Skip if `do-not-sms`.
9. **Wait:** 3 days
10. **If/Else:** Did contact upgrade?
    - YES → Conversion path.
    - NO → **Add tag:** `upsell-declined-basic-premium-30d` (auto-expires in 30 days via a cleanup workflow), remove `campaign-upsell-basic-premium`, exit.

### 2.5 Branch B — Premium → VIP

Steps:

1. **Add tag:** `campaign-upsell-premium-vip` and `upsell-recent`
2. **Set:** `upsell_offer_active` = `Premium to VIP`
3. **Send SMS:** Template `06 — Premium to VIP Personal SMS` from [assets/sms.md](assets/sms.md). **From Morgan's number** for this offer (personal, high-value).
4. **Wait:** 1 day
5. **Send Email:** Template `06 — Premium to VIP Math Email` from [assets/emails.md](assets/emails.md). The email *shows the math* — "you spent $404/mo last 3 months on Premium + PT singles. VIP is $249 unlimited PT."
6. **Wait:** 5 days
7. **If/Else:** Did contact upgrade to VIP (tag `tier-vip` OR SKU `MEM-VIP` purchase)?
   - YES → Conversion path.
   - NO → Continue.
8. **Send SMS:** Template `06 — Premium to VIP Soft Follow-Up`. Optional reply path: "want to talk it through?"
9. **Wait:** 4 days
10. **If/Else:** Upgrade?
    - YES → Conversion path.
    - NO → Add `upsell-declined-premium-vip-30d`. Exit.

### 2.6 Branch C — Nutrition Starter Consult

Steps:

1. **Add tag:** `campaign-upsell-nutrition-starter` and `upsell-recent`
2. **Send Email:** Template `06 — Nutrition Starter Offer` from [assets/emails.md](assets/emails.md). Includes intro to the nutritionist (Sam Rivera) and direct calendar link.
3. **Wait:** 2 days
4. **Send SMS:** Template `06 — Nutrition Starter SMS Nudge`. Short, conversational, single calendar link.
5. **Wait:** 5 days
6. **If/Else:** Did contact book a nutrition consult (calendar event with calendar = "Nutrition Starter")?
   - YES → Conversion path. Add tag `upsell-converted-nutrition-starter`.
   - NO → Add `upsell-declined-nutrition-starter-30d`. Exit.

### 2.7 Branch D — 4-Week Nutrition Plan

Steps:

1. **Add tag:** `campaign-upsell-nutrition-plan` and `upsell-recent`
2. **Send Email:** Template `06 — 4-Week Plan Offer` from [assets/emails.md](assets/emails.md). Includes Sam's bio, plan structure, success quote.
3. **Wait:** 2 days
4. **Send SMS:** Template `06 — 4-Week Plan SMS Nudge`.
5. **Wait:** 5 days
6. **If/Else:** Purchase of SKU `NUT-PLAN-4WK`?
   - YES → Conversion path.
   - NO → Add `upsell-declined-nutrition-plan-30d`. Exit.

### 2.8 Conversion Path (shared across all 4 branches)

When any branch detects a conversion:

1. **Add tag:** `upsell-converted-{{offer_type}}` (e.g., `upsell-converted-basic-premium`)
2. **Update field:** `last_upsell_conversion_date` = today
3. **Update field:** `total_upsell_conversions` = `total_upsell_conversions + 1`
4. **Remove tag:** `campaign-upsell-*` for this offer
5. **Notify owner:** Internal notification — "Win! {{contact.first_name}} just converted on {{upsell_offer_active}}. New MRR: ${{contact.monthly_rate}}."
6. **Send celebration SMS** (member-facing, 1 hour after purchase): Template `06 — Upgrade Celebration` from [assets/sms.md](assets/sms.md). Owner-warm tone, sets up next steps.
7. **Add to Workflow:** Reroute to relevant follow-up — for membership tier upgrades, enter "Premium Member Onboarding" mini-flow (a 7-day "now make the most of Premium" sequence — out of scope for this file but referenced). For nutrition products, route to "Nutrition Customer Onboarding."
8. **Wait 30 days, then:** Add tag `referral-prompt-ready` — surfaces this contact to [#08 Referral Engine](../08-referral-engine/) as a high-promoter (recently happy + recently upgraded = perfect referrer).

### 2.9 Publish

Save and Publish. **Toggle ON** after running the test plan below.

---

## Step 3 — Build the Decline-Cooldown Cleanup Workflow (15 min)

Tags like `upsell-declined-basic-premium-30d` should expire after 30 days so the offer can be retried.

Navigate to **Automation > Workflows > + Create Workflow**.

- **Workflow Name:** `06 — Decline Tag Cleanup`
- **Folder:** `06 - Upsell`

### 3.1 Trigger

- **Trigger:** Tag Added → any tag matching pattern `upsell-declined-*-30d`

### 3.2 Actions

1. **Wait:** 30 days
2. **Remove tag:** the specific `upsell-declined-*-30d` tag (use a workflow variable to pass the exact tag name forward)
3. **Remove tag:** `upsell-recent` (only if no other decline tag is active)
4. Exit.

If GHL doesn't support dynamic tag removal, build 4 separate sub-workflows (one per offer type). Tedious but functional.

---

## Step 4 — Wire the Funnel to the Workflow (10 min)

The Premium upgrade checkout funnel needs to communicate conversion back to the workflow.

In **Sites > Funnels > Sunrise — Premium Upgrade Checkout > Settings**:

- **On successful purchase of MEM-PREMIUM:** Add tag `tier-premium` to contact, remove tag `tier-basic`. (GHL's Payments > Products > Automations settings handle this.)

In the **MEM-PREMIUM product settings** (Payments > Products):

- **On purchase trigger:** Update `membership_tier` field to `Premium`, update `monthly_rate` to `149`. Trigger workflow `Premium Member Onboarding` (out of scope here).

Verify by purchasing the product with a Stripe test card — confirm tags update and the upsell workflow's "did they upgrade?" check fires correctly.

Repeat for **MEM-VIP** product → `tier-vip` tag, `monthly_rate` 249.

For **NUT-STARTER** and **NUT-PLAN-4WK** — on purchase, add tag `nutrition-customer-active` and trigger "Nutrition Customer Onboarding" workflow (out of scope).

---

## Step 5 — Backfill `interest-*` Tags for Existing Members (15 min)

The Nutrition Starter offer relies on `interest-nutrition` not being blocked. For new members coming through onboarding, this gets set during the day-7 check-in. For *existing* members, you need to seed reasonable defaults.

Run a bulk update:

1. **Smart list:** All `member-active`, NOT `interest-nutrition`, joined > 90 days ago.
2. **Bulk action:** Set `nutrition_interest` = `Yes — Curious` (the soft default — allows offer through gate without overpromising interest).

Members who actively reply "not interested" to the first nutrition email will get `nutrition_interest` = `No` set on their record by an inbound-SMS-handler workflow.

---

## Step 6 — Owner Smart Lists (10 min)

Navigate to **Contacts > Smart Lists > + Create**.

### List 1: Pending Upsell Sequences

- Name: `Upsell — In Sequence This Week`
- Filters: Has tag matching `campaign-upsell-*`

### List 2: Recent Conversions

- Name: `Upsell — Wins Last 30 Days`
- Filters: Has tag matching `upsell-converted-*`. Conversion date within last 30 days.

### List 3: Eligible But Not Yet Offered

- Name: `Upsell — Premium-Ready Basics`
- Filters: Tag `tier-basic`. `visits_last_30_days` ≥ 12. NOT tag `upsell-declined-basic-premium-30d`. NOT tag `upsell-recent`.

### List 4: Eligible VIP Candidates

- Name: `Upsell — VIP-Ready Premiums`
- Filters: Tag `tier-premium`. PT sessions in last 30d ≥ 4 (proxy: `last_pt_session_date` < 7 days ago AND `total_pt_sessions` ≥ 8).

These four lists feed the [#10 Owner Reporting](../10-owner-reporting-and-visibility/) Upsell widget.

---

## Test Plan

Run this test sequence. **Do not declare done until all pass.**

### Test 1 — Basic → Premium offer triggers

1. Create test contact with: `tier-basic` tag, `member-active` tag, `risk-healthy` tag, `visits_last_30_days` = 14.
2. Manually trigger workflow `06 — Behavior-Triggered Upsell` on contact.
3. **Expected within 1 minute:** SMS arrives. Tags applied: `campaign-upsell-basic-premium`, `upsell-recent`.
4. **Expected after 1 day wait:** Email lands.

### Test 2 — Conversion path fires

1. After Test 1, manually add tag `tier-premium` to contact (simulating purchase).
2. **Expected:** Within the next workflow execution cycle, conversion path fires. Tag `upsell-converted-basic-premium` applied. Owner notification sent. Celebration SMS arrives 1 hour later.

### Test 3 — Decline cooldown applies

1. Create another test contact (same setup as Test 1).
2. Let workflow run to end (no conversion).
3. **Expected:** Tag `upsell-declined-basic-premium-30d` applied. Tag `upsell-recent` retained.
4. Try to re-trigger workflow.
5. **Expected:** Trigger filter blocks (because `upsell-recent`). No new SMS.
6. Wait 30 days (or manually remove `upsell-declined-basic-premium-30d` for fast testing).
7. **Expected:** Contact becomes eligible again.

### Test 4 — At-Risk member excluded

1. Create test contact with: `tier-basic`, `member-active`, `risk-at-risk`, `visits_last_30_days` = 14.
2. Trigger workflow.
3. **Expected:** Trigger filter blocks. No SMS or email.

### Test 5 — Premium → VIP fires from Morgan's number

1. Create test contact: `tier-premium`, `member-active`, `risk-healthy`, simulate 4+ PT in 30d.
2. Trigger workflow.
3. **Expected:** SMS arrives **from Morgan's personal number** (not the general SMS number). Confirm sender.

### Test 6 — Nutrition starter at day 21

1. Create test contact: `tier-basic`, `member-active`, `risk-healthy`, `days_as_member` = 21, `nutrition_interest` = `Yes — Curious`.
2. Trigger workflow.
3. **Expected:** Branch C fires. Email with Sam intro lands.

### Test 7 — Nutrition starter blocked by "No" interest

1. Same as Test 6 but `nutrition_interest` = `No`.
2. **Expected:** Workflow exits — no offer. (Member fell through all branches.)

### Test 8 — Premium funnel checkout

1. Open Premium Upgrade Checkout funnel URL with `?contact_id={{test_contact_id}}` param.
2. **Expected:** Page renders with personalized name and attendance stat.
3. Click through Savings Calculator — confirm math is correct.
4. Complete checkout with Stripe test card.
5. **Expected:** Tag `tier-premium` applied. `tier-basic` removed. `membership_tier` field = Premium. `monthly_rate` = 149.

### Test 9 — Owner notification

1. After Test 8, check owner inbox.
2. **Expected:** "Win!" notification with member name and new MRR.

### Test 10 — Referral prompt 30 days later

1. After conversion, wait 30 days (or fast-forward).
2. **Expected:** Tag `referral-prompt-ready` applied. (This is consumed by [#08](../08-referral-engine/).)

---

## Common Build Mistakes (avoid these)

1. **Offering the wrong tier.** A VIP member with high PT usage shouldn't get the Premium → VIP offer — they're already there. The tier filter (`tier-premium`) on Branch B is critical. Test with a VIP test contact.
2. **Re-offering immediately after decline.** The `upsell-recent` tag is the safety net. If it's not getting applied, the contact will re-enter the workflow next Friday and get the same SMS again, fast path to unsubscribe.
3. **Counting visits wrong.** `visits_last_30_days` is a *rolling* count. It must be updated nightly by the attendance pipeline. If it's stale, you'll under-offer (members who attended yesterday won't be counted until tomorrow's update).
4. **Funnel checkout doesn't update tags.** Without the product-purchase automation in Step 4, the workflow never sees the conversion, never fires the celebration SMS, never notifies the owner.
5. **At-risk members getting upsold.** The trigger filter exclusion list is critical. A member who's at-risk should be left alone — pushing an upsell makes them cancel faster.
6. **Morgan's number not provisioned.** Branch B's SMS sends from a different number than the general sender. Confirm Morgan's number is set up as a sending identity in GHL. If not, fall back to the general number but adjust the SMS copy to say "Hey it's Morgan" explicitly (since the number won't tell the story).
7. **Savings calculator returns wrong math.** The calculator on the Premium funnel must use accurate Basic + add-on cost vs Premium price. Test with edge cases — what if the member says "0 PT, 0 nutrition"? (Show: "You wouldn't save money on Premium yet — but here's what changes when you start using it.") Don't claim savings when there aren't any.

---

## What's Next

Once this is live and producing wins:

- Members tagged `upsell-converted-*` are surfaced to **[#08 Referral Engine](../08-referral-engine/build.md)** as high-promoter candidates after 30 days.
- Upgrade events flow into **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)** as MRR-lift line items.
- Failed-to-convert offers feed back into the system as cohort data — over time, the gating logic can be refined (e.g., maybe 12 classes/mo is too aggressive a Basic→Premium gate; lower to 10 if conversion rate is high).
- Saved members from **[#05 Retention](../05-retention-and-churn-prevention/build.md)** with `save-mature-30d` tag are explicitly *included* in the upsell pool — a successful save followed by an upsell offer 30 days later has the highest conversion rate of any upsell cohort.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
