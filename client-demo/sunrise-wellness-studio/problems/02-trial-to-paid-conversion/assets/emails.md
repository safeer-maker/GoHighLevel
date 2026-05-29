# #02 — Email Templates

> Production-ready email copy for the 7-day trial nurture. Each email has subject, preview text, full body, and merge fields. Paste into GHL email builder.

---

## Email 1 — Day 0 — Trial Welcome

**Template name:** `02 — Day 0 — Trial Welcome`

**Send timing:** Within 5 minutes of `trial-claimed` tag being applied.

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> Your 7 days at Sunrise start now, {{contact.first_name}} ☀️

**Preview text:**
> Welcome to the studio. Here's how to make the most of every day.

---

### Email Body

**Header band:** Sunrise gradient (coral → gold). White logo. Small caps "SUNRISE WELLNESS STUDIO".

---

**[Hero image]** — Wide shot of a class mid-flow, members smiling.

---

**Greeting (H1, deep slate):**

> Hey {{contact.first_name}} —

**Body:**

> Welcome to Sunrise. I'm Morgan — the owner here — and I'm honestly thrilled you're trying us out.
>
> Your 7-day pass is now active. Here's the only thing I want you to do in the next 60 seconds: book your first class. The hardest part of any trial is the first walk-through-the-door moment. Once that's done, the rest is easy.

---

**CTA button (large, coral, centered):**

> **Book My First Class →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Sub-section: A 7-day plan I'd suggest**

**H2:** Here's what I'd do this week if I were you.

| Day | What to do |
|---|---|
| **Day 1** | Take any class that fits your schedule. Just show up. Front desk will get you set up. |
| **Day 2** | Try a different class type — if Day 1 was HIIT, do Yoga. If it was Yoga, try Strength. |
| **Day 3** | Book your free 30-min intro consult with one of our trainers. |
| **Day 4-5** | Hit the open gym floor solo. See how the equipment feels. |
| **Day 6-7** | Repeat your favorite class from earlier in the week. By now you know which one. |

> You don't have to follow this exactly — but if you do 3 classes by Day 5, you'll know whether Sunrise is the right home for you.

---

**Sub-section: Based on your goal**

> You told us your goal is **{{contact.fitness_goal_primary}}** — here's where I'd start.
>
> - **If you said Lose Weight:** Stack 2 HIIT sessions + 1 Strength + the free intro consult. Real results take ~6 weeks; the trial gives you the spark.
> - **If you said Build Muscle:** Strength Lab is your home. Bring the consult convo around progressive overload.
> - **If you said Manage Stress:** Sunrise Flow Yoga + a Recovery & Mobility session = different week.
> - **If you said Improve Fitness:** Mix everything. The trial is built for this.

(Note: this section uses If/Else logic in the email template — show only the matching block.)

---

**Sub-section: Practical stuff**

> A few things that'll save you time:
>
> - **Address:** {{custom_values.business.address_line}}
> - **Hours:** {{custom_values.hours.full}}
> - **Bring:** Workout clothes, sneakers, water bottle, towel. We have showers, lockers, mat rentals.
> - **First time:** Arrive 10 minutes early so we can show you around.
> - **Assigned trainer for your consult:** {{contact.assigned_trainer}} (or any available trainer at consult time)

---

**Closing:**

> If anything's confusing — text us at {{custom_values.business.sms_number}} or reply to this email. A real person reads everything.
>
> Excited to see you on the floor this week.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 2 — Day 2 — First Class Encouragement

**Template name:** `02 — Day 2 — First Class Encouragement`

**Send timing:** Day 2 of trial at 8 AM contact-local.

**From:** Same as Email 1.

**Subject (dynamic — show ONE based on attendance):**

- **If `last_visit_date` exists AND >= `lead_captured_at`:**
  > {{contact.first_name}}, loved having you on the floor ☀️
- **If `last_visit_date` is blank or < `lead_captured_at`:**
  > {{contact.first_name}}, your first class doesn't have to be perfect

**Preview text (dynamic):**

