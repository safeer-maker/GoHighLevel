# Day 9: Automation & Workflows

**Time Required:** 3-4 hours
**Certification Alignment:** Workflow General Overview, Auto Missed Call Text-Back Recipe, No-Show Nurture Recipe
**API Lab:** Yes - `scripts/day-09-automation-api.py`

---

## Today's Mission

This is the day everything comes together.

Over the past 8 days, you have built Sunrise Wellness Studio's entire platform piece by piece: a branded business profile with custom values (Day 1), a contact database with Smart Lists (Day 2), SMS and email templates (Day 3), booking calendars for PT sessions, group classes, and nutrition consultations (Day 4), a Membership Sales pipeline and Onboarding pipeline (Day 5), products, invoices, and coupons (Day 6), email campaigns with trigger links (Day 7), and a Free Trial funnel with forms and a survey (Day 8).

But right now, every single action requires YOU to do it manually. A lead fills out the Free Trial form? You have to notice it, send a welcome email, create a pipeline opportunity, and follow up if they do not book. Someone no-shows for a PT session? You have to remember to text them. That is not scalable -- and it is exactly the problem that **workflows** solve.

Today, you will build **workflows** -- automated sequences that run 24/7 without you lifting a finger. When someone fills out the Free Trial form? Automatic welcome SMS, welcome email, pipeline opportunity, and owner notification. When someone no-shows for a PT session? Automatic rebooking sequence. When someone misses your call? Instant text-back.

This is what makes GHL powerful -- and this is the most important day of Phase 1.

---

## Learning Objectives

By the end of today, you will be able to:

1. Understand the workflow builder interface and all available triggers and actions
2. Build a multi-step automated sequence connecting forms, templates, pipelines, and calendars
3. Implement the certification-required Missed Call Text-Back and No-Show Nurture recipes
4. Create conditional workflows with If/Else branching logic
5. Test and debug workflows safely

---

## Part 1: Workflow Builder Overview (30 min)

### What is a Workflow?

A **workflow** is an automated sequence: something happens (a **trigger**), and then GHL does things automatically (a series of **actions**). You build it once, and it runs forever -- handling repetitive tasks while you focus on coaching clients and growing the business.

Think of workflows like a recipe in a cookbook. The trigger is "when the oven reaches 350 degrees" and the actions are the cooking steps that follow automatically, one after another, in order. Some recipes have decision points too -- "if the dough is sticky, add more flour; if it is dry, add water." Workflows work the same way with **If/Else conditions**.

Here is a simple example to make it concrete:

```
TRIGGER: Someone fills out a form on your website
   |
   v
ACTION 1: Send them a welcome email
   |
   v
ACTION 2: Wait 24 hours
   |
   v
ACTION 3: If they have not booked an appointment, send a follow-up
```

That is it. Three steps, and you never have to think about welcome emails or follow-ups again.

### Why Workflows Matter

Without workflows, running Sunrise Wellness Studio looks like this:
- Check the form submissions folder every hour
- Manually copy each new lead's info into an email
- Remember to follow up in 24 hours (and somehow track who you followed up with)
- Manually update the pipeline when someone books
- Somehow remember which no-shows need a rebooking text

With workflows, ALL of that happens automatically. You build the system once, and it handles hundreds of leads the exact same way, 24 hours a day, 7 days a week.

### Trigger Categories

**Triggers** are the "when" -- the event that starts a workflow. GHL offers triggers in these categories:

| Category | Examples | Sunrise Wellness Use Case |
|----------|----------|--------------------------|
| **Contact** | Created, Tag Added, Tag Removed, Custom Field Changed | When a new contact is added to the CRM |
| **Calendar** | Appointment Booked, Appointment Status Changed | When someone books a PT session (Day 4 calendars) |
| **Form/Survey** | Form Submitted, Survey Submitted | When someone fills out the Free Trial form (Day 8) |
| **Pipeline** | Opportunity Stage Changed, Opportunity Status Changed | When a deal moves to "Trial Active" (Day 5 pipeline) |
| **Conversation** | Inbound Message, Missed Call, Voicemail | When a potential member calls and you miss it |
| **Payment** | Invoice Paid, Subscription Created | When someone pays for a membership (Day 6 products) |
| **Manual** | Added to Workflow Manually | When you manually enroll a contact |
| **Webhook/API** | Webhook Received, API Trigger | External systems triggering GHL actions |

### Action Categories

**Actions** are the "then" -- what GHL does after the trigger fires:

| Category | Examples | Sunrise Wellness Use Case |
|----------|----------|--------------------------|
| **Communication** | Send SMS, Send Email, Send Voicemail Drop | Send the welcome email template from Day 3 |
| **CRM** | Add/Remove Tag, Update Custom Field, Create Opportunity | Add "new-trial-lead" tag, create pipeline opportunity |
| **Calendar** | Book Appointment | Auto-book a tour or first session |
| **Internal** | Send Notification, Add Task | Notify yourself about a new high-value lead |
| **Logic** | Wait, If/Else, Go To, Goal | Wait 24 hours, then check if they booked |
| **External** | Webhook, HTTP Request | Send data to external tools or your Python scripts |

> **Pro Tip:** You do not need to memorize every trigger and action. The workflow builder shows them all in a searchable menu. What matters is understanding the PATTERN: trigger starts it, actions execute in order, conditions create branches. Once you understand the pattern, you can build anything.

### Exercise 9.1: Explore the Workflow Builder Interface

**Purpose:** Get comfortable with the builder before building anything real. You will click through every menu so nothing surprises you during the actual builds.

