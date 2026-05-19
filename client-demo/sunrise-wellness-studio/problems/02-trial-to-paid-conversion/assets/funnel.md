# #02 — Funnel Copy: Trial Conversion Offer

> Production-ready copy for the one-page conversion offer funnel. Paste directly into the GHL funnel builder. All `{{custom_values.*}}` and `{{contact.*}}` merge fields resolve at render time.

---

## Funnel Settings

- **Funnel name:** `Sunrise — Trial Conversion Offer`
- **Domain:** `book.sunrisewellness.com/join` (sub-path)
- **Brand colors:** Sunrise Coral `#FF6B4A`, Gold `#F4B860`, Cream `#FFF8F0`, Deep Slate `#2D3142`
- **Custom value to set after publish:** `offer.conversion_funnel_url` = the published URL
- **Pre-fill behavior:** When opened via the trial nurture emails/SMS, URL includes `?contact_id={{contact.id}}` so name, email, phone auto-fill on the checkout step.

---

## PAGE 1 — Offer / Sales Page

### Section 1: Hero (above-the-fold)

**Background:** Wide photo of the studio mid-class, warm coral/gold tones. Light overlay for text contrast.

**Eyebrow text (small, gold, all caps):**
> TRIAL CONVERSION OFFER — 48 HOURS ONLY

**H1 (huge, white, bold):**
> Loved your trial? Lock in the studio rate.

**Subheadline (medium, white):**
> {{custom_values.offer.trial_conversion_discount}}. Available for 48 hours after your trial ends.

**Primary CTA button (coral, large):**
> **Lock In My Membership →**

(Scrolls to checkout section below, OR navigates to `02 — Checkout` page.)

**Below button — small reassurance:**
> No long-term contract · Cancel anytime · Pause for vacations

---

### Section 2: Choose Your Tier (the offer math)

**Eyebrow:**
> WHAT YOU'LL PAY

**H2 (centered, deep slate):**
> Three tiers. Your TRIAL2PAID code applies to all of them.

**3-column comparison table (stacks on mobile):**

| | **Basic** | **Premium** | **VIP** |
|---|---|---|---|
| **Regular price** | {{custom_values.price.basic}} | {{custom_values.price.premium}} | {{custom_values.price.vip}} |
| **Your first month** | **$63.20** | **$119.20** | **$199.20** |
| **Enrollment fee** | ~~$49~~ Waived | ~~$49~~ Waived | $0 (always) |
| Unlimited group classes | ✅ | ✅ | ✅ |
| Open gym + functional floor | ✅ | ✅ | ✅ |
| Personal training | Add-on $85/session | **2 sessions/month included** | **Unlimited included** |
| Nutrition coaching | Add-on $50 starter | **Starter consult included** | **Monthly session included** |
| Recovery suite (sauna, cold plunge) | — | — | **Unlimited** |
| Guest passes | — | — | **2/month** |
| **Best for** | Class-focused regulars | Members who want PT in their routine | All-in on results |
| | **[Pick Basic →]** | **[Pick Premium →]** | **[Pick VIP →]** |

(Each button below the tier navigates to the checkout step with the right product pre-selected.)

---

### Section 3: What members say about the upgrade decision

**H2:**
> What other members say about picking their tier

**3 testimonial cards (carousel on mobile):**

**Testimonial 1 — Basic:**

> *"I started on Basic because I wasn't sure how often I'd actually come. Showed up 12 times in month one. Three months later I'm still on Basic and it's the perfect fit — I just love the classes. No regrets, no FOMO."*
>
> — **Diane K., Basic member since 2024**

**Testimonial 2 — Premium:**

> *"The PT sessions are the difference. Two a month sounded like nothing — turns out it's exactly the right cadence to actually fix things. I tweaked my form on the deadlift in week two and my whole back is happier."*
>
> — **Marcus T., Premium member since 2023**

**Testimonial 3 — VIP:**

> *"VIP is what got me through marathon training. Unlimited PT + the nutrition coaching + recovery suite = I was treating my body like a professional athlete on a non-athlete budget. Worth every cent."*
>
> — **Aanya R., VIP member since 2024**

---

### Section 4: FAQ

**H2:**
> Common questions before locking in

