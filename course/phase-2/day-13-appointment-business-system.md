# Day 13: Complete Appointment-Based Business System

**Time Required:** 3-4 hours
**Combines:** Calendars (Day 4) + Automation (Day 9) + Payments (Day 6) + Conversations (Day 3) + Reputation (Day 10)
**Level:** Intermediate

---

## Today's Mission

Sunrise Wellness Studio is an appointment-based business. Members book sessions, show up, pay, and (hopefully) leave a review. Right now those are four separate systems you built across four different days. They work individually, but they do not talk to each other. A member books a PT session on the calendar -- but you have to manually send the confirmation details. They show up for the session -- but you have to manually create an invoice afterward. They pay -- but nobody asks them for a review. Every gap between systems is a place where things fall through the cracks.

Today you will eliminate every gap. You are going to build the **complete appointment lifecycle** -- from the moment a member books a session all the way through to a Google review request -- as one seamless automated system.

Here is what the finished system does, with zero manual intervention:

1. Member books a PT session --> instant confirmation email + SMS with what to bring
2. 24 hours before the session --> "See you tomorrow!" reminder
3. 1 hour before --> "Almost time!" reminder with parking details
4. Member shows up --> you mark them as "showed" --> GHL auto-sends a Text2Pay invoice for $75
5. 2 hours after the session --> automated review request SMS
6. 3 days later, if they have not reviewed --> gentle follow-up

And if they do NOT show up, a completely different path fires: a gentle rebooking message, escalating to personal follow-up if they are a repeat no-show.

This is what makes a business feel professional. The member gets the right message at the right time, every time. And you never have to remember to send anything.

---

## What You'll Combine

| Phase 1 Feature | Day Built | Role in Today's System |
|-----------------|-----------|----------------------|
| PT Calendar | Day 4 | Booking entry point -- the trigger for everything |
| Group Class Calendar | Day 4 | Group class bookings with different messaging |
| Nutrition Calendar | Day 4 | Consultation bookings with different messaging |
| Appointment Reminders | Day 9 | Pre-appointment communication chain |
| SMS Templates | Day 3 | All text messages in the lifecycle |
| Email Templates | Day 3 | All email messages in the lifecycle |
| Payments / Text2Pay | Day 6 | Post-session billing |
| Products | Day 6 | PT Session ($75), Class Pack ($120), Nutrition Plan ($200) |
| Review Workflow | Day 10 | Post-service reputation building |
| Custom Fields | Day 2 | Tracking "Last Visit Date" and visit counts |

---

## The System Architecture

This diagram shows the complete flow you will build today. Each box is a step in the automation. By the end of the day, all of this will run automatically.

```
[Member Books Session] --> [Confirmation Email + SMS]
        |
        |  (customized by service type:
        |   PT / Group Class / Nutrition)
        |
[24hr Before] --> [Reminder: "See you tomorrow, {{first_name}}!"]
        |
[1hr Before] --> ["Almost time!" + parking/location details]
        |
[Appointment Time]
        |
  +-----+-----+
  |             |
[Showed]     [No-Show]
  |             |
  |       [Gentle rebooking SMS]
  |       [If 2nd no-show: different tone + "no-show-risk" tag]
  |       [If VIP: create manual follow-up task instead]
  |
[Mark Complete]
  |
[Send Payment]
  |  PT Session --> Text2Pay for $75
  |  Nutrition --> Invoice for $200 plan
  |  Group Class --> Thank-you (already paid via package)
  |
[Update Custom Fields]
  |  "Last Visit Date" = today
  |  "Total Visits" + 1
  |
[Wait 2 hours]
  |
[Review Request SMS]
  |  "How was your session with us today?"
  |  Link to Google review page
  |
[Wait 3 days]
  |
[Review Follow-Up if no review left]
```

---

## Part 1: Pre-Appointment Confirmation System (30 min)

### Why This Matters

Right now, when someone books a session on one of your Day 4 calendars, GHL sends a basic confirmation. It works, but it is generic. A PT client gets the same confirmation as a nutrition consultation booking. There is no "what to bring" information, no parking details, no enthusiasm. Compare these two confirmations:

**Generic:** "Your appointment has been confirmed for March 15 at 10:00 AM."

**What you are building:** "Hey Sarah! Your Personal Training session with Coach Mike is confirmed for Saturday, March 15 at 10:00 AM. Bring a water bottle, a towel, and wear comfortable athletic shoes. We're at 456 Wellness Ave -- free parking is in the lot behind the building. Can't wait to see you crush it!"

The second one makes the member feel taken care of. That feeling starts with the confirmation and carries through the entire experience.

