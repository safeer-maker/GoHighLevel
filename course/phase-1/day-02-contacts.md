# Day 2: Contacts & CRM Foundations

**Time Required:** 3-4 hours
**Certification Alignment:** Importing Contacts (3-part), Smart Lists, Custom Fields/Folders, Bulk Actions, Companies, Tasks, Bulk Restore
**API Lab:** Yes - `scripts/day-02-contacts-api.py`

---

## Today's Mission

Yesterday you set up Sunrise Wellness Studio's business profile, custom values, and dashboard. Today you'll build the **member database** - the heart of everything that follows. You'll design a custom field structure that captures what matters for a fitness and wellness business (membership tiers, fitness goals, preferred training times), import a batch of sample members, and create Smart Lists that segment your members for targeted marketing and operations. Every contact, workflow, and campaign you build on Days 3-10 will rely on the fields and lists you create today.

---

## Learning Objectives

By the end of today, you will be able to:
1. Design and implement a custom field structure tailored to a wellness business
2. Import contacts via CSV with proper field mapping and duplicate handling
3. Build Smart Lists for advanced member segmentation
4. Use the GHL API to programmatically manage contacts

---

## Part 1: Custom Fields & Custom Folders (45 min)

### Theory Recap

Custom Fields extend the default contact record. GHL provides standard fields (name, email, phone) but every business needs additional data points. Custom Fields can be:
- **Text** - Free text input
- **Number** - Numeric values
- **Date** - Date picker
- **Dropdown** - Single select from predefined options
- **Multi-Select** - Multiple selections from options
- **Checkbox** - True/false
- **File Upload** - Attachments
- **Textarea** - Long text

Custom Folders organize your custom fields into logical groups so the contact record stays clean and navigable.

### Hands-On Exercise 2.1: Design the Sunrise Wellness Custom Field Structure

Navigate to **Settings > Custom Fields** (or Contacts > Custom Fields):

You're building the data model for Sunrise Wellness Studio. Every member, lead, and prospect will have these fields available on their contact record.

**Folder: "Membership Info"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Membership Type | Dropdown | Free Trial, Basic ($79/mo), Premium ($149/mo), VIP ($249/mo) |
| Join Date | Date | When they started their membership |
| Expiry Date | Date | Membership end date (critical for renewal campaigns) |
| Monthly Rate | Number | Dollar amount (79, 149, 249, or custom) |
| Membership Status | Dropdown | Active, Paused, Cancelled, Expired, Trial |
| Payment Method | Dropdown | Credit Card, Bank Transfer, Cash, Pending |

**Folder: "Fitness Profile"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Fitness Goals | Multi-Select | Weight Loss, Muscle Gain, Flexibility, Endurance, General Health, Stress Relief |
| Experience Level | Dropdown | Beginner, Intermediate, Advanced |
| Preferred Time | Dropdown | Early Morning (6-8AM), Morning (8-10AM), Midday (10AM-2PM), Afternoon (2-5PM), Evening (5-9PM) |
| Preferred Classes | Multi-Select | HIIT, Yoga, Pilates, Strength Training, Spin |
| Assigned Trainer | Dropdown | Alex (Lead Trainer), Jordan (Trainer), Unassigned |
| Nutrition Coaching | Checkbox | Enrolled in nutrition program |

**Folder: "Lead Info"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Lead Source | Dropdown | Website, Facebook, Instagram, Google, Referral, Walk-in, Flyer |
| Referred By | Text | Name of referring member (for referral tracking) |
| Budget Range | Dropdown | Under $80/mo, $80-150/mo, $150-250/mo, $250+/mo |
| Interest Level | Dropdown | Just Browsing, Considering, Ready to Join |

**Folder: "Health & Safety"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Emergency Contact | Text | Name and phone number |
| Medical Conditions | Textarea | Any relevant conditions or injuries |
| Waiver Signed | Checkbox | Liability waiver completed |

**Steps:**
1. Create each Custom Folder first (Membership Info, Fitness Profile, Lead Info, Health & Safety)
2. Then create each Custom Field inside the appropriate folder
3. Note the **"Field Key"** generated for each field - you'll need these for API access on the API lab and on future days
4. Pay attention to the order of dropdown options - this is how they'll appear in forms