Navigate to **Automation > Workflows** in the left sidebar:

1. Click **+ Create Workflow**
2. You will see two options: **Start from Scratch** and **Recipes** (pre-built templates)
3. Click **Recipes** first -- browse through what GHL offers out of the box. Note the "Missed Call Text Back" and "Appointment Reminder" recipes. You will build these yourself shortly, but it is good to know they exist
4. Go back and choose **Start from Scratch**
5. You are now in the workflow builder. Here is what you see:
   - A **"Add New Workflow Trigger"** button at the top -- this is where every workflow starts
   - A blank canvas below -- this is where your actions will appear
   - A toolbar with save, publish, and settings options
6. Click **Add New Workflow Trigger** and browse through every trigger category listed above. Do not select one yet -- just read through the options
7. Click any trigger (try "Form Submitted") to add it temporarily. Below it, you will see a **+** button
8. Click the **+** button to see all available actions. Browse through the categories: Communication, CRM, Calendar, Internal, Logic, External
9. Notice the **If/Else** action under Logic -- this is how you create branches
10. Delete this test workflow without saving (click the back arrow or discard)

**What to notice:**
- The builder is visual and linear -- actions flow top to bottom
- Every action has its own configuration panel when you click on it
- The If/Else action splits the flow into two branches (YES and NO)
- Wait actions let you pause for a set time (5 minutes, 24 hours, etc.) or until a specific condition is met

---

## Part 2: Build the "New Trial Lead" Workflow (45 min)

### What Are We Building?

This is the big one. This single workflow connects almost everything you have built across Phase 1:

- **Day 8 form** (the trigger -- someone submits the Free Trial Request form)
- **Day 3 templates** (the welcome email and SMS messages)
- **Day 5 pipeline** (creating an opportunity in Membership Sales)
- **Day 4 calendars** (the booking link in the SMS)
- **Day 2 custom fields** (fitness goals in the notification)

When a potential member fills out the Free Trial form on your funnel, this workflow will automatically: tag them, send a welcome email, text them a booking link, notify you, create a pipeline opportunity, and follow up if they do not book. All without you touching a thing.

### Exercise 9.2: Build the New Trial Lead Workflow Step by Step

**Purpose:** Build Sunrise Wellness Studio's most important automation -- the one that turns a website visitor into a booked trial session without manual effort.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name this workflow:** "New Trial Lead - Welcome Sequence"

Now build it step by step. After adding each step, configure it fully before moving to the next one.

```
[TRIGGER: Form Submitted --> "Free Trial Request" form (from Day 8)]
```

**Step 1: Add the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Form Submitted**
3. In the configuration panel, select the "Free Trial Request" form you built on Day 8
4. If you did not build that exact form, select any form you created -- the logic is the same

```
    |
    v
[ACTION: Add Tag "new-trial-lead"]
```

**Step 2: Tag the Contact**
1. Click the **+** below the trigger
2. Search for **Add Tag** (under CRM actions)
3. Tag name: `new-trial-lead`
4. WHY: Tags are how you track where a contact is in their journey. This tag will be used by the Smart List you created on Day 2, and it will also be referenced by the If/Else conditions later in this workflow

```
    |
    v
[ACTION: Send Email --> "Sunrise Welcome Email" template (from Day 3)]
```

**Step 3: Send the Welcome Email**
1. Click **+** to add the next action
2. Select **Send Email**
3. Choose the "Sunrise Welcome Email" template you built on Day 3 (Exercise 3.3 or 7.1)
4. If you have not built that template yet, go back to Day 3 or Day 7 and create it first -- workflows are most powerful when they use polished templates
5. WHY: The email arrives instantly and gives the lead detailed information about the studio, membership options, and what to expect during their free trial

```
    |
    v
[ACTION: If/Else -- Does the contact have a phone number?]
  --> YES: Send SMS
  --> NO: Skip SMS (continue to next step)
```

**Step 4: Send Welcome SMS (If Phone Available)**
1. Click **+** to add an **If/Else** condition
2. Condition: Contact Field "Phone" is not empty
3. **YES branch:** Add a **Send SMS** action:
   ```
   Hi {{contact.first_name}}! Thanks for requesting your free trial
   at Sunrise Wellness Studio! We'll have your 7-day pass ready
   for you. Book your first session here: {{booking.link}}
   ```
   - Replace `{{booking.link}}` with the actual link to your PT session or Group Fitness calendar from Day 4
4. **NO branch:** Leave empty (the workflow continues to the next step after both branches merge)
5. WHY: SMS has a 98% open rate compared to about 20% for email. If you have their phone number, use it. But not everyone provides a phone number on the form, so the If/Else prevents an error

> **Pro Tip:** Keep SMS messages short and include ONE clear call-to-action. The booking link is the most important thing in this message -- everything else is just context.

```
    |
    v
[ACTION: Wait 5 minutes]
```

**Step 5: Add a Short Wait**
1. Click **+** and select **Wait** (under Logic)
2. Set to **5 minutes**
3. WHY: The 5-minute gap prevents the contact from receiving an email, SMS, AND notification all in the same second. It also allows the internal notification to arrive slightly after the lead's messages, so you can see that the lead was already contacted when you read the notification

```
    |
    v
[ACTION: Internal Notification --> Email to yourself]
```

