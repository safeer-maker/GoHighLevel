# Sunrise Wellness Studio — Business Overview

## The Business

**Sunrise Wellness Studio** is a boutique fitness + wellness studio. Picture a 4,000 sq ft space with three zones: a strength + functional training floor, a 25-mat group fitness studio, and a private nutrition consultation room. The brand is warm and energetic — sunrise-orange and coral, gold accents, language like "rise, move, glow."

The studio is open Mon–Fri 6AM–9PM, Sat 8AM–4PM, Sun 9AM–1PM. The owner-operator runs the front desk most mornings. Three trainers (one Lead, two PT), one nutritionist, and one part-time front desk cover the rest of the schedule.

### What they sell

| Offer | Price | Description |
|---|---|---|
| **Basic Membership** | $79 / month | Unlimited group classes (HIIT, Yoga, Pilates), open gym access |
| **Premium Membership** | $149 / month | Everything in Basic + 2 PT sessions / month + nutrition starter session |
| **VIP Membership** | $249 / month | Unlimited PT, unlimited classes, monthly nutrition coaching, recovery suite access |
| **Single PT Session** | $85 | Drop-in personal training |
| **PT Package — 5 sessions** | $375 | Saves $50 vs single sessions |
| **PT Package — 10 sessions** | $700 | Saves $150 |
| **Nutrition Plan (one-off)** | $199 | Personalized 4-week meal plan + 2 consults |
| **Free 7-Day Trial** | $0 | Full studio access, lead-magnet for new prospects |

### Where revenue comes from

- **70%** recurring memberships (the engine — Basic/Premium/VIP)
- **20%** PT packages and drop-ins
- **8%** Nutrition plans
- **2%** Retail (supplements, apparel — small but contributes margin)

The studio needs **roughly 180 active members** to break even and **240+** to be healthy. That math is what every system in this build serves.

---

## The Seven Customer Personas

Every problem in `problems/` is solved for one or more of these seven personas. The master diagram in [diagrams/problem-map.md](diagrams/problem-map.md) maps each pain to a persona.

### P1 — Cold Lead (the social media scroller)

Found Sunrise through an Instagram ad, a Google search ("yoga near me"), or a friend's post. They are *interested* but not committed. They want to know: does this studio fit me, what does it cost, can I try before I buy. **If we don't engage them in the first 5 minutes, the lead value drops 10x.**

### P2 — Trial Member (the test-driver)

Claimed the free 7-day trial. Walked in once or twice. They are evaluating — comparing Sunrise to the gym down the street, deciding whether $79/mo is worth it. **60–70% of trials never convert without a nurture sequence.** A trial that converts becomes a Basic Member for an average of 14 months — that's $1,100+ in LTV from a single conversion.

### P3 — Booked Lead / Booked Member (the scheduler)

Someone (lead or active member) has a PT session, class spot, or nutrition consult on the calendar. The risk: they no-show. Each no-show on a PT slot costs the studio $40–$120 in trainer time. Each no-show on a capacity-limited class blocks a spot another member could have used.

### P4 — New Member, Day 0–30 (the fragile newbie)

Just signed up. Excited but uncertain. The data is brutal: **the first 30 days predict 90-day retention.** A new member who attends in week 1, week 2, and week 3 is dramatically more likely to still be a member at month 6. We need to *prove value* fast — onboarding call, first class attended, first PT session, first nutrition consult.

### P5 — Active Member, 90+ days (the steady-state)

Made it past the danger zone. Paying every month, mostly happy. But three risks live here: **silent disengagement** (attendance drops, then cancellation), **no upsell** (a Basic who would love Premium but never gets asked), and **unsolicited goodwill** (loves the studio but never leaves a review, never refers a friend). This persona generates the bulk of revenue *and* the bulk of growth opportunities.

### P6 — Lapsed Member (the ghost)

Cancelled. Maybe billing failed, maybe injury, maybe priorities changed. Most studios mark them lost. The truth: **a lapsed member converts at roughly 2x the rate of a cold lead from ads** — and the acquisition cost is zero. We just need to re-engage them at the right moment with the right offer.

### P7 — Studio Owner (the operator)

The person paying for GHL. Needs to know: how many leads came in this week, how many trials are pending conversion, what's the MRR trajectory, which members are at risk, is the marketing ad spend paying off. Without a clean dashboard and a weekly digest, the owner runs on gut feel.

---

## Current Pain Map (Before This Build)

What Sunrise's day looked like before this GHL setup:

- Leads from Meta Ads landed in a Google form. The owner saw them when she remembered to check email — sometimes 2 hours, sometimes 2 days.
- Trial sign-ups got a manual "welcome, here's the schedule" email when the front desk had time.
- No-shows got nothing. The trainer was upset; the member never heard from anyone.
- New members got a tour and a hug, then silence until renewal failed three months later.
- Active members were loved but never asked for a review or a referral.
- Cancellations were filed and forgotten.
- The owner ran the business off a feel and a spreadsheet.

Total estimated revenue left on the table: **$8,000–$15,000 / month** in lost conversions, churned members, missed upsells, and dead pipeline visibility. The systems in this build target every line of that loss.

---

## What "Done" Looks Like

After the full build:

- A lead from any source (web, IG, Google, walk-in) is in GHL within 60 seconds, tagged by source, and getting an Email within 5 minutes.
- Every trial member is in a 7-day nurture sequence that ends with a paid-conversion offer.
- Every appointment sends three reminders and triggers a rebooking sequence if missed.
- Every new member goes through a 30-day onboarding pipeline with check-ins at day 3, 7, 14, and 30.
- Every active member is scored for engagement; drops trigger an at-risk workflow.
- Every Basic member who hits a usage threshold gets a Premium upgrade offer.
- Every happy member is asked for a review at their peak moment.
- Every promoter gets a referral link with a real reward.
- Every cancellation enters a 90-day win-back sequence.
- The owner gets a Monday-morning email with seven numbers that matter.

That's what each of the ten problem folders builds — one piece at a time, then connected.
