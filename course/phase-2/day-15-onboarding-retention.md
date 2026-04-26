# Day 15: Client Onboarding & Retention System

**Time Required:** 3-4 hours
**Combines:** Pipelines (D5) + Workflows (D9) + Memberships/Community (D10) + Conversations (D3) + Contacts/Smart Lists (D2)
**Level:** Intermediate to Advanced

---

## Today's Mission

Getting a new member through the door is a win. But the REAL win? Keeping them for years.

Think about it: you have spent Days 11-14 building systems that capture leads, move them through a sales pipeline, book appointments, and collect payments. Those systems are generating new Sunrise Wellness Studio members. But what happens AFTER someone signs up? Right now, the answer is... nothing. They get a membership, maybe an awkward "welcome" handshake, and then they are on their own. Some figure it out. Many do not. And the ones who do not? They cancel within 60 days, and you lose them forever -- along with every marketing dollar you spent acquiring them.

Here is the business reality: **it costs 5x more to acquire a new member than to retain an existing one.** A member who stays 24 months is worth 24x more revenue than a member who cancels after one month. Retention is not a "nice to have" -- it is the single biggest lever for studio profitability.

Today you will build Sunrise Wellness Studio's complete member lifecycle system. From the moment someone signs up, they enter a guided onboarding experience: a welcome sequence, first-session nudges, 2-week and 30-day check-ins, community integration, engagement monitoring, churn detection when they start slipping, and win-back campaigns if they leave. By the end of today, no member falls through the cracks -- ever.

---

## What You'll Combine

| Phase 1 Feature | Where You Built It | Role in Today's System |
|------------------|--------------------|------------------------|
| Onboarding Pipeline (D5) | Day 5, Exercise 5.5 | Tracks each new member through their first 30 days |
| Workflows (D9) | Day 9, all exercises | Automated check-ins, stage progression, churn alerts |
| Community (D10) | Day 10, Part 3 | Tier-based member portal access granted during onboarding |
| Smart Lists (D2) | Day 2, Exercise 2.5 | Identify at-risk members and highly engaged members |
| Email/SMS Templates (D3) | Day 3, all exercises | Onboarding emails, check-in messages, win-back offers |
| Custom Fields (D2) | Day 2, Exercise 2.1 | Track engagement metrics, join date, last visit |
| Tags (D2) | Day 2, Exercise 2.4 | Membership tier, engagement level, churn risk |
| Contacts (D2) | Day 2, all exercises | Core CRM records updated throughout the lifecycle |

---

## The System Architecture

This is the complete member lifecycle you are building today. Study it before you start -- every exercise maps to a section of this flow.

```
[New Member Signs Up]
(from Day 12 Sales Pipeline: Opportunity status = "Won")
        |
        v
[ONBOARDING PIPELINE: "Welcome" Stage]
  - Welcome email with membership guide
  - Community access granted (tier-based)
  - Tag: "member-{tier}" + "onboarding"
        |
        v
[Day 1-3: "Orientation" Stage]
  - "Book your first session" prompt
  - Class schedule + recommendations based on goals
  - Community intro prompt: "Say hello!"
        |
        v
[Day 4-7: "First Session Complete" Stage]
  - Post-first-session check-in
  - "How was your experience?" message
  - Recommend next class based on Fitness Goals field
        |
        v
[Day 14: "2-Week Check-In" Stage]
  - Engagement check: attended 3+ sessions?
  - Engaged --> celebration email + referral nudge
  - Not engaged --> re-engagement offer
        |
        v
[Day 30: "30-Day Review" Stage]
  - Satisfaction survey
  - Upgrade offer (Basic --> Premium path)
  - Referral program invitation
        |
        v
[Ongoing: "Established Member"]
  - Monthly engagement monitoring
  - Quarterly check-ins
  - Annual renewal reminders
        |
        v
[CHURN DETECTION LAYER -- runs in parallel]
  - No visit in 14 days --> "We miss you!" email
  - No visit in 21 days --> Personal SMS + tag "churn-risk"
  - No visit in 30 days --> Win-back offer + manager alert
  - Cancellation request --> Save sequence
```

---

## Part 1: Enhance the Onboarding Pipeline (30 min)

### Why This Matters

On Day 5 you built a basic Onboarding Pipeline with a few stages. That was fine for learning pipelines. But now you need it to serve as the backbone of a real retention system -- each stage represents a milestone in the member's first 30 days, and your workflows will move opportunities through these stages automatically based on what the member does (or does not do).

### Exercise 15.1: Rebuild the Onboarding Pipeline Stages

**Purpose:** Transform your Day 5 Onboarding Pipeline into a detailed member lifecycle tracker with clear stage definitions.

Navigate to **Opportunities > Pipelines** and open (or create) the **"Member Onboarding"** pipeline.

