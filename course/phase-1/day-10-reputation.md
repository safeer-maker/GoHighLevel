# Day 10: Reputation, Memberships & Reporting

**Time Required:** 2-3 hours
**Certification Alignment:** Reputation Management, Communities (setup, groups, access control), Reporting
**API Lab:** None

---

## Today's Mission

This is the final day of Phase 1 -- and what a journey it has been.

Over the past 9 days, you have built Sunrise Wellness Studio from the ground up: a branded business profile with custom values (Day 1), a contact database organized with Smart Lists and custom fields (Day 2), SMS and email templates (Day 3), booking calendars for PT sessions, group classes, and nutrition consultations (Day 4), a Membership Sales pipeline tracking every lead from inquiry to sign-up (Day 5), products, invoices, and coupons for memberships and services (Day 6), email campaigns and trigger links for marketing (Day 7), a Free Trial funnel with forms and a survey (Day 8), and yesterday, workflows that tie it all together into automated sequences running 24/7 (Day 9).

The studio is now a functioning automated machine. Leads come in through the funnel, get nurtured automatically, book appointments, move through the pipeline, and pay for memberships. But three critical pieces are still missing:

1. **Reputation Management** -- happy members finish their sessions, but nobody asks them for a Google review. Those 5-star reviews that would bring in new members? They are sitting in your members' heads, never posted.
2. **Community** -- members train at the studio, but there is no place for them to connect, access exclusive content, or feel like they belong to something bigger than a gym membership.
3. **Reporting** -- all this data is flowing through GHL (contacts, appointments, pipeline deals, payments), but you have not looked at it as a whole to understand what is working and what is not.

Today you will add all three. After today, Sunrise Wellness Studio is a complete, automated, reputation-building, community-driven business.

---

## Learning Objectives

By the end of today, you will be able to:

1. Set up and automate a reputation management system that generates reviews consistently
2. Build a branded community portal with tiered access based on membership level
3. Organize media storage for efficient content management
4. Navigate GHL reporting dashboards and extract actionable business insights
5. Assess your Phase 1 competency and identify areas for review before Phase 2

---

## Part 1: Reputation Management (45 min)

### What is Reputation Management?

**Reputation Management** is a system for monitoring, requesting, and responding to online reviews across platforms like Google and Facebook. In GHL, it is a dedicated section that brings all your reviews into one dashboard and gives you tools to actively generate new ones.

Think of it like a feedback loop. Your members have great experiences at Sunrise Wellness Studio, but most people do not leave reviews unless you ask. Reputation Management is the "asking" system -- automated, consistent, and polite.

### Why Does This Matter?

Here is a number that should get your attention: **93% of consumers say online reviews influence their purchasing decisions.** For a local wellness studio, reviews are not just nice to have -- they are the difference between a potential member choosing you or the gym down the street.

Consider this scenario: someone searches "fitness studio near me" on Google. Two studios appear. One has 47 reviews with a 4.8-star average. The other has 3 reviews from two years ago. Which one gets the click? The answer is obvious -- and that is why you need a system that consistently generates new reviews.

The good news is that most of your members ARE happy. They just need a nudge. That is exactly what you will build today.

### Exercise 10.1: Explore the Reputation Interface

**Purpose:** Understand what the Reputation Management section offers and what connections are required, so you know the full picture even if you cannot connect every platform today.

Navigate to **Reputation** in the left sidebar:

1. **Explore the dashboard layout:**
   - Overall rating display
   - Recent reviews section
   - Platform filters (Google, Facebook, etc.)
   - Date range selectors
   - Reply functionality

2. **Check connection options:**
   - Look for Google Business Profile integration
   - Look for Facebook Page integration
   - Note what information is required to connect each platform

3. **Understand your access level:**
   - **If you have a Google Business Profile or Facebook Page:** Connect it now. Follow the prompts -- GHL will ask you to authenticate with your Google/Facebook account and select the business listing. Once connected, your existing reviews will appear in the dashboard
   - **If you do not have these accounts:** That is perfectly fine. Explore the interface to understand what it looks like and what is required. Then focus on the exercises below -- the review REQUEST system works independently of whether platforms are connected, and it is the most valuable part

4. **Review the reply interface:**
   - Explore how you would respond to reviews directly from GHL (instead of logging into Google or Facebook separately)
   - Note the difference between a public reply (visible to everyone) and a private follow-up (only the reviewer sees it)

> **Pro Tip:** Even if you cannot connect a review platform today, the certification expects you to know HOW to connect them and WHAT happens when they are connected. Make notes on the connection flow for your certification prep.

### Exercise 10.2: Create Review Request Templates for Sunrise Wellness

**Purpose:** Build the message templates that will be used to ask members for reviews. These templates will be triggered automatically by the workflow you build in Exercise 10.3.

You will create three templates -- an initial SMS request, a professional email request, and a follow-up SMS for people who did not respond to the first ask.

