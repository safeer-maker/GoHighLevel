# Day 12: Automated Sales Pipeline

**Time Required:** 3-4 hours
**Combines:** Pipeline (D5) + Automation (D9) + Calendars (D4) + Conversations (D3) + Contacts (D2)
**Level:** Intermediate

---

## Today's Mission

Yesterday you built the lead capture system that gets people INTO the Membership Sales Pipeline. Every entry point -- funnel form, webchat, quick contact form, trigger link -- now feeds into the "New Inquiry" stage automatically. The front door works.

But what happens after they walk through that door?

Right now, nothing. A lead sits in "New Inquiry" until you manually notice them, send an outreach email, and drag their card to "Contacted." When they book a trial, you have to remember to move them to "Trial Booked." When the trial ends, you have to remember to follow up. When they sign up, you have to manually create an onboarding opportunity. Every stage transition depends on your memory and your availability -- and that means leads go cold while you are coaching a HIIT class or eating lunch.

Today you will automate what happens INSIDE the pipeline. When a lead moves from "New Inquiry" to "Contacted," an outreach sequence starts automatically. When they book a trial, the opportunity moves to "Trial Booked" without anyone touching it. When they complete the trial, a personalized conversion sequence fires based on their fitness goals. When they sign up, the opportunity marks as Won, a new opportunity is created in the Onboarding pipeline, and a congratulations email goes out -- all without you lifting a finger.

By the end of today, a lead can travel from "New Inquiry" all the way to "Closed - Member" and into onboarding with zero manual intervention. The pipeline manages itself.

---

## What You'll Combine

| Phase 1 Feature | Day Built | Role in Today's System |
|-----------------|-----------|----------------------|
| Membership Sales Pipeline | Day 5 | The structure being automated -- 7 stages from New Inquiry to Closed |
| Onboarding Pipeline | Day 5 | Receives handoff when a deal is Won |
| Automation Workflows | Day 9 | The engine driving every automatic action |
| Booking Calendars | Day 4 | Trial bookings trigger stage movement |
| SMS/Email Templates | Day 3 | Outreach, follow-up, and conversion messages |
| Contact Tags & Custom Fields | Day 2 | Personalization and conditional branching |
| Trigger Links | Day 7 | Interest signals inside emails that drive decisions |
| Coupons (TRIALCONVERT) | Day 6 | End-of-trial conversion incentive |

---

## The System Architecture

Study this diagram before you build anything. It shows every automation point in the pipeline and how workflows connect the stages. Each arrow labeled "AUTO" is something you will build today.

```
MEMBERSHIP SALES PIPELINE -- AUTOMATED
=======================================

[New Inquiry]
     |
     | AUTO: Day 11 lead capture system creates opportunity here
     |
     v
[Contacted] ──── AUTO: Outreach Sequence Workflow triggers
     |            - Personalized intro email (uses Fitness Goals from D2)
     |            - 24hr wait --> follow-up SMS with booking link
     |            - 48hr wait --> "Last chance to book your free trial" email
     |
     | AUTO: When appointment is booked (D4 calendar),
     |       opportunity moves here automatically
     v
[Trial Booked] ── AUTO: Trial Management Workflow triggers
     |             - Confirmation email with what-to-bring details
     |             - Day-before reminder SMS
     |
     | AUTO: When first session is attended,
     |       opportunity moves here automatically
     v
[Trial Active] ── AUTO: Trial Nurture sub-sequence
     |             - Day 1: "How was your first session?" SMS
     |             - Day 3: Midpoint check-in email + class schedule
     |             - Day 5: "2 days left!" + membership comparison
     |
     | AUTO: Day 6 of trial --> opportunity moves here automatically
     v
[Trial Follow-Up] ── AUTO: Conversion Workflow triggers
     |                 - Personalized offer by Fitness Goals tag
     |                 - TRIALCONVERT coupon (20% off first month)
     |                 - Day 1/2/3 escalation sequence
     |
     | AUTO: When payment received OR manual win
     v
[Closed - Member] ── AUTO: Pipeline Handoff triggers
     |                 - Tag: "active-member"
     |                 - Remove tag: "new-trial-lead"
     |                 - Congratulations email
     |                 - Create opportunity in Onboarding Pipeline
     |
     v
[New Member Onboarding Pipeline --> "Welcome" stage]


STALE DEAL DETECTION (runs parallel)
=====================================
Any opportunity with NO stage change for 7+ days:
  --> Internal notification to you
  --> Contact added to "Stale Leads" Smart List
  --> Re-engagement SMS: "Hey {{contact.first_name}}, still thinking
      about Sunrise Wellness?"
```

The key insight: **every stage transition either triggers an automation or IS triggered by an automation.** There is no gap where a lead can sit unattended. The pipeline becomes self-driving.

---

## Part 1: Map the Automation Points (30 min)

Before you build a single workflow, you need to plan. Jumping straight into the workflow builder without a map is how you end up with five overlapping automations that fire duplicate emails.

### Exercise 12.1: Pipeline Automation Blueprint

**Purpose:** Document exactly what happens at each stage so you can build workflows confidently without second-guessing what goes where.

Open a text file, spreadsheet, or notebook. Create a table with four columns for each of the seven pipeline stages. You are going to answer four questions for every stage:

1. **What triggers entry into this stage?** (How does an opportunity arrive here?)
2. **What auto-actions fire when an opportunity enters?** (What should GHL do immediately?)
3. **What ongoing actions happen while they are in this stage?** (Time-delayed follow-ups?)
4. **What triggers movement to the NEXT stage?** (What event or condition advances them?)

Fill in this blueprint:

| Stage | Entry Trigger | Auto-Actions on Entry | Ongoing Actions | Exit Trigger |
|-------|--------------|----------------------|-----------------|-------------|
| New Inquiry | Form submitted, webchat lead, or manual add (Day 11 system) | Welcome SMS + email already handled by Day 11 workflow | None -- Day 11 handles immediate follow-up | You manually move to Contacted after first outreach, OR auto-move after outreach sequence completes |
| Contacted | Manual move or auto-move after first outreach | Outreach Sequence starts: intro email, 24hr follow-up, 48hr booking push | 3-message sequence over 48 hours | Appointment booked on Trial calendar (auto-detect via calendar trigger) |
| Trial Booked | Calendar booking detected | Confirmation email, "What to Bring" SMS, add tag `trial-booked` | Day-before reminder SMS | First session attended (appointment status = "showed") |
| Trial Active | Appointment status changed to "showed" | "How was your first session?" SMS, add tag `trial-active` | Day 1/3/5/7 nurture emails | Day 6 of trial (time-based) or manual advance |
| Trial Follow-Up | Auto-move on Day 6, or manual move | Personalized conversion email based on Fitness Goals, TRIALCONVERT coupon | Day 1/2/3 escalation: email, SMS, "final offer" email | Payment received (auto) or manual win/loss |
| Closed - Member | Payment received or manual status change to Won | Tag `active-member`, remove `new-trial-lead`, congratulations email, create Onboarding opportunity | None -- they have left this pipeline's scope | N/A (terminal stage) |
| Closed - Not Now | Manual status change to Lost | Tag `closed-not-now`, add to "Re-Engage Later" Smart List, schedule 30-day re-engagement email | 30/60/90 day nurture sequence | If they re-engage, create a NEW opportunity back in New Inquiry |

> **Pro Tip:** Print this blueprint or keep it open in a second tab. Every workflow you build today will reference it. When you are deep in the workflow builder wondering "Wait, what am I supposed to do here?", this table is your answer.

**Self-Check:** Before moving on, review your blueprint and ask yourself:

- Does every stage have a clear entry trigger? (If not, leads will skip stages or get stuck.)
- Does every stage have at least one auto-action? (If not, that stage is just a label with no automation value.)
- Does every stage (except terminals) have an exit trigger? (If not, leads will pile up with no way forward.)
- Are there any gaps where a lead could sit for days with nothing happening? (If yes, add a time-based follow-up.)

---

## Part 2: Build the Outreach Sequence Workflow (45 min)

This is the first pipeline-stage workflow. It fires when an opportunity moves to "Contacted" and runs a 3-step outreach sequence designed to get the lead to book a free trial.

### Exercise 12.2: The Outreach Sequence

**Purpose:** Automate the initial sales outreach so every lead gets a consistent, well-timed sequence regardless of when they entered the pipeline or how busy you are.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Pipeline - Outreach Sequence (Contacted)"

**Step 1: Set the trigger**

```
[TRIGGER: Pipeline Stage Changed]
  Pipeline: Membership Sales
  Stage: Contacted
```

1. Click **Add New Workflow Trigger**
2. Select **Pipeline Stage Changed** (or "Opportunity Stage Changed" depending on your GHL version)
3. Configure:
   - Pipeline: Membership Sales
   - Stage moved TO: Contacted
4. This means: any time an opportunity enters the "Contacted" stage -- whether you dragged it manually or another workflow moved it -- this workflow fires

**Step 2: Add a condition to personalize by interest**

```
    |
    v
[CONDITION: If/Else -- Contact has custom field "Fitness Goals"]
  --> "Weight Loss": Branch A
  --> "Muscle Building": Branch B
  --> "General Fitness" / Other / Empty: Branch C
```

5. Add an **If/Else** action
6. Condition: Check the custom field "Fitness Goals" (from Day 2)
7. **Branch A (Weight Loss):** These leads get messaging focused on transformation results, body composition classes, and nutrition support
8. **Branch B (Muscle Building):** These leads get messaging focused on strength equipment, PT expertise, and progressive overload programming
9. **Branch C (General Fitness / Other / Empty):** These leads get the default messaging about the studio's welcoming atmosphere, class variety, and flexibility

> **Why personalize here?** A lead who told you they want to lose weight does not care about your powerlifting racks. A lead who wants to build muscle does not care about your yoga schedule. Using the data you already collected on Day 2 (via the form from Day 8) to personalize the first outreach dramatically increases booking rates. This is the whole reason you captured Fitness Goals as a custom field.

**Step 3: Build the email for each branch**

For each of the three branches, add a **Send Email** action. Here is the structure -- adapt the specific content to each fitness goal:

```
    |
    v
[ACTION: Send Email]
  Subject: "{{contact.first_name}}, your free trial at Sunrise Wellness is waiting"
  Body: Personalized by branch (see below)
```

**Branch A email body (Weight Loss focus):**
```
Hi {{contact.first_name}},

Thanks for your interest in Sunrise Wellness Studio! I noticed you're
focused on weight loss -- you're going to love what we offer.

Our members who come in with weight loss goals typically see results
within their first month, and here's why:

- Body Blast and HIIT classes designed specifically for fat loss
- Personalized nutrition consultations (included with Premium and VIP)
- A supportive community that keeps you accountable

I'd love to get you started with a free 7-day trial so you can
experience it firsthand. No commitment, no pressure -- just show up
and see how it feels.

Book your free trial here: {{calendar.trial-booking-link}}

Looking forward to meeting you!

{{user.first_name}}
Sunrise Wellness Studio
```

**Branch B email body (Muscle Building focus):**
```
Hi {{contact.first_name}},

Thanks for your interest in Sunrise Wellness Studio! I see you're
focused on building muscle -- you've found the right place.

Here's what sets us apart for strength training:

- Full free weight section with Olympic platforms
- Certified personal trainers specializing in hypertrophy programming
- HIIT and strength circuit classes to complement your lifting

I'd love to get you in for a free 7-day trial. You'll get full
access to every piece of equipment and every class on the schedule.

Book your free trial here: {{calendar.trial-booking-link}}

Let's get after it!

{{user.first_name}}
Sunrise Wellness Studio
```

**Branch C email body (General Fitness / Default):**
```
Hi {{contact.first_name}},

Thanks for reaching out to Sunrise Wellness Studio! We'd love to
show you around.

Whether you're into group classes, personal training, yoga, or just
need a welcoming gym to call home, we've got you covered:

- 30+ classes per week (HIIT, yoga, spin, strength, and more)
- Personal training with certified coaches
- Nutrition consultations for members who want guidance
- A community that actually cheers for each other

The best way to see if we're the right fit? Come in for a free
7-day trial. No commitment, no sales pitch -- just a chance to
try everything.

Book your free trial here: {{calendar.trial-booking-link}}

Hope to see you soon!

{{user.first_name}}
Sunrise Wellness Studio
```

10. Create these three email variations as templates first (navigate to **Marketing > Templates**, create them, then come back to the workflow and select the appropriate template in each branch)
11. After the email in each branch, the three branches should **merge back together** into a single path for the follow-up sequence

> **Access Note:** The merge field `{{calendar.trial-booking-link}}` may not exist in your sub-account. If not, replace it with a direct link to your Free Trial funnel page (the URL from Day 8/11). Alternatively, use a Custom Value (Day 1) to store the booking URL and reference it as `{{custom_values.trial_booking_link}}`.

**Step 4: Add the 24-hour follow-up SMS**

After the three branches merge:

```
    |
    v
[ACTION: Wait 24 hours]
    |
    v
[CONDITION: If/Else -- Has the contact booked an appointment?]
  --> YES: End workflow (they booked! The calendar trigger handles the rest)
  --> NO: Continue
    |
    v
[ACTION: Send SMS]
  "Hey {{contact.first_name}}! Just checking in -- did you get a
   chance to look at the free trial info I sent? You can book your
   7-day trial anytime here: [booking link]. No commitment, just
   come see the studio! - {{user.first_name}} at Sunrise Wellness"
```

12. Add a **Wait** action: 24 hours
13. Add an **If/Else** condition:
    - Check if the contact has an upcoming appointment on the Trial calendar (Day 4)
    - If you cannot check appointment status directly, check for the tag `trial-booked` as an alternative
    - **YES branch:** End the workflow. They already booked -- no need to follow up. Sending another message would feel pushy.
    - **NO branch:** Continue
14. Add **Send SMS** with the follow-up text above

**Step 5: Add the 48-hour final push email**

```
    |
    v
[ACTION: Wait 24 hours] (48 hours total since initial email)
    |
    v
[CONDITION: If/Else -- Has the contact booked an appointment?]
  --> YES: End workflow
  --> NO: Continue
    |
    v
[ACTION: Send Email]
  Subject: "Your free trial expires soon, {{contact.first_name}}"
  Body: (see below)
```

15. Add another **Wait** action: 24 hours (this is now 48 hours after the initial email)
16. Add another **If/Else** appointment check (same logic as step 13)
17. **YES:** End workflow
18. **NO:** Add **Send Email** with urgency messaging:

```
Hi {{contact.first_name}},

I wanted to follow up one more time -- your free 7-day trial offer
at Sunrise Wellness Studio is still available, but I don't want
you to miss out.

Here's what one of our recent trial members said:

"I was nervous about signing up anywhere, but the free trial
let me try everything without pressure. By day 3, I knew this
was my gym." -- Sarah W.

Book your trial here: [booking link]

If the timing isn't right, no worries at all. Just reply to this
email and let me know -- I'm happy to hold your spot for when
you're ready.

{{user.first_name}}
Sunrise Wellness Studio
```

19. **Save and Publish** the workflow

