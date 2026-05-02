# Day 28: Mock Certification Exam & Gap Analysis

**Time Required:** 4 hours (2 hour exam + 2 hour gap review)
**Level:** Certification Ready

## Today's Mission

Final day. You will take a comprehensive mock certification exam (100 questions, timed), score yourself, identify knowledge gaps, and finalize your readiness for the real HighLevel Admin Certification. By end of today, you will know exactly where you stand and have a clear plan if you need additional study.

## How to Take This Exam

1. Block off 2 uninterrupted hours.
2. Use pen and paper to record answers (or a blank doc). Do NOT scroll ahead to the answer key.
3. Do not use notes or Google. This mirrors real exam conditions.
4. If you don't know an answer, mark it and come back. Do not leave blank.
5. Start a 120-minute timer before Q1.
6. After Q100, score using the Answer Key section.
7. Then spend 2 hours on the Gap Analysis Worksheet.

## Mock Exam Structure

**Format:** 100 questions, 2 hours
**Sections:**
- Section A: Agency Features (20 questions) - Day 24 topics
- Section B: Sub-Account Core (25 questions) - Day 25 topics
- Section C: Marketing, Sites, Automation (25 questions) - Day 26 topics
- Section D: Advanced Scenarios (15 questions) - Phase 2 integration topics
- Section E: API & Expert (15 questions) - Phase 3 topics

**Passing:** 80% (80/100)

---

# THE FULL MOCK EXAM

## Section A: Agency Features (Questions 1-20)

**Q1:** An agency wants to sell SMS services to their sub-accounts. Before any US sub-account can send SMS at scale, what registration must be completed?
a) SOC 2 Type II
b) A2P 10DLC brand and campaign registration
c) GDPR compliance certification
d) HIPAA Business Associate Agreement

**Q2:** When creating a SaaS-configurable plan at the agency level, which feature bundle is controlled by the SaaS settings?
a) DNS records
b) Rebill rates for SMS, email, phone, AI features
c) Individual contact records
d) Payment processor credentials

**Q3:** In which area does an agency admin manage Snapshots that can be pushed to new sub-accounts?
a) Sub-account > Settings > Imports
b) Agency > Account Snapshots
c) Sub-account > Marketing > Templates
d) Agency > Staff > Permissions

**Q4:** What is the minimum permission level required for a user to create a new sub-account in an agency?
a) Agency User
b) Agency Admin
c) Sub-Account Admin
d) Sub-Account User

**Q5:** A client complains their invoice shows "HighLevel" branding. As agency admin, which setting resolves this?
a) Enable white-label in Agency Settings -> Company Billing
b) Change DNS records only
c) Update sub-account Business Profile
d) Toggle "Hide Anchor Links" in Messaging Settings

**Q6:** Which of the following is NOT included by default in a Snapshot?
a) Workflows
b) Custom fields
c) Contacts
d) Funnels

**Q7:** A sub-account has used up its monthly SMS rebill credits. What happens next?
a) SMS sending pauses until the next billing cycle
b) SMS sends fail silently
c) Overage is billed automatically if Auto-Recharge is enabled
d) Sub-account is suspended

**Q8:** To rebill Twilio SMS usage with markup, where do you configure the markup percentage?
a) Twilio dashboard
b) Agency View > Settings > Company Billing > Rebilling
c) Sub-account > Phone Numbers
d) Stripe dashboard

**Q9:** Which document type lives at the agency level and is applied to ALL sub-accounts automatically?
a) Privacy Policy link
b) Sub-account terms of service
c) Agency-level Marketplace apps installed globally
d) Contact records

**Q10:** What does the Marketplace at the agency level allow?
a) Install custom integrations and distribute to sub-accounts
b) Sell physical products
c) Manage DNS records
d) Configure Twilio

**Q11:** A white-label domain requires what three DNS record types at minimum?
a) A, CNAME, TXT
b) MX, NS, SRV
c) A, SOA, PTR
d) AAAA, DMARC, CAA

**Q12:** The Company Billing section at the agency level controls:
a) How the agency is charged by HighLevel AND how clients are rebilled
b) Only how clients pay
c) Only Twilio billing
d) Only AI feature billing

**Q13:** Which best describes a SaaS Mode plan?
a) A free trial
b) A recurring Stripe subscription tied to a sub-account with usage limits and rebill rates
c) A workflow template
d) An email drip

**Q14:** An agency staff member needs to access a specific sub-account without appearing in that sub-account's user list. What feature supports this?
a) Switch User
b) Impersonate / Sign in as
c) Support Mode toggle (Agency-only view)
d) Shared Inbox

**Q15:** Which is true about LC Phone (LeadConnector Phone)?
a) It replaces Twilio entirely with no configuration
b) It is HighLevel's managed telephony layer; some agencies use LC Phone, others self-provision Twilio
c) It only supports email
d) It is only available in EU regions

