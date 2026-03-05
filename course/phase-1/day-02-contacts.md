# Day 2: Contacts & CRM Foundations

**Time Required:** 3-4 hours
**Certification Alignment:** Importing Contacts (3-part), Smart Lists, Custom Fields/Folders, Bulk Actions, Companies, Tasks, Bulk Restore
**API Lab:** Yes - `scripts/day-02-contacts-api.py`

---

## Learning Objectives

By the end of today, you will be able to:
1. Design and implement a custom field structure for any business type
2. Import contacts via CSV with proper field mapping and duplicate handling
3. Build Smart Lists for advanced contact segmentation
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

Custom Folders organize your custom fields into logical groups so the contact record stays clean.

### Hands-On Exercise 2.1: Design a Custom Field Structure

**Scenario:** You're setting up GHL for a fitness studio. Design and create these custom fields:

Navigate to **Settings > Custom Fields** (or Contacts > Custom Fields):

**Folder: "Membership Info"**
| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Membership Type | Dropdown | Free Trial, Basic, Premium, VIP |
| Join Date | Date | When they started |
| Expiry Date | Date | Membership end date |
| Monthly Rate | Number | Dollar amount |
| Membership Status | Dropdown | Active, Paused, Cancelled, Expired |

**Folder: "Lead Info"**
| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Lead Source | Dropdown | Website, Facebook, Instagram, Referral, Walk-in, Google |
| Fitness Goals | Multi-Select | Weight Loss, Muscle Gain, Flexibility, Endurance, General Health |
| Experience Level | Dropdown | Beginner, Intermediate, Advanced |
| Preferred Time | Dropdown | Morning (6-10AM), Midday (10AM-2PM), Afternoon (2-5PM), Evening (5-9PM) |
| Budget Range | Dropdown | Under $50/mo, $50-100/mo, $100-200/mo, $200+/mo |

**Folder: "Health & Safety"**
| Field Name | Type | Options/Notes |
|------------|------|--------------|
| Emergency Contact | Text | Name and phone |
| Medical Conditions | Textarea | Any relevant conditions |
| Waiver Signed | Checkbox | Liability waiver |

**Steps:**
1. Create each Custom Folder first
2. Then create each Custom Field inside the appropriate folder
3. Note the "Field Key" generated for each field - you'll need these for API access

### Hands-On Exercise 2.2: Test Custom Fields on a Contact

1. Go to **Contacts**
2. Click **+ Add Contact** (or find an existing contact)
3. Fill in standard fields (name, email, phone)
4. Scroll down to find your custom field folders
5. Fill in all custom fields for this test contact
6. Save and verify the data persists

---

## Part 2: Importing Contacts (60 min)

### Theory Recap (Cert: 3-Part Import Process)

GHL's import process has 3 critical steps:
1. **Prepare your CSV** - Column headers must match GHL fields
2. **Check for duplicates** - GHL can match by email, phone, or both
3. **Map and import** - Map CSV columns to GHL fields

### Hands-On Exercise 2.3: Prepare a CSV for Import

Create a CSV file (`sample-contacts.csv`) with 20+ contacts. Include these columns:

```csv
First Name,Last Name,Email,Phone,Company,Lead Source,Membership Type,Join Date,Fitness Goals,Experience Level
John,Smith,john.smith@example.com,+15551234001,Smith Corp,Website,Basic,2024-01-15,Weight Loss,Beginner
Jane,Doe,jane.doe@example.com,+15551234002,,Facebook,Premium,2024-02-01,"Weight Loss,Muscle Gain",Intermediate
Mike,Johnson,mike.j@example.com,+15551234003,Johnson LLC,Referral,Free Trial,,General Health,Beginner
Sarah,Williams,sarah.w@example.com,+15551234004,,Instagram,VIP,2023-06-15,"Flexibility,Endurance",Advanced
```

**Tips for CSV preparation:**
- Phone numbers should include country code (+1 for US)
- Multi-select values are comma-separated within quotes
- Date format should match your GHL settings (YYYY-MM-DD or MM/DD/YYYY)
- Leave cells empty for missing data, don't put "N/A"