### Exercise 13.1: Build the Appointment Confirmation Workflow

**Purpose:** Create a single workflow that sends customized confirmation messages immediately after any appointment is booked, with different content depending on the service type.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Lifecycle - Confirmation"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Appointment Status** (under Calendar triggers)
3. Set status to: **Booked** (sometimes labeled "Confirmed")
4. For calendar selection: Select **All Calendars** -- you will use branching inside the workflow to customize by calendar type
5. Click **Save Trigger**

> **Why all calendars?** You could create three separate workflows (one per calendar), but that creates maintenance headaches. If you change your address or parking instructions, you would need to update three workflows instead of one. A single workflow with branching is cleaner.

**Step 2: Add If/Else Branch by Calendar**
1. Add an **If/Else** action immediately after the trigger
2. Name it: "Which Service Type?"
3. **Condition for Branch 1:** Calendar Name **contains** "PT" (or whatever you named your PT calendar on Day 4)
4. **Condition for Branch 2:** Calendar Name **contains** "Class" (or "Group" -- match your Day 4 naming)
5. **Else (default):** This catches Nutrition consultations and any other calendars

> **Naming Tip:** If your Day 4 calendar names do not contain obvious keywords like "PT" or "Class," you can also branch based on the calendar ID. But using name-based matching is easier to read and maintain.

**Step 3: PT Session Confirmation (Branch 1)**
1. In the PT branch, add a **Send Email** action:
   - **Subject:** "You're booked! PT Session on {{appointment.start_date}}"
   - **Body:**
     ```
     Hey {{contact.first_name}}!

     Your Personal Training session is confirmed:

     Date: {{appointment.start_date}}
     Time: {{appointment.start_time}}
     Duration: 60 minutes
     Location: Sunrise Wellness Studio, 456 Wellness Ave

     What to bring:
     - Water bottle
     - Towel
     - Comfortable athletic shoes
     - Any workout gear you prefer

     Parking: Free lot behind the building. Enter from Oak Street.

     If you need to reschedule, use this link: {{appointment.reschedule_url}}

     See you there!
     -- The Sunrise Wellness Team
     ```
2. Add a **Send SMS** action right after:
   - **Message:** "Hey {{contact.first_name}}! Your PT session is confirmed for {{appointment.start_date}} at {{appointment.start_time}}. Bring a water bottle and towel. See you at Sunrise Wellness! Need to reschedule? {{appointment.reschedule_url}}"

**Step 4: Group Class Confirmation (Branch 2)**
1. In the Group Class branch, add a **Send Email** action:
   - **Subject:** "Class spot reserved! {{appointment.start_date}}"
   - **Body:**
     ```
     Hi {{contact.first_name}}!

     You're in! Your group class spot is confirmed:

     Date: {{appointment.start_date}}
     Time: {{appointment.start_time}}
     Location: Sunrise Wellness Studio, Main Studio Room

     What to bring:
     - Water bottle
     - Yoga mat (we have extras if you need one)
     - Comfortable clothes you can move in

     Quick heads-up: please arrive 5-10 minutes early so we
     can start on time. The studio doors close once class begins.

     Parking: Free lot behind the building.

     Need to change plans? {{appointment.reschedule_url}}

     See you in class!
     -- The Sunrise Wellness Team
     ```
2. Add a **Send SMS** action:
   - **Message:** "You're in, {{contact.first_name}}! Group class confirmed for {{appointment.start_date}} at {{appointment.start_time}}. Arrive 5-10 min early. Bring water + yoga mat. See you there!"

**Step 5: Nutrition Consultation Confirmation (Else/Default Branch)**
1. In the Else branch, add a **Send Email** action:
   - **Subject:** "Nutrition Consultation Confirmed - {{appointment.start_date}}"
   - **Body:**
     ```
     Hi {{contact.first_name}}!

     Your Nutrition Consultation is confirmed:

     Date: {{appointment.start_date}}
     Time: {{appointment.start_time}}
     Duration: 45 minutes
     Location: Sunrise Wellness Studio, Consultation Room

     To make the most of our time together, please:
     - Write down what you typically eat in a day (a rough food diary)
     - Note any food allergies or dietary restrictions
     - Think about your top 2-3 nutrition goals

     No need to bring anything fancy -- just come ready to chat
     about how we can fuel your fitness journey!

     Need to reschedule? {{appointment.reschedule_url}}

     Looking forward to it!
     -- The Sunrise Wellness Team
     ```
