# Day 27: Capstone Project - Build a Complete Business from Zero

**Time Required:** 6-8 hours (can split over 2 sessions)
**Level:** Expert / Certification-Ready

## Today's Mission

Today is your final build. You will create a COMPLETE GoHighLevel system for a fictional multi-service business - "Harmony Health Hub" - from a blank slate to a fully operational automated business. No copying Sunrise Wellness Studio; you build from scratch with your own design choices. This capstone proves you can configure GHL for any business.

This is your portfolio piece. Treat it like a real client engagement. Your future self (and prospective employers) will review this.

---

## The Business: Harmony Health Hub

**Concept:** A multi-service wellness center combining:
- Fitness (personal training, group classes)
- Nutrition coaching
- Mental wellness (meditation classes, therapy sessions)
- Retail (supplements, wellness products)

**Revenue streams:**
- Memberships (3 tiers: Explore $89/mo, Balance $169/mo, Thrive $279/mo)
- Retail products (6 products between $20-$200)
- Paid workshops (quarterly, $150/person)
- Corporate wellness contracts ($2K-$10K/mo)

**Target clients:**
- Individual health-conscious adults 28-60
- Corporate wellness accounts (HR-driven contracts)
- Mental wellness specific clients (therapy/meditation seekers)

**Brand voice:** Warm, modern, evidence-based. Primary color #2D8B8A (teal), accent #F4A261 (warm orange). Tagline: "Your full-spectrum wellness home."

**Location:** Single physical studio (you can invent the address). Also offers virtual nutrition/therapy.

---

## Deliverables Overview

You will build these 9 sections. Check each off as you complete:

- [ ] Section 1: Foundation (Settings, Custom Values, Fields, Lists, Tags)
- [ ] Section 2: Contacts & Pipelines
- [ ] Section 3: Calendars (all 3 types)
- [ ] Section 4: Communications
- [ ] Section 5: Payments
- [ ] Section 6: Funnels & Marketing
- [ ] Section 7: Workflows
- [ ] Section 8: Community & Reputation
- [ ] Section 9: API Integration (optional)
- [ ] Final: CAPSTONE-SUMMARY.md document and self-assessment

---

## Section 1: Foundation (1 hour)

### Step 1.1 - Business Profile

Navigate: **Settings -> Business Profile**

Fill in ALL fields (not just required):

| Field | Value |
|-------|-------|
| Business Name | Harmony Health Hub |
| Legal Name | Harmony Health Hub LLC |
| Email | hello@harmonyhealthhub.com |
| Phone | Use your test number |
| Website | harmonyhealthhub.com |
| Industry | Health & Wellness |
| Address | 1200 Wellness Way, Suite 300 |
| City/State/Zip | Use your real city for testing |
| Timezone | Match your local timezone |
| Business Niche | Wellness / Fitness / Therapy |

Upload logo (use any placeholder logo or make one in Canva in 5 min).

### Step 1.2 - Custom Values (10 minimum)

Navigate: **Settings -> Custom Values**

Create these:

1. `business_name` = Harmony Health Hub
2. `booking_link_pt` = [your personal training calendar URL]
3. `booking_link_nutrition` = [nutrition calendar URL]
4. `booking_link_therapy` = [therapy calendar URL]
5. `membership_explore_link` = [Explore tier checkout URL]
6. `membership_balance_link` = [Balance tier checkout URL]
7. `membership_thrive_link` = [Thrive tier checkout URL]
8. `studio_address` = 1200 Wellness Way, Suite 300
9. `support_email` = support@harmonyhealthhub.com
10. `support_phone` = [your test number]
11. `brand_tagline` = Your full-spectrum wellness home.
12. `review_link` = [your Google review link or placeholder]

Pro tip: Even if URLs don't exist yet, put placeholder like `https://link.harmonyhealthhub.com/pt` - you will update them after the calendars are built.

### Step 1.3 - Custom Fields (3+ folders, 15+ fields)

Navigate: **Settings -> Custom Fields**

Create folders:

**Folder: Wellness Profile**
- Primary Goal (Dropdown: Weight Loss, Muscle Gain, Stress Management, General Health, Recovery, Other)
- Fitness Level (Dropdown: Beginner, Intermediate, Advanced)
- Health Conditions (Large Text)
- Dietary Preferences (Multi-select: Vegetarian, Vegan, Gluten-Free, Keto, No Restrictions, Other)
- Mental Wellness Interest (Checkbox)

