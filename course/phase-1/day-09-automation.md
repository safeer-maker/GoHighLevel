# Day 9: Automation & Workflows

**Time Required:** 3-4 hours
**Certification Alignment:** Workflow General Overview, Auto Missed Call Text-Back Recipe, No-Show Nurture Recipe
**API Lab:** Yes - `scripts/day-09-automation-api.py`

---

## Learning Objectives

1. Understand the workflow builder interface and all available triggers/actions
2. Build automated sequences with timing, conditions, and branching
3. Implement standard workflow recipes (Missed Call Text-Back, No-Show Nurture)
4. Create complex conditional workflows with If/Else logic

---

## Part 1: Workflow Builder Overview (30 min)

### Theory Recap

Workflows are GHL's automation engine. They follow a simple pattern:
**Trigger → Actions → (Conditions) → More Actions**

**Triggers** start the workflow:
- Contact events: Created, Tag Added/Removed, Field Changed
- Calendar: Appointment Booked, Appointment Status Changed
- Form/Survey: Submitted
- Pipeline: Opportunity Stage Changed, Status Changed
- Conversation: Inbound Message, Missed Call
- Payment: Invoice Paid, Subscription Created
- Manual: Added to workflow manually
- Custom: Webhook, API trigger

**Actions** do something:
- Communication: Send SMS, Send Email, Send Voicemail Drop
- CRM: Add/Remove Tag, Update Custom Field, Create Opportunity
- Calendar: Book Appointment
- Internal: Send Notification, Assign User, Add Task
- Logic: Wait, If/Else, Go To, Goal
- External: Webhook, HTTP Request

### Hands-On Exercise 9.1: Explore the Workflow Builder

Navigate to **Automation > Workflows**:

1. Click **+ Create Workflow**
2. Choose "Start from Scratch"
3. Explore the trigger options - click through each category
4. Add a test trigger (e.g., "Contact Tag Added")
5. Explore the action options - browse all available actions
6. Note the action categories and what each does
7. Delete the test workflow (don't save)

---

## Part 2: Build Your First Workflow (45 min)

### Hands-On Exercise 9.2: New Lead Welcome Sequence

**Trigger:** Form Submitted → "Free Consultation Request" (from Day 8)

Build this sequence:

```
[TRIGGER: Form Submitted]
    ↓
[ACTION: Add Tag "new-lead"]
    ↓
[ACTION: Send SMS]
  "Hi {{contact.first_name}}! Thanks for reaching out to {{business.name}}.
   We received your consultation request and will be in touch within 24 hours.
   Reply YES if you'd like a faster response!"
    ↓
[ACTION: Wait 5 minutes]
    ↓
[ACTION: Send Email]
  Template: "Welcome Email" (from Day 3)
    ↓
[ACTION: Internal Notification]
  To: Admin
  Subject: "New Lead: {{contact.first_name}} {{contact.last_name}}"
  Body: "New consultation request received.
         Email: {{contact.email}}
         Phone: {{contact.phone}}"
    ↓
[ACTION: Create Opportunity]
  Pipeline: Sales Pipeline
  Stage: New Lead
  Name: "{{contact.first_name}} {{contact.last_name}} - Consultation"
  Value: $500
    ↓
[ACTION: Wait 24 hours]
    ↓
[CONDITION: If/Else - Has tag "appointment-booked"?]
  → YES: End workflow (they already booked)
  → NO: Continue below
    ↓
[ACTION: Send SMS]
  "Hi {{contact.first_name}}, just following up on your consultation request.
   Would you like to schedule a time to chat? Book here: {{business.website}}"
    ↓
[ACTION: Wait 48 hours]
    ↓
[CONDITION: If/Else - Has tag "appointment-booked"?]
  → YES: End workflow
  → NO: Send final follow-up email
    ↓
[ACTION: Send Email]
  Subject: "One more thing, {{contact.first_name}}..."
  Body: "We haven't been able to connect yet..."
    ↓
[ACTION: Add Tag "needs-manual-followup"]
```

**Build it step by step:**
1. Add each action in order
2. Configure the timing (Wait steps)
3. Set up the If/Else conditions
4. Test by adding yourself as a contact and triggering the form

---

## Part 3: Workflow Recipes (45 min)

### Hands-On Exercise 9.3: Auto Missed Call Text-Back

**Certification Recipe**

Navigate to **Automation > Workflows > + Create Workflow**:

You can use a Recipe template if available, or build from scratch:

**Trigger:** Call Status → Missed Call (or Voicemail)

```
[TRIGGER: Missed Call / Voicemail Received]
    ↓
[ACTION: Wait 1 minute]
  (Small delay feels more natural than instant)
    ↓
[ACTION: Send SMS]
  "Sorry we missed your call! This is {{business.name}}.
   How can we help you? You can also book a time to chat:
   {{booking.link}}"
    ↓
[ACTION: Add Tag "missed-call"]
    ↓
[ACTION: Internal Notification]
  To: Assigned User (or All)
  "Missed call from {{contact.first_name}} {{contact.phone}}"
    ↓
[ACTION: Wait 30 minutes]
    ↓
[CONDITION: Has there been an inbound response?]
  → YES: End (they replied, human takes over)
  → NO: Continue
    ↓
[ACTION: Send SMS]
  "Hi {{contact.first_name}}, we tried calling you back.
   When's a good time to connect? Reply with your preferred time
   or book directly: {{booking.link}}"
```

**Test it:**
1. Call your GHL number from your personal phone
2. Don't answer in GHL
3. Wait 1 minute
4. Check your personal phone - did you receive the auto-text?
5. Check Conversations in GHL

### Hands-On Exercise 9.4: No-Show Nurture

**Certification Recipe**

**Trigger:** Appointment Status → Changed to "No-Show"

```
[TRIGGER: Appointment Status = No-Show]
    ↓
[ACTION: Wait 30 minutes]
    ↓
[ACTION: Send SMS]
  "Hi {{contact.first_name}}, we noticed you weren't able to make
   your appointment today. No worries! Life happens.
   Would you like to reschedule? Book a new time here: {{booking.link}}"
    ↓
[ACTION: Add Tag "no-show"]
    ↓
[ACTION: Wait 24 hours]
    ↓
[CONDITION: Has tag "appointment-booked"?]
  → YES: Remove tag "no-show", End workflow
  → NO: Continue
    ↓
[ACTION: Send Email]
  Subject: "We missed you, {{contact.first_name}}"
  Body: Friendly email with rebooking link and incentive
    ↓
[ACTION: Wait 3 days]
    ↓
[CONDITION: Has tag "appointment-booked"?]
  → YES: End workflow
  → NO: Continue
    ↓
[ACTION: Send SMS]
  "Final reminder: We still have a spot reserved for you
   at {{business.name}}. Book before it's gone: {{booking.link}}"
    ↓
[ACTION: Wait 7 days]
    ↓
[ACTION: Add Tag "needs-manual-followup"]
[ACTION: Create Task: "Manual follow-up needed for no-show"]
```

---

## Part 4: Appointment Reminder Workflow (30 min)

### Hands-On Exercise 9.5: Appointment Confirmation + Reminders

**Trigger:** Appointment Booked (any calendar)

```
[TRIGGER: Appointment Booked]
    ↓
[ACTION: Send SMS - Immediate Confirmation]
  "Your appointment with {{business.name}} is confirmed!
   Date: {{appointment.date}}
   Time: {{appointment.time}}
   We look forward to seeing you!"
    ↓
[ACTION: Send Email - Confirmation with details]
  Include: What to bring, parking info, contact number
    ↓
[ACTION: Add Tag "appointment-booked"]
    ↓
[ACTION: Wait until 24 hours before appointment]
    ↓
[ACTION: Send SMS - 24hr Reminder]
  "Reminder: Your appointment at {{business.name}} is tomorrow
   at {{appointment.time}}.
   Reply C to confirm or R to reschedule."
    ↓
[ACTION: Wait until 1 hour before appointment]
    ↓
[ACTION: Send SMS - 1hr Reminder]
  "See you in 1 hour! {{business.name}} - {{appointment.time}}"
```

---

## Part 5: Conditional Workflow with If/Else (30 min)

### Hands-On Exercise 9.6: Lead Nurture with Branching

**Trigger:** Contact Tag Added → "new-lead"

```
[TRIGGER: Tag Added "new-lead"]
    ↓
[CONDITION: Check Custom Field "Lead Source"]
  → IF Lead Source = "Facebook":
      Send SMS: "Thanks for connecting with us on Facebook!..."
      Add tag: "source-facebook"
  → IF Lead Source = "Google":
      Send SMS: "Thanks for finding us on Google!..."
      Add tag: "source-google"
  → IF Lead Source = "Referral":
      Send SMS: "Your friend referred you - welcome!..."
      Add tag: "source-referral"
  → ELSE (default):
      Send SMS: Generic welcome message
    ↓
[ACTION: Wait 2 days]
    ↓
[CONDITION: Has tag "appointment-booked"?]
  → YES: Send "Looking forward to meeting you" email → END
  → NO: Continue nurture
    ↓
[CONDITION: Check Custom Field "Budget Range"]
  → IF Budget > $5K:
      Send personalized high-value email
      Assign to senior sales rep
      Add tag "high-value-lead"
  → ELSE:
      Send standard nurture email
    ↓
[ACTION: Wait 3 days]
    ↓
[ACTION: Send "Did you know?" email with value content]
    ↓
[ACTION: Wait 4 days]
    ↓
[ACTION: Send "Last chance" offer email with booking link]
    ↓
[ACTION: Wait 7 days]
    ↓
[CONDITION: Has tag "appointment-booked"?]
  → YES: END
  → NO: Add tag "cold-lead", Move to "Nurture" email list
```

---

## Part 6: Testing Workflows (15 min)

### Hands-On Exercise 9.7: Workflow Testing Best Practices

1. **Test mode:** Check if your workflow has a test/debug mode
2. **Test contacts:** Use yourself or test contacts (not real leads)
3. **Shorten wait times:** Temporarily change "Wait 24 hours" to "Wait 1 minute" for testing
4. **Check each step:**
   - Was the SMS/email sent?
   - Was the tag applied?
   - Was the opportunity created?
   - Did the If/Else branch correctly?
5. **Review workflow history:** Check the execution log for your test contact
6. **Restore timing:** After testing, change wait times back to production values

---

## Part 7: API Lab - Workflow Triggers

```bash
python scripts/day-09-automation-api.py
```

The script covers:
1. Trigger a workflow via API webhook
2. Add a contact to a workflow via API
3. Build a custom webhook endpoint that receives GHL events

---

## Case Scenarios

### Case Scenario 1: Medical Spa Complete Automation

**Situation:** A medical spa needs end-to-end automation:

**Your Task:** Build these interconnected workflows:

1. **New Lead Flow:**
   - Form submission → Instant SMS + email → Tag → Opportunity creation → 3-day nurture if no booking

2. **Appointment Booked:**
   - Confirmation SMS + email → 24hr reminder → 1hr reminder → Pre-appointment intake form link

3. **Post-Appointment:**
   - Mark "Showed" → Send invoice/Text2Pay → After payment → Review request → If 5-star: ask for Google review, if <5: send to feedback form

4. **No-Show:**
   - 30-min follow-up → Rebooking offer → 3-day final attempt → Manual task if still no response

### Case Scenario 2: Real Estate Speed-to-Lead

**Situation:** A real estate agent needs to contact leads within 60 seconds of inquiry.

**Your Task:**
1. Build a "speed-to-lead" workflow:
   - Form submitted → Instant SMS → Wait 30 seconds → Attempt phone call → If no answer → Voicemail drop → Wait 5 min → Email with property details
2. Build a follow-up nurture:
   - If no response in 24hr → SMS → 48hr → Email → 72hr → SMS with urgency
3. Build a lead reassignment:
   - If assigned agent doesn't respond in 2hr → Reassign to backup agent → Notify manager

### Case Scenario 3: Speed-to-Lead (Full Build)

**Situation:** Build the fastest possible response system.

**Your Task:**
```
Lead submits form
  → [0 seconds] SMS: "Got your message! Calling you now..."
  → [30 seconds] Auto-call (if available) or Manual Action: "Call now"
  → [If no answer after 2 min] SMS: "Couldn't reach you. Book a time: [link]"
  → [5 min] Email: Detailed info + booking link
  → [2 hours] If no response → Reassign to next available agent
  → [24 hours] Day 2 nurture SMS
  → [48 hours] Day 3 nurture email
  → [72 hours] Final SMS with special offer
  → [7 days] Move to "long-term nurture" workflow
```

Build, test, and document this entire flow.

---

## Day 9 Recap Questions

1. Name 5 workflow triggers and 5 workflow actions available in GHL.
2. How does the If/Else condition work in workflows? What can you condition on?
3. What's the difference between "Wait X time" and "Wait until specific time"?
4. How do you test a workflow without affecting real contacts?
5. Explain the Missed Call Text-Back recipe step by step.
6. What happens when a contact is already in a workflow and the trigger fires again?

---

## Next Day Preview

**Day 10: Reputation, Memberships & Reporting** - Final day of Phase 1! You'll set up reputation management, build a community, and explore GHL reporting.

After Day 10, we'll review Phase 1 before moving to Phase 2 integration scenarios.