2. Add a **Send SMS** action:
   - **Message:** "Hi {{contact.first_name}}! Your Nutrition Consultation is set for {{appointment.start_date}} at {{appointment.start_time}}. Quick prep: jot down a typical day of eating + your top nutrition goals. See you soon!"

**Step 6: Save (Do Not Publish Yet)**

Save the workflow. You will publish it after building the complete system in Part 5.

> **What About the Default GHL Confirmation?** GHL calendars have a built-in confirmation notification. Once you activate this workflow, you may want to turn off the default calendar notification to avoid sending double messages. Check each calendar's settings under **Notifications** and disable the built-in confirmation email/SMS if needed.

---

## Part 2: Appointment Day System (30 min)

### Why Reminders Reduce No-Shows

Research shows that appointment reminders reduce no-shows by 30-50%. For a wellness studio where no-shows mean empty time slots and lost revenue, that is significant. A $75 PT session no-show is $75 you will never get back -- you cannot resell that hour after the fact.

On Day 9, you may have set up basic reminders. Today you will upgrade them into a proper day-of system with specific timing and useful content.

### Exercise 13.2: Build the Day-Of Reminder Chain

**Purpose:** Create a reminder sequence that starts 24 hours before the appointment and includes a final "almost time" message 1 hour before.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Lifecycle - Reminders"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Appointment Status**
3. Set status to: **Booked** (same as the confirmation workflow)
4. Select **All Calendars**

> **Wait, the same trigger as before?** Yes. Both workflows fire when an appointment is booked. The confirmation workflow sends messages immediately. This workflow uses **Wait** actions to delay until the right time before the appointment. GHL handles multiple workflows with the same trigger just fine -- they run in parallel.

**Step 2: Wait Until 24 Hours Before**
1. Add a **Wait** action
2. Select **Wait until event time** (not "Wait for a specific duration")
3. Set it to: **24 hours before** the appointment
4. This is key -- GHL will hold this workflow in a waiting state until exactly 24 hours before the booked appointment time

> **Important:** The "Wait until event time" option is specifically designed for appointment-based workflows. It calculates backward from the appointment date. If someone books a session that is only 12 hours away, this step will fire immediately (since 24 hours before has already passed). GHL handles this gracefully.

**Step 3: 24-Hour Reminder**
1. Add a **Send SMS** action:
   - **Message:** "Hey {{contact.first_name}}! Friendly reminder: you have a session at Sunrise Wellness tomorrow at {{appointment.start_time}}. We're excited to see you! Need to reschedule? {{appointment.reschedule_url}}"
2. Add a **Send Email** action:
   - **Subject:** "See you tomorrow, {{contact.first_name}}!"
   - **Body:** A friendly reminder with the appointment details, location, and what to bring (you can keep it shorter than the confirmation since they already received those details)

**Step 4: Wait Until 1 Hour Before**
1. Add another **Wait** action
2. Set it to: **1 hour before** the appointment

**Step 5: 1-Hour Reminder**
1. Add a **Send SMS** action:
   - **Message:** "Almost time, {{contact.first_name}}! Your session at Sunrise Wellness starts in about an hour ({{appointment.start_time}}). We're at 456 Wellness Ave -- parking in the back lot. See you soon!"

> **Why not an email too?** One hour before an appointment, people are not checking email. SMS is the right channel for last-minute reminders. Save email for the 24-hour reminder when people are still planning their day.

**Step 6: Add a "Running Late?" Option (Optional Enhancement)**
1. After the 1-hour SMS, you could include a line like: "Running late? Reply LATE and we'll adjust."
2. To handle this, you would create a separate workflow triggered by **Inbound Message** containing the word "LATE" and send yourself an internal notification
3. This is optional but adds a professional touch. For now, just add the text to the SMS -- you can build the response handler later

**Save the workflow.**

---

## Part 3: Post-Appointment -- Show vs. No-Show (45 min)

### The Critical Fork

This is where the system splits into two very different paths. When the appointment time passes, one of two things happens: the member showed up, or they did not. Each outcome needs a completely different response.

In GHL, you control this by changing the **appointment status**. When a member arrives, you (or your front desk) mark the appointment as "Showed" in the calendar. If they do not show up, you mark it as "No Show." These status changes become **triggers** for your automation.

### Exercise 13.3: Build the "Showed" Workflow

**Purpose:** When a member completes their session, automatically handle payment, update their records, and set up the review request.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Lifecycle - Showed"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Appointment Status**
3. Set status to: **Showed**
4. Select **All Calendars**

**Step 2: Update Contact's Custom Fields**
1. Add an **Update Contact Field** action
2. Set **Last Visit Date** = `{{appointment.start_date}}` (use the appointment date variable)
3. If you created a "Total Visits" custom field on Day 2, you can use a **Math Operation** action or a simple **Update Contact Field** to increment it