**Template 1: SMS Review Request (Initial)**

Navigate to your SMS templates (or build this inline within the workflow later):

```
Hi {{contact.first_name}}! Thanks for training with us today
at Sunrise Wellness! Could you share your experience with a
quick review? It means the world to our small team.

[REVIEW_LINK]

Thank you!
- The Sunrise Wellness Team
```

**How to set up the review link:**
- If you connected a Google Business Profile, GHL can generate a direct review link (look in Reputation settings)
- If not, you can manually find your Google review link by searching for your business on Google, clicking "Write a review," and copying the URL
- As a placeholder for this exercise, use `[REVIEW_LINK]` -- you will replace it with the real URL when you have one

**Template 2: Email Review Request**

Navigate to **Marketing > Emails > Templates** (the same place you built email templates on Day 3 and Day 7):

- **Template Name:** "Review Request - Post Session"
- **Subject:** "How was your session today, {{contact.first_name}}?"
- **Layout:**

```
[HEADER: Sunrise Wellness Studio logo + warm brand colors]

Hi {{contact.first_name}},

Thanks for visiting Sunrise Wellness Studio today!
We hope you had an amazing session.

We would love to hear about your experience. Your feedback
helps us improve AND helps other people in our community
find a place to train.

[BUTTON: "Leave a Review" --> link to Google review page]

It only takes 30 seconds, and it truly makes a difference
for our small studio.

Thank you for being part of the Sunrise Wellness family!

[FOOTER: Studio address, hours, social media links, unsubscribe]
```

**Template 3: SMS Review Follow-Up (3 Days Later)**

```
Hi {{contact.first_name}}, we hope you are still feeling great
after your session at Sunrise Wellness! If you have a spare
minute, we would really appreciate a quick review:

[REVIEW_LINK]

Your words help other people discover us. Thank you!
- Team Sunrise
```

> **Pro Tip:** The best time to ask for a review is within a few hours after a positive experience. For a wellness studio, that means after a great workout when endorphins are high and the member is feeling accomplished. That is why the workflow trigger is "Appointment Showed" rather than "Appointment Booked."

### Exercise 10.3: Build the Automated Review Request Workflow

**Purpose:** Create a workflow that automatically asks members for reviews after their sessions, without you having to remember to ask anyone. This connects to the calendars from Day 4 (the appointment trigger) and the templates you just created.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Review Request - Post Session"

```
[TRIGGER: Appointment Status --> Changed to "Showed"]
```

1. Click **Add New Workflow Trigger**
2. Select **Appointment Status** (under Calendar triggers)
3. Filter to: Status changed to **Showed**
4. WHY: You only want to request reviews from members who actually attended their session. Asking a no-show for a review would be awkward (and that is what the Day 9 No-Show Nurture workflow handles instead)

```
    |
    v
[ACTION: Wait 2 hours]
```

5. Add a **Wait** action: 2 hours
6. WHY: Give the member time to finish their session, drive home, shower, and settle in. A review request 5 minutes after their appointment ends feels too aggressive. Two hours later, they are relaxed but the positive experience is still fresh

```
    |
    v
[ACTION: Send SMS -- Review Request]
```

7. Add **Send SMS** using Template 1 from Exercise 10.2
   - If you do not have a phone number on your sub-account, use **Send Email** with Template 2 instead for this first touchpoint

```
    |
    v
[ACTION: Add Tag "review-requested"]
```

8. Add **Add Tag:** `review-requested`
9. WHY: This tag serves two purposes. First, it prevents the member from being asked for another review if they attend multiple sessions in a short period (you can add a workflow filter: "Only trigger if contact does NOT have tag review-requested"). Second, it creates a trackable metric -- you can see how many members have been asked for reviews

```
    |
    v
[ACTION: Wait 3 days]
    |
    v
[CONDITION: If/Else -- Has tag "review-left"?]
  --> YES: Send thank-you message --> End
  --> NO: Send follow-up email
```

10. Add **Wait:** 3 days
11. Add **If/Else:** Has tag `review-left`?
    - NOTE: The `review-left` tag would be applied manually when you see a new review come in, or automatically via a webhook if your Google Business Profile triggers it. For now, set up the condition -- the logic is what matters
    - **YES branch:** Add **Send SMS/Email:**
      ```
      Thank you so much for the review, {{contact.first_name}}!
      It means the world to us. See you at your next session!
      ```
      Then end the workflow
    - **NO branch:** Add **Send Email** using Template 2 from Exercise 10.2 (the detailed email with the review button)

```
    |
    v
[ACTION: Wait 5 days]
    |
    v
[CONDITION: If/Else -- Has tag "review-left"?]
  --> YES: End
  --> NO: Send final SMS request + complete sequence
```