Update the stages to match this structure:

| Stage | What It Means | How They Enter | Expected Duration |
|-------|---------------|----------------|-------------------|
| Welcome | Just signed up, no actions taken yet | Automatically when they become a member | 0-1 day |
| Orientation | Received welcome materials, exploring options | Workflow moves them after welcome email delivered | 1-3 days |
| First Session Scheduled | They have booked their first appointment | Workflow detects a calendar booking | 1-5 days |
| First Session Complete | They attended their first session | Appointment marked "Showed" | Same day |
| 2-Week Check-In | Checking engagement at the 14-day mark | Workflow triggers at day 14 | Day 14-15 |
| 30-Day Review | Full review of their first month | Workflow triggers at day 30 | Day 30-31 |
| Established Member | Fully onboarded and in ongoing retention | After 30-day review completes | Indefinite |

**For each stage:**
1. Click **Add Stage** or edit existing stages
2. Name the stage exactly as shown above
3. Drag them into the correct left-to-right order

**Set opportunity defaults:**
- **Pipeline Name:** Member Onboarding
- **Opportunity Name Convention:** "{Contact Name} - {Membership Type} - Onboarding"
- **Monetary Value:** Set to the monthly rate of their membership ($79, $149, or $249)

> **Why 7 stages?** Each stage maps to a specific automated touchpoint. When you build your workflows in Parts 2-4, the pipeline becomes your visual dashboard -- you can glance at it and instantly see: "We have 12 people in Orientation, 5 waiting on their first session, and 2 who need their 2-week check-in." Without these stages, you are flying blind.

---

## Part 2: Welcome and First Week Automation (45 min)

This is where the magic starts. You are going to build two workflows that handle the critical first 7 days of every new member's experience -- the period that determines whether they stick around or disappear.

### Exercise 15.2: Build the "New Member Welcome" Workflow

**Purpose:** Automatically welcome every new member, deliver their onboarding materials, grant community access, and nudge them to book their first session -- all without manual intervention.

Navigate to **Automation > Workflows** and click **+ Create Workflow > Start from Scratch**.

**Workflow Name:** "Onboarding: New Member Welcome Sequence"

**Step 1 -- Set the Trigger:**

Click **Add New Trigger** and select **Pipeline Stage Changed**.

Configure it:
- **Pipeline:** Member Onboarding
- **Stage:** Welcome

This means: every time an opportunity enters the "Welcome" stage of the Onboarding pipeline, this workflow fires. In your Day 12 system, when a sales opportunity is marked "Won," it should create a new opportunity in this Onboarding pipeline at the "Welcome" stage. If you did not set that up on Day 12, add it now as a workflow action in your sales pipeline "Won" workflow.

**Step 2 -- Day 0: Welcome Email**

Add action: **Send Email**

- **Template:** Create a new email or reuse/modify your "Sunrise Welcome Email" from Day 7
- **Subject:** "Welcome to Sunrise Wellness, {{contact.first_name}}! Here's everything you need"
- **Body should include:**
  - Warm, personal greeting using their first name
  - Their membership tier and what it includes (reference the Membership Type custom field)
  - Link to the class schedule (your Day 4 calendar booking links)
  - Community access link (your Day 10 community URL)
  - "Your first step: book your first session!" with a clear CTA button
  - Contact info if they have questions

> **Pro Tip:** Write the email as if Sarah, the studio owner, is personally welcoming them. Use "I" not "we." Members who feel personally welcomed are 3x more likely to attend their first session within the first week.

**Step 3 -- Day 0: Grant Community Access**

Add action: **Add Tag**
- If the contact has tag "member-basic" --> add tag "community-general"
- If "member-premium" --> add tags "community-general" + "community-premium"
- If "member-vip" --> add tags "community-general" + "community-premium" + "community-vip"

To implement this, use **If/Else** branching:
1. Add an **If/Else** action
2. **If** Contact Tag contains "member-vip" --> Add tags: "community-general", "community-premium", "community-vip"
3. **Else If** Contact Tag contains "member-premium" --> Add tags: "community-general", "community-premium"
4. **Else** --> Add tag: "community-general"

These tags should correspond to your Day 10 Community group access rules. Members with the right tags automatically get access to their tier's community content.

**Step 4 -- Day 0: Move to Orientation Stage**

Add action: **Update Opportunity**
- **Pipeline:** Member Onboarding
- **Stage:** Orientation

**Step 5 -- Day 1: "Book Your First Session" Email**

Add action: **Wait** --> 1 day

