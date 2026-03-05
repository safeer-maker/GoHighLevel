# Day 5: Opportunities & Pipelines

**Time Required:** 2-3 hours
**Certification Alignment:** Pipelines, Opportunities
**API Lab:** Yes - `scripts/day-05-opportunities-api.py`

---

## Learning Objectives

1. Design effective multi-stage sales pipelines for different business types
2. Create, manage, and track opportunities through the pipeline
3. Use pipeline data for sales forecasting and team management
4. Manage pipelines and opportunities via the GHL API

---

## Part 1: Pipeline Design (30 min)

### Theory Recap

A **Pipeline** represents a sales or business process as a series of stages. Each stage represents a step in the journey. **Opportunities** are individual deals/leads moving through the pipeline.

Key concepts:
- **Pipeline** = The process (e.g., "Sales Pipeline")
- **Stage** = A step in the process (e.g., "Qualified", "Proposal Sent")
- **Opportunity** = An individual deal at a specific stage
- **Value** = The monetary value of the deal
- **Status** = Open, Won, Lost, Abandoned

### Pipeline Design Principles

1. **Keep it simple** - 4-7 stages max. Too many stages = confusion
2. **Each stage should require action** - Moving to the next stage means something happened
3. **Define clear criteria** - What exactly qualifies a deal to move to the next stage?
4. **Include win/loss stages** - Always have clear endpoints
5. **Match your actual process** - Don't copy someone else's pipeline if it doesn't match how you sell

---

## Part 2: Create Your First Pipeline (45 min)

### Hands-On Exercise 5.1: Build a Sales Pipeline

Navigate to **Opportunities > + Create Pipeline**:

**Pipeline: "Sales Pipeline"**

Create these stages (in order):

| Stage | Purpose | Criteria to Enter |
|-------|---------|-------------------|
| 1. New Lead | Fresh inquiry | Contact created from any source |
| 2. Contacted | Initial outreach made | SMS, email, or call attempt made |
| 3. Qualified | Lead is a good fit | Budget, need, timeline confirmed |
| 4. Appointment Set | Meeting scheduled | Calendar booking confirmed |
| 5. Proposal Sent | Offer presented | Proposal/quote delivered |
| 6. Negotiation | Discussing terms | Back-and-forth on pricing/scope |
| 7. Closed - Won | Deal completed | Payment received or contract signed |
| 8. Closed - Lost | Deal not happening | Lead chose competitor or not interested |

For each stage:
1. Set the stage name
2. Set the stage order
3. Optionally set a stage color for visual clarity

### Hands-On Exercise 5.2: Create Opportunities

Now populate your pipeline with test opportunities:

1. Click **+ Add Opportunity** (or drag from contacts)
2. Create **10 sample opportunities** across different stages:

| Opportunity Name | Contact | Stage | Value | Expected Close |
|-----------------|---------|-------|-------|---------------|
| Smith Corp Deal | John Smith | Qualified | $5,000 | Next month |
| Jane's Membership | Jane Doe | Appointment Set | $2,400 | This week |
| Johnson LLC Project | Mike Johnson | Proposal Sent | $15,000 | Next month |
| Williams Consulting | Sarah Williams | New Lead | $3,000 | Unknown |
| Brown Enterprise | (create new) | Contacted | $8,000 | 2 weeks |
| Davis Package | (create new) | Negotiation | $12,000 | This week |
| Wilson Starter | (create new) | New Lead | $1,200 | Next month |
| Taylor Premium | (create new) | Qualified | $7,500 | 3 weeks |
| Anderson VIP | (create new) | Closed - Won | $20,000 | Completed |
| Martinez Trial | (create new) | Closed - Lost | $4,000 | Lost |

For each opportunity:
- Set the monetary value
- Set the expected close date
- Add notes about the deal
- Assign to a team member (yourself)

### Hands-On Exercise 5.3: Manage the Pipeline View

1. **Kanban view:** See all opportunities as cards in columns (stages)
2. **Drag and drop:** Move an opportunity from "New Lead" to "Contacted"
3. **Filter opportunities:**
   - By assigned user
   - By value range
   - By expected close date
   - By stage
4. **Sort opportunities** within a stage by value (highest first)
5. **Pipeline value summary:** Note the total value at each stage and overall

### Hands-On Exercise 5.4: Opportunity Details

Open an opportunity and explore:
1. Contact information (linked from Contacts)
2. Activity timeline (messages, calls, notes)
3. Add a note: "Spoke with client, they're interested in the premium package"
4. Change the opportunity status
5. Update the value (e.g., after negotiation)
6. Move to the next stage

