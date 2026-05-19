# #07 — Funnel Copy: Smart Review Router

> This is the critical reputation-management mechanic. A 3-page funnel that asks one simple question, then **branches to different destinations** based on the answer. High scores → Google review. Low scores → private feedback form (never public).

---

## Funnel Settings

- **Funnel name:** `Sunrise — Smart Review Router`
- **Domain:** book.sunrisewellness.com/review (or sub-path)
- **Brand colors:** Sunrise Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Primary CTA color:** Sunrise Coral
- **Font:** Heading: bold sans-serif. Body: clean readable.
- **Personalization:** Reads `contact_id` URL parameter, server-renders member first name

---

## PAGE 1 — "How Was Your Session?" (the rating selector)

### Layout

**Background:** Soft cream `#FFF8F0` with a subtle sunrise gradient strip at the top (coral fading to gold).

**Top bar:** Small Sunrise logo, centered, with brand tagline beneath in tiny gold: "Rise. Move. Glow."

---

### Section 1: Hero (centered, generous vertical spacing)

**H1 (large, deep slate, bold):**

> How was your session, {{contact.first_name}}?

**Subhead (medium, regular weight):**

> Tap how it felt. 30 seconds, single tap. That's the whole thing.

---

### Section 2: The 5-Emoji Button Row (THE critical element)

**Layout:** Single horizontal row, 5 large circular buttons, equally sized, centered. Stacks gracefully on mobile but should fit horizontally even on phones (each button ~60px diameter).

**Buttons (left to right):**

| Position | Emoji | Color around button | Hover label | Star value | Routes to |
|---|---|---|---|---|---|
| 1 | 😡 | Red border | "1 — Rough" | 1 | `/review/feedback?rating=1&contact_id={{contact.id}}` |
| 2 | 😕 | Orange border | "2 — Off" | 2 | `/review/feedback?rating=2&contact_id={{contact.id}}` |
| 3 | 😐 | Gold border | "3 — Okay" | 3 | `/review/feedback?rating=3&contact_id={{contact.id}}` |
| 4 | 😊 | Light coral border | "4 — Good" | 4 | `/review/thanks?rating=4&contact_id={{contact.id}}` |
| 5 | 😍 | Bright coral border | "5 — Loved it" | 5 | `/review/thanks?rating=5&contact_id={{contact.id}}` |

**Button size:** 60px diameter on mobile, 80px on desktop.

**Spacing between buttons:** 16px on mobile, 24px on desktop.

**Below the row, small text (centered, gold):**

> Each button takes you to a different page based on how it went.

---

### Section 3: Reassurance Footer

**Below the buttons, small centered text:**

> *Your response goes straight to Morgan. We read every single one. No spam, no follow-up unless you'd like one.*

**Even smaller, gray:**

> A {{custom_values.business.short_name}} thing.

---

### Section 4: Sticky Footer

- Small "Powered by Sunrise" link to home
- {{custom_values.business.address_short}} · {{custom_values.business.phone}}
- Tiny "Privacy" link

---

### Page 1 Design Notes

- The hero + emoji row should fit above the fold on every device — no scrolling required to make a choice.
- Each button on hover (desktop) or tap-and-hold (mobile) shows the label ("1 — Rough", etc.) for clarity.
- The buttons must be **visually equal**, not bigger for higher ratings. Subtle color variation only. Bias the design and you bias the response.
- No exit option, no "skip," no other navigation — the only path forward is tap one of the 5 buttons.
- Page load target: <1.5 seconds.

---

## PAGE 2 — Thanks + Google Redirect (high-score path)

### Layout

**Background:** Sunrise gradient (coral → gold → cream).

**Center-aligned, vertical generous spacing.**

---

### Section 1: Confirmation

**Large checkmark icon (gold, animated entrance)**

**H1 (large, white on coral, bold):**

> {{contact.first_name}}, that's amazing — thank you ☀️

**Subhead (white, regular):**

> Would you mind taking 30 more seconds to share on Google? It genuinely helps other people find us.

---

### Section 2: The Google CTA

**Primary CTA button (large, white background with coral text):**

