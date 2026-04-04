# Day 1: Dashboard & Settings Configuration

**Time Required:** 2-3 hours
**Certification Alignment:** Sub-Account Dashboard, My Profile notifications, Custom Values, Audit Logs, Employee Management

---

## Today's Mission

Today you'll transform a blank GHL sub-account into the home base for **Sunrise Wellness Studio** - a fitness and wellness business offering personal training, group classes, nutrition coaching, and memberships. By the end of today, your sub-account will have a complete business profile, custom values that auto-fill across all future templates and funnels, and a dashboard configured to track the metrics that matter for a wellness business. Everything you set up today becomes the foundation for the next 9 days.

---

## Learning Objectives

By the end of today, you will be able to:
1. Customize the GHL dashboard for different business roles
2. Configure all essential sub-account settings for Sunrise Wellness Studio
3. Set up Custom Values that will be reused across the entire course
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
2. Think about Sunrise Wellness Studio - the owner needs to see:
   - New member sign-ups (contacts created)
   - Upcoming training sessions and classes (appointments)
   - Membership revenue (pipeline/opportunities)
   - Unread messages from members (conversations)
3. Customize your dashboard to highlight these wellness-business KPIs
4. Note which widgets you'd hide for a front desk view vs an owner view:
   - **Owner view:** Revenue, new leads, appointments, conversations, pipeline
   - **Front desk view:** Today's appointments, unread conversations, tasks
   - **Trainer view:** Only their own upcoming appointments

**Document your findings:** Which widgets did you include and why? How would different staff at a wellness studio need different dashboards?

---

## Part 2: Business Profile - Sunrise Wellness Studio (45 min)

### Theory Recap

Settings is where you configure the foundation of your sub-account. Everything here affects how GHL operates for this business. Key areas:
- **Business Profile** - Company info, branding, timezone
- **My Staff** - Team members and permissions
- **Custom Values** - Dynamic placeholders used across the platform
- **General Settings** - Default behaviors

### Hands-On Exercise 1.3: Complete Business Profile Setup

Navigate to **Settings > Business Profile** and configure Sunrise Wellness Studio:

