# Day 10: Reputation, Memberships & Reporting

**Time Required:** 2-3 hours
**Certification Alignment:** Reputation Management, Communities (setup, groups, admins), Reporting
**API Lab:** No dedicated API lab

---

## Learning Objectives

1. Set up and automate reputation management (review generation)
2. Build a community/membership portal with groups and tiers
3. Navigate GHL reporting and extract actionable insights
4. Organize and manage media storage

---

## Part 1: Reputation Management (60 min)

### Theory Recap

Reputation Management in GHL helps businesses:
- Monitor online reviews (Google, Facebook)
- Send automated review requests
- Respond to reviews from within GHL
- Track review trends over time

Positive reviews are critical for local businesses - 93% of consumers say online reviews impact their purchasing decisions.

### Hands-On Exercise 10.1: Set Up Reputation Management

Navigate to **Reputation** (left sidebar):

1. **Connect review platforms:**
   - Connect Google Business Profile (if available)
   - Connect Facebook Page (if available)
   - Review what other platforms are supported
2. **Review dashboard:**
   - View overall rating
   - See recent reviews
   - Filter by platform, rating, date
3. **Reply to reviews:**
   - Find a review (or simulate one)
   - Write a professional reply
   - Understand the difference between public and private replies

### Hands-On Exercise 10.2: Create Review Request Templates

Navigate to **Reputation > Settings** (or Templates):

Create these review request templates:

**SMS Template: "Post-Service Review"**
```
Hi {{contact.first_name}}! Thanks for visiting {{business.name}} today.
We'd love to hear about your experience!
Could you take 30 seconds to leave us a review?
[REVIEW_LINK]
Thank you!
```

**Email Template: "Review Request"**
- Subject: "How was your experience, {{contact.first_name}}?"
- Body: Thank the customer, include direct review link, make it easy (star rating buttons if possible)

**SMS Template: "Follow-Up Review"**
```
Hi {{contact.first_name}}, we noticed you haven't had a chance
to leave a review yet. Your feedback really helps us improve!
[REVIEW_LINK]
- Team {{business.name}}
```

### Hands-On Exercise 10.3: Automated Review Request Workflow

Navigate to **Automation > Workflows**:

Build this workflow:

**Trigger:** Appointment Status = "Showed" (or Invoice Paid)

```
[TRIGGER: Appointment marked "Showed"]
    ↓
[ACTION: Wait 2 hours]
  (Give them time to get home)
    ↓
[ACTION: Send SMS - Review Request]
  Use your "Post-Service Review" template
    ↓
[ACTION: Add Tag "review-requested"]
    ↓
[ACTION: Wait 3 days]
    ↓
[CONDITION: Has tag "review-left"?]
  → YES: Send thank-you SMS → END
  → NO: Continue
    ↓
[ACTION: Send Email - Review Request]
  Follow-up review request email
    ↓
[ACTION: Wait 5 days]
    ↓
[CONDITION: Has tag "review-left"?]
  → YES: END
  → NO: Continue
    ↓
[ACTION: Send SMS - Final Review Request]
  "Last chance" friendly request
    ↓
[ACTION: Add Tag "review-sequence-complete"]
```

**Note:** You'll need a way to detect when a review is left. Options:
- Manual tag addition
- Webhook from Google Business API
- Periodic check via reputation monitoring

---

## Part 2: Communities & Memberships (45 min)

### Theory Recap

GHL Communities (formerly Memberships) lets you create a private membership portal for your clients. Features:
- Branded community portal
- Groups (like channels/categories)
- Content posts and discussions
- Access control (free, paid, tiered)
- Admin and moderator roles

### Hands-On Exercise 10.4: Set Up a Community

Navigate to **Memberships** (or Communities):

**Step 1: Community Setup**
1. Create a new community
2. **Branding:**
   - Community name: "{{business.name}} Inner Circle"
   - Logo: Upload business logo
   - Description: "Exclusive content and community for our members"
   - Color scheme: Match your brand
3. **Domain:** Set up community URL (subdomain or custom domain)
4. **Welcome message:** "Welcome to the {{business.name}} community! Introduce yourself in the General group."

**Step 2: Create Groups**

| Group Name | Access | Purpose |
|-----------|--------|---------|
| General | All Members | Introductions, announcements |
| Resources | All Members | Shared files, templates, guides |
| Q&A | All Members | Questions and answers |
| Premium Content | Premium Only | Exclusive training/content |
| VIP Lounge | VIP Only | VIP-exclusive discussions |
| Announcements | Admin Only (post), All (view) | Official updates |

For each group:
1. Create the group
2. Set access permissions
3. Add a description
4. Post a welcome message
5. Pin important posts

**Step 3: Admin Management**
1. Add yourself as Community Admin
2. Understand moderator roles
3. Set community guidelines/rules
4. Configure notification settings

### Hands-On Exercise 10.5: Community Access Control

1. **Free tier:** Access to General, Resources, Q&A
2. **Premium tier ($99/mo):** All free groups + Premium Content
3. **VIP tier ($299/mo):** All groups including VIP Lounge

To set up tiered access:
1. Create membership offers linked to each tier
2. Use tags or membership levels to control access
3. When a contact purchases Premium, automation grants access to Premium groups
4. Test: Can a Free member see Premium Content? (Should be blocked)

### Hands-On Exercise 10.6: Content Creation

1. Create a post in the General group:
   - Text post with an introduction
   - Post with an image/video
   - Pin the post
2. Create a resource post:
   - Upload a PDF/document
   - Add a download link
   - Tag the post with a category
3. Start a discussion/Q&A:
   - Post a question
   - Reply to your own post (simulate a thread)

---

## Part 3: Media Storage (15 min)

### Hands-On Exercise 10.7: Organize Media Storage