**Folder: Membership & Purchase**
- Membership Tier (Dropdown: None, Explore, Balance, Thrive)
- Member Since (Date)
- Lifetime Value (Monetary)
- Last Purchase Date (Date)
- Renewal Date (Date)
- Churn Risk Score (Number, 0-100)

**Folder: Corporate**
- Corporate Account Name (Text)
- Employee Count (Number)
- Contract Value Monthly (Monetary)
- HR Contact Email (Email)
- Contract End Date (Date)

Total: 16 fields, 3 folders. Meets criteria.

### Step 1.4 - Smart Lists (8 minimum)

Navigate: **Contacts -> Smart Lists -> + New Smart List**

Create:

1. **Active Members** - Tag contains "member-active"
2. **Churn Risk Members** - Tag contains "member-active" AND Custom Field "Churn Risk Score" > 60
3. **Trial Prospects** - Tag contains "trial" AND DND is No
4. **Corporate Leads** - Tag contains "corporate-lead"
5. **No-Show This Month** - Appointment status Noshow in last 30 days
6. **High LTV Customers** - Custom Field "Lifetime Value" > $1500
7. **Mental Wellness Interested** - Custom Field "Mental Wellness Interest" is true
8. **Cancelled - Win Back Candidates** - Tag contains "member-cancelled" AND last activity > 30 days ago
9. **New This Week** - Date Added in last 7 days

### Step 1.5 - Tag Strategy Document

Create a Google Doc or internal note with the tag taxonomy. Use the naming convention `category-purpose`.

**Source tags (where did they come from):**
- source-facebook
- source-google
- source-instagram
- source-referral
- source-walkin
- source-corporate
- source-webchat

**Stage tags (where they are in the journey):**
- lead-cold
- lead-warm
- lead-hot
- trial
- member-active
- member-cancelled
- member-paused

**Service interest tags:**
- interest-pt (personal training)
- interest-nutrition
- interest-therapy
- interest-classes
- interest-retail
- interest-workshop
- interest-corporate

**Behavior tags:**
- booked-consult
- attended-class
- purchased-product
- submitted-review
- referred-friend

**Engagement tags:**
- highly-engaged
- re-engagement-needed
- dnd-email
- dnd-sms

Total: 28+ tags organized into 5 categories. Meets criteria.

---

## Section 2: Contacts & Pipelines (1 hour)

### Step 2.1 - Sample Contact CSV Template

Save this as `harmony-contacts.csv` (create 30+ rows based on this template):

```csv
First Name,Last Name,Email,Phone,Tags,Primary Goal,Fitness Level,Membership Tier
Sarah,Chen,sarah.chen.test+1@yourtestdomain.com,+15551000001,"source-facebook,lead-warm,interest-pt",Weight Loss,Beginner,None
Marcus,Rivera,marcus.r.test+2@yourtestdomain.com,+15551000002,"source-google,trial,interest-classes",Muscle Gain,Intermediate,None
Jessica,Patel,jessica.p.test+3@yourtestdomain.com,+15551000003,"source-referral,member-active,interest-nutrition",General Health,Beginner,Balance
(continue through 30 rows, vary the data)
```

Rules for your 30 contacts:
- At least 10 active members (spread across 3 tiers)
- At least 5 trial users
- At least 5 cold leads
- At least 3 corporate leads
- At least 3 cancelled members
- Vary sources across all 7 source tags
- Vary fitness levels, goals, interests

Import via: **Contacts -> Import -> Upload CSV**. Map columns correctly.

### Step 2.2 - Build 3 Pipelines

Navigate: **Opportunities -> Pipelines -> + Create Pipeline**

**Pipeline 1: Individual Sales Pipeline**

Stages:
1. New Lead
2. Discovery Call Scheduled
3. Discovery Completed
4. Proposal Sent (Trial Offered)
5. In Trial
6. Converted (Member)
7. Lost

Populate with 5+ opportunities across stages. Use Monetary Value (e.g., $89, $169, $279 for the tier they are considering).

**Pipeline 2: Corporate Sales Pipeline**

Stages:
1. Inquiry Received
2. Discovery Call Booked
3. Needs Assessment Complete
4. Proposal Sent
5. Negotiation
6. Contract Signed
7. Onboarding
8. Closed Lost

Populate with 5+ opportunities. Monetary Value $2,000-$10,000.

