# Shared Foundation — Tag Taxonomy

> Tags are GHL's lightweight, multi-value labels. Use tags for **states** (boolean conditions) and **categories** (segmenting). Use [custom-fields.md](custom-fields.md) for **data** (values you store and read). Every problem's workflows add and remove tags from this list.

---

## Tag Naming Convention

All tags follow this format: `prefix-state` (lowercase, hyphenated).

Prefixes group tags by purpose:

| Prefix | Meaning | Examples |
|---|---|---|
| `lead-` | Lead lifecycle state | `lead-new`, `lead-contacted`, `lead-cold` |
| `trial-` | Trial state | `trial-active`, `trial-converted`, `trial-expired` |
| `member-` | Membership state | `member-active`, `member-paused`, `member-lapsed` |
| `tier-` | Membership tier | `tier-basic`, `tier-premium`, `tier-vip` |
| `risk-` | Engagement risk level | `risk-watching`, `risk-at-risk`, `risk-critical` |
| `source-` | Lead source | `source-instagram`, `source-google`, `source-referral` |
| `apt-` | Appointment state | `apt-noshow`, `apt-rescheduled`, `apt-completed` |
| `interest-` | Behavioral interest signal | `interest-pt`, `interest-nutrition`, `interest-vip` |
| `campaign-` | Active in a campaign | `campaign-winback-d30`, `campaign-spring-launch` |
| `do-not-` | Suppression flags | `do-not-email`, `do-not-email`, `do-not-call` |

Tags are **additive** — a contact can have many. A single member could simultaneously have `member-active`, `tier-premium`, `interest-nutrition`, and `risk-watching`.

---

## Complete Tag List

### Lead lifecycle

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `lead-new` | Form submission (any source) | When `lead-contacted` is added | #01 |
| `lead-contacted` | First Email or email sent | When `trial-active` or `member-active` is added | #01 |
| `lead-responded` | Contact replies to Email/email | When `trial-active` is added | #01 |
| `lead-cold` | 14 days with no response | When contact replies | #01 |
| `lead-lost` | 60 days no engagement | (manual cleanup) | #01 |

### Trial lifecycle

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `trial-claimed` | Trial pass downloaded / booked | When trial ends | #02 |
| `trial-active` | First class attended | On day 7 of trial | #02 |
| `trial-attended-1` | 1st class attended during trial | Permanent | #02 |
| `trial-attended-3plus` | 3+ classes attended during trial | Permanent | #02 |
| `trial-converted` | Paid membership purchased | Permanent | #02 |
| `trial-expired` | Day 7 reached without paid conversion | When `trial-converted` is added | #02 |
| `trial-not-now` | Replied "not now" to conversion offer | When `member-active` is added | #02 |

### Membership state

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `member-active` | First successful payment | When `member-paused`, `-cancelled`, or `-lapsed` is added | #04, #05, #06 |
| `member-onboarding` | Day 0–30 after signup | Day 31 | #04 |
| `member-paused` | Owner pauses membership (vacation, injury) | When unpaused | #05 |
| `member-cancelled` | Cancellation request processed | When reactivated | #09 |
| `member-lapsed` | 30 days past cancel without reactivation | When reactivated | #09 |
| `member-reactivated` | Lapsed member returns | Permanent (badge) | #09 |
| `member-vip-veteran` | Member 2+ years | Permanent | #06, #10 |

### Tier (only one at a time)

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `tier-basic` | Buys $79 membership | When upgrades | #06 |
| `tier-premium` | Buys $149 membership | When upgrades or downgrades | #06 |
| `tier-vip` | Buys $249 membership | When downgrades | #06 |

### Risk level (only one at a time)

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `risk-healthy` | Engagement score ≥ 70 | When score drops | #05 |
| `risk-watching` | Engagement score 50–69 | When score moves | #05 |
| `risk-at-risk` | Engagement score 30–49 | When score moves | #05 |
| `risk-critical` | Engagement score < 30 | When score recovers or member cancels | #05 |

### Lead source (only one at a time, set at capture)

| Tag | Used by |
|---|---|
| `source-instagram` | #01, #10 |
| `source-facebook` | #01, #10 |
| `source-google` | #01, #10 |
| `source-walkin` | #01, #10 |
| `source-referral` | #01, #08, #10 |
| `source-web` | #01, #10 |
| `source-event` | #01, #10 |

### Appointment events

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `apt-confirmed` | Member confirms via reminder | Removed when appt fires | #03 |
| `apt-completed` | Status set to "showed" after appt | Permanent record on contact | #03 |
| `apt-noshow` | Status set to "no-show" | When rebooked | #03 |
| `apt-noshow-repeat` | 2+ no-shows in 30 days | After 30 days clean | #03 |
| `apt-rescheduled` | Member rescheduled before appt | Removed at next appt | #03 |

### Behavioral interest

| Tag | When applied | Used by |
|---|---|---|
| `interest-pt` | Books or asks about PT | #06 |
| `interest-nutrition` | Books or asks about nutrition | #06 |
| `interest-vip` | Hits VIP-trigger behavior (4+ PT/mo) | #06 |
| `interest-classes-am` | Most attendance is AM | #06 (offer AM-tier discounts) |
| `interest-classes-pm` | Most attendance is PM | #06 |

### Campaign membership (temporary)

