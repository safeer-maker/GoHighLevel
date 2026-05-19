# #08 — Build Playbook: Referral Engine

> Step-by-step GHL build. Estimated time: **150 minutes** for a competent operator. Two workflows, one funnel, one form, one new custom field. Prerequisites listed first.

---

## Prerequisites (from shared-foundation/)

Confirm these exist before starting. If anything is missing, build it first.

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Engagement fields: `referral_code`, `referrals_made_count`, `referrals_converted_count` | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Referrer-side tracking |
| Lead Info fields: `referred_by_contact_id`, `referral_code_used`, `lead_source`, `lead_source_detail` | Same | Referee-side attribution |
| Tags: `member-active`, `trial-converted`, `source-referral`, `campaign-referral-promoter` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Trigger filters and segmentation |
| Custom values: `business.short_name`, `business.booking_url`, `team.owner_first`, `offer.referral_reward_referrer`, `offer.referral_reward_referee` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message copy |
| Coupon: `REF20` ($20 off first month) | [../../shared-foundation/products-and-pricing.md](../../shared-foundation/products-and-pricing.md) | Applied automatically at referee checkout |
| Product: **Personal Training — Single Session** ($85, SKU `PT-SINGLE`) | Same | The redemption target for referrer credits |
| Workflow: `01 — Instant Response — Lead Capture` | [../01-lead-capture-and-instant-response/build.md](../01-lead-capture-and-instant-response/build.md) | Receives the new referral lead |

---

## Step 0 — Add the `pt_credit_balance` Custom Field (#08-specific extension)

This field is introduced by #08 and is not in the original 48-field shared foundation. Add it before building anything else.

Navigate to **Settings > Custom Fields > Contact > Engagement & Activity** folder.

Click **+ Add Field**.

| Setting | Value |
|---|---|
| **Field Name** | PT Credit Balance |
| **Field Key** | `pt_credit_balance` |
| **Type** | Number |
| **Default Value** | `0` |
| **Description** | Number of free PT sessions the member has banked. Earned via referrals (+1 per converted referral). Decremented manually by front desk on redemption. |

**Note:** Update [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) to add this field to the Engagement & Activity folder so future problems can reference it. Total field count becomes 49.

---

## Step 1 — Build the Referral Landing Funnel (45 min)