**Pipeline 3: Member Onboarding Pipeline**

Stages:
1. Welcome Week (Day 1-7)
2. First Goals Set (Day 8-14)
3. Habit Formation (Day 15-30)
4. Checkpoint Review (Day 31-60)
5. Advocate (Day 60+)

Populate with 5+ current members. This pipeline tracks onboarding progress, not sales value.

Save a screenshot or list of opportunities per pipeline for your capstone summary.

---

## Section 3: Calendars (1 hour)

Navigate: **Calendars -> Calendar Settings -> + Create Calendar**

Build all 6:

### Calendar 1: Personal Training (Round Robin)
- Type: Round Robin
- Add 2 fake team members (use your own account + invite a dummy email)
- Duration: 45 min
- Buffer: 15 min
- Availability: Mon-Sat 6am-8pm
- Form: Require Primary Goal field

### Calendar 2: Nutrition Consultation (Basic)
- Type: Basic
- Duration: 60 min
- Availability: Tue/Thu 10am-6pm, Sat 9am-2pm
- Price: Free consult, $125 per follow-up (or free for members)

### Calendar 3: Therapy Session (Basic)
- Type: Basic
- Duration: 50 min
- Availability: Mon/Wed/Fri 10am-7pm
- Confidentiality note in booking form

### Calendar 4: HIIT Class (Class Booking)
- Type: Class Booking
- Capacity: 20
- Duration: 45 min
- Schedule: M/W/F 6am, 12pm, 6pm
- Require check-in

### Calendar 5: Yoga Class (Class Booking)
- Type: Class Booking
- Capacity: 15
- Duration: 60 min
- Schedule: Tu/Th 7am, 9am, 5:30pm; Sat 9am

### Calendar 6: Meditation Class (Class Booking)
- Type: Class Booking
- Capacity: 25
- Duration: 30 min
- Schedule: Daily 7am, 7pm

For every calendar: set a branded confirmation email, set Google Meet or physical location, test booking yourself.

Update your custom values from Section 1.2 with the real booking URLs now.

---

## Section 4: Communications (45 min)

### Step 4.1 - SMS Templates (8)

Navigate: **Marketing -> Templates -> SMS Templates**

1. **Welcome SMS:** "Hi {{contact.first_name}}! Welcome to Harmony Health Hub. Reply HELP anytime or book here: {{custom_values.booking_link_pt}}"
2. **PT Reminder 24h:** "Hi {{contact.first_name}}, this is a reminder of your training session tomorrow at {{appointment.start_time}}. Reply C to confirm."
3. **PT Reminder 1h:** "See you at Harmony in 1 hour! Address: {{custom_values.studio_address}}"
4. **Class Reminder:** "Your {{appointment.title}} class is in 2 hours. Mat is provided. See you soon!"
5. **No-Show Followup:** "Hey {{contact.first_name}}, we missed you today. Want to reschedule? {{custom_values.booking_link_pt}}"
6. **Trial Day 3:** "Day 3 of your trial! How are you feeling? Reply with a number 1-10."
7. **Review Request:** "{{contact.first_name}}, your feedback matters. Would you leave a quick review? {{custom_values.review_link}}"
8. **Renewal Reminder:** "Your Harmony membership renews on {{custom_fields.renewal_date}}. Questions? Reply here."

### Step 4.2 - Email Templates (6)

Navigate: **Marketing -> Templates -> Email Templates**

Each email must have:
- Branded header (logo + teal color)
- Clear CTA button
- Footer with unsubscribe

Build these 6:

1. **Welcome Email** (sent on lead capture)
2. **Trial Kickoff Email** (sent when they start trial)
3. **Onboarding Week 1** (sent Day 1 of membership)
4. **Class Confirmation** (sent on class booking)
5. **Nurture - Mental Wellness Focus** (for contacts tagged interest-therapy)
6. **Corporate Proposal Followup** (for corporate pipeline stage 4)

### Step 4.3 - Webchat

Navigate: **Sites -> Chat Widget**

- Brand with teal color
- Welcome message: "Hi! Curious about memberships, classes, or corporate plans? Ask anything."
- Enable contact capture (name + email)
- Install code saved for your site (document in the capstone summary)

### Step 4.4 - Phone & Missed Call

Navigate: **Settings -> Phone Numbers**

