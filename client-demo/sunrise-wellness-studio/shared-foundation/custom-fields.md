# Shared Foundation — Custom Fields

> Every Contact custom field used across all 10 problems, defined once here. Build these **first**, before any funnel, workflow, or pipeline. Every `build.md` references field names from this file.

---

## How to Build Custom Fields

Navigate to **Settings > Custom Fields > Contact** in your GHL sub-account.

Create folders first (the four below), then add fields into each folder. GHL field types we use:

- **Single Line** — short text (e.g., source, trainer name)
- **Multi-line** — paragraph text (e.g., goals, notes)
- **Number** — integers and decimals (e.g., session count, MRR)
- **Date** — ISO date (e.g., join date, last visit)
- **Date & Time** — full timestamp
- **Single Option** — dropdown (one value)
- **Multiple Options** — checkbox group (many values)
- **Phone** — formatted phone
- **Email** — validated email
- **Monetary** — currency-formatted

---

## Folder 1: Lead Info

Fields populated when a lead first enters GHL. Used by [problems/01](../problems/01-lead-capture-and-instant-response/) and [#02](../problems/02-trial-to-paid-conversion/).

| Field Name | Field Key | Type | Options / Notes |
|---|---|---|---|
| Lead Source | `lead_source` | Single Option | Instagram, Facebook, Google, Walk-in, Referral, Web Search, Other |
| Lead Source Detail | `lead_source_detail` | Single Line | Free text — e.g., campaign name, friend's name |
| Lead Campaign | `lead_campaign` | Single Line | UTM-derived campaign name |
| Lead Captured At | `lead_captured_at` | Date & Time | Auto-set on form submission |
| Lead First Response At | `lead_first_response_at` | Date & Time | Set when first Email/email sent |
| Lead Status | `lead_status` | Single Option | New, Contacted, Responded, Trial Booked, Trial Active, Converted, Lost |
| Referred By Contact ID | `referred_by_contact_id` | Single Line | GHL contact ID of referrer (used by #08) |
| Referral Code Used | `referral_code_used` | Single Line | The unique code the referrer shared |

---

## Folder 2: Fitness Profile

Member-specific fitness and goal data. Used by [#02](../problems/02-trial-to-paid-conversion/), [#04](../problems/04-new-member-onboarding/), [#06](../problems/06-upsell-and-cross-sell/).

| Field Name | Field Key | Type | Options / Notes |
|---|---|---|---|
| Primary Goal | `fitness_goal_primary` | Single Option | Lose Weight, Build Muscle, Improve Fitness, Manage Stress, Recover from Injury, Train for Event, General Wellness |
| Secondary Goals | `fitness_goals_secondary` | Multiple Options | Same options as primary |
| Experience Level | `fitness_experience` | Single Option | Beginner, Intermediate, Advanced |
| Preferred Workout Time | `preferred_workout_time` | Single Option | Early Morning (5-8AM), Morning (8-11AM), Midday (11AM-2PM), Afternoon (2-5PM), Evening (5-8PM), Late Evening (8PM+) |
| Preferred Class Types | `preferred_classes` | Multiple Options | HIIT, Yoga, Pilates, Strength, Mobility, Recovery |
| Assigned Trainer | `assigned_trainer` | Single Option | Alex (Lead), Jordan, Casey, Unassigned |
| Nutrition Coaching Interest | `nutrition_interest` | Single Option | Yes — High, Yes — Curious, No, Not Now |
| Injuries / Limitations | `injuries_limitations` | Multi-line | Free text — for trainer awareness |

---

## Folder 3: Membership Info

Active member data. Used by [#04](../problems/04-new-member-onboarding/), [#05](../problems/05-retention-and-churn-prevention/), [#06](../problems/06-upsell-and-cross-sell/), [#09](../problems/09-win-back-lapsed-members/), [#10](../problems/10-owner-reporting-and-visibility/).

| Field Name | Field Key | Type | Options / Notes |
|---|---|---|---|
| Membership Tier | `membership_tier` | Single Option | None, Trial, Basic, Premium, VIP |
| Membership Status | `membership_status` | Single Option | Prospect, Trial Active, Trial Ended, Active, Paused, Cancelled, Lapsed |
| Membership Start Date | `membership_start_date` | Date | First paid day |
| Membership Renewal Date | `membership_renewal_date` | Date | Next billing date |
| Membership Cancel Date | `membership_cancel_date` | Date | If cancelled — populated by #09 trigger |
| Cancel Reason | `cancel_reason` | Single Option | Cost, Time, Moved, Injury, Switched Studio, Not Using, Failed Payment, Other |
| Monthly Rate | `monthly_rate` | Monetary | $79, $149, or $249 |
| Total LTV to Date | `ltv_to_date` | Monetary | Updated monthly by reporting workflow |
| Days as Member | `days_as_member` | Number | Updated nightly |
| Onboarding Completed | `onboarding_completed` | Single Option | No, In Progress, Yes |
| Onboarding Completed Date | `onboarding_completed_date` | Date | Set when day-30 check completes |

---

## Folder 4: Engagement & Activity

Behavioral data driving retention, upsell, reviews, referral. Used by [#03](../problems/03-appointment-no-show-recovery/), [#05](../problems/05-retention-and-churn-prevention/), [#06](../problems/06-upsell-and-cross-sell/), [#07](../problems/07-reviews-and-reputation/), [#08](../problems/08-referral-engine/).

| Field Name | Field Key | Type | Options / Notes |
|---|---|---|---|
| Last Visit Date | `last_visit_date` | Date | Updated by check-in / class attendance |
| Visits Last 30 Days | `visits_last_30_days` | Number | Rolling 30-day attendance count |
| Visits Last 90 Days | `visits_last_90_days` | Number | Rolling 90-day count |
| Total Visits | `total_visits_lifetime` | Number | All-time |
| Last PT Session Date | `last_pt_session_date` | Date | Most recent PT |
| Total PT Sessions | `total_pt_sessions` | Number | Lifetime PT count |
| Last Class Attended | `last_class_attended` | Single Line | Class name + date |
| No-Show Count (90d) | `noshow_count_90d` | Number | Rolling 90-day no-shows |
| Engagement Score | `engagement_score` | Number | 0–100, calculated by #05 workflow |
| At-Risk Flag | `at_risk_flag` | Single Option | No, Watching, At-Risk, Critical |
| Review Submitted Date | `review_submitted_date` | Date | When member left Google review |
| Review Star Rating | `review_star_rating` | Number | 1–5 (from internal funnel) |
| Referral Code | `referral_code` | Single Line | Unique per member — e.g., SARAH-42 |
| Referrals Made | `referrals_made_count` | Number | How many people they referred |
| Referrals Converted | `referrals_converted_count` | Number | How many paid |

---

## Folder 5: Communication Preferences

Channel preferences and consent. Used by every problem that sends Email or email.

| Field Name | Field Key | Type | Options / Notes |
|---|---|---|---|
| Email Opt-In | `sms_opt_in` | Single Option | Yes, No |
| Email Opt-In | `email_opt_in` | Single Option | Yes, No |
| Marketing Opt-In | `marketing_opt_in` | Single Option | Yes, No (separate from transactional) |
| Preferred Contact Channel | `preferred_channel` | Single Option | emails, App Push, Call |
| Quiet Hours Start | `quiet_hours_start` | Single Line | e.g., 21:00 |
| Quiet Hours End | `quiet_hours_end` | Single Line | e.g., 08:00 |

---

## Full Field Count

| Folder | Fields |
|---|---|
| Lead Info | 8 |
| Fitness Profile | 8 |
| Membership Info | 11 |
| Engagement & Activity | 15 |
| Communication Preferences | 6 |
| **Total** | **48 custom fields** |

GHL handles this volume fine. Group them in folders so the contact-detail view stays organized — collapsed by default, expanded when relevant.

---

## Build Verification

After creating all fields:

1. Go to a test contact's profile.
2. Confirm you see all five folders in the custom-field sidebar.
3. Confirm each folder expands and the field list matches above.
4. Test one field of each type — single line, dropdown, date, number, monetary — by saving a value and reloading.

If any field is missing, a downstream `build.md` will fail when it tries to reference the field in a workflow action.

---

---

## Extensions Added by Specific Problem Builds

The following fields are introduced by individual problem `build.md` files when their workflows need new data. Add them to your sub-account when you build the relevant problem. They are tracked here so future maintainers don't think they're orphans.

### From #05 Retention & Churn Prevention

| Field Name | Field Key | Type | Folder | Notes |
|---|---|---|---|---|
| At-Risk Flag Previous | `at_risk_flag_previous` | Single Option | Engagement & Activity | Mirrors `at_risk_flag` one tick behind — used by #05 transition detection. |

### From #06 Upsell & Cross-Sell

| Field Name | Field Key | Type | Folder | Notes |
|---|---|---|---|---|
| Upsell Offer Active | `upsell_offer_active` | Single Option | Engagement & Activity | "None / Basic-Premium / Premium-VIP / Nutrition-Starter / Nutrition-Plan" |
| Upsell Offer Started At | `upsell_offer_started_at` | Date & Time | Engagement & Activity | Cooldown calculation |
| Last Upsell Conversion Date | `last_upsell_conversion_date` | Date | Engagement & Activity | — |
| Total Upsell Conversions | `total_upsell_conversions` | Number | Engagement & Activity | Lifetime count |
| PT Sessions 30d Snapshot | `pt_sessions_30d_snapshot` | Number | Engagement & Activity | Optional — fallback for plans without native appt-count merge |

### From #07 Reviews & Reputation

| Field Name | Field Key | Type | Folder | Notes |
|---|---|---|---|---|
| Review Ask Sent At | `review_ask_sent_at` | Date & Time | Engagement & Activity | Cooldown gate |
| Private Feedback Text | `private_feedback_text` | Multi-line | Lead Info | From 1–3 star private feedback form |
| Private Feedback Urgent | `private_feedback_urgent` | Single Option | Lead Info | Yes/No flag for owner alerting |
| Feedback Submitted Date | `feedback_submitted_date` | Date & Time | Lead Info | — |
| Feedback Phone Ok | `feedback_phone_ok` | Single Option | Lead Info | Yes/No — member consented to be called about negative feedback |

### From #08 Referral Engine

| Field Name | Field Key | Type | Folder | Notes |
|---|---|---|---|---|
| PT Credit Balance | `pt_credit_balance` | Number | Engagement & Activity | Counts unredeemed PT session credits earned via referrals |
| Referral Share URL | `referral_share_url` | Single Line | Engagement & Activity | Pre-built share URL — pasted into invite Email/email |

### From #09 Win-Back Lapsed Members

| Field Name | Field Key | Type | Folder | Notes |
|---|---|---|---|---|
| Payment Failed At | `payment_failed_at` | Date & Time | Engagement & Activity | Stripe webhook stamp |
| Cancel Notes | `cancel_notes` | Multi-line | Engagement & Activity | Free-text from cancellation form (complements structured `cancel_reason`) |
| Payment Update URL | `payment_update_url` | Single Line | Engagement & Activity | Per-contact tokenized link to Stripe customer portal |

**Updated total field count with extensions: 61 fields.**

---

## Related Foundation

- **[tags.md](tags.md)** — tag taxonomy that complements (not duplicates) these fields.
- **[pipelines.md](pipelines.md)** — pipelines that surface a subset of these fields as stage data.
- **[custom-values.md](custom-values.md)** — global variables (not per-contact).