> **Custom Field Check:** If you did not create "Last Visit Date" on Day 2, go to **Settings > Custom Fields** and create it now (type: Date). Also create "Total Visits" (type: Number) if you want visit tracking. These fields let you build Smart Lists later like "Members who haven't visited in 30+ days."

**Step 3: Branch by Service Type**
1. Add an **If/Else** action
2. Name it: "Service Type for Payment"
3. **Branch 1 (PT Session):** Calendar Name **contains** "PT"
4. **Branch 2 (Nutrition):** Calendar Name **contains** "Nutrition"
5. **Else:** Group Class (no individual payment -- they pay through class packs)

**Step 4: PT Session Payment Path (Branch 1)**

This is where you connect the appointment to actual payment -- the key integration for today.

1. Add a **Send SMS** action (Text2Pay):
   - You will create a Text2Pay link for the PT Session product ($75) you set up on Day 6
   - **Message:** "Great session today, {{contact.first_name}}! Here's the payment link for your PT session: [Text2Pay Link]. Total: $75. Thanks for choosing Sunrise Wellness!"

> **How to Generate the Text2Pay Link:**
> - Navigate to **Payments > Invoices** in a separate tab
> - Create a quick invoice template for "PT Session - $75" using the product from Day 6
> - Note the process: in a real implementation, you would either (a) use the "Send Invoice" action in the workflow if available in your GHL version, or (b) use the Text2Pay feature under Payments to generate a payment link
> - The exact action available depends on your GHL version. Look for **"Send Invoice"** or **"Create Invoice"** in the workflow action list. If neither is available, use **Send SMS** with a manually created payment link from the Payments section
> - **For practice:** Build the workflow structure with a Send SMS action containing a placeholder like "[INSERT_PAYMENT_LINK]" -- the structure and logic are what matter for learning

2. Add a **Wait** action: 24 hours
3. Add an **If/Else** condition: Check if payment has been received
   - If your GHL version has a "Payment Received" condition, use it
   - If not, you can check for a tag (you will add a "paid" tag via a separate payment-received workflow, or check manually)
4. **If NOT paid:** Send a polite payment reminder SMS:
   - "Hi {{contact.first_name}}, just a friendly reminder about the payment for your PT session. Here's the link again: [Payment Link]. Let us know if you have any questions!"

**Step 5: Nutrition Consultation Payment Path (Branch 2)**
1. Add a **Send Email** action (invoice is better for larger amounts):
   - **Subject:** "Your Nutrition Plan - Sunrise Wellness"
   - **Body:** Include the consultation summary framework and the invoice/payment link for the Nutrition Plan product ($200) from Day 6
   - For nutrition, email with an attached invoice feels more professional than a text message since the amount is higher and clients may want a receipt for their records

**Step 6: Group Class Path (Else Branch)**
1. Add a **Send SMS** action (thank-you, no payment needed):
   - **Message:** "Great energy in class today, {{contact.first_name}}! Our next class is [Day/Time]. Want to save your spot? Book here: [Calendar Link]"
2. This is a retention touch, not a payment request. Group class members typically pay through class packs or their membership -- the per-class payment is already handled

**Step 7: First Visit Check (All Branches Reconnect Here)**

After the service-specific branch, add logic that applies to ALL showed appointments:

1. Add an **If/Else** action after the branches merge
2. Name it: "First Visit?"
3. Condition: Custom field "Total Visits" **equals** 1 (or Tag **does not have** "returning-member")
4. **If first visit:**
   - Add a **Send Email** action:
     - **Subject:** "How was your first session, {{contact.first_name}}?"
     - **Body:** A warm email asking about their experience, reminding them of their membership benefits, and encouraging them to book their next session. Include calendar booking links for all three service types
   - Add a **Tag** action: Add tag `returning-member`
5. **If NOT first visit:** Skip (they will get the review request in Part 4 instead)

**Save the workflow.**

### Exercise 13.4: Build the "No-Show" Workflow

**Purpose:** When a member does not show up, automatically send a rebooking message -- with escalation logic for repeat no-shows and special handling for VIP members.

On Day 9 you may have built a basic No-Show Nurture workflow. Today you will enhance it significantly with smarter logic.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Lifecycle - No-Show"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Appointment Status**
3. Set status to: **No Show**
4. Select **All Calendars**

**Step 2: Check if This is a Repeat No-Show**
1. Add an **If/Else** action
2. Name it: "Repeat No-Show?"
3. Condition: Contact **has tag** `no-show-warning`

