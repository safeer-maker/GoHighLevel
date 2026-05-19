# Shared Foundation — Products & Pricing

> Every product the studio sells, configured in GHL Payments. These power checkout funnels, recurring subscriptions, invoices, and the upsell triggers in #06. Build once; referenced everywhere.

---

## Build Path

Navigate to **Payments > Products > + Create Product** in your GHL sub-account.

For each product below, configure:
- **Product Name** (exactly as shown)
- **Description** (the customer-facing blurb)
- **Type** (Recurring or One-Time)
- **Price** and currency
- **Image** (use brand photography — sunrise/coral aesthetic)
- **SKU** (for internal reporting)
- **Tax** if applicable

---

## Membership Products (Recurring Subscriptions)

### Basic Membership — $79/month

| Setting | Value |
|---|---|
| Product Name | Basic Membership |
| SKU | MEM-BASIC |
| Type | Recurring |
| Billing Cycle | Monthly |
| Price | $79.00 |
| Enrollment Fee | $49 (one-time, can be waived via coupon) |
| Description | Unlimited group classes — HIIT, Yoga, Pilates, Strength, Recovery. Open gym access. Cancel anytime. |

**What's included (for copy):**
- Unlimited group fitness classes
- Open gym + functional training floor access
- App access for booking and check-in
- Member community events (monthly)

---

### Premium Membership — $149/month

| Setting | Value |
|---|---|
| Product Name | Premium Membership |
| SKU | MEM-PREMIUM |
| Type | Recurring |
| Billing Cycle | Monthly |
| Price | $149.00 |
| Enrollment Fee | $49 (waivable) |
| Description | Everything in Basic + 2 personal training sessions per month + a nutrition starter consult. Built for members serious about results. |

**What's included:**
- Everything in Basic
- 2 personal training sessions / month (1 hour each)
- One nutrition starter consult on signup
- Priority class booking (book 72hr ahead instead of 48hr)
- 10% off all retail and add-on services

---

### VIP Membership — $249/month

| Setting | Value |
|---|---|
| Product Name | VIP Membership |
| SKU | MEM-VIP |
| Type | Recurring |
| Billing Cycle | Monthly |
| Price | $249.00 |
| Enrollment Fee | $0 (waived for VIP) |
| Description | Unlimited PT, unlimited classes, monthly nutrition coaching, full recovery suite access. The flagship tier. |

**What's included:**
- Everything in Premium
- Unlimited 1-on-1 personal training
- Monthly 1-hour nutrition coaching session
- Recovery suite access (sauna, cold plunge, massage gun)
- Quarterly InBody composition scan
- Guest pass: bring a friend, free, twice a month
- 20% off retail and all add-on services

---

## Personal Training (One-Time)

### Single PT Session — $85

| Setting | Value |
|---|---|
| Product Name | Personal Training — Single Session |
| SKU | PT-SINGLE |
| Type | One-Time |
| Price | $85.00 |
| Description | One 60-minute personal training session with a Sunrise certified trainer. Drop-in option for non-members or extra session for Basic members. |

---

### PT Package — 5 Sessions — $375

| Setting | Value |
|---|---|
| Product Name | PT 5-Pack |
| SKU | PT-PACK-5 |
| Type | One-Time |
| Price | $375.00 |
| Description | 5 personal training sessions. Save $50 vs single sessions. Use within 90 days. |

---

### PT Package — 10 Sessions — $700

| Setting | Value |
|---|---|
| Product Name | PT 10-Pack |
| SKU | PT-PACK-10 |
| Type | One-Time |
| Price | $700.00 |
| Description | 10 personal training sessions. Save $150 vs single sessions. Use within 180 days. |

---

## Nutrition (One-Time)

### Nutrition Starter Consult — $50

| Setting | Value |
|---|---|
| Product Name | Nutrition Starter Consult |
| SKU | NUT-STARTER |
| Type | One-Time |
| Price | $50.00 |
| Description | 45-minute one-on-one nutrition consult. Goal-setting, baseline assessment, food log review. Included free in Premium and VIP. |

---

### 4-Week Custom Nutrition Plan — $199

| Setting | Value |
|---|---|
| Product Name | 4-Week Custom Nutrition Plan |
| SKU | NUT-PLAN-4WK |
| Type | One-Time |
| Price | $199.00 |
| Description | Personalized 4-week meal plan, weekly check-ins, and two consults with our nutritionist. Tailored to your goals and dietary preferences. |

---

## Promotional / Lead-Magnet Products (Free or Low-Cost)

### Free 7-Day Trial Pass — $0

| Setting | Value |
|---|---|
| Product Name | Free 7-Day All-Access Pass |
| SKU | TRIAL-7DAY |
| Type | One-Time |
| Price | $0.00 |
| Description | 7 days of unlimited group classes and open gym access. No credit card required. Includes a complimentary intro consult on day 1. |