- Document which number is assigned
- Set up Missed Call Text Back: "Sorry we missed you! We're likely with a client. Reply here or book: {{custom_values.booking_link_pt}}"

---

## Section 5: Payments (45 min)

### Step 5.1 - Products & Prices

Navigate: **Payments -> Products -> + Create Product**

**Membership products (3 tiers, each with monthly + annual):**
- Explore Monthly - $89/mo recurring
- Explore Annual - $890/yr (2 months free)
- Balance Monthly - $169/mo recurring
- Balance Annual - $1,690/yr
- Thrive Monthly - $279/mo recurring
- Thrive Annual - $2,790/yr

**Retail products (6):**
- Harmony Protein Blend - $45
- Wellness Starter Kit - $89
- Recovery Foam Roller - $35
- Meditation Cushion Set - $75
- Harmony Branded Hoodie - $55
- Premium Supplement Bundle - $199

**Workshop products (3):**
- Nutrition Foundations Workshop - $150
- Stress Mastery Intensive - $150
- Goal-Setting Quarterly Reset - $150

**Corporate services (2):**
- Corporate Wellness Essentials - $2,000/mo
- Corporate Wellness Premium - $6,000/mo (custom)

### Step 5.2 - Coupons

Navigate: **Payments -> Coupons**

1. WELCOME20 - 20% off first month (single use per contact)
2. REFER50 - $50 off (referral program)
3. CORP10 - 10% off corporate contracts (applies to corporate products only)

### Step 5.3 - Sample Invoices

Navigate: **Payments -> Invoices -> + New Invoice**

Create 2 test invoices:

1. Individual invoice: Balance Membership + 1 workshop ($319 total), send to test contact
2. Corporate invoice: Corporate Wellness Essentials 3-month prepay ($6,000), send to test corporate contact

Document invoice IDs / URLs.

---

## Section 6: Funnels & Marketing (1 hour)

### Step 6.1 - Lead Magnet Funnel: "Free Wellness Assessment"

Navigate: **Sites -> Funnels -> + New Funnel**

Pages:
1. **Optin Page:** Headline "Discover Your Wellness Baseline in 5 Minutes" + form
2. **Thank You Page:** Confirmation + calendar embed to book follow-up call
3. **(Automation):** On form submit -> tag `lead-magnet-wellness-assessment`, start nurture workflow

### Step 6.2 - Sales Funnel: Membership Purchase

Pages:
1. **Tier Comparison Page:** 3 columns, each tier with "Choose" button
2. **Checkout Page:** Stripe checkout with upsell (workshop)
3. **Confirmation Page:** Thank you + onboarding link

### Step 6.3 - Corporate Sales Funnel

Pages:
1. **Long-Form Landing Page:** Case study, testimonials, ROI calculator
2. **Corporate Inquiry Form:** Multi-step form (company info, employee count, goals, budget)
3. **Book a Demo Page:** Calendar embed for corporate consult

### Step 6.4 - Lead Magnet Form with Qualifying Questions

Navigate: **Sites -> Forms**

Fields:
- First Name
- Email
- Primary Goal (dropdown mapped to custom field)
- Fitness Level (dropdown mapped to custom field)
- Mental Wellness Interest (checkbox mapped to custom field)
- Dietary Preferences (multi-select)

### Step 6.5 - Complex Survey with Conditional Logic

Navigate: **Sites -> Surveys -> + New Survey**

Build a "Find Your Perfect Wellness Path" survey:

- Q1: What is your primary goal? -> branches based on answer
  - If "Weight Loss" -> Q2a: Have you tried dieting before?
  - If "Stress Management" -> Q2b: Have you tried meditation?
  - If "Muscle Gain" -> Q2c: Do you currently train?
- Q3 (conditional): Availability per week (slider)
- Q4: Budget range (dropdown)
- Final: Auto-tag based on path, route to appropriate calendar

### Step 6.6 - Email Campaigns

Navigate: **Marketing -> Campaigns**

Build 4 campaigns (one per service type):
1. Personal Training Nurture (5 emails over 10 days)
2. Nutrition Nurture (4 emails over 14 days)
3. Mental Wellness Nurture (4 emails over 14 days)
4. Corporate Nurture (6 emails over 21 days)

### Step 6.7 - Trigger Links

Navigate: **Marketing -> Trigger Links**

Create trigger links for interest segmentation. When a contact clicks, auto-tag them:
- `interest-pt` link
- `interest-nutrition` link
- `interest-therapy` link
- `interest-classes` link
- `interest-workshop` link