Create at least 20 rows with varied data across all fields.

### Hands-On Exercise 2.4: Import Contacts with Duplicate Handling

Navigate to **Contacts > Import** (or the import button):

**Step 1:** Upload your CSV file
**Step 2:** Configure duplicate handling:
- Choose duplicate check method: **Email** (recommended for first import)
- Options: Skip duplicates, Update existing, or Create new
- For this exercise, select **"Update existing if duplicate found"**

**Step 3:** Map CSV columns to GHL fields:
- Map standard fields (First Name, Last Name, Email, Phone)
- Map custom fields (Lead Source, Membership Type, etc.)
- Set a default tag for this import batch: "csv-import-day2"

**Step 4:** Review and start import

**After import:**
1. Go to Contacts list and verify your contacts appear
2. Open 3-4 contacts and verify all fields mapped correctly
3. Check that multi-select fields imported properly
4. Verify the "csv-import-day2" tag was applied

### Hands-On Exercise 2.5: Handle Duplicate Imports

1. Modify your CSV - change the phone number for 3 existing contacts
2. Re-import the modified CSV with duplicate check set to **Email**
3. Choose **"Update existing"**
4. After import, verify that ONLY the phone numbers updated, not other data
5. Check: Did it create new contacts or update existing ones?

---

## Part 3: Smart Lists & Segmentation (45 min)

### Theory Recap

Smart Lists are dynamic, filter-based views of your contacts. Unlike static lists, Smart Lists automatically include/exclude contacts as their data changes. They're the foundation of targeted marketing and personalized automation.

### Hands-On Exercise 2.6: Build Smart Lists

Navigate to **Contacts** and look for the Smart List feature (usually a filter/list icon):

**Smart List 1: "Hot Leads - New This Week"**
- Filter: Created Date = Last 7 Days
- AND Lead Source = Website OR Facebook
- AND Membership Type = (empty/not set)
- Purpose: Identify new leads who haven't signed up yet

**Smart List 2: "Expiring Memberships"**
- Filter: Membership Status = Active
- AND Expiry Date = Next 30 Days
- Purpose: Target members for renewal campaigns

**Smart List 3: "Premium Upsell Candidates"**
- Filter: Membership Type = Basic
- AND Experience Level = Intermediate OR Advanced
- AND Membership Status = Active
- Purpose: Members who might upgrade to Premium

**Smart List 4: "Re-Engagement Needed"**
- Filter: Last Activity Date > 30 Days Ago
- AND Membership Status = Active
- Purpose: Active members who've gone quiet

**Smart List 5: "VIP Clients"**
- Filter: Membership Type = VIP
- AND Membership Status = Active
- Purpose: High-value clients for special treatment

For each Smart List:
1. Set the filters
2. Save and name the list
3. Verify the correct contacts appear
4. Note the count of contacts matching

### Hands-On Exercise 2.7: Smart List Advanced Filters

Experiment with advanced filter combinations:
1. Use **AND** vs **OR** logic - understand the difference
2. Try nested filter groups (AND groups within OR groups)
3. Filter by tags, custom field values, and date ranges
4. Sort results by different columns
5. Save each useful combination as a named Smart List

---

## Part 4: Bulk Actions & Contact Management (30 min)

### Hands-On Exercise 2.8: Bulk Operations

