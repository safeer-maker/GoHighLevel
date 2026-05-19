# #09 — Funnel Copy: Comeback Offer Checkout

> Production-ready copy for the Comeback Offer Funnel. A single-page checkout that auto-applies the correct win-back coupon (WB30, WB60, WB90LAST) based on URL parameter `?wb=30|60|90`. Paste directly into the GHL funnel builder.

---

## Funnel Settings

- **Funnel name:** `Sunrise — Comeback Offer`
- **Domain path:** `book.sunrisewellness.com/comeback/`
- **Brand colors:** Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Type:** Checkout funnel (2 pages: checkout + thank-you)
- **Coupon mechanism:** URL parameter `wb` → lookup → auto-applied coupon at checkout

---

## URL Pattern

```
https://book.sunrisewellness.com/comeback?wb=60
```

| Param Value | Coupon Applied | Discount |
|---|---|---|
| `wb=30` | `WB30` | 50% off first month |
| `wb=60` | `WB60` | $39 first month + waived $49 enrollment ($89 savings) |
| `wb=90` | `WB90LAST` | $29 first month + waived $49 enrollment ($99 savings) |
| (none) | (no coupon) | Standard pricing (Basic $79 + $49 enrollment) |

---

## PAGE 1 — Comeback Checkout

### Section 1: Hero (above-the-fold)

**Background:** Soft cream `#FFF8F0` with a sunrise gradient strip at top. Mid-shot photo of the studio interior — warm morning light, empty space (no models, no group shot — feels like "your spot is here, waiting").

**Eyebrow text (small, gold):**
> WELCOME BACK

**H1 (huge, deep slate, bold) — dynamic by `?wb=` value:**

| If `wb=` | H1 reads |
|---|---|
| `30` | Come back at 50% off your first month. |
| `60` | $39 first month. Enrollment waived. You save $89. |
| `90` | Last call: $29 first month, this week only. |
| (none) | Come back to Sunrise — your account's still here. |

**Subheadline (medium, deep slate):**

| If `wb=` | Subhead reads |
|---|---|
| `30` | Your member history is preserved. Your trainer's still here. Walk in tomorrow. |
| `60` | The strongest comeback offer we send. Auto-applied — no code needed. |
| `90` | Final offer of the season. Coupon expires in 7 days. |
| (none) | No enrollment fees for returning members. Your previous account picks up where you left off. |

**Below H1 — savings callout (gold pill badge):**

| If `wb=` | Savings line |
|---|---|
| `30` | **You save $39.50 this month** (50% off $79) |
| `60` | **You save $89 your first month** ($40 off + $49 enrollment waived) |
| `90` | **You save $99 your first month** ($50 off + $49 enrollment waived) |
| (none) | (suppress this section) |

---

### Section 2: The Checkout Block

**Background:** White card, soft shadow, centered on page.

**Heading (deep slate):**
> Your reactivation checkout

**Product preview (auto-rendered by GHL checkout component):**

| Item | Price | Notes |
|---|---|---|
| Basic Membership (Monthly Recurring) | $79.00 | Cancel anytime |
| Enrollment fee | (rendered based on coupon — $49 / $0 / etc) | |
| Coupon: **{{auto-applied code}}** | -{{discount}} | Auto-applied — green checkmark |
| **Total today** | **{{calculated}}** | |

**Customer info block (auto-prefilled if returning member is logged in):**

- First name
- Last name
- Email
- Phone (optional)
- Billing address (collapsed by default — only required for Stripe compliance)

**Payment block:**

- Stripe-hosted card field (PCI-compliant, never sees raw card)
- "Pay $X / month" submit button (label dynamically rendered)

**Trust line below button:**
> Secured by Stripe · Cancel anytime · No long-term contract

---

### Section 3: Tier Upgrade Option (soft cross-sell)

**Background:** Light cream panel below the main checkout.

**Heading (small, gold):**
> WHILE YOU'RE HERE

**Body:**
> Want to come back stronger? Most reactivating members go straight to Premium — adds 2 PT sessions a month + a nutrition consult for $70 more. Your comeback coupon still applies.

**Two-button row:**

> **[ Stay with Basic — $79/mo ]**  **[ Upgrade to Premium — $149/mo + same coupon ]**

(Premium button updates the checkout product on click; coupon recalculates.)

---

### Section 4: What Members Say About Coming Back

**H2:**
> Members who came back — and stayed

**Three short testimonials (carousel on mobile):**

