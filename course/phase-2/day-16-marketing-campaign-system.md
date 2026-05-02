# Day 16: Complete Marketing Campaign System

**Time Required:** 3-4 hours
**Combines:** Marketing/Email (D7) + Contacts/Smart Lists (D2) + Automation (D9) + Sites/Funnels (D8) + Reporting (D10) + Trigger Links (D7)
**Level:** Intermediate to Advanced

---

## Today's Mission

Your lead capture system (Day 11) gets people into the pipeline. Your sales pipeline (Day 12) moves them toward a decision. Your appointment system (Day 13) books them in. Your payments system (Day 14) collects the money. Your onboarding system (Day 15) keeps new members engaged.

But here is the question nobody has answered yet: **where do all those leads come from in the first place?**

Right now, Sunrise Wellness Studio depends on people stumbling across the website, hearing about it from a friend, or clicking an ad. Those are fine. But they are passive. You are waiting for leads to find you. A real marketing engine does the opposite -- it actively pulls strangers into your world, educates them until they trust you, segments them by what they actually care about, and then delivers the right offer at the right time. And when some of those leads go cold? It wakes them back up.

Today you will build that engine from scratch. You will create a lead magnet funnel ("Free 7-Day Meal Plan"), a 7-email nurture sequence that builds trust over 14 days, SMS follow-ups for people who stop opening emails, trigger link tracking that automatically segments contacts by their interests, and a re-engagement campaign that recovers cold leads. By the end of today, Sunrise Wellness has a marketing machine that runs 24/7 and fills the top of the pipeline without anyone lifting a finger.

This is the single most valuable system you will build in the entire course. Every business -- fitness studio, dental practice, agency, plumber, consultant -- needs a way to attract strangers, nurture them into warm leads, and convert them into customers. Master this, and you can build it for any client in any industry.

---

## What You'll Combine

| Phase 1 Feature | Day Built | Role in Today's System |
|-----------------|-----------|----------------------|
| Email Marketing & Templates | Day 7 | 7-email nurture sequence, re-engagement emails, trigger links |
| Trigger Links | Day 7 | Track which content each lead clicks to segment by interest |
| Contacts & Smart Lists | Day 2 | Segment leads by engagement level, interest, and recency |
| Custom Fields & Tags | Day 2 | Store interest data, track campaign progress, flag cold leads |
| Funnels & Landing Pages | Day 8 | Lead magnet landing page and thank-you page |
| Workflows & Automation | Day 9 | Nurture sequence timing, conditional branching, SMS fallbacks |
| Reporting & Dashboards | Day 10 | Track open rates, click rates, conversions, and campaign ROI |

---

## The System Architecture

Study this carefully. It shows the complete marketing campaign flow you are building today -- from first touch to conversion (or re-engagement if they go cold). Every exercise maps to a section of this diagram.

```
LEAD MAGNET FUNNEL (Exercise 16.1)
====================================
[Facebook Ad / Blog Post / Social Media]
              |
              v
[Landing Page: "Free 7-Day Meal Plan"]
  - Benefits list + sample day preview
  - Form: Name, Email, Phone (optional), Fitness Goal
              |
         [Form Submitted]
              |
              v
[Thank-You Page]
  - "Your meal plan is on its way!"
  - Bonus CTA: "Book a Free Trial Class"
  - Download link / email delivery
              |
              v
[Contact Created / Updated]
  - Tag: "lead-magnet-meal-plan"
  - Custom field: Fitness Goal = {selection}
  - Enters nurture workflow


7-EMAIL NURTURE SEQUENCE (Exercise 16.2)
==========================================
Day 0:  [Email 1] Meal plan delivery + welcome
            |
Day 2:  [Email 2] "3 Fitness Mistakes Beginners Make"
            |
Day 4:  [Email 3] Success story + TRIGGER LINKS (PT / Classes / Nutrition)
            |  \__> Trigger link clicked? --> Tag added --> Interest workflow (Ex 16.4)
            |
Day 7:  [Email 4] Class spotlight + schedule link
            |
Day 9:  [Email 5] Community + social proof
            |
Day 11: [Email 6] Free trial offer + WELCOME20 coupon
            |
Day 14: [Email 7] Final push + urgency


SMS FOLLOW-UP LAYER (Exercise 16.3)
=====================================
Runs in parallel with the email sequence:

After Email 3 (Day 4):
  - If NOT opened within 48 hours --> SMS nudge

After Email 6 (Day 11):
  - If NOT opened within 24 hours --> Resend with new subject line


TRIGGER LINK SEGMENTATION (Exercise 16.4)
============================================
Email 3 contains three trigger links:
  [Clicked "Personal Training"] --> Tag: interested-pt
      --> Send: Trainer bios + booking link
  [Clicked "Group Classes"]     --> Tag: interested-classes
      --> Send: Class schedule + trial invite
  [Clicked "Nutrition Coaching"] --> Tag: interested-nutrition
      --> Send: Consultation booking link


RE-ENGAGEMENT CAMPAIGN (Exercise 16.5)
=========================================
Smart List: tag "lead-magnet-meal-plan" + NO tag "trial-booked"
            + last activity 30+ days ago

[Re-Engagement Email 1] New angle: "Things have changed at Sunrise..."
      |  (Wait 5 days)
[Re-Engagement Email 2] Updated offer: "Exclusive comeback deal"
      |  (Wait 5 days)
[Re-Engagement Email 3] "Should we stop emailing you?"
      |
      +--> If opened/clicked --> back into nurture
      +--> If no engagement --> Tag: "newsletter-only"
           --> Monthly newsletter list (low frequency)


CAMPAIGN ANALYTICS (Exercise 16.6)
=====================================
Track: Open rates, click rates, trigger link popularity,
       lead magnet --> trial --> member conversion funnel
```

---

## Part 1: Build the Lead Magnet Funnel (45 min)

A lead magnet is the oldest trick in digital marketing, and it still works because the psychology is simple: give people something valuable for free, and they will give you their contact information in return. The "Free 7-Day Meal Plan" is perfect for a wellness studio because it attracts exactly the kind of person who would become a member -- someone who cares about health and is actively looking for guidance.

### Exercise 16.1: Create the "Free 7-Day Meal Plan" Lead Magnet Funnel

**Purpose:** Build a high-converting landing page that captures leads with a compelling free offer, then immediately starts building trust on the thank-you page.

Navigate to **Sites > Funnels** and click **+ Create Funnel**.

**Funnel Name:** "Sunrise Wellness - Free 7-Day Meal Plan"

**Step 1 -- Build the Landing Page**

Click **+ Add New Step** and name it "Meal Plan Landing Page." Choose a clean, single-column template (or start from scratch).

Build the page with these sections from top to bottom:

**Hero Section:**
- **Headline:** "Kickstart Your Health with a Free 7-Day Meal Plan"
- **Subheadline:** "Simple, delicious meals designed by our nutrition team -- delivered to your inbox in 60 seconds"
- **Hero image:** Use a placeholder image of healthy food or a bright kitchen scene (you can use GHL's stock image library or upload your own)
- **CTA Button:** "Get My Free Meal Plan" (scrolls down to the form)

**Benefits Section (3-4 bullet points with icons):**
- "Balanced meals for every fitness goal -- weight loss, muscle building, or general wellness"
- "Simple recipes with ingredients you already have -- no specialty health food store required"
- "Calorie and macro breakdowns included so you know exactly what you are eating"
- "Designed by certified nutritionists at Sunrise Wellness Studio"

**Sample Day Preview Section:**

This is the "proof" section. Show a preview of what they will get so it feels real and valuable.

```
SAMPLE: Day 3 of Your Meal Plan
---------------------------------
Breakfast: Greek Yogurt Power Bowl
  Protein-packed Greek yogurt + berries + granola + honey drizzle
  Calories: 380 | Protein: 28g

Lunch: Grilled Chicken Mediterranean Wrap
  Whole wheat wrap + grilled chicken + hummus + veggies
  Calories: 450 | Protein: 35g

Dinner: Lemon Herb Salmon with Roasted Vegetables
  Wild salmon + asparagus + sweet potato
  Calories: 520 | Protein: 40g

Snack: Almond Butter Apple Slices
  Calories: 210 | Protein: 7g

Daily Total: ~1,560 calories | 110g protein
```

Display this as a styled content block or an image. The goal is for visitors to think: "If this is just ONE day, imagine what the full week looks like." That curiosity is what converts them.

**Social Proof Section:**
- "Over 2,500 meal plans downloaded this month"
- A testimonial (create a realistic one): "I tried the 7-day meal plan and lost 4 pounds in my first week. The recipes were actually easy to make! - Jessica M."
- Sunrise Wellness Studio logo and tagline

**Form Section:**

This is the conversion point. Navigate to the form element in your page builder and configure it:

| Field | Type | Required | Maps To |
|-------|------|----------|---------|
| First Name | Text | Yes | Contact: First Name |
| Email | Email | Yes | Contact: Email |
| Phone | Phone | No | Contact: Phone |
| What's your primary fitness goal? | Dropdown | Yes | Custom Field: Fitness Goals |

**Dropdown options for Fitness Goal:**
- Weight Loss
- Build Muscle / Tone Up
- Improve Flexibility
- General Health & Wellness
- Stress Relief / Mental Health

> **Why is Phone optional?** Making phone required kills conversion rates on lead magnets. People will trade their email for a free PDF but resist giving their phone number to a business they do not trust yet. By making it optional, you get higher form completions. Those who DO provide their phone number are warmer leads -- and you can use SMS follow-ups with them (Exercise 16.3).

**Form Settings:**
- **Form Name:** "Meal Plan Download"
- **Submit Button Text:** "Send Me the Meal Plan!"
- **After Submission:** Redirect to Step 2 (Thank-You Page)

**Step 2 -- Build the Thank-You Page**

Click **+ Add New Step** and name it "Meal Plan Thank You."

**Thank-You Page Content:**

**Headline:** "Your 7-Day Meal Plan is On Its Way!"
**Subheadline:** "Check your email inbox (and spam folder, just in case) -- your meal plan will arrive within 5 minutes."

**Bonus CTA Section:**

This is the money section. The lead just opted in and they are at peak engagement. Hit them with the next logical step.

- **Headline:** "While you wait... want to try a FREE class?"
- **Body:** "Your meal plan will transform how you eat. But real results come when you combine great nutrition with the right workouts. Book a free trial class at Sunrise Wellness and experience the difference."
- **CTA Button:** "Book My Free Trial Class" (links to your Free Trial funnel or your Day 4 calendar booking page)
- **Secondary text:** "No commitment. No pressure. Just show up and sweat."

**What to Expect Section:**
- "In the next 14 days, you will receive a short email series with fitness tips, success stories, and insider wellness advice. You can unsubscribe anytime."

This sets expectations for the nurture sequence so they do not feel ambushed when the emails start arriving.

**Publish the funnel** and copy the URL. You will need it for the workflow trigger.

> **Pro Tip:** In a real client engagement, you would A/B test two versions of this landing page -- one with a short form (just name + email) and one with the fitness goal field included. The shorter form will convert more visitors, but the longer form gives you segmentation data. For this course, keep the fitness goal field because the segmentation powers your trigger link strategy in Exercise 16.4.

---

## Part 2: Build the 7-Email Nurture Sequence (60 min)

This is the core of your marketing engine. Most businesses send one follow-up email after a lead magnet download and then wonder why nobody converts. The truth is that a single email converts about 1-3% of leads. A well-crafted 7-email sequence, spaced over 14 days, converts 15-25% because it does what a single email cannot: it builds trust through repeated value delivery, educates the lead about your offer, and creates natural urgency without feeling pushy.

Each email in this sequence has a specific job. None of them are filler.

### Exercise 16.2: Build the Nurture Workflow and Email Sequence

**Purpose:** Create a 7-email automated workflow that nurtures meal plan leads from "just downloaded a freebie" to "ready to book a trial" over 14 days.

Navigate to **Automation > Workflows** and click **+ Create Workflow > Start from Scratch**.

**Workflow Name:** "Marketing: Meal Plan Nurture Sequence"

**Step 1 -- Set the Trigger**

Click **Add New Trigger** and select **Form Submitted**.
- **Form:** "Meal Plan Download" (the form you just built in Exercise 16.1)

**Step 2 -- Immediate Actions (Tag + Custom Field)**

Add these actions immediately after the trigger, with no wait:

**Action 1: Add Tag**
- Tag: `lead-magnet-meal-plan`

This tag identifies everyone who downloaded the meal plan. You will use it for Smart Lists, re-engagement campaigns, and conversion tracking.

**Action 2: Add Tag (based on Fitness Goal)**

Add an **If/Else** branch to tag them by their selected fitness goal:
- If Fitness Goals = "Weight Loss" --> Add tag: `goal-weight-loss`
- Else If Fitness Goals = "Build Muscle / Tone Up" --> Add tag: `goal-muscle`
- Else If Fitness Goals = "Improve Flexibility" --> Add tag: `goal-flexibility`
- Else If Fitness Goals = "General Health & Wellness" --> Add tag: `goal-general`
- Else --> Add tag: `goal-other`

These goal tags will be useful later if you want to send targeted content based on their stated goal. For now, they enrich the contact record.

**Action 3: Create Opportunity**
- **Pipeline:** Membership Sales
- **Stage:** New Inquiry
- **Opportunity Name:** "{{contact.first_name}} {{contact.last_name}} - Meal Plan Lead"
- **Value:** $79 (Basic membership as default estimated value)

**Action 4: Internal Notification**
- "New meal plan download: {{contact.first_name}} {{contact.last_name}} -- Goal: {{contact.fitness_goals}}"

**Step 3 -- Email 1: Meal Plan Delivery (Day 0, immediate)**

Add action: **Send Email**

- **Subject:** "Your 7-Day Meal Plan is here, {{contact.first_name}}!"
- **Body:**

```
Hi {{contact.first_name}},

Welcome! Here is your 7-Day Meal Plan as promised.

[DOWNLOAD BUTTON or LINK: "Download Your Meal Plan"]

(Link this to a PDF hosted in GHL's media library, Google Drive,
or any file hosting service. Upload a simple PDF you create, or
use a placeholder link for practice.)

A few tips to get the most out of it:

1. Start on a Monday -- it is easier to build new habits at the
   start of a week
2. Prep your ingredients on Sunday night so Day 1 is effortless
3. Do not stress about following it perfectly -- even 5 out of
   7 days will make a difference

Over the next two weeks, I will send you a few short emails with
fitness tips, success stories from our members, and some insider
wellness advice. No spam, just stuff that actually helps.

Talk soon,
Sarah
Sunrise Wellness Studio

P.S. If you want to pair this meal plan with the right workout
routine, we offer a free trial class -- no commitment, no sales
pitch, just a great workout. [Book your free trial here: LINK]
```

> **Why deliver the meal plan by email instead of just on the thank-you page?** Two reasons. First, it forces them to open your email and interact with it, which trains their inbox to show your future emails (improving deliverability). Second, it gives you an open-rate data point on day zero -- if they do not even open the delivery email, you know immediately that something is wrong (bad email address, spam folder, or they used a throwaway email).

**Step 4 -- Email 2: Value Email (Day 2)**

Add action: **Wait** --> 2 days

Add action: **Send Email**

- **Subject:** "The 3 biggest fitness mistakes (almost everyone makes #2)"
- **Body:**

```
Hi {{contact.first_name}},

How is the meal plan going? Even if you have not started yet,
no worries -- it will be there when you are ready.

In the meantime, I wanted to share something I tell every new
member at Sunrise Wellness. There are 3 mistakes that sabotage
people's fitness goals before they even get started:

Mistake #1: Going too hard, too fast
Motivation is highest on Day 1. People sprint into intense
workouts, burn out by Day 4, and quit by Day 10. The fix?
Start at 60% intensity and build up over 3 weeks.

Mistake #2: Ignoring nutrition
You cannot out-exercise a bad diet. (Good thing you have a
meal plan now.) Exercise accounts for about 20% of body
composition changes. Nutrition accounts for 80%.

Mistake #3: Working out alone
People who exercise with a friend or in a group setting are
42% more likely to stick with it past 90 days. Community is
not a nice-to-have -- it is a retention strategy.

That last one is why we built Sunrise Wellness around group
classes and community. It is harder to skip when people are
expecting you to show up.

More tips coming your way soon.

Sarah
Sunrise Wellness Studio
```

> **Why a pure value email on Day 2?** No CTA, no offer, no pitch. This email exists solely to build trust. The lead just gave you their email address two days ago. If the very next email is "BUY THIS," they unsubscribe. Instead, you teach them something useful, which makes them think: "This studio actually knows what they are talking about." That belief is what eventually converts them.

**Step 5 -- Email 3: Success Story + Trigger Links (Day 4)**

Add action: **Wait** --> 2 days

Add action: **Send Email**

- **Subject:** "How Maria lost 22 lbs (and actually kept it off)"
- **Body:**

```
Hi {{contact.first_name}},

I want to introduce you to Maria.

Maria downloaded this exact meal plan 8 months ago. She was
skeptical -- she had tried every diet app, every YouTube workout
program, every "30-day challenge." Nothing stuck.

But she decided to come in for a free trial class. She tried
our HIIT Burn class on a Tuesday morning. She was nervous.
She almost backed out in the parking lot.

She showed up anyway.

Fast forward 8 months: Maria has lost 22 pounds, she is in the
best shape of her life, and she has not missed a week since
month 2. Her secret? She found the right combination for HER.

The truth is, there is no single "best" workout. What matters
is finding the approach that fits YOUR goals and YOUR life.

Which of these sounds most like what you are looking for?

[TRIGGER LINK: "Personal training -- I want one-on-one attention"]

[TRIGGER LINK: "Group classes -- I want energy and community"]

[TRIGGER LINK: "Nutrition coaching -- I need help with my diet"]

Click the one that resonates most and I will send you something
specific to that path.

Sarah
Sunrise Wellness Studio
```

**Setting up the trigger links:**

For each trigger link in this email, you need to create them in GHL and configure the tags:

1. Navigate to **Marketing > Trigger Links** (or create them within the email editor if your version supports it)
2. Create three trigger links:

| Trigger Link Name | URL (can be any page) | Tag to Add on Click |
|-------------------|-----------------------|---------------------|
| Interest - Personal Training | Your PT info page or calendar | `interested-pt` |
| Interest - Group Classes | Your class schedule page | `interested-classes` |
| Interest - Nutrition Coaching | Your nutrition page or calendar | `interested-nutrition` |

3. Insert these trigger links into Email 3 where the placeholders are

> **Why trigger links in Email 3 specifically?** By Day 4, the lead has opened two emails from you (the meal plan delivery and the value email). They are warmed up enough to self-select their interest. Putting trigger links in Email 1 would get lower engagement because they do not trust you yet. Putting them in Email 6 would be too late -- you want to personalize the rest of the sequence based on what they click.

**Step 6 -- Email 4: Class Spotlight (Day 7)**

Add action: **Wait** --> 3 days

Add action: **Send Email**

- **Subject:** "What actually happens in a Sunrise Wellness class"
- **Body:**

```
Hi {{contact.first_name}},

A lot of people tell me they are nervous about their first
group fitness class. They imagine a room full of athletes
doing impossible moves while they struggle in the back corner.

Here is what ACTUALLY happens:

You walk in. The instructor greets you by name (yes, we
actually do this). They ask about your fitness level and any
injuries. The class starts with a warm-up that everyone can do.

During the workout, the instructor offers three difficulty
levels for every exercise: beginner, intermediate, and advanced.
Nobody is watching to see which level you pick. Everyone is
focused on their own workout.

After 45 minutes, you are sweaty, accomplished, and wondering
why you waited so long to try this.

Here is this week's class schedule:

Monday:    HIIT Burn (6 AM, 12 PM, 5:30 PM)
Tuesday:   Yoga Flow (7 AM, 6 PM)
Wednesday: Power Pilates (6 AM, 12 PM, 5:30 PM)
Thursday:  HIIT Burn (6 AM, 12 PM, 5:30 PM)
Friday:    Yoga Flow (7 AM) | Pilates (12 PM)
Saturday:  Community Class (9 AM -- free for trial members!)

Want to try one? Pick a class and book your free trial:
[BOOK A FREE TRIAL: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio
```

**Step 7 -- Email 5: Community and Social Proof (Day 9)**

Add action: **Wait** --> 2 days

Add action: **Send Email**

- **Subject:** "The real reason people stay at Sunrise Wellness"
- **Body:**

```
Hi {{contact.first_name}},

I will let you in on something.

The workouts at Sunrise Wellness are great. The nutrition
guidance is solid. The studio is clean and well-equipped.

But that is not why people stay.

People stay because of each other.

Our member community has over 400 people who encourage each
other, celebrate wins (big and small), share meal prep ideas,
and hold each other accountable. When you miss a class, someone
notices. When you hit a personal record, people cheer.

Here are a few things our members said this week:

"I came for the workouts but I stay for the people. My
Tuesday morning HIIT crew is basically family now." - Jason R.

"I have never stuck with a fitness routine longer than 3 months.
I have been at Sunrise for 14 months. The community is the
difference." - Priya K.

"My favorite part is the Saturday community class. It is free,
it is fun, and afterward half of us go get coffee." - David L.

This is not a gym where you swipe your card and put in
headphones. This is a place where people know your name.

Come see for yourself:
[BOOK A FREE TRIAL: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio
```

**Step 8 -- Email 6: The Offer (Day 11)**

Add action: **Wait** --> 2 days

Add action: **Send Email**

- **Subject:** "A thank-you gift for you, {{contact.first_name}} (20% off)"
- **Body:**

```
Hi {{contact.first_name}},

You have been following along with the meal plan and reading
these emails for almost two weeks now. That tells me something
about you -- you are serious about your health, and you are
doing your research before committing.

I respect that.

So I want to make your decision easier with something we do
not normally offer publicly:

20% off your first month at Sunrise Wellness Studio.

Use code: WELCOME20

This applies to any membership tier:
- Basic Membership: $79/mo --> $63.20/mo (first month)
- Premium Membership: $149/mo --> $119.20/mo (first month)
- VIP Membership: $249/mo --> $199.20/mo (first month)

Every membership starts with a free trial class, so you can
experience everything before you pay a single dollar.

Here is how it works:
1. Book your free trial class: [CALENDAR_LINK]
2. Show up and experience Sunrise Wellness firsthand
3. If you love it (you will), use code WELCOME20 when you
   sign up within 7 days of your trial

The code expires in 10 days.

[BOOK YOUR FREE TRIAL + CLAIM YOUR 20% OFF: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio

P.S. If you have questions about which membership tier is right
for you, just reply to this email. I read every response
personally.
```

> **Why wait until Email 6 to make an offer?** Emails 1-5 built trust through value, storytelling, and social proof. By Email 6, the lead has received 11 days of free help from you. The coupon does not feel like a sales pitch -- it feels like a genuine thank-you. This is the difference between marketing that converts and marketing that annoys.

**Step 9 -- Email 7: Final Push (Day 14)**

Add action: **Wait** --> 3 days

Add action: **Send Email**

- **Subject:** "Last chance: your WELCOME20 code expires tomorrow"
- **Body:**

```
Hi {{contact.first_name}},

Quick note -- your 20% off code (WELCOME20) expires tomorrow.

I am not going to write a long email about it. You have read
the success stories. You have seen the class schedule. You
know what we offer.

The only question left is: are you going to try it?

Here is what you have to lose by booking a free trial: nothing.
It is free. It is one hour. If you hate it, you never have to
come back.

Here is what you have to gain: a workout community that
actually sticks, nutrition guidance from people who know what
they are doing, and a 20% discount that disappears tomorrow.

[BOOK YOUR FREE TRIAL NOW: CALENDAR_LINK]

See you in class,
Sarah
Sunrise Wellness Studio
```

**Step 10 -- End of Sequence Actions**

After Email 7, add these final actions:

**Action: If/Else**
- **Condition:** Contact has tag `trial-booked` OR Contact has tag `active-member`
- **If YES:** Do nothing (they converted -- the Day 11/12 systems take over from here)
- **If NO:**
  - Add tag: `nurture-complete-no-conversion`

This tag marks leads who went through the entire sequence without booking a trial. You will target them with the re-engagement campaign in Exercise 16.5.

**Save and publish the workflow.**

> **Pro Tip for testing:** Before publishing with real wait times, change all Wait steps to 1 minute, run a test contact through the entire sequence, and verify that every email arrives correctly. Once confirmed, change the waits back to the real intervals (2 days, 3 days, etc.) and re-publish. This saves you from discovering a broken email on Day 11 of a live campaign.

---

## Part 3: SMS Follow-Up for Non-Openers (30 min)

Email open rates for nurture sequences typically hover around 25-40%. That means 60-75% of your leads are not reading your carefully crafted emails. Some of those people genuinely lost interest. But many of them simply do not check email regularly, your emails landed in Promotions/spam, or they got busy and forgot.

SMS cuts through the noise. Text messages have a 98% open rate. Using SMS as a fallback for email non-openers recovers leads that would otherwise be completely lost.

### Exercise 16.3: Build SMS Follow-Up Triggers for Non-Openers

**Purpose:** Add SMS fallback actions to the nurture workflow that re-engage leads who are not opening emails, without double-messaging people who ARE engaged.

> **Important Note on Phone Numbers:** Not every lead will have provided a phone number (it was optional on the form). Your workflow must check for a phone number before attempting to send SMS. GHL will typically skip the SMS action if no phone number exists, but adding an explicit If/Else check makes your workflow cleaner and prevents execution errors in your workflow logs.

> **If You Cannot Send SMS:** If you do not have SMS enabled in your sub-account (or if you want to keep things email-only for now), skip the SMS sends and use only the "resend with different subject line" approach. The resend technique works well on its own and does not require SMS capabilities. Both the SMS and email-only paths are documented below.

Open the "Marketing: Meal Plan Nurture Sequence" workflow you just built.

**SMS Fallback 1: After Email 3 (Day 4)**

Find Email 3 (the success story + trigger links email) in your workflow. After the Wait that follows Email 3 (the 3-day wait before Email 4), insert a new branch:

1. Add an **If/Else** action BEFORE Email 4
2. **Condition:** Contact did not open Email 3

In practice, since you already have a 3-day wait after Email 3, the timing works out naturally -- you are checking 3 days later whether they opened it. Here is how to build it:

1. After the 3-day wait (before Email 4), add **If/Else**:
   - **Condition:** "Email Activity" -- Contact did not open the email with subject containing "Maria lost 22 lbs" (or use the email event filter available in your GHL version)

2. **If NOT opened AND Contact Phone is not empty:**
   - Send SMS: "Hey {{contact.first_name}}! I sent you something about how one of our members lost 22 lbs -- check your email when you get a chance. It is a good read. - Sarah at Sunrise Wellness"

3. **If NOT opened AND Contact Phone IS empty (email-only alternative):**
   - Resend Email 3 with a different subject line: "You missed this inspiring story, {{contact.first_name}}..."
   - Use the same email body but a fresh subject to get past whatever stopped them from opening the first time

4. **If opened:** Continue to Email 4 as normal

> **Why this specific SMS?** Notice it does not repeat the email content. It just nudges them to check their email. This is intentional -- you want them to engage with the email (which has the trigger links), not just read an SMS summary. The SMS is a doorway back to the email, not a replacement for it.

**SMS Fallback 2: After Email 6 (Day 11)**

Email 6 is the offer email with the WELCOME20 coupon. This is the most important email in the sequence. If someone misses it, they miss the conversion opportunity entirely.

Find Email 6 in your workflow. After Email 6, insert:

1. Add a **Wait** --> 24 hours (this is a sub-wait within the existing sequence)
2. Add **If/Else**:
   - **Condition:** Contact did not open Email 6 (the WELCOME20 offer email)

3. **If NOT opened AND Contact Phone is not empty:**
   - Send SMS: "{{contact.first_name}}, I just sent you a 20% off code for Sunrise Wellness. It is the only discount we offer -- check your email for details! - Sarah"
   - ALSO resend Email 6 with a different subject line (see below)

4. **If NOT opened AND Contact Phone IS empty:**
   - Resend Email 6 with the SAME body but a new subject line:
   - **New Subject:** "{{contact.first_name}}, I set aside something for you"
   - This technique is called a "resend to non-openers" and typically recovers 8-12% additional opens

5. **If opened:** Continue to Email 7 as normal

**Update the wait before Email 7:** Since you added a 24-hour sub-wait for the Email 6 non-opener check, adjust the wait before Email 7. Originally it was 3 days after Email 6. Now it should be 2 days after the non-opener check (24 hours + 2 days = 3 days total from Email 6), so the final email still arrives on Day 14.

**Save the updated workflow.**

---

## Part 4: Trigger Link Segmentation (30 min)

Trigger links are one of the most underused features in GHL. Most people use them as basic "click tracking." But their real power is behavioral segmentation -- when someone clicks a trigger link, they are telling you exactly what they care about, and you can instantly deliver content tailored to that interest.

In Email 3, you included three trigger links (Personal Training, Group Classes, Nutrition Coaching). Now you will build the workflows that respond when someone clicks each one.

### Exercise 16.4: Build Interest-Based Trigger Link Workflows

**Purpose:** When a lead clicks a trigger link in Email 3, automatically send them a targeted follow-up email specific to their interest and add them to the appropriate segment for future marketing.

**Workflow 1: "Marketing: Interest - Personal Training"**

Navigate to **Automation > Workflows** and create a new workflow.

**Trigger:** Tag Added
- **Tag:** `interested-pt`

**Action 1: Wait** --> 1 day

Do not send the follow-up instantly. The lead just clicked the trigger link and is still reading Email 3. Give them a day, then follow up when they are back in their inbox fresh.

**Action 2: Send Email**
- **Subject:** "Meet your personal trainers at Sunrise Wellness"
- **Body:**

```
Hi {{contact.first_name}},

You mentioned you are interested in personal training --
great choice! One-on-one training is the fastest path to
results because every session is built around YOUR goals,
YOUR body, and YOUR schedule.

Meet our trainers:

COACH MIKE -- Strength & Conditioning Specialist
- 12 years experience
- Specialties: weight loss, muscle building, athletic performance
- Style: Structured, goal-oriented, data-driven
- "I track every metric so we can see real progress, not just
  feel-good guesses."

COACH ALYSSA -- Holistic Fitness & Flexibility
- 8 years experience
- Specialties: flexibility, injury recovery, mind-body connection
- Style: Supportive, patient, technique-focused
- "I believe in building a strong foundation first. Everything
  else follows."

Personal training packages start at $59/session, and your first
session is always free so you can find the right trainer for you.

[BOOK A FREE PT SESSION WITH MIKE: CALENDAR_LINK]
[BOOK A FREE PT SESSION WITH ALYSSA: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio
```

**Action 3: Update Opportunity Note (optional)**

If the contact already has an opportunity in the Membership Sales pipeline:
- Add a note to the opportunity: "Interested in Personal Training (clicked trigger link on {{date}})"
- This gives your sales process context about what the lead cares about

**Save and publish.**

---

**Workflow 2: "Marketing: Interest - Group Classes"**

**Trigger:** Tag Added
- **Tag:** `interested-classes`

**Action 1: Wait** --> 1 day

**Action 2: Send Email**
- **Subject:** "This week's class schedule (+ a free trial invite)"
- **Body:**

```
Hi {{contact.first_name}},

You clicked on group classes -- you are going to love the
energy in our studio.

Here is what is coming up this week:

HIIT BURN (High Intensity Interval Training)
  Mon/Wed/Thu: 6 AM, 12 PM, 5:30 PM
  45 minutes | All levels welcome
  Expect: Fast-paced circuits, strength + cardio combo
  Best for: Weight loss, cardiovascular fitness, stress relief

YOGA FLOW
  Tue/Fri: 7 AM, 6 PM
  60 minutes | All levels welcome
  Expect: Dynamic stretching, breathwork, strength poses
  Best for: Flexibility, recovery, mental clarity

POWER PILATES
  Wed/Fri: 6 AM (Wed), 12 PM (Fri)
  45 minutes | All levels welcome
  Expect: Core-focused strengthening, low-impact, high results
  Best for: Core strength, posture, injury prevention

SATURDAY COMMUNITY CLASS
  Sat: 9 AM
  60 minutes | FREE for trial members
  Expect: Rotating format -- a different style every week

Your first class is free. No membership required. Just show up.

[BOOK YOUR FREE CLASS: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio

P.S. Not sure which class to try first? Reply to this email
and tell me your goals -- I will recommend the perfect one.
```

**Save and publish.**

---

**Workflow 3: "Marketing: Interest - Nutrition Coaching"**

**Trigger:** Tag Added
- **Tag:** `interested-nutrition`

**Action 1: Wait** --> 1 day

**Action 2: Send Email**
- **Subject:** "Take your meal plan to the next level"
- **Body:**

```
Hi {{contact.first_name}},

You are already ahead of most people because you downloaded
the 7-Day Meal Plan and you are clearly thinking about
nutrition. That is half the battle.

But here is what a meal plan cannot do: it cannot adapt to
YOUR metabolism, YOUR food preferences, YOUR lifestyle, and
YOUR specific goals. That is where nutrition coaching comes in.

What a nutrition coaching session looks like:

1. We review your current eating habits (no judgment, just data)
2. We look at your fitness goals and reverse-engineer the
   nutrition plan that supports them
3. We build a customized weekly meal framework that fits YOUR
   life -- not a generic template
4. You get a follow-up check-in at 2 weeks to adjust and
   optimize

Our nutrition coaches are certified dietitians who work with
everyone from first-time meal preppers to competitive athletes.

Your first nutrition consultation is free for meal plan
subscribers.

[BOOK YOUR FREE NUTRITION CONSULTATION: CALENDAR_LINK]

Sarah
Sunrise Wellness Studio
```

**Save and publish.**

---

> **Key Insight:** Notice that each trigger link workflow delivers a DIFFERENT next step. The PT-interested lead gets trainer bios and a PT booking link. The classes-interested lead gets a class schedule and a class booking link. The nutrition-interested lead gets a consultation pitch and a consultation booking link. This is the power of behavioral segmentation -- instead of sending everyone the same generic "book a trial" email, you send each person the specific thing they told you they want. Conversion rates for segmented follow-ups are 2-3x higher than generic ones.

---

## Part 5: Re-Engagement Campaign for Cold Leads (30 min)

Not everyone converts on the first pass. Some leads download the meal plan, read a few emails, and then go quiet. That does not mean they are lost forever -- it means they were not ready. Life got busy, the timing was wrong, or they needed more time to decide.

A re-engagement campaign gives cold leads a second chance. And the "should we stop emailing you?" email at the end is not just a courtesy -- it is a list hygiene strategy that improves your deliverability for everyone else.

### Exercise 16.5: Build the Cold Lead Re-Engagement System

**Purpose:** Automatically identify leads who downloaded the meal plan but never booked a trial, and run a 3-email re-engagement sequence to either reactivate them or gracefully move them to low-frequency communication.

**Step 1 -- Create the "Cold Meal Plan Leads" Smart List**

Navigate to **Contacts > Smart Lists > + Create Smart List**

**Name:** "Cold Meal Plan Leads - 30+ Days"

**Filters:**
- Tag contains `lead-magnet-meal-plan`
- AND Tag does NOT contain `trial-booked`
- AND Tag does NOT contain `active-member`
- AND Tag does NOT contain `re-engagement-active` (prevents re-triggering if they are already in the re-engagement sequence)
- AND Date Added is more than 30 days ago (or "Last Activity" is more than 30 days ago, depending on available filters)

Save the Smart List.

> **Why 30 days?** Your nurture sequence runs for 14 days. Giving them another 16 days after that accounts for people who are slow to act. Anyone who has not booked a trial within 30 days of downloading the meal plan is genuinely cold.

**Step 2 -- Build the Re-Engagement Workflow**

Create a new workflow: **"Marketing: Meal Plan Re-Engagement"**

**Trigger:** You have two options here:

- **Option A (Manual/Periodic):** Run this as a manual bulk action on the Smart List. Go to the Smart List, select all contacts, and use "Add to Workflow" to enroll them. You would do this once a month.

- **Option B (Automated):** Use a Date/Time-based trigger that checks daily if contacts meet the Smart List criteria. Some GHL versions support this natively. Alternatively, set the trigger to "Tag Added" with tag `re-engagement-eligible`, and create a separate small workflow that adds this tag to contacts who meet the 30-day criteria.

For this exercise, use **Option A** (manual enrollment via Smart List) because it is simpler and gives you control over when the re-engagement campaign runs. In a real client setup, you would automate this with Option B.

**Action 1: Add Tag**
- Tag: `re-engagement-active`

This prevents the contact from being enrolled again while the sequence is running.

**Action 2: Re-Engagement Email 1 -- "Things Have Changed"**

Send Email:
- **Subject:** "{{contact.first_name}}, a lot has changed at Sunrise Wellness"
- **Body:**

```
Hi {{contact.first_name}},

It has been a while since you downloaded our 7-Day Meal Plan,
and I wanted to check in because a few things have changed
around here:

- We added 12 new class times (including 6 AM slots for
  early risers and 7 PM slots for the after-work crowd)
- Our new nutrition coaching program launched -- it pairs
  perfectly with the meal plan you downloaded
- We renovated the studio with new equipment and a dedicated
  stretching area
- We started a Saturday morning community class that is free
  for everyone -- members and non-members

I am not sure where you are on your fitness journey right now,
but if you have been thinking about making a change, the door
is open.

[SEE WHAT IS NEW AT SUNRISE WELLNESS: LINK]

Sarah
Sunrise Wellness Studio
```

**Action 3: Wait 5 Days**

**Action 4: If/Else -- Check for Engagement**

- **Condition:** Contact opened Re-Engagement Email 1 OR clicked any link in it
- **If YES:** They are warming back up. Continue to Email 2 (which will push them toward a trial).
- **If NO:** Still cold. Continue to Email 2 anyway (different people respond to different angles).

> **Why continue either way?** Because people respond to different messages. Email 1 used a "what is new" angle. Email 2 uses an escalated offer. Someone who ignored "what is new" might respond to a compelling deal. You give them multiple chances with multiple angles before giving up.

**Action 5: Re-Engagement Email 2 -- "Updated Offer"**

Send Email:
- **Subject:** "An exclusive offer for you (not on our website)"
- **Body:**

```
Hi {{contact.first_name}},

I have a deal for you that we are not advertising publicly.

Because you were one of our early meal plan subscribers, I
want to offer you something special:

Your first MONTH free.

Not a free class. Not a free week. A full month of unlimited
classes, community access, and a complimentary nutrition
consultation -- on us.

Here is why: I know the meal plan showed you that we know what
we are doing when it comes to nutrition. I want to show you
that the fitness side is just as good. And the best way to do
that is to let you experience it with zero risk.

No credit card required for the trial month. No automatic
billing. If you love it, you sign up. If not, you walk away
with 30 days of free workouts and no hard feelings.

[CLAIM YOUR FREE MONTH: CALENDAR_LINK]

This offer is available for the next 14 days.

Sarah
Sunrise Wellness Studio
```

> **About the free month offer:** In a real business, you would confirm this offer with the client before including it in the automation. For this course exercise, the point is to demonstrate an escalated offer in a re-engagement sequence. The first pass used a 20% coupon (WELCOME20). The re-engagement uses a stronger offer because these leads already said no to the first one.

**Action 6: Wait 5 Days**

**Action 7: If/Else -- Check for Conversion**

- **Condition:** Contact has tag `trial-booked` OR Contact clicked any link in Re-Engagement Email 2
- **If YES:** Remove tag `re-engagement-active`. End workflow. (They are re-engaged and the Day 11/12 systems handle the rest.)
- **If NO:** Continue to Email 3.

**Action 8: Re-Engagement Email 3 -- "Should We Stop Emailing You?"**

Send Email:
- **Subject:** "Should I stop sending you emails?"
- **Body:**

```
Hi {{contact.first_name}},

I have sent you a few emails over the past couple of weeks
and I have not heard back. I completely understand -- life
gets busy and fitness might not be a priority right now.

I do not want to be that business that fills your inbox with
stuff you do not want. So I have a quick question:

Do you still want to hear from us?

[TRIGGER LINK: "Yes, keep me in the loop!"]

[TRIGGER LINK: "No thanks, you can stop emailing me."]

If you click "keep me in the loop," I will add you to our
monthly newsletter -- just one email per month with wellness
tips, class updates, and the occasional special offer. No
pressure, no daily emails.

If you click "stop emailing," I will remove you from all
marketing emails immediately. No hard feelings at all.

And if you do not click anything, I will move you to the
monthly newsletter by default and you can always unsubscribe
from there.

Sarah
Sunrise Wellness Studio
```

**Set up the trigger links for Email 3:**

| Trigger Link | Tag Added |
|-------------|-----------|
| "Yes, keep me in the loop!" | `newsletter-opt-in` |
| "No thanks, stop emailing me." | `opt-out-requested` |

**Action 9: Wait 5 Days (final check)**

**Action 10: If/Else -- Final Routing**

- **If tag `newsletter-opt-in`:** Remove tag `re-engagement-active`. Add tag `newsletter-only`. Contact stays in the system and receives monthly newsletters only.
- **If tag `opt-out-requested`:** Remove tag `re-engagement-active`. Remove all marketing tags. Add tag `do-not-email`. (You can also trigger GHL's native unsubscribe functionality if available.)
- **If neither tag (no response at all):** Remove tag `re-engagement-active`. Add tag `newsletter-only`. (Default to low-frequency contact as stated in the email.)

**Save and publish the workflow.**

> **Pro Tip:** The "should we stop emailing you?" email is psychologically powerful. It communicates respect. And counterintuitively, it often reactivates cold leads -- people see the subject line, realize they DO still want to hear from you, and re-engage. Industry data shows that "breakup" emails get 2-3x higher open rates than regular marketing emails because the fear of losing access triggers action.

---

## Part 6: Campaign Analytics Review (20 min)

You have built the machine. Now you need the dashboard to monitor it. A marketing campaign without analytics is like driving with your eyes closed -- you might be going fast, but you have no idea if you are heading in the right direction.

### Exercise 16.6: Set Up Campaign Performance Tracking

**Purpose:** Build the reporting views and Smart Lists that let you monitor the health and performance of your entire marketing campaign system at a glance.

**Step 1 -- Create Performance Smart Lists**

Navigate to **Contacts > Smart Lists** and create these lists:

**Smart List 1: "Meal Plan Leads - All Time"**
- Filter: Tag contains `lead-magnet-meal-plan`
- Purpose: Total count of everyone who ever downloaded the meal plan

**Smart List 2: "Meal Plan Leads - This Month"**
- Filter: Tag contains `lead-magnet-meal-plan` AND Date Added is "This Month"
- Purpose: Monthly lead generation velocity

**Smart List 3: "Meal Plan --> Trial Booked"**
- Filter: Tag contains `lead-magnet-meal-plan` AND Tag contains `trial-booked`
- Purpose: Conversion tracking -- how many meal plan leads converted to trial bookings

**Smart List 4: "Meal Plan --> Active Member"**
- Filter: Tag contains `lead-magnet-meal-plan` AND (Tag contains `member-basic` OR `member-premium` OR `member-vip`)
- Purpose: End-to-end conversion tracking -- from free download to paying member

**Smart List 5: "Interested - Personal Training"**
- Filter: Tag contains `interested-pt`
- Purpose: Track trigger link engagement by interest area

**Smart List 6: "Interested - Group Classes"**
- Filter: Tag contains `interested-classes`

**Smart List 7: "Interested - Nutrition Coaching"**
- Filter: Tag contains `interested-nutrition`

**Step 2 -- Calculate Your Conversion Funnel**

Using the Smart Lists above, calculate these metrics (write them down or track them in a spreadsheet):

```
MARKETING CAMPAIGN CONVERSION FUNNEL
======================================

Lead Magnet Downloads (all time):     ____
  |
  v
Trial Booked:                         ____
  Conversion Rate:                    ____% (Trial / Downloads x 100)
  |
  v
Active Members (from meal plan):      ____
  Conversion Rate:                    ____% (Members / Downloads x 100)
  Trial-to-Member Rate:               ____% (Members / Trial Booked x 100)


TRIGGER LINK ENGAGEMENT
========================
Interested in PT:          ____ (___% of total leads)
Interested in Classes:     ____ (___% of total leads)
Interested in Nutrition:   ____ (___% of total leads)
No trigger link clicked:   ____ (___% of total leads)

Most popular interest: ________________


RE-ENGAGEMENT PERFORMANCE
==========================
Cold leads (30+ days):             ____
Re-engagement emails sent:         ____
Re-engaged (opened/clicked):       ____  (___%)
Opted in to newsletter:            ____  (___%)
Opted out:                         ____  (___%)
No response (moved to newsletter): ____  (___%)
```

> **Note:** Since you are working in a practice sub-account, you may not have real data to populate these metrics yet. That is fine -- the point of this exercise is to build the STRUCTURE so that when real data flows through, you can monitor it immediately. Set up the Smart Lists and the tracking template now. The numbers will fill in as you (or a real client) run the campaigns.

**Step 3 -- Review Email Performance**

Navigate to **Marketing > Emails** (or wherever your email campaign reporting lives in your GHL version).

For each email in the nurture sequence, note:

| Email | Open Rate | Click Rate | Unsubscribe Rate |
|-------|-----------|------------|-------------------|
| Email 1: Meal Plan Delivery | | | |
| Email 2: 3 Fitness Mistakes | | | |
| Email 3: Success Story + Triggers | | | |
| Email 4: Class Spotlight | | | |
| Email 5: Community Angle | | | |
| Email 6: WELCOME20 Offer | | | |
| Email 7: Final Push | | | |

**Benchmarks to compare against:**

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Open Rate | < 15% | 15-25% | 25-35% | > 35% |
| Click Rate | < 1% | 1-3% | 3-5% | > 5% |
| Unsubscribe Rate | > 2% | 1-2% | 0.5-1% | < 0.5% |

**Common problems and fixes:**

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Low open rates across all emails | Poor subject lines or deliverability issues | Test different subject lines, check spam score, warm up sending domain |
| High open rates but low click rates | Email content does not compel action, or CTAs are buried | Move CTA higher in the email, make buttons more prominent, reduce text between value and CTA |
| High unsubscribe rate on Email 2 or 3 | Lead magnet attracted wrong audience, or emails feel too frequent | Review lead magnet targeting, increase wait times between emails |
| Open rates drop sharply after Email 3 | Content fatigue, or emails are landing in Promotions tab | Vary email format (short vs. long), use plain-text style, ask recipients to move you to primary inbox |
| Email 6 (offer) has lowest open rate | Subject line looks like a promotion | Test subject lines that do not mention discounts (e.g., "A quick note" vs. "20% off!") |

---

## Integration Checkpoint

Before moving on, verify that your complete marketing campaign system meets these criteria:

**Lead Magnet Funnel:**
- [ ] Landing page has a compelling headline, benefits, sample day preview, social proof, and a form
- [ ] Form captures Name, Email, Phone (optional), and Fitness Goal
- [ ] Form fields are mapped to the correct contact fields and custom fields
- [ ] Thank-you page delivers confirmation and bonus trial CTA
- [ ] Funnel is published and accessible via URL

**Nurture Sequence:**
- [ ] Workflow triggers on the Meal Plan Download form submission
- [ ] Tags are applied immediately: `lead-magnet-meal-plan` + fitness goal tag
- [ ] Pipeline opportunity is created for every new lead
- [ ] 7 emails are spaced correctly: Day 0, 2, 4, 7, 9, 11, 14
- [ ] Email 3 contains three working trigger links (PT, Classes, Nutrition)
- [ ] Email 6 contains the WELCOME20 offer
- [ ] Email 7 creates urgency with the expiration deadline
- [ ] End-of-sequence tagging works (`nurture-complete-no-conversion` for non-converters)

**SMS Follow-Ups:**
- [ ] After Email 3: non-openers receive an SMS nudge (if phone number exists) or an email resend with a new subject line
- [ ] After Email 6: non-openers receive a resend with a different subject line (plus optional SMS)
- [ ] SMS actions include a phone number check to avoid errors
- [ ] Wait times are adjusted so Email 7 still arrives on Day 14

**Trigger Link Segmentation:**
- [ ] Three trigger links are created (PT, Classes, Nutrition)
- [ ] Each trigger link adds the correct tag on click
- [ ] Each tag triggers a separate workflow that sends a targeted follow-up email after a 1-day wait
- [ ] Follow-up emails contain interest-specific content and booking links

**Re-Engagement Campaign:**
- [ ] "Cold Meal Plan Leads" Smart List correctly identifies 30+ day non-converters
- [ ] 3-email re-engagement sequence is built (new angle, escalated offer, breakup email)
- [ ] Breakup email contains trigger links for opt-in and opt-out
- [ ] Final routing correctly handles all three outcomes (opt-in, opt-out, no response)
- [ ] `re-engagement-active` tag prevents duplicate enrollment

**Analytics:**
- [ ] Performance Smart Lists are created (all-time leads, monthly leads, conversions by stage, interest segments)
- [ ] Conversion funnel template is ready to populate with data
- [ ] Email performance benchmarks are documented for comparison

---

## Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental (2 dentists, procedures from $150 cleanings to $3,000 cosmetic work) needs a marketing campaign system to attract new patients. The practice currently relies on insurance directory listings and word-of-mouth. They have no lead magnet, no nurture sequence, and no re-engagement strategy. Patients who visit the website but do not call are lost forever.

**Your Task:** Design and build a complete marketing campaign system for BrightSmile Dental using the same framework you built for Sunrise Wellness. Build everything in your existing sub-account with "BrightSmile" in the naming.

### Lead Magnet: "Free Dental Health Guide"

**Funnel: "BrightSmile - Free Dental Health Guide"**

**Landing Page Content:**
- **Headline:** "Your Complete Guide to a Healthier Smile (Free Download)"
- **Subheadline:** "Learn the 5 daily habits that prevent 90% of dental problems -- from the dentists at BrightSmile Dental"
- **Benefits:**
  - "The #1 brushing mistake that causes cavities (and the simple fix)"
  - "When to floss, how to floss, and why most people are doing it wrong"
  - "Foods that strengthen your teeth vs. foods that silently destroy them"
  - "The warning signs you should never ignore between checkups"
- **Social proof:** "Downloaded by over 3,000 patients in our community"
- **Sample preview:** Show a page from the guide -- e.g., "The Tooth-Friendly Grocery List" with 10 items that strengthen enamel

**Form Fields:**

| Field | Type | Required | Maps To |
|-------|------|----------|---------|
| First Name | Text | Yes | Contact: First Name |
| Email | Email | Yes | Contact: Email |
| Phone | Phone | No | Contact: Phone |
| Last Dental Visit | Dropdown | Yes | Custom Field: Last Dental Visit |

**Dropdown options for Last Dental Visit:**
- Within the last 6 months
- 6-12 months ago
- 1-2 years ago
- More than 2 years ago
- I cannot remember

> **Why ask about their last visit?** This is the dental equivalent of "Fitness Goal." It tells you how urgent their need is. Someone who has not been to a dentist in 2+ years needs a very different nurture approach than someone who visited 6 months ago. The data also powers your re-engagement messaging.

**Thank-You Page:**
- "Your Dental Health Guide is on its way!"
- **Bonus CTA:** "Book a Free Dental Exam -- includes X-rays and a personalized treatment plan" (links to Day 4 dental calendar)

### 7-Email Nurture Sequence for BrightSmile

**Workflow Name:** "BrightSmile: Dental Guide Nurture Sequence"
**Tag on entry:** `lead-magnet-dental-guide`

| Email | Day | Subject | Content Focus |
|-------|-----|---------|---------------|
| 1 | 0 | "Your Dental Health Guide is here!" | Guide delivery + "Start with page 3 -- it covers the most common issue we see." Brief practice intro: friendly, modern, no-judgment philosophy |
| 2 | 2 | "The hidden cost of skipping dental visits" | Value: how small problems become expensive procedures. Cite realistic numbers ($150 cleaning vs. $800 filling vs. $2,500 root canal vs. $4,000 crown). No pitch, just education |
| 3 | 4 | "How Sarah saved $4,000 on dental work" | Patient success story: Sarah came in for a routine exam, they caught an early cavity that would have become a root canal. She paid $150 instead of $4,000. **Trigger links:** "I am interested in whitening," "I am interested in orthodontics/Invisalign," "I just need a regular checkup" |
| 4 | 7 | "What actually happens at a BrightSmile visit" | Walk through the new patient experience: warm front desk, modern equipment, gentle approach, detailed explanation before any procedure, no judgment about how long it has been since your last visit |
| 5 | 9 | "What our patients say about us" | Social proof: 3-4 patient testimonials. Family angle: "Over 200 families trust us with their dental care." Google review rating if available |
| 6 | 11 | "A special offer for new patients" | Free comprehensive dental exam + X-rays (normally $250 value). Include code HEALTHYSMILE. Emphasize: "No insurance required. No strings attached." |
| 7 | 14 | "Last chance for your free exam" | Final push with urgency: offer expires in 48 hours. "Your teeth are not going to fix themselves. But we can help -- and the first step costs you nothing." |

### Trigger Links for BrightSmile

| Trigger Link (in Email 3) | Tag | Follow-Up Email Content |
|---------------------------|-----|-------------------------|
| "I am interested in whitening" | `interested-whitening` | Whitening options explained (in-office laser vs. professional take-home trays), before/after photos, pricing ($299-$599), "Book a free whitening consultation" calendar link |
| "I am interested in orthodontics/Invisalign" | `interested-orthodontics` | Invisalign process overview (consultation, scan, custom aligners, 12-18 month typical timeline), financing options ($150-$250/month), "Book a free Invisalign consultation" calendar link |
| "I just need a regular checkup" | `interested-checkup` | What the first visit includes (exam, X-rays, cleaning, treatment plan), insurance accepted list, "Book your checkup" calendar link, hours and location |

### SMS Follow-Ups for BrightSmile

- After Email 3 (non-openers): "Hey {{contact.first_name}}, did you see the story about how one of our patients saved $4,000? Check your email -- it is worth the read. - BrightSmile Dental"
- After Email 6 (non-openers): Resend with subject "{{contact.first_name}}, your free exam offer is inside"

### Re-Engagement for BrightSmile

**Smart List:** "Cold Dental Guide Leads"
- Tag `lead-magnet-dental-guide` + NO tag `exam-booked` + NO tag `active-patient` + 30+ days since download

**3-Email Re-Engagement:**
1. **"We have new evening and Saturday hours"** -- New angle: convenience was probably the barrier. Mention extended hours (evenings until 7 PM, Saturday 8 AM-2 PM), new online booking, same-day emergency appointments
2. **"Free exam + free whitening consultation"** -- Escalated offer: bundle the exam with a complimentary whitening consultation ($100 additional value). "Because you downloaded our dental guide, we know you care about your smile. Let us help."
3. **"Should we stop sending you dental tips?"** -- Breakup email with trigger links for "Keep me in the loop" (tag: `newsletter-opt-in`) and "Stop emailing me" (tag: `opt-out-requested`). Default no-response to quarterly newsletter.

**Build the complete BrightSmile system** -- all the workflows, Smart Lists, and trigger links. Use the same step-by-step approach as the Sunrise Wellness exercises.

---

## Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media, Web Design, retainers $2,000-$10,000/month) needs a marketing campaign system to generate and nurture leads. The agency currently gets leads from referrals and cold outreach. They want to build an inbound marketing engine that attracts business owners through valuable content and converts them into strategy session bookings.

**Your Task:** Design and build a complete marketing campaign system for Elevate Digital Agency. Build everything in your existing sub-account with "Elevate" in the naming.

### Lead Magnet: "Free SEO Audit Checklist"

**Funnel: "Elevate - Free SEO Audit Checklist"**

**Landing Page Content:**
- **Headline:** "Is Your Website Invisible on Google? Find Out in 10 Minutes."
- **Subheadline:** "Download our free 47-point SEO Audit Checklist -- the same checklist our team uses for clients generating $50K-$500K/month in organic traffic"
- **Benefits:**
  - "Identify the 5 technical SEO issues that kill 80% of websites' rankings"
  - "Check if your site passes Google's Core Web Vitals (and what to fix if it does not)"
  - "Discover which keywords you SHOULD be ranking for but are not"
  - "Get a prioritized action list: fix these 10 things first for the biggest impact"
- **Social proof:** "Used by 1,200+ business owners. Average ranking improvement: 340% within 6 months."
- **Sample preview:** Show 5 of the 47 checklist items so visitors see the quality and want the rest

**Form Fields:**

| Field | Type | Required | Maps To |
|-------|------|----------|---------|
| First Name | Text | Yes | Contact: First Name |
| Business Email | Email | Yes | Contact: Email |
| Website URL | Text | Yes | Custom Field: Website URL |
| Monthly Revenue Range | Dropdown | Yes | Custom Field: Monthly Revenue Range |

**Dropdown options for Monthly Revenue Range:**
- Under $10K/month
- $10K-$50K/month
- $50K-$200K/month
- $200K-$500K/month
- $500K+/month

> **Why ask for Website URL and Revenue?** The website URL lets Elevate do a quick manual review before the strategy call (huge competitive advantage -- you can reference specific issues from their site during the call). The revenue range qualifies the lead -- a $500K/month business is a very different prospect than a $10K/month startup. Both are worth nurturing, but the sales approach and pricing will differ.

**Thank-You Page:**
- "Your SEO Audit Checklist is on its way!"
- **Bonus CTA:** "Want us to run the audit FOR you? Book a free 30-minute strategy session and we will review your site live." (links to Day 4 strategy session calendar)

### 7-Email Nurture Sequence for Elevate

**Workflow Name:** "Elevate: SEO Checklist Nurture Sequence"
**Tag on entry:** `lead-magnet-seo-checklist`

**Dynamic opportunity value based on revenue range (set in workflow):**
- Under $10K/month --> Opportunity value: $2,000/month
- $10K-$50K/month --> Opportunity value: $3,000/month
- $50K-$200K/month --> Opportunity value: $5,000/month
- $200K-$500K/month --> Opportunity value: $7,500/month
- $500K+/month --> Opportunity value: $10,000/month

Use If/Else branching on the Monthly Revenue Range custom field to set the opportunity value.

| Email | Day | Subject | Content Focus |
|-------|-----|---------|---------------|
| 1 | 0 | "Your SEO Audit Checklist is here" | Checklist delivery + quick-start tip: "Start with items 1-10 -- they cover 60% of common issues and you can check them in under 15 minutes." Brief agency intro: results-focused, transparent reporting, no long-term contracts |
| 2 | 2 | "Why your competitors are outranking you (it is not what you think)" | Value: explain that most ranking gaps are not about content quality but about technical SEO foundations and backlink authority. Provide 3 quick wins they can implement today. No pitch |
| 3 | 4 | "How we helped TechFlow grow from 2K to 47K monthly visitors" | Detailed case study with real numbers. **Trigger links:** "I need help with SEO," "I need help with PPC/Google Ads," "I need help with Social Media," "I need a new website" |
| 4 | 7 | "The 3 marketing metrics that actually matter" | Teach: CAC (Customer Acquisition Cost), LTV (Lifetime Value), and ROAS (Return on Ad Spend). Show how Elevate tracks and optimizes these for every client. Include a simple formula they can calculate for their own business |
| 5 | 9 | "What our clients say (in their own words)" | 3-4 client testimonials with specific results: "187% increase in organic traffic in 6 months," "$34K in new revenue from PPC in month 3," "Cut our cost-per-lead by 62%." Include client names, industries, and starting revenue ranges |
| 6 | 11 | "Your free strategy session is waiting" | Free 30-minute strategy session offer. "We will review your website live, identify your 3 biggest growth opportunities, and give you a prioritized action plan -- whether you hire us or not. Zero sales pressure." |
| 7 | 14 | "Last call: free strategy session spots are filling up" | Final push. Mention limited availability (only 3 strategy sessions per week). "We reviewed your website URL when you signed up and we already have some observations we would love to share with you." Direct calendar link |

### Trigger Links for Elevate

| Trigger Link (in Email 3) | Tag | Follow-Up Email Content |
|---------------------------|-----|-------------------------|
| "I need help with SEO" | `interested-seo` | Detailed SEO case study with month-by-month traffic growth chart, Elevate's SEO process (technical audit, content strategy, link building, monthly reporting), typical results timeline (3-6 months for meaningful gains), "Book your free strategy session" link |
| "I need help with PPC/Google Ads" | `interested-ppc` | PPC case study with ROAS numbers and ad spend vs. revenue breakdown, Elevate's PPC management approach (keyword research, ad copy testing, landing page optimization, weekly optimization calls), "Most clients see positive ROI within 30 days," strategy session link |
| "I need help with Social Media" | `interested-social` | Social media portfolio with engagement metrics, content calendar example, Elevate's social media management process (brand voice development, content creation, community management, monthly analytics), strategy session link |
| "I need a new website" | `interested-web-design` | Website portfolio with before/after screenshots and conversion rate improvements, Elevate's design process (discovery workshop, wireframes, design mockups, development, QA, launch), typical project timeline (6-10 weeks), pricing range ($7,500-$25,000 depending on scope), strategy session link |

### SMS Follow-Ups for Elevate

- After Email 3 (non-openers): "Hey {{contact.first_name}}, I sent you a case study about how we grew a client's traffic by 2,250% -- check your email when you get a chance. Worth the read. - Elevate Digital"
- After Email 6 (non-openers): Resend with subject "{{contact.first_name}}, I have some notes on your website"

> **Note on tone:** Agency nurture emails should be professional but not corporate. Write like a smart peer, not a sales brochure. Business owners get dozens of "we can grow your business" emails. Stand out by being specific, citing real numbers, and offering genuine value before asking for anything.

### Re-Engagement for Elevate

**Smart List:** "Cold SEO Checklist Leads"
- Tag `lead-magnet-seo-checklist` + NO tag `strategy-call-booked` + NO tag `active-client` + 30+ days since download

**3-Email Re-Engagement:**
1. **"Google just released a major algorithm update -- here is what it means for your site"** -- New angle: timely and relevant. Reference a real or hypothetical Google update. Provide 3 action items they should check on their site. Position Elevate as the expert who stays on top of changes
2. **"Free website audit + competitor analysis"** -- Escalated offer: instead of just a strategy session, offer a full written audit of their website plus a competitor analysis showing where they are winning and losing against their top 3 competitors. "This is a $500 deliverable we are offering free because we want to show you what we can do"
3. **"Should we stop sending you marketing tips?"** -- Breakup email with trigger links for "Keep me in the loop" (monthly marketing tips newsletter) and "Stop emailing me." Default no-response to quarterly newsletter

**Build the complete Elevate system** -- all the workflows, Smart Lists, and trigger links. Use the same step-by-step approach as the Sunrise Wellness exercises.

---

## Day 16 Recap

**What You Built Today:**
- A lead magnet funnel (landing page + form + thank-you page) that captures leads with a valuable free offer
- A 7-email nurture sequence that builds trust over 14 days and converts leads with a timed coupon offer
- SMS follow-up triggers for non-openers that recover leads who miss critical emails
- Trigger link segmentation that automatically routes leads into interest-specific follow-up workflows
- A 3-email re-engagement campaign that reactivates cold leads or gracefully moves them to low-frequency contact
- Campaign analytics Smart Lists and a conversion funnel tracking template

**Key Marketing Concepts:**

1. **Lead magnets attract, nurture sequences convert.** The meal plan gets people into your system. But it is the 14 days of trust-building emails that turn a stranger into someone willing to book a trial. Skipping the nurture and going straight to the offer is like proposing marriage on a first date.

2. **Timing matters more than content.** A perfectly written offer email sent on Day 1 will convert less than an average offer email sent on Day 11. The lead needs time to trust you, and that trust is built through consistent value delivery over multiple touchpoints.

3. **Trigger links turn passive readers into active segments.** When someone clicks "I am interested in Personal Training," they have just told you exactly what to sell them. That one click is worth more than 100 demographic data points because it is a behavioral signal -- they took an action that reveals intent.

4. **Re-engagement is not optional -- it is ROI optimization.** You already paid to acquire those leads (through ad spend, content creation, or time). Letting them go cold without trying to re-engage them is throwing away that investment. Even a 5% reactivation rate from the re-engagement campaign means more revenue for zero additional acquisition cost.

5. **List hygiene protects deliverability.** The "should we stop emailing you?" email is not just polite -- it is strategic. Email providers track engagement rates. If you keep emailing people who never open your emails, your sender reputation drops and MORE of your emails land in spam -- including the ones going to people who actually want them. Removing disengaged contacts makes your remaining campaigns more effective.

**Certification Review Questions:**

1. Why does the nurture sequence wait until Email 6 (Day 11) to make an offer instead of including a CTA in every email?
2. Explain how trigger links enable behavioral segmentation. Why is a trigger link click a stronger signal than a custom field value?
3. What is the purpose of the SMS follow-up after Email 3 specifically? Why not after every email?
4. Why does the re-engagement sequence include a "breakup" email? What would happen to your email deliverability if you kept emailing disengaged contacts indefinitely?
5. How do the Smart Lists you built today connect to the lead capture system (Day 11) and the sales pipeline (Day 12)?
6. A client asks: "Why should I give away a free meal plan? That is valuable content we could charge for." How do you explain the ROI of a lead magnet?

---

## Next Day Preview

**Day 17: Full Business Simulation** -- Tomorrow is the capstone of Phase 2. You will run Sunrise Wellness Studio through a complete business simulation: new leads arriving through the marketing campaign you built today, flowing through the lead capture system (Day 11), entering the sales pipeline (Day 12), booking appointments (Day 13), making payments (Day 14), and going through onboarding (Day 15). You will trace multiple leads through the entire journey, identify any gaps between systems, and stress-test the automation. By the end of Day 17, every system you have built in Phase 2 will be verified as a single, cohesive business operation.

**Before Day 17, make sure you have:**
- The lead magnet funnel published and workflow active (today's work)
- All Day 11-15 systems built, tested, and published
- At least 3-5 test contacts in your system with various tags and pipeline stages
- Your pipelines (Membership Sales + Member Onboarding) visible and accessible
- All Smart Lists from Days 11-16 created and returning results (even if test data)
- Your email and SMS templates from Day 3 still functional
- Your calendar booking links from Day 4 still active
