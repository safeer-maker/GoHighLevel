# Day 26: Admin Certification Review - Marketing, Sites & Automation

**Time Required:** 3-4 hours
**Cert Focus:** Email Builder, Campaigns, Trigger Links, Funnels, Websites, Forms, Surveys, Workflows, Recipes, Reputation

## Today's Mission
Final review day before the capstone. Today covers marketing + sites + automation + reputation - the features that make GHL a marketing powerhouse. Review through the certification lens with 30+ practice questions.

## Certification Topics
- Email Builder and templates
- Email Campaigns
- Trigger Links
- Affiliate Manager basics
- Social Planner
- Funnels vs Websites
- Domain Setup (CNAME, A records, auto-SSL)
- Page Builder
- Forms and Surveys
- Survey conditional logic
- Workflow general overview
- Auto Missed Call Text-Back Recipe
- No-Show Nurture Recipe
- Reputation Management
- Communities/Memberships
- Media Storage
- Reporting

---

## Part 1: Marketing & Email Review (60 min)

### Email Builder

**Elements available:**
- Text blocks
- Images
- Buttons
- Columns (1, 2, 3, 4)
- Dividers
- Spacers
- Social icons
- Video embeds
- Merge fields (`{{contact.first_name}}`)

**Design principles:**
- Mobile-first (60%+ opens on mobile)
- Single-column for mobile (or stacked columns)
- Buttons large enough to tap (44px+ height)
- High-contrast text
- Max width 600px

### Email Campaigns vs Workflows

**CRITICAL DISTINCTION:**

**Campaign** = One-time send to a specific audience at a specific time.
- Example: "Monthly newsletter" sent Oct 1 to Smart List "Active Members"

**Workflow** = Automated series triggered by events, running continuously.
- Example: "Welcome sequence" that fires whenever new lead signs up

| Feature | Campaign | Workflow |
|---------|----------|----------|
| Trigger | Manual launch | Automated event |
| Timing | One specific moment | Ongoing per contact |
| Audience | Static selection | Dynamic (trigger-based) |
| Best for | Newsletters, announcements | Nurture, reminders, lifecycle |

### Trigger Links

**What:** Special tracked URLs that can do things when clicked.

**Actions a trigger link can take:**
- Add/remove tag
- Move contact to pipeline stage
- Subscribe/unsubscribe from list
- Trigger a workflow
- Custom action

**Use cases:**
- Self-segmentation ("Click if interested in X")
- Unsubscribe from specific list (not all marketing)
- Lead scoring (track engagement)
- Click-to-book flows

### CAN-SPAM Requirements (Review!)

Every marketing email must have:
1. Accurate sender info
2. Truthful subject line
3. Clear identification as commercial
4. Valid physical address
5. Unsubscribe link
6. Honor unsubscribes within 10 business days

### Affiliate Manager

Set up affiliate programs:
- Custom commission structures
- Tracking links for affiliates
- Auto-calculated payouts
- Affiliate dashboard

### Social Planner

Schedule posts to:
- Facebook (pages)
- Instagram
- LinkedIn
- Google Business Profile
- TikTok (in some regions)
- YouTube

Features:
- Calendar view of scheduled posts
- AI content generation
- Image templates
- Hashtag management

---

## Part 2: Sites - Funnels vs Websites (60 min)

### CRITICAL DISTINCTION

| Feature | Funnel | Website |
|---------|--------|---------|
| **Structure** | Linear, step-by-step | Multi-page with navigation |
| **Purpose** | One specific goal | General business presence |
| **Navigation** | No menu (remove distractions) | Full menu |
| **SEO** | Limited | Full (blog, categories) |
| **Examples** | Lead magnet opt-in, sales page | Company site with services, about, blog |

### Page Builder

Same builder for both funnels and websites. Elements:
- Sections and rows
- Headings, text, images, videos
- Forms (embedded)
- Buttons, countdowns
- Galleries, testimonial sections
- Custom HTML/CSS
- Widgets (countdown, calendar embed, form)

### Domain Setup

**CNAME Record (most common):**
- Subdomain → GHL
- Example: `app.yourbiz.com` CNAME to `app.leadconnectorhq.com`

**A Record (for root domain):**
- `yourbiz.com` A record to GHL's IP

**TXT Record:**
- Domain verification
- SPF, DKIM for email

**Auto-SSL:**
- GHL automatically provisions HTTPS
- Wait 5-30 min after DNS propagation

### Common Domain Errors

| Error | Cause | Fix |
|-------|-------|-----|
| 404 when visiting | DNS not propagated | Wait longer, verify CNAME |
| SSL not secure | Still provisioning | Wait, check DNS config |
| Domain mismatch | Wrong target in CNAME | Update DNS to correct target |