12. Add **Wait:** 5 days
13. Add **If/Else:** Has tag `review-left`?
    - **YES branch:** End workflow
    - **NO branch:** Add two actions:
      - **Send SMS/Email** using Template 3 from Exercise 10.2 (the follow-up)
      - **Add Tag:** `review-sequence-complete`

14. WHY: Three requests spread across 8 days (instant SMS, 3-day email, 8-day final SMS) is polite persistence without being annoying. After three asks, stop. The `review-sequence-complete` tag tells you this member has been through the full sequence

**Save and publish the workflow.**

Here is the complete flow:

```
Appointment marked "Showed"
    |
    v
Wait 2 hours
    |
    v
Send SMS review request + Tag "review-requested"
    |
    v
Wait 3 days
    |
    v
Left a review? --> YES: Thank them, done!
    |                NO: Send email review request
    v
Wait 5 days
    |
    v
Left a review? --> YES: Done!
                   NO: Final SMS request
                       + Tag "review-sequence-complete"
```

---

## Part 2: Community / Memberships (45 min)

### What is a Community?

A **Community** (sometimes called Memberships in GHL) is a private online portal where your members can interact, access exclusive content, and feel like they belong to something beyond their gym membership.

Think of it like a private Facebook Group, but hosted on your own platform -- branded with your logo, your colors, and organized the way you want. Members log in, see posts and discussions, access resources, and connect with other members and coaches.

### Why Build a Community for a Wellness Studio?

Without a community, the member experience is transactional: show up, work out, leave. With a community, the experience extends beyond the four walls of the studio:

- **Retention:** Members who feel connected to a community are far less likely to cancel their membership
- **Value perception:** A member paying $149/month for Premium feels much better about that investment when they also have access to exclusive nutrition guides, workout plans, and direct coach interaction
- **Upselling:** Free and Basic members see what Premium and VIP members have access to, which creates natural upgrade motivation
- **Engagement between sessions:** Members can share progress, ask questions, and stay motivated on rest days

For Sunrise Wellness Studio, the community creates four tiers of access that match the membership levels from Day 6:

| Membership | Monthly | Community Access |
|------------|---------|-----------------|
| Free Trial (7 days) | $0 | Welcome group only |
| Basic ($79/mo) | $79 | Welcome + Workout Tips + Class Discussion |
| Premium ($149/mo) | $149 | All Basic groups + Nutrition Corner |
| VIP ($249/mo) | $249 | Everything + VIP Lounge |

### Exercise 10.4: Set Up the Sunrise Wellness Community

**Purpose:** Create the branded community portal that members will log into. This is the container that holds all your groups and content.

Navigate to **Memberships** (or **Communities**) in the left sidebar. The exact name depends on your GHL version -- look for either term.

**Step 1: Create the Community**
1. Click **+ Create** (or "New Community")
2. **Community Name:** "Sunrise Wellness Inner Circle"
3. **Description:** "Your home for workouts, nutrition tips, class discussions, and exclusive member content. Welcome to the Sunrise Wellness family!"
4. **Branding:**
   - Upload a logo (use the Sunrise Wellness logo if you created one on Day 1, or use a placeholder)
   - Set colors to match the Sunrise Wellness brand (warm tones -- orange, coral, gold)
   - Choose a cover image or banner (a fitness-related photo works well)
5. **Welcome Message:** "Welcome to the Inner Circle! Start by introducing yourself in the Welcome & Announcements group. Tell us your name, your fitness goals, and what classes you are most excited to try!"

**Step 2: Configure Basic Settings**
1. Set yourself as Community Admin
2. Review notification settings -- you will want to be notified of new posts and member activity
3. Set community guidelines if there is a guidelines/rules section:
   - Be supportive and positive
   - No spam or self-promotion
   - Keep health advice general (consult professionals for medical questions)
   - Respect everyone's fitness journey

### Exercise 10.5: Create Groups Matching Membership Tiers

**Purpose:** Build the group structure that organizes content and controls who sees what based on their membership level.

Create these groups inside the Sunrise Wellness Inner Circle community:

| Group | Who Can Access | Content Purpose |
|-------|---------------|-----------------|
| **Welcome & Announcements** | All Members (Free Trial through VIP) | Studio news, schedule changes, holiday hours, event announcements |
| **Workout Tips** | Basic, Premium, VIP | Exercise tutorials, proper form guides, home workout ideas for rest days |
| **Class Discussion** | Basic, Premium, VIP | Post-class conversations ("That HIIT class was intense!"), class requests, schedule feedback |
| **Nutrition Corner** | Premium and VIP only | Recipes, weekly meal prep guides, nutrition coaching tips, supplement recommendations |
| **VIP Lounge** | VIP only | Exclusive early access to new programs, direct Q&A with head trainer, behind-the-scenes content, VIP-only challenges |