**Q16:** When a Snapshot is pushed to an existing sub-account, by default it:
a) Deletes existing assets
b) Overwrites everything
c) Adds or updates assets without deleting existing data
d) Only works on brand-new sub-accounts

**Q17:** Which of the following CANNOT be set at the agency level and inherited by sub-accounts?
a) Reseller email branding
b) Default Snapshot
c) Individual contact notes
d) Marketplace apps

**Q18:** What is a Reseller account in HighLevel?
a) A sub-account with purchasing power
b) An agency that resells HighLevel to its own clients under a white-label brand
c) A third-party Twilio vendor
d) A contact tagged "Reseller"

**Q19:** An agency wants to lock specific features (e.g., Memberships) behind a paid plan upgrade. Which configuration supports this?
a) SaaS Mode plan feature restrictions
b) Staff permissions
c) Sub-account tags
d) Custom fields

**Q20:** What is the best practice when creating a new Snapshot intended for multiple client verticals?
a) Make one master Snapshot with everything
b) Create vertical-specific Snapshots (e.g., Dental, Real Estate, Fitness) to keep them lean and relevant
c) Clone the same Snapshot and rename it
d) Store all assets in a single workflow

---

## Section B: Sub-Account Core (Questions 21-45)

**Q21:** Which of the three calendar types is best suited for a yoga class with a max capacity of 15?
a) Basic
b) Round Robin
c) Class Booking
d) Collective

**Q22:** In a Round Robin calendar with 3 team members, how are new bookings distributed?
a) Always to the first team member
b) Evenly distributed by availability and rotation logic
c) Only to the member who booked most recently
d) Randomly

**Q23:** A user reports their appointment reminder SMS was never sent. Which is the FIRST place to check?
a) The appointment's calendar settings -> Notifications tab
b) Contact's DND status
c) Workflow logs
d) Twilio balance

**Q24:** What is the difference between a Tag and a Custom Field?
a) Tags are for binary labels; custom fields store structured data (text, date, number, etc.)
b) Tags are agency-level; custom fields are sub-account-level
c) They are identical
d) Tags can only be applied manually; custom fields auto-populate

**Q25:** A Smart List filter "Tag is ANY of [trial, lead-warm]" returns:
a) Only contacts with BOTH tags
b) Contacts with either trial OR lead-warm tag
c) All contacts
d) Contacts with neither tag

**Q26:** To merge two duplicate contacts, navigate to:
a) Settings -> Imports
b) The contact's profile -> More -> Merge
c) Opportunities -> Merge
d) Cannot merge, must delete

**Q27:** Where are custom field folders useful?
a) They organize custom fields into logical groups for easier contact record management
b) They do not exist in GHL
c) They control permissions
d) They replace tags

**Q28:** A pipeline opportunity's "Monetary Value" field is used in:
a) Reporting (revenue forecasts) and some workflow calculations
b) Contact photo display
c) SMS templates only
d) Nothing; it is cosmetic

**Q29:** When an opportunity stage changes, which workflow trigger fires?
a) Contact DND Changed
b) Pipeline Stage Changed (or Opportunity Status Changed)
c) Form Submitted
d) Appointment Booked

**Q30:** A booking widget should be embedded on a non-GHL website (WordPress). Which approach is standard?
a) Only share the booking URL
b) Copy the embed iframe from the calendar's Embed tab
c) FTP upload
d) Not possible

**Q31:** What is a "neverbounce" equivalent inside GHL for email list health?
a) Email Validation (built-in or via third-party)
b) Tags
c) Opportunities
d) Snapshots

**Q32:** A contact has DND status ON for SMS. Sending them an SMS via workflow will:
a) Send successfully
b) Fail silently or be skipped (DND is respected)
c) Send but be marked spam
d) Trigger an error notification to admin

**Q33:** Which of these is NOT a valid Calendar setting?
a) Buffer time before/after
b) Minimum scheduling notice
c) Daily booking limit
d) Number of tags allowed per appointment

**Q34:** Which contact merge scenario preserves the MOST data?
a) Keep oldest contact as primary
b) Keep contact with most custom field data as primary
c) Delete both and re-import
d) Hand merge via CSV

**Q35:** A user cannot see the Opportunities tab at all. Likely cause?
a) They haven't logged in today
b) Their user role/permissions exclude Opportunities
c) The feature is deprecated
d) Sub-account is suspended

**Q36:** Which best describes a Smart List vs a Static List?
a) Smart Lists update dynamically as contacts match criteria; Static Lists are manually curated
b) Smart Lists are for email; Static Lists are for SMS
c) There is no difference
d) Smart Lists require API access

**Q37:** The Bulk Actions menu for contacts can do all EXCEPT:
a) Add tags
b) Send an email campaign
c) Change ownership
d) Alter sub-account billing

**Q38:** What is the correct order to set up a Class Booking calendar?
a) Create calendar -> set capacity -> define class schedule slots -> set notifications
b) Create form -> create calendar
c) Assign team member -> create calendar
d) Write workflow -> create calendar

