# Day 3: Conversations & Communication

**Time Required:** 3-4 hours
**Certification Alignment:** Conversations Tab, SMS/Email Templates, Manual Actions, Webchat Widget, Missed Call Text Back, Phone Numbers
**API Lab:** Yes - `scripts/day-03-conversations-api.py`

---

## Today's Mission

Yesterday you built the member database for Sunrise Wellness Studio -- importing contacts, creating custom fields for fitness goals and membership tiers, and tagging members by interest. Today you'll set up the communication system that those members will actually experience. You'll create SMS and email templates branded for the studio (welcome messages, class reminders, review requests), configure the webchat widget for the studio website, and explore missed call handling. By end of today, Sunrise Wellness will have a complete template library ready for the automations you'll build on Day 9.

---

## Learning Objectives

1. Navigate and effectively use the Conversations tab across all channels
2. Create reusable SMS and Email templates with dynamic fields for Sunrise Wellness Studio
3. Configure the Webchat widget and Missed Call Text Back
4. Send messages programmatically via the GHL API

---

## Part 1: Conversations Tab Deep Dive (45 min)

### Theory Recap

The Conversations tab is GHL's unified inbox. All communication channels converge here:
- **SMS/Text** - Two-way texting via LC Phone
- **Email** - Send/receive emails
- **Facebook Messenger** - If FB page is connected
- **Instagram DM** - If IG is connected
- **Google Business Messages** - If Google profile is connected
- **WhatsApp** - If WhatsApp Business is connected
- **Webchat** - Live chat from your website/funnel
- **Phone Calls** - Call logs and recordings

For Sunrise Wellness Studio, the most critical channels are SMS (class reminders, quick updates), Email (welcome sequences, newsletters, offers), and Webchat (website visitors asking about memberships and class schedules).

### Hands-On Exercise 3.1: Explore the Conversations Interface

1. Navigate to **Conversations** (left sidebar)
2. Explore the layout:
   - **Left panel:** Contact list with filters (Unread, Starred, All, Recent)
   - **Center panel:** Message thread
   - **Right panel:** Contact details, notes, tags, appointments
3. Filter conversations by:
   - Channel type (SMS, Email, etc.)
   - Assigned user
   - Read/Unread status
   - Starred conversations
4. Try the search function - search by name, email, or message content
5. Think about how the front desk at Sunrise Wellness would use this view:
   - A new lead just filled out the "Free Trial" form on the website -- where does that conversation appear?
   - A Premium member texted asking to cancel tomorrow's PT session -- how would you find it?
   - Three unread messages came in overnight -- how do you triage them?

### Hands-On Exercise 3.2: Explore Phone Number Configuration

Navigate to **Settings > Phone Numbers**:

**If your sub-account already has a phone number:**
1. Review the existing number configuration
2. Check the assigned friendly name, forwarding rules, and call recording settings
3. Test: Send an SMS from your personal phone to the GHL number
4. Check if it appears in Conversations
5. Reply from GHL and verify it's received on your personal phone

**If no phone number exists (common for practice sub-accounts):**
1. Explore the "Buy Number" interface -- note the options (local, toll-free, area code selection)
2. Review the configuration options you WOULD set:
   - Friendly name: "Sunrise Wellness Studio"
   - Forwarding number: owner's personal cell
   - Call recording: enabled for quality assurance
3. **Focus on email-based exercises** for the rest of this lesson -- you can still practice all templates, webchat, and conversations via email
4. SMS-specific exercises become optional/theoretical -- document what you WOULD configure

**LC Trust Center (Cert Topic) - explore regardless of phone number:**
- Navigate to Settings > Phone Numbers > Trust Center (or search "Trust Center")
- Understand A2P 10DLC registration (required for US SMS)
- Review compliance requirements for SMS messaging
- Note: For a real fitness studio, your use case would be "Marketing" and "Appointment Reminders"
- Document what registration steps are required (important for certification)