For each group:
1. Click **+ Create Group** (or "Add Group")
2. Enter the group name and description
3. Set the access level (this is the key step):
   - Look for **access rules** or **offer/tier restrictions** in the group settings
   - You may need to use tags or membership products to control access. For example:
     - "Nutrition Corner" requires the contact to have the tag `premium-member` OR `vip-member`
     - "VIP Lounge" requires the tag `vip-member`
   - If tag-based access is not available directly, use the membership/offer system to gate access (link the group to a specific product from Day 6)
4. Set posting permissions:
   - Most groups: All members can post and comment
   - Welcome & Announcements: Consider making this admin-post-only for official announcements, with comments enabled so members can react

> **Pro Tip:** The access control is what makes the community a powerful retention and upselling tool. When a Basic member at $79/month sees "Nutrition Corner - Premium Members Only" and "VIP Lounge - VIP Members Only," they naturally wonder what they are missing. That curiosity drives upgrades.

### Exercise 10.6: Create Sample Content

**Purpose:** A community with no content feels dead. Seed each group with 2 posts so new members see activity from day one.

Create these sample posts:

**Welcome & Announcements (2 posts):**

Post 1 - Pinned Welcome:
- Title: "Welcome to the Sunrise Wellness Inner Circle!"
- Body: "We are so glad you are here! This community is your space to connect with fellow members, get fitness tips, discuss classes, and access exclusive content based on your membership tier. Start by introducing yourself below -- tell us your name, your fitness goals, and what class you want to try first!"

Post 2 - Schedule Update:
- Title: "This Week's Class Schedule Highlights"
- Body: "New this week: We added a Saturday 9 AM Pilates class by popular demand! Also, Tuesday's HIIT class is moving from 6 PM to 6:30 PM starting next week. Questions? Drop them in the comments."

**Workout Tips (2 posts):**

Post 1:
- Title: "5 Stretches You Should Do Before Every Workout"
- Body: Write a brief post covering 5 dynamic stretches (leg swings, arm circles, hip openers, walking lunges, torso twists) with a note that stretching prevents injury and improves performance

Post 2:
- Title: "Home Workout: No Equipment Needed"
- Body: A simple 20-minute bodyweight circuit (squats, push-ups, lunges, plank hold, burpees -- 3 rounds) for rest days

**Nutrition Corner (2 posts -- Premium/VIP only):**

Post 1:
- Title: "Weekly Meal Prep Guide: High Protein Edition"
- Body: A sample weekly meal prep plan with breakfast, lunch, dinner, and snack ideas focused on protein. Keep it simple and practical

Post 2:
- Title: "Post-Workout Smoothie Recipes"
- Body: 3 smoothie recipes using protein powder (mention the Protein Starter Kit product from Day 6 -- $45). Include ingredients and blending instructions

**VIP Lounge (2 posts -- VIP only):**

Post 1:
- Title: "VIP Early Access: New Strength Program Launching Next Month"
- Body: "VIPs, you are the first to know! We are launching a 6-week progressive strength program next month. As VIP members, you get first dibs on enrollment before we open it to everyone else. Details coming this Friday."

Post 2:
- Title: "Ask the Head Trainer Anything"
- Body: "This is your space to ask me anything about your training plan, nutrition, recovery, or goals. Drop your question below and I will respond within 24 hours. This direct access is one of the perks of being a VIP member!"

### Exercise 10.7: Design Access Control Based on Membership Tags

**Purpose:** Document how membership tags (from Day 2 and Day 6) connect to community access, creating a clear system that can be automated.

Create a reference document (or just write this down) mapping tags to community access:

```
Tag: "free-trial"
  Community Access: Welcome & Announcements only
  How tag is applied: Day 9 "New Trial Lead" workflow

Tag: "basic-member"
  Community Access: Welcome, Workout Tips, Class Discussion
  How tag is applied: When Basic membership ($79/mo) is purchased (Day 6)

Tag: "premium-member"
  Community Access: All Basic groups + Nutrition Corner
  How tag is applied: When Premium membership ($149/mo) is purchased (Day 6)

Tag: "vip-member"
  Community Access: All groups including VIP Lounge
  How tag is applied: When VIP membership ($249/mo) is purchased (Day 6)
```

In production, you would build a workflow for each:
- **Trigger:** Subscription Created or Invoice Paid for [membership product]
- **Action:** Add the appropriate tag, which grants community access

You do not need to build these workflows now -- you built plenty of workflows on Day 9. The important thing is understanding the CONNECTION between payments (Day 6), tags (Day 2), and community access (today).

---

## Part 3: Media Storage (15 min)

### What is Media Storage?

**Media Storage** is GHL's file management system -- a central library where you store images, documents, and videos that are used across the platform. Every image in your emails, every PDF in your community posts, and every logo on your funnels lives here.

Think of it like Google Drive or Dropbox, but built into GHL. When you upload a file, it gets a URL that you can reference anywhere in the platform.