> **Leave a Google Review →**

(Links to `{{custom_values.business.google_review_url}}`)

**Below button, small white text:**

> We'll redirect you automatically in 5 seconds…
>
> *(or close this tab if you'd rather not — totally fine.)*

---

### Section 3: Auto-Redirect Mechanism

**Embed in page footer (JavaScript):**

```html
<script>
  // Auto-redirect after 5 seconds, unless user has already clicked the button or closed
  var redirectTimer = setTimeout(function(){
    window.location.href = "{{custom_values.business.google_review_url}}";
  }, 5000);

  // Optional: cancel the auto-redirect if user starts interacting
  document.addEventListener('click', function(){
    clearTimeout(redirectTimer);
  });
</script>
```

The 5-second delay is intentional:
- Gives the member time to read the thanks (don't rush them).
- Gives a moment to opt out by closing the tab (respect autonomy).
- Long enough to feel intentional, short enough that members don't get distracted.

---

### Section 4: Footer

- Small Sunrise logo
- "Thank you" wordmark in gold
- {{custom_values.business.address_short}}
- Tiny "Privacy" link

---

### Page 2 Design Notes

- The thank-you message must feel warm and complete — even if the member never goes to Google, this page should leave them with a positive feeling.
- The auto-redirect text is important — never auto-redirect silently. The user should know what's about to happen.
- Don't add a guilt mechanism ("We *really* need your review!") — the soft ask works better than the hard ask, and respects the relationship.

---

## PAGE 3 — Private Feedback Form (low-score path)

### Layout

**Background:** Soft cream `#FFF8F0`, no gradient — should feel calm and serious, not celebratory.

**Center-aligned, generous vertical spacing.**

---

### Section 1: The Honest Open

**H1 (large, deep slate, bold):**

> Oof — sorry, {{contact.first_name}}. What happened?

**Subhead (medium):**

> Tell us so we can make it right. This goes straight to Morgan — never anywhere public.

---

### Section 2: The Form

Form spec in [forms.md](forms.md). High-level fields:

**Field 1 (required, multi-line text):**

> **What could we have done better?**
> 
> *(The more specific you can be, the more we can actually fix.)*

**Field 2 (optional, multi-line text):**

> **Is there anything specific we should fix today?**
> 
> *(If something's broken / unsafe / urgent, let us know.)*

**Field 3 (optional, checkbox):**

> ☐ I'd be open to a quick phone call from Morgan to talk this through.

**Field 4 (optional, radio):**

> **Best way to reach you:**
>
> ◯ Email
> ◯ Text
> ◯ Phone

---

### Section 3: Submit

**Submit button (large, coral, centered):**

> **Send to Morgan**

**Below button, small text:**

> We'll get back to you within 24 hours — often much faster.

---

### Section 4: Trust Footer

**Small centered text, dark gray:**

> *Your feedback goes only to Morgan and is never published. We don't share or sell anything. Just real feedback to a real person who can fix it.*

---

### Page 3 Design Notes

- The page should feel like writing to a friend who can actually help, not like filling out a complaint form at a hotel front desk.
- No long terms-of-service text. No CAPTCHA (unless spam becomes an issue).
- Submit button text says "Send to Morgan" — names the recipient, makes it human.
- "Sorry" in the H1 is intentional — preemptively acknowledges that the experience wasn't great. This disarms members who arrived ready to vent.

---

## PAGE 4 — Private Feedback Thank-You

Loads after Page 3 form submission.

### Layout

**Background:** Same calm cream as Page 3.

---

**H1 (centered, deep slate):**

> Got it, {{contact.first_name}}.

**Body (centered):**

> Morgan will be in touch within 24 hours. Often much faster.
> 
> Thank you for telling us — the members who tell us when something's off are the ones who actually help us run the studio better.

**Below, soft secondary CTA:**

> If you'd rather text us directly: {{custom_values.business.sms_number}}
>
> Or call: {{custom_values.business.phone}}

---

### Footer (same as Page 1)

---

## Funnel-Wide Notes

### Personalization mechanics

Every page reads `contact_id` from the URL query parameter and personalizes the greeting. If `contact_id` is missing (rare — only happens if someone manually shares the funnel URL without the param), fall back gracefully:

- Page 1: "How was your session?" (no name)
- Page 2: "That's amazing — thank you ☀️" (no name)
- Page 3: "Oof — sorry. What happened?" (no name)

### URL parameter handling

Each rating button passes `rating=X&contact_id=Y` to the next page. The destination page:
1. Reads URL parameters via JavaScript on page load
2. Posts to a workflow webhook with the values, OR triggers an inline GHL Update Contact action
3. Renders personalized content

### Mobile-first

70%+ of traffic will be mobile. Test all pages on iPhone SE (the small-screen worst case) and a mid-range Android:
- Page 1 emoji row must fit on one row on every screen
- Page 2 redirect text must be readable
- Page 3 form must be one-thumb fillable

### Accessibility

- Each emoji button has an `aria-label` matching the hover label ("1 of 5 stars - Rough", etc.)
- Color contrast WCAG AA minimum
- Keyboard navigation works (tab through buttons, Enter to select)
- Screen reader announces the rating selection clearly

### Tracking

- Page 1 visits, Page 2 visits, Page 3 visits, and form submissions are tracked in GHL Funnel Analytics
- Rating distribution (1s, 2s, 3s, 4s, 5s) becomes the studio's real NPS data
- The ratio of Page 2 visits to Page 3 visits = % of members rating 4+ vs 1-3 — the studio's actual customer satisfaction signal

---

## A/B Test Variants (after launch)

After 60 days of baseline data, consider testing:

| Test | Variant A (control) | Variant B |
|---|---|---|
| Page 1 H1 | "How was your session, {{name}}?" | "Quick — how was today?" |
| Emoji style | Default OS emoji | Custom branded star icons |
| Page 2 redirect delay | 5 seconds | 8 seconds (more reading time) |
| Page 2 CTA wording | "Leave a Google Review" | "Share on Google" (softer) |
| Page 3 H1 | "Oof — sorry. What happened?" | "We hear you. What went wrong?" |

Run each test for 4 weeks, 100+ responses per variant minimum.

---

## Edge Cases

| Scenario | Funnel behavior |
|---|---|
| Member taps button on Page 1 but then closes the tab before Page 2/3 loads | Rating IS NOT recorded (the rating handler workflow fires on Page 2/3 load, not button tap). Acceptable trade-off — protects against accidental taps. |
| Member taps 5-star, lands on Page 2, but closes the tab before auto-redirect | Tag `review-submitted-google` IS applied (page-load tracking) even though they may not actually write a Google review. Counts as "intended to review" — close enough for KPI purposes. |
| Member submits the private feedback form with empty required field | Form validation blocks submission, shows inline error: "Please tell us what we could've done better — even one sentence helps." |
| Member's `contact_id` URL param is invalid or missing | Funnel works generically (no personalization). Rating updates fail silently. Owner notification still fires from the form submission. |
| Multiple submissions from same contact within an hour | Workflow filter blocks duplicate handling — only the first counts. Subsequent ones are logged for visibility but don't re-trigger the owner alert. |
| Member tries to tap multiple emojis | Buttons should debounce — only the first tap registers. The next page loads and any subsequent tap is on a different page anyway. |

---

## What Comes Next

After funnel interaction:

- **High score (4 or 5):** Workflow 07b fires. Tag `review-submitted-google`. Field updates. Thank-you SMS lands 1 hour later. Tag `referral-prompt-ready` added 7 days later → consumed by [#08 Referral Engine](../../08-referral-engine/).
- **Low score (1, 2, 3):** Workflow 07c fires. Tag `feedback-received-private`. Owner notification HIGH PRIORITY. Owner task created with 48hr deadline. Tag `do-not-ask-reviews` applied for 180 days. Tag `risk-watching` applied — surfaces to [#05 retention monitoring](../../05-retention-and-churn-prevention/).
- **No interaction (member doesn't tap):** Email follow-up sent 3 days later. If still no engagement after 7 days, member left alone for 90 days.