**Q39:** A contact's Source field is auto-populated from:
a) The URL parameter or form/campaign that created the contact
b) Manual entry only
c) Tags
d) Pipeline stage

**Q40:** Which is the BEST use of contact segmentation for a fitness studio?
a) One big list
b) Separate Smart Lists for Leads, Trials, Active Members, Cancelled Members, Churn Risk
c) Tagging everyone "customer"
d) Custom fields only

**Q41:** In Conversations (Inbox), a "conversation" includes:
a) Only SMS
b) SMS + Email + Webchat + FB/IG DMs + GMB messages (unified view)
c) Email only
d) Phone calls only

**Q42:** To assign a specific user as the owner of incoming conversations from a particular lead source, use:
a) Conversation Assignment rules / workflows
b) Billing settings
c) Custom values
d) Not possible

**Q43:** What is the maximum file size for an image in a GHL email campaign (approximate)?
a) 10 MB per image (vary, generally keep under 1MB for deliverability)
b) 500 GB
c) 5 KB
d) Unlimited

**Q44:** An appointment No-Show status is triggered:
a) Automatically based on calendar activity
b) Manually by a staff member or via workflow automation
c) When the contact doesn't respond to SMS
d) Never

**Q45:** To configure a calendar's team members and their availability, you:
a) Add each team member with their own working hours in the calendar settings
b) Force everyone to the same schedule
c) Use custom fields
d) Use tags

---

## Section C: Marketing, Sites, Automation (Questions 46-70)

**Q46:** Which funnel page element captures lead data and triggers workflows?
a) A Form element or an Order Form
b) A text block
c) A video
d) A section background

**Q47:** Trigger Links are best used for:
a) Tracking clicks and segmenting contacts based on their interest
b) Replacing URLs permanently
c) Avoiding Twilio fees
d) Custom fields

**Q48:** A workflow's "Wait" step based on a custom field Date requires:
a) The date field to be populated, otherwise the wait may stall
b) Nothing special; it always works
c) API access
d) Only paid plans

**Q49:** To conditionally branch a workflow based on a tag, use:
a) If/Else condition
b) Send Email
c) Remove Tag
d) Wait step

**Q50:** A survey with conditional logic can:
a) Only show fixed questions
b) Show/hide questions based on previous answers and route submitters differently
c) Replace calendars
d) Only be used for NPS

**Q51:** The difference between a Funnel and a Website in GHL:
a) Funnels are linear multi-step conversion paths; Websites are multi-page site structures
b) They are identical
c) Funnels cost extra
d) Websites cannot use forms

**Q52:** A workflow trigger "Form Submitted" can be filtered by:
a) Specific form, tags, or field values
b) Only tags
c) Only timezone
d) Not filterable

**Q53:** Which email sender type allows the best deliverability for cold outreach?
a) HighLevel default sender
b) A verified custom domain with SPF, DKIM, and DMARC set correctly
c) Free Gmail
d) No-reply@localhost

**Q54:** A/B split in a workflow is used for:
a) Testing two different paths or content variants
b) Saving API calls
c) Billing
d) Nothing

**Q55:** Which workflow action type is REQUIRED to update a custom field dynamically?
a) Add/Remove Tag
b) Update Contact Field (Set Custom Field Value)
c) Send Email
d) Wait

**Q56:** To prevent a workflow from running more than once per contact:
a) Set "Allow Multiple" to No or add a filter for the unique state
b) Delete the workflow after first run
c) Not possible
d) Require API

**Q57:** An email campaign's "Resend to Non-Openers" feature:
a) Sends the same email 24-72 hours later to contacts who did not open
b) Is not available
c) Sends SMS instead
d) Changes subject lines automatically

**Q58:** Which is the correct use of Custom Values in an email template?
a) `{{custom_values.business_name}}`
b) `[business_name]`
c) `<business_name>`
d) `$business_name$`

**Q59:** A Funnel Order Bump appears:
a) On the checkout step as an optional add-on
b) After purchase only
c) Before the form
d) In the email

**Q60:** An Upsell page in a funnel runs after:
a) The initial purchase is completed
b) Before checkout
c) On optin only
d) Never

**Q61:** What is the purpose of a "1-click upsell"?
a) Allow customer to add a product without re-entering payment info
b) Discount existing orders
c) Refund a purchase
d) Change a calendar

**Q62:** A workflow triggered by "Tag Added" runs:
a) Every time that specific tag is added, including re-adds (configurable)
b) Only once ever
c) Never
d) On calendar bookings

**Q63:** To split-test a funnel page:
a) Use the funnel's built-in Split Test feature (two variants, traffic divided, stats compared)
b) Manually duplicate pages
c) Use Google Optimize only
d) Not supported

**Q64:** A "membership" product inside Memberships module delivers:
a) Gated content (courses, community) behind login
b) Physical products
c) Email campaigns
d) SMS only

**Q65:** Email unsubscribe handling is:
a) Automatic; unsubscribed contacts are flagged and future marketing emails are blocked
b) Manual only
c) Ignored
d) Requires API