Use these inside nurture emails ("Which are you most interested in? -> click to learn more").

---

## Section 7: Workflows (90 min)

Navigate: **Automation -> Workflows -> + Create Workflow**

Build ALL 9. Test each with a test contact.

### Workflow 1: New Lead Capture (Multi-Channel Source Routing)
- Trigger: Contact Created OR Form Submitted OR Webchat Started
- If-Else: Check source tag
  - If source-facebook: Send FB-tailored welcome
  - If source-google: Send search-intent welcome
  - If source-referral: Different welcome + thank referrer
  - Else: Generic welcome
- Action: Add to appropriate nurture campaign

### Workflow 2: Appointment Reminder + Confirmation
- Trigger: Appointment Booked
- Wait until 24 hours before appointment -> send 24h reminder SMS + email
- Wait until 1 hour before -> send 1h reminder SMS
- After appointment: If status = Completed, send thank-you; if No-Show, trigger Workflow 4

### Workflow 3: Trial Conversion Sequence
- Trigger: Tag added "trial"
- Day 1: Welcome to trial SMS + email
- Day 3: Check-in SMS
- Day 5: Case study email
- Day 7: Conversion offer email (with coupon WELCOME20)
- Day 10: Last chance SMS
- If tag "member-active" added anywhere -> stop

### Workflow 4: No-Show Nurture
- Trigger: Appointment Status = No Show
- Wait 30 min -> send apologetic SMS with rebook link
- Wait 2 days -> email with rebook link
- Wait 7 days -> final attempt email
- If appointment rebooked -> stop

### Workflow 5: Post-Purchase Onboarding
- Trigger: Order Form Submission (membership product)
- Add tag `member-active` + specific tier tag
- Remove tag `trial`
- Day 1: Welcome to membership email + set custom field Member Since
- Day 2: First goals SMS with booking link
- Day 7: Week 1 check-in
- Day 14: Habit formation content
- Day 30: Milestone celebration + review request

### Workflow 6: Corporate Inquiry Handling (Priority Routing)
- Trigger: Corporate inquiry form submitted
- Internal notification (SMS + email to sales team)
- Auto-assign opportunity to corporate pipeline
- Create task for owner: "Follow up in 1 hour"
- Wait 1 hour -> if task not complete, escalate

### Workflow 7: Member Retention (Churn Detection)
- Trigger: Daily at 2am (Date/Time trigger)
- Filter: Contacts tagged member-active with no activity in 21 days
- Increment Churn Risk Score custom field by 10
- If score >= 60: Send re-engagement email + internal alert
- If score >= 80: Send personal outreach task to team

### Workflow 8: Review Request Automation
- Trigger: Tag added `booked-consult` OR Appointment Completed
- Wait 2 days
- Check: Contact has NOT already been tagged `submitted-review`
- Send review request SMS with link
- Wait 3 days -> email reminder if still no review
- On click of review link -> tag `submitted-review`

### Workflow 9: Win-Back for Cancelled Members
- Trigger: Tag added `member-cancelled`
- Wait 14 days -> empathetic email, ask why
- Wait 30 days -> special win-back offer (50% off first month back)
- Wait 60 days -> final email with survey link

Test every workflow with a test contact. Document which test contact you used for each.

---

## Section 8: Community & Reputation (30 min)

### Step 8.1 - Community with Tiered Group Access

Navigate: **Memberships -> Communities** (or Sites -> Communities)

Create the "Harmony Circle" community with 3 groups:

1. **Harmony Explore** (free, all contacts + free members)
2. **Harmony Balance** (Balance + Thrive members only)
3. **Harmony Thrive** (Thrive members only, exclusive content)

Use tag-based access:
- `member-active` AND `tier-balance` -> Balance group
- `member-active` AND `tier-thrive` -> Thrive group

Seed each group with a welcome post and 2 sample posts.

### Step 8.2 - Review Request System

Already built in Workflow 8. Document:
- Which third-party review platforms are connected (Google, Facebook)
- Where the review link points
- How responses are tracked

### Step 8.3 - Reporting Dashboard

Navigate: **Reporting -> Custom Dashboard**

Create a dashboard named "Harmony Executive Overview" with widgets:
- New leads this month
- Conversion rate (leads -> members)
- Monthly recurring revenue
- Churn risk count
- Appointments this week
- Top source by conversions

