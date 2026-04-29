# GoHighLevel Admin Certification - Complete Study Guide

**Purpose:** Single-document reference for everything on the Admin Certification exam.

---

## How to Use This Guide

- **Skim** before taking the Phase 4 mock exam (30 min review)
- **Deep read** if you scored below 80% on the mock exam
- **Pre-exam cramming** the day before the real test (focus on Gotchas sections)
- **Lookup reference** during open-book practice sessions

### Hands-On Exam Practice (Recommended)

If you want a single practical you can run like a timed build, use:
- [Phase 1 Practical (BrightSmile + Elevate)](../course/phase-1/practical-brightsmile-elevate-full-build.md)

### Suggested Study Schedule
| Days Before Exam | Activity |
|------------------|----------|
| 7 days | Full read-through, take notes on weak areas |
| 5 days | Re-read weak sections, do flashcards |
| 3 days | Mock exam #1, review misses |
| 2 days | Target weak topics, re-read Gotchas |
| 1 day | Mock exam #2, light skim of Gotchas |
| Exam day | Coffee, confidence, go |

---

## Exam Overview

- **Provider:** HighLevel (via official certification portal)
- **Format:** Online, multiple choice, some scenario-based
- **Questions:** ~80-100 (verify current count at certification portal)
- **Time limit:** Typically 2 hours (verify)
- **Passing score:** 80% (verify)
- **Retake policy:** Usually allowed after a waiting period (often 24-72 hours)
- **Cost:** Check current pricing in the HighLevel certifications program
- **Proctoring:** May be webcam-monitored — check requirements before scheduling

### Before You Start the Exam
- Close all tabs except the exam
- Read scenario questions TWICE before answering
- Flag unclear questions, move on, return at end
- Watch time — pace for roughly 1 minute per question
- Don't second-guess; first instinct is usually right on factual items

---

## Topic Breakdown by Weight (Estimated)

| Topic Area | Est. % of Exam | Priority |
|-----------|----------------|----------|
| Sub-Account Core (CRM, Contacts) | 20% | HIGH |
| Automation (Workflows, Recipes) | 12% | HIGH |
| Communications | 10% | HIGH |
| Calendars | 10% | HIGH |
| Payments | 10% | MEDIUM |
| Marketing (Email, Trigger Links) | 10% | MEDIUM |
| Opportunities/Pipelines | 8% | MEDIUM |
| Sites (Funnels, Forms, Surveys) | 8% | MEDIUM |
| Agency Features | 7% | MEDIUM |
| Compliance & Legal | 5% | LOW but critical |

**Strategy:** Master HIGH priority topics first. These account for ~52% of the exam. A confident pass requires 80%+; you cannot afford to skip these.

---

# SECTION 1: Sub-Account Core (CRM & Contacts)

## Key Concepts

### Sub-Account (Location)
A single business's isolated workspace inside a HighLevel agency. Each sub-account has its own contacts, calendars, pipelines, workflows, and settings. A sub-account is what clients see; the agency manages many of them.

### Contact
A person record in the CRM. Unique identifier is typically email or phone. Contacts carry tags, custom fields, pipeline opportunities, and communication history.

### Custom Field
A data point ATTACHED TO A SPECIFIC CONTACT. Examples: Birthday, T-Shirt Size, Membership Tier. Each contact has their own value. Can be text, number, date, dropdown, checkbox, multi-select, signature, file upload.

### Custom Value
A GLOBAL variable used across the account. Examples: Business Name, Owner Phone, Booking Link. The SAME value applies everywhere it's referenced. Used in templates, workflows, and emails to avoid hardcoding.

**Critical distinction:**
- Custom Field = "This contact's birthday is March 5"
- Custom Value = "Our business phone is (555) 123-4567" (same for everyone)

### Tag
A keyword label on a contact. Used for segmentation. A contact can have many tags. Tags are free-form strings — that's why naming conventions matter.

### Smart List
A DYNAMIC filter on contacts. Updates automatically when contact data changes. Example: "Members with no session in 30 days." If a contact no longer matches the filter, they drop from the Smart List. Not a manual list.

### Static List (via tag)
Unlike Smart Lists, you can simulate static lists by applying a tag. The tag stays until manually removed.

### Folder
Organizational container for grouping Custom Fields or Custom Values. Does NOT affect logic, just UI organization.

### Business Profile / Settings
Where timezone, business hours, address, and default email/phone are configured. Timezone is CRITICAL — affects all automations, calendars, and timestamps.

## Common Exam Question Patterns

1. **"You need to store a different value for each contact..."** → Custom Field
2. **"You need to reuse the same business-wide value..."** → Custom Value
3. **"You need contacts that match a filter and update automatically..."** → Smart List
4. **"You need to label contacts for segmentation..."** → Tag
5. **"Where do you set the business timezone?"** → Sub-account Settings > Business Profile

## Gotchas (Things That Trip People Up)

### Custom Value vs Custom Field (MOST COMMON TRAP)
- Custom VALUE = global, one value for the account
- Custom FIELD = per-contact, each contact has their own value
- Merge field syntax differs: `{{custom_values.xxx}}` vs `{{contact.custom_field_xxx}}`