### Exercise 10.8: Organize Sunrise Wellness Media

**Purpose:** Create an organized folder structure so that as Sunrise Wellness grows, every team member can find the right image or document quickly.

Navigate to **Media Storage** (look under Settings or in the left sidebar -- location varies by GHL version):

1. **Review what is already there** -- you may have uploaded images during previous exercises (email templates on Day 7, funnel on Day 8, etc.)

2. **Create these organizational folders:**
   - `/sunrise-wellness/logos/` -- Business logo in different sizes, favicon, social media profile images
   - `/sunrise-wellness/class-photos/` -- Photos of group classes, trainers in action, facility shots (use placeholder images for now)
   - `/sunrise-wellness/email-images/` -- Hero images for email templates, promotional banners, seasonal graphics
   - `/sunrise-wellness/documents/` -- Waivers, intake forms, class schedules as PDFs, membership agreements

3. **Upload at least one sample file to each folder** -- this can be a placeholder image, a simple PDF you create, or any relevant file. The point is to establish the structure and practice the upload process

4. **Note the file URLs** -- after uploading, each file gets a URL. Copy one and paste it into a test email or community post to verify it works

5. **Check storage limits** -- look in your account settings for how much storage is included with your plan. For a single sub-account exercise, you will not come close to the limit, but knowing it exists is important

> **Pro Tip:** Consistent folder naming saves hours of searching later. When Sunrise Wellness has 200+ images across emails, funnels, community posts, and social media, a flat "all files in one place" structure becomes unmanageable fast.

---

## Part 4: Reporting (30 min)

### What is Reporting?

**Reporting** is your business dashboard -- the place where all the data flowing through GHL gets summarized into charts, numbers, and trends that tell you how the business is performing.

Think of it like the dashboard in your car. You do not need to understand how the engine works to read the speedometer, fuel gauge, and temperature. GHL Reporting does the same thing for your business: it takes all the complex data from contacts, appointments, pipelines, conversations, and payments and turns it into simple, readable metrics.

### Why Does Reporting Matter?

You have spent 9 days building an impressive system. But without looking at the data, you are flying blind. Reporting answers questions like:

- **Are leads coming in?** How many new contacts this month, and where are they coming from?
- **Are they booking?** What percentage of leads book an appointment? What is the no-show rate?
- **Are they converting?** How many leads become paying members? At what membership tier?
- **What is working?** Is Instagram or Google driving more sign-ups? Are the Day 7 email campaigns getting opened?
- **What needs attention?** Is the no-show rate climbing? Did response times get slower?

For a studio owner, looking at these numbers weekly is the difference between reacting to problems and preventing them.

### Exercise 10.9: Explore the Reporting Dashboard

**Purpose:** Get familiar with every reporting section so you know where to find any metric a business owner might ask about.

Navigate to **Reporting** in the left sidebar:

**Section 1: Overview Dashboard**
1. Look at the default dashboard view
2. Change the date range -- try "Last 7 Days," "Last 30 Days," and "This Month"
3. Note the key metrics displayed:
   - New contacts created
   - Appointments booked
   - Conversations (messages sent/received)
   - Pipeline value

**Section 2: Contact Reports**
1. Find the contact/lead source report
2. Answer these questions for Sunrise Wellness:
   - How many new contacts were added this month? (Probably just your test contacts, but the report should show them)
   - Which lead source is the most common? (Look at how contacts were created -- form submission, manual, API, import from Day 2)
   - What is the trend? Is the number growing week over week?

**Section 3: Appointment Reports**
1. Find the appointment reporting section
2. Look for these metrics:
   - Total appointments booked
   - **Show rate** -- what percentage of booked appointments were marked "Showed"
   - **No-show rate** -- what percentage were marked "No Show"
   - Which calendar has the most bookings (PT, Group Fitness, or Nutrition from Day 4)

**Section 4: Pipeline Reports**
1. Navigate to pipeline/opportunity reporting
2. Look for:
   - Total pipeline value (sum of all open opportunities)
   - Conversion rate (what percentage of opportunities move from "New Inquiry" to "Won")
   - Average deal value
   - Deals by stage (how many are stuck in each stage of the Membership Sales pipeline from Day 5)

**Section 5: Conversation Reports**
1. Find conversation/communication reporting
2. Look for:
   - Total messages sent and received
   - Average response time (how quickly you respond to incoming messages)
   - Messages by channel (SMS, email, webchat, etc.)

**Section 6: Attribution Reports**
1. Look for source or attribution reporting
2. This answers the critical question: "Which lead source performs BEST?"
3. The ideal attribution report shows: Source (Google, Instagram, Referral, etc.) --> Contacts Created --> Appointments Booked --> Deals Won --> Revenue
4. For Sunrise Wellness, this would tell you whether to invest more in Instagram ads or Google ads based on which one actually produces paying members, not just leads

