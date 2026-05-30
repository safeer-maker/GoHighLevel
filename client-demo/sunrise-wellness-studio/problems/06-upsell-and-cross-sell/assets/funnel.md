# #06 — Funnel Copy: Premium Upgrade Checkout (+ VIP variant)

> Production-ready copy for the Premium upgrade checkout funnel. The page is personalized via URL parameters (`?contact_id={{contact.id}}`) so the headline addresses the member by name and references their actual attendance. A separate VIP upgrade funnel uses the same structure with VIP-specific copy.

---

## Funnel Settings

- **Funnel name:** `Sunrise — Premium Upgrade Checkout`
- **Domain:** book.sunrisewellness.com/premium (or sub-path)
- **Brand colors:** Sunrise Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Primary CTA color:** Sunrise Coral
- **Personalization:** Reads `contact_id` URL parameter, server-renders member name, current `monthly_rate`, `visits_last_30_days`, `tier-basic` confirmation

---

## PAGE 1 — Why Premium (one-pager: landing + checkout combined)

### Section 1: Personalized Hero (above-the-fold)

**Background:** Light cream `#FFF8F0` with a subtle sunrise gradient strip at the top. Optional: small studio photo on the right (desktop) — mobile shows headline only.

**Eyebrow (small, gold):**
> A PERSONAL LOOK AT YOUR PREMIUM UPGRADE

**H1 (large, deep slate, bold):**
> {{contact.first_name}}, you attended **{{contact.visits_last_30_days}} classes** last month.
> Premium fits you.

**Subheadline (medium):**
> You're already using the studio like a Premium member. Here's what changes if your membership matches — including the actual math.

**Primary CTA button (coral, large):**
> **See What I'd Save →**

(Scrolls to the Savings Calculator section below.)

**Below button — small trust line:**
> No long-term contract · Pro-rated billing · Downgrade anytime · Real humans answer questions

---

### Section 2: The Savings Calculator (interactive widget)

**H2 (centered, deep slate):**
> Let's do the math on *your* membership

**Body intro:**
> Two questions. Takes 15 seconds. Shows you exactly what you'd spend on Basic + add-ons vs. Premium.

---

**Widget structure (interactive, JavaScript-driven on GHL funnel page):**

**Question 1 (slider or button group):**

> **How many PT sessions do you typically do per month?**

| Option | Stored value |
|---|---|
| 0 — never tried PT | 0 |
| 1 PT session/month | 1 |
| 2 PT sessions/month | 2 |
| 3 PT sessions/month | 3 |
| 4 or more PT sessions/month | 4 |

**Question 2 (radio buttons):**

> **Do you ever buy nutrition consults?**

| Option | Stored value |
|---|---|
| No — never thought about it | 0 |
| Maybe once or twice a year | 1 |
| Yes — at least every couple months | 4 |
| Often — it's part of my routine | 12 |

**Live calculation (displayed below questions, updates as user clicks):**

```
Your current spending on Basic + add-ons:
  Basic membership:           $79/mo
  + PT sessions (X × $85):    $XXX/mo
  + Nutrition consults (avg): $XX/mo
                              -------
  Estimated total:            $XXX/mo

Premium membership (covers all this):
  Premium:                    $149/mo

You'd save: $XX/mo
            $XXX/year
```

**Edge case (when user selects "0 PT, 0 nutrition"):**

The calculator shows:

> Your current spending is **$79/mo** on Basic.
> Premium is **$149/mo** — that's $70 more.
>
> You wouldn't *save money today* on Premium. But here's what changes:
> - You'd get **2 PT sessions/month included** (worth $170 retail)
> - You'd get a **nutrition starter consult on signup** (worth $50)
> - And if you ever start using either, Premium pays for itself.
>
> Premium isn't always about saving — sometimes it's about unlocking what's next.

**Below the calculator, transition CTA:**

> **Yes, let's do Premium →**

(Scrolls to the Comparison + Checkout section below.)

---

### Section 3: Premium vs Basic — Side-by-Side

**H2 (centered):**
> What changes when you upgrade

**Comparison table (mobile: stacks; desktop: side-by-side):**

