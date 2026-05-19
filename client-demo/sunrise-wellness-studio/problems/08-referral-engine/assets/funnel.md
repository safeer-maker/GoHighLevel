# #08 — Funnel Copy: Referral Landing

> Production-ready copy for the referral landing funnel. The headline and hero block dynamically render the referrer's first name from the URL parameter `ref_name`. Paste directly into the GHL funnel builder.

---

## Funnel Settings

- **Funnel name:** `Sunrise — Referral Landing`
- **Domain path:** `book.sunrisewellness.com/refer/`
- **Brand colors:** Same as #01 — Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Primary CTA color:** Coral
- **Personalization mechanism:** URL parameter `ref_name` rendered via `{{request.params.ref_name}}` merge field

---

## URL Pattern (the link members share)

```
https://book.sunrisewellness.com/refer/?ref_name=SARAH&ref_id=abc123xyz&ref_code=SARAH-42&lead_source=Referral
```

| Param | Source | Used For |
|---|---|---|
| `ref_name` | Referrer's first name, uppercased | Hero personalization |
| `ref_id` | Referrer's GHL contact ID | Form hidden field → `referred_by_contact_id` |
| `ref_code` | Referrer's `referral_code` (e.g., SARAH-42) | Form hidden field → `referral_code_used` |
| `lead_source` | Fixed value `Referral` | Form hidden field → `lead_source` |

---

## PAGE 1 — Personalized Hero / Landing Page

### Section 1: Hero (above-the-fold)

**Background:** Same as #01 — bright morning shot of a sun-drenched studio. Coral/gold tones. Light dark overlay for text contrast. Use the *exact same* hero photo as the main lead-capture funnel so the brand is instantly recognizable.

**Eyebrow text (small, gold):**
> A GIFT FROM A FRIEND

**H1 (huge, white, bold) — personalized:**
> {{request.params.ref_name}} sent you $20 off your first month at {{custom_values.business.short_name}}.

**Fallback H1 if `ref_name` is empty:**
> Your friend sent you $20 off your first month at {{custom_values.business.short_name}}.

**Subheadline (medium, white, readable):**
> They thought you'd love it here. Claim their $20 credit, try every class free for 7 days, and decide for yourself. No credit card needed today.

**Primary CTA button:**
> **Claim My $20 Credit + Free Pass →**

(Scrolls to Page 2 form OR navigates to `/refer/claim`.)

**Below button — small trust line:**
> ★★★★★ 4.9 from 240+ members · Cancel anytime · $20 off applied automatically

---

### Section 2: Social Proof Bar — same as #01

**Layout:** Single row, centered.

**Text (left):**
> Trusted by **240+** Springfield wellness lovers — and now, by {{request.params.ref_name}}.

**(Fallback: drop the "and now, by..." clause if `ref_name` is empty.)**

**Right side:** Five gold stars + "**4.9 / 5.0** on Google"

**Below:** Three small circular member photos (avatar style) with first names.

---

### Section 3: Why {{request.params.ref_name}} Sent You This

**H2 (centered, deep slate):**
> Why {{request.params.ref_name}} sent you this

**(Fallback: "Why your friend sent you this")**

**Body (single paragraph, deep slate, large):**
> Sunrise members refer friends for one reason: this place changes how they feel about working out. Whether it's the 6 AM HIIT crew that knows your name, the Sunday morning yoga that resets the week, or the trainer who actually teaches instead of just yelling — there's a reason {{request.params.ref_name}} thought of you when we asked who they'd bring.

---

### Section 4: What You Get (claim breakdown)

**H2 (centered):**
> Here's what's waiting for you

**3-column layout** (stacks on mobile). Each column: icon + bold label + 1-line description.

| Icon | Label | Description |
|---|---|---|
| 🎁 | **$20 off your first month** | Applied automatically at checkout — no code needed. |
| ☀️ | **7-day free trial first** | Try every class and the gym before you decide. No card required. |
| 🌱 | **Intro consult with a trainer** | 30 minutes to map your goals — free, no strings. |

**Below the columns — single CTA, smaller:**
> **Yes, claim my $20 credit →**

---

### Section 5: Real Members. Real Wins.