### Hands-On Exercise 2.2: Test Custom Fields on a Contact

1. Go to **Contacts**
2. Click **+ Add Contact** to create a test member
3. Fill in standard fields:
   - First Name: **Maria**
   - Last Name: **Chen**
   - Email: **maria.chen@example.com**
   - Phone: **+15551234001**
4. Scroll down to find your custom field folders and fill in:
   - Membership Type: **Premium ($149/mo)**
   - Join Date: **(today's date)**
   - Membership Status: **Active**
   - Fitness Goals: **Weight Loss, Flexibility**
   - Experience Level: **Intermediate**
   - Preferred Time: **Morning (8-10AM)**
   - Preferred Classes: **Yoga, Pilates**
   - Assigned Trainer: **Alex (Lead Trainer)**
   - Lead Source: **Instagram**
   - Waiver Signed: **Checked**
5. Save and reopen the contact to verify all data persisted correctly
6. Check that multi-select fields (Fitness Goals, Preferred Classes) saved both values

---

## Part 2: Importing Contacts (60 min)

### Theory Recap (Cert: 3-Part Import Process)

GHL's import process has 3 critical steps:
1. **Prepare your CSV** - Column headers must match GHL fields or be mappable
2. **Check for duplicates** - GHL can match by email, phone, or both
3. **Map and import** - Map CSV columns to GHL fields, review, and execute

### Hands-On Exercise 2.3: Prepare a Sunrise Wellness Member CSV

Create a CSV file (`sunrise-wellness-members.csv`) with 25+ contacts representing a mix of Sunrise Wellness Studio members and leads. Include these columns:

```csv
First Name,Last Name,Email,Phone,Membership Type,Join Date,Membership Status,Fitness Goals,Experience Level,Preferred Time,Preferred Classes,Assigned Trainer,Lead Source,Monthly Rate
Maria,Chen,maria.chen@example.com,+15551234001,Premium ($149/mo),2025-01-15,Active,"Weight Loss,Flexibility",Intermediate,Morning (8-10AM),"Yoga,Pilates",Alex (Lead Trainer),Instagram,149
David,Park,david.park@example.com,+15551234002,VIP ($249/mo),2024-06-01,Active,"Muscle Gain,Endurance",Advanced,Early Morning (6-8AM),"HIIT,Strength Training",Alex (Lead Trainer),Referral,249
Emma,Rodriguez,emma.r@example.com,+15551234003,Basic ($79/mo),2025-03-01,Active,General Health,Beginner,Evening (5-9PM),Yoga,Jordan (Trainer),Website,79
James,Wilson,james.w@example.com,+15551234004,Free Trial,,Trial,"Weight Loss,Muscle Gain",Beginner,Afternoon (2-5PM),,Unassigned,Facebook,0
Aisha,Patel,aisha.p@example.com,+15551234005,Premium ($149/mo),2024-11-20,Active,"Stress Relief,Flexibility",Intermediate,Midday (10AM-2PM),"Yoga,Pilates",Jordan (Trainer),Google,149
Tom,Baker,tom.baker@example.com,+15551234006,Basic ($79/mo),2025-02-10,Active,Weight Loss,Beginner,Morning (8-10AM),HIIT,Unassigned,Walk-in,79
Lisa,Nguyen,lisa.n@example.com,+15551234007,VIP ($249/mo),2024-03-15,Active,"Muscle Gain,Flexibility,Endurance",Advanced,Early Morning (6-8AM),"HIIT,Strength Training,Yoga",Alex (Lead Trainer),Referral,249
Carlos,Rivera,carlos.r@example.com,+15551234008,Premium ($149/mo),2025-01-05,Paused,Weight Loss,Intermediate,Evening (5-9PM),HIIT,Jordan (Trainer),Instagram,149
Priya,Sharma,priya.s@example.com,+15551234009,Basic ($79/mo),2024-09-01,Active,General Health,Beginner,Morning (8-10AM),Pilates,Unassigned,Flyer,79
Marcus,Thompson,marcus.t@example.com,+15551234010,,,,"Weight Loss,Endurance",Beginner,Evening (5-9PM),,Unassigned,Website,
```

**Create at least 25 rows** with these distribution guidelines:
- 3-4 VIP members, 6-8 Premium, 8-10 Basic, 3-4 Free Trial, 2-3 leads (no membership)
- Mix of all experience levels and preferred times
- Some with Assigned Trainer = "Unassigned" (for a Smart List later)
- A few with Membership Status = "Paused" or "Expired"
- Varied Lead Sources across all options

**Tips for CSV preparation:**
- Phone numbers should include country code (+1 for US)
- Multi-select values are comma-separated within quotes: `"Weight Loss,Muscle Gain"`
- Date format should match your GHL settings (YYYY-MM-DD recommended)
- Leave cells empty for missing data (leads without a membership), don't put "N/A"

### Hands-On Exercise 2.4: Import Members with Duplicate Handling

Navigate to **Contacts > Import** (or the import button):

**Step 1:** Upload your `sunrise-wellness-members.csv` file

**Step 2:** Configure duplicate handling:
- Choose duplicate check method: **Email** (recommended for first import)
- Select **"Update existing if duplicate found"** (this handles the Maria Chen contact you created manually in Exercise 2.2)

**Step 3:** Map CSV columns to GHL fields:
- Map standard fields: First Name, Last Name, Email, Phone
- Map custom fields: Membership Type, Join Date, Membership Status, Fitness Goals, Experience Level, Preferred Time, Preferred Classes, Assigned Trainer, Lead Source, Monthly Rate
- Set a default tag for this import batch: **"sunrise-import-day2"**

**Step 4:** Review the mapping summary and start the import

**After import - verify everything:**
1. Go to the Contacts list and confirm your contacts appear
2. Open **Maria Chen** - verify the import updated (not duplicated) her record
3. Open 3-4 other contacts and verify:
   - All standard fields mapped correctly
   - Custom fields populated in the right folders
   - Multi-select fields (Fitness Goals, Preferred Classes) show multiple values
   - The "sunrise-import-day2" tag was applied to all imported contacts
4. Check any contacts with empty membership data (leads) - confirm empty fields stayed empty

### Hands-On Exercise 2.5: Handle Duplicate Imports

Test GHL's duplicate handling to understand how it works:

1. Modify your CSV - change the phone number for 3 existing members
2. Re-import the modified CSV with duplicate check set to **Email**
3. Choose **"Update existing"**
4. After import, verify:
   - Did it create new contacts or update existing ones?
   - Did ONLY the phone numbers change, or did other fields get overwritten?
   - Check the contact count - it should be the same as before, not doubled
5. Check **Audit Logs** (Settings > Audit Logs) to see the import actions logged

---

## Part 3: Smart Lists & Segmentation (45 min)

### Theory Recap

Smart Lists are dynamic, filter-based views of your contacts. Unlike static tags, Smart Lists automatically include/exclude contacts as their data changes. When a member upgrades from Basic to Premium, they automatically move from the "Basic Members" list to the "Premium Members" list without any manual work.

Smart Lists are the foundation of targeted marketing and personalized automation - you'll use them on Day 6 (Email Marketing) and Day 7 (Workflows).

### Hands-On Exercise 2.6: Build Sunrise Wellness Smart Lists

Navigate to **Contacts** and look for the Smart List feature (usually a filter/list icon near the top of the contacts view):

**Smart List 1: "Active Premium Members"**
- Filter: Membership Type = Premium ($149/mo)
- AND Membership Status = Active
- **Purpose:** Target for VIP upgrade offers and exclusive class invites

**Smart List 2: "Expiring This Month"**
- Filter: Membership Status = Active
- AND Expiry Date = within next 30 days
- **Purpose:** Trigger renewal campaigns and retention outreach

**Smart List 3: "Morning Exercisers"**
- Filter: Preferred Time = Early Morning (6-8AM) OR Morning (8-10AM)
- AND Membership Status = Active
- **Purpose:** Promote morning-specific classes (6AM HIIT, 7AM Yoga) and early-bird scheduling changes

**Smart List 4: "Needs Trainer Assignment"**
- Filter: Assigned Trainer = Unassigned
- AND Membership Status = Active OR Trial
- **Purpose:** Identify members and trial users who haven't been matched with a trainer yet - front desk follow-up list

**Smart List 5: "VIP Clients"**
- Filter: Membership Type = VIP ($249/mo)
- AND Membership Status = Active
- **Purpose:** High-value members for white-glove treatment, early access to new programs, personal check-ins

**Smart List 6: "Trial Conversions Needed"**
- Filter: Membership Type = Free Trial
- AND Membership Status = Trial
- **Purpose:** Free trial members who need a conversion push before their 7 days expire

**Smart List 7: "Re-Engagement Needed"**
- Filter: Membership Status = Paused OR Last Activity Date > 30 Days Ago
- **Purpose:** Members who've gone quiet or paused - win-back campaign targets

For each Smart List:
1. Set the filters using the filter builder
2. Save and name the list exactly as shown above
3. Verify the correct contacts appear based on your imported data
4. Note the count of contacts matching each list

### Hands-On Exercise 2.7: Smart List Advanced Filters

Experiment with more complex filter combinations:

1. **AND vs OR logic:** Create a list for "Premium OR VIP members who prefer morning times" - this requires nesting: (Membership Type = Premium OR VIP) AND (Preferred Time = Early Morning OR Morning)
2. **Nested filter groups:** Try building a filter with AND groups inside an OR group
3. **Tag + Custom Field combo:** Find all contacts with tag "sunrise-import-day2" AND Fitness Goals contains "Weight Loss"
4. **Date-based filters:** Find members who joined in the last 90 days
5. Sort results by different columns (Join Date, Membership Type, etc.)
6. Save each useful combination as a named Smart List

---

## Part 4: Bulk Actions & Contact Management (30 min)

### Hands-On Exercise 2.8: Bulk Operations

1. Go to Contacts and select multiple members using the checkbox selection
2. Practice these bulk actions:
   - **Bulk Tag:** Select all VIP and Premium members, add tag **"priority-member"**
   - **Bulk Tag:** Select all Basic members, add tag **"upsell-candidate"**
   - **Bulk Delete:** Delete 2-3 test contacts (you'll restore them in the next exercise)

**Note on Bulk Email/SMS:** You'll set up email and SMS sending on Day 3 (Conversations). For now, focus on tagging and organizational bulk actions. If you have phone/email configured, you can optionally test a bulk message to a small group.

### Hands-On Exercise 2.9: Bulk Restore Deleted Contacts

1. After deleting contacts in the previous exercise
2. Navigate to the deleted contacts section (trash/archive area in Contacts)
3. Select the deleted contacts
4. Use **Bulk Restore** to recover them
5. Verify they're back in the main contact list with ALL data intact (custom fields, tags, everything)
6. Check Audit Logs to see both the delete and restore actions

### Hands-On Exercise 2.10: Tasks for Member Follow-Up

1. Open the contact record for a **Free Trial** member
2. Create a task:
   - Title: **"Call to schedule first training session - Trial Day 2"**
   - Due date: Tomorrow
   - Assign to yourself (in a real studio, you'd assign to Front Desk Morgan)
   - Priority: High
3. Open a **Paused** member's record and create a task:
   - Title: **"Win-back call - offer 20% return discount"**
   - Due date: This week
   - Priority: Medium
4. Open an **Unassigned Trainer** member and create a task:
   - Title: **"Match with trainer based on fitness goals and preferred time"**
   - Due date: Today
   - Priority: High
5. Navigate to the **Tasks view** and see all tasks aggregated
6. Mark one task as complete and verify it updates

### Hands-On Exercise 2.11: Companies (Optional)

1. Go to **Contacts > Companies** (or the Companies tab)
2. Create a company: **"Springfield Corporate Wellness"**
3. Associate 3-4 contacts with this company
4. **Use case for Sunrise Wellness:** A local company buys a corporate wellness package, and you want to group all their employees as contacts under that company. This lets you track the corporate account separately from individual memberships.
5. Understand when to use Companies vs Tags for grouping:
   - **Companies:** When contacts share an organizational relationship (corporate wellness clients, family plans)
   - **Tags:** When contacts share a characteristic but aren't organizationally related ("weight-loss-goal", "morning-person")

---

## Part 5: API Lab - Contact Management with Python

### Setup

Make sure you've completed the API setup from the prerequisites:
```bash
cd scripts/
pip install -r requirements.txt
cp config.py.example config.py
# Edit config.py with your API key and location ID
```

### Run the API Lab

Open and study `scripts/day-02-contacts-api.py`. The script demonstrates:

1. **Create a contact** via API with Sunrise Wellness custom fields
2. **Search contacts** with filters (find all Premium members)
3. **Update a contact** (change membership status, assign a trainer)
4. **List all contacts** with pagination
5. **Delete a contact** via API
6. **Bulk operations** - create multiple contacts from a list

Run each function one at a time and observe the API responses:

```bash
python scripts/day-02-contacts-api.py
```

### API Exercises

After studying the script, try these modifications:

1. Create 5 new contacts with full Sunrise Wellness custom fields (membership, fitness goals, trainer, etc.)
2. Write a search that finds all contacts where Membership Type = "VIP ($249/mo)"
3. Write a function that upgrades a member: changes Membership Type from Basic to Premium and updates Monthly Rate from 79 to 149
4. Create a script that exports all contacts to a new CSV file (reverse of the import)
5. Write a function that finds all contacts with Assigned Trainer = "Unassigned" and prints a summary

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Clinic - Patient Contact Structure

**Situation:** BrightSmile Dental Clinic needs a contact/patient database in GHL. Their needs are very different from a fitness studio - they track treatment history, insurance, and dental-specific scheduling. You won't reconfigure your sub-account; instead, document the complete design.

**Your Task:**

**1. Design the Custom Field structure for BrightSmile Dental:**

**Folder: "Patient Info"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Patient Type | Dropdown | New Patient, Returning, Referred, Emergency |
| Last Visit Date | Date | Date of most recent appointment |
| Next Appointment Type | Dropdown | Cleaning, Filling, Crown, Root Canal, Whitening, Veneer Consultation, Orthodontic Check, Emergency |
| Preferred Dentist | Dropdown | Dr. Sarah Kim, Dr. James Okafor |
| Visit Frequency | Dropdown | Every 6 Months, Quarterly, As Needed |

**Folder: "Insurance & Billing"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Insurance Provider | Dropdown | Aetna, BlueCross, Cigna, Delta Dental, MetLife, United, Self-Pay, Other |
| Insurance ID | Text | Policy number |
| Coverage Level | Dropdown | Basic, Standard, Premium, None |
| Payment Plan Active | Checkbox | Currently on a payment plan for a procedure |
| Outstanding Balance | Number | Dollar amount owed |

**Folder: "Treatment Plan"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Active Treatment | Dropdown | None, Whitening Series, Invisalign, Crown Prep, Implant Process |
| Treatment Stage | Dropdown | Consultation, In Progress, Follow-Up, Completed |
| Treatment Value | Number | Total procedure cost ($150-$3000+) |
| Medical Alerts | Textarea | Allergies, medications, conditions affecting dental work |

**2. Design a sample CSV with 15 patient records** (on paper or in a file):
- Mix of new and returning patients
- Various insurance providers including 2-3 self-pay patients
- A few with active treatment plans and payment plans
- Different preferred dentists
- At least 2 emergency patients

**3. Design Smart Lists for BrightSmile Dental:**
- **"Overdue for Cleaning"** - Last Visit Date > 6 months ago, Patient Type = Returning
- **"Active Treatment - Follow-Up Needed"** - Treatment Stage = In Progress or Follow-Up
- **"Self-Pay Patients"** - Insurance Provider = Self-Pay (target for in-house dental plan offers)
- **"Dr. Kim's Patients"** - Preferred Dentist = Dr. Sarah Kim (for schedule management)
- **"Outstanding Balance"** - Outstanding Balance > 0 AND Payment Plan Active = unchecked (need billing follow-up)

**4. Compare with Sunrise Wellness:**
- Dental custom fields focus on clinical history and insurance; wellness fields focus on preferences and goals
- Dental needs stricter data privacy controls (HIPAA) - how would "Only Assigned Data" help?
- Both use Smart Lists for follow-up, but the triggers are different (visit-based vs membership-based)

### Case Scenario 2: Elevate Digital Agency - Client Contact Structure

**Situation:** Elevate Digital Agency needs to track clients and prospects in GHL. Their contacts aren't consumers - they're businesses buying marketing services. The data structure is completely different from both the wellness studio and the dental clinic.

**Your Task:**

**1. Design the Custom Field structure for Elevate Digital Agency:**

**Folder: "Client Account"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Service Package | Dropdown | SEO Only, PPC Only, Social Media, Full Stack (SEO+PPC+Social), Email Marketing, Web Design |
| Monthly Retainer | Number | Dollar amount ($2,000 - $10,000) |
| Contract Start Date | Date | When the engagement began |
| Contract End Date | Date | When the contract is up for renewal |
| Account Manager | Dropdown | Rachel (AM), Derek (AM), Unassigned |
| Client Status | Dropdown | Prospect, Onboarding, Active, Paused, Churned |

**Folder: "Business Profile"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Industry | Dropdown | Healthcare, Real Estate, Legal, E-Commerce, Restaurant, SaaS, Other |
| Company Size | Dropdown | 1-10, 11-50, 51-200, 200+ |
| Annual Revenue | Dropdown | Under $500K, $500K-$1M, $1M-$5M, $5M+ |
| Website URL | Text | Client's website |
| Current Marketing Spend | Number | Monthly marketing budget before Elevate |

**Folder: "Performance & Pipeline"**

| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Lead Source | Dropdown | Inbound (Website), Referral, Cold Outreach, Networking Event, LinkedIn |
| Proposal Value | Number | Dollar value of pending proposal |
| Pipeline Stage | Dropdown | Discovery Call, Audit Delivered, Proposal Sent, Negotiation, Closed Won, Closed Lost |
| Upsell Opportunity | Multi-Select | Add SEO, Add PPC, Add Social, Increase Retainer, Add Email, Web Redesign |

**2. Design a sample CSV with 15 client/prospect records:**
- 6-8 active clients across different service packages and industries
- 3-4 prospects at various pipeline stages
- 2-3 churned or paused clients (win-back targets)
- Mix of Account Managers and 2 unassigned
- Retainers ranging from $2,000 to $10,000/month

**3. Design Smart Lists for Elevate Digital Agency:**
- **"Contracts Expiring in 60 Days"** - Contract End Date = within next 60 days, Client Status = Active
- **"Upsell Opportunities"** - Upsell Opportunity is not empty AND Client Status = Active
- **"Rachel's Book of Business"** - Account Manager = Rachel AND Client Status = Active (track her portfolio)
- **"High-Value Prospects"** - Pipeline Stage = Proposal Sent OR Negotiation AND Proposal Value > $5,000
- **"Churned - Win-Back Targets"** - Client Status = Churned, contract ended within last 6 months

**4. Key differences from Sunrise Wellness and BrightSmile Dental:**
- **Revenue tracking:** Agency tracks monthly retainers per client (B2B); wellness tracks membership tiers (B2C); dental tracks per-procedure billing
- **Contact volume:** Wellness studio might have 500+ members; agency might have 20-50 active clients but each is worth $2K-$10K/month
- **Smart List purpose:** Wellness lists drive marketing campaigns to many people; agency lists drive individual account management actions
- **"Only Assigned Data":** Critical for agencies - Rachel shouldn't see Derek's client data. At the wellness studio, the front desk needs to see everyone.

---

## Day 2 Recap Questions

Test your understanding:

1. What's the difference between a Custom Field (created today) and a Custom Value (created on Day 1)? When would Sunrise Wellness use each?
2. When importing the member CSV, what are the three duplicate-handling options, and which did you choose for Sunrise Wellness?
3. How does a Smart List differ from a static tag-based list? Give a Sunrise Wellness example where a member would automatically move between Smart Lists.
4. You want to send a promotional email to all Basic members who joined in the last 90 days and prefer morning classes. How would you create this segment?
5. A Sunrise Wellness member was accidentally deleted from the contacts list yesterday. How do you recover them, and will their custom field data still be intact?
6. What API endpoint do you use to create a new contact, and what fields are required? (Refer to `scripts/day-02-contacts-api.py`)

---

## Next Day Preview

**Day 3: Conversations & Communication** - You'll set up all communication channels for Sunrise Wellness Studio: email, SMS (if phone number available), and the web chat widget that members will see on your website/funnel. You'll create message templates for common studio communications (class reminders, welcome messages, membership renewal nudges) and use the API to send messages programmatically.

Make sure you have:
- A phone number purchased in your GHL account (optional - if you don't have one, you'll still complete all email and webchat exercises)
- Access to an email address for testing
- Your Sunrise Wellness contacts from today's import (you'll message them on Day 3)
