# Build Order — From Empty Sub-Account to Running Engine

> The recommended sequence to build the full Sunrise Wellness Studio system. Total estimated time: **15–20 hours** for a solo operator, or 1 full day for a small team working in parallel after the foundation is complete.

---

## Why Order Matters

Many of the workflows reference fields, tags, pipelines, products, and outputs of *other* workflows. Building out of order means:

- Workflows reference fields that don't exist → trigger errors at save time
- Workflows depend on tags that haven't been added to the taxonomy → cleanups required later
- Engagement-score-driven systems (#06, #07, #08) trigger on empty data if `#05` isn't running yet
- Testing one system without its upstream feed means manually faking state — slower, error-prone

Build in the order below.

---

## Phase 0 — Sub-Account Prep (1 hour)

Before any of this build. Verify or complete:

| Step | What | Where |
|---|---|---|
| 0.1 | Sub-account created and provisioned in your GHL agency account | Agency dashboard |
| 0.2 | Business Profile set (name, address, timezone, phone, logo) | **Settings > Business Profile** |
| 0.3 | At least one GHL phone number provisioned for Email | **Settings > Phone Numbers** |
| 0.4 | Sending domain set up with SPF/DKIM/DMARC for email deliverability | **Settings > Email Services** |
| 0.5 | Stripe (or other payment processor) connected | **Payments > Integrations** |
| 0.6 | Google Business Profile connected for review integration | **Reputation > Integrations** |
| 0.7 | Meta + Google Ads pixels installed sitewide | **Sites > Tracking Codes** |

**Verification:** Send a test Email to your own number from Conversations. Send a test email to a real inbox. Both should arrive within seconds.

---

## Phase 1 — Shared Foundation (3–4 hours)

Everything in [`shared-foundation/`](../shared-foundation/). Build all five before touching any problem folder.

| Order | File | Time | Notes |
|---|---|---|---|
| 1.1 | [custom-values.md](../shared-foundation/custom-values.md) | 30 min | 60 values across 8 groups. Faster than fields — mostly typing. |
| 1.2 | [custom-fields.md](../shared-foundation/custom-fields.md) | 60 min | 48+ fields across 5 folders. Build folders first, then fields per folder. |
| 1.3 | [tags.md](../shared-foundation/tags.md) | 30 min | Apply naming convention strictly — typos here cause silent workflow failures later. |
| 1.4 | [pipelines.md](../shared-foundation/pipelines.md) | 45 min | Three pipelines (Membership Sales, Onboarding, Retention) with all stages. |
| 1.5 | [products-and-pricing.md](../shared-foundation/products-and-pricing.md) | 45 min | 10 products + 5 base coupons. Test checkout flow with a Stripe test card. |

**Verification — do NOT skip:**

1. Create a test contact and apply 4 mixed tags (`member-active`, `tier-premium`, `risk-healthy`, `interest-pt`). Confirm contact filter views work.
2. Move that contact through all three pipelines manually. Confirm every stage exists.
3. Process a test checkout for Basic Membership with the `TRIAL2PAID` coupon applied. Confirm price, tags, and subscription created.
4. Type `{{` in a Conversations test message — confirm autocomplete shows all 60 custom values.

If any verification fails, fix the foundation before proceeding. Every problem assumes this is correct.

---

## Phase 2 — Calendar Setup (1 hour)

Calendars are not in shared-foundation (they're not data — they're appointment infrastructure), but every problem from `#03` onward needs them.

| Calendar Name | Type | Capacity | Duration | Used by |
|---|---|---|---|---|
| `Intro Consult — Free` | One-on-One | 1 | 30 min | #01, #02 (trial sign-ups) |
| `Personal Training — 60min` | Round Robin | 1 per trainer | 60 min | #02, #04, #06 |
| `Nutrition Starter Consult` | One-on-One (Sam) | 1 | 45 min | #04, #06 |
| `Goal Review` | One-on-One (Morgan/Alex) | 1 | 30 min | #04 (day-21 review) |
| `Group Class — HIIT` | Class Booking | 20 | 60 min | #04, #05 (attendance feed) |
| `Group Class — Yoga` | Class Booking | 25 | 60 min | Same |
| `Group Class — Pilates` | Class Booking | 12 | 60 min | Same |
| `Group Class — Strength` | Class Booking | 16 | 60 min | Same |
| `Group Class — Recovery` | Class Booking | 15 | 45 min | Same |

Each calendar's confirmation, reschedule, and cancellation behaviors are tuned in `#03` (no-show recovery system).

---

## Phase 3 — Critical Path Problems (8–12 hours)

Build in this order. Each problem can be built and verified before starting the next.

### 3.1 — [#01 Lead Capture & Instant Response](../problems/01-lead-capture-and-instant-response/) (90 min)

Why first: nothing downstream works without leads in the system. Easy to verify (you can submit a form yourself).

### 3.2 — [#03 No-Show Recovery](../problems/03-appointment-no-show-recovery/) (90 min)

Why second: every system from `#02` onward involves booked appointments. Building this early means every test of every other system is appointment-safe.

### 3.3 — [#02 Trial-to-Paid Conversion](../problems/02-trial-to-paid-conversion/) (2 hours)

Why third: receives directly from `#01`. Build/test as a continuous pipeline (submit form, book trial, run nurture).

### 3.4 — [#04 New Member Onboarding](../problems/04-new-member-onboarding/) (2 hours)

Why fourth: receives directly from `#02`. After this is built, the **acquisition pipeline is complete** end-to-end. You can demo this slice to a client even if #05–#10 aren't built yet.

### 3.5 — [#05 Retention & Churn Prevention](../problems/05-retention-and-churn-prevention/) (2.5 hours — the most complex)

Why fifth: the keystone system. Computes `engagement_score` and `at_risk_flag` that `#06`, `#07`, `#08` all read. Build before any downstream system to avoid empty-data triggers.

**Critical sub-step:** Run the nightly engagement scoring workflow manually once after building, on a sample of test contacts, to confirm the score math is correct. Spot-check 5–10 contacts.

### 3.6 — [#10 Owner Reporting & Visibility](../problems/10-owner-reporting-and-visibility/) (90 min)

Why sixth (out of natural order): build this *before* #06, #07, #08 so you can see those systems' impact in the dashboard the moment they fire. Smart Lists and the Weekly Digest read from already-existing tags and pipelines — they don't require #06–#09 to exist.

---

## Phase 4 — Engagement Amplifiers (3 hours)

These read from `#05` and amplify member value. Can be built in any order or in parallel.

### 4.1 — [#06 Upsell & Cross-Sell](../problems/06-upsell-and-cross-sell/) (60 min)

### 4.2 — [#07 Reviews & Reputation](../problems/07-reviews-and-reputation/) (60 min)

### 4.3 — [#08 Referral Engine](../problems/08-referral-engine/) (60 min)

After 4.3, run a quick cross-system test: take a test contact, manually set their engagement_score to 90 and `tier-basic` tag, attend a class (simulate via "showed" status on a test appointment), and watch all three systems fire their triggers within hours. All three should respect `do-not-*` opt-outs and not collide.

---

## Phase 5 — Win-Back & Recovery (90 min)

### 5.1 — [#09 Win-Back Lapsed Members](../problems/09-win-back-lapsed-members/) (90 min)

Last because it requires a `member-cancelled` event to test. Manually cancel a test member's subscription in Stripe → confirm `#05` tags `member-cancelled` → confirm `#09` workflow enrolls them → fast-forward time (or use a shortened test variant of the workflow) to verify all four touch points.

---

## Phase 6 — Integration Testing (2 hours)

After all 10 systems are live. Run the end-to-end scenario in [end-to-end-scenario.md](end-to-end-scenario.md) with a fresh test contact. Trace them from lead → trial → paid → onboarded → engaged → upsold → reviewer → referrer → cancelled → reactivated. **Every transition should fire automatically.** If any transition requires manual intervention, that's a bug in the wiring — investigate before declaring done.

---

## Time Budget Summary

| Phase | Duration |
|---|---|
| Phase 0 — Prep | 1 hr |
| Phase 1 — Foundation | 3–4 hr |
| Phase 2 — Calendars | 1 hr |
| Phase 3 — Critical Path (6 problems) | 8–12 hr |
| Phase 4 — Amplifiers (3 problems) | 3 hr |
| Phase 5 — Win-Back | 1.5 hr |
| Phase 6 — Integration Test | 2 hr |
| **Total** | **19.5–24.5 hr** |

**Solo operator:** 2.5–3 working days.

**Two-person team:** After Phase 0+1 (one person, can't parallelize foundation), split Phase 3+ so person A builds odd-numbered problems and person B builds even-numbered. Phase 6 integration test always together. Total wall time: 1.5 days.

---

## Parallelization Opportunities (for teams)

Once Phase 1+2 are done by one person:

- **Person A:** #01, #03, #05, #07, #09
- **Person B:** #02, #04, #06, #08, #10

Hand off at #05 — Person B's downstream systems (#06, #08) need #05 done first. Realistically, Person B starts #02 → #04 → #10 (no #05 dep) and waits for Person A to finish #05 before starting #06 and #08.

---

## After Build — Operational Setup

Once everything is live:

1. **Owner training (30 min)** — walk the owner through the three pipelines, the dashboard, the Monday digest email, and how to read the at-risk alerts.
2. **Front-desk training (30 min)** — Conversations inbox triage, how to handle replies to lead-capture Email, how to escalate vs auto-respond.
3. **Existing-member import (1 hour)** — import current member list with correct tier/start-date tags, slot into Retention pipeline at appropriate stages.
4. **Ad pixel verification (15 min)** — submit a test lead from a Meta-tagged URL, confirm conversion event fires in Meta Events Manager.
5. **First weekly digest sanity check (Monday after launch)** — review the first auto-sent digest. Numbers should match what owner expects intuitively. If wildly off, debug smart-list filters.

---

## Maintenance Cadence (after launch)

| Cadence | What |
|---|---|
| **Daily (owner, 5 min)** | Glance dashboard, action At-Risk members |
| **Weekly (owner, 15 min)** | Read Monday digest, action stuck pipeline items |
| **Monthly (operator, 1 hour)** | Refresh seasonal offer custom values, rotate testimonials in funnels, check workflow execution history for errors |
| **Quarterly (operator, 2 hours)** | Review smart-list filters as taxonomy grows, refresh email templates, run end-to-end scenario test, audit cancel reasons |
| **Annually (operator + owner, half day)** | Review all KPIs vs targets, retire low-performing campaigns, add new seasonal challenges |

---

## Common Build Mistakes (across all 10 problems)

1. **Building workflows before tags exist.** GHL accepts the action, then silently fails to apply non-existent tags. Always build the tag taxonomy in Phase 1.5 first.
2. **Forgetting opt-out checks.** Every Email-sending action must check `do-not-email` tag and `sms_opt_in` field. Build a workflow snippet/template you reuse.
3. **Inconsistent state.** Workflow updates the pipeline stage but forgets to update the parallel tag (or vice versa). Always pair stage moves with tag updates in the same action sequence.
4. **No quiet-hours respect on marketing.** Transactional messages (lead capture instant response, payment failure) ignore quiet hours; marketing messages (upsell offers, reviews, referrals) respect 8 AM – 9 PM contact-local time.
5. **Testing in production.** Build a "Test" contact tag and exclude it from every marketing workflow. Use it for QA without polluting metrics or risking sending test messages to real members.

---

## Related Files

- **[master-automation-graph.md](master-automation-graph.md)** — how all 10 systems connect.
- **[end-to-end-scenario.md](end-to-end-scenario.md)** — narrative trace of a single lead.
- **[../README.md](../README.md)** — folder entry point.
