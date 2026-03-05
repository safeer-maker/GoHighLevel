# Day 4: Calendars & Booking Systems

**Time Required:** 3-4 hours
**Certification Alignment:** Group Calendars (Round Robin), Basic Calendar, Class Booking, Calendar Management, Calendar Settings, User Calendar Links
**API Lab:** Yes - `scripts/day-04-calendars-api.py`

---

## Learning Objectives

1. Set up and configure all GHL calendar types (Group, Basic, Class)
2. Manage appointments and configure advanced calendar settings
3. Use user-specific calendar links for proper lead routing
4. Create and manage appointments via the GHL API

---

## Part 1: Understanding Calendar Types (15 min)

### Theory Recap

GHL offers 3 calendar types, each serving different booking needs:

| Calendar Type | Use Case | How It Works |
|--------------|----------|-------------|
| **Group (Round Robin)** | Sales teams, multiple service providers | Rotates bookings evenly across team members |
| **Unassigned (Basic)** | Single-person booking, generic service | No specific user assigned; anyone can manage |
| **Class Booking** | Group events, webinars, workshops | Multiple people book the same time slot |
| **Collective** | Requires ALL team members available | Books only when everyone is free (coming soon) |

---

## Part 2: Group Calendar - Round Robin (45 min)

### Theory Recap

Round Robin calendars distribute appointments evenly across team members. When a lead books, GHL checks each team member's availability and assigns based on:
- **Equal distribution** - Spreads bookings evenly
- **Availability** - Only shows open slots from available members
- **Priority** - You can set priority order for assignment

### Hands-On Exercise 4.1: Create a Round Robin Calendar

Navigate to **Calendars > + Create Calendar > Group**:

**Calendar Name:** "Sales Consultation"

**Step 1: Basic Settings**
- Name: "Sales Consultation"
- Description: "Book a free 30-minute consultation with our sales team"
- Duration: 30 minutes
- Buffer time: 15 minutes between appointments
- Minimum scheduling notice: 2 hours (prevent last-minute bookings)

**Step 2: Team Members**
- Add yourself as a team member
- If you have other users, add them too
- Set individual availability for each member:
  - Mon-Fri: 9:00 AM - 5:00 PM
  - Exclude lunch: 12:00 PM - 1:00 PM
- Set round-robin distribution: "Optimize for equal distribution"

**Step 3: Booking Form**
- Required fields: Name, Email, Phone
- Add custom questions:
  - "What are you most interested in?" (Dropdown)
  - "Preferred contact method" (Radio: Call / Email / Text)
  - "Any specific questions?" (Textarea)

**Step 4: Confirmation Settings**
- Confirmation page: "Thank you! Your consultation is booked."
- Send confirmation email: Yes
- Send confirmation SMS: Yes
- Add to Google Calendar: Enable (if connected)

**Step 5: Notifications**
- Notify assigned team member via email and SMS
- Notify admin on all new bookings

Save and get the booking link.

### Hands-On Exercise 4.2: Test the Round Robin