Add action: **Send Email**
- **Subject:** "{{contact.first_name}}, let's get your first session on the calendar!"
- **Body should include:**
  - Acknowledge they are new and might not know where to start
  - Based on their Fitness Goals custom field, recommend a specific class:
    - Weight Loss --> "Try our HIIT Burn class -- it is our most popular for results"
    - Flexibility --> "Our Yoga Flow class on Tuesday mornings is perfect for you"
    - Strength --> "Check out Power Pilates -- low impact, high results"
    - General Fitness --> "HIIT Burn is a great starting point for all fitness levels"
  - Direct booking link to the recommended calendar (from Day 4)
  - Reassurance: "Everyone is a beginner at first. Our instructors will guide you through everything."

> **Implementation Note:** If you cannot dynamically branch by Fitness Goals in the email body, create separate email templates for each goal and use If/Else branching in the workflow to send the right one. Alternatively, use a single email with a general recommendation and add the personalized detail as a P.S. line.

**Step 6 -- Day 3: First Nudge (If No Booking)**

Add action: **Wait** --> 2 days (total of 3 days from sign-up)

Add action: **If/Else**
- **Condition:** Contact has tag "first-session-booked" (you will set this tag in your Day 13 appointment system or add a workflow trigger when they book any appointment)
- **If YES (already booked):** Go to End / do nothing
- **If NO (has not booked):**
  - Send SMS: "Hey {{contact.first_name}}! Your Sunrise Wellness membership is active -- have you checked out the class schedule yet? Book your first session here: [CALENDAR_LINK]. We can't wait to see you! - Sarah"
  - Internal notification to yourself: "New member {{contact.first_name}} {{contact.last_name}} has not booked after 3 days"

**Step 7 -- Day 5: Stronger Nudge (If Still No Booking)**

Add action: **Wait** --> 2 more days

Add action: **If/Else** (same condition: no "first-session-booked" tag)
- **If still no booking:**
  - Send Email: Subject "Need help choosing your first class, {{contact.first_name}}?"
  - Body: More personal tone. Offer to help them choose. Mention that many new members feel unsure. Include a "Reply to this email and I'll personally recommend a class for you" CTA.
  - Create a **Task** assigned to yourself: "Call {{contact.first_name}} -- hasn't booked first session after 5 days" with a due date of tomorrow

> **Why the escalation?** Day 1 is a helpful nudge. Day 3 is a gentle reminder. Day 5 is a personal outreach because if they have not booked in 5 days, an automated email alone will not fix it. The system detects the risk and brings a human into the loop. This is the right balance of automation and personal touch.

**Save and publish the workflow.**

---

### Exercise 15.3: Build the "First Session Celebration" Workflow

**Purpose:** When a new member completes their first session, celebrate it, recommend what to do next, and move them forward in the onboarding pipeline.

Create a new workflow: **"Onboarding: First Session Complete"**

**Trigger:** Appointment Status Changed
- **Status:** Showed
- **Calendar:** (select your PT, HIIT, Yoga, and Pilates calendars -- or use "Any Calendar")

**Add a Filter:** Only fire for contacts who have the tag "onboarding"

This ensures the workflow only fires for NEW members completing their FIRST session, not established members attending their regular sessions.

**Action 1: Add Tag**
- Add tag: "first-session-complete"
- Remove tag: "onboarding" (they are now past the initial onboarding nudge phase)

**Action 2: Update Opportunity**
- **Pipeline:** Member Onboarding
- **Stage:** First Session Complete

**Action 3: Send Email (Celebration + Next Steps)**
- **Subject:** "You did it, {{contact.first_name}}! Here's what's next"
- **Body:**
  - Celebrate: "Your first session is in the books! That's the hardest one -- showing up is literally the biggest step."
  - Ask how it went: "Hit reply and let me know how you felt afterward!"
  - Recommend next class based on Fitness Goals custom field (same logic as Exercise 15.2, Step 5)
  - Community CTA: "Introduce yourself in the community and share how your first session went! [COMMUNITY_LINK]"
  - Tease the schedule: "Here's what's coming up this week: [CALENDAR_LINK]"

**Action 4: Wait 1 Day, Then Prompt Community Intro**

Add a **Wait** --> 1 day

Add action: **Send SMS**
- "Hey {{contact.first_name}}! Have you had a chance to check out the Sunrise Wellness community? It's where our members share tips, stay motivated, and connect. Jump in and say hi: [COMMUNITY_LINK] - Sarah"

**Save and publish.**

> **Pro Tip:** This workflow has a subtle but powerful effect. By celebrating the first session and immediately providing a clear "next step," you eliminate the post-first-visit uncertainty that causes many members to hesitate and eventually drop off. The community prompt on Day 2 adds social connection, which is the strongest retention lever of all -- people do not quit a community, they quit a gym.

---

## Part 3: Engagement Monitoring and Check-Ins (45 min)

The first week is handled. Now you need systems for the two critical retention milestones: 14 days and 30 days. These are not arbitrary -- industry data shows that member engagement at these two checkpoints strongly predicts long-term retention.