### Hands-On Exercise 3.3: Send Your First Messages

Think of this as Sunrise Wellness reaching out to members from your Day 2 contacts.

1. Open one of your test contacts in Conversations (someone tagged "interested-pt" or "free-trial")
2. **Send via Email** (works for everyone):
   - Switch to the email channel
   - Compose a quick message: "Hi {{contact.first_name}}, thanks for your interest in Sunrise Wellness Studio! We'd love to help you reach your fitness goals. Reply to this email or visit us at the studio to get started."
   - Try the formatting options: bold, italic, insert links, add attachments
   - Insert Custom Values by typing `{{` to see the dropdown
3. **Send via SMS** (if phone number available):
   - Switch to SMS channel
   - Send: "Hi {{contact.first_name}}, welcome to {{business.name}}! Reply to this text or call us at {{business.phone}} to schedule your free trial."
   - If no phone number: read through the SMS interface and note how it works, then skip to email
4. Test a message with multiple Custom Values:
   - "Hi {{contact.first_name}}, {{business.name}} has a special offer for you: {{offer.free_trial}}. Call us at {{business.phone}} to claim it!"
   - Verify that the custom values you set on Day 1 resolve correctly

---

## Part 2: SMS & Email Templates (75 min)

### Theory Recap

Templates save time and ensure every member gets a consistent, professional message from Sunrise Wellness. GHL supports:
- **SMS Templates** - Short text templates with merge fields (160-character awareness)
- **Email Templates** - Rich HTML email templates with the drag-and-drop builder

You'll create templates that cover the full member lifecycle: inquiry, booking, reminder, follow-up, and re-engagement. These same templates will be plugged into workflows on Day 9.

### Hands-On Exercise 3.4: Create SMS Templates

Navigate to **Marketing > Templates** (or access via Conversations > Templates icon):

Create these 5 SMS templates for Sunrise Wellness Studio:

**Template 1: "Welcome New Lead"**
*Trigger context: Someone just inquired about a membership (Free Trial, Basic, Premium, or VIP)*
```
Hi {{contact.first_name}}! Thanks for your interest in Sunrise Wellness Studio.

We'd love to learn about your fitness goals and find the right program for you. Reply to this text or call us at {{business.phone}} to schedule your free 7-day trial!

- The Sunrise Wellness Team
```

**Template 2: "Class Reminder - 24hr"**
*Trigger context: Member has a group fitness class (HIIT, Yoga, or Pilates) booked for tomorrow*
```
Hi {{contact.first_name}}, friendly reminder! Your group fitness class at Sunrise Wellness is tomorrow.

Date: {{appointment.date}}
Time: {{appointment.start_time}}

Please arrive 5-10 min early. Bring water and a towel!

Need to cancel? Reply CANCEL or call {{business.phone}}.
```

**Template 3: "PT Session Reminder"**
*Trigger context: Member has a Personal Training session booked for the next day*
```
Hi {{contact.first_name}}, you have a Personal Training session tomorrow at Sunrise Wellness!

Date: {{appointment.date}}
Time: {{appointment.start_time}}

Wear comfortable workout clothes and bring water. Your trainer will have your program ready.

Reply YES to confirm or call {{business.phone}} to reschedule.
```

**Template 4: "Follow-Up - No Response"**
*Trigger context: A lead inquired but hasn't replied within 48 hours*
```
Hi {{contact.first_name}}, I wanted to follow up on your inquiry about Sunrise Wellness Studio.

We're currently offering a free 7-day trial with no commitment. Would you like to come check us out?

Book your trial here: {{business.website}}

- The Sunrise Wellness Team
```

**Template 5: "Review Request"**
*Trigger context: Member completed a PT session or attended a class (sent 2 hours after)*
```
Hi {{contact.first_name}}! Thanks for your session at Sunrise Wellness today. We hope you had a great workout!

Would you mind leaving us a quick review? It helps other people find us: [REVIEW_LINK]

Thank you! See you next time.
```