---

## Part 3: Forms & Surveys (45 min)

### Forms vs Surveys

| Feature | Form | Survey |
|---------|------|--------|
| **Length** | Short, single page | Long, multi-page |
| **Conditional Logic** | No | Yes (branching) |
| **Use case** | Simple capture | Qualification, assessment |

### Form Configuration

- Required vs optional fields
- Field types (same as custom fields)
- Submit button text
- Success message or redirect URL
- Workflow trigger on submit

### Surveys - Conditional Logic

**Key feature:** Questions shown depend on previous answers.

Example flow:
```
Page 1: "What type of business do you run?" 
  Options: Service, Product, SaaS

Page 2 branches:
  If Service: "What services?", "Client count?"
  If Product: "What products?", "AOV?"
  If SaaS: "MRR?", "User count?"

Page 3 (all paths): "Budget?", "Timeline?"
```

### Workflow Triggers

Both forms and surveys can fire workflows on submission:
- Tag contact based on answers
- Create opportunity
- Send confirmation
- Route to team member
- Create task

---

## Part 4: Workflows Deep Review (90 min)

### Trigger Categories (Memorize!)

| Category | Example Triggers |
|----------|-----------------|
| **Contact Events** | Contact Created, Tag Added, Field Changed |
| **Calendar** | Appointment Booked, Status Changed, No-Show |
| **Form/Survey** | Form Submitted, Survey Completed |
| **Pipeline** | Opportunity Created, Stage Changed, Status Changed |
| **Conversation** | Inbound Message, Missed Call |
| **Payment** | Invoice Paid, Subscription Created, Payment Failed |
| **Manual** | Added to Workflow manually or via API |
| **Custom** | Inbound Webhook, Scheduled (time-based) |

### Action Categories

| Category | Examples |
|----------|----------|
| **Communication** | Send SMS, Email, Voicemail Drop, WhatsApp |
| **CRM** | Add Tag, Update Field, Create Opp, Assign User |
| **Calendar** | Book Appointment |
| **Internal** | Notification, Task Creation |
| **Logic** | Wait, If/Else, Goto, Goal Event |
| **External** | HTTP Webhook, Zapier, Custom Integration |

### If/Else Conditions

Can check:
- Contact fields (standard and custom)
- Tags (has/doesn't have)
- Opportunity stage/status/value
- Custom values (global)
- Math comparisons

### Wait Steps

- **Wait X minutes/hours/days** - Fixed delay
- **Wait Until specific time** - "Wait until 10 AM tomorrow"
- **Wait Until appointment time** - Based on calendar event

### Goal Events

**PAUSE/EXIT workflow** when event occurs:
- Tag added/removed
- Pipeline stage reached
- Custom field value
- Appointment status

**Use case:** Stop nurture when goal achieved.

### Recipes (Pre-Built Templates - MEMORIZE!)

### Recipe 1: Auto Missed Call Text-Back

**Full flow:**
```
Trigger: Missed Call (inbound)
  ↓
Wait: 1 minute
  ↓
Action: Send SMS
  Content: "Sorry we missed your call! How can we help?"
  ↓
Action: Add Tag "missed-call"
  ↓
Action: Internal Notification to owner
  ↓
Wait: 30 minutes
  ↓
If/Else: Inbound message received?
  YES → End
  NO → Send follow-up SMS
```

### Recipe 2: No-Show Nurture

**Full flow:**
```
Trigger: Appointment Status = No-Show
  ↓
Wait: 30 minutes
  ↓
Action: Send SMS
  Content: "Sorry we missed you! Let's reschedule."
  Include: {{booking.link}}
  ↓
Action: Add Tag "no-show"
  ↓
Wait: 24 hours
  ↓
If/Else: "appointment-booked" tag?
  YES → End
  NO → Send email with incentive
  ↓
Wait: 3 days
  ↓
If/Else: Booked?
  YES → End
  NO → Final SMS attempt
  ↓
Wait: 7 days
  ↓
Action: Add Tag "needs-manual-followup"
```

**Memorize both recipes step-by-step for the exam.**

---

## Part 5: Reputation Management (30 min)

### Connect Review Platforms

- **Google Business Profile** - Most important (local SEO)
- **Facebook** - Via FB page integration
- **Yelp** - Integration limited

### Review Request Workflows

**Standard flow:**
```
Trigger: Appointment "Showed" or Invoice Paid
  ↓
Wait: 2 hours
  ↓
Send SMS: "How was your experience? [Review link]"
  ↓
Wait: 3 days
  ↓
If no review: Send email follow-up
  ↓
Wait: 5 days
  ↓
Final SMS with incentive (be careful - can't trade reviews for discounts on some platforms)
```

### Review Response Best Practices

- Respond to ALL reviews (good and bad)
- Good: Thank genuinely, mention something specific
- Bad: Acknowledge, apologize, move offline ("Please email us so we can make it right")
- Never argue publicly

### Review Compliance

**CAN'T DO:**
- Pay for reviews
- Trade discounts for reviews
- Selectively request reviews only from happy customers (FTC issue)

**CAN DO:**
- Ask all customers for honest review
- Send generic "How was your visit?" asking before review

---

## Part 6: Memberships & Communities (30 min)

### Community Setup

- Brand the community (logo, colors, name)
- Custom domain option
- Mobile app (GHL Community app)

### Groups

- Create multiple groups
- Access control (all members, specific tags, paid tier)
- Admins and moderators
- Content types: text posts, images, videos, files, polls

### Tiered Access

Link groups to membership levels:
- Free tier → access to General group
- Paid tier → access to Premium content
- VIP tier → access to all groups including VIP Lounge

### Memberships/Courses

- Course creation with lessons
- Video hosting
- Progress tracking
- Certificates (some plans)

---

## Part 7: Reporting (30 min)

### Standard Reports

| Report | Shows |
|--------|-------|
| Appointment | Booked, showed, no-show rates |
| Call | Total calls, duration, missed |
| Contact | New contacts, by source |
| Conversion | Lead to appointment, appointment to sale |
| Agent/User | Performance by team member |
| Attribution | Lead source effectiveness |

### Google Analytics

Integration provides:
- Traffic by source
- Page views
- Bounce rate
- Conversion tracking

### Custom Reports

Some plans allow custom report building:
- Select data sources
- Apply filters
- Set date ranges
- Visualize (charts, tables)

---

## Part 8: Practice Quiz - 30 Questions

### Q1
Campaign vs Workflow - key difference?
a) Campaign is free, Workflow costs money
b) Campaign = one-time send; Workflow = automated, triggered, ongoing
c) They're the same
d) Workflow is for email only