> **Pro Tip:** Many GHL users set up the system but never look at reports. This is a mistake. Schedule 15 minutes every Monday morning to review the dashboard. Catching a problem early (like a rising no-show rate) lets you fix it before it becomes a crisis.

### Exercise 10.10: Design the "Studio Owner's Weekly Report" Checklist

**Purpose:** Create a simple checklist that the Sunrise Wellness Studio owner would review every Monday morning in 15 minutes. This is not a GHL feature -- it is a business practice document that tells you WHERE to look and WHAT to look for.

Write out this checklist (in a notes document, text file, or just on paper):

```
SUNRISE WELLNESS STUDIO -- WEEKLY REPORT CHECKLIST
Review every Monday morning (15 minutes)

LEADS & CONTACTS
[ ] New contacts this week: _____  (Goal: 20+)
[ ] Lead sources breakdown: Google ___ | Instagram ___ | Referral ___ | Other ___
[ ] Leads in "New Inquiry" stage with no activity > 48 hours: ___
    Action: Follow up today if any are stale

APPOINTMENTS
[ ] Total appointments booked this week: _____  (Goal: 50+)
[ ] Show rate: _____%  (Goal: 85%+)
[ ] No-show rate: _____%  (Red flag if above 20%)
    Action: If no-show rate is high, review the reminder workflow timing

PIPELINE & REVENUE
[ ] New opportunities created: _____
[ ] Opportunities won (new members): _____
[ ] Opportunities lost: _____  (Why? Check notes)
[ ] Total pipeline value: $_____
[ ] Revenue collected this week: $_____

CONVERSATIONS
[ ] Average response time: _____ minutes  (Goal: under 15 min)
[ ] Unread messages right now: _____
    Action: Respond to all unread before end of day

REPUTATION
[ ] New reviews this week: _____  (Goal: 3+)
[ ] Average review rating: _____  (Goal: 4.5+)
[ ] Any negative reviews needing response? [ ] Yes [ ] No
    Action: Respond to all reviews within 24 hours

COMMUNITY
[ ] New community members this week: _____
[ ] Most active group: _____
[ ] Any unanswered questions in Q&A? [ ] Yes [ ] No
```

This checklist turns raw GHL data into actionable weekly decisions. It takes the reporting dashboard from "interesting" to "useful."

---

## Part 5: Phase 1 Self-Assessment

You have now completed all 10 days of Phase 1. Before moving to Phase 2 (where features combine into complex, real-world business systems), it is important to honestly assess where you stand.

### Confidence Rating

Rate yourself on a scale of 1 to 5 for each day's topic:

- **1** = I do not understand this at all, I need to redo the lesson
- **2** = I have a vague understanding but could not do it without step-by-step instructions
- **3** = I understand the concept and could do it with some reference checking
- **4** = I am comfortable and could do it independently
- **5** = I could teach this to someone else

| Day | Topic | Key Skills | Confidence (1-5) |
|-----|-------|-----------|-------------------|
| 1 | Dashboard & Settings | Business profile setup, custom values, dashboard customization | |
| 2 | Contacts & CRM | Import contacts, custom fields, tags, Smart Lists | |
| 3 | Conversations & Communication | SMS/Email templates, merge fields, webchat | |
| 4 | Calendars | Calendar types, booking widgets, availability settings | |
| 5 | Opportunities & Pipelines | Pipeline stages, opportunity management, deal tracking | |
| 6 | Payments & Invoicing | Products, invoices, coupons, payment links | |
| 7 | Marketing & Email | Email builder, campaigns, trigger links | |
| 8 | Sites, Forms & Surveys | Funnels, forms with custom fields, surveys, conditional logic | |
| 9 | Automation & Workflows | Triggers, actions, If/Else branching, certification recipes | |
| 10 | Reputation, Community, Reporting | Review requests, community groups, reporting metrics | |

### What to Do With Your Scores

- **Any topic rated 3 or below:** Go back and redo the hands-on exercises for that day before starting Phase 2. Phase 2 assumes solid competency in ALL Phase 1 topics because you will be combining multiple features in every lesson
- **Topics rated 4-5:** You are ready. These are your strengths
- **Pay special attention to Day 9 (Workflows):** This is the foundation for nearly everything in Phase 2. If you rated it below 4, spend extra time practicing before moving on

---

## Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental is a family dentistry practice. Patient reviews are critical for dental practices -- people are trusting you with their health, so they rely heavily on what other patients say. The practice also needs a patient education community (most patients have questions about brushing, flossing, and procedures) and clear reporting on patient acquisition and retention.

### Task 1: Reputation Management for BrightSmile

**Build the automated review request system:**

Post-appointment reviews are especially important for dental because dental anxiety is real. When a nervous patient reads "Dr. Chen was so gentle and explained everything -- I barely felt the filling!" it directly addresses their biggest fear.

Build this workflow:

```
[TRIGGER: Appointment Status --> Showed]
    |
    v
[Wait 3 hours]
  (Longer wait than Sunrise Wellness -- dental patients may need
   time for numbness to wear off before they feel like writing)
    |
    v
[Send SMS/Email: Review Request]
  "Hi {{contact.first_name}}, thank you for visiting BrightSmile
   Dental today! We hope your visit was comfortable. If you have
   a moment, we would love to hear about your experience:
   [REVIEW_LINK]
   Your review helps other patients feel confident about their
   dental care."
    |
    v
[Add Tag: "review-requested"]
    |
    v
[Wait 3 days]
    |
    v
[If/Else: Has tag "review-left"?]
  --> YES: Send thank-you email --> End
  --> NO: Send follow-up email with a different angle:
          "Your feedback helps us serve you better"
    |
    v
[Wait 5 days]
    |
    v
[Send final request + Tag "review-sequence-complete"]
```

**Create review response templates:**

Write template responses that the dental team would use:

- **5-Star Review Response:** "Thank you so much, {{contact.first_name}}! We are thrilled that you had a positive experience. Dr. Chen and the whole team appreciate your kind words. We look forward to seeing you at your next visit!"

- **3-4 Star Review Response:** "Thank you for your feedback, {{contact.first_name}}. We appreciate you sharing your experience and are always looking for ways to improve. If there is anything specific we could do better, please do not hesitate to reach out to us directly at [phone number]."

- **1-2 Star Review Response:** "We are sorry to hear that your experience did not meet your expectations, {{contact.first_name}}. Patient comfort is our top priority. We would like to understand what happened and make it right. Please call us at [phone number] so we can discuss this personally."

### Task 2: Community for BrightSmile -- "Dental Health Hub"

Set up a patient education community:

| Group | Access | Content Focus |
|-------|--------|---------------|
| **Welcome** | All Patients | Practice news, holiday closures, new services |
| **Dental Health 101** | All Patients | Brushing and flossing guides, when to call the dentist, common myths debunked |
| **Smile Gallery** | All Patients | Before/after photos (with patient consent), treatment explanations |
| **Procedure Prep** | Patients with Upcoming Procedures | What to expect during cleanings, fillings, crowns, whitening, Invisalign. Reduces anxiety by removing the unknown |
| **Post-Treatment Care** | Recent Patients | Aftercare instructions for each procedure, what is normal vs. when to call |

Create 2 sample posts:
- "Dental Health 101" post: "The Right Way to Floss (It Is Not What You Think)" -- a friendly guide to proper flossing technique
- "Procedure Prep" post: "What to Expect During Your First Crown Procedure" -- step-by-step walkthrough to reduce patient anxiety

### Task 3: Weekly Report for BrightSmile

Design a dental-specific weekly report checklist focused on:

```
BRIGHTSMILE DENTAL -- WEEKLY REPORT
[ ] New patient inquiries: _____ (Goal: 15+)
[ ] Appointments booked: _____
[ ] Show rate: _____% (Dental target: 90%+)
[ ] Treatment acceptance rate: _____% (How many patients who received
    a treatment plan actually scheduled the procedure)
[ ] Average review rating: _____
[ ] New reviews this week: _____
[ ] Revenue from procedures: $_____
[ ] Outstanding invoices: $_____
```

---

## Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency does not need Google reviews the same way a local business does. Instead, they need **client testimonials** and **case study permissions** -- which serve a similar purpose (social proof) but are collected differently. They also need a client portal where active clients can access reports and resources, and a reporting dashboard focused on lead generation and client retention.

### Task 1: Reputation System for Elevate -- Testimonials and Case Studies

For an agency, reputation is built through client success stories, not star ratings. Build this workflow:

```
[TRIGGER: Custom Date Field "90 Days Since Onboarding"]
  (Or manually trigger at the 90-day mark -- long enough to have
   measurable results to reference)
    |
    v
[Send Email: Results Recap + Testimonial Request]
  - Subject: "90 days with Elevate - look at what we have accomplished"
  - Body: Summary of results achieved (template with placeholders
    for specific metrics). Then: "Would you be willing to share a
    brief testimonial about your experience working with us? It
    helps other business owners find the right partner."
  - Include a link to a simple testimonial form (2 fields:
    "Your testimonial" and "Can we use your name and company?")
    |
    v
[Add Tag: "testimonial-requested"]
    |
    v
[Wait 7 days]
    |
    v
[If/Else: Has tag "testimonial-received"?]
  --> YES: Send thank-you + ask: "Would you also be open to a brief
           case study interview? 15 minutes on Zoom -- we'll write
           everything and just need your approval." --> End
  --> NO: Send friendly follow-up: "Just a quick reminder about the
          testimonial request. Even 2-3 sentences would mean a lot."
    |
    v
[Wait 14 days]
    |
    v
[Tag: "testimonial-sequence-complete"]
```