**Self-Check:** Open the workflow in the builder and trace the entire path from trigger to end. Ask yourself:
- Does every branch eventually lead to either an "End" or a "Send" action? (No dead ends.)
- Are the If/Else checks happening BEFORE the follow-ups? (You never want to send "did you book?" to someone who already booked.)
- Is the wait timing realistic? (24hr and 48hr gives the lead breathing room without losing momentum.)

---

## Part 3: Build the Trial Management Workflow (40 min)

This workflow handles the transition from "Contacted" to "Trial Booked" to "Trial Active" -- the entire trial experience from booking to completion.

### Exercise 12.3: Auto-Move on Booking + Trial Nurture Sequence

**Purpose:** When a lead books a trial appointment (on the Day 4 calendar), automatically advance their pipeline opportunity to "Trial Booked" and launch a nurture sequence that keeps them engaged through all 7 days of the trial.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Pipeline - Trial Management"

**Step 1: Trigger on appointment booking**

```
[TRIGGER: Appointment Booked]
  Calendar: Free Trial / PT Trial (whichever calendar you use for trials)
```

1. Click **Add New Workflow Trigger**
2. Select **Appointment Booked** (or "Calendar - Appointment Booked")
3. Filter to your trial-specific calendar from Day 4
4. This fires the moment someone books, regardless of how they booked (from the outreach email, the funnel, or a direct link)

**Step 2: Move the pipeline opportunity**

```
    |
    v
[ACTION: Update Opportunity]
  Pipeline: Membership Sales
  Move to Stage: Trial Booked
```

5. Add **Update Opportunity** (or "Move Opportunity" depending on GHL version)
6. Pipeline: Membership Sales
7. New Stage: Trial Booked
8. This is the key automation -- the opportunity card moves on the pipeline board automatically, without anyone dragging it

**Step 3: Tag and confirm**

```
    |
    v
[ACTION: Add Tag "trial-booked"]
    |
    v
[ACTION: Send Email]
  Subject: "You're booked! Here's what to bring to your trial"
  Body: (see below)
    |
    v
[ACTION: Send SMS]
  "Confirmed! Your free trial at Sunrise Wellness is booked for
   {{appointment.date}} at {{appointment.time}}. Bring: water bottle,
   towel, workout clothes, and a positive attitude! See you there.
   - {{user.first_name}}"
```

9. Add **Add Tag:** `trial-booked`
10. Add **Send Email:**

```
Subject: You're booked! Here's everything you need for your trial

Hi {{contact.first_name}},

Great news -- your free 7-day trial at Sunrise Wellness Studio is
officially booked!

APPOINTMENT DETAILS:
Date: {{appointment.date}}
Time: {{appointment.time}}
Location: [your studio address]

WHAT TO BRING:
- Water bottle (we have a refill station)
- Comfortable workout clothes and athletic shoes
- A towel (or grab one from the front desk)
- An open mind -- you're going to love it!

WHAT TO EXPECT:
When you arrive, check in at the front desk. We'll give you a
quick tour of the studio, introduce you to the team, and get you
set up for your first session. The whole thing takes about 15
minutes before your workout starts.

DURING YOUR 7-DAY TRIAL:
You'll have unlimited access to all classes and equipment. Here
are the most popular sessions to try:

- Morning HIIT (Mon/Wed/Fri at 6:30 AM) -- high energy, great
  for all levels
- Power Yoga (Tue/Thu at 7:00 PM) -- perfect for recovery days
- Strength Circuit (Sat at 9:00 AM) -- guided strength training

You can see the full schedule and book classes in advance here:
[class schedule link]

See you soon!

{{user.first_name}}
Sunrise Wellness Studio
```

11. Add **Send SMS** with the short confirmation text

**Step 4: Day-before reminder**

```
    |
    v
[ACTION: Wait until 1 day before appointment]
    |
    v
[ACTION: Send SMS]
  "Hey {{contact.first_name}}, just a reminder -- your free trial
   at Sunrise Wellness is tomorrow at {{appointment.time}}!
   Address: [studio address]. Free parking in the rear lot.
   Can't wait to meet you! - {{user.first_name}}"
```

12. Add a **Wait** action: Until 1 day before the appointment date/time
13. Add **Send SMS** with the reminder

> **Note:** If your GHL version does not support "Wait until X time before appointment," use a different approach: calculate the wait time based on when the booking was made. For example, if most people book 3-5 days out, a 2-day wait gets you close. The exact timing is less important than the fact that it happens automatically.

**Step 5: Post-first-session nurture (Days 1-7)**

This is where the workflow gets powerful. After their first session, you want to keep them engaged for the entire 7-day trial.

```
    |
    v
[WAIT: Until appointment date/time passes]
    |
    v
[ACTION: Update Opportunity]
  Move to Stage: Trial Active
    |
    v
[ACTION: Add Tag "trial-active"]
    |
    v
[ACTION: Remove Tag "trial-booked"]
```

14. Add a **Wait** action: Until after the appointment date/time
15. Add **Update Opportunity:** Move to "Trial Active" stage
16. Add **Add Tag:** `trial-active`
17. Add **Remove Tag:** `trial-booked` (keeps tags clean -- they are no longer "booked," they are "active")

Now add the nurture sequence:

```
    |
    v
[ACTION: Wait 4 hours after appointment]
    |
    v
[ACTION: Send SMS -- Day 1]
  "Hey {{contact.first_name}}! How was your first session at
   Sunrise Wellness? I'd love to hear what you thought!
   - {{user.first_name}}"
    |
    v
[ACTION: Wait until Day 3]
    |
    v
[ACTION: Send Email -- Day 3 Check-In]
  Subject: "How's your trial going, {{contact.first_name}}?"
  Body: Midpoint check-in + highlight classes they haven't tried
        + class schedule link
    |
    v
[ACTION: Wait until Day 5]
    |
    v
[ACTION: Send Email -- Day 5 Membership Preview]
  Subject: "Loving Sunrise Wellness? Let's make it official"
  Body: Membership tier comparison (Basic $79 / Premium $149 /
        VIP $249) + benefits breakdown + "Your trial ends in 2 days"
    |
    v
[ACTION: Wait until Day 7]
    |
    v
[ACTION: Send Email -- Day 7 Final + Coupon]
  Subject: "Last day of your trial + a special offer inside"
  Body: TRIALCONVERT coupon (20% off first month from Day 6) +
        urgency ("Your access expires tonight") + direct
        membership signup link
    |
    v
[ACTION: Update Opportunity]
  Move to Stage: Trial Follow-Up
```

18. Add the Day 1 SMS (wait 4 hours after the appointment, then send)
19. Add the Day 3 email (wait until 2 days after the Day 1 SMS)
20. Add the Day 5 email (wait until 2 days after Day 3)
21. Add the Day 7 email with the **TRIALCONVERT** coupon code you created on Day 6

Here is the Day 7 email body:

```
Hi {{contact.first_name}},

Today is the last day of your free trial at Sunrise Wellness Studio.

I hope you had an incredible week! Whether you crushed a HIIT class,
found your zen in yoga, or pushed new limits in a PT session, I hope
you felt what makes this place special -- the community, the coaches,
and the energy.

Here's the good news: I have a special offer just for trial members.

USE CODE: TRIALCONVERT
GET: 20% off your first month of any membership

Here's what's available:

BASIC ($79/mo --> $63.20 with code)
- Unlimited gym access
- 10 group classes per month

PREMIUM ($149/mo --> $119.20 with code)
- Everything in Basic
- Unlimited group classes
- 2 PT sessions per month
- 1 nutrition consultation

VIP ($249/mo --> $199.20 with code)
- Everything in Premium
- Unlimited PT sessions
- Unlimited nutrition consultations
- Priority class booking

Choose your membership here: [membership signup link]

This offer expires in 48 hours. After that, standard pricing applies.

No matter what you decide, it was great having you this week.

{{user.first_name}}
Sunrise Wellness Studio
```

