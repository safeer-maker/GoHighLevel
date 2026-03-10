# Day 1: Dashboard & Settings Configuration

**Time Required:** 2-3 hours
**Certification Alignment:** Sub-Account Dashboard, My Profile notifications, Custom Values, Audit Logs, Employee Management

---

## Learning Objectives

By the end of today, you will be able to:
1. Customize the GHL dashboard for different business roles
2. Configure all essential sub-account settings (business profile, branding, timezone)
3. Set up Custom Values and understand how they cascade across the platform
4. Navigate and interpret Sub-Account Audit Logs

---

## Part 1: Dashboard Overview (30 min)

### Theory Recap

The GHL sub-account dashboard is your command center. It displays key performance indicators (KPIs) including:
- **Opportunities** - Pipeline value and stage distribution
- **Conversations** - Unread messages, response times
- **Appointments** - Upcoming, completed, no-shows
- **Tasks** - Pending tasks by team member
- **Google Analytics** - If connected, traffic and conversion data

The dashboard is customizable per user - each team member can see what matters to them.

### Hands-On Exercise 1.1: Explore the Default Dashboard

1. Log into your GHL sub-account
2. Navigate to **Dashboard** (left sidebar)
3. Document what widgets/sections you see by default
4. Note the date range selector at the top - change it to "Last 30 Days", "This Month", "Last 7 Days"
5. Click into each widget to understand what data it shows

**What to observe:**
- Which metrics are shown?
- Can you click on numbers to drill down?
- What happens when you change the date range?

### Hands-On Exercise 1.2: Customize Dashboard Views

1. Look for the dashboard customization options (gear icon or "Customize" button)
2. Create a **"Sales Manager" view**: Focus on Opportunities, Appointments, and Conversion metrics
3. Create an **"Operations" view**: Focus on Tasks, Conversations, and Team performance
4. Switch between views to understand how different roles need different data

**Document your findings:** Which widgets did you include in each view and why?

---

## Part 2: Business Profile & Settings (45 min)

### Theory Recap

Settings is where you configure the foundation of your sub-account. Everything here affects how GHL operates for this business. Key areas:
- **Business Profile** - Company info, branding, timezone
- **My Staff** - Team members and permissions
- **Custom Values** - Dynamic placeholders used across the platform
- **General Settings** - Default behaviors

### Hands-On Exercise 1.3: Complete Business Profile Setup

Navigate to **Settings > Business Profile** and configure:

1. **Business Name:** Enter a business name (use a fictional one for practice, e.g., "Sunrise Dental Clinic")
2. **Address:** Full business address
3. **Phone Number:** Business phone
4. **Website:** Business website URL
5. **Logo:** Upload a logo (you can use any placeholder image)
6. **Timezone:** Set correct timezone - this affects ALL scheduling in the system
7. **Business Category:** Select appropriate category

**Critical Note:** Timezone affects calendars, workflows, and reporting. Always set this first.

### Hands-On Exercise 1.4: Configure User Notification Preferences

Navigate to **Settings > My Profile**:

1. Review all notification options:
   - Email notifications (new lead, appointment booked, etc.)
   - SMS/text notifications
   - Desktop/browser notifications
2. Enable notifications for:
   - New conversation messages
   - Appointment bookings
   - Form submissions
3. Test each notification type by triggering the associated event

**Why this matters:** In real client setups, notification configuration is the #1 thing that determines whether users actually engage with GHL daily.

### Hands-On Exercise 1.5: Set Up Custom Values

Navigate to **Settings > Custom Values**:

Custom Values are global variables you can use anywhere in GHL (emails, SMS, funnels, workflows). They act as placeholders that auto-fill with the stored value.

1. Create or verify these Custom Values exist:
   - `{{business.name}}` - Your business name
   - `{{business.phone}}` - Main phone number
   - `{{business.email}}` - Main email address
   - `{{business.address}}` - Full address
   - `{{business.website}}` - Website URL
   - `{{business.hours}}` - Business hours text (e.g., "Mon-Fri 9AM-5PM")