**Answer: b)**

### Q2
A trigger link can:
a) Only track clicks
b) Track clicks + add tag + trigger workflow + subscribe/unsubscribe
c) Only send emails
d) Replace Google Analytics

**Answer: b)**

### Q3
Funnel vs Website primary difference?
a) Website is mobile, funnel is desktop
b) Funnel is linear with one goal; Website is multi-page with navigation
c) Funnel is free
d) Same thing

**Answer: b)**

### Q4
For "app.mybiz.com" to point to GHL, what DNS record?
a) A record
b) CNAME to app.leadconnectorhq.com
c) MX record
d) TXT record

**Answer: b)**

### Q5
Form vs Survey difference?
a) Form is long, survey is short
b) Form is simple capture; Survey has conditional/branching logic
c) Same thing
d) Survey is only for research

**Answer: b)**

### Q6
The Missed Call Text-Back recipe first step after trigger is:
a) Send SMS immediately
b) Wait 1 minute
c) Add tag
d) Notify team

**Answer: b)** Wait 1 min makes the response feel less robotic.

### Q7
A goal event in a workflow:
a) Tracks revenue goals
b) Pauses/exits workflow when event occurs (e.g., conversion)
c) Shows KPIs
d) Sets priorities

**Answer: b)**

### Q8
What's the difference between "Wait X minutes" and "Wait Until"?
a) No difference
b) Wait X = relative delay; Wait Until = specific time/event
c) Wait Until is deprecated
d) Wait X only works in days

**Answer: b)**

### Q9
Reviewing bad reviews best practice:
a) Delete them
b) Respond privately to move offline and resolve
c) Argue publicly
d) Ignore them

**Answer: b)**

### Q10
Can you pay for Google reviews?
a) Yes, if it's real customers
b) Yes, any amount
c) NO - violates Google policy and FTC
d) Only via Google Ads

**Answer: c)**

### Q11
Email campaign audience is defined by:
a) All contacts always
b) Smart List or tag-based selection
c) Random selection
d) Most recent 100

**Answer: b)**

### Q12
Survey conditional logic allows:
a) Math operations
b) Different questions shown based on previous answers
c) Auto-submission
d) Multi-language

**Answer: b)**

### Q13
Inbound webhook trigger receives:
a) Outgoing emails
b) HTTP POST requests from external systems
c) SMS messages
d) Phone calls

**Answer: b)**

### Q14
If/Else condition can check:
a) Only tags
b) Contact fields, tags, opp stage, custom values, math
c) Only email
d) Only calendar events

**Answer: b)**

### Q15
The No-Show Nurture recipe starts with what wait?
a) Immediate SMS
b) 30-minute wait
c) 24-hour wait
d) 1-week wait