22. After the Day 7 email, add **Update Opportunity:** Move to "Trial Follow-Up" stage

23. **Save and Publish** the workflow

**Self-Check:** Count the touchpoints in this workflow. A single trial member should receive:
- 1 confirmation email + 1 confirmation SMS (booking)
- 1 reminder SMS (day before)
- 1 SMS (day 1 post-session)
- 3 emails (day 3, day 5, day 7)

That is 7 automated touchpoints across 7 days. Without this workflow, you would have to remember to send each one manually for every single trial member.

---

## Part 4: Build the Conversion Workflow (35 min)

The lead has finished their trial and sits in "Trial Follow-Up." This is the highest-stakes stage in the entire pipeline -- they have experienced the studio and now they need to decide. Your job is to make that decision easy.

### Exercise 12.4: Personalized Conversion Sequence

**Purpose:** Deliver a targeted 3-day conversion sequence that matches the lead's fitness goals, creating urgency without being pushy.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Pipeline - Conversion Sequence (Trial Follow-Up)"

**Step 1: Trigger on stage entry**

```
[TRIGGER: Pipeline Stage Changed]
  Pipeline: Membership Sales
  Stage moved TO: Trial Follow-Up
```

1. Set the trigger to fire when an opportunity enters the "Trial Follow-Up" stage

**Step 2: Branch by fitness goal for personalized offer**

```
    |
    v
[CONDITION: If/Else -- Contact custom field "Fitness Goals"]
  --> "Weight Loss": Recommend Premium ($149)
  --> "Muscle Building": Recommend VIP ($249)
  --> Other / Empty: Recommend Basic ($79) as entry point
```

2. Add an **If/Else** condition on the "Fitness Goals" custom field
3. The logic: different goals align with different membership tiers:
   - **Weight Loss** leads benefit most from Premium because it includes nutrition consultations and unlimited classes -- both critical for weight loss
   - **Muscle Building** leads benefit most from VIP because it includes unlimited PT sessions -- essential for progressive strength programming
   - **General Fitness** leads may not need the premium features yet, so Basic is a lower-friction entry point

**Step 3: Day 1 -- The personalized recommendation email**

For each branch, add a **Send Email** tailored to their goal:

**Weight Loss branch:**
```
Subject: The membership built for your weight loss goals

Hi {{contact.first_name}},

Over the past 7 days, I've watched you put in the work at Sunrise
Wellness -- and I'm impressed. You showed up, you pushed yourself,
and now I want to help you keep that momentum going.

Based on your goals, I'd recommend our PREMIUM membership ($149/mo):

Why Premium is perfect for weight loss:
- UNLIMITED group classes (Body Blast, HIIT, and Spin are your best
  friends for fat loss)
- 2 PT sessions/month (your trainer will build a program around YOUR
  body and YOUR goals)
- 1 nutrition consultation/month (exercise is only half the equation
  -- nutrition is the other half)

And remember, your trial member code TRIALCONVERT gets you 20% off
your first month: just $119.20 to get started.

Ready to keep going? Sign up here: [Premium signup link]

Or reply to this email if you have any questions. I'm here to help.

{{user.first_name}}
Sunrise Wellness Studio
```

**Muscle Building branch:**
```
Subject: Ready to build serious muscle? Here's your next step

Hi {{contact.first_name}},

I saw you in the weight room this week and I can tell -- you know
what you're doing. The question is: do you want to do it alone, or
do you want a certified strength coach programming your workouts,
tracking your progress, and pushing you past plateaus?

Based on your goals, I'd recommend our VIP membership ($249/mo):

Why VIP is built for muscle building:
- UNLIMITED personal training (a new program every 4-6 weeks,
  periodized for progressive overload)
- UNLIMITED nutrition consultations (you can't build muscle in a
  deficit -- let's get your macros dialed in)
- Priority class booking (never miss Strength Circuit Saturday)
- Full access to every piece of equipment, every class, every coach

Your trial code TRIALCONVERT gets you 20% off month one: $199.20.

Let's build something: [VIP signup link]

{{user.first_name}}
Sunrise Wellness Studio
```

**General / Default branch:**
```
Subject: Keep the momentum going, {{contact.first_name}}

Hi {{contact.first_name}},

Your 7-day trial at Sunrise Wellness is wrapping up, and I hope
you enjoyed it as much as we enjoyed having you.

If you're ready to keep going, our BASIC membership is the easiest
way to start:

BASIC ($79/mo):
- Unlimited gym access (open 5 AM to 10 PM daily)
- 10 group classes per month
- Access to locker rooms, showers, and the smoothie bar

And you can always upgrade later if you want personal training,
nutrition coaching, or unlimited classes.

Your trial code TRIALCONVERT saves you 20% on month one: $63.20.

Join here: [Basic signup link]

Not sure which plan is right? Reply and I'll help you figure it out.

{{user.first_name}}
Sunrise Wellness Studio
```

4. After all three branches merge back together, continue with the escalation sequence

**Step 4: Day 2 -- SMS nudge**

```
    |
    v
[ACTION: Wait 24 hours]
    |
    v
[CONDITION: If/Else -- Opportunity status = Won?]
  --> YES: End workflow (they already signed up!)
  --> NO: Continue
    |
    v
[ACTION: Send SMS]
  "Hi {{contact.first_name}}, just checking in! Your TRIALCONVERT
   code (20% off) expires tomorrow. Any questions about memberships?
   I'm happy to hop on a quick call. - {{user.first_name}}"
```

5. Add **Wait:** 24 hours
6. Add **If/Else:** Check if the opportunity status is already "Won" (they may have signed up after the Day 1 email)
7. **YES:** End workflow
8. **NO:** Send the SMS

**Step 5: Day 3 -- Final offer email**

```
    |
    v
[ACTION: Wait 24 hours]
    |
    v
[CONDITION: If/Else -- Opportunity status = Won?]
  --> YES: End workflow
  --> NO: Continue
    |
    v
[ACTION: Send Email]
  Subject: "Last chance: your 20% off expires tonight"
  Body: Final urgency + social proof + direct signup link +
        "If now isn't the right time, no hard feelings"
```

9. Add **Wait:** 24 hours
10. Add **If/Else:** Check opportunity status again
11. **YES:** End
12. **NO:** Send the final email:

```
Hi {{contact.first_name}},

This is my last email about your trial -- I promise.

Your TRIALCONVERT code (20% off your first month) expires tonight
at midnight. After that, standard pricing kicks in.

Here's what other trial members have said:

"I almost didn't sign up, and now I can't imagine my week without
Sunrise Wellness." -- James R.

"The free trial sold me. The community kept me." -- Ana M.

If you're ready: [membership signup link]

If now isn't the right time, I completely understand. Your contact
info is saved, and you're always welcome to come back when the
timing is better. Just reply to this email or text us anytime.

All the best,

{{user.first_name}}
Sunrise Wellness Studio
```

13. **Save and Publish** the workflow

> **Pro Tip:** Notice the tone shift across the three days. Day 1 is helpful and informative. Day 2 is a casual check-in. Day 3 acknowledges the pressure and gives them an out. This progression builds urgency without being aggressive -- critical for a wellness brand where trust matters more than hard selling.

---

## Part 5: Pipeline-to-Pipeline Handoff (30 min)

This is the automation that connects your two pipelines. When an opportunity is Won in the Membership Sales pipeline, it should automatically create a new opportunity in the New Member Onboarding pipeline -- so the new member immediately enters the onboarding process without any manual data entry.

### Exercise 12.5: The Handoff Workflow