Take a screenshot for the summary doc.

---

## Section 9: API Integration (Optional, 60 min)

If your sub-account has API access, do this for bonus points.

### Script 1: Export All Members to CSV

Save to `scripts/harmony_export_members.py`:

```python
import os
import csv
import requests

API_KEY = os.environ["GHL_API_KEY"]
LOCATION_ID = os.environ["GHL_LOCATION_ID"]
BASE = "https://services.leadconnectorhq.com"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Version": "2021-07-28",
    "Accept": "application/json",
}

def fetch_members():
    members = []
    url = f"{BASE}/contacts/"
    params = {"locationId": LOCATION_ID, "limit": 100, "query": "member-active"}
    while url:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        members.extend(data.get("contacts", []))
        url = data.get("meta", {}).get("nextPageUrl")
        params = None
    return members

def write_csv(members, filename="harmony_members.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["First", "Last", "Email", "Phone", "Tier"])
        for m in members:
            tier = ""
            for cf in m.get("customFields", []):
                if cf.get("key") == "membership_tier":
                    tier = cf.get("value", "")
            writer.writerow([
                m.get("firstName", ""),
                m.get("lastName", ""),
                m.get("email", ""),
                m.get("phone", ""),
                tier,
            ])

if __name__ == "__main__":
    members = fetch_members()
    write_csv(members)
    print(f"Exported {len(members)} members.")
```

### Script 2: Webhook Receiver for New Contact Notifications

Save to `scripts/harmony_webhook_receiver.py`:

```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
SECRET = os.environ.get("WEBHOOK_SECRET", "change-me")

@app.post("/ghl/new-contact")
def handle_new_contact():
    if request.headers.get("X-Webhook-Secret") != SECRET:
        return jsonify({"error": "unauthorized"}), 401
    payload = request.get_json(force=True)
    print(f"NEW CONTACT: {payload.get('email')} from {payload.get('source')}")
    # TODO: send Slack/email notification here
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055)
```

Configure a workflow Webhook action to POST to this endpoint on Contact Created.

### Script 3: Auto-Update Lead Score Custom Field

Save to `scripts/harmony_lead_score.py`:

```python
import os
import requests

API_KEY = os.environ["GHL_API_KEY"]
LOCATION_ID = os.environ["GHL_LOCATION_ID"]
BASE = "https://services.leadconnectorhq.com"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Version": "2021-07-28",
    "Content-Type": "application/json",
}

def score_contact(contact):
    score = 0
    tags = contact.get("tags", [])
    if "source-referral" in tags: score += 30
    if "booked-consult" in tags: score += 25
    if "trial" in tags: score += 20
    if "interest-corporate" in tags: score += 40
    if "highly-engaged" in tags: score += 15
    return min(score, 100)

def update_score(contact_id, score):
    url = f"{BASE}/contacts/{contact_id}"
    body = {"customFields": [{"key": "lead_score", "field_value": score}]}
    r = requests.put(url, headers=headers, json=body)
    r.raise_for_status()

# Run against all contacts (fetch similar to script 1)
```

If you do not have API access, skip this section. You still earn full marks on the other 8.

---

## Evaluation Rubric (50 points)

Self-score at the end:

| Category | Points | Description |
|----------|--------|-------------|
| Business Profile Complete | 5 | All fields configured |
| Custom Values (10+) | 5 | At least 10 functional custom values |
| Custom Fields Structure | 10 | 3 folders, 15+ fields, well organized |
| Contacts Imported | 5 | 30+ contacts with custom fields populated |
| Pipelines (3) | 5 | All 3 pipelines built and populated |
| All 3 Calendar Types | 5 | 6 calendars, proper configuration |
| Communications Library | 5 | Templates created, webchat configured |
| Payment System | 5 | Products, coupons, sample invoices |
| Marketing Funnels | 5 | Both funnels built, survey with logic |
| Complete Workflows (8+) | 10 | All listed workflows built and tested |
| Community Setup | 2 | Groups with tier-based access |
| Reputation System | 2 | Automated review requests |
| End-to-End Tested | 5 | Full journey walkthrough documented |
| Bonus: API Integration | 5 | Working Python integration |

**Passing score: 40/50**

### Scoring guidance