### Exercise 15.4: Build the "2-Week Check-In" Workflow

**Purpose:** At the 14-day mark, automatically check how engaged the new member is and respond accordingly -- celebrate the engaged ones, reach out to the ones who are slipping.

Create a new workflow: **"Onboarding: 2-Week Check-In"**

**Trigger:** Tag Added
- **Tag:** "member-basic" OR "member-premium" OR "member-vip"

This fires when someone first becomes a member (the tag is added during signup or by your Day 12 workflow).

**Action 1: Wait 14 Days**

Add action: **Wait** --> 14 days

This is why the tag-added trigger works well here: the wait starts from the exact moment they became a member.

**Action 2: Update Opportunity**

Move their Onboarding Pipeline opportunity to the **"2-Week Check-In"** stage.

**Action 3: If/Else -- Check Engagement**

Here is where you evaluate whether this member is on track:

- **Condition:** Contact has tag "first-session-complete" AND custom field "Sessions Attended" >= 3

> **Note on Tracking Sessions:** The "Sessions Attended" custom field needs to be incremented each time an appointment is marked "Showed." You can add this as an action in a simple workflow: Trigger = Appointment Status Changed to "Showed" --> Action = Update Custom Field "Sessions Attended" + 1. Build this helper workflow first if you have not already.

**If ENGAGED (3+ sessions):**
1. Send Email: "You're Crushing It, {{contact.first_name}}!"
   - Celebrate their consistency: "You've attended {{contact.sessions_attended}} sessions in your first two weeks -- that puts you ahead of 80% of new members!"
   - Tease what is coming: mention an upcoming class they have not tried, or a community event
   - Soft referral ask: "Know someone who'd love Sunrise Wellness? When they sign up, you both get a free PT session!"
   - Add tag: "engaged-2wk"

**If NOT ENGAGED (fewer than 3 sessions):**
1. Send Email: "We've Noticed You Haven't Been In Lately, {{contact.first_name}}"
   - Empathetic tone -- do not guilt them: "Life gets busy, and we totally get it."
   - Ask what is holding them back: "Is it scheduling? Not sure which class to try? Just reply and let me know -- I'm here to help."
   - Include an incentive: "Book a session this week and I'll throw in a free 30-minute nutrition consultation -- my way of helping you get the most out of your membership."
   - Add tag: "needs-engagement-2wk"

**Save and publish.**

---

### Exercise 15.5: Build the "30-Day Review" Workflow

**Purpose:** At the 30-day mark, conduct a full satisfaction check, present upgrade opportunities, invite them to the referral program, and graduate them from onboarding.

Create a new workflow: **"Onboarding: 30-Day Review"**

**Trigger:** Tag Added
- **Tag:** "member-basic" OR "member-premium" OR "member-vip" (same as 15.4)

**Action 1: Wait 30 Days**

**Action 2: Update Opportunity**
- Move to **"30-Day Review"** stage in the Onboarding Pipeline

**Action 3: Send Satisfaction Survey Email**
- **Subject:** "Your first month at Sunrise Wellness -- how did we do?"
- **Body:**
  - Acknowledge the milestone: "Can you believe it has been a month already?"
  - Link to a survey (reuse your Day 8 survey skills):
    - Overall satisfaction (1-5 stars or scale)
    - Favorite class/service so far
    - What would you improve?
    - Would you recommend Sunrise Wellness to a friend? (1-10 NPS score)
  - Make it short: "It takes less than 2 minutes and helps us make your experience even better."

> **Pro Tip:** You can build this survey using GHL's survey builder (Day 8) and trigger a workflow when the survey is submitted to update the contact's custom fields with their responses. This gives you searchable satisfaction data in your CRM.

**Action 4: Wait 2 Days (Give Time to Complete Survey)**

**Action 5: If/Else -- Upgrade Opportunity**

- **Condition:** Contact has tag "member-basic"

**If BASIC member:**
- Send Email: "Get More From Sunrise Wellness -- Upgrade to Premium"
  - Compare what they have vs. what Premium includes
  - Highlight the specific Premium benefits that match their Fitness Goals
  - Include a special upgrade offer: "Upgrade this week and get your first month of Premium at the Basic rate -- just $79 instead of $149"
  - Trigger link: "I'm interested in upgrading" (tracks interest even if they do not upgrade immediately)

**If PREMIUM member:**
- Send Email about VIP benefits (similar structure, different comparison)

**If VIP member:**
- Skip the upgrade email (they are already at the top tier)
- Instead, send an exclusive "VIP Thank You" email with a personal touch

**Action 6: Referral Program Invitation**

Add action: **Send Email** (for all tiers)
- **Subject:** "Love Sunrise Wellness? Share it and earn rewards"
- **Body:**
  - Introduce the referral program
  - Benefit: "When your friend signs up, you get a free PT session ($75 value) and they get 20% off their first month"
  - Make it easy: include a shareable referral link or unique coupon code
  - Social proof: "Sarah T. referred 3 friends last month and earned 3 free PT sessions!"

