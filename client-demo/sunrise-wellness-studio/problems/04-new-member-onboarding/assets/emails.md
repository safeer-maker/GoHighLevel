# #04 — Email Templates

> Six emails across the 30-day onboarding series. Tier-conditional sections (Basic/Premium/VIP). Goal-conditional sections (Lose Weight / Build Muscle / etc.). Paste into GHL with If/Else blocks.

---

## Email 1 — Day 0 — Welcome to the Studio

**Template name:** `04 — Day 0 — Welcome to the Studio`

**Send timing:** Within 5 minutes of `member-onboarding` tag added.

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> Welcome to the studio, {{contact.first_name}} ☀️

**Preview text:**
> Your member portal, your app, your first-class link — all below.

---

### Email Body

**Header band:** Sunrise gradient (coral → gold). Logo. "MEMBER" badge.

---

**[Hero image]** — Wide shot of the studio at peak class hour, full and energetic.

---

**Greeting (H1):**

> Hey {{contact.first_name}} — welcome to the team.

**Body:**

> I'm Morgan. You'll see me at the front desk most mornings, and you'll hear from me a few times over the next 30 days as you settle in.
>
> Here's what I want you to focus on this first week: **show up once.** That's it. Don't plan a 5-day program. Don't research the perfect routine. Pick one class that fits your week and walk through the door. The system you're building takes care of itself after that.

---

**CTA button (large coral, centered):**

> **Book My First Class →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Sub-section: Everything you need in one place**

**H2:** Your member dashboard

| Resource | Link |
|---|---|
| **Member portal** (book classes, manage billing) | [{{custom_values.business.short_name}} portal] |
| **Member app** | [iOS] · [Android] |
| **Class schedule** (this week) | [Schedule] |
| **Member-only Facebook group** | [Join] |
| **First-time guide** (parking, lockers, what to bring) | [First-time guide] |

---

**Sub-section: Tier-specific (conditional on `membership_tier`)**

**If Basic:**

> **Your Basic membership includes:**
> - Unlimited group classes (HIIT, Yoga, Pilates, Strength, Recovery)
> - Open gym + functional training floor access
> - App + member portal
> - Monthly member community events
>
> Want to add a one-time PT session or nutrition consult? They're available à la carte (PT $85, nutrition consult $50) — or upgrade to Premium anytime.

**If Premium:**