### 1.1 Create the funnel

Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Referral Landing`
- **Type:** Lead Generation
- **Template:** Start blank

### 1.2 Build Page 1 — Personalized Hero

Click **+ Add Step > Landing Page**. Name it `01 — Hero (Personalized)`.

Build in the page editor following the page-by-page copy in **[assets/funnel.md](assets/funnel.md)**.

The critical bit: **the H1 reads the URL parameter `?ref_name=` and renders the referrer's first name**. In the GHL page builder, drag a Text element and use the merge field syntax:

```
{{request.params.ref_name}} sent you $20 off your first month at {{custom_values.business.short_name}}
```

If `ref_name` is not present in the URL, fall back to a generic headline ("Your friend sent you $20 off your first month at Sunrise"). In the funnel builder, this is done by setting a default value for the URL parameter merge field, or by using two text elements (one conditional on the param being present, one on it being absent).

### 1.3 Build Page 2 — Claim Form Page

Click **+ Add Step > Form Page**. Name it `02 — Claim`.

Embed the form `Referral Capture` (built in Step 2 below). The form has hidden fields that read from URL parameters:

- `ref_name` → `lead_source_detail` (so the owner sees "Sarah" in lead source detail on the new contact)
- `ref_id` → `referred_by_contact_id` (Sarah's GHL contact ID)
- `ref_code` → `referral_code_used` (Sarah's code, e.g., `SARAH-42`)
- `lead_source` → defaults to `Referral`

Full layout in [assets/funnel.md](assets/funnel.md).

### 1.4 Build Page 3 — Thank-You Page

Click **+ Add Step > Thank-You Page**. Name it `03 — Welcome`.

Mostly the same as #01's thank-you page, but with one personalization line at the top:

> "Tell Sarah thanks — she just earned a free PT session because of you ☀️"

(Replace "Sarah" with `{{request.params.ref_name}}` merge.)

### 1.5 Publish & note the URL

Click **Publish**. The base URL becomes the link template:

```
https://book.sunrisewellness.com/refer/?ref_name=SARAH&ref_id=abc123xyz&ref_code=SARAH-42&lead_source=Referral
```

---

## Step 2 — Build the Referral Capture Form (15 min)

Navigate to **Sites > Forms > + Build Form**.

- **Form Name:** `Referral Capture`

This is a clone of `Lead Capture — Free 7-Day Pass` (from [#01](../01-lead-capture-and-instant-response/assets/forms.md)) with three extra hidden fields. Full spec in **[assets/forms.md](assets/forms.md)**.

| Order | Field | Type | Required | Maps to | Notes |
|---|---|---|---|---|---|
| 1 | First Name | Text | Yes | `contact.first_name` | |
| 2 | Last Name | Text | Yes | `contact.last_name` | |
| 3 | Phone | Phone | Yes | `contact.phone` | |
| 4 | Email | Email | Yes | `contact.email` | |
| 5 | Primary goal | Dropdown | Yes | `fitness_goal_primary` | Same options as #01 |
| 6 | Consent checkbox | Checkbox | Yes | `sms_opt_in` + `email_opt_in` | |
| 7 | (hidden) lead_source | Hidden | — | `lead_source` | Default value: `Referral` |
| 8 | (hidden) referred_by_contact_id | Hidden | — | `referred_by_contact_id` | Reads URL param `ref_id` |
| 9 | (hidden) referral_code_used | Hidden | — | `referral_code_used` | Reads URL param `ref_code` |
| 10 | (hidden) lead_source_detail | Hidden | — | `lead_source_detail` | Reads URL param `ref_name` |

**Form settings:**

- **On Submit:** Redirect to `03 — Welcome` page.
- **Send notification email:** No (the #01 Instant Response Workflow handles all notifications).
- **Add to workflow:** Leave blank.

**Important:** Confirm the existing `01 — Instant Response — Lead Capture` workflow includes the new `Referral Capture` form in its trigger filter. Navigate to that workflow, edit the trigger, and add `Referral Capture` to the form OR list.

---

## Step 3 — Build Workflow 1: Referral Code Generation (30 min)

This workflow runs once per active member, the moment they become active. It generates and stores their unique referral code.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `08a — Referral Code Generation`
- **Folder:** Create folder `08 - Referral Engine` and put it there

Full spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 3.1 Trigger

- **Trigger:** Contact Tag Added
- **Tag:** `member-active`
- **Filter:** Custom field `referral_code` is empty (so re-trigger on reactivated members doesn't overwrite a working code)

### 3.2 Action: Generate Code

GHL doesn't have a native "generate unique string" action. Use one of these approaches:

**Approach A — Custom JS via Webhook (recommended):**

- **Action:** Webhook
- **Method:** POST
- **URL:** A small Make.com / Zapier / custom endpoint that takes `{first_name, contact_id}` and returns `FIRSTNAME-XX` where `XX` is the last 2 chars of the contact ID (alphanumeric uppercase).
- **Body:** `{"first_name": "{{contact.first_name}}", "contact_id": "{{contact.id}}"}`
- **Response handling:** Capture the returned `referral_code` value.

**Approach B — Math in GHL (simpler, less unique):**

- **Action:** Update Contact Field
- **Field:** `referral_code`
- **Value:** `{{contact.first_name | upper}}-{{contact.id | last_2}}`

GHL's templating supports basic string functions in many accounts. If `| upper` and `| last_2` aren't supported, use Approach A.

### 3.3 Action: Build Share URL

- **Action:** Update Contact Field
- **Field:** Create a new field for this: `referral_share_url` (Single Line, in Engagement folder) — add it now if not yet present.
- **Value:**
```
{{custom_values.business.website}}/refer/?ref_name={{contact.first_name | upper}}&ref_id={{contact.id}}&ref_code={{contact.referral_code}}&lead_source=Referral
```

### 3.4 Action: Send Referral-Invite SMS to Member

After a 24-hour wait (let them settle in as a member first), send the "here's your link" SMS.

- **Action:** Wait — 24 hours
- **Action:** Send SMS
- **Template:** SMS A from [assets/sms.md](assets/sms.md) — "Member Referral Invite"

### 3.5 Action: Send Referral-Invite Email to Member

Sent the same day as the SMS, ~30 min after.

- **Action:** Wait — 30 minutes
- **Action:** Send Email
- **Template:** Email "Your Sunrise Referral Link" from [assets/emails.md](assets/emails.md)

### 3.6 Publish

Click **Save** then **Publish**. Toggle the workflow ON.

---

## Step 4 — Build Workflow 2: Referral Conversion Credit (45 min)

This is the workflow that closes the loop — when a referred trial converts, the referrer gets credit.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `08b — Referral Conversion Credit`
- **Folder:** `08 - Referral Engine`

### 4.1 Trigger

- **Trigger:** Contact Tag Added
- **Tag:** `trial-converted`
- **Filter:** Custom field `referred_by_contact_id` is NOT empty

### 4.2 Action: Lookup the Referrer Contact

- **Action:** Find Contact by ID
- **Lookup value:** `{{contact.referred_by_contact_id}}`
- **Store as:** `referrer` (referenced as `{{referrer.first_name}}`, `{{referrer.email}}`, etc. for the rest of the workflow)

### 4.3 Action: Increment Referrer's `referrals_made_count`

- **Action:** Update Contact Field — *on referrer*
- **Field:** `referrals_made_count`
- **Value:** `{{referrer.referrals_made_count + 1}}`

(If GHL's template engine doesn't support arithmetic, use a Webhook to increment via the API — same pattern as Step 3.2.)

### 4.4 Action: Increment Referrer's `referrals_converted_count`

- **Action:** Update Contact Field — *on referrer*
- **Field:** `referrals_converted_count`
- **Value:** `{{referrer.referrals_converted_count + 1}}`

### 4.5 Action: Increment Referrer's `pt_credit_balance` (the reward)

- **Action:** Update Contact Field — *on referrer*
- **Field:** `pt_credit_balance`
- **Value:** `{{referrer.pt_credit_balance + 1}}`

### 4.6 Action: Send Referrer Notification SMS

- **Action:** Send SMS — *to referrer*
- **Template:** SMS B from [assets/sms.md](assets/sms.md) — "Referrer Got A Conversion"
- **Skip if:** Referrer has tag `do-not-sms`

### 4.7 Action: Send Referrer Notification Email

- **Action:** Wait — 5 minutes (give the SMS a head start)
- **Action:** Send Email — *to referrer*
- **Template:** Email "Your friend just signed up!" from [assets/emails.md](assets/emails.md)
- **Skip if:** Referrer has tag `do-not-email`

### 4.8 Action: Send Referee Welcome SMS (to the new member)

- **Action:** Send SMS — *to triggering contact (the new member)*
- **Template:** SMS C from [assets/sms.md](assets/sms.md) — "Referee Welcome"

### 4.9 Action: Send Referee Welcome Email

- **Action:** Wait — 10 minutes
- **Action:** Send Email — *to triggering contact*
- **Template:** Email "Welcome — and thanks for trusting Sarah's recommendation" from [assets/emails.md](assets/emails.md)

### 4.10 Action: Owner Internal Notification

- **Action:** Send Internal Notification
- **To:** `{{custom_values.business.owner_email}}`
- **Subject:** `Referral converted: {{referrer.first_name}} → {{contact.first_name}}`
- **Body:** Quick celebration note with both names + referrer's running total.

### 4.11 Publish

Click **Save** then **Publish**. Toggle the workflow ON.

---

## Step 5 — Build Workflow 3: Quarterly Top-Referrer Recognition (15 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `08c — Quarterly Top Referrer Recognition`
- **Folder:** `08 - Referral Engine`

### 5.1 Trigger

- **Trigger:** Scheduled — recurring
- **Schedule:** Quarterly — first day of each calendar quarter (Jan 1, Apr 1, Jul 1, Oct 1) at 9 AM owner-local time.

### 5.2 Action: Find Top 3 Referrers

GHL's native scheduled workflows can't easily "find top N" — use a Smart List + Webhook approach:

- **Action:** Webhook
- **URL:** Custom endpoint that queries the GHL Contacts API for contacts with `referrals_converted_count > 0` updated in the last 90 days, sorted descending, top 3.
- **Response:** Array of 3 contact IDs.

Alternative if Webhook isn't viable: a manually-curated smart list "Top Referrers — This Quarter" that the owner reviews on Day 1 and bulk-enrolls into a one-off workflow.

### 5.3 Action: For Each Top Referrer

For each of the 3:

- **Action:** Add Tag → `campaign-referral-promoter`
- **Action:** Increment `pt_credit_balance` by 2 (bonus)
- **Action:** Send Email → "Quarterly Top Referrer Recognition" from [assets/emails.md](assets/emails.md)
- **Action:** Send Internal Notification to owner: "Hand-deliver a Sunrise sweatshirt + handwritten card to {{contact.first_name}} {{contact.last_name}} — this quarter's top referrer."

### 5.4 Publish

Save and publish. Toggle ON.

---

## Step 6 — Verify URL Parameter Wiring (10 min)

The single biggest failure mode for this system is URL params not flowing into form hidden fields. Test:

### 6.1 Test URL

Build a test URL:

```
https://book.sunrisewellness.com/refer/?ref_name=TESTUSER&ref_id=test-contact-001&ref_code=TESTUSER-99&lead_source=Referral
```

Open in incognito.

### 6.2 Verify Page 1

The H1 should read: "TESTUSER sent you $20 off your first month at Sunrise"

If it shows the fallback ("Your friend sent you…"), the `request.params.ref_name` merge isn't reading. Fix the funnel-page text element.

### 6.3 Verify Form Submission

Submit the form with test data. Open the resulting contact in GHL.

**Expected:**
- `lead_source` = `Referral`
- `lead_source_detail` = `TESTUSER`
- `referred_by_contact_id` = `test-contact-001`
- `referral_code_used` = `TESTUSER-99`
- Tag `source-referral` applied (by #01 workflow)

---

## Test Plan

Run this complete test sequence after publishing. **Do not declare done until all six pass.**

### Test 1 — Code generation fires on first member-active

1. Create a test contact `Test Referrer One`, email + phone yours.
2. Apply tag `member-active` manually.
3. **Expected within 30 seconds:**
   - `referral_code` populated (e.g., `TEST-XX`)
   - `referral_share_url` populated with the full URL
4. **Expected after 24 hours:**
   - SMS arrives with the share link.
   - Email arrives ~30 min after SMS.

(For testing speed: temporarily set the Wait to 1 min instead of 24 hours; reset to 24 hours after test.)

### Test 2 — Code does NOT re-generate on reactivation

1. On the same test contact, remove `member-active`, then re-add it.
2. **Expected:** Workflow filter blocks re-entry (referral_code is no longer empty). Original code stays intact.

### Test 3 — Referral landing page personalizes

1. Open `https://book.sunrisewellness.com/refer/?ref_name=TESTREF&ref_id=xyz&ref_code=TESTREF-99` in incognito.
2. **Expected:** Hero reads "TESTREF sent you $20 off…"
3. Open the URL WITHOUT `?ref_name=…`.
4. **Expected:** Fallback hero reads "Your friend sent you $20 off…"