**Q66:** Which best describes a Drip vs Campaign in Marketing?
a) Drip is a time-delayed sequence; Campaign can be broadcast (immediate send)
b) No difference
c) Drip is paid
d) Campaign is SMS only

**Q67:** To preview an email on mobile before sending:
a) Use the built-in mobile preview in the email editor
b) Send to yourself only
c) Not possible
d) Use external service

**Q68:** A website page can embed a calendar by:
a) Dropping the calendar widget/embed element onto the page
b) Writing raw HTML only
c) Impossible without API
d) Only via funnel

**Q69:** Forms can send data to external systems via:
a) Webhook action in an attached workflow (and direct webhook from Form settings)
b) FTP
c) Email only
d) Not possible

**Q70:** The best practice for a high-converting landing page is:
a) One clear CTA, focused headline, proof elements, minimal distractions
b) 20 buttons on the page
c) Video that autoplays with sound
d) Pop-up on every scroll

---

## Section D: Advanced Scenarios (Questions 71-85)

**Q71:** A client's workflow is sending duplicate SMS to contacts. Most likely cause?
a) Two workflows triggered by similar events both send SMS
b) Twilio glitch
c) Contact imported twice
d) Tag is stuck

**Q72:** A fitness studio wants to auto-tag contacts who book 3+ classes in a month. Best approach?
a) Workflow counting appointment bookings using a numeric custom field
b) Manual review
c) Not possible
d) Pipeline stages

**Q73:** A dental practice wants appointment reminders to vary by procedure type. Best approach?
a) Separate calendars per procedure, each with its own reminder templates
b) One big calendar with long generic messages
c) Manual send
d) Tag-based dispatch only

**Q74:** Corporate leads should bypass the standard nurture and go straight to a sales rep. Best workflow design?
a) Trigger on form submission, If/Else on "corporate" tag, assign to user and create task
b) Same as individuals
c) Use a separate sub-account
d) Manual forwarding

**Q75:** A contact books a call but never replies to confirmation SMS. After 1 hour, the workflow should:
a) Send an alternate channel message (email) and flag for manual followup
b) Cancel the appointment automatically
c) Do nothing
d) Delete the contact

**Q76:** A membership onboarding workflow has 30+ steps. Best practice?
a) Break into smaller, modular sub-workflows (Onboarding Week 1, Week 2, Month 2) called via "Go to workflow"
b) Keep it all in one giant workflow
c) Use only tags
d) Use only email

**Q77:** A contact is tagged both `member-active` and `member-cancelled` due to a glitch. Impact?
a) Smart Lists and workflows may behave inconsistently; clean up data immediately
b) No impact
c) Automatic fix
d) Nothing to do

**Q78:** A review request workflow should NOT send to contacts who:
a) Already submitted a review OR are tagged DND
b) All contacts should get it
c) Only new contacts
d) Only old contacts

**Q79:** An invoice is sent, marked paid, but the workflow tagging "paid" never runs. First check?
a) Workflow trigger: is it listening for Invoice Paid and is the filter correct?
b) Twilio settings
c) Calendar
d) Business profile

**Q80:** A payment workflow should kick off after Stripe charges successfully. Correct trigger?
a) Order Form Submission OR Payment Received
b) Form Submitted (generic)
c) Appointment Booked
d) Contact Created

**Q81:** A corporate contract (B2B) spans 12 months. Best way to track renewal in GHL?
a) Custom field "Contract End Date" + workflow Date trigger to send renewal workflow 60 days prior
b) Manual calendar reminders
c) Ignore
d) Google Calendar

**Q82:** A pipeline's stage-change trigger fires regardless of direction. To only fire when moving forward:
a) Add a filter checking previous stage OR use opportunity status logic
b) Not possible
c) Always fires backward
d) Delete the pipeline

**Q83:** An A/B test shows 52% vs 48% for variant A vs B on 150 visitors. Decision?
a) Not statistically significant yet, keep test running
b) Declare A the winner
c) Declare B the winner
d) Stop all tests

**Q84:** A multi-location wellness brand with 3 studios. Best GHL structure?
a) Separate sub-accounts per location (managed by one agency), or use tags + custom fields in one sub-account if simpler
b) One sub-account with no segmentation
c) Only an agency account
d) Not possible

**Q85:** A workflow needs to branch based on whether a contact's Primary Goal custom field is "Weight Loss" or "Stress Management" or other. Best element?
a) If/Else with conditions on the custom field value
b) Multiple copies of the workflow
c) Manual send
d) Tag-based only

---

## Section E: API & Expert (Questions 86-100)

**Q86:** The HighLevel v2 API base URL is:
a) https://services.leadconnectorhq.com
b) https://api.highlevel.com/v1
c) https://rest.gohighlevel.com/v1
d) https://api.stripe.com

**Q87:** To authenticate with the HighLevel v2 API:
a) Bearer token (OAuth 2.0 or Agency/Location API key) + Version header
b) Basic auth with email
c) Cookie only
d) No auth required