> **How this works:** The first time someone no-shows, they will NOT have this tag, so they go to the "first no-show" branch. At the end of that branch, you add the tag. If they no-show again, they WILL have the tag, so they go to the "repeat no-show" branch. Simple but effective.

**Step 3: First No-Show Path (Does NOT have "no-show-warning" tag)**

1. Add a **Wait** action: 30 minutes
   - Why wait? You do not want to message them the instant they miss the appointment. Maybe they are stuck in traffic and will show up 10 minutes late. Give a grace period
2. Add a **Send SMS** action:
   - **Message:** "Hi {{contact.first_name}}, we missed you at Sunrise Wellness today! No worries -- things happen. Want to rebook? Here's a link to grab a new time: [Calendar Booking Link]. We'd love to see you!"
3. Add a **Tag** action: Add tag `no-show-warning`
4. Add a **Wait** action: 24 hours
5. Add an **If/Else** condition: Has tag `appointment-rebooked`? (You would add this tag via your booking confirmation workflow)
   - **If rebooked:** Remove the `no-show-warning` tag (they rebooked, give them a clean slate), then end workflow
   - **If NOT rebooked:** Send a follow-up email:
     - **Subject:** "We saved a spot for you, {{contact.first_name}}"
     - **Body:** Friendly email with booking links, mention of what they are missing, and a gentle nudge. Do NOT guilt-trip -- keep it warm and inviting

**Step 4: Repeat No-Show Path (HAS "no-show-warning" tag)**

This person has no-showed at least once before. The tone shifts slightly.

1. Add an **If/Else** action
2. Name it: "VIP Member?"
3. Condition: Contact **has tag** `member-vip` (the tag from Day 6 / membership tier)

**Step 4a: VIP Repeat No-Show**
- VIP members pay $249/month. You do NOT send them an automated "you missed your appointment" text. That feels impersonal for someone paying premium rates.
1. Add a **Create Task** action (or **Internal Notification**):
   - **Task title:** "VIP No-Show: {{contact.first_name}} {{contact.last_name}} - Personal Follow-Up Needed"
   - **Assign to:** Yourself (or the account owner)
   - **Due date:** Today
   - **Description:** "{{contact.first_name}} is a VIP member ($249/mo) who has no-showed twice. Do NOT send automated messages. Call them personally to check in and rebook."
2. Add a **Tag** action: Add tag `no-show-risk`

**Step 4b: Non-VIP Repeat No-Show**
1. Add a **Send SMS** action:
   - **Message:** "Hi {{contact.first_name}}, we noticed you've missed a couple of sessions lately. We want to make sure everything is okay! If your schedule has changed, we can find times that work better. Let us know: [Calendar Link]"
2. Add a **Tag** action: Add tag `no-show-risk`
3. Add a **Send Email** action:
   - **Subject:** "Let's find a better time for you, {{contact.first_name}}"
   - **Body:** Empathetic email acknowledging that schedules change, offering flexible booking options, mentioning virtual or alternative session times if available

> **Why the "no-show-risk" tag matters:** On Day 2, you learned about Smart Lists. Create a Smart List called "No-Show Risk" where the filter is "Tag is no-show-risk." This gives you a dashboard of members who might be disengaging -- perfect for proactive outreach before they cancel their membership entirely.

**Save the workflow.**

---

## Part 4: Post-Service --> Payment --> Review Chain (45 min)

### Connecting the Dots

This is the part that makes the whole system feel like one continuous experience. After the member has showed up and paid, you want to capture that positive post-session energy and channel it into a Google review. But you need to time it right -- too soon feels pushy, too late and the feeling fades.

### Exercise 13.5: Payment Tracking Workflow

**Purpose:** When a payment is received (from the Text2Pay link or invoice sent in Exercise 13.3), tag the contact and prepare them for the review request.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Appointment Lifecycle - Payment Received"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select **Payment Received** (under Payment triggers)
   - If your GHL version does not have this trigger, use **Invoice Status Changed** to "Paid" or **Order Form Submission** -- check what is available in your trigger list
3. Save the trigger

**Step 2: Add Payment Confirmation**
1. Add a **Send SMS** action:
   - **Message:** "Payment received! Thanks, {{contact.first_name}}. Your receipt has been emailed. See you at your next session!"
2. Add a **Tag** action: Add tag `paid-current`
3. Add a **Remove Tag** action: Remove tag `payment-pending` (if you used this tag in Exercise 13.3)

