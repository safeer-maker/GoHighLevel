# Day 5: Opportunities & Pipelines

**Time Required:** 2-3 hours
**Certification Alignment:** Pipelines, Opportunities
**API Lab:** Yes - `scripts/day-05-opportunities-api.py`

---

## Today's Mission

Your Sunrise Wellness Studio now has contacts in the CRM (Day 2), communication templates ready to send (Day 3), and booking calendars for PT sessions, group fitness classes, and nutrition consultations (Day 4). But here is the problem: someone fills out a form expressing interest in a Premium membership. Another person finishes their 7-day free trial yesterday. A third person called last Tuesday asking about VIP pricing. How do you know where each of these people stands? Who needs a follow-up call? Who is about to sign up? Who went cold?

That is where **Pipelines and Opportunities** come in. Today you will build a visual sales tracking system that shows every potential member's journey from first inquiry to paid membership -- and a second pipeline for onboarding new members after they sign up. By the end of today, you will never lose track of a lead again.

---

## Learning Objectives

1. Understand what pipelines and opportunities are and why every business needs them
2. Design and build a multi-stage sales pipeline for Sunrise Wellness Studio
3. Create and manage opportunities (individual deals) through the pipeline
4. Build a second pipeline for member onboarding
5. Calculate pipeline metrics for sales forecasting

---

## Part 1: Understanding Pipelines & Opportunities (20 min)

### What is a Pipeline?

A **pipeline** is a visual board that shows the stages of a process. If you have ever used Trello, Jira, or any Kanban-style board, the concept is identical: columns represent stages, and cards move from left to right as they progress.

Think of it like a conveyor belt at a factory. Raw material enters on the left, goes through processing stages, and a finished product comes out on the right. In your case, the "raw material" is a new lead who expressed interest, and the "finished product" is a paying member at Sunrise Wellness Studio.

Here is what it looks like in practice:

```
New Inquiry --> Contacted --> Trial Booked --> Trial Active --> Follow-Up --> Member!
```

Each column is a **stage**. Each card moving through those columns is an **opportunity**.

### What is an Opportunity?

An **opportunity** is a single potential deal sitting at a specific stage. It represents one person's journey through your pipeline. For example:

- "Jane Doe - Interested in Premium Membership - $149/mo" is an opportunity
- It sits in the "Trial Booked" stage because Jane has a free trial starting Monday

Every opportunity has four key pieces of information:
- **Contact** -- the person (linked to their CRM record from Day 2)
- **Stage** -- where they are in the process right now
- **Value** -- how much the deal is worth in dollars
- **Status** -- open (still in progress), won (they signed up), or lost (they decided not to)

### Why Do You Need This?

Without a pipeline, you are tracking leads in your head, on sticky notes, or in a spreadsheet that gets outdated the moment you close the tab. With a pipeline:

- **You instantly see how many leads are at each stage** -- one glance tells you that 5 people are in free trials right now
- **You know who needs follow-up** -- anyone sitting in a stage too long gets attention
- **You can forecast revenue** -- 8 people in trials at $149/mo average means roughly $1,192/mo in potential new revenue
- **You never lose track of a potential member** -- every inquiry has a card, every card has a next action
- **Your team stays aligned** -- if you hire a front desk person, they can see exactly where every lead stands without asking you

> **Pro Tip:** Pipelines are not just for sales. You can create a pipeline for any multi-step process: member onboarding, event planning, partnership outreach, even internal projects. If it has stages, it can be a pipeline.

### Pipeline Design Principles

Before you start building, keep these rules in mind:

1. **Keep it simple** -- 4-7 stages is the sweet spot. Fewer than 4 and you lack visibility. More than 7 and people stop updating because it feels like busywork.
2. **Each stage needs a clear action** -- Moving a card forward means something specific happened. "Contacted" means you actually reached out. "Trial Booked" means a calendar booking exists.
3. **Define entry criteria** -- Everyone on the team should agree on what qualifies a deal to enter a stage. No ambiguity.
4. **Always have endpoints** -- You need both a "Won" and a "Lost" stage. Deals that stay open forever pollute your data.
5. **Match your real process** -- Do not copy a template pipeline if it does not reflect how Sunrise Wellness actually converts leads. Build what matches reality.

