# Day 25: Admin Certification Review - Sub-Account Mastery

**Time Required:** 3-4 hours
**Cert Focus:** Launchpad, Communications, CRM, Calendars, Pipelines, Payments

## Today's Mission
Today covers sub-account level features - the day-to-day operations every user experiences. Since you built the complete Sunrise Wellness Studio over 10+ days, you have hands-on memory. Today's goal: formalize that knowledge into certification-ready recall with rapid-fire exercises and 25+ practice questions.

## Certification Topics
- Launchpad features
- Communications (phone, webchat, templates, missed call text-back)
- CRM (contacts, custom fields, custom values, smart lists, bulk actions, tasks, companies, bulk restore)
- Calendar types (Group/Round Robin, Basic/Unassigned, Class Booking, Collective)
- Opportunities and pipelines
- Payments (Invoices, Products, Text2Pay, Coupons, Orders, Subscriptions, Transactions)

---

## Part 1: Launchpad (20 min)

### What Is Launchpad?

**Launchpad** is GHL's new-sub-account onboarding checklist. Step-by-step wizard guides users through essential setup.

### Key Launchpad Steps

1. **Business Profile** - Name, address, phone, timezone
2. **Phone Number** - Buy and configure
3. **Import Contacts** - CSV upload
4. **Connect Integrations** - Google, Facebook, Stripe
5. **Build First Pipeline**
6. **Create First Calendar**
7. **Build First Workflow**
8. **Send First Campaign**

### Why Launchpad Matters for Cert

- Shows you understand the recommended onboarding order
- Proves you know what "day 1" looks like for a new sub-account
- Differentiates agencies that guide clients from those who don't

---

## Part 2: Communications Review (60 min)

### Conversations Architecture

Unified inbox. All channels appear here:
- SMS (if A2P registered)
- Email (if domain authenticated)
- Facebook Messenger (if FB page connected)
- Instagram DM (if IG connected)
- Google Business Messages
- WhatsApp Business
- Webchat (widget on site/funnel)
- Phone Calls (logs + recordings)

### SMS Templates Best Practices

- Keep under 160 characters when possible (one SMS segment)
- Include opt-out: "Reply STOP to opt out"
- Use merge fields: `{{contact.first_name}}`, `{{appointment.time}}`
- Avoid spam triggers: all caps, $$$, "FREE!!"

### Email Templates

- Subject line: under 50 chars for mobile
- Preview text: 85-90 chars
- Always mobile-responsive
- Include unsubscribe link (CAN-SPAM)

### Manual Actions

**What:** Workflow steps that require human action to continue.

**Use case:** "Call this lead" - workflow pauses, user calls, marks complete, workflow continues.

**Different from:** Fully automated actions (SMS, email) that fire without human touch.

### Webchat Widget (2-Part Setup)

**Part 1: Configure**
- Appearance (color, position, greeting)
- Offline message
- Pre-chat form (collect name/email/phone)

**Part 2: Install**
- On GHL funnel/website: toggle on
- On external site: paste JavaScript snippet

### Missed Call Text-Back

Auto-sends SMS when a call is missed. Game-changer for small businesses.

Workflow:
```
[Trigger: Missed Call]
[Wait 1 min]
[Send SMS: "Sorry we missed your call! How can we help?"]
```

### Phone Number Types (Memorize!)

| Type | Digits | Use Case |
|------|--------|----------|
| Local | 10 | Local business |
| Toll-Free | 10 (starts 800, 888, etc.) | National |
| Vanity | 10 (spells word) | Memorable marketing |
| Short Code | 5-6 | High-volume, enterprise |

---

## Part 3: CRM Deep Review (60 min)

### Contacts CRUD

- **Create:** Manual or import
- **Read:** View, search, filter
- **Update:** Edit fields, add tags, add notes
- **Delete:** Permanent or archive

### Importing Contacts (3-Part Process - Cert Topic!)

**Part 1: Prepare CSV**
- Column headers match or are mappable
- Phone numbers with country code
- Dates in consistent format
- Multi-select values comma-separated in quotes