| Question | Answer |
|---|---|
| **Can I switch tiers later?** | Yes — anytime. Upgrade with a single email, downgrade with one click in the member portal. Pro-rated immediately. |
| **What if I need to pause?** | You can pause your membership up to 60 days per year, no fee. Just email us or use the portal. |
| **Is there a contract?** | No. Month-to-month. Cancel anytime — we'd rather you stay because it's working than out of guilt. |
| **What if the auto-renewal date doesn't work for me?** | We can shift your billing date once after the first month — just ask. |
| **Can I bring a friend?** | After you join, you get a personal referral link. Your friend gets $20 off their first month and you get a free PT session. (More: [#08 Referral](../08-referral-engine/)) |
| **What if I want to bring it to my company for corporate rates?** | Reply to any of our emails or call {{custom_values.business.phone}} — Morgan handles corporate inquiries personally. |
| **What if my card declines?** | We retry once at 24hr, then email you. You have 7 days to update billing before any pause to access. |
| **Coupon code doesn't work?** | The TRIAL2PAID code is single-use per contact and valid 48hr after your trial wraps. If it's expired or used, reply to your last email from Morgan and she'll extend it. |

---

### Section 5: One More Time — Final CTA

**Background:** Coral gradient.

**H2 (white, bold):**
> Lock in your rate. Keep the momentum.

**Subhead (white):**
> {{custom_values.offer.trial_conversion_discount}}. 48 hours from your trial end.

**Primary CTA (large white-on-coral inverse):**
> **Lock In My Membership →**

**Below button:**
> Cancel anytime · No contract · Pause for vacations

---

### Footer

- Studio: `{{custom_values.business.address_line}}` · `{{custom_values.business.phone}}`
- Hours: `{{custom_values.hours.full}}`
- Social icons: Instagram · Facebook · Google
- Small links: Privacy · Terms · Contact
- Footer text: `{{custom_values.legal.footer}}`

---

## PAGE 2 — Checkout

### Section 1: Mini-Hero

**Background:** Soft cream `#FFF8F0`.

**Eyebrow:**
> ALMOST THERE

**H1:**
> Welcome to Sunrise, {{contact.first_name}} ☀️

**Subhead:**
> Your TRIAL2PAID discount is applied below. Cancel anytime, no contract.

---

### Section 2: Checkout Form

**Layout:** Two-column on desktop (left: order summary; right: payment), single-column on mobile.

#### Left column — Order summary

**Heading:**
> Your membership

**Tier toggle (radio buttons):**
- **○ Basic — $63.20 first month, then $79/mo**
  - Unlimited classes + open gym
- **○ Premium — $119.20 first month, then $149/mo** (default)
  - Basic + 2 PT/mo + nutrition consult
- **○ VIP — $199.20 first month, then $249/mo**
  - Unlimited PT + monthly nutrition + recovery suite

**Coupon row:**
> Coupon **TRIAL2PAID** — applied ✓
> *20% off first month + $49 enrollment waived*

**Order bump (small, optional):**
> ☐ **Add a PT 5-Pack — $375** *(save $50 vs single sessions, use within 90 days)*

**Total line (bold):**
> Today: **[calculated]** · Then [tier price] monthly

---

#### Right column — Pre-filled contact details

**Heading:**
> Confirm your info

| Field | Pre-filled value |
|---|---|
| First name | `{{contact.first_name}}` |
| Last name | `{{contact.last_name}}` |
| Email | `{{contact.email}}` |
| Phone | `{{contact.phone}}` |

**Below contact:** Stripe credit-card element (number, expiry, CVC, ZIP).

**Address:** Auto-prompt only if billing requires it; else hidden.

**Final submit button (large coral):**

> **Complete My Membership →**

**Below submit, small text:**
> By submitting you authorize {{custom_values.business.short_name}} to charge your card monthly. Cancel anytime in your member portal or by emailing {{custom_values.business.email}}.

---

### Section 3: Trust strip (below checkout)

**3-icon row:**

| Icon | Text |
|---|---|
| 🔒 | Secure checkout via Stripe |
| ↩️ | Cancel anytime |
| 💬 | Real-human support |

---

## PAGE 3 — Confirmation / Welcome

### Section 1: Confirmation Header

**Background:** Sunrise gradient (coral → gold → white).

**Large gold checkmark icon**

**H1:**
> Welcome to the studio, {{contact.first_name}} ☀️

**Subhead:**
> You're officially a member since today. Here's everything you need.

---

### Section 2: What happens next (numbered)

**H2:**
> Your first 7 days as a member

1. **In the next 5 minutes** — You'll get a welcome text and email with your member portal login and the app link.
2. **Tomorrow morning** — Morgan will send you a personal "welcome to the team" message. Reply with anything.
3. **Within 7 days** — Your onboarding kickoff: book your first as-a-member class and (if Premium/VIP) your first PT session.
4. **Day 14** — Two-week check-in. We make sure you're getting what you came for.
5. **Day 30** — Goal review. Sit down with a trainer (or Morgan) and dial in the next 90 days.

---

### Section 3: One-click action items

**H2:**
> Do these now to save future you time

**3 buttons (coral, stacked on mobile, row on desktop):**

> **[Book My First Class →]**
> Links to `{{custom_values.business.booking_url}}`

> **[Download the Member App →]**
> Links to App Store + Google Play badges

> **[Join the Member Community →]**
> Links to private Facebook group invite

---

### Section 4: Receipt + Account Details

**Plain-styled section:**

> **Membership tier:** [purchased tier]
> **First charge:** $[calculated] on today
> **Recurring:** $[monthly rate] on [renewal date]
> **Receipt:** sent to `{{contact.email}}`
> **Member portal:** [link to portal]
>
> Need to change billing or pause? Use the portal or email `{{custom_values.business.email}}`.

---

### Section 5: A note from Morgan

**Italic, deep slate, gold accent border:**

> *"Welcome in, {{contact.first_name}}. I notice every single new member, and I take it personally that you chose us. Over the next 30 days I (or one of the team) will check in a couple of times to make sure you're getting what you came for. If at any point something isn't working, text me at {{custom_values.business.sms_number}} — I read everything."*
>
> *— Morgan Riley, Owner*

---

### Footer (same as Page 1)

---

## A/B Test Variants (optional, for later)

Once 50+ conversions land, test:

### Hero headline variants

| Variant | H1 |
|---|---|
| Current (default) | Loved your trial? Lock in the studio rate. |
| Outcome | Keep the momentum. Lock in {{custom_values.price.basic}}/mo. |
| Direct offer | 20% off your first month — your trial-converter rate. |

### Tier default

| Variant | Default selected |
|---|---|
| Current (default) | Premium |
| Lower friction | Basic |
| Anchor high | VIP (then lets people downgrade) |

Test one at a time, run for 2 weeks each, target 30+ funnel views per variant.

---

## Mobile-First Notes

- Most trial members will tap the funnel link from a phone after reading a Day 5 email or Day 7 SMS — optimize for one-thumb completion.
- Tier toggle: use big radio buttons (≥ 40px tap target).
- Stripe card element: native iOS/Android keyboard for card number.
- Sticky CTA bar on scroll: "Continue to Checkout →" stays at the bottom of the screen during the comparison table.
- Page load target: < 2 seconds on 4G. The funnel runs on a single image (hero), inline SVGs, no carousels.

---

## Conversion Tracking

Hook the checkout completion to:

| Platform | Event |
|---|---|
| Meta Pixel | `Purchase` event with value = first-month charge |
| Google Ads | `Conversion` event, label `trial_to_paid`, value = first-month charge |
| GHL native analytics | Automatic on Order Submitted |

These feed [#10 Owner Reporting](../10-owner-reporting-and-visibility/) for cost-per-converted-member by source.

---

## What Comes Next

After confirmation, the contact:

1. Gets tagged `trial-converted`, `member-active`, `member-onboarding`, and the corresponding tier tag.
2. Is enrolled in workflow `04 — New Member Onboarding`.
3. Their opportunity in Membership Sales moves to `Won — Paid Member`.
4. A new opportunity is created in the Onboarding pipeline at stage `Welcome Sent (Day 0)`.

See **[../04-new-member-onboarding/build.md](../04-new-member-onboarding/build.md)** for the next 30-day experience.