1. Select multiple contacts (checkbox selection)
2. Practice these bulk actions:
   - **Bulk Tag:** Add tag "fitness-studio-member" to selected contacts
   - **Bulk Email:** Send a test email to selected contacts
   - **Bulk SMS:** Send a test SMS (if phone numbers are configured)
   - **Bulk Delete:** Delete 2-3 test contacts (you'll restore them next)

### Hands-On Exercise 2.9: Bulk Restore Deleted Contacts

1. After deleting contacts in the previous exercise
2. Navigate to the deleted contacts section (trash/archive)
3. Select the deleted contacts
4. Use **Bulk Restore** to recover them
5. Verify they're back in the main contact list with all data intact

### Hands-On Exercise 2.10: Tasks Management

1. Open a contact record
2. Create a task:
   - Title: "Follow up on membership interest"
   - Due date: Tomorrow
   - Assign to yourself
   - Priority: High
3. Create 3 more tasks on different contacts
4. Navigate to the Tasks view and see all tasks aggregated
5. Mark a task as complete and verify it updates

### Hands-On Exercise 2.11: Companies

1. Go to **Contacts > Companies** (or the Companies tab)
2. Create a company: "FitLife Studios"
3. Associate 3 contacts with this company (use the business name field)
4. View the company record and see associated contacts
5. Understand when to use Companies vs Tags for grouping

---

## Part 5: API Lab - Contact Management with Python

### Setup

Make sure you've completed the API setup:
```bash
cd scripts/
pip install -r requirements.txt
cp config.py.example config.py
# Edit config.py with your API key and location ID
```

### Run the API Lab

Open and study `scripts/day-02-contacts-api.py`. The script demonstrates:

1. **Create a contact** via API
2. **Search contacts** with filters
3. **Update a contact** (modify custom fields)
4. **List all contacts** with pagination
5. **Delete a contact** via API
6. **Bulk operations** - create multiple contacts from a list

Run each function one at a time and observe the API responses.

```bash
python scripts/day-02-contacts-api.py
```

### API Exercises

After studying the script:
1. Modify it to create 5 contacts with your custom fields
2. Write a search that finds all contacts with "Membership Type = Premium"
3. Write a function that updates a contact's membership status
4. Create a script that exports all contacts to a CSV file

---

## Case Scenarios

### Case Scenario 1: Gym Member Import

**Situation:** PowerFit Gym has 500 members in a Google Sheet. They need them imported into GHL with proper segmentation.

**Given Data Structure:**
- Name, Email, Phone, Membership (Monthly/Annual/Day Pass), Start Date, Trainer Assigned, Location (Downtown/Westside)

**Your Task:**
1. Design the custom field structure needed
2. Prepare the CSV with proper formatting
3. Import with duplicate handling (some members may already exist as leads)
4. Create Smart Lists:
   - "Annual Members" (for renewal campaigns)
   - "Day Pass Users" (for conversion campaigns)
   - "Downtown Location" and "Westside Location"
   - "Unassigned to Trainer" (need trainer assignment)
5. Tag all imported contacts with "powergym-member"

### Case Scenario 2: Marketing Agency Contact Segmentation

**Situation:** A marketing agency has contacts from multiple campaigns across Facebook, Google Ads, and organic website traffic. They need to segment for personalized follow-up.

**Your Task:**
1. Create custom fields for:
   - Campaign Source, Ad Set, Landing Page URL, Lead Magnet Downloaded, Industry
2. Create Smart Lists for:
   - "Facebook Leads - Last 30 Days" (for retargeting)
   - "High-Intent" (visited pricing page or downloaded case study)
   - "Industry: Healthcare" (for industry-specific nurture)
   - "No Response in 7 Days" (for re-engagement)
3. Design a tagging strategy:
   - What tags would you use?
   - When should tags be applied (manual vs automated)?

### Case Scenario 3: Contact Data Cleanup

**Situation:** After 6 months of use, a sub-account has messy data: duplicate contacts, missing fields, inconsistent tags.

**Your Task:**
1. Use Smart Lists to find contacts with missing email addresses
2. Find potential duplicates (same phone number, different email)
3. Bulk update a tag across all contacts matching a filter
4. Delete test/fake contacts and verify with audit logs
5. Document a "data hygiene" checklist for monthly maintenance

---

## Day 2 Recap Questions

1. What's the difference between a Custom Field and a Custom Value?
2. When importing contacts, what are the three duplicate-handling options?
3. How does a Smart List differ from a static tag-based list?
4. You need to send a promotional email to all Basic members who joined in the last 90 days. How would you create this segment?
5. A contact was accidentally deleted yesterday. How do you recover it?
6. What API endpoint do you use to create a new contact, and what fields are required?

---

## Next Day Preview

**Day 3: Conversations & Communication** - You'll set up all communication channels, create templates, configure the webchat widget, and use the API to send messages programmatically.

Make sure you have:
- A phone number purchased in your GHL account (or plan to purchase one)
- Access to an email address for testing