- Attended: "Here's what to do next."
- Not attended: "Walking in the first time is the hardest part. Here's what to expect."

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

---

**Conditional Block A (show if attended ≥1 class):**

> Saw your name on the class list yesterday — thanks for showing up. The first one is always the most intimidating; you got past it.
>
> Here's what I'd do next: while the momentum is fresh, book one more class for this week. Same time of day if it worked. Different class type if you want to mix it up.

**CTA button (coral):**
> **Book My Next Class →**

> If you have a few minutes, also book your **free 30-min intro consult** — it's the quickest way to dial your trial into your actual goals.

---

**Conditional Block B (show if NOT attended yet):**

> Quick check — your trial is on Day 2, and I haven't seen you on the floor yet. **Totally normal.** Walking into a new studio the first time is the single hardest part of any trial.
>
> Here's exactly what happens when you walk in:
>
> 1. You're greeted at the front desk (probably by me or Taylor). We say hi, ask if you've been before, and walk you to wherever you're going.
> 2. We give you the 60-second studio tour — locker rooms, water, the floor, the studio.
> 3. We introduce you to your instructor before class. They'll know you're new.
> 4. You take the class at whatever level feels right. Modifications offered for everything.
> 5. After class you head out, or you grab a coffee in the lounge, or you book the next thing. No pressure.
>
> That's it. No initiation ritual. No spotlight.

**CTA button:**
> **Pick a Class Time →**

> Reply to this email if there's something specific keeping you from booking — injury, schedule conflict, nervous about the vibe — anything. I'd rather know and help.

---

**Sub-section (both versions): A short note from someone who was once where you are**

> *"I almost didn't show up for my first class. I was sure everyone there would already know each other and I'd be the weird new one. Within five minutes that was wrong. By week two I was asking the trainer how to scale a movement. By month three I'd dropped 12 pounds. Just go to one class."*
>
> — **Priya M., member since 2024**

---

**Closing:**

> Whatever you decide — I'm here.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 3 — Day 4 — Testimonial / Social Proof

**Template name:** `02 — Day 4 — Testimonial / Social Proof`

**Send timing:** Day 4 of trial at 9 AM contact-local.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, what people don't tell you about the first month

**Preview text:**
> Three real stories from members. The pattern surprised us.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> You're halfway through your trial. By now you've either fallen in love or you're on the fence.
>
> Most people we ask say the same thing: *"I had no idea how much the consistency of just showing up 3x a week would change my mood, my sleep, and my energy."* Not the dramatic weight-loss story — that comes later. The first thing that changes is mood.
>
> Three real stories from members who started exactly where you are.

---

**Testimonial 1:**

> **Priya M. — member since 2024**
>
> *"I had a desk job that was wrecking my back. I thought I needed a gym. What I actually needed was a studio with a trainer who'd watch my form. Six weeks in, the back pain is mostly gone. I haven't lost weight on the scale — but my whole posture has changed. People keep asking what's different."*

---

**Testimonial 2:**

> **Marcus T. — member since 2023**
>
> *"I'd tried four gyms in two years. Lost interest by month two every time. This was the first place where the trainers learned my name AND my goals AND remembered both. I've now been here 18 months. Down 22 pounds, but more importantly I lift more now than I did at 25."*

---

**Testimonial 3:**

> **Diane K. — member since 2024**
>
> *"After my knee surgery I thought I was done with fitness. The recovery program here — slow strength work, mobility, the trainer modifying every movement for me — got me to where I'm running again at 58. I cried after my first 1-mile run. That's the kind of place this is."*

---

**Sub-section: What's actually included**

> Just so the math is concrete — at any tier, you get:
>
> - **Basic ({{custom_values.price.basic}}/mo):** unlimited group classes + open gym
> - **Premium ({{custom_values.price.premium}}/mo):** Basic + 2 PT/mo + nutrition starter consult
> - **VIP ({{custom_values.price.vip}}/mo):** unlimited PT + monthly nutrition + recovery suite + guest passes
>
> Most people start on Basic. About 1 in 4 upgrade within 3 months because the PT/nutrition piece is hard to pass up once you've tried it.