**Purpose:** Eliminate the gap between "they signed up" and "we started onboarding them." Every new member enters the onboarding pipeline within seconds of their deal being marked Won.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Pipeline - Sales to Onboarding Handoff"

```
[TRIGGER: Opportunity Status Changed]
  Pipeline: Membership Sales
  Status: Won
    |
    v
[ACTION: Add Tag "active-member"]
    |
    v
[ACTION: Remove Tag "new-trial-lead"]
    |
    v
[ACTION: Remove Tag "trial-active"]
    |
    v
[ACTION: Remove Tag "trial-booked"]
    |
    v
[ACTION: Send Email]
  Subject: "Welcome to the Sunrise Wellness family!"
  Body: (see below)
    |
    v
[ACTION: Create Opportunity]
  Pipeline: New Member Onboarding
  Stage: Welcome
  Name: "{{contact.first_name}} {{contact.last_name}} - Onboarding"
  Value: (match the membership value from the won opportunity)
    |
    v
[ACTION: Internal Notification]
  "NEW MEMBER: {{contact.first_name}} {{contact.last_name}} just
   signed up! Onboarding opportunity created. Next step: schedule
   their orientation session."
```

Build it:

1. **Trigger:** Opportunity Status Changed --> Pipeline: Membership Sales --> Status: Won
2. **Add Tag:** `active-member` (this tag will be used across multiple systems to identify paying members)
3. **Remove Tags:** `new-trial-lead`, `trial-active`, `trial-booked` (clean up all prospecting tags -- they are no longer a prospect, they are a member)
4. **Send Email -- Congratulations:**

```
Subject: Welcome to the Sunrise Wellness family, {{contact.first_name}}!

Hi {{contact.first_name}},

IT'S OFFICIAL! You are now a member of Sunrise Wellness Studio,
and we could not be more excited to have you.

Here's what happens next:

1. ORIENTATION SESSION: You'll receive a booking link shortly to
   schedule your studio orientation. This is a 30-minute session
   where we'll:
   - Set up your member profile
   - Walk through the full class schedule
   - Set your initial fitness goals with a trainer
   - Answer any questions you have

2. MEMBER APP ACCESS: Download the Sunrise Wellness app to:
   - Book classes in advance
   - Track your workout history
   - Connect with other members

3. YOUR FIRST MONTH: Here are my top 3 tips for getting the most
   out of your membership:
   - Try at least 3 different class types in your first 2 weeks
   - Book your sessions in advance (popular classes fill up!)
   - Introduce yourself to the coaches -- they're here for YOU

Welcome aboard. This is going to be great.

{{user.first_name}}
Sunrise Wellness Studio
```

5. **Create Opportunity** in the New Member Onboarding pipeline:
   - Pipeline: New Member Onboarding
   - Stage: Welcome
   - Opportunity Name: "{{contact.first_name}} {{contact.last_name}} - Onboarding"
   - Value: Use the same value as the won opportunity if possible, or set a default (e.g., $149 for the average membership)

6. **Internal Notification:** Alert yourself (or the front desk) that a new member needs onboarding attention

7. **Save and Publish** the workflow

**Self-Check:** Think through edge cases before moving on:
- What if someone's opportunity is marked Won by accident? (The onboarding opportunity is created, but you can delete it. Consider adding a confirmation step if this is a concern.)
- What if the same contact has multiple opportunities? (GHL handles this per-opportunity, so only the Won opportunity triggers the workflow.)
- What about "Closed - Not Now" deals? (That is a Lost status, not Won, so this workflow does not fire. You could build a separate workflow for Lost deals if you want.)

---

## Part 6: Stale Deal Detection (20 min)

Every sales pipeline has deals that go quiet. A lead who was enthusiastic last week stops responding. An opportunity sits in "Contacted" for 10 days because you forgot about it. Without a system to catch these, they slip through the cracks forever.

### Exercise 12.6: The Stale Deal Alert System

**Purpose:** Automatically identify opportunities that have not moved stages in 7 days and trigger re-engagement actions so no deal is ever forgotten.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Pipeline - Stale Deal Alert"

There are two approaches to building this. Choose whichever your GHL version supports:

**Approach A: Stage-based time trigger**

```
[TRIGGER: Pipeline Stage Changed]
  Pipeline: Membership Sales
  Stage: Any stage EXCEPT "Closed - Member" and "Closed - Not Now"
    |
    v
[ACTION: Wait 7 days]
    |
    v
[CONDITION: If/Else -- Is the opportunity STILL in the same stage?]
  --> YES (stale): Continue to alerts
  --> NO (moved): End workflow (they progressed, not stale)
```

1. Trigger on any stage change in the Membership Sales pipeline (excluding closed stages)
2. Wait 7 days
3. Check if the opportunity is still in the same stage it was when the workflow triggered. If the contact's current pipeline stage matches the stage that triggered this workflow, the deal is stale. If they have moved, they are fine.

**Approach B: Recurring check with Smart List**

If your GHL version does not support the "check current stage" condition easily, use a Smart List approach:

1. Create a **Smart List** called "Stale Pipeline Leads":
   - Filter: Opportunity status = Open
   - AND: Opportunity last stage change date is more than 7 days ago
   - AND: Pipeline = Membership Sales
2. Set up a recurring workflow that checks this Smart List daily and sends notifications for any matches

> **Access Note:** The exact implementation depends on what conditions your GHL version exposes. If neither approach works perfectly, a simpler version is: trigger on stage entry, wait 7 days, and send the alert regardless. You will get some false positives (deals that moved on day 6), but catching stale deals imperfectly is better than not catching them at all.

**Alert actions (for either approach):**

```
    |
    v
[ACTION: Internal Notification]
  Subject: "STALE DEAL: {{contact.first_name}} has not moved in 7 days"
  Body: "{{contact.first_name}} {{contact.last_name}} has been in
        the [current stage] stage for 7+ days. Pipeline: Membership
        Sales. Value: [deal value]. Take action now."
    |
    v
[ACTION: Add Tag "stale-lead"]
    |
    v
[ACTION: Send SMS]
  "Hey {{contact.first_name}}, it's {{user.first_name}} from
   Sunrise Wellness! I wanted to check in -- are you still
   interested in giving the studio a try? No pressure, just
   wanted to make sure I didn't lose touch. Let me know!"
```

4. **Internal Notification:** Alerts you to take action
5. **Add Tag:** `stale-lead` (this tag feeds the Smart List for pipeline reporting)
6. **Send SMS:** A casual, no-pressure re-engagement message

7. **Save and Publish** the workflow

> **Pro Tip:** The 7-day threshold is a starting point. After running this for a month, review the data. If most of your successful conversions happen within 5 days of entering a stage, tighten the alert to 5 days. If your sales cycle is longer (like a dental clinic or agency), extend it to 10-14 days. Let the data guide you.

---

## Part 7: End-to-End Test (30 min)

You have built five workflows today. Now you need to prove they work together as a single system. You will walk one test contact through the entire pipeline from "New Inquiry" to "Closed - Member" and into the Onboarding pipeline.

### Exercise 12.7: Full Pipeline Walkthrough

**Purpose:** Verify that every workflow triggers correctly, every stage transition fires the right automation, and the pipeline-to-pipeline handoff works end to end.

**Important:** This test involves triggering real workflows that send real emails and SMS messages. Use your own email and phone number so you can verify each message arrives.

**Step 1: Prepare your test environment**

Open four browser tabs:
1. **Contacts** -- to watch tags and fields change
2. **Opportunities > Membership Sales Pipeline** -- to watch the opportunity move
3. **Opportunities > New Member Onboarding Pipeline** -- to watch the handoff
4. **Automation > Workflows** -- to watch workflow execution logs