**Action 7: Graduate to Established Member**

Add action: **Wait** --> 2 days

Add action: **Update Opportunity**
- Move to **"Established Member"** stage

Add action: **Remove Tag** --> "onboarding" (if still present)
Add action: **Add Tag** --> "established-member"

**Save and publish.**

> **Why graduate them?** Moving members from "onboarding" to "established" is not just organizational -- it changes which workflows apply to them. Onboarding workflows stop firing (because they check for the "onboarding" tag), and ongoing retention workflows (Part 4) start applying. This clean handoff prevents members from getting duplicate messages.

---

## Part 4: Churn Detection and Win-Back (45 min)

This is the safety net. Even with a great onboarding experience, some members will start drifting. The goal is to detect it EARLY and intervene BEFORE they cancel.

### Exercise 15.6: Build the "At-Risk Member" Detection System

**Purpose:** Automatically identify members who are disengaging and escalate the response based on how long they have been absent.

This exercise has two parts: a Smart List for quick visual checks and a workflow for automated responses.

**Part A -- Create a "Last Visit" Tracking System**

Before you can detect churn, you need to know when each member last visited. You may already have a "Last Visit Date" custom field from Day 2. If not, create it now:

1. Navigate to **Settings > Custom Fields**
2. Create a new field in the "Membership Info" folder:
   - **Name:** Last Visit Date
   - **Type:** Date

3. Build a helper workflow to keep it updated:
   - **Workflow Name:** "Helper: Update Last Visit Date"
   - **Trigger:** Appointment Status Changed --> Status: Showed (any calendar)
   - **Action:** Update Custom Field --> "Last Visit Date" = {{current_date}}

This means every time a member attends a session, their "Last Visit Date" gets updated. Simple but essential.

**Part B -- Create Smart Lists for At-Risk Members**

Navigate to **Contacts > Smart Lists** and create the following:

**Smart List 1: "No Visit in 14+ Days"**
- Filter 1: Tag contains "established-member" (only track post-onboarding members)
- Filter 2: Custom Field "Last Visit Date" is before 14 days ago
- Filter 3: Tag does NOT contain "churn-risk" (exclude already-flagged members)
- Filter 4: Custom Field "Membership Status" = Active

**Smart List 2: "Churn Risk -- Active"**
- Filter 1: Tag contains "churn-risk"
- Filter 2: Custom Field "Membership Status" = Active

**Smart List 3: "Cancelled Members -- Last 90 Days"**
- Filter 1: Custom Field "Membership Status" = Cancelled
- Filter 2: Custom Field "Cancellation Date" is within the last 90 days

> **Pro Tip:** Check these Smart Lists weekly as part of your studio management routine. The automated workflows below handle the initial outreach, but reviewing these lists helps you spot patterns -- like if a particular class time lost 5 members, maybe the new instructor is not connecting.

**Part C -- Build the "Churn Prevention" Workflow**

Create a new workflow: **"Retention: Churn Prevention Escalation"**

**Trigger:** Custom Field Changed
- **Field:** Last Visit Date
- **Condition:** This is a bit of a workaround. Since GHL does not have a "X days since last value" trigger natively, you have two options:

**Option 1 (Recommended): Date-based workflow with tag trigger**
- Create a daily/weekly "check" workflow that runs against your Smart List:
  - Go to your "No Visit in 14+ Days" Smart List
  - Manually add those contacts to the workflow (or use a scheduled campaign)
  
**Option 2: Tag-based trigger with manual monitoring**
- Create a workflow triggered by tag "check-engagement" that you add periodically

For this exercise, we will build the ACTION side -- the escalation sequence -- and you can trigger it however works best in your setup:

**Workflow Name:** "Retention: Churn Prevention Escalation"

**Trigger:** Tag Added --> "needs-reengagement"

**14-Day Absent -- Gentle Nudge:**
1. Send Email: "We Miss You at Sunrise Wellness, {{contact.first_name}}!"
   - Warm, no-pressure tone
   - Highlight what has been happening at the studio: new class, community activity, a member success story
   - "Your spot in [their usual class time] is waiting for you!"
   - Include booking link

**Wait 7 Days**

**21-Day Absent -- Personal Outreach:**
1. If/Else: Check if tag "first-session-complete" exists (did they ever actually come in?)
   - **If they attended before:**
     - Send SMS: "Hey {{contact.first_name}}, it's Sarah from Sunrise Wellness. I noticed you haven't been in for a bit and wanted to check in personally. Everything okay? If there's anything I can help with, just reply here. - Sarah"
     - Add tag: "churn-risk"
   - **If they NEVER attended:**
     - Send Email: "Let's Start Fresh, {{contact.first_name}}"
     - Offer: "Come in for a free personal orientation session -- I'll walk you through everything one-on-one"
     - Add tag: "churn-risk"