1. Open the booking link in an incognito browser window
2. Book an appointment
3. Check which team member was assigned
4. Book another appointment - verify it goes to a different team member (or same if you're the only one)
5. Check in Calendar view that the appointment appears
6. Verify confirmation email/SMS was sent

---

## Part 3: Unassigned / Basic Calendar (30 min)

### Hands-On Exercise 4.3: Create a Basic Calendar

Navigate to **Calendars > + Create Calendar > Unassigned**:

**Calendar Name:** "General Inquiry"

Configure:
1. **Duration:** 15 minutes
2. **Availability:** Mon-Fri 9AM-5PM
3. **Booking form:** Name, Email, Phone, "How can we help you?" (Textarea)
4. **Auto-confirmation:** Enable
5. **Allow walk-ins:** If available, enable for same-day booking

**Key Difference from Round Robin:**
- No team member is pre-assigned
- Any team member can claim/manage the appointment
- Good for general inquiries, initial calls, or single-person businesses

Test by booking through the link and verifying in the Calendar view.

---

## Part 4: Class Booking Calendar (30 min)

### Hands-On Exercise 4.4: Create a Class Booking Calendar

Navigate to **Calendars > + Create Calendar > Class Booking**:

**Calendar Name:** "Group Fitness Class"

Configure:
1. **Class name:** "HIIT Workout"
2. **Duration:** 45 minutes
3. **Maximum attendees:** 15 per class
4. **Recurring schedule:**
   - Monday, Wednesday, Friday: 6:00 AM, 12:00 PM, 5:30 PM
   - Saturday: 9:00 AM
5. **Booking form:** Name, Email, Phone, "Experience Level" (Dropdown: Beginner/Intermediate/Advanced)
6. **Waitlist:** Enable (when class is full, allow waitlist sign-ups)
7. **Cancellation policy:** Allow cancellation up to 4 hours before class

**Test the class booking:**
1. Open the booking link
2. Book a spot in a class
3. Book 2 more spots (simulate other attendees)
4. Verify the attendee count updates
5. Check attendee list in the calendar

---

## Part 5: Calendar Management (30 min)

### Hands-On Exercise 4.5: Manage Appointments

Navigate to **Calendars** main view:

1. **View modes:** Switch between Day, Week, and Month views
2. **Appointment details:** Click on an existing appointment:
   - View contact info
   - Change status: Confirmed, Showed, No-Show, Cancelled
   - Reschedule by dragging (if supported)
   - Add notes
3. **Book on behalf of a customer:**
   - From the calendar, click on an empty slot
   - Select "Book Appointment"
   - Search for an existing contact or create a new one
   - Complete the booking
4. **Mark outcomes:**
   - Find your test appointment
   - Mark it as "Showed" (they attended)
   - Find another and mark as "No-Show"

### Hands-On Exercise 4.6: Calendar Settings Deep Dive

Navigate to **Settings > Calendars** (or Calendar Settings):

Explore and configure:
1. **Google Calendar sync** - Connect your Google Calendar for two-way sync
2. **Outlook Calendar sync** - If applicable
3. **Timezone settings** - Verify it matches your business profile
4. **Working hours** - Default availability
5. **Appointment slot intervals** - How granular the time slots are (every 15, 30, 60 min)
6. **Overbooking protection** - Prevent double-booking across calendars

### Hands-On Exercise 4.7: User-Specific Calendar Links

**Using `{{user.calendar}}`:**

This is a merge field that resolves to the specific user's calendar link. It's critical for lead assignment:

1. Find the `{{user.calendar}}` merge field
2. Understand when to use it:
   - When a lead is assigned to a specific team member
   - In automated follow-ups where the lead should book with THEIR assigned rep
   - In round-robin assignments where subsequent communication should keep the same rep
3. Test it:
   - Assign a contact to yourself
   - Use `{{user.calendar}}` in a message to that contact
   - Verify it resolves to YOUR calendar booking link

---

## Part 6: API Lab - Calendar & Appointments

```bash
python scripts/day-04-calendars-api.py
```

The script covers:
1. List all calendars in your sub-account
2. Get available time slots for a calendar
3. Create an appointment via API
4. Update appointment status
5. Delete/cancel an appointment

### API Exercises

1. Build a script that checks tomorrow's appointments and prints a summary
2. Create a function that finds all "No-Show" appointments from the past week
3. Write a script that creates an appointment and sends a confirmation SMS (combining Day 3 + Day 4 APIs)

---

## Case Scenarios

### Case Scenario 1: Fitness Studio Booking System

**Situation:** A fitness studio needs booking for 3 different services:
- Personal Training (4 trainers, round robin)
- Group Classes (HIIT, Yoga, Pilates - max 20 per class)
- Nutrition Consultation (1 nutritionist, basic calendar)

**Your Task:**
1. Create a Round Robin calendar: "Personal Training Session"
   - 60-minute sessions, 15-min buffer
   - 4 trainers (use test accounts or yourself)
   - Mon-Sat availability
   - Custom question: "What are your fitness goals?"
2. Create 3 Class Booking calendars:
   - "HIIT Class" - Mon/Wed/Fri 6AM & 5:30PM, max 20
   - "Yoga Class" - Tue/Thu 7AM & 6PM, max 15
   - "Pilates Class" - Mon/Wed/Fri 10AM, max 12
3. Create a Basic Calendar: "Nutrition Consultation"
   - 45-minute sessions
   - Tue/Thu 9AM-3PM only
   - Custom intake form with dietary restrictions dropdown
4. Test booking on all calendars
5. Create a confirmation workflow outline (which messages send when)

### Case Scenario 2: Consulting Firm - Lead-Specific Booking

**Situation:** A consulting firm assigns leads to specific consultants via automation. When following up, the lead should ONLY book with their assigned consultant.

**Your Task:**
1. Create a Round Robin calendar for initial lead assignment
2. Set up the `{{user.calendar}}` link system
3. Design the flow:
   - Lead fills out inquiry form
   - Automation assigns to a consultant (round robin)
   - Follow-up SMS/email includes `{{user.calendar}}` so they book with their assigned consultant
4. Test the complete flow with 2 different contacts
5. Document what happens if the assigned consultant is unavailable

---

## Day 4 Recap Questions

1. What are the 3 main calendar types in GHL, and when would you use each?
2. How does Round Robin distribution work? Can you prioritize certain team members?
3. What is buffer time, and why is it important for service-based businesses?
4. Explain the `{{user.calendar}}` merge field and when to use it.
5. A client says "My team is getting double-booked." What calendar settings would you check?
6. How do you handle no-shows in GHL calendars? What status options are available?

---

## Next Day Preview

**Day 5: Opportunities & Pipelines** - You'll design sales pipelines, create and manage opportunities, and track deal flow both manually and via API.