- 50/50 = Exceptional. Portfolio-ready, ready for paid client work.
- 45-49 = Excellent. Minor gaps, certification-ready.
- 40-44 = Passing. Strong foundation, polish the rough edges.
- 35-39 = Near-passing. Identify 1-2 weak sections and rebuild them.
- <35 = Needs more practice. Revisit the Phase 1-2 lessons on weak areas.

---

## Step-by-Step Build Order (Recommended)

Do NOT jump around. Follow this order to avoid dependency problems:

1. Business Profile -> everything depends on it being set.
2. Custom Fields & Custom Values -> needed before workflows, forms, or emails reference them.
3. Tags Strategy Document -> decide before you start tagging.
4. Contacts Import -> now your test data exists.
5. Calendars -> now booking links exist, update custom values.
6. Pipelines & Opportunities -> data to route through.
7. Products & Coupons -> needed by checkout funnels.
8. Templates (SMS + Email) -> needed by workflows.
9. Funnels & Forms & Survey -> where leads enter.
10. Workflows -> tie everything together.
11. Community & Reputation -> final layer.
12. API scripts -> after everything is stable.

---

## Hints and Tips

- Work in this order: Settings -> Custom Fields -> Contacts -> Calendars -> Pipelines -> Products -> Templates -> Funnels -> Workflows.
- Test EVERY workflow with a test contact before marking complete.
- Use tag naming convention: `category-purpose` (e.g., "member-active", "source-facebook"). Consistency is the difference between a usable system and chaos.
- Document as you go. This is also a portfolio piece.
- If you get stuck, do NOT skip forward - go back to the specific Phase 1-3 lesson covering that topic.
- Use branching workflow logic whenever possible (If/Else) rather than creating 5 separate workflows.
- When in doubt, mirror how a real client would use it, not what looks neat in the editor.
- Name everything consistently. `Workflow: 05 - Post-Purchase Onboarding` is better than `new workflow 3`.

---

## Final Submission

Create a file called `CAPSTONE-SUMMARY.md` in your personal notes or this repo. Include:

1. **Screenshots or written descriptions of each build section** (9 sections)
2. **Self-assessment score** (fill the rubric)
3. **Lessons learned** (at least 5 bullet points)
4. **What you would improve** (at least 3 bullet points)
5. **Time spent per section** (honest tracking)
6. **Links to any external resources** (forms, funnel URLs)

Template:

```markdown
# Harmony Health Hub - Capstone Summary

## Overview
Built complete GHL sub-account for Harmony Health Hub in [X] hours.

## Section Completion
- [x] Section 1: Foundation
- [x] Section 2: Contacts & Pipelines
- ...

## Self-Assessment Score: __/50

| Category | Score | Notes |
|----------|-------|-------|
| Business Profile | 5/5 | All fields done |
| ... | ... | ... |

## Lessons Learned
1. ...
2. ...

## What I Would Improve
1. ...
2. ...

## Time Per Section
Section 1: 55 min
Section 2: 70 min
...
```

---

## Case Scenarios for Variations

Once you complete the Harmony Health Hub capstone, these two case scenarios let you prove versatility. Not required, but excellent portfolio additions.

### Case 1: Rebuild this capstone for BrightSmile Dental

Adaptations:
- Pipeline: New Patient -> Consultation -> Treatment Plan -> Scheduled -> Completed -> Follow-up
- Calendars: Cleaning (Class booking style, multi-hygienist), Consultation (Basic), Emergency (Basic with urgent routing)
- Products: Procedure deposits, whitening ($300), Invisalign ($4500), membership plan ($39/mo)
- Workflows: Pre-op SMS prep, post-op care, 6-month recall
- Custom fields: Insurance info, last cleaning date, treatment plan stage

### Case 2: Rebuild this capstone for Elevate Digital Agency

Adaptations:
- Pipelines: Agency Sales (longer cycle), Client Onboarding, Retainer Management
- Calendars: Discovery Call (Round Robin across 3 account execs), Strategy Session (Basic), Monthly Review (Basic)
- Products: Retainer tiers ($2K, $5K, $10K), one-time projects, audits ($1500)
- Workflows: Proposal follow-up, contract renewal 60 days before, monthly report delivery
- Custom fields: Agency services purchased, current MRR, contract end date, account exec

---

## Congratulations

If you completed the Harmony Health Hub capstone at 40/50 or above, you are operationally certification-ready. Tomorrow (Day 28) is the mock exam - the final checkpoint before the real HighLevel Admin Certification.

Rest tonight. You earned it.