**Testimonial 1:**
> "I took 6 months off after a knee injury and was nervous about coming back. The owner remembered my name from the day I walked in. My trainer adjusted everything for the recovery. I'm now stronger than before."
> — **James K., reactivated 2024**

**Testimonial 2:**
> "I cancelled when my work schedule went crazy. Six weeks later I got a "we miss you, 50% off" text and figured what the hell. Best decision. The 6 AM crew is family now."
> — **Lin H., reactivated 2024**

**Testimonial 3:**
> "Switched to a cheaper gym, hated it, came back. Sunrise was nice about it — no "told you so," no fees. Just "welcome back."
> — **Marcus T., reactivated 2023**

---

### Section 5: FAQs

**H2:**
> A few quick answers

**Accordion (expand-on-click):**

**Q: Do I have to start over with onboarding?**
> A: Not at all. Your previous tier, trainer, goal notes, and member history are all preserved. You log in like you never left. We'll do a quick "what's changed in your goals" check-in in week 1, but no full reonboarding.

**Q: What if I want to cancel again later?**
> A: Cancel any time, no fees, no hassle. We process cancellations through the same form as before. If life shifts again, you're welcome back at any point.

**Q: Can I pause instead of paying monthly?**
> A: Yes — paused memberships are $0/month for up to 3 months, account preserved. If you want to start that way instead of a full reactivation, just hit reply to any of our messages and Morgan will set it up personally.

**Q: Is the coupon really auto-applied? Do I need to enter a code?**
> A: Auto-applied. Look at the checkout block above — you'll see the coupon line with a green checkmark. No code entry needed.

**Q: When does the coupon expire?**
> A: WB30: 14 days. WB60: 21 days. WB90LAST: 7 days. After that, you can still come back at standard pricing — the coupon is the only thing that expires, not your option to return.

---

### Section 6: Footer

- Studio address: `{{custom_values.business.address_line}}`
- Phone: `{{custom_values.business.phone}}`
- Hours: `{{custom_values.hours.full}}`
- Small links: Privacy · Terms · Contact · Cancellation Policy
- Icons: Instagram · Facebook · Google Maps

---

## PAGE 2 — Welcome Back / Thank-You

### Section 1: Confirmation

**Background:** Sunrise gradient (coral → gold → white).

**Large checkmark icon (gold)**

**H1:**
> Welcome back, {{contact.first_name}} ☀️

**Subhead:**
> Your membership is reactivated and your first class is one tap away. We just texted you a booking link.

**Mini-summary block (white panel):**

| Item | Status |
|---|---|
| Membership | **{{contact.membership_tier}}** — ${{contact.monthly_rate}}/month |
| First payment | **Processed** ({{date_today}}) |
| Next billing | {{date_today + 30 days}} |
| Member status | **Active** |

---

### Section 2: What Happens Next

**H2:**
> What happens next

**Numbered list:**

1. **In the next 5 minutes** — You'll get a text from Morgan personally welcoming you back.
2. **This week** — Your previous trainer ({{contact.assigned_trainer}}) will check in to recalibrate your goals.
3. **Walk in any time** — Front desk will be expecting you. No re-orientation needed unless you want one.

---

### Section 3: Book Your First Class Back

**CTA (large coral button, centered):**

> **Book My First Class →**

(Links to `{{custom_values.business.booking_url}}`)

**Below button (small):**
> Or browse the schedule, see who's teaching what — your member portal is already loaded.

---

### Section 4: Soft Secondary CTAs

**3-icon row:**

| Icon | Action |
|---|---|
| 📱 | **Get the Sunrise app** — [iOS] [Android] |
| 📅 | **See this week's schedule** |
| 💪 | **Book a fresh PT session** (first one for returners is on us) |

---

### Section 5: Footer — same as Page 1

---

## Coupon Auto-Application Mechanics — Builder Notes

The single most important technical detail in this funnel: **the coupon must auto-apply silently from the URL parameter**, with zero member action required.

### Approach 1 — Native GHL Checkout Coupon-from-URL (preferred)

In the GHL checkout component settings:
- Find **"Coupon source"** or **"Pre-apply coupon from URL"**
- Set parameter name: `wb`
- Set lookup map:
  - `30` → `WB30`
  - `60` → `WB60`
  - `90` → `WB90LAST`

If GHL exposes this natively, use it. Cleanest, most robust.

### Approach 2 — JS Snippet on Funnel Page (fallback)

If GHL doesn't expose native URL→coupon lookup, embed this snippet on the funnel page (top of `<head>`, runs before checkout renders):