> **Your Premium membership includes:**
> - Everything in Basic
> - **2 PT sessions / month** — I'd book your first one this week, it's the fastest way to dial in your form and your plan
> - **One nutrition starter consult** — included on signup; book it whenever you're ready
> - 72hr advance class booking (vs Basic's 48hr)
> - 10% off retail and add-ons
>
> CTA: **[Book My First PT Session →](booking link to PT calendar)**

**If VIP:**

> **Your VIP membership includes:**
> - Everything in Premium PLUS:
> - **Unlimited PT** (book as much as your trainer's calendar holds)
> - **Monthly nutrition coaching session** (recurring)
> - **Recovery suite** (sauna, cold plunge, massage gun) — unlimited
> - **2 guest passes / month** (bring a friend)
> - **Quarterly InBody scan**
> - 20% off retail and add-ons
>
> CTA: **[Book My First VIP PT Session →]** · **[Book Recovery Suite →]**

---

**Sub-section: Based on your goal**

> You told us your primary goal is **{{contact.fitness_goal_primary}}**. Here's where I'd start:

**If Lose Weight:**

> - Aim for 3 sessions in week 1: 2 HIIT or Strength + 1 Yoga (recovery matters).
> - Book your nutrition consult by day 14 — diet drives 60% of weight outcomes.
> - Expect the scale to be flat for 2-3 weeks while your body recomposes. Don't quit at week 3.

**If Build Muscle:**

> - Strength Lab is your home — 3x/week minimum if possible.
> - Book your first PT session early to set baseline numbers and form.
> - Sleep + protein matter as much as the lifting. Ask the trainer.

**If Manage Stress:**

> - Sunrise Flow Yoga + Recovery & Mobility = the magic combo.
> - Try the 6 AM class if your mornings allow — best mood ROI.
> - Recovery suite (VIP) or sauna (Premium add-on) compounds the effect.

**If Improve Fitness:**

> - Mix all five class types in your first 14 days. By Day 14 you'll know your favorites.
> - Track your sleep + energy alongside workouts.

**If Recover from Injury:**

> - Book a PT session before any group class — the trainer needs to see the movement first.
> - Sunrise Flow Yoga (gentle variant), Recovery & Mobility, and Pilates Reformer are your starting menu.
> - Pace, don't push. Healing is non-negotiable.

(Use If/Else logic in email template against `fitness_goal_primary`.)

---

**Sub-section: What I'm going to do for you over the next 30 days**

> Here's roughly what to expect from us:
>
> - **Tomorrow:** A short personal text from me to check you got everything.
> - **Day 7:** A friendly check-in email — how's it going?
> - **Day 14:** A milestone celebration — and a real review of how week 1-2 went.
> - **Day 21:** An invitation to book a 30-min goal review with {{contact.assigned_trainer}} (or me if you'd rather).
> - **Day 30:** Graduation — you're officially past the danger zone of "new member who never came back."
>
> Throughout: if you text {{custom_values.business.sms_number}} or reply to any email, a real person reads it within a few hours.

---

**Closing:**

> Welcome in. Glad you're here.
>
> — Morgan
>
> Morgan Riley · Owner & Head Coach, {{custom_values.business.name}}

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 2 — Day 7 — Week 1 Check-In

**Template name:** `04 — Day 7 — Week 1 Check-In`

**Send timing:** Day 7 of membership at 9 AM contact-local.

**From:** Same as Email 1.

**Subject (conditional on `visits_last_30_days`):**

- **If 1+ visits:** {{contact.first_name}}, how was week one?
- **If 0 visits:** {{contact.first_name}}, your first week — quick check

**Preview text:**
> Honest check-in, not a guilt trip. One question.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

---

**Block A — if 1+ visits:**

> You've been in! Saw your name on the class list. The hardest part — that first walk-through-the-door moment — is now behind you.
>
> Here's what I want to ask: **how was it?** What clicked, what felt off, anything you wish were different?
>
> Just hit reply — I read everything. Even one line helps.

---

**Block B — if 0 visits:**

> Week 1 is wrapping up and I haven't seen you on the floor yet. **No drama from me** — life is a thing.
>
> Here's the only thing I'd ask: was there a specific blocker?
>
> - Schedule didn't line up with class times?
> - Nervous about walking in solo?
> - The app/booking confused you?
> - Something else entirely?
>
> Hit reply with one word and I'll respond with whatever's useful. (Or just send "fine" and I'll know to back off.)

---

**Sub-section (both versions): Most-popular classes this week**

> If you haven't found your favorite yet, the most-loved classes in the last 30 days at the studio:
>
> - **{{custom_values.class.hiit}}** — Mon/Wed/Fri 6 AM & 5:30 PM
> - **{{custom_values.class.yoga}}** — Tue/Thu 7 AM, Sat 9 AM
> - **{{custom_values.class.strength}}** — Mon/Wed 6:30 AM & 6 PM
>
> Whichever feels closest to your goal of **{{contact.fitness_goal_primary}}** — book one.

**CTA button (coral):**

> **Book a Class →**

---

**Sub-section: Tier-specific (conditional)**

**If Premium / VIP and `last_pt_session_date` is empty:**

> Quick reminder — your membership includes PT sessions and you haven't used one yet. {{contact.assigned_trainer}} is holding time for you. Tap below to grab one:
>
> **[Book My First PT Session →]({{custom_values.business.booking_url}})**

**If Premium / VIP and `nutrition_starter` not booked:**

> Your nutrition starter consult is also included — 45 min with Sam Rivera, our nutritionist. Most members do this in week 2-3.
>
> **[Book Nutrition Consult →]**

---

**Closing:**

> Thanks for the first week.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 3 — Day 14 — Two-Week Milestone (Healthy version, 3+ visits)

**Template name:** `04 — Day 14 — Two-Week Milestone`

**Send timing:** Day 14 of membership at 8 AM contact-local. IF `visits_last_30_days >= 3`.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, two weeks in — let's talk about it ☀️

**Preview text:**
> You're past the early-quitter zone. Here's what changes from here.

---

### Email Body

**[Hero image]** — Members high-fiving after class.

---

**Greeting (H1):**

> {{contact.first_name}} — two weeks. That's not nothing.

**Body:**

> Quick stats from your first two weeks:
>
> - **Visits:** {{contact.visits_last_30_days}}
> - **Last class:** {{contact.last_class_attended}}
> - **Days since join:** 14
>
> Most new members who hit 3+ classes by day 14 stay for **at least a year**. That's not a marketing line — it's the actual pattern in our data. You're now in that group.

---

**Sub-section: What changes in weeks 3-4**

> Weeks 3-4 are when the early novelty wears off and real consistency starts. A few things that help:
>
> 1. **Pick your two non-negotiable days.** Treat them like meetings. The members who do this stick.
> 2. **Try one new class type** you haven't done yet. Variety = adherence.
> 3. **Book your goal review** — it's coming up in week 3. (Email Day 21 will remind you, no pressure today.)
> 4. **Note what your body feels like** at week 4 vs week 1. Subtle, but it's real.

---

**Sub-section: Tier-conditional**

**If Basic AND visits_last_30_days >= 5:**

> Quick honest thought: you're attending a lot. **5+ visits in 2 weeks** is Premium-tier behavior. Premium adds 2 PT sessions/month + a nutrition consult, which would probably 2x the impact of your current routine.
>
> No pressure — just want you to know it's available. **[See Premium →](link to upsell info)**

**If Premium AND last_pt_session_date is empty:**

> Heads up — you're 2 weeks in and haven't used a PT session yet. They don't roll over forever (they re-stock monthly). Book one this week:
>
> **[Book PT with {{contact.assigned_trainer}} →]**

**If VIP:**

> You're on the flagship tier — make sure you're using the unlimited PT and recovery suite. If something's blocking you, reply and I'll fix it personally.

---

**Sub-section: Celebrate (literally)**

> Tonight after class: have the smoothie. Take the day off tomorrow. Sleep an extra hour. You earned the consistency.

---

**Closing:**

> See you on the floor.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 4 — Day 14 — At-Risk (zero visits)

**Template name:** `04 — Day 14 — At-Risk (zero visits)`

**Send timing:** Day 14 at 8 AM contact-local. IF `visits_last_30_days == 0`.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, an honest two-week check-in

**Preview text:**
> Not a sales email. Two real options.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Quick honest email. You're 14 days into your membership and haven't been able to make it in yet. I want to be straight with you about this because **I'd rather have an awkward conversation now than auto-renew you in 30 days for something you're not using.**
>
> Two real options:

---

**Option Block 1 (gold border):**

> **Option A: We figure out what's blocking you.**
>
> Hit reply with what's in the way (schedule, anxiety about walking in solo, life is wild right now, the gym is too far, whatever) and I'll personally help find a path. I've talked dozens of members through their stuck spot. Almost always solvable.

---

**Option Block 2 (gold border):**

> **Option B: We pause your membership.**
>
> You can pause up to 60 days/year, no fee, no awkwardness. Membership goes on hold; restart whenever life lets you. Reply with "pause" and I'll set it up.

---

**Sub-section: A third thing**

> If you've decided Sunrise just isn't the right fit — that's also fine. Email back "not for me" and I'll process a cancellation today, no questions, no win-back drips. We're not for everyone.

---

**Closing:**

> Whichever direction makes sense, the door's open.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 5 — Day 21 — Goal Review Invite

**Template name:** `04 — Day 21 — Goal Review Invite`

**Send timing:** Day 21 of membership at 9 AM contact-local.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, your 30-min goal review is open

**Preview text:**
> The session that turns "I'm a member" into "I have a plan."

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> You're three weeks in. This is the moment when most members shift from "trying things" to "running a plan."
>
> I want to invite you to a **30-minute goal review** with {{contact.assigned_trainer}} (or me if you'd rather). It's not a sales call — it's literally just:
>
> 1. What's working so far?
> 2. What's not?
> 3. What do you want the next 90 days to look like?
>
> Most members leave with a clear weekly schedule, one form fix, and one nutrition tweak. That's it.

---

**CTA button (coral):**

> **Book My Goal Review →**

(Links to the Goal Review calendar — 30-min slots with {{contact.assigned_trainer}} or Morgan)

---

**Sub-section: What we'll talk about (so it's not mysterious)**

| Topic | Why |
|---|---|
| Your stated goal: **{{contact.fitness_goal_primary}}** | Confirming this is still the right north star |
| Last 3 weeks of attendance + class types | Pattern recognition — what to lean into, what to drop |
| Form fixes | Most members have 1 movement that's worth correcting |
| Nutrition direction | Even 1 tweak compounds over months |
| The next 90-day plan | Specific classes, specific PT cadence, specific milestones |

---

**Sub-section: Tier-conditional callout**

**If Basic:**

> If we identify that your goal would be massively accelerated by PT or nutrition coaching, we'll talk about whether Premium makes sense for you. No pressure either way — most Basic members stay Basic happily forever.

**If Premium / VIP:**

> Bring your most recent PT notes if you have them. We'll fold those into the plan.

---

**Closing:**

> 30 minutes, real plan, no fluff.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 6 — Day 30 — Graduation

**Template name:** `04 — Day 30 — Graduation`

**Send timing:** Day 30 of membership at 10 AM contact-local.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, you made 30 days ☀️

**Preview text:**
> The early-quitter zone is officially behind you. Here's what's next.

---

### Email Body

**Header band:** Sunrise gradient. Gold "30 DAYS" badge.

---

**Greeting (H1):**

> {{contact.first_name}}, one month in. Look at you.

**Body:**

> 30 days is the line in the sand. **70% of new members who don't make it past Day 30 are gone by Day 90.** You're not them.
>
> Your numbers at Day 30:
>
> - **Total visits:** {{contact.total_visits_lifetime}}
> - **Last visit:** {{contact.last_visit_date}}
> - **Days as member:** 30
> - **Tier:** {{contact.membership_tier}}

---

**Sub-section: What changes from here**

> A few things shift after Day 30:
>
> 1. **You're past the early-quitter danger zone.** You can stop overthinking attendance and start optimizing for results.
> 2. **You'll hear from us less.** No more weekly check-ins — you graduated. We'll touch base at the right moments (PT session bookings, milestone celebrations, the occasional studio update).
> 3. **You become part of the community.** Member events, referral perks, the rest.

---

**Sub-section: Tier-conditional next-step**

**If Basic AND `total_visits_lifetime >= 12`:**

> One real observation: you've attended **12+ times in 30 days** — that's serious commitment. At that frequency, Premium ($149/mo) becomes interesting because the 2 PT sessions + nutrition consult would amplify what you're already doing.
>
> Not a hard pitch — just an honest "you might love this." **[Compare tiers →](link to upgrade page)**

**If Basic AND visits 6-11:**

> You're at a healthy class cadence. If you ever want to layer in PT or nutrition (à la carte or Premium upgrade), {{contact.assigned_trainer}} or I are happy to talk through it.

**If Basic AND visits 1-5:**

> Honest note: you're under-using the membership at this attendance level. Two paths: come more (we'd love that — reply and we'll find a schedule that sticks), or pause/cancel without drama. Both are fine.

**If Premium:**

> Your **2 PT sessions / month** restock monthly — don't let unused sessions stack up unused. {{contact.assigned_trainer}} can adjust cadence if you want more or fewer.
>
> If you're using everything Premium offers and want to go deeper — VIP unlocks unlimited PT + recovery suite. Reply if you want the comparison.

**If VIP:**

> You're on flagship tier. Make sure you're using:
> - **Unlimited PT** — book as many as your week allows
> - **Recovery suite** — most VIPs underuse this; 2x/week of sauna + cold plunge is the move
> - **Monthly nutrition** — your next session is coming up
> - **Guest passes** — bring a friend (2 free passes/month)
>
> Anything not landing for you? Reply and I'll personally fix it.

---

**Sub-section: One ask**

> If the first 30 days were good, **leave a Google review**. It's the single biggest help to a small studio. Takes 90 seconds:
>
> **[Leave a Google Review →]({{custom_values.business.google_review_url}})**
>
> (If anything was *not* good, hit reply instead. I want to know.)

(Note: this is a soft review-ask. The full review system is built in [#07 Reviews](../../07-reviews-and-reputation/).)

---

**Closing:**

> Welcome to the not-a-new-member-anymore club.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email-Building Notes

**Tone progression:**
- Day 0: warm welcome, clear expectations
- Day 7: honest check-in, not corporate
- Day 14 (healthy): celebration + slight tier-upsell on high engagement
- Day 14 (at-risk): radical honesty + real pause/cancel options
- Day 21: invitation, not pressure
- Day 30: graduation tone, congratulations, tier-appropriate next-step

**Conditional logic blocks:**
- Tier-conditional: Email 1, 2, 3, 6 — 3 branches each (Basic / Premium / VIP)
- Goal-conditional: Email 1 — 5 branches (Lose Weight / Build Muscle / Manage Stress / Improve Fitness / Recover from Injury)
- Visit-count-conditional: Email 2 subject line, Email 6 next-step block

Build these in GHL using template-level If/Else blocks against the relevant custom field.

**Personalization fallbacks:**
- `{{contact.first_name}}` → "there"
- `{{contact.assigned_trainer}}` → "one of our trainers"
- `{{contact.last_class_attended}}` → "your last class"
- `{{contact.visits_last_30_days}}` → "your recent visits"

**Mobile rendering:**
- Single column. CTAs ≥ 44px. Body 16px.
- Stats blocks (Day 14 and Day 30) need to render cleanly even when numbers are zero.

**Deliverability:**
- One emoji per subject max. ☀️ on Day 0, 14, 30. None on Day 7, 21.
- Day 14 at-risk email subject is the most spam-flag-prone — no "URGENT" type words, kept human.

---

## What Comes Next

After Day 30, the contact handoffs to **[#05 Retention](../../05-retention-and-churn-prevention/)** at the appropriate stage:
- 3+ visits → "Healthy"
- 1-2 visits → "Watching"
- 0 visits → "Critical" (Retention takes the save attempt)

SMS counterparts for each onboarding day live in **[sms.md](sms.md)**.

The complete workflow with branching logic in **[workflow.md](workflow.md)**.