**Q88:** Which header is REQUIRED on v2 API requests?
a) Version: 2021-07-28 (or current supported date)
b) X-Client-ID
c) User-Agent: HighLevel
d) X-Stripe-Key

**Q89:** A workflow's Webhook action sends data to:
a) A URL you specify, with a JSON payload, method POST (configurable)
b) Email only
c) Fixed HighLevel servers
d) SMS gateway

**Q90:** A webhook received from GHL must be verified how?
a) Via a shared secret or signature header the receiver checks
b) No verification needed
c) Only via SSL
d) Basic auth

**Q91:** Rate limiting on the HighLevel API:
a) Exists; vary by endpoint - design retry logic with backoff
b) Unlimited
c) 1 request per day
d) Only on contacts endpoint

**Q92:** To search contacts by custom field value via API, you typically:
a) Use the Contacts Search endpoint with a query or filter payload
b) Loop through all contacts
c) Not possible
d) Use Stripe

**Q93:** When creating a contact via API, the minimum required fields include:
a) locationId plus at least one of email/phone
b) Only firstName
c) Full SSN
d) Password

**Q94:** OAuth 2.0 in HighLevel is used for:
a) Marketplace apps and multi-tenant integrations
b) Single-user scripts only
c) Billing only
d) Not supported

**Q95:** A Python requests.post call to create a contact should include:
a) headers with Authorization, Version, Content-Type: application/json and a JSON body
b) Only URL
c) XML body
d) Form-encoded only

**Q96:** A common error "401 Unauthorized" when calling the API means:
a) The token is missing, expired, or invalid
b) Rate limit exceeded
c) Server is down
d) Contact not found

**Q97:** A "429 Too Many Requests" response indicates:
a) Rate limit hit; back off and retry with exponential backoff
b) Authentication failure
c) Invalid JSON
d) Contact exists

**Q98:** To bulk-update 10,000 contacts with a custom field value, the best pattern is:
a) Paginated GET + concurrent PUT requests with rate-limit-aware throttling and idempotency
b) One giant request
c) Manual
d) Loop without sleep

**Q99:** Marketplace apps distributed to sub-accounts can:
a) Install custom features, workflows, and UI surfaces scoped to each sub-account
b) Only change the logo
c) Edit DNS
d) Nothing

**Q100:** The BEST overall indicator that your HighLevel build is production-ready:
a) You can walk a new client through a complete end-to-end journey and every workflow, template, and integration has been tested with real data
b) The workflows look pretty in the editor
c) You have more than 10 tags
d) The dashboard loads fast

---

# END OF EXAM

Stop your timer. Record total time taken.

---

# ANSWER KEY

## Quick Answer Key (Letters Only)

Section A:
1-b, 2-b, 3-b, 4-b, 5-a, 6-c, 7-c, 8-b, 9-c, 10-a, 11-a, 12-a, 13-b, 14-b, 15-b, 16-c, 17-c, 18-b, 19-a, 20-b

Section B:
21-c, 22-b, 23-a, 24-a, 25-b, 26-b, 27-a, 28-a, 29-b, 30-b, 31-a, 32-b, 33-d, 34-b, 35-b, 36-a, 37-d, 38-a, 39-a, 40-b, 41-b, 42-a, 43-a, 44-b, 45-a

Section C:
46-a, 47-a, 48-a, 49-a, 50-b, 51-a, 52-a, 53-b, 54-a, 55-b, 56-a, 57-a, 58-a, 59-a, 60-a, 61-a, 62-a, 63-a, 64-a, 65-a, 66-a, 67-a, 68-a, 69-a, 70-a

Section D:
71-a, 72-a, 73-a, 74-a, 75-a, 76-a, 77-a, 78-a, 79-a, 80-a, 81-a, 82-a, 83-a, 84-a, 85-a

Section E:
86-a, 87-a, 88-a, 89-a, 90-a, 91-a, 92-a, 93-a, 94-a, 95-a, 96-a, 97-a, 98-a, 99-a, 100-a

---

## Detailed Explanations

### Section A: Agency Features

**Q1 - b)** A2P 10DLC is the US carrier-mandated registration for application-to-person messaging. Without a registered brand and campaign, sub-accounts face heavy throttling and deliverability failures. SOC 2, GDPR, and HIPAA are important but unrelated to SMS ability.

**Q2 - b)** SaaS Mode plans specifically control rebill rates on the metered services (SMS, email, phone, AI). DNS records, contacts, and processor credentials are not tied to plan tiers.

**Q3 - b)** Agency -> Account Snapshots is where snapshots live and are pushed. Imports are for contact CSVs, Templates are message templates, Staff is user management.

**Q4 - b)** Only Agency Admin can create sub-accounts. Agency User has restricted scope; sub-account roles cannot create peers.

**Q5 - a)** White-label is toggled in Agency Settings -> Company Billing and associated branding locations. DNS alone does not change invoice branding; sub-account Business Profile does not govern agency-issued invoices.