**Part 2: Check for Duplicates**
- Match by: Email, Phone, or Both
- Actions on duplicate:
  - Skip
  - Update existing
  - Create new (creates duplicates)

**Part 3: Map and Import**
- Map CSV columns → GHL fields (standard + custom)
- Review preview
- Start import
- Monitor progress

### Custom Fields

**Types:**
| Type | Use Case |
|------|----------|
| Text | Names, short answers |
| Textarea | Long text, notes |
| Number | Quantities, amounts |
| Date | Dates without time |
| Dropdown | Single choice from list |
| Multi-Select | Multiple choices |
| Checkbox | Yes/No |
| File Upload | Documents, images |

### Custom Folders

Organize custom fields by category:
- Membership Info
- Fitness Profile
- Health & Safety
- Billing

### Custom Values (vs Custom Fields!)

**CRITICAL DISTINCTION:**
- **Custom VALUE** = Global variable (business phone, offer text) - ONE value for whole account
- **Custom FIELD** = Per-contact data (Jane's phone, Jane's membership) - different for each contact

### Smart Lists vs Static Lists vs Tags

**Smart List:** Dynamic, filter-based. Updates automatically.
Example: "VIP Members - Joined 30+ Days" auto-includes anyone matching.

**Static List:** Manual selection (not commonly used in GHL).

**Tag:** Simple label. Can trigger workflows, filter Smart Lists.

### Bulk Actions

- Bulk email
- Bulk SMS
- Bulk add tag
- Bulk remove tag
- Bulk delete
- Bulk export
- Bulk merge (for duplicates)
- **Bulk Restore** (recover deleted contacts!)

### Companies

Group contacts by the business they belong to.
- One company = multiple contacts
- Useful for B2B (agencies, consulting)
- NOT the same as tags

### Tasks

- Attach to contacts
- Due dates and priorities
- Assign to team members
- View aggregated task list

---

## Part 4: Calendars Review (60 min)

### Four Calendar Types (Memorize Cold!)

| Type | Configuration | Use Case |
|------|---------------|----------|
| **Group (Round Robin)** | Multiple team members, rotate bookings | Sales teams, multi-trainer gyms |
| **Unassigned (Basic)** | Single user or generic | Solo practitioner, one-service |
| **Class Booking** | Multiple people per slot | Workshops, group classes, webinars |
| **Collective** | Requires ALL listed users available | Team meetings (rare) |

### Essential Settings

- **Duration** - Length of appointment
- **Buffer** - Gap between appointments
- **Min notice** - How far ahead bookings allowed
- **Availability** - Days/times open
- **Booking form** - What to collect

### Distribution Logic (Round Robin)

- **Equal Distribution:** Each team member gets same number
- **Availability-Based:** Whoever is free soonest
- **Manual:** Admin assigns

### User Calendar Links

`{{user.calendar}}` - Merge field that resolves to the contact's ASSIGNED user's calendar.

**Use case:** Leads assigned to Alex should book with Alex. Use `{{user.calendar}}` in follow-up messages.

### Class Booking Specific

- **Max attendees** - Cap per slot
- **Waitlist** - Sign up if full
- **Cancellation policy** - Allow within X hours

### Calendar Settings

- Google/Outlook 2-way sync
- Timezone (inherits from sub-account)
- Overbooking protection
- Public calendar URL vs embedded

---

## Part 5: Pipelines Review (45 min)

### Pipeline = Process

Visual representation of a multi-stage process.

### Design Principles

- 4-7 stages optimal
- Clear entry criteria for each stage
- Always have Won and Lost end states
- Each stage = specific action happened

### Opportunity Status

Four values:
- **Open** - In progress
- **Won** - Successful
- **Lost** - Didn't convert
- **Abandoned** - No activity, gave up

### Multiple Pipelines

Not just for sales. Examples:
- Sales Pipeline
- Onboarding Pipeline
- Project Delivery
- Customer Support Escalation
- Recruitment

### Key Features

- Kanban view (drag cards between stages)
- List view (sortable table)
- Filter by stage, value, user, date
- Weighted pipeline value (value × probability)
- Stage-triggered automations (move to stage = workflow fires)

---

## Part 6: Payments Review (60 min)