2. Create custom values for:
   - `{{offer.free_consultation}}` - "Free 30-Minute Consultation"
   - `{{offer.discount}}` - "20% Off Your First Visit"
   - `{{booking.link}}` - Your calendar booking URL (you'll set this up on Day 4)

3. Test a Custom Value:
   - Go to **Conversations**
   - Start composing a message
   - Type `{{` and see if your custom values appear in the dropdown
   - Verify they resolve to the correct values

**Pro Tip:** Custom Values save massive time. Instead of updating your phone number in 50 templates, you update one Custom Value and it propagates everywhere.

---

## Part 3: Audit Logs & Security (30 min)

### Theory Recap

Audit Logs track every action taken in your sub-account - who did what, when. This is critical for:
- Security monitoring
- Troubleshooting ("who deleted that contact?")
- Compliance (HIPAA, SOC2)
- Team accountability

### Hands-On Exercise 1.6: Explore Sub-Account Audit Logs

Navigate to **Settings > Audit Logs** (or search for "Audit Logs"):

1. Review recent activity logs
2. Filter by:
   - Date range
   - User/team member
   - Action type (create, update, delete)
   - Entity type (contact, opportunity, workflow, etc.)
3. Find the actions YOU performed today (business profile updates, custom value creation)
4. Export audit logs if the option is available

**Document:** What types of actions are logged? What details are captured for each log entry?

### Hands-On Exercise 1.7: Add Employees/Staff

Navigate to **Settings > My Staff** (or Team Management):

1. Understand the difference between Agency users and Sub-Account users
2. Create a test employee (use a secondary email if available):
   - Assign the "User" role
   - Set appropriate permissions
3. Review available permission levels:
   - What can each role access?
   - Can you create custom roles?
4. Understand "Only Assigned Data" - when enabled, users only see contacts/opportunities assigned to them

---

## Part 4: Templates & Quick Setup (15 min)

### Hands-On Exercise 1.8: Enable/Disable Templates

Navigate to **Settings > Templates** (or related section):

1. Review what templates are available (email, SMS, workflow)
2. Understand how to enable/disable templates for sub-account users
3. Note which templates come pre-built and which you need to create

---

## Case Scenarios

### Case Scenario 1: New Dental Clinic Onboarding

**Situation:** You've been hired to set up GHL for "Bright Smiles Dental," a dental clinic with 2 dentists, 1 hygienist, and 1 front desk receptionist.

**Your Task:**
1. Configure the Business Profile completely for a dental clinic
2. Set up Custom Values for:
   - Clinic name, address, phone
   - Hours: "Mon-Thu 8AM-5PM, Fri 8AM-2PM"
   - Emergency number
   - New patient offer: "Free Dental Exam & X-Rays for New Patients"
3. **Plan** the notification preferences for each role (document what you'd configure):
   - Front desk: ALL notifications (calls, messages, appointments)
   - Dentists: appointment notifications only
   - Hygienist: appointment reminders only
4. Configure YOUR notification preferences as if you were the front desk (full notifications)
5. Document what you configured and why

**Deliverable:** Screenshot or document your complete settings configuration.

### Case Scenario 2: Real Estate Team User Roles (Planning Exercise)

**Situation:** A real estate team "Metro Homes Realty" has:
- 1 Team Lead (needs full access + reporting)
- 3 Agents (need conversations, contacts, and their own pipelines only)
- 1 Admin Assistant (needs to manage calendars and send messages, but not see financial data)

**Your Task (document-based - no extra accounts needed):**
1. Navigate to Settings > My Staff and explore the available permission options
2. **Plan** the permission structure for each role - document what you WOULD enable/disable for each
3. Create a permission matrix table showing each role vs. each GHL feature (access level: Full / View Only / No Access)
4. Explore the "Only Assigned Data" toggle and document what it does
5. If you have a secondary email, optionally create ONE test user to see how permissions look from their side

**Note:** You don't need to create all 5 users. The learning goal is understanding GHL's permission system and designing role-based access.

**Deliverable:** A permission matrix table showing each role and their access levels for each GHL feature.

---

## Day 1 Recap Questions

Test your understanding:

1. Where do you set the timezone for a sub-account, and why is it the first thing you should configure?
2. What are Custom Values and how do they differ from Contact Custom Fields?
3. If a contact's phone number changes, do you update a Custom Value or a Custom Field? Why?
4. What information can you find in Sub-Account Audit Logs?
5. Explain the "Only Assigned Data" permission option and when you'd use it.
6. A client says "my team isn't getting notified when leads come in." Where do you look first?

---

## Next Day Preview

**Day 2: Contacts & CRM Foundations** - We'll dive into the heart of GHL: the contact database. You'll learn to import contacts, create custom fields, build smart lists, and start working with the GHL API to manage contacts programmatically.

Make sure you have:
- A sample CSV file with at least 20 fake contacts (name, email, phone, company) ready for import
- Your Python environment set up (see `scripts/requirements.txt`)