**Wait 9 Days (30 Days Total)**

**30-Day Absent -- Win-Back Offer + Human Escalation:**
1. Send Email: "A Special Offer Just for You, {{contact.first_name}}"
   - Acknowledge the gap: "We know life gets busy, and we understand."
   - Win-back offer: "Come back this week and get a free personal training session ($75 value) -- no strings attached"
   - Include a coupon code: "COMEBACK" (create this in Payments from Day 6)
   - Make it time-limited: "This offer expires in 7 days"
2. Create Task: "URGENT: Call {{contact.first_name}} {{contact.last_name}} -- 30-day absence, win-back offer sent"
   - Assign to yourself
   - Due date: tomorrow
3. Send Internal Notification: Alert yourself or the studio manager

**Save and publish.**

---

### Exercise 15.7: Build the "Win-Back Campaign" for Cancelled Members

**Purpose:** Not every member who cancels is gone forever. People cancel for temporary reasons -- they moved, had a baby, got busy at work. A well-timed win-back campaign brings some of them back.

Create a new workflow: **"Retention: Win-Back -- Cancelled Members"**

**Trigger:** Tag Added --> "cancelled-member" (add this tag in your cancellation workflow)

**Action 1: Wait 14 Days**
- Do not email them the day they cancel. Give them space. Reaching out too soon feels desperate.

**Action 2: Send Email 1 -- "Things Have Changed"**
- **Subject:** "A lot has happened at Sunrise Wellness since you left"
- **Body:**
  - Do NOT guilt them for leaving
  - Highlight genuine new additions: new classes, new equipment, new instructors, new community features
  - Keep it informational, not salesy
  - "We'd love to have you back, but no pressure. Just wanted you to know what's new."

**Action 3: Wait 14 Days**

**Action 4: Send Email 2 -- Social Proof**
- **Subject:** "See what Sunrise Wellness members are saying"
- **Body:**
  - Share 2-3 member success stories or testimonials
  - Community highlights (if you have screenshots of community activity from Day 10)
  - "Our community has grown a lot -- there are [X] members now sharing tips, celebrating wins, and motivating each other."

**Action 5: Wait 14 Days**

**Action 6: Send Email 3 -- Comeback Offer**
- **Subject:** "We saved a spot for you, {{contact.first_name}}"
- **Body:**
  - Special comeback offer: "Rejoin this month and get your first month at 50% off -- plus a free PT session to get you started fresh"
  - Coupon: "WELCOMEBACK50"
  - Time limit: "This offer is good for 7 days"
  - Easy CTA: Button linking directly to your signup funnel (Day 8/14)

**Action 7: Wait 7 Days**

**Action 8: If/Else -- Did They Rejoin?**
- **If** tag "member-basic" or "member-premium" or "member-vip" was added (they came back!):
  - Move them into the Onboarding Pipeline again at "Welcome" stage
  - Add tag: "returning-member" (so your welcome email can be slightly different)
- **If NOT:**
  - Add tag: "win-back-failed"
  - Move to monthly newsletter only (reduce email frequency to avoid being annoying)

**Save and publish.**

---

## Part 5: Member Upgrade Path (20 min)

Retention is not just about preventing cancellations -- it is also about growing the value of each member. A Basic member who upgrades to Premium is worth almost twice as much without any acquisition cost.

### Exercise 15.8: Build Automated Upgrade Prompts

**Purpose:** Identify members whose usage patterns suggest they would benefit from (and are likely to accept) a higher membership tier.

Create a new workflow: **"Retention: Upgrade Opportunity Detection"**

**Trigger:** Custom Field Changed --> "Sessions Attended"

**Branch 1: Heavy-Use Basic Members**

If/Else:
- Contact has tag "member-basic"
- AND Custom Field "Sessions Attended" >= 8 (8+ sessions per month = attending 2x/week)

**If YES:**
- Send Email: "You're Getting So Much Out of Sunrise Wellness -- Imagine Getting Even More"
  - Acknowledge their commitment: "You've attended {{contact.sessions_attended}} sessions -- that's amazing!"
  - Compare: "Right now your Basic membership gives you [X]. Premium would unlock [Y, Z] -- including classes like [specific classes they cannot currently access]"
  - Financial angle: "At the rate you're going, Premium actually saves you money per session"
  - Trigger Link: "Tell me more about Premium" (tracks interest for follow-up)
  - Trigger Link: "I'm happy with Basic" (stops future upgrade emails for 90 days)
- Add tag: "upgrade-prompt-sent"

**Branch 2: Premium Members Using Nutrition Services**