(Identical to #01 — three testimonials. Re-used intentionally so the brand experience is consistent across funnels.)

**H2:**
> Real members. Real wins.

**Testimonial 1:**
> "I'd tried four gyms in two years. This is the first one I actually look forward to. The 6 AM HIIT class genuinely changed my mornings."
> — **Priya M., member since 2024**

**Testimonial 2:**
> "Lost 22 pounds in 4 months, and honestly the food coaching was the biggest piece. The trainers don't just yell at you — they teach you."
> — **Marcus T., member since 2023**

**Testimonial 3:**
> "After my injury I thought I was done with fitness. The recovery program here got me back. I'm doing things I haven't done since college."
> — **Diane K., member since 2024**

---

### Section 6: How It Works

**H2:**
> Here's how it works

**4-step layout (numbered, horizontal on desktop):**

| Step | Title | Description |
|---|---|---|
| **1** | **Claim your pass** | Quick form — 30 seconds. Your $20 credit and {{request.params.ref_name}}'s name come with you. |
| **2** | **We text you a booking link** | Pick your first class or PT session. |
| **3** | **Try 7 days, free** | Every class, every machine, the whole studio. |
| **4** | **If you join — $20 off month one** | Auto-applied at checkout if you decide to stay. Cancel anytime. |

---

### Section 7: Final CTA (sticky on scroll)

**Background:** Coral gradient.

**H2 (white, bold):**
> {{request.params.ref_name}} thinks you'll love it. We do too.

**(Fallback: "Your friend thinks you'll love it. We do too.")**

**Subhead (white):**
> 7 days free. $20 off your first month. No credit card needed today.

**Primary CTA:**
> **Claim My $20 Credit + Free Pass →**

**Below button — small reassurance:**
> No pushy sales. Just the studio.

---

### Footer — same as #01

- Studio address: `{{custom_values.business.address_line}}`
- Phone: `{{custom_values.business.phone}}`
- Hours: `{{custom_values.hours.full}}`
- Small links: Privacy · Terms · Contact
- Icons: Instagram, Facebook, Google Maps

---

## PAGE 2 — Claim / Form Page

### Section 1: Mini-Hero (personalized)

**Background:** Soft cream `#FFF8F0` with a subtle sunrise gradient strip at top.

**Eyebrow:**
> CLAIMING YOUR FRIEND'S GIFT

**H1:**
> You're 30 seconds from your free week + $20 credit.

**Subhead:**
> Tell us a little about you so we can text you a booking link. {{request.params.ref_name}}'s credit comes with you automatically.

**(Fallback subhead: drop the "{{request.params.ref_name}}'s credit" clause; use "Your $20 credit comes with you automatically.")**

---

### Section 2: The Form

(Form fields exact spec in [forms.md](forms.md).)

**Form heading (small, above form):**
> All fields below. We ask about your goal so we don't waste your time recommending the wrong class.

**Submit button label:**
> **Get My Free Week + $20 Credit →**

**Below button (small):**
> By submitting, you agree to receive texts and emails from `{{custom_values.business.short_name}}`. We'll never spam, sell, or share your info. Reply STOP anytime.

---

### Section 3: Trust Strip — identical to #01

| Icon | Text |
|---|---|
| 🚫💳 | No credit card |
| ⏸️ | Cancel anytime |
| 💬 | Real humans reply |

---

## PAGE 3 — Thank-You / Welcome Page

### Section 1: Confirmation (personalized credit message)

**Background:** Sunrise gradient (coral → gold → white).

**Large checkmark icon (gold)**

**H1:**
> You're in, `{{contact.first_name}}` — check your phone!

**Subhead:**
> We just texted you a booking link from `{{custom_values.business.short_name}}`. Tap it and you'll be set up in under a minute.

**Personal thank-you band (gold panel):**
> ☀️ **Tell {{request.params.ref_name}} thanks** — they just earned a free PT session because of you. We'll send them a note too.

**(Fallback: "Tell your friend thanks — they just earned a free PT session because of you.")**

---

### Section 2: While You're Here — same as #01

**H2:**
> While you're waiting — meet the studio.

**Embed:** Instagram feed widget showing @sunrisewellnessstudio.

---

### Section 3: What Happens Next

**H2:**
> What happens next?

**Numbered list:**

1. **In the next 5 minutes** — You'll get a text with a link to book your first class or PT session.
2. **Day 1** — Show up. Front desk will greet you and give you the studio tour. Tell them {{request.params.ref_name}} sent you.
3. **Day 7** — Your trainer follows up to see how it went and answer any questions.
4. **If you join** — Your $20 credit auto-applies at checkout. You don't need a code.

---

### Footer — same as #01

---

## Personalization Mechanics — Builder Notes

GHL's funnel builder supports URL parameter merge fields. The expression `{{request.params.ref_name}}` resolves at page-render time to whatever value is in the URL.

**Critical fallback handling:**

For each text element that uses `{{request.params.ref_name}}`, the GHL builder should expose a "default value" or "fallback" field. Use these defaults:

| Element | Default if `ref_name` missing |
|---|---|
| H1 hero | `Your friend` |
| Social proof "and now, by" clause | (suppress entirely — drop the clause) |
| Section 3 H2 | `Why your friend sent you this` |
| Section 4 sticky CTA | `Your friend` |
| Thank-you "Tell X thanks" | `your friend` |

If GHL doesn't support per-element fallbacks, use the JS Custom Code block at the top of each page:

```javascript
<script>
  if (!new URLSearchParams(window.location.search).get('ref_name')) {
    document.querySelectorAll('[data-ref-name]').forEach(el => {
      el.textContent = 'your friend';
    });
  }
</script>
```

And tag each personalized element with `data-ref-name="true"` attribute.

---

## Mobile-First Notes

- Same as #01: 70%+ mobile traffic, CTA buttons ≥ 56px, form page optimized for one-thumb completion.
- Personalized headline renders as 2–3 lines on mobile when name is long (e.g., "ELIZABETH") — verify wrapping at common name lengths (4, 8, 12 chars).
- Hero photo: ensure subject's face is above-the-fold even on smallest phones; use `object-position: top`.

---

## A/B Test Variants (after baseline)

| Test | Variant A (control) | Variant B |
|---|---|---|
| Hero H1 angle | "{{ref_name}} sent you $20 off…" | "{{ref_name}} thinks you'd love Sunrise. Here's $20 to try it." |
| Sticky CTA angle | "{{ref_name}} thinks you'll love it. We do too." | "Walk in once with {{ref_name}}'s gift. We'll do the rest." |
| Reward framing | "$20 off your first month" | "$20 credit + waived enrollment ($69 saved)" |

Test one at a time, 2 weeks each, 50+ visits per variant minimum before declaring a winner.