```html
<script>
  (function() {
    const params = new URLSearchParams(window.location.search);
    const wb = params.get('wb');
    if (!wb) return;
    const couponMap = { '30': 'WB30', '60': 'WB60', '90': 'WB90LAST' };
    const code = couponMap[wb];
    if (!code) return;

    // Wait for GHL checkout to render
    const tryApply = setInterval(function() {
      const couponInput = document.querySelector('input[name="coupon"], input[data-field="coupon"]');
      if (couponInput) {
        couponInput.value = code;
        couponInput.dispatchEvent(new Event('change', { bubbles: true }));
        couponInput.dispatchEvent(new Event('input', { bubbles: true }));
        clearInterval(tryApply);
      }
    }, 250);

    // Stop trying after 10 seconds
    setTimeout(function() { clearInterval(tryApply); }, 10000);
  })();
</script>
```

### Approach 3 — Three Separate Funnels (if neither above works)

Build three distinct funnels — `/comeback-30`, `/comeback-60`, `/comeback-90` — each with its coupon hardcoded in the checkout component. Less elegant; more to maintain. Use only as last resort.

---

## Dynamic Headline Mechanics

The headline + subhead + savings callout all change based on `?wb=` value.

### Approach: JS Snippet (universal)

```html
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const wb = new URLSearchParams(window.location.search).get('wb');
    const content = {
      '30': {
        h1: 'Come back at 50% off your first month.',
        sub: 'Your member history is preserved. Your trainer\'s still here. Walk in tomorrow.',
        savings: 'You save $39.50 this month (50% off $79)'
      },
      '60': {
        h1: '$39 first month. Enrollment waived. You save $89.',
        sub: 'The strongest comeback offer we send. Auto-applied — no code needed.',
        savings: 'You save $89 your first month ($40 off + $49 enrollment waived)'
      },
      '90': {
        h1: 'Last call: $29 first month, this week only.',
        sub: 'Final offer of the season. Coupon expires in 7 days.',
        savings: 'You save $99 your first month ($50 off + $49 enrollment waived)'
      },
      'default': {
        h1: 'Come back to Sunrise — your account\'s still here.',
        sub: 'No enrollment fees for returning members. Your previous account picks up where you left off.',
        savings: null
      }
    };
    const c = content[wb] || content['default'];
    document.querySelector('[data-dynamic="h1"]').textContent = c.h1;
    document.querySelector('[data-dynamic="sub"]').textContent = c.sub;
    const savingsEl = document.querySelector('[data-dynamic="savings"]');
    if (c.savings) {
      savingsEl.textContent = c.savings;
    } else {
      savingsEl.style.display = 'none';
    }
  });
</script>
```

And tag each headline/subhead/savings element with the matching `data-dynamic="..."` attribute.

---

## Mobile-First Notes

- 70%+ of comeback traffic is mobile (members tap from the SMS link).
- Stripe checkout component must render cleanly on mobile — verify card field auto-focuses to numeric keyboard.
- Coupon-applied indicator (green checkmark + "WB60 applied") must be visible above the fold on mobile — this is the trust signal that the offer is real.
- Tier-upgrade buttons (Section 3) stack vertically on mobile.

---

## Conversion Tracking

| Platform | Event | Notes |
|---|---|---|
| Meta Pixel | `Purchase` event with monetary value | Distinguish in-platform: `lead_source = winback` |
| Google Ads | `Conversion` label `reactivation`, value = `monthly_rate × 6` | LTV for reactivated members is more conservative |
| GHL native analytics | Automatic — checkout success tracked |

---

## Build Verification

After creating the funnel:

1. Open `https://book.sunrisewellness.com/comeback?wb=30` in incognito.
2. **Expected:**
   - H1 reads "Come back at 50% off your first month."
   - Coupon `WB30` shows in checkout with green checkmark.
   - Subtotal calculation: $79 × 50% = $39.50 + $49 enrollment = $88.50 (or whatever WB30 actually waives).
3. Repeat for `?wb=60` and `?wb=90` — verify each shows its correct headline + coupon + savings.
4. Open `https://book.sunrisewellness.com/comeback` (no param) — verify generic copy, no coupon applied, standard pricing.
5. Complete a test checkout with `?wb=60` using a Stripe test card. Verify:
   - `member-reactivated` tag applies (via Workflow `09d`)
   - All campaign-winback-* tags removed
   - Retention pipeline moves to "Reactivated" stage
   - Welcome-back SMS + email arrive
   - Owner internal notification fires