### Test 4 — End-to-end referral flow

1. Open the referral URL from Test 3 (with full params).
2. Fill the form with a NEW test contact (`Test Referee One`, different email/phone).
3. Submit.
4. **Expected in GHL on Test Referee One:**
   - All four hidden fields populated correctly.
   - Tag `source-referral` applied by the #01 Instant Response workflow.
   - Welcome SMS + email from the #01 workflow arrives (not yet a referral-conversion notification — that fires only on trial conversion).

### Test 5 — Referral conversion credit fires

1. On `Test Referee One`, manually apply tag `trial-converted`.
2. **Expected within 60 seconds:**
   - On `Test Referrer One`: `referrals_made_count` and `referrals_converted_count` both increment by 1; `pt_credit_balance` increments by 1.
   - Referrer receives the "your friend joined!" SMS, then email.
   - Referee receives the "welcome from Sarah's referral" SMS, then email.
   - Owner receives internal notification email.

### Test 6 — Code uniqueness

1. Create two contacts with the same first name (e.g., two test contacts both named `Morgan`).
2. Apply `member-active` to both.
3. **Expected:** Each gets a *different* code (`MORGAN-XX` vs `MORGAN-YY`, where XX/YY are different contact ID fragments).

---

## Common Build Mistakes

1. **URL params not reaching form hidden fields.** Hidden form field "default value" must be configured as **"Read from URL parameter"** with the parameter name matching exactly (`ref_id`, `ref_code`, `ref_name`). If GHL's form builder doesn't expose this option, use a hidden text field with the default value set via JS snippet on the form-page load.
2. **Referrer field `referred_by_contact_id` empty.** Most common cause: members are sharing the raw landing URL without the query params (they typed it into the browser, or stripped the params when copying). Solution: always have members share via the **Send My Link** SMS — the link in that SMS is pre-built with their params.
3. **PT credit balance not incrementing.** If `pt_credit_balance` shows 0 after a conversion, the arithmetic merge `{{referrer.pt_credit_balance + 1}}` isn't being evaluated by GHL. Switch Step 4.5 to a Webhook that calls the GHL API to add 1 to the field.
4. **Referrer notification fires for the referrer themself.** Bug: the workflow updates the *triggering* contact's fields instead of the *referrer's*. Fix: every action in Workflow 2 that targets the referrer must explicitly use the `referrer` lookup variable, not implicit "contact."
5. **Code collisions on same-first-name members.** If you used the simpler Approach B in Step 3.2 and two contacts have contact IDs ending in the same 2 chars, you get duplicate codes. Approach A (webhook with rejection-on-collision logic) is more robust at scale. Acceptable for studios under 500 members; rebuild as Approach A above that.
6. **Quarterly recognition fires on members who got their first referral 89 days ago.** Make sure the smart list filter is `referrals_converted_count > 0 in trailing 90d` — not lifetime. Otherwise the same 3 power-referrers win every quarter forever and newer rising stars don't get recognized.

---

## What's Next

Once this is live and verified:

- New referred leads flow through **[#02 Trial-to-Paid Conversion](../02-trial-to-paid-conversion/build.md)** like any other trial (no special referral treatment in the trial flow itself — the magic happens at the bookends).
- Top referrers also surface in **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)** under the "Top Referrers (Quarterly)" smart list.
- The `pt_credit_balance` field is consumed by the front-desk POS flow — when a member books a PT session, the system checks the balance first and prompts "Use 1 of N free credits?" before charging.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