| What you get | Basic ($79/mo) | **Premium ($149/mo)** |
|---|---|---|
| Unlimited group classes | ✓ | ✓ |
| Open gym access | ✓ | ✓ |
| App booking | ✓ | ✓ |
| Member community events | ✓ | ✓ |
| **Personal training (2/mo)** | Not included | **✓ Included** |
| **Nutrition starter consult** | $50 separate | **Included on signup** |
| **Priority class booking** | 48hr | **72hr ahead** |
| **Retail / add-on discount** | None | **10% off everything** |
| **Bring-a-friend day pass** | $25 each | **2 free/month** |
| Monthly investment | $79 | $149 |

---

### Section 4: Testimonials

**H2 (centered):**
> Members who made the switch

**2 testimonial cards (carousel on mobile):**

**Testimonial 1:**

> "I bumped to Premium six months in because I kept buying PT sessions à la carte and the math made it obvious. The bonus is that having PT 'built in' actually made me use it consistently — and that's when the progress started compounding."
>
> — **Priya M., Premium since 2024**

**Testimonial 2:**

> "Honestly the nutrition consult was the kicker. I'd been working out for a year and not seeing the changes I wanted. One conversation with Sam, two food tweaks, and three months later I was somewhere new. Premium paid for itself in the first month I had it."
>
> — **Marcus T., Premium since 2023**

---

### Section 5: The Checkout Block

**H2 (centered, deep slate):**
> Ready? Let's get you on Premium.

**Body:**
> Your tier will update immediately. We'll **pro-rate this month's billing** so you don't pay twice for overlapping days, and your renewal date stays the same.

---

**Checkout form (GHL native Stripe block):**

| Field | Pre-filled | Notes |
|---|---|---|
| Name | {{contact.first_name}} {{contact.last_name}} | Pre-filled from contact record |
| Email | {{contact.email}} | Pre-filled |
| Phone | {{contact.phone}} | Pre-filled |
| Payment method | (existing card on file if Stripe vaulted) | Otherwise new card form |
| Coupon code | `UPGRADE10` (auto-applied) | 10% off first month |
| **Order summary** | Premium Membership — $149/mo (today: $134.10 after 10% off) | Pro-ration calculated server-side |

**Submit button:**

> **Upgrade to Premium for $134.10 today →**

**Below button (small):**
> You'll be charged $149/mo starting next billing cycle ({{next_billing_date}}). Cancel or downgrade anytime in your account settings.

---

### Section 6: Reassurance / FAQ

**H2 (small):**
> Quick answers before you commit

**Accordion (3 items, expandable):**

**Q1: Can I downgrade back to Basic if Premium isn't for me?**
> Yes — anytime, no penalty. Downgrades are pro-rated and take effect at the next billing cycle. Just text Morgan or use your account settings.