**Answer: b)**

### Q16
Community access tiers are based on:
a) Random assignment
b) Tags or membership level
c) Only paid plan
d) Alphabetical

**Answer: b)**

### Q17
What's the purpose of the Social Planner?
a) Schedule meetings
b) Schedule social media posts across platforms
c) Team task management
d) Calendar sync

**Answer: b)**

### Q18
A CNAME record does:
a) Points domain to an IP address
b) Points subdomain to another domain
c) Sets email authentication
d) Blocks traffic

**Answer: b)**

### Q19
Auto-SSL in GHL means:
a) You set up SSL manually
b) HTTPS certificate provisioned automatically after DNS setup
c) SSL costs extra
d) SSL is not available

**Answer: b)**

### Q20
Review request can be automated via:
a) Only manual emails
b) Workflow triggered by appointment "Showed" or payment
c) Only Google Reviews
d) Must be in-person

**Answer: b)**

### Q21
An Affiliate Manager enables:
a) Managing employees
b) Affiliate programs with tracking links and commissions
c) Managing suppliers
d) Customer management

**Answer: b)**

### Q22
Attribution report shows:
a) Email opens
b) Which lead source generated each contact/conversion
c) Revenue only
d) User login activity

**Answer: b)**

### Q23
Default unsubscribe link in emails:
a) Optional
b) Required for compliance (CAN-SPAM)
c) Only for marketing emails
d) Only in USA

**Answer: b)**

### Q24
Media Storage in GHL is for:
a) Contacts
b) Uploaded files (images, videos, documents) used across GHL
c) Voicemails
d) Backups

**Answer: b)**

### Q25
A workflow goal "Opportunity Status = Won" will:
a) Mark random opps as won
b) Exit the workflow when a contact's opp is marked Won
c) Create an opp
d) Increase values

**Answer: b)**

### Q26
Class Booking calendar with max 15: 16th person:
a) Still books
b) Goes to waitlist if enabled, or blocked
c) Creates new slot
d) Downgrades to private booking

**Answer: b)**

### Q27
Bulk action NOT available in GHL:
a) Bulk SMS
b) Bulk email
c) Bulk call
d) Bulk add tag

**Answer: c)** You can't bulk call 500 people simultaneously.

### Q28
Which is NOT a valid appointment status?
a) Confirmed
b) Showed
c) No-show
d) Delivered

**Answer: d)** "Delivered" is a message status, not appointment.

### Q29
Page Builder can be used for:
a) Only funnels
b) Only websites
c) Both funnels and websites (same builder)
d) Only emails

**Answer: c)**

### Q30
If a workflow has a Goal "Tag 'converted' added" and contact gets tagged mid-sequence:
a) Workflow continues normally
b) Workflow pauses/exits at next step check
c) Workflow restarts
d) Error

**Answer: b)**

---

## Part 9: End-to-End Mini Build (90 min)

### The Challenge

Build a COMPLETE marketing campaign for Sunrise Wellness in 90 minutes. Time-limited.

**Deliverables:**
1. Lead magnet funnel (15 min)
2. 3-email nurture sequence (25 min)
3. Workflow connecting form → nurture → pipeline (20 min)
4. Trigger link for segmentation (10 min)
5. Review request automation (15 min)
6. Test end-to-end (5 min)

**Tests your speed and confidence on cert topics.**

---

## Quick Reference Cheat Sheet

| Topic | Fact |
|-------|------|
| Campaign | One-time send |
| Workflow | Automated, event-triggered |
| Trigger Link | Track + action (tag, pipeline, subscribe) |
| Funnel | Linear, one goal |
| Website | Multi-page, navigation |
| CNAME | Subdomain → another domain |
| Form | Simple capture |
| Survey | Multi-page, conditional logic |
| Missed Call Recipe | Wait 1min → SMS → Tag → Notification → Wait 30min → Follow-up |
| No-Show Recipe | Wait 30min → SMS → Tag → Wait 24h → Email → Wait 3d → SMS |
| Goal Event | Pauses/exits workflow when achieved |
| Wait Types | Wait X duration, Wait Until time/event |
| Trigger Categories | Contact, Calendar, Form, Pipeline, Conversation, Payment, Manual, Webhook |
| Review Compliance | Don't pay for reviews, ask all customers |

---

## Day 26 Recap

You've completed the three review days. You now know:
- Day 24: Agency-level features
- Day 25: Sub-account core
- Day 26: Marketing, sites, automation

Tomorrow: Capstone project to prove you can build from scratch.

## Next Day Preview

**Day 27: Capstone Project** - Build a complete GHL system for "Harmony Health Hub" from scratch. 6-8 hours. Evaluated against 50-point rubric.
