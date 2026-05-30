# #01 — Funnel Copy: Free 7-Day Pass Lead Capture

> Production-ready copy for every page of the lead capture funnel. Paste directly into the GHL funnel builder. All `{{custom_values.*}}` and `{{contact.*}}` merge fields resolve at render time — do not replace them with literals.

---

## Funnel Settings

- **Funnel name:** `Sunrise — Free 7-Day Pass — Lead Capture`
- **Domain:** book.sunrisewellness.com (or sub-path on main site)
- **Brand colors:** Sunrise Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Primary CTA color:** Sunrise Coral, white email, 8px rounded corner, large mobile-tappable
- **Font:** Heading: bold sans-serif (Poppins or Montserrat). Body: clean readable (Inter or Open Sans).

---

## PAGE 1 — Hero / Landing Page

### Section 1: Hero (above-the-fold)

**Background:** Full-width photo — bright morning shot of someone mid-stretch in a sun-drenched studio, warm coral/gold tones, smile visible. Light dark overlay for email contrast.

**Eyebrow email (small, gold):**
> YOUR FIRST 7 DAYS — ON US

**H1 (huge, white, bold):**
> Rise stronger. Move better. Glow brighter.

**Subheadline (medium, white, readable):**
> Try every class, every machine, and meet your trainer — all free for 7 days. No credit card. No pressure. Just the studio Springfield's been talking about.

**Primary CTA button:**
> **Claim My Free 7-Day Pass →**

(Button scrolls to Page 2 form OR opens form in modal.)

**Below button — small trust line:**
> ★★★★★ 4.9 from 240+ members · Cancel anytime · No credit card

---

### Section 2: Social Proof Bar

**Layout:** Single row, centered.

**Text (left):**
> Trusted by **240+** Springfield wellness lovers

**Right side:** Five gold stars + small email "**4.9 / 5.0** on Google"

**Below:** Three small circular member photos (avatar style) with first names.

---

### Section 3: What's Included in Your 7 Days

**H2 (centered, deep slate):**
> Everything you get — completely free

**3-column layout** (stacks on mobile). Each column: icon + bold label + 1-line description.

| Icon | Label | Description |
|---|---|---|
| ☀️ (sunrise icon) | **Unlimited Group Classes** | HIIT, Yoga, Pilates, Strength, Recovery — try them all. |
| 💪 (dumbbell icon) | **Full Gym Access** | Functional training floor, free weights, recovery zone. |
| 🌱 (sprout icon) | **Personal Intro Consult** | 30 minutes with a trainer to map out your goals. |

**Below the columns — single CTA, smaller:**
> **Yes, I want my free 7 days →**

---

### Section 4: Real Members. Real Wins.

**H2:**
> Real members. Real wins.

**3 testimonial cards** (carousel on mobile). Each: photo, name, member-since date, 1-line quote.

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

### Section 5: How the Free Trial Works

**H2:**
> Here's how it works

**3-step layout (numbered, horizontal on desktop):**

| Step | Title | Description |
|---|---|---|
| **1** | **Claim your pass** | Tell us a tiny bit about you. Takes 30 seconds. |
| **2** | **We email you a booking link** | Pick your first class or PT session — whatever fits your week. |
| **3** | **Walk in & start** | Show up. We'll take care of the rest. |

---

### Section 6: Final CTA (sticky on scroll)

**Background:** Coral gradient.

**H2 (white, bold):**
> Your sunrise starts now.

**Subhead (white):**
> 7 days. Every class. No commitment. Let's go.

**Primary CTA:**
> **Claim My Free 7-Day Pass →**

**Below button — small reassurance:**
> No credit card. No pushy sales. Just the studio.

---

### Footer

- Studio address: `{{custom_values.business.address_line}}`
- Email: `{{custom_values.business.email}}`
- Hours: `{{custom_values.hours.full}}`
- Small links: Privacy · Terms · Contact
- Icons: Instagram, Facebook, Google Maps

---

## PAGE 2 — Claim / Form Page

### Section 1: Mini-Hero

**Background:** Soft cream `#FFF8F0` with a subtle sunrise gradient strip at top.

**Eyebrow:**
> STEP 1 OF 1

**H1:**
> You're 30 seconds from your free 7 days.

**Subhead:**
> Tell us a little about you so we can email you a booking link.

---

### Section 2: The Form

(Form fields exact spec in [forms.md](forms.md).)

**Form heading (small, above form):**
> All fields below. Yes, we ask about your goal — so we don't waste your time recommending the wrong class.

**Submit button label:**
> **Get My Free 7-Day Pass →**

**Below button (small):**
> By submitting, you agree to receive emails from `{{custom_values.business.short_name}}`. We'll never spam, sell, or share your info. Reply STOP anytime.

---

### Section 3: Trust Strip

**3-icon row, small, gray email:**

| Icon | Text |
|---|---|
| 🚫💳 | No credit card |
| ⏸️ | Cancel anytime |
| 💬 | Real humans reply |

---

## PAGE 3 — Thank-You / Welcome Page

### Section 1: Confirmation

**Background:** Sunrise gradient (coral → gold → white).

**Large checkmark icon (gold)**

**H1:**
> You're in, `{{contact.first_name}}` — check your email!

**Subhead:**
> We just emailed you a booking link from `{{custom_values.business.short_name}}`. Tap it and you'll be set up in under a minute.

**Below subhead — friendly note:**
> *Didn't see the email within a couple minutes? Check your spam folder for the welcome email, or email us at `{{custom_values.business.email}}` and we'll get you sorted.*

---

### Section 2: While You're Here

**H2:**
> While you're waiting — meet the studio.

**Embed:** Instagram feed widget showing @sunrisewellnessstudio's last 6 posts.

---

### Section 3: Soft Secondary CTA

**Centered, gold panel:**

> **Follow us so you don't miss class drops.**
> 
> [Instagram icon] [Facebook icon] [Google Maps icon]

---

### Section 4: What Happens Next

**H2:**
> What happens next?

**Numbered list:**

1. **In the next 5 minutes** — You'll get a email with a link to book your first class or PT session.
2. **Day 1** — Show up. Front desk will greet you and give you the studio tour.
3. **Day 7** — Your trainer follows up to see how it went and answer any questions.

---

### Footer (same as Page 1)

---

## A/B Test Variants (optional, for later)

Once the funnel is live and producing data, consider testing these variants. **Do not launch with more than one variant active.**

### Hero H1 variants

| Variant | H1 |
|---|---|
| Aspirational (default) | Rise stronger. Move better. Glow brighter. |
| Direct | Try every class, free, for 7 days. |
| Outcome | The studio Springfield's been talking about — free for a week. |

### Primary CTA button variants

| Variant | Button label |
|---|---|
| Possessive (default) | Claim My Free 7-Day Pass → |
| Action-led | Start My Free Week → |
| Soft | See if Sunrise Is for Me → |

---

## Mobile-First Notes

- 70%+ of traffic will be mobile. Optimize the form page for one-thumb completion.
- CTA buttons must be at least 56px tall on mobile.
- Hero image: ensure subject's face is visible above the fold even on small phones (use object-position: top).
- Form: email field with email keyboard, dropdowns native (not custom-styled).
- Page load target: <2 seconds on 4G.
