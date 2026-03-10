# Day 3: Conversations & Communication

**Time Required:** 3-4 hours
**Certification Alignment:** Conversations Tab, SMS/Email Templates, Manual Actions, Webchat Widget, Missed Call Text Back, Phone Numbers
**API Lab:** Yes - `scripts/day-03-conversations-api.py`

---

## Learning Objectives

1. Navigate and effectively use the Conversations tab across all channels
2. Create reusable SMS and Email templates with dynamic fields
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
4. Try the search function - search by name, email, phone, or message content

### Hands-On Exercise 3.2: Explore Phone Number Configuration

Navigate to **Settings > Phone Numbers**:

**If your sub-account already has a phone number:**
1. Review the existing number configuration
2. Check the assigned friendly name, forwarding rules, and call recording settings
3. Test: Send an SMS from your personal phone to the GHL number
4. Check if it appears in Conversations
5. Reply from GHL and verify it's received on your personal phone

**If no phone number exists (and you can't purchase one):**
1. Explore the "Buy Number" interface - note the options (local, toll-free, area code selection)
2. Review the configuration options you WOULD set (friendly name, forwarding, recording)
3. **Focus on email-based exercises** for the rest of this lesson - you can still practice templates, webchat, and conversations via email
4. SMS-specific exercises become optional/theoretical - document what you WOULD configure

**LC Trust Center (Cert Topic) - explore regardless of phone number:**
- Navigate to Settings > Phone Numbers > Trust Center
- Understand A2P 10DLC registration (required for US SMS)
- Review compliance requirements for SMS messaging
- Document what registration steps are required (important for certification)

### Hands-On Exercise 3.3: Send Your First Messages

1. Open a contact in Conversations (or create one first)
2. Send an **SMS message** - type and send
3. Send an **Email** - switch to email channel, compose and send
4. Try the message formatting options:
   - Bold, italic in emails
   - Insert links
   - Add attachments
   - Insert Custom Values (type `{{` to see the dropdown)
5. Test sending a message with a Custom Value: "Hi {{contact.first_name}}, welcome to {{business.name}}!"

---

## Part 2: SMS & Email Templates (60 min)

### Theory Recap

Templates save time and ensure consistent messaging. GHL supports:
- **SMS Templates** - Short text templates with merge fields
- **Email Templates** - Rich HTML email templates with the drag-and-drop builder

### Hands-On Exercise 3.4: Create SMS Templates

Navigate to **Marketing > Templates** (or Conversations > Templates):

Create these 5 SMS templates:

**Template 1: "Welcome New Lead"**
```
Hi {{contact.first_name}}! Thanks for your interest in {{business.name}}.

We'd love to learn more about your goals. Reply to this text or call us at {{business.phone}} to get started!
```

**Template 2: "Appointment Reminder - 24hr"**
```
Hi {{contact.first_name}}, this is a reminder that you have an appointment with {{business.name}} tomorrow.

Date: {{appointment.date}}
Time: {{appointment.time}}

Reply YES to confirm or call {{business.phone}} to reschedule.
```

**Template 3: "Follow-Up After No Response"**
```
Hi {{contact.first_name}}, I noticed we haven't connected yet. I wanted to follow up on your inquiry.

Is there a good time to chat? You can also book a call here: {{business.website}}

- Team {{business.name}}
```

**Template 4: "Review Request"**
```
Hi {{contact.first_name}}! Thank you for visiting {{business.name}}. We hope you had a great experience!

Would you mind leaving us a quick review? It helps us serve you better: [REVIEW_LINK]

Thank you!
```

**Template 5: "Payment Confirmation"**
```
Hi {{contact.first_name}}, we've received your payment of ${{payment.amount}}.

Invoice #: {{invoice.number}}
Thank you for choosing {{business.name}}!

Questions? Call us at {{business.phone}}
```

For each template:
1. Create the template with the name above
2. Use the correct merge fields
3. Test it by inserting into a conversation (but don't send yet)

### Hands-On Exercise 3.5: Create Email Templates

Navigate to **Marketing > Email Templates** (or Email Builder):

Create these 5 email templates using the drag-and-drop builder:

**Template 1: "Welcome Email"**
- Header with business logo
- Greeting: "Welcome to {{business.name}}, {{contact.first_name}}!"
- Body: Brief intro, what to expect, next steps
- CTA button: "Book Your First Appointment"
- Footer: Contact info, social links, unsubscribe link

**Template 2: "Appointment Confirmation"**
- Clean, professional design
- Appointment details (date, time, location)
- What to bring / how to prepare
- Cancel/reschedule link
- Map/directions link

**Template 3: "Monthly Newsletter"**
- Header with logo and month/year
- 3 content sections with images
- Tip of the month
- Special offer section
- Social media links
- Unsubscribe link (required for compliance!)

**Template 4: "Promotional Offer"**
- Eye-catching hero image
- Offer headline: "{{offer.discount}}"
- Urgency element: "Offer ends [DATE]"
- CTA button: "Claim Your Offer"
- Terms and conditions
- Unsubscribe link

**Template 5: "Re-Engagement"**
- Subject line: "We miss you, {{contact.first_name}}!"
- Body: "It's been a while since your last visit"
- Special comeback offer
- CTA: "Come Back and Save"

For each template:
1. Use the drag-and-drop email builder
2. Add proper merge fields
3. Preview in both desktop and mobile views
4. Save as a reusable template

---

## Part 3: Manual Actions (30 min)

### Theory Recap

Manual Actions are steps in a workflow that require human intervention. When a workflow hits a Manual Action step, it pauses and notifies the assigned user to complete the action. Examples:
- "Call this lead" - user must make the call and mark complete
- "Send personalized proposal" - user reviews and sends
- "Review application" - user makes a decision

### Hands-On Exercise 3.6: Create and Execute Manual Actions

1. Navigate to **Conversations** or **Contacts**
2. Find the Manual Actions section (or create one via a workflow)
3. Create a manual action:
   - Type: "Call Lead"
   - Description: "Call this lead to introduce our services. Ask about their goals and timeline."
   - Assign to yourself
4. Practice completing the manual action:
   - Open the action
   - Perform the required task
   - Mark as "Complete"
   - Add outcome notes

---

## Part 4: Webchat Widget (30 min)

### Theory Recap (Cert: 2-Part Webchat Setup)

The Webchat widget adds a live chat bubble to your website or funnel. When visitors type a message, it creates a conversation in GHL that you can respond to in real-time.

### Hands-On Exercise 3.7: Set Up the Webchat Widget

Navigate to **Sites > Chat Widget** (or Settings > Chat Widget):

**Part 1: Configure the Widget**
1. Enable the chat widget
2. Customize appearance:
   - Widget color (match your brand)
   - Widget position (bottom-right is standard)
   - Greeting message: "Hi there! How can we help you today?"
   - Agent avatar (upload a photo or use business logo)
3. Set availability:
   - Online hours (when to show "Available")
   - Offline message: "We're currently offline. Leave a message and we'll get back to you!"
4. Configure auto-responses:
   - Initial auto-reply when someone messages
   - Collect visitor info (name, email, phone) before starting chat

**Part 2: Install the Widget**
1. Get the embed code from the widget settings
2. If you have a funnel/website in GHL, install it there (toggle it on)
3. If external website: copy the JavaScript snippet for installation
4. Test the widget:
   - Open your funnel/website
   - Click the chat bubble
   - Send a test message
   - Go to Conversations and verify you received it
   - Reply from Conversations and verify it appears in the widget

### Hands-On Exercise 3.8: Configure Missed Call Text Back

Navigate to **Settings > Phone Numbers** (or search for "Missed Call"):

1. Enable **Missed Call Text Back**
2. Configure the auto-response message:
   ```
   Sorry we missed your call! This is {{business.name}}.
   How can we help you? Reply to this text or we'll call you back shortly.
   ```
3. Set the delay (how long after a missed call to send the text)
4. Test it:
   - Call your GHL number
   - Don't answer
   - Wait for the auto-text to send
   - Verify in Conversations

---

## Part 5: API Lab - Messaging via API

### Run the Conversations API Lab

```bash
python scripts/day-03-conversations-api.py
```

The script demonstrates:
1. Send an SMS to a contact via API
2. Send an email to a contact via API
3. Retrieve conversation history for a contact
4. Search conversations

### API Exercises

1. Write a script that sends a welcome SMS to all contacts tagged "new-lead"
2. Build a function that retrieves the last 5 messages in a conversation
3. Create a notification system: if a contact has an unread message for 1+ hours, print an alert

---

## Case Scenarios

### Case Scenario 1: Law Firm Communication Setup

**Situation:** Configure your sub-account's communication templates as if it were a law firm. Focus on template creation and webchat setup (no additional staff needed).

**Your Task:**
1. Create SMS templates for (even if no phone number, practice writing them):
   - Initial inquiry response (under 2 minutes)
   - Consultation scheduling confirmation
   - Case status update notification
   - Invoice/payment reminder
   - Post-case satisfaction survey request
2. Create email templates for:
   - Welcome packet email (what to bring, what to expect)
   - Case update email with professional formatting
   - Referral request email
3. Set up the webchat widget with:
   - Legal disclaimer in the greeting
   - After-hours message with emergency contact info
   - Pre-chat form requiring name, email, phone, and case type (dropdown)
4. If you have a phone number: configure missed call text back with a professional legal tone. If not: document what the message WOULD say.

### Case Scenario 2: Restaurant Communication System

**Situation:** Configure your sub-account's templates and webchat as if it were "The Garden Table" restaurant.

**Your Task:**
1. Set up available communication channels:
   - Configure webchat widget with a restaurant greeting and reservation inquiry flow
   - If phone number available: set up missed call text back
2. Create SMS templates (practice writing them even if no phone number):
   - Reservation confirmation
   - Day-of reminder (2 hours before)
   - Waitlist notification ("Your table is ready!")
   - Thank-you with review request (2 hours after reservation time)
3. Create email templates:
   - Weekly specials newsletter
   - Birthday/anniversary special offer
   - Event invitation (wine tasting, live music, etc.)
4. Test what you can:
   - Open the webchat widget and send a test message
   - Reply from GHL Conversations
   - Send an email to a test contact using your templates

---

## Day 3 Recap Questions

1. Name all the communication channels available in GHL Conversations.
2. What's the difference between an SMS Template and an Email Template in terms of personalization capabilities?
3. How does the Webchat widget capture visitor information before starting a chat?
4. What is the LC Trust Center, and why is A2P 10DLC registration important?
5. Explain Manual Actions - when would you use them instead of automated steps?
6. What GHL API endpoint do you use to send an SMS, and what parameters are required?

---

## Next Day Preview

**Day 4: Calendars & Booking Systems** - You'll create all calendar types (Round Robin, Basic, Class), configure booking settings, and use the API to manage appointments.

Make sure you have:
- At least 1 contact with a valid email and phone number
- Your business hours defined (from Day 1 custom values)