---

## Part 3: Second Pipeline (30 min)

### Hands-On Exercise 5.5: Create an Onboarding Pipeline

Create a second pipeline for post-sale client onboarding:

**Pipeline: "Client Onboarding"**

| Stage | Purpose |
|-------|---------|
| 1. Welcome | Contract signed, starting onboarding |
| 2. Setup | Account/service configuration |
| 3. Training | Client training/orientation |
| 4. Launch | Service goes live |
| 5. 30-Day Check | First milestone review |
| 6. Active Client | Successfully onboarded |

Create 3 opportunities in this pipeline to practice.

**Key insight:** Pipelines aren't just for sales. They can track any multi-step process: onboarding, project management, support tickets, hiring, etc.

---

## Part 4: Pipeline Analytics (15 min)

### Hands-On Exercise 5.6: Analyze Your Pipeline

Review your pipeline data:

1. **Total pipeline value:** Sum of all open opportunities
2. **Stage conversion:** What percentage of deals move from each stage to the next?
3. **Average deal size:** Total value / number of opportunities
4. **Stage duration:** How long do deals typically stay in each stage?
5. **Win rate:** Won deals / (Won + Lost deals)

Calculate these metrics manually for your 10 test opportunities. In production, GHL reporting handles this.

---

## Part 5: API Lab - Pipeline Management

```bash
python scripts/day-05-opportunities-api.py
```

The script covers:
1. List all pipelines
2. Get pipeline stages
3. Create an opportunity
4. Update opportunity stage (move through pipeline)
5. Search opportunities by stage/status

### API Exercises

1. Build a script that calculates total pipeline value per stage
2. Create a function that identifies "stale" opportunities (no activity in 7+ days)
3. Write a pipeline report: opportunities by stage, total value, average deal size

---

## Case Scenarios

### Case Scenario 1: SaaS Sales Pipeline

**Situation:** A SaaS company sells a $199/month software product. Their sales process:
1. Free trial sign-up (from website)
2. Onboarding call scheduled
3. Call completed - demo given
4. Trial active (14-day trial)
5. Follow-up at day 7
6. Trial ending - conversion attempt
7. Subscribed or Churned

**Your Task:**
1. Design and create this pipeline with appropriate stages
2. Create 10 opportunities at various stages with realistic values ($199/mo = $2,388/yr)
3. Create a Smart List of "Trial users about to expire" (Day 12-14 of trial)
4. Design the automation flow: what happens at each stage transition?
5. Calculate: If 30% convert from trial, what's the expected monthly revenue from your pipeline?

### Case Scenario 2: Home Services - Dual Pipeline

**Situation:** "Quick Fix Plumbing" needs:
- Sales Pipeline: Lead > Estimate Scheduled > Estimate Given > Approved > Job Scheduled > Job Completed > Paid
- Warranty Pipeline: Claim Received > Inspecting > Approved/Denied > Repair Scheduled > Completed

**Your Task:**
1. Create both pipelines
2. Populate each with 5 sample opportunities
3. Design the handoff: when a sales deal reaches "Job Completed," how does it move to warranty tracking?
4. Set opportunity values for the sales pipeline ($150-$5000 range)
5. Document the criteria for each stage transition

### Case Scenario 3: Pipeline Forecasting

**Situation:** You have 20 opportunities in your sales pipeline:
- 5 in Qualified ($50K total)
- 4 in Appointment Set ($35K total)
- 3 in Proposal Sent ($45K total)
- 2 in Negotiation ($30K total)

Historical conversion rates: Qualified>Appt: 60%, Appt>Proposal: 75%, Proposal>Negotiation: 50%, Negotiation>Won: 70%

**Your Task:**
1. Calculate the weighted pipeline value (value x probability of closing)
2. Forecast expected revenue for next month
3. Identify which stage needs the most attention for maximum impact

---

## Day 5 Recap Questions

1. What's the difference between a Pipeline and an Opportunity?
2. How many stages should a pipeline typically have, and why?
3. When would you create multiple pipelines vs. one pipeline with more stages?
4. How do you calculate a weighted pipeline value?
5. What API endpoint do you use to move an opportunity to a different stage?
6. A sales manager says "I can't see my team's deals." What permission or setting would you check?

---

## Next Day Preview

**Day 6: Payments & Invoicing** - You'll set up products, create invoices, configure payment processing, and use the API for payment operations.