**Q6 - c)** Snapshots package assets (workflows, custom fields, funnels, pipelines, calendars, forms). They do NOT carry contacts; contacts are user data, not configuration.

**Q7 - c)** Auto-Recharge in agency billing handles overages without interruption. Without it, SMS can pause.

**Q8 - b)** Company Billing > Rebilling controls markup percentages. Twilio and Stripe dashboards are separate systems.

**Q9 - c)** Marketplace apps installed at the agency level can be distributed globally. Privacy policy links and contact records are sub-account specific.

**Q10 - a)** Agency Marketplace is where custom integrations live and get distributed.

**Q11 - a)** A, CNAME, TXT are the minimum. MX/NS/SRV are unrelated to white-label domain verification; AAAA/DMARC/CAA are supplemental.

**Q12 - a)** Company Billing governs both how the agency pays HighLevel and how clients are rebilled.

**Q13 - b)** SaaS Mode plan = a recurring Stripe subscription tied to a sub-account with usage limits and rebill configuration.

**Q14 - b)** "Sign in as" / impersonation is the standard feature. Switch User is for your own accounts, not other clients.

**Q15 - b)** LC Phone is HighLevel's managed telephony layer. Some agencies use it; others self-provision Twilio.

**Q16 - c)** Snapshots are additive/updating by default, not destructive. They do NOT delete existing data.

**Q17 - c)** Contact notes are sub-account-only and cannot be inherited from agency.

**Q18 - b)** A Reseller is a white-label agency selling HighLevel under its own brand.

**Q19 - a)** SaaS Mode plan feature restrictions enable tier-gated features like Memberships.

**Q20 - b)** Vertical-specific snapshots are best practice. One giant Snapshot is bloated and irrelevant to most clients.

### Section B: Sub-Account Core

**Q21 - c)** Class Booking is designed for capped group sessions. Basic is 1:1, Round Robin rotates across team members.

**Q22 - b)** Round Robin distributes by availability and rotation logic, not purely randomly or first-come.

**Q23 - a)** Always check the calendar's Notifications tab FIRST; that's where the appointment reminder is configured. Then check DND and workflow logs.

**Q24 - a)** Tags = binary labels. Custom Fields = structured data with types.

**Q25 - b)** "Any of" is OR logic.

**Q26 - b)** Merge is accessed from the contact profile -> More menu.

**Q27 - a)** Folders group custom fields. Fields in a folder show together on the contact record.

**Q28 - a)** Monetary Value drives revenue forecasts and can drive calculations in workflows.

**Q29 - b)** Pipeline Stage Changed is the exact trigger.

**Q30 - b)** Copy the iframe embed from the calendar's Embed tab - standard approach.

**Q31 - a)** Email Validation services clean lists of bad addresses.

**Q32 - b)** DND causes the send to be skipped silently. That is the intended behavior.

**Q33 - d)** Calendars don't limit tags per appointment.

**Q34 - b)** Keeping the record with most field data as primary preserves the most info.

**Q35 - b)** User role permissions control tab visibility.

**Q36 - a)** Smart = dynamic; Static = manual.

**Q37 - d)** Bulk actions are contact-level; billing is not bulk-mutable from here.

**Q38 - a)** Create calendar, set capacity, define slots, set notifications - correct order.

**Q39 - a)** Source is auto-populated by UTM/campaign/URL parameters.

**Q40 - b)** Multi-segment Smart Lists provide actionable segmentation.

**Q41 - b)** Conversations unify SMS, email, webchat, FB/IG DMs, GMB messages.

**Q42 - a)** Conversation assignment rules or workflows handle ownership routing.

**Q43 - a)** Varies by plan; rule of thumb is to keep images under 1 MB for deliverability. Actual cap is around 10 MB.

**Q44 - b)** No-Show is a manual or automated status change; not automatic from calendar alone.

**Q45 - a)** Each team member has their own hours within the calendar settings.

### Section C: Marketing, Sites, Automation

**Q46 - a)** Forms and Order Forms capture data and trigger workflows.

**Q47 - a)** Trigger Links track clicks and allow tag-based segmentation.

**Q48 - a)** Wait-until-date needs the field populated; else the wait may stall indefinitely.

**Q49 - a)** If/Else is the branching construct.

**Q50 - b)** Conditional logic in surveys = dynamic question flow + routing.

**Q51 - a)** Funnels are linear conversion paths; Websites are multi-page structures.

**Q52 - a)** You can filter Form Submitted trigger by form, tags, field values.

**Q53 - b)** Custom domain with SPF/DKIM/DMARC = best deliverability.

**Q54 - a)** A/B split tests two variants.

**Q55 - b)** Update Contact Field action sets custom field values.

**Q56 - a)** Allow Multiple = No or add a filter.

**Q57 - a)** Resend to non-openers re-sends the email after a delay.

**Q58 - a)** `{{custom_values.name}}` is the correct Liquid-style syntax.

**Q59 - a)** Order Bump appears on checkout.

