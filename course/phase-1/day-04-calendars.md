# Day 4: Calendars & Booking Systems

**Time Required:** 3-4 hours
**Certification Alignment:** Group Calendars (Round Robin), Basic Calendar, Class Booking, Calendar Management, Calendar Settings, User Calendar Links
**API Lab:** Yes - `scripts/day-04-calendars-api.py`

---

## Today's Mission

Sunrise Wellness Studio needs three types of booking: one-on-one Personal Training sessions (Round Robin among trainers), Group Fitness Classes where multiple members book the same time slot (HIIT, Yoga, Pilates), and Nutrition Consultations with a single specialist (Basic Calendar). Today you'll create all three using GHL's calendar types, configure booking forms with fitness-specific intake questions, and test the full booking experience from the member's perspective. These calendars connect directly to the templates you created on Day 3 -- the "PT Session Reminder" and "Class Reminder" SMS templates will fire when members book through these calendars, which you'll wire up with workflows on Day 9.

---

## Learning Objectives

1. Understand the three GHL calendar types and when each applies to Sunrise Wellness services
2. Create and configure Round Robin, Basic, and Class Booking calendars with custom booking forms
3. Manage appointments: view modes, status marking, and booking on behalf of members
4. Configure advanced calendar settings: Google sync, timezone, overbooking protection
5. Explore user-specific calendar links (`{{user.calendar}}`) for trainer-specific booking

---

## Part 1: Understanding Calendar Types (20 min)

### Theory Recap

GHL offers 3 calendar types (plus Collective, which is less common). Each maps to a different Sunrise Wellness service:

| Calendar Type | Sunrise Wellness Use | How It Works |
|--------------|---------------------|-------------|
| **Group (Round Robin)** | Personal Training Sessions | Rotates bookings across trainers (you + future staff). When a member books PT, GHL assigns the next available trainer. |
| **Unassigned (Basic)** | Nutrition Consultation | Single specialist handles all bookings. No rotation needed -- the nutritionist is the only person offering this service. |
| **Class Booking** | HIIT, Yoga, Pilates classes | Multiple members book the same time slot. A 6AM HIIT class can have up to 20 people. |
| **Collective** | Staff meetings (rare) | Requires ALL selected members to be available. Used internally, not for member-facing booking. |

**Why these matter for the studio:**
- **Round Robin for PT** - In production, you'd have 3 trainers. Members book "Personal Training" without choosing a specific trainer, and GHL distributes evenly. For now, you'll add yourself as the sole member (all bookings go to you), but you'll learn the full Round Robin interface.
- **Basic for Nutrition** - There's only one nutritionist, so rotation doesn't apply. Simple and clean.
- **Class Booking for Group Fitness** - This is the only type that allows multiple people per slot. A yoga class with 15 spots needs this.

---

## Part 2: Round Robin - Personal Training Session (45 min)

### Hands-On Exercise 4.1: Create a Round Robin Calendar

Navigate to **Calendars > + Create Calendar > Group**:

**Calendar Name:** "Personal Training Session"