### Smart List vs Tag
- Smart List = dynamic filter (auto-updates)
- Tag = manual label (sticks until removed)
- Smart Lists are REPORTS, not storage
- Tags are STORAGE, not filters (though Smart Lists can filter BY tag)

### Bulk Restore Access Location
- Found in: Contacts > Bulk Actions > View Deleted Contacts
- Deleted contacts are recoverable for a limited window (verify current window)
- After the window, they are permanently gone
- Always prefer tag-based archival ("archived-2026") over deletion

### Custom Field Type Locking
- Once a field has data, you CANNOT change its type freely
- Plan field types carefully before launch

### Contact Merge
- Merging contacts COMBINES their data (tags, fields, opportunities, communication)
- One contact is kept, the other is removed
- Conversations move to the kept contact

### Things to NEVER Confuse
- Company vs Contact (Company = organization, can have many contacts)
- Custom Field vs Custom Value (covered above)
- Tag vs Smart List (covered above)
- Note vs Task (Note = free text; Task = assigned, has due date)

---

# SECTION 2: Communications

## All Channels in HighLevel

| Channel | Use Case | Requires |
|---------|----------|----------|
| SMS | Short transactional + promotional | Twilio phone, A2P (US) |
| MMS | Image/media messages | Twilio phone, A2P (US), slight cost premium |
| Email | Marketing + transactional | Email service (Mailgun or LC Email) |
| Voice (call) | Outbound/inbound calls | Twilio phone |
| Voicemail Drop | Pre-recorded VM without ringing | Configured voicemail recording |
| WhatsApp | International messaging | WhatsApp Business setup |
| Facebook Messenger | FB page messaging | FB page integration |
| Instagram DM | IG messaging | IG Business integration |
| GMB Chat | Google Business chat | GMB integration |
| Webchat | Website chat widget | Widget installed on site |
| Review Request | Ask for review | GMB/Facebook connection |
| Manual Call/SMS | Task-driven human action | Nothing — workflow adds task |

## Phone Number Types

- **Local number** — tied to an area code, looks regional
- **Toll-free number** — 800/888/877/866/855/844/833 prefix
- **Short code** — 5-6 digit (NOT typically available in HighLevel; usually Twilio long code)

**Exam-relevant fact:** HighLevel provisions numbers via Twilio. Most sub-accounts use 10-digit long code numbers.

## A2P 10DLC Facts to Memorize

- **What it is:** Application-to-Person messaging on 10-digit long codes (US-only regulation)
- **Required for:** All US SMS sending via long-code numbers
- **Registration components:** Brand registration + Campaign registration
- **Brand:** Your business (EIN, address, business type)
- **Campaign:** The use case (customer care, marketing, 2FA, etc.)
- **Without registration:** Messages get filtered/blocked by carriers
- **Country scope:** US ONLY — not Canada, UK, Australia, etc.
- **Fees:** One-time brand fee + monthly campaign fee (plus per-message fees)
- **Timing:** Approval can take days to weeks — plan ahead
- **Throughput:** Registered campaigns get higher trust score and higher throughput

**Common exam trap:** Questions may ask about A2P in non-US contexts. A2P 10DLC is US-only.

## Manual Actions Explanation

Manual Actions are workflow steps that assign a TASK to a user rather than automating the message. Use when:
- Personalization requires human judgment
- Legal/compliance requires human intervention
- High-value lead requires a human touch

Types:
- **Manual SMS** — task to send an SMS (template may be pre-filled)
- **Manual Call** — task to call the contact (scripts may be attached)
- **Manual Email** — task to send an email

The workflow pauses at the Manual Action until the user completes the task.

## Webchat 2-Part Setup

Webchat requires TWO things configured:
1. **Widget configuration inside HighLevel** — look and feel, fields, routing, welcome message
2. **Embed code installed on the website** — JavaScript snippet placed in site HTML (before `</body>`)

If either is missing, widget does not appear or does not work.

Additional configurations:
- **Business hours** — when widget is "live" vs "leave a message"
- **SMS continuation** — captures phone number, continues conversation as SMS if visitor leaves
- **Auto-reply** — initial message when visitor opens widget

## Common Exam Patterns

1. "Why isn't SMS sending in the US?" → A2P 10DLC not registered
2. "Webchat widget not appearing on site?" → Embed code missing
3. "Need to send pre-recorded voicemail without call?" → Voicemail Drop
4. "Need human to call, but triggered by a form?" → Manual Call action in workflow

## Things to NEVER Confuse

- SMS vs MMS (MMS = media, slightly higher cost)
- Campaign (messaging) vs Campaign (A2P registration) — different concepts
- Workflow manual action vs manually doing it outside a workflow
- HighLevel email vs external email (SMTP via Mailgun was common; LC Email is native)

---

# SECTION 3: Calendars

## Calendar Types Table