### Products

**Two types:**
- One-time (single purchase)
- Recurring (subscription)

**Setup:**
- Name, description, price
- For recurring: billing interval (monthly, yearly, weekly)
- Image
- Tax-inclusive/exclusive

### Invoice Statuses (Memorize!)

- Draft
- Sent
- Viewed
- Paid
- Overdue
- Void

### Recurring Invoices

- Auto-generate on schedule
- Auto-pay if card on file
- Pause/resume capability
- Proration on changes

### Taxes

Configure once, apply to invoices:
- Percentage or fixed
- Name (Sales Tax, VAT)
- Default applied automatically

### Text2Pay

Send payment link via SMS. Click, enter card, paid.

**Use case:** After service delivery, before they leave.

### Coupons

**Types:**
- Percentage (20% off)
- Fixed Amount ($50 off)

**Restrictions:**
- Minimum order amount
- Specific products only
- Usage limits (per customer, total)
- Expiry date
- Single-use or multi-use

### Payment Dashboards

- **Orders** - Completed purchases
- **Subscriptions** - Active recurring billing
- **Transactions** - All payment events (success, failed, refunded)

### Failed Payment Handling

- Auto-retry (configurable)
- Email client on failure
- Pause subscription after X failures

---

## Part 7: Practice Quiz - 25 Questions

### Q1
What's the difference between a Custom Value and a Custom Field?
a) Same thing
b) Custom Value = global variable; Custom Field = per-contact data
c) Custom Field is read-only; Custom Value is editable
d) Custom Value is for payments only

**Answer: b)**

### Q2
A dentist books 30-minute cleanings with 1 hygienist. What calendar type?
a) Round Robin
b) Unassigned (Basic)
c) Class Booking
d) Collective

**Answer: b)** Single person, single bookings = Basic/Unassigned.

### Q3
A yoga studio offers drop-in classes with up to 15 people. What calendar type?
a) Round Robin
b) Unassigned
c) Class Booking
d) Collective

**Answer: c)**

### Q4
Which contact field type allows multiple selections?
a) Text
b) Dropdown
c) Multi-Select
d) Checkbox

**Answer: c)**

### Q5
How do you recover a deleted contact?
a) Can't, it's permanent
b) Contact HighLevel support
c) Bulk Restore from deleted contacts view
d) Re-import from backup

**Answer: c)**

### Q6
CAN-SPAM requires emails to include:
a) Unsubscribe link only
b) Unsubscribe link + physical address
c) Full legal name
d) Signature from CEO

**Answer: b)**

### Q7
You have 500 contacts but only want to email 100 "VIP Members." How?
a) Bulk email all 500
b) Create Smart List filtering VIP, send to list
c) Manually pick 100 contacts
d) Delete non-VIPs first

**Answer: b)**

### Q8
"Equal distribution" vs "Availability-based" in Round Robin:
a) Both prioritize availability
b) Equal = same count per person; Availability = whoever is free next
c) Availability is deprecated
d) Equal only works with 2+ people

**Answer: b)**

### Q9
What does `{{user.calendar}}` do?
a) Shows all calendars
b) Resolves to the contact's assigned user's calendar link
c) Shows user's Google Calendar
d) It's not valid

**Answer: b)**

### Q10
A Class Booking calendar for yoga:
- Max attendees: 20
- What happens at the 21st booker?
a) Error
b) Booked anyway
c) Goes on waitlist (if enabled) or blocked
d) Overflow to next class

**Answer: c)**

### Q11
Pipelines can be used for:
a) Sales only
b) Any multi-stage process
c) Only marketing
d) Only appointment tracking

**Answer: b)** Onboarding, projects, support, hiring - anything.

### Q12
What are opportunity statuses?
a) New, Old
b) Open, Won, Lost, Abandoned
c) Active, Inactive
d) Pending, Approved

**Answer: b)**

### Q13
Which invoice status indicates the client saw the invoice but didn't pay?
a) Sent
b) Viewed
c) Paid
d) Overdue

**Answer: b)** Sent = delivered, Viewed = actually opened.