**For each template:**
1. Create the template with the exact name above
2. Verify the merge fields are valid (type `{{` to browse available fields)
3. Preview the template by inserting it into a test conversation (but don't send unless you want to test delivery)
4. Note: If you don't have a phone number, still create these templates -- they'll be available when SMS is activated, and you're learning the template system either way

### Hands-On Exercise 3.5: Create Email Templates

Navigate to **Marketing > Email Templates** (or the Email Builder):

Create these 5 email templates using the drag-and-drop builder:

**Template 1: "Welcome to Sunrise Wellness"**
*Sent to: New members who just signed up (any tier)*
- **Header:** Business logo (or placeholder), warm hero image of a fitness studio
- **Greeting:** "Welcome to Sunrise Wellness, {{contact.first_name}}!"
- **Body:**
  - "We're thrilled to have you join our community. Here's what to expect:"
  - Bullet list: studio hours (Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM), class types available (HIIT, Yoga, Pilates), PT booking info
  - "Your membership includes access to all group classes. Check out the schedule and book your first class!"
- **CTA Button:** "Book Your First Class"
- **Footer:** Studio address (use {{business.address}}), phone ({{business.phone}}), email ({{business.email}}), unsubscribe link

**Template 2: "Your Training Session is Confirmed"**
*Sent to: Members who booked a Personal Training or Nutrition Consultation*
- Clean, professional design
- Appointment details: date, time, session type
- What to bring: workout clothes, water, any relevant intake forms
- "Your trainer/nutritionist will have your personalized program ready."
- CTA: "Add to Calendar" or "Reschedule"
- Cancel/reschedule link
- Studio address with map link

**Template 3: "Monthly Newsletter"**
*Sent to: All active members, monthly*
- **Header:** Logo + "Sunrise Wellness Monthly" + month/year
- **Section 1:** This month's class schedule highlights (new class times, special workshops)
- **Section 2:** Fitness tip of the month (e.g., "5 Post-Workout Recovery Tips")
- **Section 3:** Member spotlight (placeholder section -- "Meet [Member Name]!")
- **Special offer section:** "Refer a friend and you both get {{offer.referral}}"
- Social media links (placeholder icons)
- **Unsubscribe link** (required for CAN-SPAM compliance!)

**Template 4: "Special Offer"**
*Sent to: Leads or members eligible for a promotion*
- Eye-catching hero image (fitness/wellness themed)
- Offer headline: "Exclusive for You: {{offer.discount}}"
- Body: "For a limited time, take advantage of this special offer at Sunrise Wellness Studio."
- Urgency: "This offer expires on [DATE] -- don't miss out!"
- **CTA Button:** "Claim Your Offer"
- Terms and conditions (small text)
- Unsubscribe link

**Template 5: "We Miss You"**
*Sent to: Members who haven't visited in 30+ days*
- Subject line: "We miss you, {{contact.first_name}}!"
- Warm, inviting tone: "It's been a while since your last visit to Sunrise Wellness. We'd love to see you back!"
- Highlight what's new: "Since your last visit, we've added [new class/trainer/equipment]"
- Comeback offer: "Come back this week and enjoy a complimentary smoothie from our juice bar"
- **CTA:** "Book a Class Today"
- Unsubscribe link

**For each template:**
1. Use the drag-and-drop email builder
2. Add proper merge fields (type `{{` to insert)
3. Preview in both desktop and mobile views -- fitness members check email on phones between sets
4. Save as a reusable template
5. Use brand-consistent colors throughout (pick a warm palette: sunrise oranges, energetic yellows, clean whites)

---

## Part 3: Manual Actions (30 min)

### Theory Recap

Manual Actions are steps in a workflow that require human intervention. When a workflow hits a Manual Action step, it pauses and notifies the assigned user to complete the action before proceeding. At Sunrise Wellness, these would be used for high-touch interactions that shouldn't be fully automated.

Examples for the studio:
- "Call VIP lead" -- owner personally calls a VIP membership inquiry
- "Review nutrition intake form" -- nutritionist reviews before scheduling
- "Follow up on injury concern" -- trainer calls a member who reported discomfort

### Hands-On Exercise 3.6: Create and Execute Manual Actions

1. Navigate to **Conversations** and select one of your test contacts
2. Find the Manual Actions area (Tasks / Manual Actions section)
3. Create a manual action for a Sunrise Wellness scenario:
   - **Type:** "Call Lead - VIP Inquiry"
   - **Description:** "This lead inquired about the VIP membership ($249/mo). Call them personally to discuss benefits: unlimited PT sessions, priority booking, nutrition coaching included, and exclusive member events. Ask about their fitness goals and timeline."
   - **Assign to:** Yourself (as the studio owner)
4. Practice completing the manual action:
   - Open the action
   - Since this is practice, simulate performing the task
   - Mark as "Complete"
   - Add outcome notes: "Spoke with contact. Interested in VIP tier. Scheduling a studio tour for Saturday."
5. Create a second manual action:
   - **Type:** "Review Injury Report"
   - **Description:** "Member reported knee discomfort during HIIT class. Review their intake form and call to discuss modifications. Consider recommending Yoga or Pilates as alternatives."
   - Assign to yourself, complete with notes

**Why this matters:** On Day 9, you'll build workflows that include Manual Action steps. A VIP lead might trigger an automatic welcome SMS, but the personal follow-up call stays manual because that human touch converts high-value prospects.

---

## Part 4: Webchat Widget (30 min)

### Theory Recap (Cert: 2-Part Webchat Setup)

The Webchat widget adds a live chat bubble to your website or funnel. For Sunrise Wellness, this captures website visitors who are browsing class schedules, membership info, or trainer profiles and want to ask a quick question before committing.

### Hands-On Exercise 3.7: Set Up the Webchat Widget

Navigate to **Sites > Chat Widget** (or Settings > Chat Widget):

**Part 1: Configure the Widget for Sunrise Wellness**
1. Enable the chat widget
2. Customize appearance:
   - **Widget color:** Choose a warm, energetic color (sunrise orange or vibrant coral -- match your brand)
   - **Widget position:** Bottom-right (standard)
   - **Greeting message:** "Hey there! Welcome to Sunrise Wellness Studio. Have questions about classes, memberships, or personal training? We're here to help!"
   - **Agent name:** "Sunrise Wellness Team"
   - **Agent avatar:** Upload a logo or friendly team photo
3. Set availability:
   - **Online hours:** Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM (match studio hours)
   - **Offline message:** "We're currently closed, but leave your name and email and we'll get back to you first thing! Studio hours: Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM."
4. Configure lead capture:
   - Before starting the chat, collect: Name, Email, Phone (optional)
   - This creates or updates a contact in GHL -- tying back to the contact system from Day 2

**Part 2: Install and Test the Widget**
1. Get the embed code from the widget settings
2. If you have a funnel/website in GHL: toggle the widget on for that site
3. If no site yet: copy the JavaScript snippet (you'll use it when building funnels on Day 7)
4. Test the widget:
   - Open your funnel/website (or the preview)
   - Click the chat bubble
   - Fill in the pre-chat form (name, email)
   - Send a test message: "Hi, I'm interested in the Basic membership. What does it include?"
   - Go to **Conversations** and verify the message appears
   - Reply from Conversations: "Great question! The Basic membership ($79/mo) includes unlimited group fitness classes and locker access. Would you like to try a free 7-day trial?"
   - Verify the reply appears in the widget

### Hands-On Exercise 3.8: Configure Missed Call Text Back

**This exercise requires a phone number. If you don't have one, read through the setup steps and document what you WOULD configure. Skip to the API Lab.**

Navigate to **Settings > Phone Numbers** (or search for "Missed Call Text Back"):

1. Enable **Missed Call Text Back**
2. Configure the auto-response message for Sunrise Wellness:
   ```
   Sorry we missed your call! This is Sunrise Wellness Studio.

   How can we help? Whether it's class schedules, membership info, or booking a session - reply to this text and we'll get right back to you!

   Studio hours: Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM
   ```
3. Set the delay: 1 minute after the missed call
4. Test it (if phone number available):
   - Call your GHL number from your personal phone
   - Don't answer
   - Wait for the auto-text to send
   - Verify it appears in Conversations
   - Note: This is one of the highest-converting automations in GHL -- a lead calls, nobody answers, but they immediately get a text response. For Sunrise Wellness, this catches the person who called during a busy class but still wants to sign up.

---

## Part 5: API Lab - Messaging via API

### Run the Conversations API Lab

```bash
cd scripts/
python day-03-conversations-api.py
```

The script demonstrates:
1. Send an SMS to a contact via API (requires phone number on the sub-account)
2. Send an email to a contact via API
3. Retrieve conversation history for a contact
4. Search conversations

### API Exercises

1. **Welcome blast:** Write a script that sends a welcome email to all contacts tagged "free-trial" using the Day 2 contacts you imported
2. **Conversation reader:** Build a function that retrieves the last 5 messages in a conversation and prints them with timestamps
3. **Unread monitor:** Create a script that checks for unread messages older than 1 hour and prints an alert (simulating what a front desk dashboard might show)

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Clinic

**Situation:** BrightSmile Dental Clinic needs a complete communication template library and webchat setup. They have 2 dentists, 1 hygienist, and 1 front desk staff. Their patients need clear, professional communication for appointments, post-procedure care, insurance matters, and recall notices.

**Design the following (document your decisions, create what you can):**

1. **SMS Templates** (create these in GHL alongside your Sunrise Wellness templates):
   - **"Appointment Reminder - 48hr"**: "Hi {{contact.first_name}}, your dental appointment at BrightSmile Dental is in 2 days. Date: {{appointment.date}}, Time: {{appointment.start_time}}. Please arrive 10 min early. Reply C to confirm or call {{business.phone}} to reschedule."
   - **"Post-Procedure Care"**: "Hi {{contact.first_name}}, thanks for your visit today. Remember: avoid hot foods for 2 hours, take prescribed medication as directed. If you experience unusual pain or swelling, call us immediately at {{business.phone}}. - Dr. [Name], BrightSmile Dental"
   - **"Insurance Follow-Up"**: "Hi {{contact.first_name}}, we've submitted your insurance claim for your recent visit. You can expect to hear from your provider within 5-10 business days. Questions? Call us at {{business.phone}}."
   - **"6-Month Recall Notice"**: "Hi {{contact.first_name}}, it's been 6 months since your last cleaning at BrightSmile Dental! Regular cleanings are key to a healthy smile. Book your next visit: {{business.website}} or call {{business.phone}}."

2. **Email Templates** (design on paper or create in GHL):
   - **"Welcome to BrightSmile"**: New patient welcome with office hours, what to bring (insurance card, ID, medical history), parking instructions, patient portal link
   - **"Post-Visit Summary"**: Professional recap of procedures performed, care instructions, next appointment recommendation, payment summary

3. **Webchat Widget**:
   - Greeting: "Welcome to BrightSmile Dental! How can we help you today?"
   - **Key requirement:** Include a dental disclaimer in the chat: "Please note: This chat is for scheduling and general inquiries only. For dental emergencies, call us directly at {{business.phone}} or visit your nearest emergency room."
   - Pre-chat form: Name, Email, Phone, "Reason for inquiry" dropdown (New Patient, Existing Patient - Schedule, Insurance Question, Emergency)
   - After-hours message with emergency contact guidance

4. **Reflect:** How does dental communication differ from fitness studio communication? Consider HIPAA implications, urgency levels, and the tone of post-procedure care messages versus workout reminders.

### Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency manages SEO, PPC, Social Media, and Web Design for clients paying monthly retainers ($2K-$10K/mo). They need professional communication templates for onboarding new clients, keeping them informed about campaign performance, and managing contract renewals. Their 2 account managers are the primary client contacts.

**Design the following (document your decisions, create what you can):**

1. **SMS Templates** (create these in GHL):
   - **"Onboarding Welcome"**: "Hi {{contact.first_name}}, welcome to Elevate Digital! Your account manager will reach out within 24 hours to schedule your kickoff call. In the meantime, check your email for our onboarding questionnaire. - Elevate Digital Team"
   - **"Monthly Report Ready"**: "Hi {{contact.first_name}}, your monthly performance report for [MONTH] is ready! Check your email for the full breakdown. Questions? Reply here or book a review call: {{business.website}}"
   - **"Strategy Call Reminder"**: "Hi {{contact.first_name}}, reminder: your strategy call with Elevate Digital is tomorrow at {{appointment.start_time}}. We'll be reviewing your campaign performance and next month's plan. See you then!"
   - **"Contract Renewal Notice"**: "Hi {{contact.first_name}}, your Elevate Digital agreement is coming up for renewal on [DATE]. Let's schedule a call to review your results and discuss next steps. Book here: {{business.website}}"

2. **Email Templates** (design on paper or create in GHL):
   - **"Client Onboarding Kit"**: Welcome email with team introductions (account manager, specialists assigned), project timeline, login credentials for reporting dashboard, communication expectations (response times, meeting cadence)
   - **"Monthly Performance Report"**: Professional email template with sections for each service (SEO rankings, PPC spend/ROI, social media metrics), key wins, action items for next month, and CTA to book a review call

3. **Webchat Widget**:
   - Greeting: "Welcome to Elevate Digital! Looking to grow your online presence? Chat with us about our SEO, PPC, Social Media, and Web Design services."
   - Pre-chat form: Name, Email, Company Name, "What service are you interested in?" dropdown (SEO, PPC/Paid Ads, Social Media Management, Email Marketing, Web Design, Full Digital Strategy)
   - Professional, B2B tone throughout
   - After-hours: "Our team is available Mon-Fri 9AM-6PM. Leave your details and we'll reach out on the next business day."

4. **Reflect:** How does B2B agency communication differ from B2C fitness studio communication? Consider the decision-making timeline (longer for agencies), the need for ROI justification in messaging, and how the tone shifts from friendly/motivational (fitness) to professional/results-oriented (agency).

---

## Day 3 Recap Questions

1. Name all the communication channels available in GHL Conversations. Which ones would be most important for Sunrise Wellness Studio?
2. What's the difference between an SMS Template and an Email Template in terms of personalization capabilities? Why did we create both a "Class Reminder" SMS and a "Session Confirmed" email?
3. How does the Webchat widget capture visitor information before starting a chat? Why is this important for converting website visitors into Sunrise Wellness members?
4. What is the LC Trust Center, and why is A2P 10DLC registration important? What would Sunrise Wellness need to register for?
5. Explain Manual Actions -- why would the studio owner want to personally call VIP inquiries rather than automate that step?
6. How would you use the templates you created today in a workflow? (Preview: Day 9 will connect these templates to triggers like "new contact created" or "appointment booked")

---

## Next Day Preview

**Day 4: Calendars & Booking Systems** - Sunrise Wellness needs three types of booking: Personal Training (Round Robin), Group Fitness Classes (Class Booking), and Nutrition Consultations (Basic Calendar). You'll create all three, configure booking forms with fitness-specific fields, and test the full booking experience. The confirmation templates you built today will connect to these calendars when you build workflows on Day 9.

Make sure you have:
- At least 2-3 test contacts with valid email addresses (from Day 2)
- Your business hours defined (from Day 1 custom values)
- Your SMS and email templates saved (from today)
