# Sunrise Wellness Studio — Complete GoHighLevel Business Build

> A full, client-ready GoHighLevel build for a wellness studio / gym — funnels, emails, SMS, automations, pipelines, calendars, products, and reporting — organized around **10 real business problems**, each with a pitch page and a step-by-step build playbook.

---

## What's Inside

This folder is a complete, self-contained demonstration of a GoHighLevel business setup for **Sunrise Wellness Studio** — a boutique fitness + wellness studio offering memberships ($79 / $149 / $249), personal training, group classes (HIIT, Yoga, Pilates), and nutrition coaching.

The build is organized **by business problem**, not by GHL feature. That means:

- A studio owner can flip open `problems/03-appointment-no-show-recovery/README.md` and see exactly what we're solving and why.
- A GHL operator can flip to the same folder's `build.md` and rebuild the entire system click-by-click in a clean sub-account.
- Every funnel page, email, SMS, and workflow has the **production-ready copy** sitting in the `assets/` subfolder — no placeholders to fill in.

---

## How to Use This Folder

### If you are the studio owner (or a prospect)

Read in this order — total time about 7 minutes:

1. **[00-business-overview.md](00-business-overview.md)** — who Sunrise Wellness is and the seven customer personas we'll engage.
2. **[diagrams/problem-map.md](diagrams/problem-map.md)** — the master diagram. Which persona has which pain, and which system we built to solve it.
3. **[client-talking-points.md](client-talking-points.md)** — one paragraph per problem, suitable for a sales conversation.
4. Pick any problem in `problems/` and read its `README.md` — that is the pitch for that specific system.

### If you are the GHL operator building this

Read in this order:

1. **[integration/build-order.md](integration/build-order.md)** — what to build first, second, third.
2. **[shared-foundation/](shared-foundation/)** — five files defining every custom field, tag, pipeline, custom value, and product. Build these once, reuse everywhere.
3. **[scripts/README.md](scripts/README.md)** — run the provisioning scripts to create custom fields, tags, pipelines, products, and calendars via API automatically. Takes ~5 minutes instead of hours in the UI.
4. Work through `problems/01-...` through `problems/10-...` in order. Each problem's `build.md` lists prerequisites (shared-foundation assets) and exact GHL clicks.
5. **[integration/master-automation-graph.md](integration/master-automation-graph.md)** — how the ten isolated systems connect into one engine once everything is built.
6. **[integration/end-to-end-scenario.md](integration/end-to-end-scenario.md)** — trace one lead's full journey through every system as a test.

---

## The 10 Problems We Solve

| # | Problem | Who it hurts | Where it lives |
|---|---|---|---|
| 01 | **Lead Capture & Instant Response** — leads from IG/FB/Google go cold before anyone replies | Cold lead | [problems/01-lead-capture-and-instant-response/](problems/01-lead-capture-and-instant-response/) |
| 02 | **Trial-to-Paid Conversion** — free trials never convert to paying members | Trial member | [problems/02-trial-to-paid-conversion/](problems/02-trial-to-paid-conversion/) |
| 03 | **Appointment No-Show Recovery** — PT and class no-shows waste trainer hours and revenue | Booked lead / member | [problems/03-appointment-no-show-recovery/](problems/03-appointment-no-show-recovery/) |
| 04 | **New Member Onboarding** — new members ghost in the first 30 days | New member (day 0–30) | [problems/04-new-member-onboarding/](problems/04-new-member-onboarding/) |
| 05 | **Retention & Churn Prevention** — active members quietly disengage, then cancel | Active member (90+ days) | [problems/05-retention-and-churn-prevention/](problems/05-retention-and-churn-prevention/) |
| 06 | **Upsell & Cross-Sell** — Basic members never upgrade; PT and nutrition go un-sold | Active member | [problems/06-upsell-and-cross-sell/](problems/06-upsell-and-cross-sell/) |
| 07 | **Reviews & Reputation** — inconsistent Google reviews hurt local SEO | Happy member (under-asked) | [problems/07-reviews-and-reputation/](problems/07-reviews-and-reputation/) |
| 08 | **Referral Engine** — word-of-mouth happens but isn't systematic or rewarded | Promoter member | [problems/08-referral-engine/](problems/08-referral-engine/) |
| 09 | **Win-Back Lapsed Members** — cancelled members are never re-engaged | Lapsed member | [problems/09-win-back-lapsed-members/](problems/09-win-back-lapsed-members/) |
| 10 | **Owner Reporting & Visibility** — owner has no clear view of pipeline, revenue, or retention | Studio owner | [problems/10-owner-reporting-and-visibility/](problems/10-owner-reporting-and-visibility/) |