---

## Part 2: Build the Sunrise Wellness Sales Pipeline (45 min)

### What is This Pipeline For?

This is the **Membership Sales Pipeline** -- the primary pipeline for Sunrise Wellness Studio. It tracks every person from the moment they show interest to the moment they become a paying member (or decide not to join). This connects directly to the work you have already done:

- Contacts from Day 2 become opportunities here
- Templates from Day 3 are what you send at each stage
- Calendar bookings from Day 4 move people from "Contacted" to "Trial Booked"

### Hands-On Exercise 5.1: Create Your Sales Pipeline

*This exercise teaches you to design and build a pipeline from scratch.*

Navigate to **Opportunities > Pipelines** (left sidebar) and click **+ Create Pipeline**.

**Pipeline Name:** "Membership Sales"

Create these 7 stages in order:

| # | Stage Name | What It Means | How Someone Gets Here |
|---|-----------|--------------|----------------------|
| 1 | New Inquiry | Someone expressed interest in Sunrise Wellness | Filled out a website form, called the studio, walked in, sent a DM, or was referred by a friend |
| 2 | Contacted | You have reached out to them | You sent an SMS, email, or made a phone call (using templates from Day 3) |
| 3 | Trial Booked | Their free 7-day trial is scheduled | They booked through a calendar (Day 4) or you booked on their behalf |
| 4 | Trial Active | They are currently experiencing the studio | They showed up for their first session -- they are in the building! |
| 5 | Trial Follow-Up | Their trial is ending soon, decision time | Day 5-7 of their trial. This is the critical conversion window. |
| 6 | Closed - Member | They signed up and paid! | Selected a membership plan (Basic $79, Premium $149, VIP $249, or Annual $790) |
| 7 | Closed - Not Now | They decided not to join at this time | Budget, timing, or fit was not right |

**To create each stage:**
1. Click **Add Stage** (or the + button)
2. Type the stage name exactly as shown above
3. Drag stages to reorder if needed -- they should flow left to right from New Inquiry to the Closed stages
4. Optionally set stage colors for visual clarity (suggestion: green for "Closed - Member", red for "Closed - Not Now", blue for middle stages)

> **Pro Tip:** Notice the stage is called "Closed - Not Now" instead of "Lost." This is intentional. "Lost" sounds final. "Not Now" leaves the door open -- these contacts go into a nurture email sequence and many will come back in 1-3 months. The language matters for both your mindset and your team's.

### Hands-On Exercise 5.2: Populate Your Pipeline with Opportunities

*This exercise teaches you to create individual opportunities and associate them with contacts.*

Now that the pipeline structure exists, you need deals in it. Create **10 sample opportunities** across different stages so you can practice managing a realistic pipeline.