**Step 6: Notify Yourself**
1. Click **+** and select **Internal Notification** (under Internal actions)
2. Notification type: **Email** (sent to your GHL user email)
3. Subject: `New Trial Lead: {{contact.first_name}} {{contact.last_name}}`
4. Body:
   ```
   A new free trial request just came in!

   Name: {{contact.first_name}} {{contact.last_name}}
   Email: {{contact.email}}
   Phone: {{contact.phone}}
   Fitness Goals: {{contact.fitness_goals}}

   The welcome email and SMS have already been sent automatically.
   An opportunity has been created in the Membership Sales pipeline.
   ```
   - The `{{contact.fitness_goals}}` field references the custom field you created on Day 1/Day 2. If you used a different field name, adjust accordingly
5. WHY: Even though the workflow handles everything, you still want to know when leads come in. This notification lets you add a personal touch (a quick phone call) on top of the automation

```
    |
    v
[ACTION: Create Opportunity in "Membership Sales" pipeline]
```

**Step 7: Create a Pipeline Opportunity**
1. Click **+** and select **Create Opportunity** (under CRM)
2. Configure:
   - **Pipeline:** Membership Sales (from Day 5)
   - **Stage:** New Inquiry (the first stage)
   - **Opportunity Name:** `{{contact.first_name}} {{contact.last_name}} - Free Trial`
   - **Value:** $79 (the Basic membership price -- a reasonable starting estimate)
   - **Source:** Free Trial Funnel
3. WHY: Without this step, you would have to manually create an opportunity for every lead. Now, every form submission automatically appears on your Membership Sales pipeline board, ready for tracking

```
    |
    v
[ACTION: Wait 24 hours]
```

**Step 8: Wait for First Follow-Up**
1. Click **+** and select **Wait**
2. Set to **24 hours**
3. WHY: You want to give the lead time to read your email, click the booking link, and book a session. Following up immediately after the welcome would feel pushy

```
    |
    v
[CONDITION: If/Else -- Has tag "trial-booked"?]
  --> YES: End workflow (they booked their first session!)
  --> NO: Send follow-up email
```

**Step 9: First Follow-Up Check**
1. Click **+** and add an **If/Else** condition
2. Condition: Contact has tag `trial-booked`
   - NOTE: This tag would be applied by a separate workflow (the Appointment Booked workflow in Part 4). For now, just set up the condition -- you can add the tagging workflow after
3. **YES branch:** Add an **End Workflow** action or simply leave it empty (the workflow stops)
4. **NO branch:** Add a **Send Email** action:
   - Subject: "Ready to start your free trial, {{contact.first_name}}?"
   - Body: Friendly reminder about the free 7-day trial, benefits of getting started, booking link, and a mention of what classes are available this week
5. WHY: Not everyone books immediately. Some people need a nudge. This check prevents you from sending a follow-up to someone who already booked (which would feel impersonal and automated)

```
    |
    v
[ACTION: Wait 48 hours]
    |
    v
[CONDITION: If/Else -- Has tag "trial-booked"?]
  --> YES: End workflow
  --> NO: Send "last chance" email + tag for manual follow-up
```

**Step 10: Final Follow-Up**
1. Add another **Wait** action: 48 hours
2. Add another **If/Else** condition: Has tag `trial-booked`?
3. **YES branch:** End workflow
4. **NO branch:** Add two actions:
   - **Send Email:** Subject: "Your free trial is waiting, {{contact.first_name}}" -- Body: Create urgency. Mention that the free trial offer is available for a limited time. Include the booking link one more time. Add a testimonial or success story if you have one
   - **Add Tag:** `needs-manual-followup`
5. WHY: After 3 automated touches over 3 days, if the lead still has not booked, it is time for personal outreach. The `needs-manual-followup` tag makes these contacts easy to find using a Smart List (you could create one: "Tag is needs-manual-followup AND Tag is NOT trial-booked")

**Save and Publish the workflow.** Do NOT publish it to live status yet -- you will test it in Part 6.

Here is the complete flow at a glance:

```
Form Submitted ("Free Trial Request")
    |
    v
Add Tag: "new-trial-lead"
    |
    v
Send Email: Welcome template (Day 3)
    |
    v
If phone exists? --> YES: Send SMS with booking link
    |                  NO: Skip
    v
Wait 5 minutes
    |
    v
Internal Notification: Alert yourself
    |
    v
Create Opportunity: Membership Sales pipeline, "New Inquiry" stage, $79
    |
    v
Wait 24 hours
    |
    v
Has tag "trial-booked"? --> YES: Done!
    |                        NO: Send follow-up email
    v
Wait 48 hours
    |
    v
Has tag "trial-booked"? --> YES: Done!
                             NO: Send "last chance" email
                                 + Tag "needs-manual-followup"
```

---

## Part 3: Certification Recipes (45 min)

These two workflows are specifically called out in the GHL certification. You need to know how to build them from memory. Both are common real-world automations that every GHL sub-account should have.

### What is the Missed Call Text-Back?

When someone calls your business and you cannot answer, they typically hang up and call a competitor. The **Missed Call Text-Back** workflow solves this by instantly sending an automated text message that says "Sorry we missed your call! How can we help?" This keeps the lead engaged even though you could not pick up the phone.

For Sunrise Wellness Studio, think about this scenario: it is 7 PM on a Tuesday. You are coaching a group HIIT class. Someone calls the studio number asking about memberships. You cannot answer because you are mid-class. Without this workflow, that lead is gone. With it, they get an instant text with a booking link, and by the time your class ends, they have already booked a tour.

### Exercise 9.3: Build the Missed Call Text-Back Workflow

**Purpose:** Build the GHL certification recipe that automatically responds to missed calls, keeping potential members engaged even when you cannot answer the phone.