**Step 3: Bridge to Review Request**
1. Add a **Wait** action: 2 hours
   - Why 2 hours? The member just paid. They are still in a good mood from the session. They have had time to shower, eat, settle in -- but the experience is still fresh. This is the sweet spot for a review request
2. Add a **Send SMS** action (Review Request):
   - **Message:** "Hey {{contact.first_name}}! We loved seeing you at Sunrise Wellness today. If you have 30 seconds, would you mind sharing your experience? It really helps us out: [Google Review Link]. Thank you!"

> **Google Review Link:** This is the direct link to your Google Business review page. If you set up Google integration on Day 10, you can find this link in **Reputation > Settings**. If you do not have Google connected, use a placeholder URL for now -- the workflow structure is what matters.

**Step 4: Review Follow-Up**
1. Add a **Wait** action: 3 days
2. Add an **If/Else** condition: Has tag `left-review`?
   - **If YES:** End workflow (no need to ask again)
   - **If NO:** Send a follow-up email:
     - **Subject:** "Quick favor, {{contact.first_name}}?"
     - **Body:**
       ```
       Hi {{contact.first_name}},

       A few days ago you had a session at Sunrise Wellness
       and we hope you loved it!

       If you have a minute, we'd really appreciate a quick
       Google review. It helps other people discover us and
       it honestly makes our day to read your feedback.

       [Leave a Review] (link to Google review page)

       Already left one? Ignore this -- and THANK YOU!

       -- The Sunrise Wellness Team
       ```

> **The "left-review" Tag:** GHL's Reputation Management can detect when reviews come in (if Google is connected). You can create a workflow triggered by "Review Received" that adds the `left-review` tag to the contact. If you do not have Google connected, you will need to add this tag manually when you see a review come in.

**Save the workflow.**

### Exercise 13.6: Group Class Review Request (No Payment Step)

**Purpose:** Group class members do not pay per session -- they pay through memberships or class packs. So the review request needs to fire based on the appointment completion, not payment.

Navigate to **Automation > Workflows**

You have two options for handling this:

**Option A: Add to the "Showed" Workflow**

Go back to the "Appointment Lifecycle - Showed" workflow (Exercise 13.3). In the Group Class branch (the Else branch), after the thank-you SMS:

1. Add a **Wait** action: 2 hours
2. Add a **Send SMS** action (same review request message from Exercise 13.5)
3. Add a **Wait** action: 3 days
4. Add the same review follow-up logic from Exercise 13.5

**Option B: Create a Separate Workflow (Cleaner)**

Create a new workflow triggered by Appointment Status = Showed, filtered to only the Group Class calendar:

1. **Trigger:** Appointment Status = Showed, Calendar = Group Class calendar
2. **Wait:** 2 hours
3. **Send SMS:** Review request
4. **Wait:** 3 days
5. **If/Else:** Has tag `left-review`?
   - **No:** Send follow-up email
   - **Yes:** End

> **Which option is better?** Option B is cleaner because it keeps your workflows modular. Each workflow has one clear purpose. But Option A works fine if you prefer fewer workflows. Choose whichever makes sense to you -- the important thing is that every service type eventually leads to a review request.

**Save the workflow.**

---

## Part 5: End-to-End Test (30 min)

### Exercise 13.7: Test the Complete Appointment Lifecycle

**Purpose:** Walk through the entire system you just built and verify that each step fires correctly. This is the most important part of the day -- building workflows is only half the job. Testing them is the other half.

**Testing Approach:**

You are going to simulate the complete lifecycle using a test contact. If you created a test contact on Day 2, use that one. Otherwise, create a new contact now with a name like "Test Member" and use your own email and phone number so you can verify messages are received.

> **Publishing Workflows:** Before testing, you need to **Publish** all the workflows you built today. Go to each one and toggle it from Draft to Published (or click the Publish button). Workflows in Draft mode do not fire.

**Test Path 1: Successful PT Session (Full Happy Path)**

Walk through these steps and check off each verification:

1. **Book a PT Session**
   - Go to **Calendars** and book a PT session for your test contact
   - Or use the calendar booking link as if you were the member
   - **Verify:** Confirmation email received? Confirmation SMS received? Content mentions PT-specific details (water bottle, towel)?

2. **Check Reminder Chain**
   - Since you probably booked the test appointment for today or tomorrow, the 24-hour reminder should fire soon (or may have already passed)
   - **Verify:** Check the workflow execution log. Navigate to the contact's record and look at the **Activity** or **Workflow** tab to see which workflows are active and what step they are on
   - **Shortcut for testing:** If you do not want to wait 24 hours, you can temporarily change the Wait times to 5 minutes, test, and then change them back