| Tag | When applied | When removed | Used by |
|---|---|---|---|
| `campaign-onboarding` | Active in onboarding sequence | Day 31 | #04 |
| `campaign-trial-nurture` | Active in trial nurture | Day 7 of trial | #02 |
| `campaign-winback-d30` | In day-30 win-back step | After day 30 step fires | #09 |
| `campaign-winback-d60` | In day-60 win-back step | After day 60 step fires | #09 |
| `campaign-winback-d90` | In day-90 win-back step | After day 90 step fires | #09 |
| `campaign-review-ask` | Sent review-ask Email | 30 days after | #07 |
| `campaign-referral-promoter` | Tagged as a top referrer (quarterly) | Next quarter | #08 |

### Suppression / consent

| Tag | Meaning | Used by |
|---|---|---|
| `do-not-email` | Hard block on Email sends | Every Email-sending workflow checks |
| `do-not-email` | Hard block on email sends | Every email-sending workflow checks |
| `do-not-call` | Hard block on outbound calls | Owner / staff awareness |
| `do-not-market` | Suppresses all marketing (keeps transactional) | All marketing workflows |
| `vip-do-not-disturb` | High-value member, owner-only contact | All workflows except #05 critical |

---

## Tag vs Field Decision Rule

When designing a new workflow, ask:

- **Is this a boolean state?** ("are they in onboarding?") → Tag.
- **Is this a single value from a fixed set?** ("which tier?") → Either, but prefer tag for tier-style (faster smart-list filtering).
- **Is this a number, date, or free text?** → Custom field.
- **Will I filter on this in a smart list?** → Tag is faster.
- **Will I display this on the contact card?** → Field shows nicer.

For tier and risk, we use **both** a tag *and* a field. The tag is for fast filtering in smart lists; the field is for the contact card and reporting. Workflows keep them in sync.

---

## Smart Lists Built On These Tags

The reporting system (#10) uses these tag-based smart lists. Build these after tags exist:

| Smart List | Tag Filter |
|---|---|
| All Hot Leads | `lead-new` OR `lead-responded` AND NOT `trial-active` |
| Active Trials Needing Attention | `trial-active` AND NOT `trial-attended-3plus` |
| New Members in Onboarding | `member-active` AND `member-onboarding` |
| All At-Risk Members | `risk-at-risk` OR `risk-critical` |
| Basic Members (Upsell Targets) | `tier-basic` AND `member-active` |
| Lapsed Members (Win-Back Targets) | `member-lapsed` |
| Top Referrers (Quarterly) | `campaign-referral-promoter` |
| VIP Veterans | `member-vip-veteran` |

---

## Build Verification

After creating tags:

1. Go to **Settings > Tags** (or **Contacts > Tags** depending on GHL UI version).
2. Confirm all tags exist with the exact lowercase, hyphenated naming above.
3. Apply 4–5 mixed tags to a test contact to confirm rendering and filtering work.
4. Build the "All Hot Leads" smart list as a sanity check.

---

---

## Extensions Added by Specific Problem Builds

Operational and transient tags introduced by individual problem builds. Add to your sub-account as you build each problem. These follow the same `prefix-state` convention.

### From #02 Trial-to-Paid Conversion

`trial-warm`, `trial-needs-personal-touch`, `trial-high-engagement-no-convert`

### From #03 Appointment No-Show Recovery

`apt-pending`, `apt-needs-reschedule`, `apt-needs-response`, `apt-front-desk-action`, `apt-cancelled`

### From #04 New Member Onboarding

`onboarding-attended-week1`, `onboarding-needs-nudge`, `onboarding-save-attempted`, `onboarding-needs-response`, `onboarding-front-desk-action`, `member-pause-requested`, `member-cancel-requested`, `owner-save-sms`

### From #05 Retention & Churn Prevention

`transition-to-watching`, `transition-to-at-risk`, `transition-to-critical` (transition triggers — applied for one workflow tick then removed)

`save-watching-success`, `save-at-risk-engaged`, `save-at-risk-success-pending`, `save-at-risk-failed`, `save-critical-success-pending`, `member-saved` (persistent "saved" badge), `save-mature-30d`

`campaign-retention-watching`, `retention-reply-received`

### From #06 Upsell & Cross-Sell

`campaign-upsell-basic-premium`, `campaign-upsell-premium-vip`, `campaign-upsell-nutrition-starter`, `campaign-upsell-nutrition-plan`

`upsell-recent`, `upsell-converted-basic-premium`, `upsell-converted-premium-vip`, `upsell-converted-nutrition-starter`, `upsell-converted-nutrition-plan`, `upsell-declined-30d`, `upsell-interest-confirmed`, `upsell-decline-explicit`

`referral-prompt-ready` (handoff tag to #08), `email-engaged-30d`, `sms-engaged-30d`

### From #07 Reviews & Reputation

`review-submitted-google`, `feedback-received-private`, `do-not-ask-reviews`, `review-skipped-cooldown`, `review-no-response`, `feedback-phone-ok`, `feedback-owner-resolved`, `review-replied-positive`, `feedback-conversational`, `review-deferred`, `review-needs-help`

### From #08 Referral Engine

`referral-code-generated` (audit marker after #08 generates and stores referral_code)

### From #09 Win-Back Lapsed Members

`payment-failed-pending`, `payment-recovered`, `member-permanent-loss` (Day 120 final)

### Anniversaries & milestones (from #10 Reporting)

`anniversary-1yr`, `anniversary-2yr`, `anniversary-3yr` (applied by nightly anniversary check workflow)

---

## Related Foundation

- **[custom-fields.md](custom-fields.md)** — contact data fields (the "value" half).
- **[pipelines.md](pipelines.md)** — pipelines that complement tags for stage tracking.
