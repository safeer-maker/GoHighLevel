# End-to-End Scenario — One Lead, Every System

> A narrative trace of a single person, Sarah Chen, from the moment she clicks an Instagram ad to the moment she becomes a VIP veteran two years later. Every system fires when it should. Use this as the integration test — run a similar trace through your built sub-account and verify every transition happens automatically.

---

## Meet Sarah

- **Age:** 34
- **Where she lives:** Springfield (within Sunrise's 5-mile catchment)
- **Goal:** Lose 15 lbs, build a sustainable workout routine
- **Schedule:** Marketing manager, prefers morning workouts
- **Current state:** Has never been to Sunrise, doesn't know it exists
- **Channel of first touch:** Instagram (a friend liked Sunrise's post)

---

## Day 0, 7:42 PM — Lead Capture (`#01`)

Sarah is scrolling Instagram on her couch. A Sunrise ad appears: "Rise stronger. Move better. Glow brighter." She taps. The funnel loads in 1.4 seconds.

She scrolls the page, reads two testimonials, scrolls to the form. Fills it in 38 seconds:

- First name: Sarah
- Last name: Chen
- Phone: 555-0142
- Email: sarah.chen@email.com
- Goal: Lose Weight
- Time preference: Morning (8–11 AM)
- ✅ Consents to texts/emails

Submits. Lands on the thank-you page. Sees the Instagram feed widget. Follows @sunrisewellnessstudio.

**What fires in GHL (within 60 seconds):**

| System | Action |
|---|---|
| `#01` workflow trigger | "Form Submitted: Lead Capture — Free 7-Day Pass" |
| Custom fields set | `lead_source` = "Instagram", `lead_captured_at` = 2026-05-18 19:42, `fitness_goal_primary` = "Lose Weight", `preferred_workout_time` = "Morning (8-11AM)", `sms_opt_in` = "Yes", `email_opt_in` = "Yes" |
| Tags added | `source-instagram`, `lead-new` |
| Pipeline | Membership Sales > "New Lead" stage, opportunity value $948 |

**7:43 PM** — Sarah's phone buzzes. Email from Morgan: *"Hey Sarah, it's Morgan from Sunrise ☀️ Welcome! Pick a time that fits your week and we'll see you soon: book.sunrisewellness.com Reply HELP for anything, STOP to opt out."*

She smiles. Taps the link. Books a free intro consult for Saturday 10 AM. Calendar event fires.

**What fires in GHL (within seconds):**

| System | Action |
|---|---|
| Calendar trigger | Appointment booked: Intro Consult, Saturday 2026-05-23 10:00 |
| `#01` workflow | Detects `apt-booked` event → marks `trial-claimed` tag |
| Pipeline | Membership Sales > "Trial Booked" stage |
| `#02` workflow trigger | "Tag added: trial-claimed" → enters trial nurture |
| `#03` workflow trigger | Appointment created → schedules reminders for 48hr, 24hr, 2hr |

**7:45 PM** — Welcome email lands in Sarah's inbox (the 2-min delay let the Email land first). Subject: *"Welcome, Sarah — your free 7-day pass is ready ☀️"*

**7:45 PM** — Morgan's inbox gets a notification: *"New lead: Sarah Chen from Instagram"*. She's having dinner — opens it, reads, replies-all in her CRM: "Will message her personally tomorrow morning."

---

## Day 1–6 — Trial Nurture (`#02`) + No-Show Recovery (`#03`)

### Saturday morning (Day 0 + 2)

**8:00 AM** — `#03` fires 2hr reminder Email: *"Sarah, your 10am Intro Consult with Alex is in 2 hours. We're at 123 Wellness Way — door's open, parking out front. See you soon!"*

**9:50 AM** — Sarah arrives. Front desk welcomes her by name (the dashboard showed her arrival window). 30-min consult with Alex. Books her first HIIT class for Monday 7 AM. Walks out energized.

**What fires:**
- `#03` workflow: appointment status set to "showed" → tag `apt-completed`, removes reminder sequence
- New calendar event: Monday 7 AM HIIT class → `#03` schedules reminders for that one too
- `lead_status` = "Trial Active", custom field `last_visit_date` updated

### Sunday (Day 1)

**9:15 AM** — `#02` Day 1 email fires: *"Sarah, here's how to crush your first week"* — a goal-personalized class suggestion list.

### Monday (Day 2)

**6:50 AM** — `#03` 10-min pre-class reminder. *"Sarah, HIIT in 10. Studio's open ☀️"*

**7:55 AM** — Class ends. Sarah feels great. Status set to "showed".

**8:30 AM** — `#02` Day 2 nudge Email: *"Sarah! Heard you crushed HIIT this morning 💪 Tomorrow's Yoga at 7am is the perfect recovery — want me to save you a spot?"*

She replies: "Yes please!" Front desk books her in.

### Tuesday (Day 3)

**7:00 AM** — Yoga class. Attended. `trial-attended-3plus` tag applied (she's now done 2; close).

### Wednesday (Day 4)

**8:30 AM** — `#02` Day 4 email: testimonial-heavy *"Real members. Real wins."* email with two member stories about weight loss + sustainable routine.

### Thursday (Day 5)

She's now done 3 classes. Tag `trial-attended-3plus` applied (third class today).

**10:00 AM** — `#02` Day 5 conversion offer email fires: *"Sarah, want to keep going?"* Pitches Basic Membership ($79/mo) with TRIAL2PAID coupon → 20% off first month + waived $49 enrollment.

**10:01 AM** — `#02` Day 5 Email: *"Sarah, just sent you an email about staying on as a member — TLDR your first month is $63 instead of $128 if you join this week. Link: book.sunrisewellness.com/join Reply YES for me to call you."*

She doesn't reply immediately. She's at lunch.

### Friday (Day 6)

**8:15 AM** — `#02` Day 6 personal-touch Email from Morgan: *"Sarah, no rush — but I'd love to chat about what's working and what's not before your trial ends. Free 5-min call today? Reply with a time."*

Sarah replies: "Sure, after 4pm?" Morgan books a 5-min call at 5 PM.

**5:00 PM** — Call. Sarah asks about Premium (the PT sessions she heard about). Morgan walks her through it. Sarah says she wants to start with Basic, see how it goes.

**5:10 PM** — Morgan sends her the checkout link manually through Conversations.

**5:12 PM** — Sarah pays. $79 charged, coupon applied → $63 actual. Subscription created in Stripe.

**What fires in GHL:**

| System | Action |
|---|---|
| Payment webhook | `subscription.created` event → `member-active` tag, `tier-basic` tag, `trial-converted` tag, `membership_tier` = "Basic", `membership_start_date` = today |
| `#02` workflow | Exits (`trial-converted` removes contact from active workflow) |
| Pipeline | Membership Sales → "Won — Paid Member" stage |
| `#04` workflow trigger | "Tag added: member-active" → enters onboarding |
| Pipeline | Onboarding → "Welcome Sent (Day 0)" stage |
| Owner notification | "🎉 Sarah Chen converted to Basic Member" |

**5:15 PM** — Sarah gets onboarding Welcome emails from `#04`. *"Welcome to the family, Sarah ☀️"*

---

## Days 7–30 — Onboarding (`#04`) + Background No-Show Recovery (`#03`)

`#04` runs its 30-day cadence: Day 1, 3, 7, 14, 21, 30 check-ins. Sarah's milestones:

- **Day 1:** Welcome email, app download Email.
- **Day 3:** First-week class encouragement Email. She attends Pilates (her 4th total class).
- **Day 7:** Week-1 check-in email. *"How's it going, Sarah?"* She replies positively.
- **Day 14:** Two-week milestone celebration Email. *"You've made it 2 weeks! 🎉"*. She's done 6 classes.
- **Day 21:** Goal Review invite — books a 30-min sit-down with Alex for Day 23.
- **Day 23:** Goal Review session. Alex updates her `fitness_goal_primary` to "Lose Weight" + adds secondary "Build Muscle". Tag `interest-nutrition` applied (she mentioned wanting meal advice).
- **Day 28:** First missed class. Booked a HIIT, didn't show. `#03` fires recovery sequence — 2hr post-noshow Email: *"Sarah, missed you at HIIT this morning. Life happens! Tomorrow's slot is open — want me to grab it for you?"*. She rebooks for next day.
- **Day 30:** Onboarding graduation email. *"30 days down, Sarah. You're officially a Sunriser."* Engagement score computed: 78 (Healthy).

**What fires:**

| System | Action |
|---|---|
| `#04` workflow | Day 30 reached → `member-onboarding` tag removed, `onboarding_completed` = "Yes" |
| Pipeline | Onboarding → "Onboarded (Day 30)" (Won) |
| `#05` workflow | New opportunity in Retention pipeline → "Healthy" stage. Tag `risk-healthy` applied. `engagement_score` field populated. |

---

## Days 31–90 — Settling-In, Retention Watch (`#05`)

`#05`'s nightly engagement scoring runs. Sarah's score wobbles:

- **Day 45:** Score = 82. Healthy. No intervention.
- **Day 60:** She's been to 9 classes in last 30 days. Score = 88. Tag `interest-classes-am` applied (almost all AM attendance). Pipeline still Healthy.
- **Day 70:** Work travel — only 2 visits in week of Day 65–72. Score drops to 64. Tag transitions `risk-healthy` → `risk-watching`.

**What fires:**

| System | Action |
|---|---|
| `#05` workflow | Score transition detected → `transition-to-watching` tag → light check-in Email sent: *"Sarah, haven't seen you this week — everything good? Tomorrow's 7am Yoga is a soft landing if you want it."* |
| Pipeline | Retention → "Watching" stage |

She replies: "Yeah, was traveling. Will be back Monday." Tag `retention-reply-received` applied. Morgan doesn't need to intervene.

- **Day 72:** Sarah returns, attends 3 classes that week. Score recovers to 79.
- **Day 80:** Pipeline back to Healthy. `risk-watching` removed, `risk-healthy` re-applied.

---

## Day 95 — Upsell Trigger (`#06`)

Sarah has now attended **13 classes in 30 days** (she's hooked). `#06`'s nightly workflow detects this threshold.

**What fires:**

| System | Action |
|---|---|
| `#06` workflow trigger | Filter: `tier-basic` AND `risk-healthy` AND visits_last_30_days >= 12 |
| Tag applied | `campaign-upsell-basic-premium`, `upsell_offer_started_at` = today |
| Action | Email: *"Sarah, you're crushing Basic — let me show you Premium"*. Includes savings math (2 PT sessions/month + nutrition consult vs. paying for them separately). |

Sarah opens the email. Doesn't act immediately.

**Day 97** — `#06` follow-up Email: *"Sarah, the Premium upgrade includes 2 PT sessions + nutrition — saves ~$135 vs paying separately. Want to chat?"*

**Day 98** — Sarah replies: "Tell me more." Conversation moves to front desk → Alex offers a free PT trial session. Sarah books it.

**Day 100** — She has the PT session. Loves it. Upgrades to Premium that evening. Stripe charges $149.

**What fires:**

| System | Action |
|---|---|
| Stripe webhook | Subscription updated → `tier-basic` removed, `tier-premium` added, `monthly_rate` = $149 |
| `#06` workflow | Detects upgrade → `upsell-converted-basic-premium` tag, `total_upsell_conversions` += 1 |
| Pipeline | Retention opportunity value updates: $79*12 → $149*12 |
| `#05` engagement score | Boost +10 (upsell conversion is a strong engagement signal) → score now 89 |
| Owner notification | "🎉 Sarah upgraded Basic → Premium ($70/mo MRR lift)" |

---

## Day 105 — Review Ask (`#07`)

Sarah attends her first Premium-included PT session on Day 102. Killer session. `#07`'s post-PT review-ask workflow fires.

**Day 103, 11:00 AM** (delayed 24hr to land at peak-memory moment):

| System | Action |
|---|---|
| `#07` workflow | Email to Sarah: *"Sarah, hope yesterday's PT session was as good as it looked! 30 seconds for a quick rating? sunrise.studio/review"* |

Sarah taps. Smart Review Router funnel opens. She taps 😍 (5 stars).

| System | Action |
|---|---|
| Funnel branch | 5-star path → redirect to `{{custom_values.business.google_review_url}}` |
| Page 2 prompt | *"Thanks! Take 30 sec to share on Google so others can find us?"* |

Sarah leaves a Google review: *"Best decision I made this year. The PT sessions and morning HIIT are legit changing my life. Morgan and Alex actually care."*

**What fires:**

| System | Action |
|---|---|
| `#07` workflow | `review_submitted_date` = today, `review_star_rating` = 5, tag `review-submitted-google` |
| `#07` follow-up | Thank-you Email the next morning |
| `#08` workflow | 5-star reviewer + 100+ days member + tier-premium → `referral-prompt-ready` tag → eligible for next referral nudge |
| Owner notification | "📣 5-star Google review from Sarah Chen — go say thanks publicly" |

---

## Day 115 — Referral Loop (`#08`)

`#08` fires the referral-prompt Email to Sarah: *"Sarah ☀️ since you've been loving Sunrise — share your link with a friend. They get $20 off, you get a free PT session: sunrise.studio/r/SARAH-42"*

Sarah forwards the link to her coworker Diana.

**That evening** — Diana clicks the link. Lands on the Referral Landing Funnel — page shows *"Sarah sent you $20 off your first month at Sunrise Wellness Studio"*. Diana fills the form.

**What fires:**

| System | Action |
|---|---|
| `#01` workflow | New lead enters with `lead_source` = "Referral", `referred_by_contact_id` = Sarah's GHL ID, `referral_code_used` = "SARAH-42" |
| Tag applied | `source-referral` |
| Standard `#01` flow continues | Diana gets instant Email, books trial |
| `#08` workflow standby | Will fire reward credit when Diana converts |

**Day 122** — Diana converts to paid Basic Member after a 7-day trial (her own `#02` nurture).

**What fires:**

| System | Action |
|---|---|
| `#08` workflow trigger | Diana's `trial-converted` + `referred_by_contact_id` populated → Sarah gets credit |
| Sarah's contact | `pt_credit_balance` += 1, `referrals_converted_count` += 1, tag `campaign-referral-promoter` |
| Email to Sarah | *"Sarah! Diana just signed up — your free PT session is in the bank ☀️ Use it anytime: book.sunrisewellness.com"* |
| Email to Diana | *"Welcome to Sunrise, Diana ☀️ Sarah's a great friend to send your way — see you soon!"* |
| Owner notification | "Sarah Chen earned a referral reward (Diana Williams converted)" |

---

## Day 180 — At-Risk Save Test (`#05`)

Six months in. Sarah hits a rough patch — work stress, family stuff. Misses 3 weeks. Engagement score drops from 86 to 41.

**What fires:**

| System | Action |
|---|---|
| `#05` workflow | Score transition `risk-healthy` → `risk-watching` → `risk-at-risk` (over 2 weeks) |
| Pipeline | Retention → "At-Risk" stage |
| Save sequence | Personal email from Morgan: *"Sarah, just checking in. The studio misses you. No agenda — just want to make sure you're okay."* |

Sarah replies: "Thanks Morgan. Going through a tough month. Will be back next week."

**What fires:**

| System | Action |
|---|---|
| Tag applied | `retention-reply-received`, `save-at-risk-success-pending` |
| Pipeline | Retention → "Save In Progress" |

**Day 195** — Sarah returns. Attends 4 classes that week. Score recovers to 72.

**What fires:**

| System | Action |
|---|---|
| Tag transitions | `risk-at-risk` → `risk-watching` → `risk-healthy` over 2 weeks |
| Pipeline | Retention → "Saved" (Won) — opportunity closes positive |
| Tag applied | `member-saved` (badge — keeps for life) |

---

## Day 365 — One-Year Anniversary

`#10`'s nightly anniversary check fires:

| System | Action |
|---|---|
| Owner notification | "🎂 Sarah Chen — 1 year anniversary today. Total LTV $1,176. Total referrals: 1 (Diana). Send a card." |
| Tag applied | `anniversary-1yr` |

Morgan writes a handwritten note. Mails it.

---

## Day 730 — VIP Veteran Status

Two years in. Sarah hits `member-vip-veteran` tag threshold.

| System | Action |
|---|---|
| `#06` workflow | Anniversary-aware upsell — pitches VIP upgrade with a "you've earned it" angle |
| Tag applied | `member-vip-veteran` |

Sarah upgrades to VIP. $249/mo. `#10` flags her in the next Weekly Digest as a milestone moment.

---

## What If It Goes Wrong — The Cancellation Path

Hypothetical: at Day 400, Sarah moves to Chicago for work.

**Day 400** — Sarah submits the cancellation form (linked from the member portal). Reason: "Moved away."

**What fires:**

| System | Action |
|---|---|
| Cancellation workflow | `member-active` removed, `member-cancelled` tag applied, `membership_cancel_date` = today, `cancel_reason` = "Moved" |
| Pipeline | Retention → "Lost — Cancelled" |
| `#09` workflow trigger | Cancel event detected → branches on cancel_reason |
| Cancel-reason filter | "Moved" → suppress comeback offers (she literally can't come back) but send a warm goodbye |

**Day 400, 6 PM** — Day 1 goodbye email from Morgan: *"Sarah, we'll miss you. If Springfield ever pulls you back, your spot's here. Glow on."* No offer pitch.

**Day 430** — `#09` Day 30 check-in normally fires, but cancel_reason = "Moved" suppresses the offer-based touch and sends only a light *"Hi Sarah — hope Chicago's treating you well"* note.

If she'd cancelled for "Cost" or "Time" instead, the full Win-Back cascade (D30 check, D60 $39 offer, D90 last-call $29) would have fired.

---

## What Triggered When — System Touchpoint Log

| Day | System | Event | Outcome |
|---|---|---|---|
| 0 (7:42 PM) | `#01` | Form submitted | Lead in CRM, Email sent <60s |
| 0 (7:43 PM) | Booking | Intro consult booked | `#03` reminders scheduled |
| 2 | `#03` + `#02` | Pre-class reminder + trial nurture begins | Sarah arrives, attends |
| 5 (Day 5 of trial) | `#02` | Conversion offer emails | Sarah considers |
| 6 | `#02` | Personal-touch Email from owner | Sarah replies, books call |
| 6 (5 PM) | Payment | Converts to Basic ($63) | `#02` exits, `#04` enrolls |
| 7 | `#04` | Welcome email + onboarding starts | Sarah in Onboarding pipeline |
| 14, 21, 28, 30 | `#04` | Onboarding cadence | Sarah graduates Healthy |
| 28 | `#03` | No-show recovery (1 missed class) | Sarah rebooks next day |
| 70 | `#05` | Score drops, Watching | Light check-in Email, Sarah replies |
| 80 | `#05` | Recovered to Healthy | Pipeline back to Healthy |
| 95 | `#06` | Basic→Premium upsell triggered | Email sent |
| 100 | `#06` | Sarah upgrades | `tier-premium`, MRR +$70/mo |
| 103 | `#07` | Post-PT review ask | 5-star, Google review left |
| 115 | `#08` | Referral prompt Email | Sarah shares link with Diana |
| 122 | `#08` | Diana converts | Sarah gets PT credit |
| 180 | `#05` | At-risk save sequence | Sarah recovers, `member-saved` |
| 365 | `#10` | Anniversary alert | Owner sends handwritten card |
| 730 | `#06` | VIP upgrade pitch | Sarah upgrades to VIP |

**Total touchpoints to Sarah over 2 years:** 47 automated messages, plus 6 direct owner interventions. Owner labor: roughly 15 minutes of direct attention spread across the entire 2-year relationship.

**Sarah's outcome:** 2-year retention, Basic → Premium → VIP, 1 successful referral, 5-star Google review, brand promoter.

**Sarah's lifetime value to date:** $79 (first month discount) + $79 × 2 + $149 × 18 + $249 × 4 = **$3,815** plus the LTV of her 1 referral (~$1,100) = **~$4,900 total.** Plus brand value of her Google review.

---

## The Integration Test (use this on your build)

After building all 10 systems, take a test contact and walk them through this exact scenario over a compressed timeline (use shortened wait durations in test versions of workflows). At each transition above, verify:

- ✅ The expected tag is applied
- ✅ The expected pipeline stage is reached
- ✅ The expected message is sent
- ✅ No duplicate triggers fire
- ✅ Opt-outs are respected (test by adding `do-not-email` mid-scenario)

If every transition happens automatically with zero manual intervention, the engine is wired correctly.

---

## Related Files

- **[master-automation-graph.md](master-automation-graph.md)** — visual of all the handoffs above.
- **[build-order.md](build-order.md)** — how to assemble the engine.
- **[../diagrams/customer-journey.md](../diagrams/customer-journey.md)** — Sarah's path on the lifecycle map.
- **[../diagrams/revenue-impact.md](../diagrams/revenue-impact.md)** — the math behind Sarah's $4,900 contribution.