**Q2: How do PT sessions work — do I lose them if I don't use them?**
> Your 2 PT sessions/month roll over for one billing cycle. If you don't use them in the current month, they're available the next month. After that, they expire (otherwise we'd never know how to staff trainers).

**Q3: What if I'm not sure I'll use the nutrition consult?**
> The nutrition consult is included free on Premium signup — you get one within the first 30 days. If you don't book it, no charge, no harm. Many members book it just to meet Sam and end up loving it.

---

### Section 7: Footer

- Studio: {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Small links: Privacy · Terms · Contact
- Icons: Instagram, Facebook, Google Maps

---

## PAGE 2 — Welcome to Premium (Thank-You)

### Section 1: Confirmation

**Background:** Sunrise gradient (coral → gold → cream).

**Large checkmark icon (gold)**

**H1:**
> Welcome to Premium, {{contact.first_name}} ☀️

**Subhead:**
> Your tier is active starting now. Your first PT session and nutrition consult are unlocked.

---

### Section 2: What to Do This Week (3-card layout)

**H2:**
> 3 things to set up this week

**Card 1:**
> ☀️ **Book your first PT session**
>
> Pick a trainer, pick a time. 60 minutes, completely included.
>
> [**Book PT →**] (button — links to PT calendar)

**Card 2:**
> 🌱 **Book your nutrition starter consult**
>
> 45 minutes with Sam. Talk goals, get 2–3 specific food changes that move the needle.
>
> [**Book Nutrition →**] (button — links to nutrition calendar)

**Card 3:**
> 💪 **Try one new class style this week**
>
> Premium opens up priority booking. If you've been HIIT-only, try a Pilates Reformer or Strength Lab. You've got the access — use it.
>
> [**Browse Classes →**] (button — links to schedule)

---

### Section 3: Soft Footer

**Centered, cream panel:**

> **Questions? Text Morgan at {{custom_values.business.sms_number}} or reply to your welcome Email.**
>
> Your Premium benefits never expire as long as your membership is active. Welcome to the next chapter. 🎉

---

### Footer (same as Page 1)

---

## VIP Upgrade Funnel — Variant

The VIP funnel mirrors this structure with these changes:

### Hero H1

> {{contact.first_name}}, you booked **{{contact.placeholder.pt_count_30d}} PT sessions** last month.
> VIP would have saved you money.

### Savings Calculator

Adjusts the math:

```
Your current spending (Premium + PT extras):
  Premium membership:         $149/mo
  + Extra PT (X × $85):       $XXX/mo
                              -------
  Estimated total:            $XXX/mo

VIP membership (unlimited PT included):
  VIP:                        $249/mo

You'd save: $XX/mo
            $XXX/year
```

### Comparison table — Premium vs VIP

| What you get | Premium ($149/mo) | **VIP ($249/mo)** |
|---|---|---|
| Unlimited group classes | ✓ | ✓ |
| **PT sessions/month** | 2 included | **Unlimited** |
| **Nutrition coaching** | Starter consult only | **Monthly 1hr session** |
| **Recovery suite access** | $20/visit | **Unlimited included** |
| **Quarterly InBody scan** | $75 each | **Included** |
| **Bring-a-friend pass** | 2/mo | **2/mo** |
| **Retail / add-on discount** | 10% | **20%** |
| **Enrollment fee** | $49 (waived for upgrades) | **$0** |
| Monthly investment | $149 | $249 |

### Testimonials — VIP-specific

> "I went VIP for the unlimited PT and the recovery suite, but the surprise was the monthly nutrition coaching — that became the most valuable hour of my month."
>
> — **Diane K., VIP since 2024**

> "I do strength training 4x a week. The InBody scans every quarter let me see what's actually happening with composition, not just the scale. I'd pay $249 for that one feature alone — everything else is bonus."
>
> — **Raj P., VIP since 2023**

### Checkout

| Field | Value |
|---|---|
| Product | VIP Membership |
| Price | $249/mo |
| Enrollment fee | $0 (always waived for VIP upgrades) |
| Coupon | none auto-applied (VIP-bound members are conversion-ready; coupons cheapen the tier) |

### Thank-You page additions

Card 4: **Book your first InBody scan** (link to InBody calendar)
Card 5: **Tour the recovery suite** (text "Tour" to {{custom_values.business.sms_number}} and front desk schedules you)

---

## Mobile-First Notes

- The savings calculator must work flawlessly on mobile — half the upsell traffic is from members tapping the email CTA on their phone.
- Comparison tables stack to single-column rows on mobile, with the Premium/VIP column highlighted.
- Checkout block uses GHL's native Stripe payment element which is mobile-optimized.
- Hero H1 uses readable font size (32–40px on mobile, 48–64px on desktop).
- All CTA buttons minimum 56px tall, thumb-friendly.

---

## A/B Test Variants (after launch)

| Test | Variant A (control) | Variant B |
|---|---|---|
| Hero | "You attended X classes" | "Members like you save $X/year on Premium" |
| Calculator | Live JS widget | Static side-by-side table only |
| Coupon | UPGRADE10 (10% off first month) | No coupon (test whether the offer needs sweetening) |
| Thank-you CTAs | 3 booking cards | 1 hero CTA (Book PT now) only |

Run each test 30 days minimum, 50+ conversions per variant.

---

## What Comes Next

After successful checkout:

- Tag `tier-premium` (or `tier-vip`) added, `tier-basic` removed.
- `monthly_rate` field updated.
- Workflow `06 — Behavior-Triggered Upsell` detects the conversion via the tag → fires the celebration Email + owner notification.
- Member is enrolled in **Premium Member Onboarding** (or **VIP Member Onboarding**) mini-flow — a 7-day "make the most of your tier" sequence (out of scope for this file).
- 30 days later, member receives `referral-prompt-ready` tag — surfaces to [#08 Referral Engine](../../08-referral-engine/) as a high-promoter.