**Q60 - a)** Upsell runs after initial purchase.

**Q61 - a)** 1-click upsell = no re-enter payment.

**Q62 - a)** Tag Added trigger runs each time the tag is added (configurable).

**Q63 - a)** Funnel split test feature is built-in.

**Q64 - a)** Membership products deliver gated content.

**Q65 - a)** Unsubscribe is auto-handled; contacts are flagged.

**Q66 - a)** Drip = time-delayed; Campaign = broadcast.

**Q67 - a)** Built-in mobile preview exists.

**Q68 - a)** Calendar embed widget is available on page builders.

**Q69 - a)** Webhook action in workflow (or direct webhook from form settings).

**Q70 - a)** Single clear CTA, focused headline, proof, minimal distraction.

### Section D: Advanced Scenarios

**Q71 - a)** Two workflows firing same action = classic duplicate-send cause.

**Q72 - a)** Numeric custom field counter incremented per booking.

**Q73 - a)** Separate calendars per procedure with tailored notifications.

**Q74 - a)** Trigger on form, If/Else on corporate tag, assign + task.

**Q75 - a)** Multi-channel fallback + manual flag is best practice.

**Q76 - a)** Modular sub-workflows keep automation maintainable.

**Q77 - a)** Conflicting tags break Smart Lists and workflow logic; clean up immediately.

**Q78 - a)** Exclude already-reviewed and DND contacts.

**Q79 - a)** Check trigger first - correct trigger event and filters.

**Q80 - a)** Order Form Submission or Payment Received.

**Q81 - a)** Date custom field + Date trigger workflow 60 days prior.

**Q82 - a)** Filter on previous stage or use opportunity status logic.

**Q83 - a)** 150 visitors, 4-point spread = not stat significant. Keep running.

**Q84 - a)** Separate sub-accounts per location or unified with segmentation if simpler.

**Q85 - a)** If/Else on custom field value.

### Section E: API & Expert

**Q86 - a)** services.leadconnectorhq.com is v2.

**Q87 - a)** Bearer token + Version header.

**Q88 - a)** Version header is required.

**Q89 - a)** Webhook action POSTs JSON to your URL.

**Q90 - a)** Shared secret or signature header verification.

**Q91 - a)** Rate limits exist; design retry + backoff.

**Q92 - a)** Contacts Search endpoint supports filter payloads.

**Q93 - a)** locationId + (email or phone).

**Q94 - a)** OAuth 2.0 is for marketplace apps and multi-tenant integrations.

**Q95 - a)** headers with Authorization, Version, Content-Type: application/json + JSON body.

**Q96 - a)** 401 = token invalid/missing/expired.

**Q97 - a)** 429 = rate limit; exponential backoff.

**Q98 - a)** Paginated fetch + throttled concurrent updates + idempotency.

**Q99 - a)** Marketplace apps scope features to each sub-account.

**Q100 - a)** End-to-end tested with real data = production-ready truth.

---

## Common Wrong-Answer Traps

A few distractors to watch for:

- **Q1:** "HIPAA BAA" is tempting because healthcare clients need it, but it is NOT the SMS prerequisite.
- **Q6:** "Custom fields" as excluded from Snapshots is wrong - they ARE included. Contacts are the exception.
- **Q16:** "Overwrites everything" is a common fear, but snapshots are additive by default.
- **Q23:** Checking Twilio balance is tempting but comes AFTER the calendar notification config.
- **Q32:** "Send but mark spam" is a tempting distractor; GHL simply skips the send.
- **Q71:** "Twilio glitch" is rarely the cause of duplicates; almost always it's overlapping workflows.
- **Q83:** "Declare A the winner" is the impatient wrong answer at 52/48 on 150 visitors.
- **Q96 vs Q97:** 401 is auth; 429 is rate. Don't mix them up.

---

## Scoring Interpretation

| Score | Status | Next Step |
|-------|--------|-----------|
| 90-100% | Exam Ready | Schedule the real HighLevel Admin exam this week |
| 80-89% | Very Close | Review missed topics, retake mock in 3 days, then exam |
| 70-79% | Need More Study | 1-2 weeks of targeted review before exam |
| <70% | Not Ready | Full re-review of Phase 4, rebuild capstone, then retake mock |

---

## Gap Analysis Worksheet

After scoring, fill this out. Do not skip - this is where the real learning happens.

**Total Score:** ____ / 100 = ____%

**Time Taken:** ____ minutes (target: under 120)

**Section Scores:**
- Section A (Agency): ____ / 20
- Section B (Sub-Account Core): ____ / 25
- Section C (Marketing/Sites/Automation): ____ / 25
- Section D (Advanced Scenarios): ____ / 15
- Section E (API & Expert): ____ / 15

**Weakest Section:** __________________

**Specific Topics I Got Wrong:**
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________
5. _________________________________
(continue as needed)

**For each wrong answer, journal:**