---

**CTA button (coral):**

> **See the Conversion Offer →**

(Links to `{{custom_values.offer.conversion_funnel_url}}` — the funnel from Step 1 of build.md)

> P.S. The conversion offer drops tomorrow — {{custom_values.offer.trial_conversion_discount}}. Just a heads up so you can plan around it.

---

**Closing:**

> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 4 — Day 5 — Conversion Offer (the big one)

**Template name:** `02 — Day 5 — Conversion Offer`

**Send timing:** Day 5 of trial at 10 AM contact-local.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, your member rate is ready ☀️

**Preview text:**
> 20% off first month + waived enrollment. 48 hours only.

---

### Email Body

**Header band:** Sunrise gradient.

---

**[Hero image]** — Bright photo of the studio at peak hours, full and energetic.

---

**Greeting (H1):**

> Hey {{contact.first_name}} —

**Body:**

> Your trial ends in 2 days. Whatever you've decided, I want to make the math easy.
>
> Here's the offer I'd give you in person if you stopped me on the way out of class:

---

**Offer Block (large, gold border, centered):**

> **{{custom_values.offer.trial_conversion_discount}}**
>
> Use code **TRIAL2PAID** at checkout. Valid for 48 hours.
>
> Applies to Basic, Premium, or VIP — your choice.

---

**3-Tier Comparison Table:**

| Tier | Your member rate | What you get |
|---|---|---|
| **Basic** | **$63.20** first month, then $79/mo | Unlimited classes + open gym |
| **Premium** | **$119.20** first month, then $149/mo | Basic + 2 PT/mo + nutrition consult |
| **VIP** | **$199.20** first month, then $249/mo | Unlimited PT + monthly nutrition + recovery suite |

> Enrollment fee ($49) is waived for all three. Cancel anytime — month-to-month, no contract.

---

**CTA button (large coral):**

> **Lock In My Membership →**

(Links to `{{custom_values.offer.conversion_funnel_url}}`)

---

**Sub-section: Why this offer expires**

> Quick honest note — this isn't a fake-urgency trick. The reason the offer expires 48 hours after your trial wraps is that **trial-to-paid conversion is what keeps the studio's lights on**. We can give you a real discount as a trial-converter that we can't give as a permanent rate. Hence the window.
>
> If life is in the way and you need a few more days — reply to this email and I'll extend the code for you personally. No questions.

---

**Sub-section: FAQ**

| Question | Answer |
|---|---|
| Can I switch tiers later? | Yes — anytime. Upgrade or downgrade with a single email. |
| Can I pause if I travel? | Yes — pause up to 60 days/year, no fee. |
| What if I don't use it? | Cancel anytime. We'd rather you stay because it's working than out of guilt. |
| Is the offer different for the higher tiers? | Same 20% off + waived enrollment — just applied to a bigger base. The VIP discount is larger in absolute dollars. |
| Can I bring a friend on the offer? | Refer them after you join — they get $20 off, you get a free PT session. (See [our referral page](../08-referral-engine/).) |

---

**Closing:**

> Whatever you decide, thank you for trying us this week. It genuinely means something to me when someone walks through our door.
>
> — Morgan
>
> P.S. If you've been doing the math — at {{custom_values.price.basic}}/mo, Sunrise costs less per day than the average coffee. That's never the reason to join, but it's worth a second look if cost is the hesitation.

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 5 — Day 7 — Last Call

**Template name:** `02 — Day 7 — Last Call`

**Send timing:** Day 7 of trial at 9 AM contact-local.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, last call (no pressure — just a heads up)

**Preview text:**
> Your trial ends tonight. Here's the last reminder.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Quick last note — your trial ends tonight at midnight, and the **TRIAL2PAID** code expires with it.
>
> I'm not going to keep emailing about it after today. If you've decided Sunrise isn't for you, that's totally fine — just hit reply with "not now" and I'll stop the nudges. (Your info stays in our system if you change your mind months from now.)
>
> If you've been on the fence — here's the offer one more time:

---

**Offer Block (compact):**