> **Access Note:** This workflow requires a phone number connected to your GHL sub-account. If you do not have a phone number set up, **build the workflow structure anyway** -- it is excellent practice for the certification exam, and you can activate it later when you add a phone number. For the SMS actions, use an Email action as a stand-in so you can still test the flow.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Missed Call Text-Back"

```
[TRIGGER: Call Status --> Missed Call / Voicemail]
```

1. Click **Add New Workflow Trigger**
2. Select **Call Status** (under Conversation triggers)
3. Filter to: **Missed** (and optionally Voicemail)

```
    |
    v
[ACTION: Wait 1 minute]
```

4. Add a **Wait** action: 1 minute
5. WHY: A 1-minute delay makes the text feel more natural. An instant auto-reply within 2 seconds feels robotic. A 1-minute delay feels like "oh, they just saw the missed call and texted me"

```
    |
    v
[ACTION: Send SMS]
```

6. Add a **Send SMS** action:
   ```
   Sorry we missed your call! This is Sunrise Wellness Studio.
   How can we help you today?

   You can also book a studio tour or first session here:
   {{booking.link}}
   ```
   - Replace `{{booking.link}}` with your actual calendar booking link from Day 4
   - If you do not have a phone number, use **Send Email** instead with the same message content

```
    |
    v
[ACTION: Add Tag "missed-call"]
    |
    v
[ACTION: Internal Notification]
```

7. Add **Add Tag** action: `missed-call`
8. Add **Internal Notification:**
   - Type: Email to yourself
   - Subject: `Missed Call: {{contact.first_name}} {{contact.phone}}`
   - Body: "You missed a call from {{contact.first_name}} ({{contact.phone}}). An automated text has been sent. Follow up when available."

```
    |
    v
[ACTION: Wait 30 minutes]
    |
    v
[CONDITION: If/Else -- Has the contact replied?]
  --> YES: End (a human conversation has started)
  --> NO: Send follow-up
```

9. Add **Wait** action: 30 minutes
10. Add **If/Else** condition: Check if the contact has replied (look for "Last Message Direction" = Inbound, or check for a reply-related condition in your workflow builder)
    - **YES branch:** End workflow. The contact replied, so a real conversation is happening now
    - **NO branch:** Add another **Send SMS** (or Email):
      ```
      Hi {{contact.first_name}}, we tried calling you back.
      When is a good time to connect? Reply with your preferred
      time or book directly: {{booking.link}}
      ```

```
    |
    v
[ACTION: Add Tag "missed-call-no-reply"]
```

11. After the NO branch follow-up, add **Add Tag:** `missed-call-no-reply`
12. WHY: This tag lets you create a Smart List of people who called but never engaged. You might reach out manually, or include them in a future marketing campaign

**Save the workflow.**

### What is the No-Show Nurture?

A **no-show** is when someone books an appointment but does not show up. It happens in every business, but especially in fitness -- life gets busy, motivation dips, or they simply forgot. The No-Show Nurture workflow automatically reaches out to reschedule, so the relationship does not go cold.

For Sunrise Wellness Studio, imagine this: Sarah booked a 2 PM PT session but never showed up. Without automation, her trainer might not even notice until the next day. With the No-Show Nurture workflow, Sarah gets a friendly "we missed you" text 30 minutes after her missed session, a rebooking email the next day, and a special incentive offer if she still has not rebooked after 3 days.

### Exercise 9.4: Build the No-Show Nurture Workflow

**Purpose:** Build the GHL certification recipe that automatically re-engages contacts who miss their appointments, reducing lost revenue and keeping the relationship warm.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "No-Show Nurture Sequence"

```
[TRIGGER: Appointment Status --> Changed to "No Show"]
```

1. Click **Add New Workflow Trigger**
2. Select **Appointment Status** (under Calendar triggers)
3. Filter to: Status changed to **No Show**
4. Optionally filter to specific calendars (PT Session, Group Fitness, Nutrition Consultation from Day 4) or leave it for all calendars

```
    |
    v
[ACTION: Wait 30 minutes]
```

5. Add a **Wait** action: 30 minutes
6. WHY: Do not text someone the second they miss the appointment. They might be running late and about to walk in. 30 minutes is enough to confirm they are truly a no-show, while still being timely enough that they remember the appointment

```
    |
    v
[ACTION: Send SMS/Email -- "We missed you"]
```

7. If you have a phone number, add **Send SMS**:
   ```
   Hi {{contact.first_name}}, we missed you at Sunrise Wellness
   today! No worries at all - life happens. Whenever you are
   ready, let's get you rescheduled: {{booking.link}}
   ```
8. If you do not have a phone number, add **Send Email** with the same message (more detail is fine in email format since you have more space)

```
    |
    v
[ACTION: Add Tag "no-show"]
```

9. Add **Add Tag:** `no-show`
10. WHY: Tracking no-shows with a tag lets you identify patterns. If someone has the "no-show" tag added three times, that tells you something about their engagement level

```
    |
    v
[ACTION: Wait 24 hours]
    |
    v
[CONDITION: If/Else -- Has tag "appointment-booked"?]
  --> YES: Remove tag "no-show" --> End
  --> NO: Send email with incentive
```

11. Add **Wait:** 24 hours
12. Add **If/Else:** Has tag `appointment-booked`?
    - **YES branch:** They rebooked! Add a **Remove Tag** action for `no-show`, then end the workflow
    - **NO branch:** Add **Send Email:**
      - Subject: "We saved your spot, {{contact.first_name}}"
      - Body: Friendly email acknowledging they missed their session. Include a rebooking link, mention what classes or sessions are available this week, and offer a small incentive (e.g., "Book this week and we will throw in a free smoothie from the Nutrition Bar")