| Question # | What was I confused about? | Course Day that covers it | Redo exercise OR re-read? |
|------------|----------------------------|---------------------------|---------------------------|
| | | | |
| | | | |
| | | | |

**Patterns I notice in my wrong answers:**
- ________________________________
- ________________________________
- ________________________________

---

## Personalized Study Plan Generator

Based on your gaps, follow the plan that matches your score band.

### If you scored 90-100%

**You're ready.** Use these 2 days to:
- Day 1: Skim the official HighLevel Certifications Program material (Michael Johnson curriculum) to align with exam phrasing.
- Day 2: Schedule the real exam. Take it within 7 days while the material is fresh.

### If you scored 80-89%

**2-day polish plan:**
- Day 1 AM: Re-read lessons covering your wrong answers.
- Day 1 PM: Redo the single worst-section exercises (from Days 24-26 or Phase 3).
- Day 2: Retake this mock exam (try to push 90+). Then schedule real exam.

### If you scored 70-79%

**2-week targeted review:**
- Days 1-3: Re-read your weakest phase's lessons in full.
- Days 4-7: Redo practical exercises in weak areas (hands-on in the sub-account).
- Days 8-10: Take mock exam again.
- Days 11-14: If 85+ on retake, schedule real exam. Otherwise extend another week.

### If you scored <70%

**3-4 week rebuild:**
- Week 1: Revisit Phase 1 (Days 1-10) actively, taking notes.
- Week 2: Revisit Phase 2 (Days 11-17) and rebuild any weak systems.
- Week 3: Redo Capstone (Day 27) from scratch. Score 40+/50.
- Week 4: Retake mock exam. Target 85+ before scheduling the real exam.

---

## Final Readiness Checklist

Work through every item. Check each only when honestly yes.

- [ ] Scored 80%+ on mock exam
- [ ] Completed Capstone project (minimum 40/50)
- [ ] Can explain all 3 calendar types (Basic, Round Robin, Class Booking) without looking
- [ ] Can list all workflow trigger categories (Contact, Opportunity, Appointment, Conversation, Payment, Form, Custom/Webhook, Date/Time)
- [ ] Can diagram the customer journey through GHL (lead -> contact -> opportunity -> customer -> member)
- [ ] Have studied official Michael Johnson cert materials
- [ ] Comfortable with both UI navigation AND API concepts
- [ ] Built something for my own business/portfolio
- [ ] Can articulate the difference between Tags, Custom Fields, Custom Values
- [ ] Know where to find: Snapshots, SaaS Mode config, A2P 10DLC registration, Company Billing, Marketplace
- [ ] Have recovered from at least one broken workflow during build (debugging skill)
- [ ] Can write a basic Python script that creates or updates a contact via API

---

## If You're Ready - Registering for the Real Exam

Navigate to HighLevel's certification program portal (typically linked from your agency dashboard under Certifications, or through certifications.gohighlevel.com).

**Expect:**
- Official Admin Certification exam fee (check current pricing)
- Time-limited exam window (typically 2 hours)
- Webcam proctoring may be required
- Retake policy: usually a 7-14 day wait and a retake fee
- Certificate issued upon passing 80%+
- Ability to add certification to LinkedIn, resume, agency proposals

**Pre-exam checklist:**
- [ ] Stable internet
- [ ] Quiet distraction-free room
- [ ] ID ready if proctored
- [ ] Water and a snack
- [ ] Logged into test environment ahead of time

---

## Congratulations & Next Steps

You have completed 28 days of GoHighLevel mastery. That is roughly 70-100 hours of deliberate practice, 11,000+ lines of structured course content, and three fully-built practice businesses.

**Where to go next:**

1. **Take the real certification exam.** The sooner, the fresher.
2. **Build portfolio with real client work.** One paid engagement is worth 10 tutorials.
3. **Join the HighLevel community.** Facebook groups, official Slack, Twitter/X communities. Answer others' questions - teaching cements mastery.
4. **Specialize.** Pick a vertical (dental, real estate, fitness, agencies) or a layer (white-label SaaS, custom API integrations, membership sites). Depth beats breadth after this point.
5. **Keep learning.** HighLevel ships features monthly. Subscribe to the changelog. Dedicate 1 hour a week to exploring new features before clients ask.

**Beyond HighLevel:**
- API and automation skills transfer to any platform (Zapier, Make, n8n, custom backends).
- You now understand how marketing, sales, and ops systems connect - that is valuable regardless of the tool.
- Your capstone is a portfolio artifact. Package screenshots and outcomes into a case study.

---

## Thank You & Final Reflection

Take 15 minutes before closing this file to journal:

**1. What surprised you over the 28 days?**


**2. Which day had the biggest "aha!" moment?**


**3. What system will you build first for a real business?**


**4. Who will you share this knowledge with?**


**5. Commit: the single next action you will take this week.**


---

**You finished. Now go ship something real.**

Sunrise Wellness Studio. BrightSmile Dental. Elevate Digital Agency. Harmony Health Hub. These are fictional - but your next build will not be. Go.