### Q14
What's Text2Pay?
a) Pay by voice text
b) Payment link sent via SMS
c) SMS for bills
d) Automatic billing

**Answer: b)**

### Q15
A coupon restricted to "Premium Membership" only:
a) Works on any product
b) Fails checkout on other products
c) Only works at certain times
d) Applied automatically everywhere

**Answer: b)**

### Q16
What field types does GHL support? (pick all that apply)
a) Text, Number, Date
b) Dropdown, Multi-Select, Checkbox
c) File Upload, Textarea
d) All of the above

**Answer: d)**

### Q17
Importing contacts: duplicate checked by email. Setting "Update existing" does:
a) Creates new contact anyway
b) Updates matched contact with new CSV data
c) Deletes old, creates new
d) Errors out

**Answer: b)**

### Q18
Companies are:
a) Same as tags
b) Separate entity that contacts can belong to
c) Only for agencies
d) Not supported

**Answer: b)**

### Q19
A Smart List with filter "Created Date = Last 7 Days":
a) Static list of today's contacts
b) Dynamic list that auto-updates as time moves
c) Breaks after 7 days
d) Errors

**Answer: b)**

### Q20
Missed Call Text-Back workflow trigger:
a) Any call
b) Missed incoming call
c) Outbound call
d) Voicemail only

**Answer: b)**

### Q21
Tasks in GHL can be:
a) Only assigned to contacts
b) Assigned to contacts AND team members with due dates
c) Only a checklist
d) Integrated with Asana

**Answer: b)**

### Q22
Recurring invoice with auto-pay requires:
a) Manual entry each time
b) Customer's card on file
c) Bank account connection
d) PayPal only

**Answer: b)**

### Q23
Webchat widget is configured in:
a) Two parts: Appearance config, then installation
b) One step
c) Only via code
d) Only on mobile app

**Answer: a)**

### Q24
Coupon usage limit of 100:
a) Works only 100 times total across all customers
b) Each customer can use 100 times
c) Lasts 100 days
d) 100% off

**Answer: a)** Total uses across all customers.

### Q25
What's the minimum notice setting on a calendar?
a) How long a booking lasts
b) How far ahead someone can book (prevents last-minute)
c) How long to notify the user
d) Expiration time

**Answer: b)**

---

## Part 8: Rapid-Fire Recall Exercise

Time yourself - these should come instantly:

**10-second challenges:**
- [ ] Name all 4 calendar types
- [ ] Name all 4 opportunity statuses
- [ ] Name all communication channels
- [ ] Name all 6 invoice statuses

**20-second challenges:**
- [ ] List the 3 parts of contact import
- [ ] Name all custom field types
- [ ] List all coupon restrictions

**30-second challenges:**
- [ ] Explain difference: Custom Value vs Custom Field
- [ ] Explain difference: Smart List vs Tag
- [ ] Explain: Round Robin distribution logic

**If any are slow, review that section.**

---

## Quick Reference Cheat Sheet

| Topic | Key Points |
|-------|-----------|
| Calendar Types | Group (RR), Basic (Unassigned), Class Booking, Collective |
| Opp Statuses | Open, Won, Lost, Abandoned |
| Invoice Statuses | Draft, Sent, Viewed, Paid, Overdue, Void |
| Import 3-Parts | Prepare CSV → Check Duplicates → Map and Import |
| Custom Field Types | Text, Number, Date, Dropdown, Multi-Select, Checkbox, File, Textarea |
| Bulk Actions | Email, SMS, Tag, Delete, Export, Merge, **Restore** |
| Round Robin Logic | Equal Distribution OR Availability-Based |
| Coupon Types | Percentage, Fixed Amount |
| Coupon Restrictions | Min order, Product-specific, Usage limit, Expiry |
| `{{user.calendar}}` | Resolves to contact's assigned user's calendar |

---

## Day 25 Recap

Sub-account core features are where you live daily. Tomorrow: marketing, sites, and automation - the "cool" features that drive growth.

## Next Day Preview

**Day 26: Marketing, Sites & Automation Review** - Email Builder, Campaigns, Trigger Links, Funnels, Forms, Surveys, Workflows, Recipes, Reputation. 30+ practice questions.