> Even though it's free, build it as a product so trial claims flow through the same checkout system → easier reporting, easier conversion tracking, easier coupon mechanics for upgrades.

---

### Trial Conversion Offer — $79 (first month) + $0 enrollment

This is the *same* Basic Membership product, sold with a coupon applied. Build a coupon:

| Coupon | TRIAL2PAID |
|---|---|
| Discount | 20% off first month + waive $49 enrollment |
| Valid for | 14 days after trial start |
| Single use per contact | Yes |
| Stackable | No |

---

## Win-Back Products / Coupons

### Win-Back D30 Coupon — WB30

| Setting | Value |
|---|---|
| Coupon Code | WB30 |
| Discount | 50% off first month back |
| Applies to | Basic, Premium, VIP |
| Valid for | 14 days from issue |

### Win-Back D60 Coupon — WB60

| Setting | Value |
|---|---|
| Coupon Code | WB60 |
| Discount | First month $39 + waived enrollment |
| Applies to | Basic only (encourages re-entry, upgrade later) |
| Valid for | 21 days from issue |

### Win-Back D90 Coupon — WB90LAST

| Setting | Value |
|---|---|
| Coupon Code | WB90LAST |
| Discount | First month $29 + waived enrollment |
| Applies to | Basic only |
| Valid for | 7 days from issue (urgency) |

---

## Referral Coupons (used by #08)

### Referee First-Month Discount — REF20

| Setting | Value |
|---|---|
| Coupon Code | REF20 (or referrer-specific, e.g., REF-SARAH-42) |
| Discount | $20 off first month |
| Applies to | Basic, Premium, VIP |
| Valid for | 30 days from issue |

### Referrer Reward — issued as a free PT session credit (not a product purchase — a workflow grants a `PT-SINGLE` redemption)

---

## Seasonal / Campaign Products

### Spring Reset Challenge — $99

| Setting | Value |
|---|---|
| Product Name | Spring Reset 30-Day Challenge |
| SKU | CAMP-SPRING |
| Type | One-Time |
| Price | $99.00 |
| Description | 30-day full studio access + meal plan + 2 PT sessions + nutritionist check-ins. Limited spots. |

(Recreate this product each season — Summer Strong, Fall Forward, etc.)

---

## Product Summary Table

| Category | Product | Price | Recurring? |
|---|---|---|---|
| Membership | Basic | $79/mo | ✅ |
| Membership | Premium | $149/mo | ✅ |
| Membership | VIP | $249/mo | ✅ |
| PT | Single Session | $85 | — |
| PT | 5-Pack | $375 | — |
| PT | 10-Pack | $700 | — |
| Nutrition | Starter Consult | $50 | — |
| Nutrition | 4-Week Plan | $199 | — |
| Lead Magnet | Free 7-Day Trial | $0 | — |
| Seasonal | Spring Reset | $99 | — |

Plus 6 coupons (TRIAL2PAID, WB30, WB60, WB90LAST, REF20, plus referrer-specific generated codes).

---

## Reporting Categories

Set GHL product categories so the #10 reporting dashboard can break down revenue cleanly:

| Category | Products |
|---|---|
| Memberships | Basic, Premium, VIP |
| Personal Training | Single, 5-Pack, 10-Pack |
| Nutrition | Starter Consult, 4-Week Plan |
| Trials / Lead Magnets | Free 7-Day Trial |
| Campaigns | Spring Reset, future seasonals |

---

## Build Verification

After creating all products:

1. Go to **Payments > Products** — confirm all 10 products show with correct prices and recurring flags.
2. Go to **Payments > Coupons** — confirm all 5 base coupons exist with correct discount logic.
3. Create a test checkout link for **Basic Membership** with `TRIAL2PAID` coupon applied — verify total is correct.
4. Run a test transaction with a Stripe test card to verify the product flows into the contact's payment history.

---

---

## Extensions Added by Specific Problem Builds

### From #05 Retention & Churn Prevention

| Coupon | Value |
|---|---|
| `RETAIN-PT` | Free PT-SINGLE redemption — used by at-risk save offer; 14-day validity |

### From #06 Upsell & Cross-Sell

| Coupon | Value |
|---|---|
| `UPGRADE10` | 10% off first month at upgrade (e.g., Basic → Premium); 30-day validity, single use per contact |

---

## Related Foundation

- **[custom-values.md](custom-values.md)** — display copy mirrors these prices (`{{custom_values.price.basic}}`).
- **[custom-fields.md](custom-fields.md)** — `membership_tier` and `monthly_rate` fields are populated based on which product is purchased.
- **[pipelines.md](pipelines.md)** — Membership Sales pipeline closes "Won" on successful product purchase.