```
    |
    v
[ACTION: Wait 3 days]
    |
    v
[CONDITION: If/Else -- Has tag "appointment-booked"?]
  --> YES: End
  --> NO: Final attempt + manual follow-up tag
```

13. Add **Wait:** 3 days
14. Add **If/Else:** Has tag `appointment-booked`?
    - **YES branch:** End workflow
    - **NO branch:** Add these actions:
      - **Send SMS/Email:** Final rebooking attempt:
        ```
        Hi {{contact.first_name}}, we still have availability this
        week at Sunrise Wellness. We would love to see you back!
        Book here: {{booking.link}}
        ```
      - **Add Tag:** `needs-manual-followup`
      - WHY: After three automated touchpoints (30 min, 24 hours, 3 days) without a response, further automation becomes annoying. The `needs-manual-followup` tag tells you to pick up the phone and have a real conversation

**Save the workflow.**

---

## Part 4: Appointment Confirmation and Reminder Workflow (30 min)

### What is an Appointment Reminder Workflow?

Every calendar system sends basic confirmations. But GHL lets you build a **multi-step reminder sequence** that dramatically reduces no-shows. Instead of one confirmation email at booking time, you send: an instant confirmation, a reminder 24 hours before, and a final "see you soon" message 1 hour before.

For Sunrise Wellness Studio, this connects directly to the calendars you built on Day 4. Every PT session booking, every group class sign-up, and every nutrition consultation will automatically get this confirmation and reminder sequence.

### Exercise 9.5: Build the Appointment Confirmation and Reminder Workflow

**Purpose:** Reduce no-shows by building a multi-touch reminder sequence that keeps booked appointments top of mind for your members.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Confirmation + Reminders"

```
[TRIGGER: Appointment Booked (any calendar)]
```

1. Click **Add New Workflow Trigger**
2. Select **Appointment Booked** (under Calendar triggers)
3. You can either select all calendars or filter to specific ones from Day 4 (PT Session, Group Fitness, Nutrition Consultation). For now, apply to all calendars

```
    |
    v
[ACTION: Send Email -- Instant Confirmation]
```

4. Add **Send Email** immediately (no wait):
   - Use the appointment confirmation template from Day 3 if you created one, or build inline:
   - Subject: "You're booked! See you at Sunrise Wellness"
   - Body: Include appointment date, time, location, and what to bring (e.g., "Wear comfortable workout clothes and bring a water bottle. We will provide everything else!")
   - Include a "Need to reschedule?" link to your calendar

```
    |
    v
[ACTION: Add Tag "appointment-booked"]
```

5. Add **Add Tag:** `appointment-booked`
6. WHY: This tag is referenced by BOTH the New Trial Lead workflow (Part 2) and the No-Show Nurture workflow (Part 3). When this tag gets applied, those workflows know the contact has booked and can stop sending follow-ups. This is how workflows talk to each other

```
    |
    v
[ACTION: Wait until 24 hours before appointment]
```

7. Add a **Wait** action
8. Look for "Wait until event" or "Wait until before appointment" option -- this is different from "Wait 24 hours." You want the workflow to wait until 24 hours BEFORE the appointment time, not 24 hours from now
   - If this specific option is not available in your builder, use the appointment reminder features built into the calendar settings from Day 4 for the timing, and just build the instant confirmation part here

```
    |
    v
[ACTION: Send SMS/Email -- 24-Hour Reminder]
```

9. Add **Send SMS** (or Email if no phone number):
   ```
   Reminder: Your session at Sunrise Wellness Studio is tomorrow
   at {{appointment.start_time}}.

   Reply C to confirm or R to reschedule.
   ```
   - The "Reply C or R" technique is powerful -- it creates engagement AND gives you a way to confirm attendance

```
    |
    v
[ACTION: Wait until 1 hour before appointment]
```

10. Add another **Wait** action: until 1 hour before appointment

```
    |
    v
[ACTION: Send SMS/Email -- Final Reminder]
```

11. Add **Send SMS** (or Email):
    ```
    See you in 1 hour at Sunrise Wellness! {{appointment.start_time}}
    ```
    - Keep this one short. They already know the details. This is just a final nudge

**Save the workflow.**

> **Pro Tip:** The "Reply C to confirm" technique in Step 9 does something clever -- it gets the contact to open a two-way conversation. Once they reply, you can follow up naturally in the Conversations tab. It also acts as a soft confirmation, helping you predict no-shows (people who do not reply are more likely to no-show).

---

## Part 5: Lead Nurture with Branching (30 min)

### What is Conditional Branching?

So far, your workflows have been mostly linear: trigger, action, wait, action. But real people are not all the same. Someone who found Sunrise Wellness on Instagram has different expectations than someone who was referred by a friend. Someone whose goal is weight loss responds to different messaging than someone who wants to build muscle.

**Conditional branching** uses If/Else logic to send different people down different paths in the same workflow. It is like a "choose your own adventure" book -- the story branches based on choices.

This exercise uses the custom fields you created on Day 2 (like "How did you hear about us?" and "Fitness Goals") to personalize the experience.

### Exercise 9.6: Build a Lead Source + Goals Nurture Workflow

**Purpose:** Create a personalized welcome experience that adapts based on where the lead came from and what their fitness goals are, using the custom fields from Day 2.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Personalized Lead Nurture"

```
[TRIGGER: Tag Added --> "new-trial-lead"]
```