If/Else:
- Contact has tag "member-premium"
- AND tag "nutrition-consultation-booked" exists (set when they book a nutrition calendar from Day 4)

**If YES:**
- Send Email: "You Love Nutrition Coaching -- VIP Gives You Unlimited Access"
  - Highlight: "VIP includes unlimited nutrition coaching sessions (a $75 value each time) plus [other VIP perks]"
  - Trigger Link: "Tell me more about VIP"
  - Trigger Link: "Not right now"
- Add tag: "upgrade-prompt-sent"

> **Pro Tip:** Be careful not to over-send upgrade emails. Use the "upgrade-prompt-sent" tag to prevent sending more than one upgrade email per quarter. Add a condition at the start of each branch: If tag "upgrade-prompt-sent" was added MORE than 90 days ago (or does not exist), proceed. Otherwise, stop.

**Save and publish.**

---

## Integration Checkpoint

Before moving on, verify each piece is connected to the others. Walk through this checklist:

- [ ] **Pipeline:** Member Onboarding pipeline has 7 stages (Welcome through Established Member) and displays correctly in the Opportunities view
- [ ] **Welcome Automation:** New members entering the pipeline trigger a welcome email + community access + booking nudges on Days 1, 3, and 5
- [ ] **First Session:** When a new member's appointment is marked "Showed," they get a celebration email and their pipeline stage updates automatically
- [ ] **2-Week Check-In:** At 14 days, engaged members get a celebration message and disengaged members get a re-engagement offer
- [ ] **30-Day Review:** At 30 days, members receive a satisfaction survey, upgrade offer (if applicable), and referral program invitation, then graduate to "Established Member"
- [ ] **Churn Detection:** Smart Lists correctly identify members with no visit in 14+ days, and the escalation workflow sends progressively more urgent outreach at 14, 21, and 30 days
- [ ] **Win-Back:** Cancelled members receive a 3-email sequence over 6 weeks with a comeback offer
- [ ] **Upgrades:** High-usage Basic and Premium members receive targeted upgrade prompts with trigger link tracking
- [ ] **No Conflicts:** Onboarding workflows only fire for contacts with the "onboarding" tag, and retention workflows only fire for "established-member" contacts -- no overlap

**Test the full flow** by creating a test contact, adding them to the Onboarding Pipeline at "Welcome," and verifying that the first workflow fires. Check each workflow's execution log for errors.

---

## Case Scenario 1: BrightSmile Dental -- Patient Retention System

BrightSmile Dental loses 30% of new patients after their first visit because there is no follow-up system. Dr. Martinez wants a patient lifecycle that ensures every new patient feels cared for and returns for their recommended treatments.

**Your Challenge:** Adapt today's system for a dental practice.

**Onboarding Pipeline -- "New Patient Journey":**
| Stage | Dental Equivalent |
|-------|-------------------|
| Welcome | Patient registered, paperwork complete |
| First Visit Scheduled | Initial exam/cleaning booked |
| First Visit Complete | Exam done, treatment plan presented |
| 1-Week Follow-Up | Post-visit check-in, treatment acceptance |
| Treatment In Progress | Patient is completing recommended treatments |
| Recall Scheduled | 6-month cleaning scheduled |
| Established Patient | Active in recall system |

**Key Workflows to Build:**

1. **New Patient Welcome:** Registration triggers welcome email with office info, what to expect at first visit, parking instructions, insurance FAQ, and patient portal access

2. **Post-First-Visit Follow-Up:** After first exam, send a summary of findings plus the treatment plan. If treatment was recommended, follow up in 48 hours: "Do you have any questions about the treatment plan Dr. Martinez discussed?" If they have not scheduled treatment within 7 days, send a reminder with financing options

3. **6-Month Recall System:** This is the dental equivalent of your churn detection:
   - 5 months after last cleaning --> "Your 6-month cleaning is coming up! Book now for the best times"
   - 6 months --> "It's time for your cleaning! [BOOKING_LINK]"
   - 6.5 months --> SMS: "Hi {{contact.first_name}}, we noticed you haven't scheduled your cleaning yet. Regular cleanings prevent costly issues down the road. Book here: [LINK]"
   - 7 months --> "We're concerned about your dental health" email + task for office manager to call
   - 12 months overdue --> Win-back: "It's been a while! Come back with a free exam -- on us" + special offer

4. **Annual Check-Up Reminder:** For patients with annual insurance benefits: "You have {{contact.insurance_remaining}} in unused dental benefits that expire December 31. Don't leave money on the table -- schedule your remaining treatments now."

5. **Win-Back for Lost Patients:**
   - Patients with no visit in 18+ months
   - "We've upgraded! New technology, same caring team"
   - Comeback offer: complimentary exam
   - If no response --> reduce to annual holiday card only