| Type | When to Use | Example |
|------|-------------|---------|
| **Round Robin** | Multiple team members share slots; system rotates | Sales team: 5 reps, balance load |
| **Collective** | Multiple people MUST attend together | Discovery call with rep + manager |
| **Class** | Group session, multiple attendees for same slot | Yoga class: 1 instructor, 15 students |
| **Service** | Service booking with specific team member | PT session with specific trainer |
| **Personal** | Single user's calendar | Owner's 1:1 consultations |
| **Unassigned** | No specific owner; captures leads | Generic "Book a Call" |

## Exam Trap: Collective vs Round Robin

**This is one of the most tested distinctions.**

- **Round Robin:** ONE person from the group is assigned per booking. System rotates among team.
  - Example: 3 sales reps, lead books → assigned to Rep #1, next lead → Rep #2, etc.
- **Collective:** ALL specified people attend TOGETHER on the booking.
  - Example: Sales rep + sales manager both attend the same discovery call.

**Memory trick:** RouND = oNe. Collective = Collection of people.

## Calendar Settings to Know

- **Buffer Time** — minutes between appointments (before/after)
- **Minimum Scheduling Notice** — how far in advance can someone book (e.g., 2 hours)
- **Minimum Booking Window** — farthest out someone can book (e.g., 60 days)
- **Slot Interval** — time between slot starts (e.g., 30 min)
- **Slot Duration** — length of the appointment
- **Appointment Capacity** — how many can book same slot (important for Class type)
- **Availability** — days and hours when bookings allowed
- **Date Specific Hours** — overrides for specific dates
- **Auto Confirm vs Manual Confirm** — does booking need staff approval?

## Appointment Statuses

- **New** — just booked, not yet handled
- **Confirmed** — approved
- **Showed** — attended
- **No Show** — did not attend
- **Cancelled** — cancelled by contact or staff
- **Invalid** — marked as bogus

**Workflow trigger:** "Appointment Status Changed" can fire based on transitions.

## Calendar Groups

Group multiple calendars under a shared booking link. Useful when a lead chooses between service types.

## Common Exam Patterns

1. "3 trainers, one booking page, rotates among them" → Round Robin
2. "Sales rep + manager attend every discovery call" → Collective
3. "Yoga class with 15 spots" → Class calendar
4. "Need 15 min break between appointments" → Buffer Time
5. "Prevent bookings less than 2 hours out" → Minimum Scheduling Notice

## Things to NEVER Confuse

- Round Robin vs Collective (covered above)
- Slot Interval vs Slot Duration (interval = start-to-start; duration = length of appt)
- Minimum Notice (how soon can they book) vs Minimum Window (how far out)
- Calendar Group vs Calendar Team (Group = booking link; Team = assigned users)

---

# SECTION 4: Opportunities / Pipelines

## Key Concepts

### Pipeline
A visual representation of stages a deal progresses through. Think "sales funnel in kanban view."

### Stage
A step in the pipeline. Examples: New Lead > Qualified > Proposal > Negotiation > Won/Lost.

### Opportunity
A potential deal, assigned to a stage, tied to a contact, with a monetary value.

### Status Values (MEMORIZE)

| Status | Meaning |
|--------|---------|
| **Open** | Active deal, in progress |
| **Won** | Deal closed successfully |
| **Lost** | Deal dead, did not close |
| **Abandoned** | No activity, dropped |

These are separate from STAGE. A deal can be "Open in Qualified stage" or "Won in Closed stage."

## Pipeline vs Workflow (Exam Favorite)

- **Pipeline** = visual tracking of deal progression (kanban board)
- **Workflow** = automation that runs based on triggers

A pipeline doesn't automate anything by itself. A workflow can MOVE opportunities between stages, but the pipeline just displays them.

**Common pattern:** Workflow is triggered by "Opportunity Stage Changed" → sends email or creates task.

## Stage Transition Triggers

Workflows can trigger on:
- Opportunity Created
- Opportunity Status Changed (Open/Won/Lost/Abandoned)
- Opportunity Stage Changed
- Opportunity Value Changed (verify availability)

Workflows can perform:
- Move Opportunity to Stage X
- Update Opportunity Status
- Update Opportunity Value
- Assign Opportunity to User

## Opportunities vs Contacts

- Contacts exist independently of opportunities
- One contact can have many opportunities (different deals at different times)
- Opportunity is tied to a contact by ID

## Common Exam Patterns

1. "Track deals visually through stages" → Pipeline
2. "Deal closed successfully" → Status = Won
3. "Deal went cold, no activity" → Status = Abandoned
4. "Automatically email when deal reaches Proposal stage" → Workflow with "Stage Changed" trigger
5. "Move opportunity forward based on form submission" → Workflow with Move action

## Gotchas

- A deal moved to a "Won stage" does NOT automatically set Status = Won. Status must be set explicitly (manually or via workflow).
- Lost deals stay in pipeline unless filtered out
- Multiple pipelines per sub-account supported — don't force one pipeline to do everything

## Things to NEVER Confuse

- Pipeline vs Workflow (Pipeline = tracking; Workflow = automation)
- Stage vs Status (Stage = position in pipeline; Status = state of deal)
- Opportunity vs Contact (Opportunity = deal; Contact = person)