**Step 1: Basic Settings**
- **Name:** "Personal Training Session"
- **Description:** "Book a 1-on-1 Personal Training session at Sunrise Wellness Studio. Our certified trainers will create a custom workout plan based on your goals."
- **Duration:** 60 minutes
- **Buffer time:** 15 minutes between appointments (trainer needs time to clean equipment, review the next client's program, and reset the training area)
- **Minimum scheduling notice:** 4 hours (prevents last-minute bookings that disrupt the trainer's day)

**Step 2: Team Members**
- Add yourself as the team member
- **Single-user reality:** Round Robin with one person assigns all bookings to you. This is perfectly fine for learning. In a production Sunrise Wellness Studio, you'd add your 3 trainers here (Coach Mike, Coach Sarah, Coach Jess), and GHL would distribute sessions evenly among them.
- Set your availability:
  - **Monday - Friday:** 6:00 AM - 9:00 PM
  - **Saturday:** 8:00 AM - 4:00 PM
  - **Sunday:** Closed for PT (group classes only on Sunday)
- Explore the distribution settings:
  - **"Optimize for equal distribution"** - Ensures each trainer gets roughly the same number of sessions per week. Best for Sunrise Wellness so no trainer is overloaded.
  - **"Availability-based"** - Books whoever has the next open slot. Faster for the member but can lead to uneven workloads.
  - Select "Optimize for equal distribution" for the studio.

**Step 3: Booking Form**
- **Required fields:** Name, Email, Phone
- **Add custom questions for the PT intake:**
  - **"Fitness Goals"** (Dropdown): Weight Loss / Muscle Building / Endurance / Flexibility / Injury Rehabilitation / General Fitness
  - **"Experience Level"** (Dropdown): Beginner (new to working out) / Intermediate (1-2 years) / Advanced (3+ years)
  - **"Any injuries or medical conditions we should know about?"** (Textarea) - Critical for trainer safety and liability
- These custom fields map to the contact fields you created on Day 2. When someone books, their answers populate their contact record.

**Step 4: Confirmation Settings**
- **Confirmation page message:** "You're all set! Your Personal Training session at Sunrise Wellness Studio is confirmed. You'll receive a confirmation email shortly with all the details. Please arrive 10 minutes early wearing comfortable workout clothes and bring a water bottle."
- **Send confirmation email:** Yes (this will use a default confirmation, or your Day 3 "Your Training Session is Confirmed" email template once workflows are set up)
- **Send confirmation SMS:** Yes (if phone number available; otherwise email only)
- **Add to Google Calendar:** Enable if connected (the member gets a calendar invite)

**Step 5: Notifications**
- Notify assigned team member (you) via email on new bookings
- Enable cancellation and reschedule notifications

Save the calendar and copy the booking link.

### Hands-On Exercise 4.2: Test the Round Robin Booking

1. Open the booking link in an **incognito/private browser window** (so you experience it as a member would)
2. Browse available dates and times -- verify the availability matches what you configured (Mon-Sat, studio hours)
3. Select a time slot and fill out the booking form:
   - Name: Use a test name (e.g., "Alex Test Member")
   - Email: Use a real email you can check
   - Fitness Goals: "Weight Loss"
   - Experience Level: "Beginner"
   - Injuries: "Previous knee surgery - cleared for exercise with modifications"
4. Complete the booking
5. Verify:
   - Check the **Calendar view** in GHL -- does the appointment appear?
   - Check the **Contact record** -- was a new contact created (or existing one updated) with the intake answers?
   - Check your email -- did you receive a notification as the assigned trainer?
   - Check the confirmation page message displayed correctly
6. Book a second appointment at a different time to see how the calendar fills up
7. Since you're the only team member, both bookings go to you. Note: with multiple trainers, GHL would distribute to the next available/least-booked trainer.

---

## Part 3: Basic Calendar - Nutrition Consultation (30 min)

### Hands-On Exercise 4.3: Create a Basic Calendar

Navigate to **Calendars > + Create Calendar > Unassigned**:

**Calendar Name:** "Nutrition Consultation"

**Step 1: Basic Settings**
- **Name:** "Nutrition Consultation"
- **Description:** "Schedule a 45-minute nutrition consultation with our certified nutritionist. We'll review your dietary habits, set goals, and create a personalized nutrition plan."
- **Duration:** 45 minutes
- **Buffer time:** 15 minutes (nutritionist needs time to prep notes for next client)
- **Minimum scheduling notice:** 24 hours (nutritionist needs time to review intake form)

**Step 2: Availability**
- **Tuesday:** 9:00 AM - 3:00 PM
- **Thursday:** 9:00 AM - 3:00 PM
- All other days: Not available
- This reflects the Sunrise Wellness nutritionist's schedule -- they work Tuesdays and Thursdays only.

**Step 3: Booking Form**
- **Required fields:** Name, Email, Phone
- **Custom questions for nutrition intake:**
  - **"Dietary restrictions"** (Multi-select / Checkboxes): Vegetarian / Vegan / Gluten-Free / Dairy-Free / Keto / Paleo / Halal / Kosher / No Restrictions
  - **"Current supplements you're taking"** (Textarea): "List any vitamins, protein powders, or supplements you currently use"
  - **"Primary nutrition goal"** (Dropdown): Weight Management / Sports Performance / Muscle Gain / General Health / Medical Dietary Needs
- Note: The multi-select for dietary restrictions is important -- members often have multiple restrictions (e.g., Vegan + Gluten-Free)

**Step 4: Confirmation**
- Confirmation message: "Your Nutrition Consultation is confirmed! Please complete the intake questionnaire we'll email you before your appointment. This helps your nutritionist prepare a personalized plan. See you at Sunrise Wellness Studio!"
- Enable email confirmation

**Key difference from Round Robin:**
- No team member rotation -- this is an unassigned/basic calendar
- In practice, the nutritionist claims and manages these appointments
- Ideal when there's a single provider for a service type
- The nutritionist's limited Tue/Thu availability is enforced by the calendar, not by team member settings

Test by opening the booking link in incognito and booking a slot. Verify it only shows Tuesday and Thursday availability.

---

## Part 4: Class Booking - Group Fitness Classes (45 min)

### Hands-On Exercise 4.4: Create Class Booking Calendars

Navigate to **Calendars > + Create Calendar > Class Booking**:

You'll create 3 class calendars. Each group fitness class at Sunrise Wellness has its own schedule, capacity, and character.

**Class Calendar 1: "HIIT Class"**
- **Name:** "HIIT Class"
- **Description:** "High-Intensity Interval Training. 45 minutes of heart-pumping cardio and strength circuits. All fitness levels welcome -- modifications provided!"
- **Duration:** 45 minutes
- **Maximum attendees:** 20 per class
- **Recurring schedule:**
  - Monday: 6:00 AM, 5:30 PM
  - Wednesday: 6:00 AM, 5:30 PM
  - Friday: 6:00 AM, 5:30 PM
- **Booking form:** Name, Email, Phone, "Experience Level" (Dropdown: First Timer / Beginner / Intermediate / Advanced)
- **Waitlist:** Enable -- when a class hits 20, allow waitlist sign-ups (members get notified if a spot opens)
- **Cancellation:** Allow cancellation up to 2 hours before class (prevents empty spots from last-minute no-shows while giving members some flexibility)

**Class Calendar 2: "Yoga Flow"**
- **Name:** "Yoga Flow"
- **Description:** "A flowing vinyasa-style yoga class focused on breath, movement, and flexibility. Perfect for stress relief and recovery. Mats provided."
- **Duration:** 60 minutes
- **Maximum attendees:** 15 per class (smaller for personalized attention and mat spacing)
- **Recurring schedule:**
  - Tuesday: 7:00 AM, 6:00 PM
  - Thursday: 7:00 AM, 6:00 PM
- **Booking form:** Name, Email, Phone, "Yoga Experience" (Dropdown: Brand New / Some Experience / Regular Practitioner)
- **Waitlist:** Enable
- **Cancellation:** Allow up to 4 hours before class

**Class Calendar 3: "Pilates Core"**
- **Name:** "Pilates Core"
- **Description:** "Mat-based Pilates focusing on core strength, posture, and body awareness. Low impact but highly effective. Suitable for all levels including rehabilitation."
- **Duration:** 50 minutes
- **Maximum attendees:** 12 per class (smallest class -- Pilates requires more individual form correction)
- **Recurring schedule:**
  - Monday: 10:00 AM
  - Wednesday: 10:00 AM
  - Friday: 10:00 AM
  - Saturday: 9:00 AM
- **Booking form:** Name, Email, Phone, "Any physical limitations?" (Textarea)
- **Waitlist:** Enable
- **Cancellation:** Allow up to 4 hours before class

**After creating all 3 class calendars:**
1. Open each booking link in incognito and verify:
   - Only the correct days/times appear
   - The max capacity is displayed (or booking closes when full)
   - The custom fields appear on the form
2. Book a spot in each class to test
3. Book multiple spots in one class (use different test contacts) to verify the attendee count increments
4. Check the attendee list from the calendar view in GHL

---

## Part 5: Calendar Management (30 min)

### Hands-On Exercise 4.5: Manage Appointments

Navigate to the **Calendars** main view. You should now have 5 calendars: Personal Training, Nutrition Consultation, HIIT Class, Yoga Flow, and Pilates Core.

**View Modes:**
1. Switch between **Day**, **Week**, and **Month** views
2. In Week view, observe how all 5 calendars layer together -- this is how the front desk at Sunrise Wellness would see the full studio schedule
3. Filter by specific calendar to see only PT sessions, or only group classes

**Appointment Management:**
1. Click on one of your test PT appointments:
   - View the contact info and intake answers (fitness goals, experience level, injuries)
   - Change status to **Confirmed**
   - Add a note: "Member prefers morning sessions. Focus on lower body - knee modification needed."
2. Click on a group class booking:
   - View the attendee list
   - Note: class bookings show the total registered vs. capacity (e.g., "3/20 booked")

**Status Workflow (practice with your test appointments):**
- **Confirmed** - Member confirmed they're coming
- **Showed** - Member actually showed up (mark this after the session)
- **No-Show** - Member didn't come (triggers follow-up in workflows you'll build on Day 9)
- **Cancelled** - Member cancelled (frees the slot for someone else)

Mark your test appointments with different statuses to see how GHL tracks them.

**Book on Behalf of a Member:**
1. From the calendar view, click on an empty time slot
2. Select "Book Appointment"
3. Search for an existing contact from your Day 2 database
4. Complete the booking as if a member called the front desk: "I'd like to book a PT session for next Tuesday at 10 AM"
5. This is how the front desk staff at Sunrise Wellness would handle phone-in bookings

### Hands-On Exercise 4.6: Calendar Settings Deep Dive

Navigate to **Settings > Calendars** (or the calendar settings gear icon):

**Explore and configure:**

1. **Google Calendar Sync** (optional connection):
   - If you have a Google account: connect it for two-way sync
   - Trainer benefit: PT sessions booked in GHL automatically appear on the trainer's personal Google Calendar, preventing double-booking with personal appointments
   - If not connecting: understand that this is how trainers would see their schedule outside of GHL

2. **Outlook Calendar Sync** - Same concept, Microsoft ecosystem

3. **Timezone Settings**:
   - Verify timezone matches your Sunrise Wellness Studio location
   - Important: Members booking from different timezones see slots in THEIR timezone, but the appointment is at YOUR studio's local time
   - This matters if Sunrise Wellness runs virtual nutrition consultations for remote clients

4. **Overbooking Protection**:
   - Ensure "Prevent overbooking across calendars" is enabled
   - Scenario: A trainer has a PT session at 10 AM. They shouldn't also appear as teaching a class at 10 AM. Cross-calendar protection handles this.
   - Test: Try to book two appointments at the same time on different calendars and see if GHL blocks it

5. **Appointment Slot Intervals**:
   - Review how granular the booking slots are (every 15, 30, or 60 minutes)
   - For PT (60 min + 15 min buffer), slots should start every 75 minutes
   - For classes, slots are fixed by the recurring schedule

### Hands-On Exercise 4.7: User Calendar Links

**Understanding `{{user.calendar}}`:**

This merge field resolves to the specific assigned user's calendar booking link. For Sunrise Wellness, this is how you'd implement trainer-specific booking:

1. Find where `{{user.calendar}}` is available:
   - Open an email template or SMS template
   - Type `{{user.` and browse the available fields
   - Note the `{{user.calendar}}` option

2. **Sunrise Wellness use case:**
   - A new member books PT through the Round Robin calendar and gets assigned to Coach Mike
   - All future communication with that member includes `{{user.calendar}}` instead of the generic PT booking link
   - The member always books with Coach Mike from that point forward -- building the trainer-client relationship
   - This is critical for retention: members who bond with a specific trainer stay longer

3. **Test it:**
   - Assign one of your test contacts to yourself (you're the only user, but the concept applies)
   - Create a test message using `{{user.calendar}}`: "Ready for your next session? Book directly with your trainer: {{user.calendar}}"
   - Verify it resolves to YOUR calendar booking link
   - In production with multiple trainers, this would resolve to each trainer's unique link

4. **Design exercise:** How would you use `{{user.calendar}}` in a Sunrise Wellness workflow?
   - Day 3 template "PT Session Reminder" could include a reschedule link using `{{user.calendar}}`
   - Follow-up messages after a PT session: "Great workout today! Book your next session: {{user.calendar}}"
   - This keeps the member with the same trainer rather than going back into the Round Robin

---

## Part 6: API Lab - Calendar & Appointments

### Run the Calendars API Lab

```bash
cd scripts/
python day-04-calendars-api.py
```

The script covers:
1. List all calendars in your sub-account (you should see all 5 you created today)
2. Get available time slots for a specific calendar
3. Create an appointment via API
4. Update an appointment status (Confirmed, Showed, No-Show, Cancelled)
5. Delete/cancel an appointment

### API Exercises

1. **Daily schedule summary:** Write a script that checks tomorrow's appointments across ALL calendars and prints a morning briefing:
   ```
   === Sunrise Wellness - Tomorrow's Schedule ===
   PT Sessions: 3 booked
   - 7:00 AM: Alex M. (Weight Loss, Beginner)
   - 10:00 AM: Jordan T. (Muscle Building, Advanced)
   - 4:00 PM: Sam R. (General Fitness, Intermediate)
   
   Group Classes:
   - 6:00 AM HIIT: 14/20 spots filled
   - 10:00 AM Pilates: 8/12 spots filled
   - 5:30 PM HIIT: 19/20 spots filled (nearly full!)
   
   Nutrition: 2 consultations (Tue only)
   ```

2. **No-show tracker:** Build a function that finds all "No-Show" appointments from the past week and lists the contacts (input for a re-engagement workflow)

3. **Cross-API exercise (Day 3 + Day 4):** Write a script that creates a PT appointment via API and then sends a confirmation SMS/email to the contact using the messaging API from Day 3

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Clinic

**Situation:** BrightSmile Dental Clinic has 2 dentists, 1 hygienist, and 1 front desk staff. They need a calendar system that handles routine checkups, cosmetic consultations, hygienist cleanings, and same-day emergency slots. Design their calendar structure.

**Design and document the following (create what you can in GHL):**

1. **"General Checkup" (Basic Calendar)**
   - Duration: 30 minutes
   - Availability: Mon-Fri 8AM-5PM (lunch break 12-1PM)
   - Booking form: Name, Email, Phone, "Insurance provider" (Dropdown), "Reason for visit" (Dropdown: Routine Checkup / Toothache / Follow-Up / Other), "Last dental visit" (Dropdown: Less than 6 months / 6-12 months / Over a year / First visit)
   - Minimum scheduling notice: 24 hours
   - Buffer: 10 minutes (room turnover and sterilization)

2. **"Cosmetic Consultation" (Basic Calendar)**
   - Duration: 45 minutes (longer because of discussion and imaging)
   - Availability: Tue/Thu 9AM-3PM only (cosmetic days)
   - Booking form: Name, Email, Phone, "Procedure of interest" (Multi-select: Teeth Whitening / Veneers / Bonding / Invisalign / Smile Makeover), "Budget range" (Dropdown), "Have you had cosmetic dental work before?" (Yes/No)
   - Buffer: 15 minutes

3. **"Emergency Dental" (Basic Calendar)**
   - Duration: 30 minutes (initial assessment)
   - Availability: Mon-Fri 8AM-5PM -- **same-day only** (set minimum notice to 0, maximum advance booking to same day)
   - Booking form: Name, Email, Phone, "Describe the emergency" (Textarea -- required), "Pain level 1-10" (Dropdown)
   - No buffer (emergencies override normal scheduling)
   - Note: This calendar shows only TODAY's remaining slots

4. **"Hygienist Cleaning" (Round Robin -- if multiple hygienists)**
   - Duration: 60 minutes
   - Availability: Mon-Fri 8AM-4PM
   - With 1 hygienist, this effectively works like a Basic calendar. If BrightSmile hires a second hygienist, the Round Robin distributes cleanings evenly.
   - Booking form: Name, Email, Phone, "Insurance" (Dropdown), "Any dental anxiety concerns?" (Textarea)

5. **Reflect:** Dental scheduling has unique constraints that fitness doesn't:
   - Room availability (only 2 treatment rooms) limits concurrent appointments
   - Equipment sterilization time adds mandatory buffer
   - Emergency slots must be kept open but not wasted if unused
   - Insurance verification needs to happen BEFORE the appointment
   - How would you handle these constraints in GHL?

### Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency has 2 account managers and 3 specialists. They need calendars for sales calls (strategy calls with prospects), onboarding kickoffs for new clients, and monthly review calls with existing clients. Their scheduling needs are different from Sunrise Wellness because everything is virtual and business-hours only.

**Design and document the following (create what you can in GHL):**

1. **"Strategy Call" (Round Robin)**
   - Distributes among 2 account managers
   - Duration: 30 minutes
   - Availability: Mon-Fri 9AM-5PM (no weekends -- B2B hours)
   - Booking form: Name, Email, Company Name, "Company website" (Text), "Services interested in" (Multi-select: SEO / PPC / Social Media / Email Marketing / Web Design), "Monthly marketing budget" (Dropdown: Under $2K / $2K-$5K / $5K-$10K / $10K+), "What's your biggest marketing challenge?" (Textarea)
   - Buffer: 10 minutes (account manager needs time to review prospect's website before the call)
   - This is the agency's sales calendar -- the intake form doubles as lead qualification

2. **"Onboarding Kickoff" (Basic Calendar)**
   - Duration: 60 minutes
   - Availability: Mon-Fri 10AM-3PM (prime collaboration hours)
   - Booking form: Name, Email, "Services purchased" (pre-filled by account manager when booking on behalf of client), "Preferred communication channel" (Dropdown: Email / Slack / Phone), "Key stakeholders to include on calls" (Textarea)
   - This is booked BY the agency FOR the client (not self-service), typically after a contract is signed
   - Minimum notice: 48 hours (team needs prep time)

3. **"Monthly Review Call" (Round Robin)**
   - Distributes among 2 account managers (same client always sees the same manager via `{{user.calendar}}`)
   - Duration: 30 minutes
   - Availability: Mon-Fri 9AM-5PM
   - Booking form simplified: Name, Email, "Topics to discuss" (Textarea -- so the account manager can prepare the report)
   - Recurring: These would ideally be set as recurring monthly appointments

4. **Reflect:** How does agency calendar design differ from fitness studio design?
   - No "class booking" type needed -- all meetings are 1-on-1 or small group
   - `{{user.calendar}}` is critical -- clients must always meet with THEIR account manager
   - Lead qualification happens through the booking form (budget, services, challenges)
   - Virtual meetings mean no physical space constraints, but timezone management becomes important
   - How would you handle a client in a different timezone?

---

## Day 4 Recap Questions

1. What are the 3 main calendar types in GHL? Map each to a Sunrise Wellness service and explain why that type fits.
2. How does Round Robin distribution work for Personal Training? What happens when a trainer goes on vacation -- how would you adjust?
3. What is buffer time, and why does Sunrise Wellness need 15 minutes between PT sessions? What would happen without it?
4. Explain the `{{user.calendar}}` merge field. Why is it important that a member who started with Coach Mike continues booking with Coach Mike?
5. A Premium member says "I can't find any available Pilates slots this week." Walk through the troubleshooting steps you'd take in the calendar settings.
6. How do Class Booking calendars differ from Round Robin? Could you use Round Robin for group fitness classes? Why or why not?
7. How do you handle no-shows in GHL calendars? What status options are available, and how would Sunrise Wellness use each one?

---

## Next Day Preview

**Day 5: Opportunities & Pipelines** - You'll design the Sunrise Wellness sales pipeline to track member journeys from "New Lead" through "Free Trial" to "Active Member." Every contact who books a PT session or inquires about membership moves through this pipeline. You'll create stages, manage opportunities, and see how the calendar bookings from today feed into the sales process.

Make sure you have:
- All 5 calendars created and tested (PT, Nutrition, HIIT, Yoga, Pilates)
- At least 3-4 test appointments booked across different calendars
- Your Day 3 templates saved (they'll connect to calendars via workflows on Day 9)