### Task 2: Community for Elevate -- "Client Portal"

Set up a professional client portal:

| Group | Access | Content Focus |
|-------|--------|---------------|
| **Announcements** | All Clients | Agency news, platform updates (Google algorithm changes, new ad features), industry alerts |
| **Strategy & Insights** | All Clients | Monthly industry reports, marketing tips, best practices articles |
| **Your Reports** | All Clients | Monthly performance report posts (one thread per client, or a general "your report is ready" notification) |
| **Resource Library** | All Clients | Brand guidelines templates, content calendar templates, social media image size guides, SEO checklists |
| **Premium Strategy** | Premium Clients ($5K+/mo) | Advanced strategy discussions, early access to new services, priority Q&A with the agency founder |

Create 2 sample posts:
- "Strategy & Insights" post: "Google's Latest Algorithm Update: What It Means for Your Business" -- plain-English summary of a recent (or hypothetical) algorithm change with actionable advice
- "Resource Library" post: "Download: 2024 Social Media Image Size Guide" -- a reference document with dimensions for all major platforms

### Task 3: Weekly Report for Elevate

Design an agency-specific weekly report checklist:

```
ELEVATE DIGITAL AGENCY -- WEEKLY REPORT
[ ] New leads this week: _____ (Goal: 10+)
[ ] Strategy calls booked: _____
[ ] Proposals sent: _____
[ ] Proposal win rate: _____% (Goal: 30%+)
[ ] New clients onboarded: _____
[ ] Client retention rate: _____% (Goal: 95%+)
[ ] Contracts expiring in 30 days: _____
    Action: Start renewal conversation for each
[ ] Average response time to leads: _____ (Goal: under 1 hour)
[ ] Active client satisfaction: Any negative signals?
    [ ] Missed deadlines  [ ] Unanswered questions  [ ] Performance dips
[ ] Pipeline value: $_____ (total potential monthly retainer)
```

---

## Day 10 Recap

**What You Built Today:**
- Automated review request workflow (connecting to Day 4 calendars and Day 9 workflow patterns)
- Review request SMS and email templates
- Sunrise Wellness Inner Circle community with 5 tiered groups
- Sample content for each group
- Access control mapping between membership tags and community groups
- Organized media storage folder structure
- A clear understanding of reporting dashboards and how to read them
- A weekly report checklist for the studio owner

**Certification Review Questions:**

1. What is the recommended timing for sending a review request after a service appointment? Why not immediately?
2. How do you handle negative reviews within GHL? What is the difference between a public response and a private follow-up?
3. Explain how Community access tiers work -- how do tags or membership levels control which groups a member can see?
4. Name 5 key metrics a business owner should review weekly in the GHL reporting dashboard
5. What is attribution reporting, and why is it important for deciding where to spend marketing budget?
6. How does the review request workflow connect to the appointment workflows from Day 9?

---

## Phase 1 Complete!

Congratulations. Over 10 days, you have gone from a blank GHL sub-account to a fully-functioning automated business system for Sunrise Wellness Studio:

- **Day 1:** Built the foundation -- business profile, custom values, dashboard
- **Day 2:** Created the contact database -- imports, custom fields, tags, Smart Lists
- **Day 3:** Set up communications -- SMS/email templates, webchat, conversation management
- **Day 4:** Built booking calendars -- PT sessions, group classes, nutrition consultations
- **Day 5:** Created the sales system -- Membership Sales pipeline, Onboarding pipeline, opportunity tracking
- **Day 6:** Set up payments -- membership products, invoices, coupons, payment links
- **Day 7:** Launched marketing -- email campaigns, trigger links, behavioral tracking
- **Day 8:** Built the front door -- Free Trial funnel, lead capture forms, member survey
- **Day 9:** Automated everything -- workflows for leads, no-shows, missed calls, reminders, and personalized nurture
- **Day 10:** Added the finishing touches -- reputation management, community portal, reporting

Every piece connects to every other piece. That is the power of GHL -- it is not 10 separate tools, it is one integrated system.

---

## What Comes Next: Phase 2 Preview

Phase 2 (Days 11-17) shifts from building individual features to **combining them into real-world business scenarios.** Instead of learning one feature per day, you will tackle multi-feature challenges:

- **Day 11:** Multi-Channel Lead Capture -- combine Sites, Forms, Contacts, and Automation into a complete lead generation machine
- **Day 12:** Sales Pipeline Automation -- connect CRM, Pipeline, Calendar, and Workflows into an automated sales system
- **Days 13-17:** Increasingly complex real-world integration scenarios

Phase 2 assumes solid competency in ALL Phase 1 topics. If any area on your self-assessment scored below 3, review that day's lesson before starting Phase 2.

Take a breather. You have earned it. Then, when you are ready, let's take everything you have built and make it work even harder.