**Step 2: Create a test contact and opportunity**

1. Create a new contact:
   - Name: Test PipelineAuto
   - Email: Your real email
   - Phone: Your real phone
   - Custom field "Fitness Goals": Weight Loss
   - Tag: `new-trial-lead`
2. Create a new opportunity in the Membership Sales pipeline:
   - Name: "Test PipelineAuto - Premium Interest"
   - Contact: Test PipelineAuto
   - Stage: New Inquiry
   - Value: $149

**Step 3: Trigger the Outreach Sequence**

1. Move the opportunity from "New Inquiry" to "Contacted" (drag the card or edit the opportunity)
2. Watch the "Pipeline - Outreach Sequence" workflow:
   - Did it trigger? (Check the workflow execution log)
   - Did you receive the personalized email? (It should be the Weight Loss version since you set Fitness Goals = Weight Loss)
3. **Do NOT wait 24/48 hours for the follow-ups.** For testing purposes, either:
   - Temporarily edit the workflow to change the waits to 1 minute each, run the test, then change them back
   - Or simply verify the first email arrives and trust the wait/send pattern works (the logic is the same, just time-delayed)

**Step 4: Trigger the Trial Management**

1. Book an appointment on your Trial calendar for the test contact (simulate what would happen when a lead clicks the booking link in the outreach email)
2. Watch the "Pipeline - Trial Management" workflow:
   - Did the opportunity automatically move to "Trial Booked"? (Check the Membership Sales pipeline)
   - Did you receive the confirmation email and SMS?
   - Did the `trial-booked` tag appear on the contact?

**Step 5: Simulate the trial completion**

1. Since you cannot wait 7 real days, manually advance:
   - Move the opportunity to "Trial Active" (or let the workflow do it if you set the appointment time to the past)
   - Then move it to "Trial Follow-Up"
2. Watch the "Pipeline - Conversion Sequence" workflow:
   - Did it trigger on the "Trial Follow-Up" stage entry?
   - Did you receive the personalized conversion email? (Should be the Premium recommendation since Fitness Goals = Weight Loss)

**Step 6: Trigger the handoff**

1. Change the opportunity status to **Won** (either from the opportunity detail screen or the pipeline settings)
2. Watch the "Pipeline - Sales to Onboarding Handoff" workflow:
   - Did the `active-member` tag appear on the contact?
   - Were the old tags (`new-trial-lead`, `trial-active`, `trial-booked`) removed?
   - Did you receive the congratulations email?
   - **Most importantly:** Switch to the New Member Onboarding pipeline tab. Is there a new opportunity for "Test PipelineAuto - Onboarding" in the "Welcome" stage?

**Step 7: Document results**

| Test Step | Expected Result | Actual Result | Pass/Fail |
|-----------|----------------|---------------|-----------|
| Move to Contacted | Outreach Sequence triggers, personalized email received | | |
| Book trial appointment | Opp moves to Trial Booked, confirmation email + SMS received | | |
| Appointment passes | Opp moves to Trial Active, Day 1 SMS received | | |
| Move to Trial Follow-Up | Conversion Sequence triggers, personalized offer received | | |
| Mark as Won | Tags updated, congrats email, Onboarding opp created | | |
| Check Onboarding pipeline | New opportunity exists in Welcome stage | | |

**If anything fails,** check these common issues:
- Is the workflow published? (Draft workflows do not fire.)
- Is the trigger configured for the correct pipeline and stage?
- Are the merge fields correct? (A typo in `{{contact.first_name}}` means no personalization.)
- Did a previous workflow already move the opportunity past the expected stage? (Race conditions between workflows.)

**Step 8: Clean up**

After testing, delete the test contact and both test opportunities so they do not pollute your pipeline data. Revert any temporary workflow changes (like 1-minute waits) back to their production values.

---

## Case Scenario 1: BrightSmile Dental -- Automated Patient Treatment Pipeline

**Situation:** BrightSmile Dental Clinic (2 dentists, 1 hygienist, 1 front desk person) built their Patient Treatment Pipeline on Day 5 with 8 stages: New Patient Inquiry, Consultation Scheduled, Exam Complete, Treatment Proposed, Treatment Accepted, In Treatment, Treatment Complete, and Declined. They also built an Insurance Claims Pipeline with 5 stages.

Right now, a patient calls to ask about teeth whitening. The front desk person creates an opportunity, books the consultation, and then... nothing happens automatically. The dentist finishes the exam and writes a treatment plan on paper. Someone has to remember to move the pipeline card. If the patient does not respond to the treatment proposal, nobody follows up until someone happens to glance at the pipeline board.

**Your Task:** Automate the entire Patient Treatment Pipeline using the same principles you applied to Sunrise Wellness.

**Part A: Map the automation points**

Create a blueprint table (like Exercise 12.1) for BrightSmile's pipeline:

| Stage | Entry Trigger | Auto-Actions | Exit Trigger |
|-------|--------------|-------------|-------------|
| New Patient Inquiry | Form submitted or phone call logged | Welcome email + "What to expect at your first visit" PDF attachment + internal notification to front desk | Consultation booked on dental calendar |
| Consultation Scheduled | Calendar booking detected | Auto-move opportunity, confirmation email with office address and "arrive 15 min early for paperwork," add tag `consult-booked` | Dentist marks exam complete in system |
| Exam Complete | Manual move by dentist or staff | Auto-trigger "Treatment Plan Builder" notification to dentist, patient receives "Your exam results are ready" email | Treatment plan sent to patient |
| Treatment Proposed | Manual move or auto after treatment plan is sent | Auto-send treatment plan email with cost breakdown, payment plan options for procedures over $500, follow-up sequence starts | Patient accepts or declines |
| Treatment Accepted | Patient confirms (via reply, form, or in-person -- manually moved) | Auto-trigger payment plan setup for procedures over $500, schedule first procedure, send pre-procedure instructions, add tag `treatment-active` | All procedures complete |
| In Treatment | First procedure scheduled or started | Appointment reminders for each visit, aftercare instructions after each procedure, next-visit scheduling prompts | Final procedure complete |
| Treatment Complete | All procedures finished (manual move) | Satisfaction survey, request Google review, schedule 6-month checkup reminder, add tag `treatment-complete` | N/A (terminal) |
| Declined | Patient declines treatment (manual move) | Add tag `treatment-declined`, 30-day follow-up email ("We understand, we're here when you're ready"), add to "Re-Engage" Smart List | Re-inquiry creates new opportunity |

**Part B: Build the critical workflows**

Build these three workflows for BrightSmile:

**Workflow 1: "Dental - Consultation to Treatment Proposal"**
```
[TRIGGER: Appointment Status Changed to "Showed" on Dental Consultation calendar]
    |
    v
[ACTION: Update Opportunity --> move to "Exam Complete"]
    |
    v
[ACTION: Wait 2 hours] (gives dentist time to write treatment plan)
    |
    v
[ACTION: Internal Notification]
  "Reminder: {{contact.first_name}}'s exam is done. Please enter
   the treatment plan so the proposal email can be sent."
    |
    v
[ACTION: Wait 24 hours]
    |
    v
[CONDITION: Has opportunity moved to "Treatment Proposed"?]
  --> YES: End
  --> NO: Send another internal reminder ("URGENT: treatment plan
          for {{contact.first_name}} still pending")
```