3. **Mark as Showed**
   - Go to **Calendars**, find the test appointment, and change the status to **Showed**
   - **Verify:** Text2Pay / invoice SMS sent? "Last Visit Date" custom field updated? If this is the first visit, did the "first session" email send?

4. **Check Payment Flow**
   - If using a real Text2Pay link, complete the test payment
   - If using placeholders, manually add the `paid-current` tag to simulate payment
   - **Verify:** Payment confirmation SMS sent? `paid-current` tag added?

5. **Check Review Request**
   - The review request should fire 2 hours after the payment (or after marking showed for group classes)
   - **Shortcut:** Temporarily change the 2-hour wait to 5 minutes for testing
   - **Verify:** Review request SMS received? Google review link is correct and clickable?

**Test Path 2: No-Show Path**

1. Book another appointment for the test contact
2. When the appointment time passes, mark it as **No Show**
3. **Verify:** 30-minute wait, then rebooking SMS? `no-show-warning` tag added?
4. **Bonus:** Mark the same contact as No Show a second time and verify the repeat no-show logic fires

**Test Path 3: VIP No-Show (If Applicable)**

1. Add the `member-vip` tag to your test contact
2. Make sure they also have the `no-show-warning` tag (from the previous test)
3. Mark an appointment as No Show
4. **Verify:** No automated SMS sent? Internal task created for personal follow-up?

> **Testing Tip:** After each test, check the contact's **Activity Feed** in their contact record. This shows every email, SMS, tag change, and workflow action that fired. It is your debugging dashboard. If something did not fire, check: (1) Is the workflow published? (2) Does the trigger match? (3) Is there an If/Else condition the contact does not meet?

**After Testing:**

- Reset your Wait times back to the production values (24 hours, 1 hour, 2 hours, 3 days)
- Remove test tags from your test contact if you want a clean slate
- Review any workflows that did not fire correctly and troubleshoot

---

## Integration Checkpoint

You have now built a complete appointment-based business system. Verify each piece is in place:

- [ ] **Confirmation workflow** fires on booking and sends service-specific messages (PT / Class / Nutrition)
- [ ] **24-hour reminder** sends the day before the appointment
- [ ] **1-hour reminder** sends an hour before with location details
- [ ] **"Showed" workflow** fires when appointment is marked as showed
- [ ] **Payment link or invoice** sends automatically after a PT or Nutrition session
- [ ] **Custom fields** update (Last Visit Date, Total Visits)
- [ ] **First-visit email** sends for new members
- [ ] **No-show workflow** sends rebooking message after 30-minute grace period
- [ ] **Repeat no-show** escalation works (different messaging + "no-show-risk" tag)
- [ ] **VIP no-show** creates a manual task instead of automated messaging
- [ ] **Payment received** triggers confirmation and bridges to review request
- [ ] **Review request** sends 2 hours after payment (or after group class)
- [ ] **Review follow-up** sends 3 days later if no review received
- [ ] **All workflows** are published and tested

**Total workflows built today:** 4-5 (Confirmation, Reminders, Showed, No-Show, Payment/Review)

---

## Case Scenario 1: BrightSmile Dental

**Scenario:** BrightSmile Dental needs the same appointment lifecycle system, but for dental procedures. Their services are very different from a wellness studio -- dental appointments involve medical prep, insurance, and procedure-specific aftercare.

**Your Task:** Adapt the system you just built for BrightSmile Dental. Think through each stage and how it changes.

### Appointment Confirmation
- **New Patient Exam ($150):** Confirmation should include: what to bring (insurance card, photo ID, list of current medications), arrive 15 minutes early for paperwork, nothing to eat 2 hours before if X-rays are planned
- **Teeth Cleaning ($200):** Confirmation includes: appointment will take about 60 minutes, brush and floss as normal beforehand, what to expect during the cleaning
- **Whitening ($450):** Confirmation includes: avoid coffee/wine/dark foods for 48 hours before, the procedure takes about 90 minutes, sensitivity is normal afterward
- **Complex Procedures ($1,500-$3,000):** Confirmation includes: pre-procedure instructions specific to the work being done, any fasting requirements, arrange someone to drive you if sedation is involved

### Reminders
- 48-hour reminder (dental patients need more advance notice to prep)
- 2-hour reminder with parking and office location
- Include a "running late?" option since dental offices run on tight schedules