Navigate to **Media Storage**:

1. Review what's already in your media library
2. Create organizational folders:
   - `/images/logos/`
   - `/images/social/`
   - `/documents/templates/`
   - `/documents/contracts/`
   - `/videos/`
3. Upload sample files to each folder
4. Note file URLs - these can be used in emails, funnels, and workflows
5. Understand storage limits for your plan

---

## Part 4: Reporting (30 min)

### Theory Recap

GHL Reporting provides insights across all features. Key metrics include:
- Lead generation (where leads come from, conversion rates)
- Communication (messages sent, response rates, call logs)
- Appointments (booked, showed, no-showed)
- Pipeline (deals by stage, win rate, revenue)
- Marketing (email opens/clicks, campaign performance)

### Hands-On Exercise 10.8: Explore the Reporting Dashboard

Navigate to **Reporting**:

1. **Overview Dashboard:**
   - Review the default metrics displayed
   - Change the date range (7 days, 30 days, 90 days)
   - Identify your top-performing lead sources

2. **Appointment Reports:**
   - How many appointments were booked this period?
   - What's the show rate?
   - Which calendar type performs best?

3. **Call Reports:**
   - Total calls, duration, missed calls
   - Call recordings (if enabled)
   - Peak call times

4. **Agent/User Reports:**
   - How is each team member performing?
   - Response times
   - Tasks completed

5. **Attribution/Source Reports:**
   - Which lead sources generate the most contacts?
   - Which sources convert to appointments?
   - Which sources generate the most revenue?

### Hands-On Exercise 10.9: Create Custom Reports (if available)

1. Check if GHL supports custom report building
2. Create a report focused on:
   - "This Month's Lead Pipeline" - leads by source, stage, value
   - "Team Performance" - appointments per team member, response times
3. Set up report scheduling (weekly email with key metrics) if available
4. Export report data to CSV for further analysis

---

## Part 5: Phase 1 Review & Self-Assessment

### Phase 1 Competency Checklist

Rate yourself (1-5) on each area:

| Day | Topic | Confidence (1-5) | Notes |
|-----|-------|-------------------|-------|
| 1 | Dashboard & Settings | | |
| 2 | Contacts & CRM | | |
| 3 | Conversations | | |
| 4 | Calendars | | |
| 5 | Opportunities & Pipelines | | |
| 6 | Payments & Invoicing | | |
| 7 | Marketing & Email | | |
| 8 | Sites, Forms & Surveys | | |
| 9 | Automation & Workflows | | |
| 10 | Reputation, Memberships, Reporting | | |

Areas scoring below 3 → Review that day's lesson before proceeding to Phase 2.

### Integration Preview

Phase 2 starts with combining everything you learned:
- Day 11: Multi-Channel Lead Capture (Sites + Forms + Contacts + Automation)
- Day 12: Sales Pipeline Automation (CRM + Pipeline + Calendar + Workflows)
- And more complex, real-world integration scenarios...

---

## Case Scenarios

### Case Scenario 1: Restaurant Review System

**Situation:** "The Garden Table" restaurant wants automated review requests.

**Your Task:**
1. Set up reputation management for the restaurant
2. Create a workflow:
   - After a reservation time passes (simulate with appointment "Showed")
   - Wait 2 hours
   - Send SMS review request with direct Google review link
   - If no review in 3 days, send a follow-up
   - Track: who received requests, who left reviews
3. Create a response template for:
   - 5-star reviews: Thank them, invite back
   - 1-3 star reviews: Apologize, offer to make it right, take offline
4. Set up a notification when any review below 4 stars comes in

### Case Scenario 2: Coaching Community with 3 Tiers

**Situation:** "Elevate Coaching" offers a membership community with 3 access levels.

**Your Task:**
1. Build the community with proper branding
2. Create groups for each tier:
   - **Free:** Welcome group, basic resources
   - **Standard ($97/mo):** Bi-weekly coaching calls, templates, Q&A
   - **Premium ($297/mo):** Everything in Standard + 1-on-1 calls, VIP group, premium resources
3. Create an onboarding workflow:
   - New member signs up → Welcome email → Tag with tier → Grant community access → Post intro prompt
4. Create upgrade prompts:
   - After 30 days in Free tier → SMS: "Ready to level up? Standard members get..."
5. Create content for each group (at least 3 posts per group)

### Case Scenario 3: Comprehensive Reporting Setup

**Situation:** A business owner wants a weekly report covering all key metrics.

**Your Task:**
1. Define the KPIs that matter:
   - New leads (count + source)
   - Appointments (booked, showed, no-showed)
   - Pipeline value (new, won, lost)
   - Revenue (invoices paid)
   - Reviews (new reviews, average rating)
2. Navigate reporting and find each metric
3. Create a manual "Weekly Report" template documenting:
   - Where to find each metric in GHL
   - How to export the data
   - Benchmark targets for each metric
4. Set up automated notifications for critical metrics (e.g., show rate drops below 60%)

---

## Day 10 Recap Questions

1. How do you set up automated review requests in GHL?
2. What's the recommended timing for sending a review request after a service?
3. How do you handle negative reviews within GHL?
4. Explain Community access tiers - how do you restrict group access by membership level?
5. What key reports should a business owner review weekly?
6. How does GHL's reporting handle attribution (knowing which marketing channel generated each lead)?

---

## Phase 1 Complete!

Congratulations on completing Phase 1. You now have hands-on experience with every core feature in GHL.

**Next: Phase 2 (Days 11-17)** will combine these features into real-world business systems. We'll build complete solutions that integrate multiple features together.

Before starting Phase 2, review any areas where you scored below 3 on the self-assessment. Phase 2 assumes solid competency in all Phase 1 topics.
