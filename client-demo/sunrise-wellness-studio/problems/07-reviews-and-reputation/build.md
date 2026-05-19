# #07 — Build Playbook: Reviews & Reputation

> Step-by-step GHL build. Estimated time: **2 hours** for a competent operator. The smart review router funnel is the heart of the build — get the branching logic right first, then wire the trigger workflow.

---

## Prerequisites (from shared-foundation/)

| Foundation Asset | Where Defined | Used For |
|---|---|---|
| Engagement & Activity fields (`review_submitted_date`, `review_star_rating`) | [../../shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md) | Stamping review history |
| Tags: `member-active`, `campaign-review-ask`, `review-submitted-google`, `feedback-received-private`, `do-not-ask-reviews`, `risk-*`, `do-not-sms`, `do-not-email` | [../../shared-foundation/tags.md](../../shared-foundation/tags.md) | Eligibility + state |
| Custom values: `business.google_review_url`, `business.short_name`, `team.owner_first`, `business.sms_number`, `voice.signature_owner` | [../../shared-foundation/custom-values.md](../../shared-foundation/custom-values.md) | Message and funnel copy |
| Output of [#03 Appointment No-Show Recovery](../03-appointment-no-show-recovery/) — appointment status changes accurately set "Showed" | [#03](../03-appointment-no-show-recovery/) | Trigger source |
| Output of [#05 Retention](../05-retention-and-churn-prevention/) — `risk-*` tags populated nightly | [#05](../05-retention-and-churn-prevention/) | Eligibility gate |

Also required: **the studio's actual Google Business Profile URL for direct review submission**. Get it from Google My Business → Get more reviews → copy the short URL. Looks like `https://g.page/r/SunriseWellnessStudio/review`. Confirm it's set in `custom_values.business.google_review_url`.

---

## Step 1 — Build the Smart Review Router Funnel (45 min)

This is the central mechanic. Navigate to **Sites > Funnels > + New Funnel**.

- **Funnel Name:** `Sunrise — Smart Review Router`
- **Type:** Lead Generation (we're capturing a form response, even though we route differently after)
- **Template:** Start blank
- **Domain:** book.sunrisewellness.com/review (or sub-path)

Full copy in **[assets/funnel.md](assets/funnel.md)**.

### 1.1 Build Page 1 — The Rating Selector

Click **+ Add Step > Landing Page**. Name `01 — How Was It`.

**Layout:**

- Brand header band (sunrise gradient strip at top)
- Hero section, centered, vertically generous spacing:
  - Logo (small, top)
  - H1: "How was your session, {{contact.first_name}}?"
  - Subhead: "30 seconds — tap how it felt."

- **The 5-button row** (this is the critical element):
  - 5 large, equally-sized circular emoji buttons in a horizontal row (stacks on mobile if needed but should fit horizontally even on phones — keep them at ~60px each)
  - Button 1: 😡 (1 star) — value `1`
  - Button 2: 😕 (2 stars) — value `2`
  - Button 3: 😐 (3 stars) — value `3`
  - Button 4: 😊 (4 stars) — value `4`
  - Button 5: 😍 (5 stars) — value `5`

- Below buttons: small text "Each button takes you to a different page based on how it went."

- Footer: minimal — small "Powered by Sunrise" link to home.

### 1.2 Configure the routing logic

Each button must:

1. Set the `review_star_rating` custom field on the contact to the corresponding value (1–5).
2. Set `review_submitted_date` to today.
3. Redirect to the correct next page based on score.

**How to implement in GHL:**

GHL funnel buttons can either link to a URL OR trigger an action. For this build, use **5 separate buttons, each linked to a different URL with the rating as a query parameter**:

| Emoji | Linked URL |
|---|---|
| 😡 | `/review/feedback?rating=1&contact_id={{contact.id}}` |
| 😕 | `/review/feedback?rating=2&contact_id={{contact.id}}` |
| 😐 | `/review/feedback?rating=3&contact_id={{contact.id}}` |
| 😊 | `/review/thanks?rating=4&contact_id={{contact.id}}` |
| 😍 | `/review/thanks?rating=5&contact_id={{contact.id}}` |

The `/review/feedback` path goes to **Page 3 (private feedback)**.
The `/review/thanks` path goes to **Page 2 (Google redirect)**.

When the target page loads, it:
1. Reads `rating` and `contact_id` from URL params.
2. Updates the contact's `review_star_rating` and `review_submitted_date` fields (via a small inline workflow trigger — see Step 4).
3. Renders the appropriate next-page content.

### 1.3 Build Page 2 — High-Score Thanks + Google Redirect

Click **+ Add Step > Landing Page**. Name `02 — Thanks Google`.

**Layout:**

- H1: "{{contact.first_name}}, that's amazing — thank you ☀️"
- Subhead: "Would you mind sharing it on Google? Takes 30 seconds and helps a ton."
- Large CTA button: **Leave a Google Review →** linking to `{{custom_values.business.google_review_url}}`
- Below button: "We'll redirect you automatically in 5 seconds…"
- **JavaScript auto-redirect** after 5 seconds to the Google review URL (in case the member doesn't tap the button)

**Auto-redirect snippet (embed in page footer):**

```html
<script>
  setTimeout(function(){
    window.location.href = "{{custom_values.business.google_review_url}}";
  }, 5000);
</script>
```

The 5-second delay gives the member time to read the thanks, plus a chance to opt out (by closing the tab) if they'd rather not. Don't make it instant — feels coercive.

### 1.4 Build Page 3 — Private Feedback Form

Click **+ Add Step > Form Page**. Name `03 — Private Feedback`.

**Layout:**

- H1: "Oof — sorry, {{contact.first_name}}. What happened?"
- Subhead: "Tell us so we can make it right. This goes straight to Morgan — never anywhere public."
- Embedded form (built in Step 2 below)
- Submit button label: "Send to Morgan"
- Below: "We'll get back to you within 24 hours, often faster."

**Form fields:** spec in [assets/forms.md](assets/forms.md). High-level: a single "What could we have done better?" multi-line field + optional "I'd be willing to chat by phone" checkbox + optional contact-preference radio.

### 1.5 Publish

Click **Publish**. Note the URLs.

---

## Step 2 — Build the Private Feedback Form (10 min)

Navigate to **Sites > Forms > + Build Form**.

- **Form Name:** `Review — Private Feedback (Low Score)`

Fields per **[assets/forms.md](assets/forms.md)**. Quick overview:

| # | Field | Type | Required | Maps to |
|---|---|---|---|---|
| 1 | What could we have done better? | Multi-line text | ✅ | `private_feedback_text` (new field — add to Lead Info folder) |
| 2 | Is there anything specific we should fix today? | Multi-line text | ❌ | `private_feedback_urgent` (new field) |
| 3 | Would you be open to a quick phone call from Morgan? | Checkbox | ❌ | (sets tag `feedback-phone-ok`) |
| 4 | Best way to reach you | Radio (Email / Text / Phone) | ❌ | (sets `preferred_channel` field) |
| 5 | (hidden) Star rating | Hidden number | — | `review_star_rating` (populated from URL param via JS) |
| 6 | (hidden) Contact ID | Hidden text | — | (matches contact to record) |

**Submit behavior:** Redirect to a simple thank-you page: "Got it. Morgan will be in touch within 24 hours. We mean it."

**Form settings:**

- **On submit, send internal notification to:** `{{custom_values.business.owner_email}}` with subject `URGENT: Low review score from {{contact.first_name}} {{contact.last_name}}` and full body of the feedback. Priority: HIGH.
- **On submit, trigger workflow:** the "Low Score Handler" workflow (Step 4 below).

---

## Step 3 — Add Custom Fields If Missing (5 min)

Check **Settings > Custom Fields > Contact > Lead Info folder**:

| Field Name | Field Key | Type | Notes |
|---|---|---|---|
| Private Feedback Text | `private_feedback_text` | Multi-line | From low-score form |
| Private Feedback Urgent | `private_feedback_urgent` | Multi-line | Anything urgent to fix |
| Feedback Submitted Date | `feedback_submitted_date` | Date | When low-score form submitted |
| Feedback Phone OK | `feedback_phone_ok` | Single Option | Yes / No |

The `review_submitted_date` and `review_star_rating` fields should already exist in the Engagement & Activity folder per [shared-foundation/custom-fields.md](../../shared-foundation/custom-fields.md).

---

## Step 4 — Build the Post-Class Review Ask Workflow (40 min)

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**.

- **Workflow Name:** `07 — Post-Class Review Ask`
- **Folder:** Create folder `07 - Reviews` and put it there
- **Re-entry:** Tag-based (allow re-entry on a *new* appointment, but block within 90-day window)

Full spec in **[assets/workflow.md](assets/workflow.md)**. Build order:

### 4.1 Trigger

- **Trigger:** Appointment Status Changed
- **Filter — New Status equals:** `Showed` (or `Completed`, depending on your GHL terminology)
- **Filter — Contact has tag:** `member-active`
- **Filter — Contact does NOT have tag:** `risk-at-risk`, `risk-critical`, `do-not-ask-reviews`, `campaign-review-ask` (the last one is the 90-day cooldown)
- **Filter — Contact does NOT have any active campaign tag from #06 upsell:** prevents collision with active upsell sequence

### 4.2 Action — Check 90-Day Cooldown

- **Action:** If/Else
- **Condition:** `review_submitted_date` is null OR more than 90 days ago
- **YES:** Continue
- **NO:** Add tag `review-skipped-cooldown` (for visibility), exit

### 4.3 Action — Wait 30 Minutes (the endorphin window)

- **Action:** Wait — 30 minutes
- **Reason:** Members have post-class endorphins. Asking immediately feels transactional; waiting 30 min hits the "I feel good about that workout" window perfectly.

### 4.4 Action — Add `campaign-review-ask` Tag

- **Action:** Add Tag → `campaign-review-ask`
- **Reason:** Locks the 90-day cooldown.

### 4.5 Action — Branch by Appointment Type

The SMS copy differs slightly for class vs PT. Use If/Else on calendar name:

- **Action:** If/Else
  - Appointment calendar = "PT" → use SMS template `07 — Post-PT Review Ask`
  - Else (group class) → use SMS template `07 — Post-Class Review Ask`

### 4.6 Action — Send Review-Ask SMS

- **Action:** Send SMS
- **Template:** matched above from [assets/sms.md](assets/sms.md)
- **From:** `{{custom_values.business.sms_number}}`
- **Skip if:** `do-not-sms` OR `sms_opt_in` ≠ Yes

### 4.7 Action — Stamp the Ask Time

- **Action:** Update Contact Field → `review_ask_sent_at` = `{{now}}` (add this field if not present — Engagement & Activity folder)

### 4.8 Action — Wait 3 Days, Check for Response

- **Action:** Wait — 3 days
- **Action:** If/Else — does contact have `review-submitted-google` OR `feedback-received-private` tag?
  - YES → Exit (review completed in some form)
  - NO → Continue

### 4.9 Action — Send Follow-Up Email

- **Action:** Send Email
- **Template:** `07 — Review Follow-Up Email` from [assets/emails.md](assets/emails.md)
- **Skip if:** `do-not-email` OR `email_opt_in` ≠ Yes

### 4.10 Action — Wait 7 Days, Final Check

- **Action:** Wait — 7 days
- **Action:** If/Else — submitted in any form?
  - YES → Exit (workflow saw a successful submission)
  - NO → Add tag `review-no-response`. Schedule next eligibility for 90 days from now (i.e., the `campaign-review-ask` tag will auto-clear via a sub-workflow after 90 days).

### 4.11 Publish

Save and **Publish**. Toggle ON only after running the test plan.

---

## Step 5 — Build the Review Submission Handler Workflows (30 min)

Two small workflows: one for the high-score (Google) path, one for the low-score (private) path.

### Workflow 07b — High-Score Detection

When a member lands on Page 2 (Thanks + Google redirect), we want to:
1. Stamp their `review_star_rating` field (4 or 5).
2. Stamp `review_submitted_date`.
3. Add the `review-submitted-google` tag (note: this assumes they actually click through to Google — we can't 100% verify they leave a review there, but the tap-through is the best signal we have).
4. Notify the owner.

**Trigger:** URL Visited → `/review/thanks` (use GHL's URL trigger feature; if not available, fire from a hidden form on the page that auto-submits on load)

**Filter:** URL contains `rating=4` OR `rating=5`

**Actions:**

1. Update Field: `review_star_rating` = value from URL param
2. Update Field: `review_submitted_date` = today
3. Add Tag: `review-submitted-google`
4. Remove Tag: `campaign-review-ask` (workflow done)
5. Notify owner: "{{contact.first_name}} just tapped a {{rating}}-star review and was sent to Google!"
6. Wait 7 days
7. Add tag: `referral-prompt-ready` — feeds [#08 Referral Engine](../08-referral-engine/) (happy member is a prime referrer)
8. Exit

### Workflow 07c — Low-Score Handler

**Trigger:** Form Submitted → `Review — Private Feedback (Low Score)`

**Filter:** Contact has tag `campaign-review-ask`

**Actions:**

1. Update Field: `review_star_rating` = value from hidden field
2. Update Field: `review_submitted_date` = today
3. Update Field: `feedback_submitted_date` = today
4. Update Field: `private_feedback_text` = form field value
5. Add Tag: `feedback-received-private`
6. Remove Tag: `campaign-review-ask`
7. Add Tag: `do-not-ask-reviews` for **180 days** (we never ask again after a complaint — the cooldown is twice as long)
8. Notify Owner: HIGH PRIORITY email. Subject: `URGENT: {{contact.first_name}} {{contact.last_name}} left a {{rating}}-star private feedback`. Body: includes member name, phone, full feedback text, urgent issue if any, phone-call preference.
9. Create Task: Assigned to Owner. Title: `Follow up with {{contact.first_name}} {{contact.last_name}} — private feedback`. Due: 48 hours.
10. If `feedback_phone_ok` = Yes → Notify Owner additionally: "Member said OK to phone call."
11. Add tag: `risk-watching` (a member who's unhappy enough to leave 1-3 stars is also a retention risk — surface to [#05](../05-retention-and-churn-prevention/) monitoring)
12. Exit

### Publish both workflows.

---

## Step 6 — Build the Cooldown Cleanup Workflow (10 min)

`campaign-review-ask` should auto-clear after 90 days so the next eligible appointment can re-trigger.

- **Workflow Name:** `07 — Review Ask Cooldown Cleanup`
- **Folder:** `07 - Reviews`

### Trigger

- **Tag Added:** `campaign-review-ask`

### Actions

1. Wait 90 days
2. Remove tag: `campaign-review-ask`
3. Remove tag: `review-skipped-cooldown` (if present)
4. Exit

For `do-not-ask-reviews` (180-day version, applied after low-score feedback):

- Separate workflow with same structure, 180-day wait, removes `do-not-ask-reviews`.

---

## Step 7 — Owner Smart Lists (10 min)

Navigate to **Contacts > Smart Lists > + Create**.

### List 1: Pending Private Feedback Follow-Ups

- Name: `Reviews — Awaiting Owner Follow-Up`
- Filters: Tag `feedback-received-private`. `feedback_submitted_date` within last 7 days. No tag `feedback-owner-followed-up`.

### List 2: Recent Google Reviews Submitted

- Name: `Reviews — Google Wins (30d)`
- Filters: Tag `review-submitted-google`. `review_submitted_date` within last 30 days.

### List 3: High Promoters Ready for Referral Ask

- Name: `Reviews — Promoters Ripe for Referral`
- Filters: Tag `referral-prompt-ready` AND `review-submitted-google` (these are members who just left a 5-star review — perfect referral candidates).

### List 4: Eligible Review Asks Pending

- Name: `Reviews — Eligible But Not Asked Recently`
- Filters: Tag `member-active`. No tag `campaign-review-ask`. No tag `do-not-ask-reviews`. Last visit within 7 days. (Owner uses this to manually ask the right people in person.)

These feed [#10 Owner Reporting](../10-owner-reporting-and-visibility/).

---

## Test Plan

Run this test sequence. **Do not declare done until all pass.**

### Test 1 — Funnel routing for high score

1. Open the Smart Review Router URL: `/review/?contact_id={{test_contact_id}}`.
2. Tap the 😍 (5-star) emoji.
3. **Expected:** Lands on Page 2 ("Thanks!"). After 5 seconds, auto-redirects to Google review URL.
4. **Expected in GHL (Test Contact):** Tag `review-submitted-google` applied. `review_star_rating` = 5. `review_submitted_date` = today. Owner notification email lands.

### Test 2 — Funnel routing for low score

1. Open same URL with a different contact.
2. Tap the 😡 (1-star) emoji.
3. **Expected:** Lands on Page 3 (private feedback form).
4. Fill out form and submit.
5. **Expected:** Redirected to private thank-you page. Owner gets HIGH PRIORITY email. Owner task created. Tag `feedback-received-private` applied. Tag `do-not-ask-reviews` applied with 180-day expiry. Tag `risk-watching` applied (surfaces to retention monitoring).

### Test 3 — Workflow trigger from appointment

1. Set test contact: tag `member-active`, tag `risk-healthy`, no recent review.
2. Create an appointment for the contact, mark status = "Showed".
3. **Expected within 30 minutes:** Review-ask SMS arrives at test phone.
4. **Expected in GHL:** Tag `campaign-review-ask` applied.

### Test 4 — Cooldown blocks repeat asks

1. Same test contact from Test 3. Create another appointment within 90 days. Mark "Showed".
2. **Expected:** Workflow filter blocks. No SMS fires. Tag `review-skipped-cooldown` applied for visibility.

### Test 5 — At-Risk member excluded

1. Test contact with tag `risk-at-risk`. Create appointment, mark "Showed".
2. **Expected:** Filter blocks. No SMS.

### Test 6 — Follow-up email fires after no response

1. Test contact, fresh, eligible. Workflow fires SMS.
2. Wait 3 days (or fast-forward by manually advancing the wait step).
3. **Expected:** Follow-up email arrives.

### Test 7 — Suppression respected

1. Test contact with `do-not-sms` tag.
2. Workflow fires.
3. **Expected:** SMS skipped. Email step still fires after 3-day wait (since `do-not-email` not set).

### Test 8 — Referral prompt 7 days after Google review

1. After Test 1 (high score submitted), wait 7 days (or fast-forward).
2. **Expected:** Tag `referral-prompt-ready` applied. (Consumed by [#08](../08-referral-engine/).)

### Test 9 — Multiple emoji buttons all work

1. Test with each of the 5 emojis in sequence (on 5 different test contacts).
2. **Expected:** 1, 2, 3 → Page 3. 4, 5 → Page 2. Each star rating correctly stamped.

### Test 10 — Auto-redirect after 5 seconds

1. After tapping 5-star, observe Page 2 in browser.
2. **Expected:** Browser auto-redirects to Google review URL after 5 seconds without user action.

---

## Common Build Mistakes (avoid these)

1. **Asking the wrong people.** If the filter `NOT risk-at-risk` isn't in place, you'll send review asks to members who are about to cancel — guaranteed 1-star territory. Verify the filter rigorously.
2. **Sending the SMS too fast.** The 30-minute wait is intentional. Sending the SMS immediately after class feels mechanical; the endorphin window 30 min later is when the member is most positive.
3. **Page 2 redirect too fast.** If the redirect is instant, members feel railroaded. The 5-second delay shows the thank-you and gives a graceful exit. Keep it.
4. **No `do-not-ask-reviews` 180-day cooldown after a complaint.** Without this, a member who left private feedback could get re-asked in 90 days and leave more frustrated feedback. The 180-day cooldown gives time to fix the underlying issue.
5. **Funnel button URLs missing `contact_id`.** Without the contact_id, the rating handler workflow can't match the rating back to the right contact. Test the URL renders correctly with the merge field substituted.
6. **Google review URL is wrong.** Many studios use a long Google Maps URL instead of the dedicated "leave a review" short URL. Get the right one from Google My Business → "Share review form."
7. **Asking after a no-show.** Trigger filter is "Status = Showed" not "Status changed." A no-show appointment whose status later gets changed to "showed" by a front-desk correction won't auto-trigger because the status was never "Showed" at appointment time. Test with a real appointment marked Showed at end-of-day.
8. **Owner missing private complaints.** The HIGH PRIORITY email subject is critical — owner must filter/route this in their email client so it's seen quickly. Test the email arrives and is distinguishable from regular notifications.

---

## What's Next

Once this is live:

- Steady Google review growth — track week-over-week.
- Private complaints reach owner in <48hr, often <2hr — owner can save members who would have churned silently.
- High-rating members surface as referral candidates to **[#08 Referral Engine](../08-referral-engine/build.md)**.
- Reputation health KPIs flow into **[#10 Owner Reporting](../10-owner-reporting-and-visibility/build.md)** — Google star rating, review count delta, complaint resolution time.

Full integration: [../../integration/master-automation-graph.md](../../integration/master-automation-graph.md)