> **{{custom_values.offer.trial_conversion_discount}}**
> Code: **TRIAL2PAID** — expires tonight at midnight.

---

**CTA button (coral):**

> **Lock In My Membership →**

(Links to `{{custom_values.offer.conversion_funnel_url}}`)

---

**Sub-section: What you can do in the last 12 hours**

> If you want to squeeze one more class in today — here's what's still open:
>
> - **6 PM Sunrise HIIT** — usually has spots until 4 PM
> - **7 PM Sunrise Flow Yoga** — open
> - **Open gym** — until 9 PM
>
> [Book a final trial class →]({{custom_values.business.booking_url}})

---

**Closing:**

> Whatever you decide tonight, thanks for spending the week with us.
>
> — Morgan
>
> P.S. If you want to convert but the timing's bad this week (paycheck, travel, whatever) — reply and I'll extend the offer by a week. Just ask.

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 6 — Day 8 — Recap / Soft Goodbye

**Template name:** `02 — Recap — Trial Expired (Soft)`

**Send timing:** Day 8 (12 hours after Day 7 last-call Email), IF contact has `trial-expired` AND NOT `trial-converted` AND NOT `trial-not-now`.

**From:** Same as Email 1.

**Subject:**
> Your Sunrise trial wrapped — quick note

**Preview text:**
> No pressure email. Just want you to know our door's still open.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Your 7-day pass wrapped last night. I didn't see you convert — and that's completely OK.
>
> I'm not going to chase you with weekly emails. We're not that studio.
>
> Here's what I want you to know:
>
> - **You can come back anytime.** Your info stays in our system. If you walk in 6 months from now, we already have your goals, your preferred classes, and a record of which trainer you clicked with.
> - **If timing was the issue** — money, schedule, an injury, life — just reply with a one-word answer and I'll know what to send when the timing's right. Examples: "$" / "schedule" / "injury" / "later".
> - **If we weren't the right fit** — that's also fine. We're not for everyone, and we'd rather you find your right place than feel guilted into ours. If you have one piece of feedback, I'd love to hear it. One line is enough.

---

**Sub-section: Stay in touch (low-key)**

> If you want occasional updates — new classes, seasonal challenges, the rare studio event — you're already on our list. We send roughly one email a month, never spammy. You can unsubscribe with one click below.

---

**Closing:**

> Thanks for the week. It mattered.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email-Building Notes

**Tone calibration:**
- First-person owner voice throughout. Morgan is the brand.
- Acknowledge resistance instead of pretending it doesn't exist (Day 2 "totally normal," Day 5 "honest note," Day 8 "we're not that studio").
- Offer real exits ("not now," "extend the code"). Soft language outperforms hard urgency for this audience.

**Conditional logic in templates:**
- Email 2 has two version blocks based on `last_visit_date`. Use GHL's "If/Else block" in the email builder, not duplicate templates.
- Email 1 has a goal-specific block driven by `fitness_goal_primary`. Same mechanism.

**Mobile rendering:**
- Single column. CTA buttons ≥ 44px tall.
- Body font 16px. Headlines 22-28px.
- Header image max 600px wide.

**Deliverability:**
- One emoji per subject line max. Sunrise ☀️ is the brand emoji.
- Verify SPF/DKIM/DMARC on the sending domain.
- Avoid "FREE!", "ACT NOW!", excessive caps — Day 5 conversion email is the most spam-flag-prone; keep clean.

**Personalization fallbacks:**
- `{{contact.first_name}}` → "there"
- `{{contact.fitness_goal_primary}}` → "your goal" (skip the goal-specific block)
- `{{contact.assigned_trainer}}` → "one of our trainers"

---

## What Comes Next

After Day 7, the contact takes one of three paths:

1. **Converted** → handed off to [#04 New Member Onboarding](../04-new-member-onboarding/), which runs its own 30-day welcome sequence.
2. **Not Now** → enters the long-tail nurture (monthly cadence, out of scope here).
3. **Silent expiration** → gets this Email 6 recap, then enters the long-tail nurture.

The Email counterparts for each day live in **[]()**.