**Workflow 2: "Dental - Treatment Proposal Follow-Up"**
```
[TRIGGER: Pipeline Stage Changed --> Treatment Proposed]
    |
    v
[ACTION: Send Email]
  Subject: "Your treatment plan from BrightSmile Dental"
  Body: Procedure details + total cost + payment plan options
        for procedures over $500 (e.g., "$1,200 crown = $100/mo
        x 12 months, 0% interest") + "Reply to accept or call
        us with questions"
    |
    v
[ACTION: Wait 3 days]
    |
    v
[CONDITION: Still in "Treatment Proposed"?]
  --> YES: Send follow-up SMS
      "Hi {{contact.first_name}}, just checking in about your
       treatment plan from BrightSmile. Any questions I can
       answer? - Dr. [Name]'s office"
  --> NO: End
    |
    v
[ACTION: Wait 4 days] (7 days total)
    |
    v
[CONDITION: Still in "Treatment Proposed"?]
  --> YES: Send final email with urgency
      "We want to make sure you get the care you need. Your
       treatment plan is valid for 30 days. Call us at [phone]
       to discuss options."
  --> NO: End
```

**Workflow 3: "Dental - Payment Plan Auto-Setup"**
```
[TRIGGER: Pipeline Stage Changed --> Treatment Accepted]
    |
    v
[CONDITION: Opportunity value > $500?]
  --> YES: Send email with payment plan options + payment link
      "Hi {{contact.first_name}}, we've prepared flexible payment
       options for your [procedure]: [full pay / 3-month / 6-month
       / 12-month plan details]. Click here to select your plan
       and get started: [payment link]"
  --> NO: Send email with one-time payment link
      "Hi {{contact.first_name}}, here's the payment link for
       your upcoming [procedure]: [payment link]. You can pay
       before your visit or at the front desk."
    |
    v
[ACTION: Add Tag "treatment-active"]
    |
    v
[ACTION: Internal Notification]
  "{{contact.first_name}} accepted treatment ([procedure], [value]).
   Payment plan email sent. Schedule first procedure."
```

**Part C: Reflection questions**

1. BrightSmile's pipeline involves clinical decisions (exam results, treatment plans) that cannot be automated. How does this change your automation strategy compared to a purely sales-driven pipeline like Sunrise Wellness? (Think about this: you automate the COMMUNICATION and REMINDERS around clinical decisions, not the decisions themselves. The dentist still decides the treatment plan -- you just make sure it gets sent to the patient promptly and followed up on automatically.)

2. A patient might need 4-6 separate appointments for a full orthodontics treatment ($4,500). How do you track individual appointment attendance within a single pipeline opportunity? (The opportunity stays in "In Treatment" while individual appointments are tracked on the calendar. Each appointment triggers its own reminder workflow from Day 13's system.)

3. What happens to the Insurance Claims Pipeline when a treatment is accepted? Should the treatment pipeline trigger a new opportunity in the insurance pipeline? (Yes -- this is a pipeline-to-pipeline handoff, identical to the Sunrise Wellness Sales-to-Onboarding handoff. When treatment is accepted, auto-create an insurance claim opportunity in the Claims pipeline.)

---

## Case Scenario 2: Elevate Digital Agency -- Automated Client Acquisition Pipeline

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media, Email Marketing, Web Design) built their Client Acquisition Pipeline on Day 5 with 7 stages: Lead, Discovery Call Scheduled, Discovery Complete, Proposal Sent, Negotiation, Contract Signed, and Lost. They also built a Project Delivery Pipeline with 6 stages.

The agency's sales cycle is much longer than a fitness studio's. A lead might take 2-4 weeks to go from initial inquiry to signed contract. The deal values are $2,000-$10,000 per month in recurring retainer revenue, so every lost deal is expensive. Right now, the agency founder personally manages every deal, and three proposals are sitting unsent because she has been too busy with client work to write them.

**Your Task:** Automate the Client Acquisition Pipeline to reduce the founder's manual workload and ensure no deal gets stuck.

**Part A: Map the automation points**

| Stage | Entry Trigger | Auto-Actions | Exit Trigger |
|-------|--------------|-------------|-------------|
| Lead | Website form, LinkedIn outreach response, referral (manual add) | Welcome email acknowledging inquiry + intake questionnaire link + internal notification with lead details + add tag `agency-lead` | Discovery call booked on calendar |
| Discovery Call Scheduled | Calendar booking detected | Auto-move opportunity, confirmation email with "What to prepare for our strategy call" + meeting link, add tag `discovery-scheduled` | Discovery call completed (appointment status changed) |
| Discovery Complete | Appointment status = showed | Auto-move opportunity, internal notification "Discovery notes needed for {{contact.first_name}} -- proposal due in 48 hours," send thank-you email to prospect | Proposal sent (manual move or auto after proposal email) |
| Proposal Sent | Manual move after proposal is emailed | Auto-send "Your proposal from Elevate Digital" email with proposal document, start 3-day follow-up sequence, add tag `proposal-sent` | Prospect responds (positive to Negotiation, negative to Lost) |
| Negotiation | Manual move when prospect responds with questions or counteroffers | Internal notification "{{contact.first_name}} is in negotiation -- respond within 4 hours," add tag `negotiation-active` | Contract signed or deal lost |
| Contract Signed | Manual move or payment received | Tag `active-client`, congratulations email, create Project Delivery opportunity in "Kickoff" stage, internal notification "New client! Start onboarding." | N/A (terminal) |
| Lost - No Budget / Bad Fit | Manual move | Tag `agency-lost`, add to "Lost Leads" Smart List, 30/60/90 day re-engagement emails, remove active tags | Re-inquiry creates new opportunity |

**Part B: Build the critical workflows**

**Workflow 1: "Agency - Discovery Call Management"**
```
[TRIGGER: Appointment Booked on "Strategy Call" calendar]
    |
    v
[ACTION: Update Opportunity --> move to "Discovery Call Scheduled"]
    |
    v
[ACTION: Send Email]
  Subject: "Your strategy call with Elevate Digital is confirmed"
  Body: "Hi {{contact.first_name}}, looking forward to our call on
        {{appointment.date}} at {{appointment.time}}.

        To make the most of our 30 minutes, here's what I'd love
        you to think about beforehand:
        1. Your top 3 marketing goals for the next 12 months
        2. Your current monthly marketing budget (even a range helps)
        3. What's working and what isn't in your current marketing
        4. Your biggest competitor (we'll look them up before the call)

        Talk soon!
        [Founder Name], Elevate Digital"
    |
    v
[ACTION: Wait until 1 day before appointment]
    |
    v
[ACTION: Send SMS]
  "Quick reminder: our strategy call is tomorrow at
   {{appointment.time}}. Meeting link: [link]. Looking
   forward to it! - [Founder], Elevate Digital"
    |
    v
[WAIT: Until after appointment time]
    |
    v
[ACTION: Update Opportunity --> move to "Discovery Complete"]
    |
    v
[ACTION: Internal Notification]
  "Discovery call with {{contact.first_name}} complete.
   Enter notes and begin proposal. Target: send proposal
   within 48 hours."
    |
    v
[ACTION: Send Email to prospect]
  Subject: "Great talking with you, {{contact.first_name}}"
  Body: "Thanks for taking the time today. I've got a clear
        picture of what you need, and I'm excited about the
        possibilities. I'll have a custom proposal in your
        inbox within 48 hours. In the meantime, feel free to
        reply with anything else you'd like me to consider."
```