1. Click **Add New Workflow Trigger**
2. Select **Contact Tag Added**
3. Tag: `new-trial-lead`
4. NOTE: This trigger fires when the New Trial Lead workflow (Part 2) adds the tag. This is an example of **workflow chaining** -- one workflow triggers another. It keeps each workflow focused on one job

```
    |
    v
[CONDITION: If/Else -- Check "How did you hear about us?"]
```

5. Add **If/Else** condition
6. Condition: Custom field "How did you hear about us?" (or "Lead Source" -- whatever you named it on Day 2)
7. Build these branches:

**Branch: Instagram or Facebook**
   - **Send Email:**
     - Subject: "Welcome from our social family!"
     - Body: Reference that you connected on social media. Include links to your Instagram/Facebook pages. Mention that you post daily workout tips and class highlights. "Follow us for daily motivation and behind-the-scenes studio content!"

**Branch: Referral**
   - **Send Email:**
     - Subject: "Your friend knows great fitness!"
     - Body: Thank them for the referral. Mention the referral program ("Did you know? When you sign up, your friend who referred you gets a free month!"). Make them feel like they are joining a community, not just a gym

**Branch: Default (all other sources)**
   - **Send Email:**
     - Subject: "Welcome to the Sunrise Wellness family!"
     - Body: General welcome email focusing on the studio's story, mission, and what makes it different

8. After all branches merge, add a **Wait** action: 2 days

```
    |
    v
[Wait 2 days]
    |
    v
[CONDITION: If/Else -- Check "Fitness Goals"]
```

9. Add another **If/Else** condition
10. Condition: Custom field "Fitness Goals" (from Day 2)
11. Build these branches:

**Branch: Weight Loss**
   - **Send Email:**
     - Subject: "Real results from real members"
     - Body: Share a weight loss success story (can be fictional for the exercise). Highlight the combination of group fitness classes + nutrition coaching. Include a CTA to book a nutrition consultation (link to the Day 4 Nutrition Consultation calendar)

**Branch: Muscle Gain / Strength Training**
   - **Send Email:**
     - Subject: "Meet your new training partner"
     - Body: Focus on Personal Training sessions. Mention the PT calendar booking link (Day 4). Highlight the facility's equipment and trainer certifications

**Branch: Default (General Fitness, Flexibility, Stress Relief, etc.)**
   - **Send Email:**
     - Subject: "There's something for everyone at Sunrise"
     - Body: Overview of all offerings -- group classes (HIIT, Yoga, Pilates), personal training, nutrition coaching. Let them explore and find what fits

**Save the workflow.**

> **Pro Tip:** In production, you would add more branches and wait steps to build a longer nurture sequence. For now, two rounds of branching is enough to demonstrate the concept. The key insight is that EVERY contact gets a personalized experience -- even though you built it once and it runs automatically.

---

## Part 6: Testing Workflows (15 min)

### Why Test Before Publishing?

A workflow with a mistake can send embarrassing messages to real contacts. Imagine sending "Hi {{contact.first_name}}" to a lead because you forgot to connect the merge field -- they literally receive the text "Hi {{contact.first_name}}." Or imagine the 24-hour wait accidentally being set to 24 minutes, so a lead gets three emails in one hour.

Testing prevents these problems.

### Exercise 9.7: Testing Best Practices

**Purpose:** Learn how to safely test workflows before turning them on for real contacts.

Follow these steps for EACH workflow you built today:

**Step 1: Create a Test Contact**
1. Go to **Contacts** and create a new contact using your own details
2. Name: "Test Workflow" (or your real name)
3. Email: Your actual email (so you receive the test messages)
4. Phone: Your actual phone number (if testing SMS)
5. Fill in custom fields: Set "Fitness Goals" to "Weight Loss," set "How did you hear about us?" to "Instagram"
6. WHY: Using your real contact info means you will receive every message the workflow sends, so you can check the content, formatting, and timing

**Step 2: Shorten Wait Times (Temporarily)**
1. Open each workflow you built today
2. Change all "Wait 24 hours" to "Wait 1 minute"
3. Change all "Wait 48 hours" to "Wait 2 minutes"
4. Change all "Wait 3 days" to "Wait 3 minutes"
5. WHY: You do not want to wait 3 actual days to see if your workflow works. Shortened times let you verify the entire flow in minutes

**Step 3: Publish and Trigger**
1. Set the workflow to **Published** (or Draft with test mode if available)
2. For the New Trial Lead workflow: Submit the Free Trial form with your test contact's info
3. For the Missed Call workflow: Call your GHL number and let it ring (if you have a phone number)
4. For the No-Show workflow: Create a test appointment and change its status to "No Show"
5. For the Appointment Confirmation workflow: Book an appointment using your test contact
6. For the Lead Nurture workflow: Add the `new-trial-lead` tag to your test contact manually

**Step 4: Verify Each Step**
1. Check your email -- did you receive the welcome email?
2. Check your phone -- did you receive the SMS? (If applicable)
3. Check the **Contacts** tab -- was the tag applied?
4. Check the **Opportunities** tab -- was the pipeline opportunity created?
5. Check the workflow execution log: Open the workflow, find the test contact, and review which steps executed and which are pending

**Step 5: Restore Production Timing**
1. After testing, go back into each workflow
2. Change all wait times back to their real values (24 hours, 48 hours, 3 days, etc.)
3. Save each workflow
4. **This step is critical** -- forgetting to restore timing means real contacts will get all three follow-ups in 3 minutes

> **Pro Tip:** Keep your test contact in the system permanently. Label it clearly (e.g., "TEST - Do Not Delete") so you can re-test workflows anytime you make changes.