---

# SECTION 5: Payments

## Product Types

| Type | Description | Billing |
|------|-------------|---------|
| **One-time** | Single charge | Once |
| **Recurring** | Subscription | Weekly/Monthly/Yearly |
| **Free** | No charge | N/A (used for lead magnets, trials) |
| **Physical** | Ships a product | One-time typical |
| **Digital** | Digital delivery | One-time typical |
| **Service** | Service-based | Can be one-time or recurring |

## Product vs Price

- A Product can have multiple Prices (e.g., monthly $99, yearly $999)
- Customers choose a price at checkout (or funnel pre-selects)

## Invoice Statuses (ALL 6 — MEMORIZE)

| Status | Meaning |
|--------|---------|
| **Draft** | Created but not sent |
| **Sent** | Delivered to customer, awaiting payment |
| **Viewed** | Customer opened invoice link |
| **Paid** | Payment received in full |
| **Partially Paid** | Some payment received, balance remaining |
| **Overdue** | Due date passed, unpaid |
| **Void** | Cancelled, no longer collectable |

**Note:** There are 6-7 depending on HighLevel version — verify current states.

## Coupon Types and Restrictions

### Types
- **Percentage** — e.g., 20% off
- **Fixed Amount** — e.g., $10 off

### Restrictions / Settings
- **Duration:** One-time, Forever, Specific Months (for subscriptions)
- **Max Uses:** Total uses across all customers
- **Max Uses Per Customer:** Limit per person
- **Expiration Date:** When coupon stops working
- **Products Applicable:** Which products accept the coupon
- **Minimum Order Amount:** Must spend X to apply

## Text2Pay Scenarios

**What it is:** Send an invoice via SMS; customer pays directly from phone.

**When to use:**
- In-person service, customer walks out owing money
- Phone-only customer who struggles with email
- Follow-up on overdue invoices
- Low-friction upsell

**How it works:**
1. Create invoice in HighLevel
2. Send via SMS option
3. Customer receives link
4. Customer taps link, pays via mobile-friendly page
5. Invoice marked Paid automatically

## Payment Processors

- **Stripe** — most common, widely integrated
- **PayPal** — supported
- **NMI** — alternative
- **Authorize.net** — alternative
- **Square** — may be supported (verify)

## Common Exam Patterns

1. "Customer hasn't paid and due date passed" → Status: Overdue
2. "Subscription that auto-charges monthly" → Recurring product
3. "20% off applies only to first 3 months" → Coupon with Duration: Specific Months (3)
4. "Customer walked out without paying" → Text2Pay
5. "Invoice created but not sent" → Status: Draft

## Gotchas

- Invoice VOID is not the same as REFUND. Void = cancelled before payment. Refund = money returned after payment.
- Coupons can stack unexpectedly if not restricted — always set Max Uses and check rules
- Recurring products billing cycle starts from the first successful charge date
- Subscription failed payment does NOT auto-cancel — workflow or staff action required

## Things to NEVER Confuse

- Void vs Refund (pre-payment cancel vs post-payment return)
- Product vs Price (Product = item; Price = billing option)
- One-time vs Recurring (confirm at product level)

---

# SECTION 6: Marketing (Email, Trigger Links, Campaigns)

## Campaign vs Workflow (EXAM FAVORITE)

- **Campaign** — scheduled/sequenced messages to a list or segment (classic email blast or drip)
- **Workflow** — event-driven automation with branching logic

### Key Differences

| Feature | Campaign | Workflow |
|---------|----------|----------|
| Trigger | Manual send or schedule | Event (form, tag, etc.) |
| Branching | Limited | Full If/Else logic |
| Conditions | Basic | Extensive |
| Channels | Usually single-channel | Multi-channel (SMS, email, voicemail, tasks) |
| Typical Use | Newsletter, blast | Nurture, onboarding, re-engagement |

**Exam tip:** If the question has IF/THEN logic, it's a Workflow. If it's "send this to everyone on Thursday," it's a Campaign.

## Email Types in HighLevel

- **Marketing Email** — promotional, requires unsubscribe
- **Transactional Email** — receipts, booking confirmations
- **Campaign Email** — part of a scheduled campaign
- **Workflow Email** — sent via automation trigger

## Email Builder Features