**Workflow 2: "Agency - Proposal Follow-Up Sequence"**
```
[TRIGGER: Pipeline Stage Changed --> Proposal Sent]
    |
    v
[ACTION: Wait 3 days]
    |
    v
[CONDITION: Still in "Proposal Sent"?]
  --> Moved: End
  --> Still here: Continue
    |
    v
[ACTION: Send Email]
  Subject: "Thoughts on the proposal, {{contact.first_name}}?"
  Body: "Hi {{contact.first_name}}, just wanted to check in on the
        proposal I sent over. I know it's a lot to digest, so I
        wanted to offer a few options:

        1. QUICK CALL: If you have questions, let's jump on a
           15-minute call: [booking link]
        2. EMAIL: Reply to this email with any questions
        3. NOT RIGHT NOW: No hard feelings -- just let me know and
           I'll follow up in a few months

        The proposal is valid for 30 days."
    |
    v
[ACTION: Wait 4 days] (7 days total)
    |
    v
[CONDITION: Still in "Proposal Sent"?]
  --> Moved: End
  --> Still here: Continue
    |
    v
[ACTION: Send SMS]
  "Hey {{contact.first_name}}, wanted to make sure you received the
   Elevate Digital proposal. Any questions? Happy to jump on a quick
   call. - [Founder]"
    |
    v
[ACTION: Wait 7 days] (14 days total)
    |
    v
[CONDITION: Still in "Proposal Sent"?]
  --> Moved: End
  --> Still here: Continue
    |
    v
[ACTION: Send Email -- Final]
  Subject: "Closing the loop on your proposal"
  Body: "Hi {{contact.first_name}}, I want to respect your time, so
        this will be my last follow-up on the proposal. If you'd like
        to move forward, the proposal is valid for another 16 days.
        If the timing isn't right, I completely understand -- I'll
        check back in 3 months to see if things have changed.
        Either way, it was great connecting with you."
    |
    v
[ACTION: Add Tag "proposal-no-response"]
    |
    v
[ACTION: Internal Notification]
  "{{contact.first_name}} has not responded to proposal in 14 days.
   Consider calling directly or moving to Lost."
```

**Workflow 3: "Agency - Client Onboarding Handoff"**
```
[TRIGGER: Opportunity Status Changed --> Won, Pipeline: Client Acquisition]
    |
    v
[ACTION: Add Tag "active-client"]
    |
    v
[ACTION: Remove Tags: "agency-lead", "discovery-scheduled",
         "proposal-sent", "negotiation-active"]
    |
    v
[ACTION: Send Email]
  Subject: "Welcome to Elevate Digital, {{contact.first_name}}!"
  Body: "The contract is signed and we are officially partners!

        Here's what happens in the next 7 days:

        1. KICKOFF CALL: You'll receive a booking link within 24
           hours to schedule our kickoff meeting
        2. ACCESS SETUP: We'll need login credentials for your
           current marketing platforms (Google Ads, Meta, Analytics,
           etc.) -- I'll send a secure form for that
        3. STRATEGY DOCUMENT: Within 5 business days, you'll receive
           a comprehensive strategy document for your approval
        4. LAUNCH: Once you approve the strategy, we go live

        Your dedicated account manager is [Name]. They'll be your
        primary contact from here on out.

        Excited to get started!

        [Founder Name]
        Elevate Digital"
    |
    v
[ACTION: Create Opportunity]
  Pipeline: Project Delivery
  Stage: Kickoff
  Name: "{{contact.first_name}} - [Service Type] Delivery"
  Value: [match contract value]
    |
    v
[ACTION: Internal Notification]
  "NEW CLIENT: {{contact.first_name}} signed! Contract value:
   [value]/mo. Create project in PM tool. Schedule kickoff call.
   Assign account manager."
```

**Part C: Reflection questions**

1. Agency deals can sit in "Negotiation" for weeks as terms go back and forth. How would you set the stale deal alert threshold differently for Elevate Digital versus Sunrise Wellness? (For the fitness studio, 7 days is stale. For an agency, 14 days in Negotiation might be normal. Set thresholds per-stage: 5 days for Lead, 3 days for Discovery Complete, 14 days for Proposal Sent, 14 days for Negotiation.)

2. Elevate Digital's proposals are custom documents that take 2-8 hours to write. The "Proposal Sent" auto-email assumes the proposal is ready. How would you handle the gap between "Discovery Complete" and "Proposal Sent" without the founder forgetting? (Add an internal reminder workflow: trigger on "Discovery Complete," wait 24 hours, send internal notification "Proposal for {{contact.first_name}} is due in 24 hours." Wait another 24 hours, send urgent reminder. This does not automate the proposal writing -- it automates the accountability.)

3. A retainer client paying $5,000/mo is worth $60,000/year. How does this change how aggressively you follow up compared to a $79/mo gym membership? (Higher value = more personal touchpoints. Instead of only automated emails, the agency should trigger tasks for personal phone calls at key stages. The automation handles the administrative follow-up; the human handles the relationship.)

---

## Integration Checkpoint

Before moving to tomorrow's lesson, verify that your pipeline automation system is complete and functional:

**Workflows built today:**

| # | Workflow Name | Trigger | Status |
|---|-------------|---------|--------|
| 1 | Pipeline - Outreach Sequence (Contacted) | Opp moves to Contacted | Published? |
| 2 | Pipeline - Trial Management | Appointment booked on Trial calendar | Published? |
| 3 | Pipeline - Conversion Sequence (Trial Follow-Up) | Opp moves to Trial Follow-Up | Published? |
| 4 | Pipeline - Sales to Onboarding Handoff | Opp status changed to Won | Published? |
| 5 | Pipeline - Stale Deal Alert | Opp enters any non-closed stage | Published? |

**Connections verified:**

- [ ] Moving an opportunity to "Contacted" triggers personalized outreach
- [ ] Booking a trial appointment auto-moves the opportunity to "Trial Booked"
- [ ] The trial nurture sequence sends messages on Days 1, 3, 5, and 7
- [ ] Day 7 email includes the TRIALCONVERT coupon from Day 6
- [ ] Moving to "Trial Follow-Up" triggers a personalized conversion sequence based on Fitness Goals
- [ ] Marking an opportunity as Won creates an Onboarding pipeline opportunity
- [ ] Tags are updated correctly at each transition (added and removed)
- [ ] Stale deals trigger internal notifications after 7 days

**System integration with Day 11:**

- [ ] Day 11's lead capture system creates opportunities in "New Inquiry"
- [ ] Today's outreach sequence picks up when those opportunities move to "Contacted"
- [ ] There are no duplicate workflows firing (Day 11 handles entry, Day 12 handles progression)

---

## Day 12 Recap Questions

1. Why is it important to check "has the contact already booked?" before sending follow-up messages in the Outreach Sequence? What would happen if you skipped that check?

2. The Conversion Sequence recommends different membership tiers based on Fitness Goals. Why recommend Premium for Weight Loss and VIP for Muscle Building instead of always pushing the most expensive tier?

3. Explain the pipeline-to-pipeline handoff in your own words. What problem does it solve, and what would happen without it?

4. The Stale Deal Alert uses a 7-day threshold. Name two situations where you would change that number, and in which direction.

5. You built 5 workflows today. In what order do they fire for a lead who goes from New Inquiry all the way to Closed - Member? List the workflow name and what triggers each one.

6. A lead enters "Trial Follow-Up" but never responds to the 3-day conversion sequence. What happens to their opportunity? What should happen? (Hint: think about whether any of today's workflows handle this scenario, and what you might add.)

---

## Next Day Preview

**Day 13: Complete Appointment-Based Business System** -- Today you automated the pipeline. Tomorrow you automate the appointments. You will build the complete appointment lifecycle: booking confirmation, 24-hour and 1-hour reminders, post-session invoicing via Text2Pay, no-show rebooking sequences, and automated Google review requests. By the end of Day 13, a member can book a session, attend it, pay for it, and leave a review -- all triggered by a single calendar booking.

Make sure you have:
- All 5 workflows published and tested
- The end-to-end test (Exercise 12.7) completed with documented results
- Both case scenarios thought through (you do not need to build everything, but the planning is essential)
- A clear understanding of how pipeline stage triggers, opportunity status changes, and calendar events work together
