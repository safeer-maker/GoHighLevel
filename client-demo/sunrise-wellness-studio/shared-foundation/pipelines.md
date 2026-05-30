# Shared Foundation — Pipelines

> Three opportunity pipelines, each owning a discrete chunk of the customer lifecycle. Tags and custom fields handle most state — pipelines are for **owner-visible deal flow** where a stage change is a meaningful business event.

---

## Why Three Pipelines, Not One?

A common GHL mistake is one giant pipeline with 12 stages. That looks like progress but breaks reporting (an opportunity in "Trial Booked" can't simultaneously be in "Day-30 Renewal Risk"). Three smaller pipelines, each scoped to a phase, gives clean reporting and lets the owner glance at the kanban and immediately see what matters.

| Pipeline | Owns | Used by problem |
|---|---|---|
| **Membership Sales** | Lead → Paid Member | #01, #02 |
| **Onboarding** | New Member → Onboarded (Day 0–30) | #04 |
| **Retention** | Active Member → At-Risk → Saved / Lapsed | #05, #09 |

The same contact can have an opportunity in multiple pipelines simultaneously. That's intentional — a new member is *done* with Sales (won), *in progress* in Onboarding, and *not yet entered* in Retention.

---

## Pipeline 1: Membership Sales

**Purpose:** Track every lead from first touch to paid member. Owner watches this for trial-conversion forecasting.

**Build path:** `Opportunities > Pipelines > + Create Pipeline > "Membership Sales"`

### Stages

| Order | Stage Name | Enter Condition | Exit Condition | Won/Lost? |
|---|---|---|---|---|
| 1 | **New Lead** | Form submitted, walk-in logged, or referral signup | Contact replies OR trial booked | — |
| 2 | **Contacted** | First outbound Email or email sent | Contact replies OR 14 days elapsed | — |
| 3 | **Trial Booked** | Trial appointment exists on calendar | Trial start date | — |
| 4 | **Trial Active** | Trial start date passes | Day 7 of trial | — |
| 5 | **Conversion Offer Sent** | Day 5–7 of trial, offer email/Email fires | Member pays OR declines | — |
| 6 | **Won — Paid Member** | Successful first payment | (terminal — opportunity status "Won") | ✅ Won |
| 7 | **Lost — Trial Expired** | Day 7 with no conversion | (terminal — status "Lost") | ❌ Lost |
| 8 | **Lost — Never Engaged** | 30 days no engagement from "Contacted" | (terminal — status "Lost") | ❌ Lost |

### Opportunity value field

Set opportunity value = `monthly_rate × 12` so the kanban total reflects projected annual revenue (e.g., $79 × 12 = $948 per lead).

### Owner's "what to do" with this pipeline

- Glance the kanban every morning. Anything in "Trial Active" past 4 days needs an offer.
- "Contacted" stage older than 7 days = stale — handed off to a long nurture or marked lost.
- Won column ÷ (Won + Lost) = trial-to-paid conversion rate. Headline KPI.

---

## Pipeline 2: Onboarding

**Purpose:** Track new members through the critical first 30 days. Surfaces members who are falling behind on onboarding milestones.

**Build path:** `Opportunities > Pipelines > + Create Pipeline > "Onboarding"`

### Stages

| Order | Stage Name | Enter Condition | Exit Condition | Won/Lost? |
|---|---|---|---|---|
| 1 | **Welcome Sent (Day 0)** | First payment processed | Day 1 Email/email fires | — |
| 2 | **First Visit Confirmed** | `last_visit_date` populated | 7 days from join | — |
| 3 | **Week 1 Check-In** | Day 7 reached | Member replies or day 14 | — |
| 4 | **Two-Week Milestone** | Day 14, member has visited 2+ times | Day 21 | — |
| 5 | **Goal Review (Day 21)** | Day 21 reached, owner books goal-review call | Call completed | — |
| 6 | **Onboarded (Day 30)** | Day 30 with 3+ visits + goal review done | (terminal — status "Won") | ✅ Won |
| 7 | **Onboarding At-Risk** | Day 14 with 0–1 visit | Member re-engages OR day 30 | — |
| 8 | **Early Churn Risk** | Day 21 with 0 visits | Day 30 cancel or save | — |

### Opportunity value field

Set value = `monthly_rate × 12` again, but this pipeline is more about *kanban visibility* than revenue tracking — the won/lost ratio is the real KPI.

### Owner's "what to do" with this pipeline

- Daily glance: anything in "Onboarding At-Risk" or "Early Churn Risk" gets a personal owner call. These are the saves.
- Won % at Day 30 = onboarding effectiveness. Target: 80%+.

---

## Pipeline 3: Retention

**Purpose:** Track active members who slip into at-risk states, plus win-back attempts for lapsed members. Owner uses this to see who needs intervention.

**Build path:** `Opportunities > Pipelines > + Create Pipeline > "Retention"`

### Stages

| Order | Stage Name | Enter Condition | Exit Condition | Won/Lost? |
|---|---|---|---|---|
| 1 | **Healthy** | Engagement score ≥ 70 | Score drops below 70 | — |
| 2 | **Watching** | Engagement score 50–69 | Score moves up or down | — |
| 3 | **At-Risk** | Engagement score 30–49 | Save action taken OR score continues down | — |
| 4 | **Critical** | Engagement score < 30 | Save action OR member cancels | — |
| 5 | **Save In Progress** | Owner intervention (PT offer, check-in call, etc.) sent | Member re-engages OR cancels | — |
| 6 | **Saved** | Score returns to ≥ 70 | (terminal — status "Won") | ✅ Won |
| 7 | **Lost — Cancelled** | Member submits cancel | Moves to Win-Back stage 1 | ❌ Lost |
| 8 | **Win-Back D30** | 30 days post-cancel | Day 60 fires | — |
| 9 | **Win-Back D60** | Day 60 post-cancel | Day 90 fires | — |
| 10 | **Win-Back D90** | Day 90 post-cancel | Day 120 — final | — |
| 11 | **Reactivated** | Lapsed member buys membership again | (terminal — status "Won") | ✅ Won |
| 12 | **Permanent Loss** | Day 120 post-cancel, no reactivation | (terminal — status "Lost") | ❌ Lost |

### Opportunity value field

For active members: value = `monthly_rate × 12`. For win-back: value = `monthly_rate × 6` (more conservative LTV estimate for reactivated).

### Owner's "what to do" with this pipeline

- The owner's most valuable kanban. Daily glance: who's in "At-Risk" or "Critical"? Take one action (text, free PT offer, in-person hello).
- Saved ÷ (Saved + Lost-Cancelled) = save rate. Target: 30%+.
- Reactivated ÷ (Reactivated + Permanent Loss) = win-back rate. Target: 15%+.

---

## How Tags and Pipelines Coordinate

Pipelines are owner-facing; tags are workflow-facing. Both update together:

| Event | Pipeline action | Tag action |
|---|---|---|
| New lead | Create opportunity in Membership Sales → Stage "New Lead" | Add `lead-new`, `source-*` |
| Trial booked | Move to "Trial Booked" | Add `trial-claimed` |
| Trial converts | Move to "Won — Paid Member" + create opportunity in Onboarding | Add `trial-converted`, `member-active`, `tier-*`, `member-onboarding` |
| Day 30 onboarding complete | Move Onboarding opp to "Onboarded" (Won) + create opportunity in Retention "Healthy" | Remove `member-onboarding`; add `risk-healthy` |
| Engagement drops below 70 | Move Retention opp to "Watching" or "At-Risk" | Update `risk-*` tag |
| Member cancels | Move Retention opp to "Lost — Cancelled" → stage "Win-Back D30" after 30 days | Add `member-cancelled`, `member-lapsed` at day 30 |
| Lapsed reactivates | Move Retention opp to "Reactivated" + create new Onboarding opp | Add `member-reactivated`, remove `member-lapsed`, add `member-onboarding` |

Every workflow that changes a pipeline stage **also** updates the corresponding tag, in the same action sequence. Inconsistent state is the #1 bug source — keep them paired.

---

## Build Verification

After building all three pipelines:

1. Create a test contact and walk them through the Membership Sales pipeline manually — drag the opportunity stage by stage. Confirm each stage exists, named exactly as above.
2. Repeat for Onboarding and Retention.
3. Confirm the kanban view shows projected revenue totals at the top of each stage column.
4. Confirm "Won" columns have a green dollar total; "Lost" columns have a red flag.

---

## Related Foundation

- **[custom-fields.md](custom-fields.md)** — fields used as opportunity value sources (`monthly_rate`) and stage-transition conditions (`engagement_score`, `last_visit_date`).
- **[tags.md](tags.md)** — tag taxonomy that updates alongside pipeline stage changes.