For each opportunity below, follow these steps:
1. Click **+ Add Opportunity** (or the + button within a specific stage)
2. **Name** the opportunity (this is typically the person's name + what they are interested in)
3. **Select or create the contact** -- some will use contacts from your Day 2 database, others you will create fresh
4. **Set the stage** by placing it in the correct column
5. **Set the monetary value** -- this represents the membership price they would pay
6. **Set the expected close date** -- when you think this deal will close (pick dates within the next 2-4 weeks)
7. **Add notes** about the opportunity

| Opportunity Name | Contact | Stage | Value | Notes |
|-----------------|---------|-------|-------|-------|
| Sarah - Premium Interest | Sarah Williams (from Day 2) | New Inquiry | $149/mo | Found us on Instagram, asked about class schedule |
| Mike - VIP Family Plan | Mike Johnson (from Day 2) | Contacted | $249/mo | Wants VIP for himself and wife, sent info packet via email |
| Lisa - Basic Starter | Create new: Lisa Chen | Trial Booked | $79/mo | Starting with Basic, trial begins Monday |
| James - HIIT Enthusiast | Create new: James Rodriguez | Trial Active | $149/mo | Day 3 of trial, loved the HIIT class, leaning Premium |
| Emma - Nutrition + VIP | Create new: Emma Thompson | Trial Follow-Up | $249/mo | Day 6 of trial, raving about the nutrition consultation, strong VIP candidate |
| Tom - Corporate Annual | Create new: Tom Baker | Contacted | $790/yr | Annual plan, corporate wellness budget, needs invoice for employer |
| Raj - Returning Member | Create new: Raj Patel | New Inquiry | $79/mo | Was a member 6 months ago, wants to rejoin, starting with Basic |
| Ana - Yoga Focus | Create new: Ana Martinez | Trial Active | $149/mo | Day 4 of trial, only interested in yoga classes, considering Premium |
| David - New Member | Create new: David Kim | Closed - Member | $149/mo | Signed up for Premium yesterday after a great trial week! |
| Karen - Budget Pause | Create new: Karen White | Closed - Not Now | $79/mo | Enjoyed the trial but has budget concerns, revisit in 3 months |

After creating all 10, step back and look at your pipeline in Kanban view. You should see cards distributed across the stages, giving you a visual snapshot of your "sales funnel."

### Hands-On Exercise 5.3: Work the Pipeline

*This exercise teaches you to interact with the pipeline view -- the day-to-day actions you will perform.*

Now that your pipeline has data, practice the core actions:

1. **Kanban View** -- This is the default view. Each stage is a column, each opportunity is a card. Observe how the layout gives you an instant read on your business health.

2. **Drag and Drop** -- Simulate a real update: you just called Raj Patel about rejoining. Drag "Raj - Returning Member" from **New Inquiry** to **Contacted**. This is the most common pipeline action -- moving a deal forward after taking action.

3. **Filter Opportunities** -- Click the filter icon and try these:
   - Show only "Trial Active" opportunities (who is in the building right now?)
   - Show only opportunities with value above $149/mo (who are the high-value prospects?)
   - Show only opportunities in "New Inquiry" and "Contacted" (who still needs outreach?)

4. **Sort by Value** -- Within a stage, sort opportunities by monetary value. This helps you prioritize: if you only have time to follow up with one Trial Follow-Up lead today, pick the highest-value one.

5. **Pipeline Summary** -- Look at the stage totals. What is the total dollar value sitting at each stage? This is your **pipeline snapshot** -- it tells you at a glance how much potential revenue is in play.

### Hands-On Exercise 5.4: Dive Into Opportunity Details

*This exercise teaches you to work inside a single opportunity record.*

Click on "Emma - Nutrition + VIP" to open the opportunity detail view:

1. **View the linked contact** -- Click through to Emma's contact record. You should see her CRM data from Day 2's structure (name, email, phone, custom fields).

2. **Add a note** -- In the opportunity notes section, type: "Day 6 of trial. Emma completed 3 HIIT classes and 1 nutrition consultation. She specifically mentioned loving the personalized nutrition plan. Leaning heavily toward VIP for the unlimited nutrition access. Follow up tomorrow with the VIP benefits breakdown email."

3. **Check the activity timeline** -- This shows all interactions: emails sent, calls made, notes added. Over time, this becomes the complete history of the deal.

4. **Update the value** -- If Emma mentioned she also wants the Protein Starter Kit ($45 one-time on top of VIP), you could note that or adjust the value to reflect total first-month spend.

5. **Move to next stage** -- If you just had a conversion call with Emma and she said "Send me the payment link," you would move her from Trial Follow-Up to Closed - Member. (For now, leave her in Trial Follow-Up since we are just practicing.)

---

## Part 3: Member Onboarding Pipeline (30 min)

### What is an Onboarding Pipeline?

When someone becomes a member (moves to "Closed - Member" in the sales pipeline), their journey is not over -- it is just beginning. The first 30 days of a new membership determine whether someone stays for years or cancels after month one.

An **onboarding pipeline** ensures every new member gets a consistent, high-quality first experience. Without it, some new members get a great welcome while others fall through the cracks depending on how busy the front desk is that day.

Think of it this way: the sales pipeline answers "Did they sign up?" The onboarding pipeline answers "Are they actually engaged and likely to stay?"

### Why a Separate Pipeline?

You might wonder: "Why not just add more stages to the sales pipeline?" Because they serve different purposes:

- **Sales pipeline** = pre-sale. Goal: convert leads to members. Measured by conversion rate.
- **Onboarding pipeline** = post-sale. Goal: activate and retain new members. Measured by engagement and retention.

Mixing them creates a single pipeline with 12+ stages, which violates the "keep it simple" principle. Separate pipelines keep each process focused.

### Hands-On Exercise 5.5: Create the Onboarding Pipeline

*This exercise teaches you to build a second pipeline and understand that pipelines serve different business functions.*

Navigate to **Opportunities > Pipelines** and click **+ Create Pipeline**.

**Pipeline Name:** "New Member Onboarding"

| # | Stage Name | What Happens Here | How Long |
|---|-----------|-------------------|----------|
| 1 | Welcome | Contract signed, first payment received, welcome email sent (using Day 3 templates) | Day 0 |
| 2 | Orientation Scheduled | First PT session or studio tour booked (using Day 4 calendars) | Days 1-3 |
| 3 | First Session Complete | They attended their first class or PT session -- they have physically been in the studio | Days 3-7 |
| 4 | 2-Week Check-In | Phone call or in-person chat: "How's everything going? Any questions?" | Day 14 |
| 5 | 30-Day Review | Formal feedback: engagement survey, attendance review, are they hitting their goals? | Day 30 |
| 6 | Established Member | Fully onboarded. Regular attendance pattern. They know the studio, the staff, and their routine. | Day 30+ |

**After creating the pipeline, add 3 opportunities:**

1. **David - New Premium Member** -- Move David Kim (who was "Closed - Member" in the sales pipeline) into this pipeline at the "Welcome" stage. He just signed up yesterday!
2. **Create: Priya Sharma - Basic Onboarding** -- Priya signed up for Basic last week and has her orientation tour tomorrow. Place her in "Orientation Scheduled."
3. **Create: Marcus Lee - VIP First Month** -- Marcus is a VIP member who joined 3 weeks ago and has attended 8 classes. Place him in "30-Day Review."

> **Pro Tip:** Pipelines are not just for sales. Any multi-step process where you need visibility and accountability can be a pipeline: member onboarding, event planning, partnership outreach, complaint resolution, even equipment procurement. If it has stages, it can be a pipeline.

---

## Part 4: Pipeline Analytics & Metrics (15 min)

### What Are Pipeline Metrics?

Raw opportunity data becomes powerful when you do basic math with it. **Pipeline metrics** tell you the health of your business: Are you generating enough leads? Are they converting? How much revenue can you expect next month?

You do not need fancy reporting tools for this -- you can calculate everything from the pipeline you just built.

### Hands-On Exercise 5.6: Calculate Your Pipeline Metrics

*This exercise teaches you to extract actionable business insights from pipeline data.*

Using your 10 test opportunities from Exercise 5.2, calculate the following (grab a calculator or do it by hand):

**1. Total Open Pipeline Value**
Add up the monetary value of all opportunities that are NOT in "Closed - Member" or "Closed - Not Now":
- New Inquiry: Sarah $149 + Raj $79 = $228
- Contacted: Mike $249 + Tom $790 = $1,039
- Trial Booked: Lisa $79 = $79
- Trial Active: James $149 + Ana $149 = $298
- Trial Follow-Up: Emma $249 = $249
- **Total open pipeline value = $______** (calculate it yourself and verify)

**2. Average Deal Size**
Total open pipeline value / number of open deals = $____

**3. Win Rate**
Won opportunities / (Won + Lost) = David / (David + Karen) = 1/2 = **50%**
(With only 2 closed deals, this is not statistically meaningful, but you now know how to calculate it.)

**4. Weighted Pipeline Value**
This is the most useful metric. Not every open deal will close. Deals further along in the pipeline are more likely to close than fresh inquiries. Assign a probability to each stage:

| Stage | Probability | Why |
|-------|------------|-----|
| New Inquiry | 10% | Most inquiries do not convert |
| Contacted | 20% | You have made contact, slight improvement |
| Trial Booked | 40% | They committed to trying the studio |
| Trial Active | 60% | They are physically experiencing the product |
| Trial Follow-Up | 80% | They have completed the trial and are deciding |

**Weighted value** = (Each opportunity's value x its stage probability)

Calculate it for each open opportunity:
- Sarah: $149 x 0.10 = $14.90
- Raj: $79 x 0.10 = $7.90
- Mike: $249 x 0.20 = $49.80
- Tom: $790 x 0.20 = $158.00
- Lisa: $79 x 0.40 = $31.60
- James: $149 x 0.60 = $89.40
- Ana: $149 x 0.60 = $89.40
- Emma: $249 x 0.80 = $199.20

**Total weighted pipeline value = $______** (add them up)

This number is your realistic revenue forecast. It is far more useful than the raw total because it accounts for the likelihood of each deal actually closing.

> **Pro Tip:** Track these metrics weekly. If your weighted pipeline value is dropping, you need more leads at the top of the funnel. If deals are piling up in "Trial Follow-Up" without closing, your conversion process needs work. The numbers tell you exactly where to focus.

---

## Part 5: API Lab - Pipeline Management

### Run the Opportunities API Lab

```bash
python scripts/day-05-opportunities-api.py
```

The script covers:
1. List all pipelines in your sub-account
2. Get pipeline stages for a specific pipeline
3. Create an opportunity via API
4. Update an opportunity's stage (move through the pipeline programmatically)
5. Search opportunities by stage or status

### API Exercises

These are stretch challenges for those comfortable with Python:

1. **Pipeline value calculator** -- Build a script that pulls all opportunities, groups them by stage, and calculates total value per stage plus the weighted pipeline value using the probabilities from Exercise 5.6.

2. **Stale opportunity finder** -- Create a function that identifies opportunities with no activity in 7+ days. These are deals that are going cold and need immediate attention.

3. **Pipeline report generator** -- Write a script that outputs a formatted report: opportunity count by stage, total value by stage, average deal size, and win rate. This is the kind of script the studio owner would run every Monday morning.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental - Patient Treatment Pipeline

**Situation:** BrightSmile Dental Clinic (2 dentists, 1 hygienist, 1 front desk) needs to track patients from initial inquiry through treatment completion. Unlike Sunrise Wellness where the "product" is a membership, dental patients often need specific procedures with per-procedure pricing. A single patient might need multiple treatments over several visits.

**Your Task:**

**1. Design and create a "Patient Treatment Pipeline":**

| # | Stage | What It Means |
|---|-------|--------------|
| 1 | New Patient Inquiry | Someone called, messaged, or submitted a form asking about dental services |
| 2 | Consultation Scheduled | An initial exam/consultation is booked on the calendar |
| 3 | Exam Complete | The dentist has assessed the patient and created a treatment plan |
| 4 | Treatment Proposed | The patient received the cost estimate and treatment plan details |
| 5 | Treatment Accepted | The patient agreed to proceed, payment plan arranged if needed |
| 6 | In Treatment | Active procedures in progress (may span multiple visits) |
| 7 | Treatment Complete | All planned procedures are finished, final follow-up done |
| 8 | Declined - Not Proceeding | Patient chose not to proceed with recommended treatment |

**2. Create 5 sample opportunities with dental-specific details:**

| Opportunity Name | Value | Stage | Notes |
|-----------------|-------|-------|-------|
| John Smith - Crown Replacement | $1,200 | Consultation Scheduled | Referred by existing patient, chipped tooth |
| Maria Garcia - Whitening Package | $450 | Treatment Proposed | Wants whitening before her wedding in 3 months |
| Bob Wilson - Full Orthodontics | $4,500 | Treatment Accepted | Monthly payment plan: $375/mo x 12 months |
| Sue Chen - Emergency Root Canal | $800 | In Treatment | Came in as emergency, procedure started same day |
| Tim Brown - General Checkup | $200 | Exam Complete | Routine exam, may need 2 fillings ($300 additional) |

**3. Design a second pipeline: "Insurance Claims Tracking"**

| # | Stage | What Happens |
|---|-------|-------------|
| 1 | Claim Submitted | Paperwork sent to insurance company |
| 2 | Under Review | Insurance company is processing |
| 3 | Approved | Claim approved, awaiting payment |
| 4 | Payment Received | Insurance payment deposited |
| 5 | Denied | Claim denied -- appeal or patient pays |

**Reflection questions:**
- How does a dental pipeline differ from a fitness pipeline? (Hint: one-time procedures vs. recurring memberships)
- Why would a dental clinic track insurance claims as a separate pipeline instead of adding stages to the treatment pipeline?

---

### Case Scenario 2: Elevate Digital Agency - Client Acquisition Pipeline

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media, Email Marketing, Web Design) needs to track prospective clients from lead to signed contract. Agency sales cycles are longer and involve larger deal values than fitness memberships. A single deal might be worth $2,000-$10,000 per month in recurring retainer revenue.

**Your Task:**

**1. Design and create a "Client Acquisition Pipeline":**

| # | Stage | What It Means |
|---|-------|--------------|
| 1 | Lead | Someone inquired about agency services (website form, referral, LinkedIn outreach) |
| 2 | Discovery Call Scheduled | A strategy call is booked (using a calendar like Day 4) |
| 3 | Discovery Complete | Needs assessed: which services, budget range, goals, timeline |
| 4 | Proposal Sent | Custom proposal delivered with scope, pricing, and timeline |
| 5 | Negotiation | Back-and-forth on scope, price, or terms |
| 6 | Contract Signed | Deal won -- retainer agreement signed, onboarding begins |
| 7 | Lost - No Budget / Bad Fit | Prospect chose another agency, does not have budget, or is not a good fit |

**2. Create 5 sample opportunities:**

| Opportunity Name | Value | Stage | Notes |
|-----------------|-------|-------|-------|
| TechStartup Inc - SEO + PPC | $5,000/mo | Proposal Sent | Series A startup, aggressive growth targets, 12-month contract proposed |
| Local Bakery - Social Media | $2,000/mo | Discovery Call Scheduled | Owner wants Instagram and Facebook management, small budget |
| LawFirm Partners - Full Suite | $10,000/mo | Negotiation | Want all 5 services, discussing whether to include web redesign in retainer or bill separately |
| FitGear Online - PPC Only | $3,000/mo | Contract Signed | E-commerce brand, Google and Meta ads, signed last Friday |
| Green Landscaping - Web Design | $8,000 project | Lead | Referral from existing client, needs a new website, not a retainer |

**3. Design a second pipeline: "Project Delivery"**

| # | Stage | What Happens |
|---|-------|-------------|
| 1 | Kickoff | Onboarding call, access credentials gathered, project brief signed off |
| 2 | Strategy | Research, audits, and strategy document created |
| 3 | Execution | Campaigns launched, content created, development in progress |
| 4 | Review | Client reviews deliverables, feedback round |
| 5 | Launched | Everything is live (website, campaigns, etc.) |
| 6 | Ongoing Management | Transitioned to monthly retainer management and reporting |

**Reflection questions:**
- Elevate Digital has both monthly retainers ($2K-$10K/mo) and one-time projects ($3K-$15K). How do you handle the pipeline value field for recurring vs. one-time deals?
- Why is "Discovery Complete" a separate stage from "Proposal Sent"? What happens between those two stages? (Hint: the agency needs time to research, analyze, and build a custom proposal.)
- How would you use `{{user.calendar}}` (from Day 4) to ensure each prospect always books with the same account manager?

---

## Day 5 Recap Questions

1. In plain English, what is a Pipeline and what is an Opportunity? How do they relate to each other?
2. How many stages should a pipeline have, and why not 15?
3. Why did we create TWO pipelines for Sunrise Wellness (Sales + Onboarding) instead of one long pipeline?
4. What is a "weighted pipeline value" and why is it more useful than just adding up all the deal values?
5. A lead has been sitting in "Trial Follow-Up" for 10 days without moving. What should happen, and what does this tell you about your process?
6. How would you use the GHL API to find all opportunities stuck in a single stage for too long?

---

## Next Day Preview

**Day 6: Payments & Invoicing** -- Sunrise Wellness needs to actually get paid! You will create all the studio's products (memberships, sessions, supplements, and packages), build invoices, set up promotional coupons like the "20% Off Your First Month" offer from Day 1's custom values, and explore Text2Pay for sending payment links via SMS. Even if you do not have Stripe connected, you will build the entire payment infrastructure so it is ready to go live.

Make sure you have:
- Both pipelines created (Membership Sales + New Member Onboarding)
- At least 10 opportunities in the sales pipeline across multiple stages
- A clear understanding of how pipeline stages map to real-world actions at the studio