1. **Business Name:** Sunrise Wellness Studio
2. **Address:** 123 Wellness Way, Springfield (use your real timezone city for accurate scheduling)
3. **Phone:** Your test number or a placeholder (if you don't have a GHL phone number yet, that's fine - enter a placeholder and note it for later)
4. **Website:** Use your GHL funnel URL (you'll create this on Day 8 - leave blank or use a placeholder for now)
5. **Logo:** Upload a wellness/fitness logo (find a free one at sites like Canva, Unsplash, or Flaticon)
6. **Timezone:** Your actual timezone - this affects ALL scheduling in the system
7. **Business Category:** Health & Wellness / Fitness

**Critical Note:** Timezone is the first thing to set. If you configure it wrong, every calendar slot, workflow trigger, and appointment reminder will fire at the wrong time. For Sunrise Wellness Studio, think about this: classes at 6AM need to trigger reminders at 5:30AM in the RIGHT timezone.

### Hands-On Exercise 1.4: Configure Notification Preferences

Navigate to **Settings > My Profile**:

1. Review all notification options:
   - Email notifications (new lead, appointment booked, etc.)
   - SMS/text notifications (if phone number is configured)
   - Desktop/browser notifications
2. Enable notifications for:
   - New conversation messages (member inquiries about classes, pricing)
   - Appointment bookings (training sessions, consultations)
   - Form submissions (new leads signing up for the free trial)
3. Test each notification type by triggering the associated event

**Sunrise Wellness Staff Notification Plan** (document this for future reference):

| Role | Conversations | Appointments | Forms | Pipeline Changes |
|------|--------------|--------------|-------|-----------------|
| Owner (You) | All | All | All | All |
| Lead Trainer (Alex) | Assigned only | Own bookings | No | No |
| Trainer (Jordan) | Assigned only | Own bookings | No | No |
| Nutritionist (Sam) | Assigned only | Own bookings | Intake forms only | No |
| Front Desk (Morgan) | All | All | All | No |

**Note:** Since you're the only real user on this sub-account, configure YOUR notifications as the owner (everything on). Document what you WOULD set for each staff role - you'll reference this when we explore permissions later today.

### Hands-On Exercise 1.5: Set Up Custom Values for Sunrise Wellness

Navigate to **Settings > Custom Values**:

Custom Values are global variables you can use anywhere in GHL (emails, SMS, funnels, workflows). They act as placeholders that auto-fill with the stored value. These values will be reused across ALL templates, emails, funnels, and workflows for the rest of this course.

Create these Custom Values:

**Standard Business Values:**

| Custom Value | Value |
|-------------|-------|
| `{{business.name}}` | Sunrise Wellness Studio |
| `{{business.phone}}` | (your number or placeholder) |
| `{{business.email}}` | hello@sunrisewellness.com |
| `{{business.address}}` | 123 Wellness Way, Springfield |
| `{{business.website}}` | (your GHL funnel URL - update on Day 8) |
| `{{business.hours}}` | Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM |

**Wellness-Specific Offer Values:**

| Custom Value | Value |
|-------------|-------|
| `{{offer.free_trial}}` | Free 7-Day Trial Pass |
| `{{offer.discount}}` | 20% Off Your First Month |
| `{{offer.referral}}` | Refer a Friend, Get a Free PT Session |

**Test your Custom Values:**
1. Go to **Conversations**
2. Start composing a message (you can compose to yourself or a test contact)
3. Type `{{` and verify your custom values appear in the dropdown
4. Select one and confirm it resolves to the correct value

**Pro Tip:** Custom Values save massive time. Instead of updating your phone number in 50 templates, you update one Custom Value and it propagates everywhere. For Sunrise Wellness Studio, when you build email templates on Day 6 and funnels on Day 8, every `{{business.name}}` will automatically say "Sunrise Wellness Studio."

---

## Part 3: Audit Logs & Staff Planning (30 min)

### Theory Recap

Audit Logs track every action taken in your sub-account - who did what, when. This is critical for:
- Security monitoring
- Troubleshooting ("who deleted that contact?")
- Compliance (HIPAA considerations for wellness/health businesses)
- Team accountability

### Hands-On Exercise 1.6: Explore Sub-Account Audit Logs

Navigate to **Settings > Audit Logs** (or search for "Audit Logs"):

1. Review recent activity logs
2. Filter by:
   - Date range
   - Action type (create, update, delete)
   - Entity type (contact, opportunity, workflow, etc.)
3. Find the actions YOU performed today:
   - Business profile creation/update
   - Custom value creation
   - Notification preference changes
4. Export audit logs if the option is available

**Document:** What types of actions are logged? What details are captured for each log entry? For a wellness studio handling member health data, which audit log entries would be most important to monitor?

### Hands-On Exercise 1.7: Staff Planning (Single-User Adapted)

Navigate to **Settings > My Staff**:

Since you have a single sub-account without extra team members, this exercise focuses on understanding the permission system and planning roles for Sunrise Wellness Studio.

1. Explore the available permission options and roles in the My Staff interface
2. **Plan the Sunrise Wellness staff structure** (document in a text file or on paper):

| Role | Person | Permissions Needed |
|------|--------|--------------------|
| Owner/Admin | You (active) | Full access to everything |
| Lead Trainer | Alex | Appointments, assigned contacts, conversations, no billing |
| Trainer | Jordan | Own appointments only, no financial data, no settings |
| Nutritionist | Sam | Appointments, assigned contacts, custom intake forms, no billing |
| Front Desk | Morgan | Conversations, all appointments, contacts, no billing settings |

3. If you have a secondary email, create ONE test user to see how permissions look from their side
4. Explore the **"Only Assigned Data"** toggle and document what it does:
   - With this ON for a trainer, they'd only see clients booked with them
   - With this OFF, they'd see all studio members (not ideal for privacy)
   - For Sunrise Wellness: trainers and the nutritionist should have "Only Assigned Data" enabled; front desk should have it disabled so they can help any member

**Note:** You don't need to create all 5 users. The learning goal is understanding GHL's permission system so you can design role-based access for any business.

---

## Part 4: Templates Quick Setup (15 min)

### Hands-On Exercise 1.8: Review Available Templates

Navigate to **Settings > Templates** (or related section):

1. Review what templates are available (email, SMS, workflow)
2. Note which pre-built templates could apply to a wellness business:
   - Appointment reminders (perfect for training sessions)
   - Welcome sequences (new member onboarding)
   - Review requests (post-session feedback)
3. Understand how to enable/disable templates for sub-account users
4. Don't configure templates yet - you'll build custom ones for Sunrise Wellness on Day 6 (Email Marketing) and Day 7 (Workflows)

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Clinic Setup

**Situation:** You're now thinking through how you'd configure GHL for **BrightSmile Dental Clinic** - a dental practice with 2 dentists, 1 hygienist, and 1 front desk receptionist. You won't reconfigure your sub-account (it stays as Sunrise Wellness), but you'll document a complete setup plan.

**Your Task:**

**1. Document the complete Business Profile:**
- Business Name: BrightSmile Dental Clinic
- Address: 456 Smile Avenue, Springfield
- Hours: Mon-Thu 8AM-5PM, Fri 8AM-2PM, Sat-Sun Closed
- Category: Healthcare / Dental
- Phone: Main line + separate emergency after-hours number

**2. Design Custom Values for a dental practice:**

| Custom Value | Value |
|-------------|-------|
| `{{business.name}}` | BrightSmile Dental Clinic |
| `{{business.phone}}` | (555) 234-5678 |
| `{{business.email}}` | smile@brightsmile.com |
| `{{business.address}}` | 456 Smile Avenue, Springfield |
| `{{business.hours}}` | Mon-Thu 8AM-5PM, Fri 8AM-2PM |
| `{{emergency.phone}}` | (555) 234-9999 |
| `{{offer.new_patient}}` | Free Dental Exam & X-Rays for New Patients |
| `{{offer.whitening}}` | 50% Off Professional Whitening - Limited Time |
| `{{offer.referral}}` | Refer a Friend, Both Get $50 Off Next Visit |

**3. Plan the staff permission matrix:**

| Role | Contacts | Conversations | Appointments | Pipeline | Payments | Settings |
|------|----------|--------------|--------------|----------|----------|----------|
| Dentist | Assigned | Assigned | Own schedule | View only | No | No |
| Hygienist | Assigned | No | Own schedule | No | No | No |
| Front Desk | All | All | All schedules | View only | View only | No |
| Admin/Owner | All | All | All | Full | Full | Full |

**4. Notification plan:**
- Configure YOUR sub-account notifications as if you were the front desk receptionist: turn on ALL notifications (calls, messages, appointments, form submissions) since they're the first point of contact for every patient
- Document: Why would a dentist only want appointment notifications? (They're busy with procedures and don't need to see every new lead message)

**5. Audit Log considerations:**
- What actions would be especially important to track at a dental clinic? (Think HIPAA: contact record access, data exports, deleted records, permission changes)

### Case Scenario 2: Elevate Digital Agency Setup

**Situation:** You're planning how you'd configure GHL for **Elevate Digital Agency** - a marketing agency with 2 account managers, 3 specialists, and 1 project manager, serving small-to-medium businesses.

**Your Task:**

**1. Document the Business Profile for an agency:**
- Business Name: Elevate Digital Agency
- Address: 789 Marketing Blvd, Suite 300, Springfield
- Hours: Mon-Fri 9AM-6PM
- Category: Professional Services / Marketing
- Website: elevateagency.com

**2. Design Custom Values for an agency:**

| Custom Value | Value |
|-------------|-------|
| `{{business.name}}` | Elevate Digital Agency |
| `{{business.phone}}` | (555) 345-6789 |
| `{{business.email}}` | hello@elevateagency.com |
| `{{business.address}}` | 789 Marketing Blvd, Suite 300, Springfield |
| `{{business.hours}}` | Mon-Fri 9AM-6PM |
| `{{offer.audit}}` | Free Website & SEO Audit |
| `{{offer.consultation}}` | Free 30-Minute Strategy Session |
| `{{onboarding.link}}` | (client onboarding survey URL - placeholder) |
| `{{offer.retainer_discount}}` | 15% Off First 3 Months for Annual Contracts |

**3. Plan the staff permission matrix:**

| Role | Contacts | Conversations | Appointments | Pipeline | Reporting | Settings |
|------|----------|--------------|--------------|----------|-----------|----------|
| Account Manager | Assigned clients | Assigned | Own | Assigned | Assigned clients | No |
| Specialist | Assigned tasks only | No | No | No | No | No |
| Project Manager | All | All | All | All | All | No |
| Agency Owner | All | All | All | All | All | Full |

**4. Compare agency vs local business setup:**
Document these key differences:
- **"Only Assigned Data"** is critical for agencies where account managers should only see their own clients, not each other's. At Sunrise Wellness, the front desk needs to see all members.
- **Pipeline importance:** An agency lives in pipelines (prospect > proposal > onboarding > active client > renewal). A wellness studio uses pipelines less (mainly for new lead > trial > member conversion).
- **Custom Values focus:** Agency custom values lean toward offers and onboarding. Wellness studio values lean toward hours, location, and membership offers.
- **Conversations volume:** A wellness studio gets more direct member messages. An agency has fewer but more complex client threads.

---

## Day 1 Recap Questions

Test your understanding:

1. Where do you set the timezone for Sunrise Wellness Studio, and why is it the first thing to configure? (Hint: think about 6AM class reminders)
2. What Custom Values did you create for Sunrise Wellness, and where will they appear throughout the rest of this course?
3. What's the difference between Custom Values and Contact Custom Fields? (You'll create Custom Fields tomorrow)
4. A Sunrise Wellness member says "your phone number changed on your website." Do you update a Custom Value or a Custom Field? Why?
5. Explain the "Only Assigned Data" permission and how you'd use it for trainers at the studio vs the front desk.
6. A trainer at Sunrise Wellness says "I'm not getting notifications when clients book sessions." Where do you look first?

---

## Next Day Preview

**Day 2: Contacts & CRM** - You'll build the complete member database for Sunrise Wellness Studio. You'll create custom fields for membership type, fitness goals, trainer assignment, experience level, and more. Then you'll import a batch of sample members via CSV and build Smart Lists for targeted marketing: "Active Premium Members," "Expiring This Month," "Morning Exercisers," and others.

Make sure you have:
- A sample CSV with 20+ fake wellness studio members ready (or you'll create one during the lesson)
- Python environment set up if you want to try the API lab (`scripts/requirements.txt`)