**Think About:** What custom fields does BrightSmile need that Sunrise Wellness does not? (Hint: insurance provider, last cleaning date, treatment plan status, preferred hygienist, next recall date)

---

## Case Scenario 2: Elevate Digital Agency -- Client Retention System

Elevate Digital Agency has a 70% client retention rate at 12 months -- decent, but the CEO wants to push it to 85%. The problem is not results -- clients are getting good ROI -- the problem is that nobody TELLS them about the results consistently, so clients feel neglected and shop around.

**Your Challenge:** Adapt today's system for a B2B agency.

**Onboarding Pipeline -- "Client Success Journey":**
| Stage | Agency Equivalent |
|-------|-------------------|
| Welcome | Contract signed, kickoff scheduled |
| Kickoff Complete | Strategy session done, deliverables agreed |
| 30-Day Results Preview | First month performance report delivered |
| 90-Day Strategy Review | Quarterly review meeting completed |
| Established Client | Ongoing with quarterly reviews |
| Renewal Period | Contract renewal approaching (60 days out) |

**Key Workflows to Build:**

1. **Client Onboarding:** Contract signed triggers:
   - Welcome email with team introductions, communication preferences form, and portal access
   - Kickoff meeting booking link (calendar from Day 4 concepts)
   - "What to expect in your first 30 days" document
   - Slack/community channel access for real-time communication
   - Internal task: "Prepare {{contact.company}} kickoff deck"

2. **30-Day Results Preview:** Exactly 30 days after kickoff:
   - Email: "Your First 30 Days with Elevate -- Here's What We've Accomplished"
   - Include key metrics even if early: "We've published X posts, your website traffic is up Y%, and we've identified Z optimization opportunities"
   - Trigger link: "Schedule a call to discuss" (tracks engagement)
   - If they click the trigger link --> high engagement, add tag "client-engaged"
   - If they do NOT open the email in 5 days --> alert account manager to call them

3. **Quarterly Business Reviews (QBRs):**
   - Every 90 days: automated email with performance summary + QBR meeting booking link
   - Post-QBR survey: "How would you rate this quarter's performance?" (1-5)
   - If rating < 3 --> immediate alert to CEO + "save" workflow
   - If rating >= 4 --> referral ask: "Know another business that needs marketing help?"
   - Track QBR completion in a custom field -- if a client skips a QBR, that is a churn signal

4. **Churn Prevention -- Engagement Drop Detection:**
   - Client has not responded to emails in 30 days --> alert account manager
   - Client has not logged into reporting portal in 30 days --> "Here's your latest results" email with key metrics embedded directly (no login required)
   - Client mentions "cancel," "looking at other agencies," or "budget cuts" in any conversation --> tag "churn-risk" + immediate CEO notification
   - QBR rating dropped from previous quarter --> proactive outreach: "I noticed [concern], let's discuss how we can improve"

5. **Contract Renewal Automation:**
   - 90 days before contract end date --> internal alert: "Start renewal prep for {{contact.company}}"
   - 60 days out --> send "Year in Review" with full ROI summary
   - 45 days out --> if no renewal signal, schedule renewal discussion meeting
   - 30 days out --> send renewal proposal with options (same tier, upgrade, multi-year discount)
   - 14 days out --> if not renewed, escalate to CEO

6. **Win-Back for Lost Clients:**
   - Monthly newsletter with case studies and industry insights (stay top of mind)
   - 90 days after churn --> "Here's what we've been up to" + new service announcement
   - 6 months after churn --> "Let's catch up" coffee meeting invitation (no pitch, just relationship)

**Think About:** What is the biggest difference between B2C retention (Sunrise Wellness) and B2B retention (Elevate Digital)? (Hint: B2B retention is relationship-driven and requires human touchpoints at key moments. Automation handles the scheduling and reminders, but a human must show up for the QBRs, calls, and save conversations. The system's job is to make sure nothing falls through the cracks, not to replace the human relationship.)

---

## What You Built Today

Take a step back and look at what you just created:

- A **7-stage Onboarding Pipeline** that visually tracks every new member's journey
- A **Welcome Sequence** that makes every new member feel personally guided through their first week
- **Engagement Check-Ins** at 14 and 30 days that automatically adapt based on the member's activity level
- A **Churn Detection System** that catches disengaging members within 2 weeks and escalates through 3 levels of outreach
- A **Win-Back Campaign** that re-engages cancelled members over 6 weeks
- An **Upgrade Path** that identifies members who would benefit from a higher tier

This is not just automation -- it is a system that makes every member feel like the studio cares about them personally, at scale. Sunrise Wellness Studio now handles 100 members with the same personalized attention it would give 10.

Tomorrow on Day 16, you will build the marketing engine that fills this retention system with new members -- a complete lead magnet campaign system with nurture sequences, trigger link segmentation, and re-engagement campaigns.