---

## Part 7: API Lab - Workflow Triggers

If you are working through the API labs, the Day 9 script demonstrates how to interact with workflows programmatically:

```bash
cd scripts/
python day-09-automation-api.py
```

The script covers:
1. **Trigger a workflow via API webhook** -- fire a workflow from an external system
2. **Add a contact to a workflow via API** -- programmatically enroll contacts
3. **Build a custom webhook endpoint** that receives GHL events and processes them in Python

See the script comments for detailed setup instructions.

---

## Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental is a family dentistry practice offering cleanings ($150), fillings ($300), crowns ($1,200), whitening ($500), and Invisalign ($3,000+). They need automation for the full patient lifecycle: from first inquiry to post-treatment follow-up.

**Your Task:** Build 3 workflows for BrightSmile Dental in your sub-account. Use the same Sunrise Wellness sub-account -- just name each workflow clearly with "BrightSmile" so you can tell them apart.

### Workflow 1: "BrightSmile - New Patient Inquiry"

A potential patient fills out a "Request Appointment" form on the dental website. Build the automated response:

```
[TRIGGER: Form Submitted --> "Request Appointment"]
    |
    v
[Add Tag: "new-patient-inquiry"]
    |
    v
[Send Email: Welcome to BrightSmile Dental]
  - Subject: "Welcome to BrightSmile Dental, {{contact.first_name}}!"
  - Body: Introduction to the practice, what to expect at the first
    visit, insurance information needed, office hours (Mon-Fri 8AM-5PM),
    and a link to the new patient intake form
    |
    v
[Create Opportunity: "Patient Pipeline" --> "New Inquiry" stage]
  - Value: $150 (initial cleaning/exam)
    |
    v
[Wait 5 minutes]
    |
    v
[Internal Notification: "New patient inquiry from {{contact.first_name}}"]
    |
    v
[Send Email: New Patient Intake Form]
  - Subject: "One quick step before your first visit"
  - Body: Link to the new patient intake form (medical history,
    insurance, allergies, current medications)
    |
    v
[Wait 24 hours]
    |
    v
[If/Else: Has tag "appointment-booked"?]
  --> YES: End
  --> NO: Send follow-up email: "Still looking for a dentist?"
           Include patient testimonials and the booking link
    |
    v
[Wait 48 hours]
    |
    v
[If/Else: Has tag "appointment-booked"?]
  --> YES: End
  --> NO: Send "limited availability" email + Add tag
          "needs-manual-followup"
```

### Workflow 2: "BrightSmile - Appointment Reminder"

```
[TRIGGER: Appointment Booked]
    |
    v
[Send Email: Appointment Confirmation]
  - Include: Date, time, what to bring (insurance card, ID, intake
    form if not completed online), parking info, office location
    |
    v
[Add Tag: "appointment-booked"]
    |
    v
[Wait until 24 hours before appointment]
    |
    v
[Send SMS/Email: "Your dental appointment is tomorrow at
 {{appointment.start_time}}. Please arrive 10 minutes early.
 Reply C to confirm."]
    |
    v
[Wait until 1 hour before appointment]
    |
    v
[Send SMS/Email: "See you in 1 hour at BrightSmile Dental!
 Address: 123 Main St. Remember to bring your insurance card."]
```

### Workflow 3: "BrightSmile - No-Show Recovery"

```
[TRIGGER: Appointment Status --> No Show]
    |
    v
[Wait 30 minutes]
    |
    v
[Send SMS/Email: "Hi {{contact.first_name}}, we missed you at
 BrightSmile Dental today. We hope everything is okay! When you
 are ready, let's reschedule: {{booking.link}}"]
    |
    v
[Add Tag: "dental-no-show"]
    |
    v
[Wait 24 hours]
    |
    v
[Send Email: "Your dental health matters"]
  - Body: Gentle reminder about the importance of regular dental
    visits, mention that postponing care leads to bigger (and more
    expensive) issues, include rebooking link
    |
    v
[Wait 3 days]
    |
    v
[If/Else: Has tag "appointment-booked"?]
  --> YES: Remove tag "dental-no-show" --> End
  --> NO: Send final email with a special offer
          ("Book this week and receive a complimentary whitening
           consultation") + Add tag "needs-manual-followup"
```

**Design Exercise:** Write down what you would change about each workflow if BrightSmile had a receptionist answering phones during business hours. How would the Missed Call Text-Back recipe differ for a dental office that is staffed 8-5 but closed on weekends?

---

## Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency offers SEO ($2,000/mo), PPC Management ($3,000/mo), Social Media ($2,500/mo), and Web Design ($5,000-$10,000 per project). Their sales cycle is longer than a wellness studio -- prospects research, compare agencies, and request proposals before committing. The automation needs to nurture leads through a longer decision process.

**Your Task:** Build 3 workflows for Elevate Digital Agency in your sub-account. Name each workflow with "Elevate" prefix.

### Workflow 1: "Elevate - New Lead Nurture"

A business owner fills out a "Free Strategy Session" form on the agency website:

```
[TRIGGER: Form Submitted --> "Free Strategy Session"]
    |
    v
[Add Tag: "new-agency-lead"]
    |
    v
[Send Email: "Your Strategy Session Request"]
  - Subject: "Thanks for reaching out, {{contact.first_name}}!"
  - Body: Professional welcome. Introduce the agency, mention
    notable clients or results (e.g., "We've helped 50+ businesses
    increase organic traffic by an average of 187%"). Include a
    link to book the strategy session call
    |
    v
[Create Opportunity: "Agency Sales Pipeline" --> "New Lead" stage]
  - Value: $3,000 (average monthly retainer as starting estimate)
    |
    v
[Internal Notification: "New agency lead: {{contact.first_name}}
 from {{contact.company_name}}"]
    |
    v
[Wait 1 day]
    |
    v
[Send Email: Case Study]
  - Subject: "How we helped [Company] grow 3x in 6 months"
  - Body: Detailed case study with specific numbers, strategy
    overview, and testimonial. CTA: "Ready for similar results?
    Book your strategy session"
    |
    v
[Wait 3 days]
    |
    v
[If/Else: Has tag "strategy-call-booked"?]
  --> YES: End
  --> NO: Send email: "5 Questions to Ask Any Digital Agency"
         - Educational content that positions Elevate as the
           expert. Include booking link at the bottom
    |
    v
[Wait 4 days]
    |
    v
[If/Else: Has tag "strategy-call-booked"?]
  --> YES: End
  --> NO: Send "limited spots" email + Add tag
          "needs-manual-followup"
```

### Workflow 2: "Elevate - Client Onboarding"

When a deal is marked as Won in the pipeline, trigger the onboarding sequence:

```
[TRIGGER: Opportunity Status --> Won]
    |
    v
[Add Tag: "active-client"]
[Remove Tag: "new-agency-lead"]
    |
    v
[Send Email: "Welcome to Elevate Digital!"]
  - Subject: "Let's get started, {{contact.first_name}}!"
  - Body: Welcome aboard. Introduce the team. Outline the
    onboarding timeline: Week 1 = discovery and audit,
    Week 2 = strategy development, Week 3 = implementation
    begins. Include a link to the onboarding questionnaire
    |
    v
[Wait 2 days]
    |
    v
[Send Email: Onboarding Questionnaire]
  - Subject: "Quick questionnaire to kick things off"
  - Body: Link to a detailed survey covering: business goals,
    target audience, competitors, brand guidelines, logins
    needed (Google Analytics, ad accounts, etc.)
    |
    v
[Wait 30 days]
    |
    v
[Send Email: 30-Day Check-In]
  - Subject: "Your first month with Elevate - here's the progress"
  - Body: Template for sharing results, next steps, and
    asking for feedback. Include a link to schedule a review call
    |
    v
[Internal Notification: "30-day check-in due for
 {{contact.first_name}} at {{contact.company_name}}"]
```

### Workflow 3: "Elevate - Contract Renewal Reminder"

Proactively reach out before contracts end:

```
[TRIGGER: Custom Date Field "Contract End Date" is 30 days away]
  (NOTE: Use a Date-based trigger or a manual enrollment
   when the date approaches if your builder does not support
   date field triggers directly)
    |
    v
[Internal Notification: "Contract renewal approaching for
 {{contact.first_name}} at {{contact.company_name}}
 - ends in 30 days"]
    |
    v
[Send Email: "Your contract renewal is coming up"]
  - Subject: "Let's talk about your next chapter with Elevate"
  - Body: Summary of results achieved during the contract period.
    Options for renewal: same plan, upgrade to additional services,
    or custom package. Include a scheduling link for a renewal call
    |
    v
[Wait 23 days]  (now 7 days before contract end)
    |
    v
[If/Else: Has tag "contract-renewed"?]
  --> YES: End
  --> NO: Send "renewal offer" email
    |
    v
[Send Email: "Special renewal offer"]
  - Subject: "Exclusive offer for continuing clients"
  - Body: Offer a 10% discount for annual commitment, or a free
    add-on service (e.g., one month of Social Media added to their
    SEO retainer). Create urgency: "This offer expires when your
    current contract ends on {{contact.contract_end_date}}"
    |
    v
[Internal Notification: "URGENT: {{contact.company_name}} contract
 ends in 7 days - no renewal yet"]
```

**Design Exercise:** Elevate Digital's sales cycle is typically 2-4 weeks (vs. a few days for a fitness studio). How does this affect the wait times in your nurture workflow? What additional touchpoints might you add for a $10,000/month prospect vs. a $2,000/month prospect?

---

## Day 9 Recap

**What You Built Today:**
- New Trial Lead workflow (connecting Day 8 form, Day 3 templates, Day 5 pipeline, Day 4 calendars)
- Missed Call Text-Back (certification recipe)
- No-Show Nurture (certification recipe)
- Appointment Confirmation and Reminders
- Personalized Lead Nurture with conditional branching
- Testing and debugging skills

**Certification Review Questions:**

1. What is the difference between a workflow **trigger** and a workflow **action**? Name 3 examples of each
2. Explain the Missed Call Text-Back recipe step by step -- why is there a 1-minute wait before the text?
3. In the No-Show Nurture workflow, why do you check for the "appointment-booked" tag before sending follow-ups?
4. What is the difference between "Wait 24 hours" and "Wait until 24 hours before appointment"? When would you use each?
5. How do you test a workflow safely without sending messages to real contacts?
6. What happens when a contact is already in a workflow and the trigger fires again? (Hint: look for "Allow re-entry" settings)
7. How do workflows "talk to each other"? (Hint: think about how tags connect the workflows you built today)

---

## Next Day Preview

**Day 10: Reputation, Memberships & Reporting** -- The final day of Phase 1! You will build an automated review request system that asks happy members for Google reviews after their sessions, create a "Sunrise Wellness Inner Circle" community portal with tiered access for different membership levels, and review the reporting dashboard to understand how the entire system you have built over 10 days is performing. After Day 10, Sunrise Wellness Studio will be a fully automated business.