- Drag-drop blocks
- Merge fields (contact + custom values)
- AB testing (subject lines, content)
- Schedule send
- Time zone send (based on contact's timezone)
- Preview desktop + mobile

## Trigger Link Capabilities

A trigger link is a trackable URL embedded in email/SMS. When clicked, it:

1. **Tags the contact** (e.g., "clicked-pricing-link")
2. **Moves them in a pipeline** (opportunity stage change)
3. **Subscribes them to a list/segment**
4. **Unsubscribes them** (opt-out link)
5. **Starts/stops a workflow**
6. **Triggers a workflow** with a "link clicked" event

**Use cases:**
- Segment interested leads by behavior
- Measure email engagement
- Drive workflow branching

## Email Compliance (CAN-SPAM)

### CAN-SPAM Act Requirements (US)
1. **Accurate "From" line** — no deception
2. **Non-misleading subject line**
3. **Identify as ad** if it's promotional
4. **Include physical mailing address**
5. **Provide clear unsubscribe** — honored within 10 business days
6. **Monitor what others do for you** — you're responsible for contractors' compliance

### Practical Implications
- Never send without unsubscribe link
- Never use deceptive subject lines
- Include business address in footer (use Custom Value for this)
- Honor unsubscribes immediately (HighLevel does this automatically)

## Email Deliverability Factors

- Sender reputation (IP + domain)
- SPF, DKIM, DMARC records
- Bounce rate (keep low — clean lists)
- Complaint rate (keep very low)
- Engagement (opens, clicks) — high engagement improves rep
- Content quality (no spam words, balanced text/image)

## Common Exam Patterns

1. "Email sequence that branches on form answer" → Workflow
2. "Scheduled newsletter every Tuesday" → Campaign
3. "Track who clicked the pricing link" → Trigger Link with tag
4. "Legally required in marketing emails" → Unsubscribe link + physical address
5. "Subscriber unsubscribed, legally must stop within..." → 10 business days

## Gotchas

- Campaigns and Workflows both send emails — knowing WHEN to use which is tested
- Trigger links only fire if the EXACT tracked link is clicked — don't mix with raw URLs
- Unsubscribe link must be clearly visible (not hidden tiny gray text at bottom)

## Things to NEVER Confuse

- Campaign vs Workflow (covered)
- Marketing email vs Transactional email (compliance rules differ)
- Trigger link vs regular link (trigger link has tracking UUID)

---

# SECTION 7: Sites (Funnels, Websites, Forms, Surveys)

## Funnel vs Website (MEMORIZE DISTINCTION)

| Aspect | Funnel | Website |
|--------|--------|---------|
| Purpose | Linear conversion path | Multi-page information |
| Structure | Step-by-step (step 1 > step 2 > step 3) | Navigation-based (menu to pages) |
| Analytics | Per-step conversion tracking | Per-page views |
| Example | Lead magnet > Thank you > Upsell | Home, About, Services, Contact |
| CTA | ONE focused goal | Multiple CTAs possible |

**Exam trap:** Both use the same page builder and look similar. The difference is PURPOSE and STRUCTURE.

## Page Builder Elements

- Sections (rows/columns)
- Text blocks
- Images
- Buttons (CTA)
- Forms (embedded)
- Surveys (embedded)
- Calendar widget (booking)
- Video embed
- Countdown timer
- Testimonials
- Custom HTML/code
- Pop-ups

## DNS Records Basics

Required knowledge for connecting custom domains.

| Record Type | Purpose | Example |
|-------------|---------|---------|
| **A Record** | Maps domain to IPv4 address | example.com → 1.2.3.4 |
| **CNAME** | Maps subdomain to another domain | www.example.com → ghl.com |
| **TXT** | Text info (SPF, DKIM, verification) | v=spf1 include:... |
| **MX** | Mail server routing | mail.example.com |

### For HighLevel
- Custom domain for funnel/site: typically CNAME or A record
- Email sending domain: requires SPF + DKIM + DMARC (TXT records)
- Verification: may require TXT record with unique value

### Propagation
- DNS changes take 0 min to 48 hours to propagate
- Use tools like `dig`, `nslookup`, or whatsmydns.net to verify

## Form vs Survey Distinction

| Aspect | Form | Survey |
|--------|------|--------|
| Pages | Single page | Multi-page (steps) |
| Fields | Displayed all at once | One question at a time typical |
| Conditional Logic | Limited | Full — question order depends on answers |
| Use Case | Lead capture, contact, signup | Qualification, assessment, quiz |
| Embed | Inline, popup, full-page | Inline, popup, full-page |

**Memory trick:** Form = simple. Survey = smart (conditional).

## Survey Conditional Logic

- Skip logic: "If Q1 = Yes, skip to Q5"
- Show/hide questions based on prior answers
- Multiple ending pages based on answers
- Useful for lead qualification

**Example:** Sunrise Wellness Studio intake survey.
- Q1: "What's your goal?" → Weight loss / Strength / Flexibility
- If Weight loss → Q2a: "Current weight?" 
- If Strength → Q2b: "Current lift numbers?"
- If Flexibility → Q2c: "Any injuries?"

## Form/Survey Settings

- **Post-submit action:** Redirect URL, show message, close popup
- **Trigger workflow:** Start a workflow on submit
- **Notification email:** Email to staff on submit
- **Captcha:** Block bots
- **Duplicate handling:** How to treat repeat submissions
- **Field mapping:** Map to custom fields on the contact

## Common Exam Patterns

1. "Lead magnet → opt-in → thank you → upsell" → Funnel
2. "Home, About, Services, Blog" → Website
3. "One question at a time, branches on answer" → Survey
4. "Simple email+name capture" → Form
5. "Map domain to HighLevel site" → DNS record (CNAME typical)
6. "Show different question based on prior answer" → Survey conditional logic

## Gotchas

- Funnel and Website use same builder — don't assume they're different tools
- DNS TTL affects propagation; low TTL before making changes
- Form submissions go to contact; survey submissions ALSO go to contact (with answers as custom fields)
- Captcha reduces bots but can deter real users on mobile — use wisely

## Things to NEVER Confuse

- Funnel vs Website (purpose, not tool)
- Form vs Survey (single page vs multi-page/conditional)
- A record vs CNAME (A = IP; CNAME = another domain)

---

# SECTION 8: Automation (Workflows, Recipes)

## Triggers vs Actions

- **Trigger** — what STARTS the workflow (event-based)
- **Action** — what the workflow DOES (send, wait, update, branch)

### Common Triggers
- Contact Created
- Contact Tag Added / Removed
- Form Submitted
- Survey Submitted
- Appointment Booked / Status Changed
- Opportunity Created / Stage Changed / Status Changed
- Payment Received
- Invoice Status Changed
- Email Opened / Clicked
- Trigger Link Clicked
- Birthday Reminder
- Call Status
- Inbound Message
- Task Completed
- Customer Replied

### Common Actions
- Send SMS / Email / Voicemail Drop
- Wait (duration or until specific time)
- If / Else branch
- Add / Remove Tag
- Update Contact Field
- Create / Update Opportunity
- Move Opportunity to Stage
- Create Task
- Manual Action (Call/SMS/Email assigned to user)
- Add to Workflow / Remove from Workflow
- Notify user (internal email/SMS)
- Webhook (call external URL)
- GPT / AI action (verify availability)

## If/Else Patterns

### Common Patterns
1. **Tag check:** If contact has tag "trial-member" → send trial email; Else → send general email
2. **Custom field check:** If goal = "weight loss" → weight loss track; Else if "strength" → strength track
3. **Lead score check:** If lead score > 50 → sales qualified; Else nurture
4. **Appointment status:** If showed → post-visit follow-up; If no-show → recovery sequence
5. **Time-based:** If current time is weekend → wait until Monday; Else send now

### Best Practice
- Label branches clearly ("Yes-weight-loss" vs "Yes")
- Keep branches under 4 conditions (if more, rethink structure)
- Always have an Else branch (never orphan contacts)

## Recipe: Missed Call Text-Back (STEP BY STEP — MEMORIZE)

**Trigger:** Inbound Call Status = Missed (or Voicemail)

**Actions:**
1. Wait 1 minute (optional, feels less robotic)
2. Send SMS: "Hi {{contact.first_name}}, sorry we missed your call! We'll get back to you shortly. Reply here if it's urgent."
3. Add tag: "missed-call-text-back-sent"
4. Create task: "Return call to {{contact.first_name}}" assigned to available rep
5. Wait 24 hours
6. If tag "replied" → end workflow
7. Else → send follow-up SMS or internal notification

**Why it matters:** This is one of the most-tested HighLevel workflows. It's the "Hello World" of GHL automation.

## Recipe: No-Show Nurture (STEP BY STEP — MEMORIZE)

**Trigger:** Appointment Status Changed to "No Show"

**Actions:**
1. Wait 1 hour
2. Send SMS: "Hey {{contact.first_name}}, we missed you at your {{appointment.title}} today. Everything okay?"
3. Wait 1 day
4. If no reply → Send email with rebooking link (trigger link)
5. Wait 2 days
6. If still no reply → Add tag "no-show-cold" and end
7. Else (replied or booked) → Remove from sequence

**Variant:** Some workflows include a manual call task at step 4 instead of rebooking link.

## Wait vs Wait Until

- **Wait [duration]** — wait X minutes/hours/days
  - Example: Wait 2 days
- **Wait Until [specific time]** — wait until a specific calendar point
  - Example: Wait until Monday 9am
  - Example: Wait until contact's birthday
  - Example: Wait until appointment time

**Use Wait Until for:**
- Business hour sending (don't SMS at 2am)
- Pre-appointment reminders (24 hours before appointment)
- Birthday/anniversary messages
- Specific-date launches

## Goal Events

A goal event in a workflow marks a contact as having achieved the workflow's purpose. Once a goal is met:
- Workflow can branch to a "goal path"
- Contact can be removed from the nurture sequence
- Prevents sending sequences to converted contacts

**Example:** "Lead" workflow has Goal = "Became Paying Member." Once they pay, they skip the rest of the nurture.

## Workflow Settings

- **Contact Re-entry:** Can the same contact enter again? (Once vs Multiple)
- **Stop on Reply:** Halt workflow if contact replies to SMS/email
- **Timezone:** Run in contact's timezone or account timezone
- **Business Hours Only:** Only send during defined hours

## Common Exam Patterns

1. "Send SMS 24 hours before appointment" → Wait Until [appointment time - 24h]
2. "Missed call triggers text" → Missed Call Text-Back recipe
3. "Send X if tag present, Y if not" → If/Else on tag
4. "Stop sending once they book" → Goal event = booking
5. "Don't send during overnight hours" → Business Hours Only setting

## Gotchas

- Workflow wait steps DO pause during off-hours if Business Hours enabled — plan for delays
- Tag loops: avoid "add tag X" that triggers workflow that "adds tag X" (infinite loop)
- Contact re-entry: if set to "once," contact who completes will not re-enter even if they should
- Test with test contacts BEFORE going live — shorten waits for testing, restore after
- Draft vs Published — a draft workflow does nothing

## Things to NEVER Confuse

- Trigger vs Action (trigger starts, action does)
- Wait vs Wait Until (duration vs specific time)
- Campaign vs Workflow (scheduled send vs event-driven)
- Goal event vs End of workflow (goal = early exit on success)

---

# SECTION 9: Agency Features

## Agency Dashboard vs Sub-Account Dashboard

- **Agency Dashboard** — where agency admins manage all sub-accounts
- **Sub-Account Dashboard** — where a client/user works inside a single business

## Snapshots

**What:** A template of a sub-account's configuration (workflows, pipelines, campaigns, forms, custom fields, etc.)

**Use case:** Build once, deploy to many clients.

### What Snapshots CAN include
- Workflows
- Pipelines & stages
- Forms & surveys
- Funnels & websites
- Email templates
- SMS templates
- Custom fields & values
- Calendars (config, not bookings)
- Trigger links
- Tags

### What Snapshots CANNOT include
- Contacts
- Conversations
- Payment processor credentials
- Phone numbers (provisioned per sub-account)
- Domain connections

### Deploying a Snapshot
- Apply to new or existing sub-account
- Existing sub-account: MAY overwrite or merge (verify behavior)
- New sub-account: clean deploy

## Multi-Sub-Account Access

- Agency users can access multiple sub-accounts
- Sub-account users typically access ONE sub-account
- Role determines permissions within sub-account

## User Roles

- **Agency Admin** — full agency access
- **Agency User** — limited agency access
- **Sub-Account Admin** — full access to one sub-account
- **Sub-Account User** — limited access (custom permissions)

## White-Label Touchpoints (MEMORIZE 5+)

| Touchpoint | What to White-Label |
|------------|---------------------|
| **Platform URL** | Custom domain (app.youragency.com instead of app.gohighlevel.com) |
| **Mobile app** | Custom branded mobile app (LeadConnector or custom) |
| **Login page** | Your logo, colors, branding |
| **Email sender** | Emails from your domain, not HighLevel's |
| **Help/Support URL** | Point to your support resources |
| **Marketplace** | Custom marketplace for your agency |
| **Desktop app** | Custom branded desktop widget (verify) |
| **Favicon** | Your favicon in browser tabs |
| **Agency logo** | Replace HighLevel branding throughout |
| **Invoice branding** | Your branding on invoices sent to clients |

**Exam tip:** Know at least 5 of these cold.

## Agency vs Sub-Account Users

| Aspect | Agency User | Sub-Account User |
|--------|-------------|------------------|
| Scope | All agency sub-accounts | One sub-account (usually) |
| Created by | Agency admin | Agency admin or sub-account admin |
| Billing access | Maybe | No |
| Snapshot access | Yes | No |
| White-label settings | Maybe | No |

## SaaS Mode

Allows agencies to resell HighLevel as their own platform with custom pricing, plans, and features per plan.

- Create plans (Starter, Pro, Enterprise)
- Assign features per plan (workflows, phone numbers, contacts limit, etc.)
- Bill clients directly
- Auto-provision on signup

## Common Exam Patterns

1. "Template a sub-account for reuse" → Snapshot
2. "Client sees HighLevel branding" → Enable white-label
3. "Agency user vs sub-account user" → Scope (many vs one)
4. "Resell HighLevel as own platform" → SaaS Mode
5. "Snapshot does NOT include..." → Contacts, conversations, credentials

## Gotchas

- Snapshot overwrite vs merge behavior — verify on your tier
- White-label requires custom domain setup (DNS)
- Mobile app branding requires Apple/Google developer accounts and separate fees
- SaaS Mode pricing is separate from agency base cost

## Things to NEVER Confuse

- Agency vs Sub-Account user (covered)
- Snapshot vs Template (snapshot = full config; template = single asset like email)
- SaaS Mode vs Agency Mode (SaaS = reselling; Agency = managing clients)

---

# SECTION 10: Compliance

## GDPR Essentials (EU)

**Who:** Anyone processing EU residents' personal data (even from the US)

**Key Requirements:**
- **Lawful basis** — consent, contract, legitimate interest, etc.
- **Right to access** — user can request their data
- **Right to erasure** — user can request deletion ("right to be forgotten")
- **Right to portability** — user can receive data in standard format
- **Breach notification** — notify authorities within 72 hours
- **DPA** — Data Processing Agreement with processors (HighLevel provides)
- **Privacy policy** — clear, accessible, explains data use
- **Consent** — must be freely given, specific, informed, unambiguous

**Practical HighLevel:**
- Use GDPR-compliant forms (explicit consent checkbox)
- Provide unsubscribe
- Support deletion requests (manually or via workflow)

## HIPAA + BAA (US Healthcare)

**HIPAA** — Health Insurance Portability and Accountability Act
- Applies to "covered entities" (healthcare providers, insurers) and their business associates
- Protects "PHI" (Protected Health Information)

**BAA** — Business Associate Agreement
- Contract between covered entity and service provider
- Service provider agrees to safeguard PHI
- REQUIRED if using HighLevel for PHI

**Important:** HighLevel offers HIPAA compliance ONLY on certain tiers with BAA signed. Default accounts are NOT HIPAA-compliant.

**Example:** BrightSmile Dental Clinic storing patient info — needs HIPAA-compliant HighLevel + BAA signed.

## A2P 10DLC (US SMS)

Covered in Section 2. Compliance framework for US SMS messaging via long codes.

**Penalties for non-compliance:**
- Messages blocked/filtered
- Account suspended by Twilio
- Potential carrier fines

## CAN-SPAM Act (US Email)

**Covered in Section 6.**

Key rules:
- Accurate From
- Honest Subject
- Physical address
- Unsubscribe link
- Honor unsubscribes within 10 business days
- Identify as ad if promotional

**Penalties:** Up to $50,120 per email in violation (verify current cap)

## California Consumer Privacy Act (CCPA)

**Who:** Businesses serving California residents meeting size thresholds

**Key Rights:**
- Right to know (what data is collected)
- Right to delete
- Right to opt out of sale of data
- Right to non-discrimination
- Right to correct (via CPRA amendment)

**"Do Not Sell My Personal Information"** link required if you sell data.

## Other Compliance Mentions

- **TCPA** (US) — Telephone Consumer Protection Act (covers robo-calls, SMS consent)
- **CASL** (Canada) — Anti-Spam Legislation (stricter than CAN-SPAM)
- **PIPEDA** (Canada) — Personal Information Protection
- **COPPA** (US) — Children's Online Privacy (under 13)

## Common Exam Patterns

1. "EU customer requests deletion" → GDPR right to erasure
2. "Dental clinic storing patient info" → HIPAA + BAA required
3. "US SMS not sending" → A2P 10DLC
4. "Email must include..." → Physical address + unsubscribe (CAN-SPAM)
5. "California resident data" → CCPA

## Gotchas

- HIPAA is NOT automatic — BAA must be signed
- A2P is US-only — don't confuse with international
- CCPA thresholds matter (not all businesses covered)
- GDPR applies even to non-EU businesses if serving EU residents
- "Consent" in GDPR is stricter than in US CAN-SPAM

## Things to NEVER Confuse

- GDPR vs CCPA (EU vs California; GDPR is stricter)
- HIPAA vs BAA (law vs contract enforcing law)
- CAN-SPAM vs CASL (US vs Canada; CASL stricter)
- A2P 10DLC vs general SMS consent (A2P is US regulation)

---

# Exam Day Checklist

## Night Before
- [ ] Light skim of Gotchas sections
- [ ] Re-read any flagged topics
- [ ] Confirm exam time and URL
- [ ] Test webcam if proctored
- [ ] Sleep 7+ hours

## Morning Of
- [ ] Eat a real meal
- [ ] Water nearby (if allowed)
- [ ] Close all other tabs/apps
- [ ] Quiet room, lock door
- [ ] Confirm stable internet
- [ ] Bathroom before start

## During Exam
- [ ] Read scenarios TWICE
- [ ] Flag unclear, move on, return at end
- [ ] Pace roughly 1 min per question
- [ ] Don't second-guess factual questions
- [ ] Leave no blanks — guess if must

## After Submit
- [ ] Capture your score
- [ ] If passed: celebrate, add to LinkedIn
- [ ] If missed: review which topics, retake plan

---

# Quick Reference Cheat Sheet

| Term | One-Line Definition |
|------|---------------------|
| Custom Field | Data attached to specific contact |
| Custom Value | Global variable, same everywhere |
| Tag | Manual segmentation label |
| Smart List | Dynamic filter on contacts |
| Round Robin | Rotates bookings among team |
| Collective | All listed people attend same booking |
| Pipeline | Visual kanban of deal stages |
| Workflow | Event-driven automation |
| Campaign | Scheduled/sequenced messages |
| Trigger Link | Trackable URL that fires actions |
| Funnel | Linear conversion path |
| Website | Multi-page informational site |
| Form | Single-page lead capture |
| Survey | Multi-page conditional questionnaire |
| Snapshot | Sub-account template |
| A2P 10DLC | US SMS compliance (long codes) |
| BAA | HIPAA service provider contract |
| Goal Event | Workflow exit on success |
| Wait Until | Wait for specific calendar time |
| Void Invoice | Cancel pre-payment |
| Refund | Return money post-payment |

---

# Final Notes

- Verify all figures (question count, time limit, passing score) at the official HighLevel certification page before exam day — they may change.
- This guide complements, not replaces, the Phase 4 lessons. If you haven't done the lessons and mock exam, do those first.
- When in doubt between two answers, eliminate what's definitely wrong, then pick based on "what a beginner wouldn't know."
- Trust your prep. You've built this stuff hands-on in Sunrise Wellness Studio — muscle memory matters.

Good luck.