### Post-Appointment
- **Showed pathway:**
  - Send aftercare instructions by procedure type (this is critical for dental -- different procedures have very different aftercare)
  - Cleaning: "Avoid eating for 30 minutes. If sensitivity persists beyond 24 hours, call us."
  - Whitening: "Avoid dark foods/drinks for 48 hours. Here is your maintenance guide."
  - Complex: "Detailed aftercare PDF attached. Call us immediately if you experience [symptoms]."
  - Generate invoice for the procedure amount
  - If insurance is involved, send a "Your insurance has been billed" notification instead

- **No-show pathway:**
  - More formal tone than a wellness studio (dental no-shows have bigger consequences)
  - Include that the reserved time could have helped another patient (gentle accountability)
  - Offer to reschedule to a less-busy day/time

### Review Request
- Wait 24 hours (not 2 -- dental patients need recovery time)
- Personalize by procedure: "How was your cleaning experience?" vs. "How is your recovery going? When you're feeling up to it, we'd love to hear about your experience"
- For complex procedures, wait 7 days before requesting a review

**Design Challenge:** Map out the complete BrightSmile workflow on paper or in a note. What triggers, branches, and messages would you need? You do not need to build it in GHL -- the thinking exercise is what matters. But if you have time, try building at least the confirmation workflow.

---

## Case Scenario 2: Elevate Digital Agency

**Scenario:** Elevate Digital Agency's "appointments" are client meetings -- strategy calls, onboarding sessions, and quarterly reviews. The lifecycle is very different because the "product" is not a physical service but a relationship-driven professional engagement.

**Your Task:** Adapt the appointment lifecycle for a digital agency context.

### Meeting Confirmation
- **Strategy Call (Prospect):** Confirmation includes: pre-call questionnaire link, Zoom meeting link, "Please have your current marketing metrics ready (website traffic, social media followers, current ad spend)," meeting agenda preview
- **Onboarding Session (New Client):** Confirmation includes: what access credentials to prepare (Google Analytics, social media logins, website admin), welcome packet PDF attached, Zoom link, "This session typically runs 90 minutes"
- **Monthly Review (Existing Client):** Confirmation includes: Zoom link, "Your monthly report is attached -- please review before our call so we can focus on strategy, not just numbers," agenda preview
- **Quarterly Strategy Session:** Confirmation includes: pre-meeting survey link ("What are your goals for next quarter?"), Zoom link, agenda, "We recommend having your executive team join this call"

### Reminders
- 24-hour reminder with Zoom link re-sent (people always lose it)
- 15-minute reminder: "Your call starts in 15 minutes. Here is your Zoom link: [link]" -- for virtual meetings, the link in the final reminder is essential
- No "parking details" needed -- it is virtual

### Post-Meeting
- **Showed pathway:**
  - For Strategy Call (Prospect): Auto-send a "Thanks for your time" email + proposal PDF within 2 hours + move pipeline opportunity to "Proposal Sent" stage
  - For Onboarding: Send "Welcome aboard" email + next steps checklist + schedule the first monthly review
  - For Monthly Review: Send meeting summary email + action items + any updated deliverables
  - No immediate payment request for strategy calls (retainer billing is monthly, not per-meeting)

- **No-show pathway:**
  - Very professional tone: "We had your strategy call scheduled for today but didn't see you on Zoom. Would you like to reschedule? Here's a link to find a new time."
  - For existing clients who no-show: Internal notification to account manager (this could signal client disengagement)
  - For prospects who no-show: Follow up once, then move to "Cold" pipeline stage if no response in 48 hours

### Follow-Up (Instead of Review Request)
- Agencies do not typically ask for Google reviews after meetings -- instead:
  - After Strategy Call: "Have you had a chance to review the proposal?" follow-up in 48 hours
  - After Onboarding: "How was your onboarding experience?" satisfaction survey
  - After 90 days as a client: THEN request a Google review or case study participation
  - Request LinkedIn recommendation instead of (or in addition to) Google review

**Design Challenge:** What is the biggest difference between building this system for a service business (dental/wellness) vs. a professional services firm (agency)? Think about how the payment model changes everything -- per-session billing vs. monthly retainers means the "appointment > payment > review" chain works completely differently.

---

## What You Built Today

You started the day with separate, disconnected features: calendars that book appointments, templates that send messages, products that generate invoices, and a reputation system that requests reviews. Now you have a single, unified system where one event (a booking) sets off an entire chain of perfectly timed actions that guide the member from booking to review without a single manual step.

This is the power of integration. Each feature you built in Phase 1 was a building block. Today you connected those blocks into a machine.

Tomorrow, you will do the same thing for your sales and payment systems -- building a complete e-commerce funnel that sells memberships online, handles abandoned checkouts, and onboards new members automatically.

---

*Phase 2 continues with Day 14: E-Commerce & Payment Funnel System*