---

## Folder Map

```
client-demo/sunrise-wellness-studio/
├── README.md                          ← you are here
├── 00-business-overview.md            ← who Sunrise is, personas, revenue model
├── client-talking-points.md           ← 1-pager for sales conversations
├── diagrams/
│   ├── problem-map.md                 ← master mermaid: personas → problems → solutions
│   ├── customer-journey.md            ← lifecycle from cold lead → promoter
│   └── revenue-impact.md              ← $ impact per problem
├── shared-foundation/
│   ├── custom-fields.md               ← every contact field used across problems
│   ├── tags.md                        ← tag taxonomy
│   ├── pipelines.md                   ← Membership Sales, Onboarding, Retention
│   ├── custom-values.md               ← business-wide variables (hours, phone, etc.)
│   └── products-and-pricing.md        ← memberships, PT, packages, retail
├── scripts/                           ← API provisioning scripts (run these first)
│   ├── README.md                      ← setup + execution instructions
│   ├── .env.example                   ← copy to .env, add your API key
│   ├── config.py / ghl_client.py      ← shared HTTP client with retry, dry-run, logging
│   ├── 01_custom_values.py            ← provisions 72 custom values
│   ├── 02_custom_fields.py            ← provisions 64 custom fields in 5 folders
│   ├── 03_tags.py                     ← scaffolds 117-tag taxonomy
│   ├── 04_pipelines.py                ← provisions 3 pipelines + stages
│   ├── 05_products_and_coupons.py     ← provisions 10 products + 7 coupons
│   ├── 06_calendars.py                ← provisions 9 calendars
│   ├── 99_verify_foundation.py        ← verifies all assets match spec
│   └── data/                          ← source-of-truth JSON for each asset type
├── problems/
│   ├── 01-lead-capture-and-instant-response/
│   ├── 02-trial-to-paid-conversion/
│   ├── 03-appointment-no-show-recovery/
│   ├── 04-new-member-onboarding/
│   ├── 05-retention-and-churn-prevention/
│   ├── 06-upsell-and-cross-sell/
│   ├── 07-reviews-and-reputation/
│   ├── 08-referral-engine/
│   ├── 09-win-back-lapsed-members/
│   └── 10-owner-reporting-and-visibility/
│       Each contains:
│         README.md      ← client-pitch layer
│         build.md       ← step-by-step GHL build
│         assets/        ← funnel.md, emails.md, sms.md, workflow.md, forms.md
└── integration/
    ├── master-automation-graph.md     ← how all 10 systems interconnect
    ├── build-order.md                 ← what to build first → last
    └── end-to-end-scenario.md         ← one lead's full journey through all 10
```

---

## What Makes This "Eyecatchy"

A typical GHL setup is a pile of disconnected pieces — a funnel here, a workflow there, no story. This build is different:

- **Every system maps to a real customer pain.** No "let's set up a workflow because GHL has workflows." Every automation has a target persona and a measurable outcome.
- **The ten systems compose into one engine.** Lead capture feeds trial conversion. Trial conversion feeds onboarding. Onboarding feeds retention. Retention forks into upsell, reviews, and referrals. Churn fires win-back. The owner sees all of it in one dashboard. See [integration/master-automation-graph.md](integration/master-automation-graph.md).
- **Production-ready, not template-shaped.** Funnel copy is written for *this* business, in *this* tone. Email subject lines, SMS bodies, button microcopy — all real, all on-brand.
- **Replicable by any operator.** Every `build.md` is precise enough that a competent GHL operator can replicate the system in a fresh sub-account in 30–90 minutes per problem.

---

## Build Time Estimate

| Phase | What | Time |
|---|---|---|
| Shared foundation | Custom fields, tags, pipelines, products, custom values | 3–4 hours |
| Problems 01–10 | Funnels, emails, SMS, workflows for each | 30–90 min each = 8–14 hours |
| Integration | Connecting workflows, dashboard, reporting digest | 2–3 hours |
| **Total** | **Complete sub-account ready for the studio to start using** | **15–20 hours** |

A solo operator can stand up the entire build in 2–3 working days. A team can split problems and do it in one.
