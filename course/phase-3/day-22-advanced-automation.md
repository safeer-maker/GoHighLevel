# Day 22: Advanced Automation Patterns

**Time Required:** 3-4 hours
**Level:** Expert

## Today's Mission
You have built dozens of workflows over 21 days. Today you level up to expert patterns: nested If/Else with 5+ conditions, math operations for lifetime value tracking, goal events that pause workflows intelligently, exponential backoff re-engagement, and complex lead routing. These patterns separate GHL power users from GHL experts.

## Learning Objectives
1. Build complex conditional logic with nested If/Else
2. Use math operations to track LTV and dynamic pricing
3. Implement goal events to pause/exit workflows
4. Design exponential backoff sequences
5. Debug workflows using execution logs

---

## Part 1: Complex Conditional Logic (60 min)

### Nested If/Else Patterns

Simple workflows have one condition. Real business logic often has 3-5 layered decisions.

### Exercise 22.1: Smart Lead Router for Sunrise Wellness

**Goal:** Route each lead to the right sales treatment based on multiple signals.

```
[TRIGGER: Tag "new-trial-lead" added]
    |
[Check Fitness Goals custom field]
    |
    +-- Weight Loss --+
    |                 |
    |    [Check Budget Range]
    |         |
    |         +-- > $150 --+
    |         |            |
    |         |   [Check Experience Level]
    |         |        |
    |         |        +-- Advanced -> Recommend VIP, assign to Alex (Lead Trainer), send "Premium+ email"
    |         |        +-- Intermediate -> Recommend Premium + PT consult booking
    |         |        +-- Beginner -> Recommend Premium with gentle-start plan
    |         |
    |         +-- $80-150 -> Recommend Basic + "Worth the upgrade" nurture
    |         +-- < $80 -> Send value-first content, nurture 14 days
    |
    +-- Muscle Gain --+
    |                 |
    |    [Assign to Alex (Lead Trainer)]
    |    [Book PT consult via {{user.calendar}}]
    |    [Send "Meet your trainer" email]
    |
    +-- Flexibility/Stress Relief --+
    |    [Assign to Jordan (Yoga specialist)]
    |    [Book trial class]
    |    [Send yoga-focused welcome]
    |
    +-- Default --> Generic welcome nurture
```

**Build in GHL:**

1. Trigger: Tag Added = "new-trial-lead"
2. Add If/Else action
3. First condition: Custom Field "Fitness Goals" contains "Weight Loss"
4. On YES branch: Add another If/Else for Budget Range
5. Continue nesting up to 5 levels deep

**Pro Tip:** After 3 levels deep, consider splitting into separate workflows called via "Move to Workflow" action. More maintainable.

### Exercise 22.2: AND vs OR Logic

**Scenario:** Identify high-value members for VIP upsell campaign

Condition: `(Has tag "premium-member" AND joined > 90 days ago) OR (Opportunity value > $500)`

In GHL's condition builder:
- Use "All" for AND groups
- Use "Any" for OR groups
- You can nest AND groups inside OR groups

```
[IF (tag = 'premium-member' AND join_date < 90 days ago) OR opportunity_value > 500]
  -> Send VIP upgrade offer
[ELSE]
  -> Continue standard nurture
```

---

## Part 2: Math Operations and Custom Values (45 min)

### What Are Math Actions?

GHL workflows can do math on custom fields and custom values:
- Add, subtract, multiply, divide
- Update custom field based on calculation
- Track running totals

### Exercise 22.3: Member Lifetime Value Tracker

**Setup:**
1. Create Custom Field: "Lifetime Value" (Number) on contacts
2. Create Custom Field: "Payment Count" (Number)

**Workflow: "Track LTV on Payment"**

```
[TRIGGER: Payment Received]
    |
[Math Action: Add payment amount to Lifetime Value]
  Lifetime Value = Lifetime Value + {{payment.amount}}
    |
[Math Action: Increment Payment Count]
  Payment Count = Payment Count + 1
    |
[IF Lifetime Value > 1000]
  -> Add tag "vip-candidate"
  -> Internal notification: "Member reached $1K LTV: {{contact.first_name}}"
[ELSE IF Lifetime Value > 500]
  -> Add tag "high-value-member"
```

**Use case:** After a year, you know exactly which members have spent the most. Target them for annual plan upgrades, referral requests, testimonials.

### Exercise 22.4: Dynamic Referral Discount

**Setup:**
1. Custom Field: "Referral Count" (Number)
2. Each successful referral increments this

**Workflow: "Reward Referrers"**

```
[TRIGGER: Tag "referred-someone" added]
    |
[Math: Referral Count + 1]
    |
[IF Referral Count = 3]
  -> Apply REFERRAL coupon (free PT session)
  -> Send celebration email: "You referred 3 friends! Here's a free session 💪"
    |
[IF Referral Count = 5]
  -> Send: "You've unlocked VIP ambassador status!"
  -> Add tag "brand-ambassador"
```

### Discount Calculation Example

```
Custom Field: Discount Percent = (Referral Count * 5)
(Each referral = 5% off, capped at 25%)

In workflow:
[Math: Discount = Referral Count * 5]
[If Discount > 25]
  [Set Discount = 25]  // Cap it
[Apply coupon with Discount %]
```

---

## Part 3: Goal Events (45 min)

### What Are Goals?

Goals are events that PAUSE or EXIT a workflow when achieved. Critical for nurture sequences.

**Problem without goals:**
- Send 7-email nurture
- Lead converts on email 3
- Leads still gets emails 4-7 (annoying, unprofessional)

**Solution with goals:**
- Set goal "Trial Booked" on the workflow
- When achieved, workflow stops immediately

### Exercise 22.5: Nurture Sequence with Goal

**Workflow: "Lead Magnet Nurture"** (from Day 16)

```
[TRIGGER: Form Submitted "Free Meal Plan"]
    |
[GOAL SET: Tag "trial-booked" added] <-- defined once at workflow level
    |
[Email 1: Meal plan delivery]
[Wait 2 days]
[Email 2: Value content]
[Wait 2 days]
[Email 3: Success story]
[Wait 3 days]
[Email 4: Product spotlight]
[Wait 2 days]
[Email 5: Community]
[Wait 2 days]
[Email 6: Offer]
[Wait 3 days]
[Email 7: Last chance]
    |
[End]
```

**How it works:**
- At ANY point during the sequence, if the contact gets tagged "trial-booked"
- The workflow exits IMMEDIATELY
- No more emails sent
- Optional: trigger a new workflow ("Trial Booked Sequence")

### Exercise 22.6: Multi-Goal Workflow

Some nurture needs multiple goals:

**Sunrise Wellness Master Nurture Goals:**
- Goal 1: "trial-booked" → stop, they're in the trial sequence now
- Goal 2: "active-member" → stop, they converted, now in onboarding
- Goal 3: "unsubscribed" → stop, respect their wish

Build workflow with multiple goals - achieving ANY one stops the flow.

### Goal Types in GHL

| Goal Type | Example |
|-----------|---------|
| **Tag Added** | Tag "trial-booked" added |
| **Tag Removed** | Tag "subscribed" removed |
| **Opportunity Status** | Opportunity marked "Won" |
| **Custom Field Change** | "Membership Status" = "Active" |
| **Appointment Status** | Appointment marked "Showed" |

---

## Part 4: Exponential Backoff Re-Engagement (30 min)

### What Is Exponential Backoff?

Gaps between messages grow larger over time. Respects the user, reduces unsubscribes.

**Standard sequence:**
Day 1 → Day 4 → Day 11 → Day 25 → Day 55 → Day 115

### Exercise 22.7: Lapsed Member Win-Back

**Trigger:** Tag "cancelled" added (member cancelled membership)

```
[TRIGGER: Tag "cancelled" added]
    |
[Remove tags: "active-member", "auto-renew"]
[Add tag: "win-back-sequence"]
    |
[GOAL: Tag "active-member" added] <-- they rejoin
    |
--- Day 1 ---
[Email: "We're sorry to see you go"]
Body: Heartfelt, no pressure, asks for feedback
    |
[Wait 3 days]
    |
--- Day 4 ---
[Email: "What could we have done better?"]
Include: Survey link (2-minute, 5 questions)
    |
[Wait 7 days]
    |
--- Day 11 ---
[Email: "A fresh start offer"]
Include: WELCOME20 coupon, new class highlights
    |
[Wait 14 days]
    |
--- Day 25 ---
[Email: "Checking in"]
Soft touch, share a member transformation story
    |
[Wait 30 days]
    |
--- Day 55 ---
[Email: "One final offer"]
$49 first month (deeper discount than WELCOME20)
    |
[Wait 60 days]
    |
--- Day 115 ---
[Add tag "cold-do-not-email"]
[Remove from active marketing lists]
[Move to long-term quarterly newsletter only]
```

**Why it works:**
- Immediate contact feels caring, not pushy
- Gaps grow so they forget you briefly then remember
- Deeper discounts over time catches budget-sensitive leads
- Final cutoff prevents endless nagging

---

## Part 5: Workflow Debugging (45 min)

### Reading Execution Logs

Every workflow execution is logged. Open Automation > Workflows > [workflow name] > Execution Log.

Each entry shows:
- Contact
- Start time
- Each step that fired
- Each condition evaluation
- Any errors or skips

### Exercise 22.8: Debug a Broken Workflow

**Scenario:** You built a workflow that should send a welcome SMS when someone fills the trial form. It's not firing. Troubleshoot:

**Step 1: Check the trigger**
- Did the form submission actually happen?
- Is the trigger matching the right form?

**Step 2: Check contact data**
- Does the contact have a phone number?
- Is the phone number in correct format?

**Step 3: Check conditions**
- Are there If/Else conditions that skip SMS?
- Tag conditions - does the contact have/not have the required tag?

**Step 4: Check GHL account**
- Does your sub-account have a phone number?
- Is A2P 10DLC registered?

**Common bugs:**
1. Tag case-sensitivity ("Premium" vs "premium")
2. Missing custom field values
3. Trigger firing before data populates (add 1-min wait after trigger)
4. Workflow paused or disabled
5. Rate limit hit on SMS/email

### Exercise 22.9: Testing Protocol

**Before activating any workflow:**

1. Create test contacts for each branch path
2. Temporarily shorten all Wait steps to 1 minute
3. Run each path, verify each step fires
4. Check execution log for each test contact
5. After verification, restore real wait times
6. Mark workflow as tested (add to workflow description)

**Testing log template:**

```
WORKFLOW: New Trial Lead
DATE TESTED: 2024-03-15
TESTER: [name]

Test 1 - Happy Path (lead books trial within 24hr):
- Contact: test-happy@yopmail.com
- Filled form ✅
- Received welcome SMS ✅
- Received welcome email ✅
- Booked appointment within 24hr ✅
- Opportunity moved to "Trial Booked" ✅
- Day 2 follow-up SMS: DID NOT FIRE (correct, goal achieved) ✅

Test 2 - Slow Path (lead doesn't book):
- Contact: test-slow@yopmail.com
- Filled form ✅
- Received welcome SMS ✅
- No booking
- Day 2 follow-up SMS sent ✅
- Day 4 final email sent ✅
- Tagged "needs-manual-followup" ✅

PASS: Ready for production
```

---

## Part 6: Intelligent Lead Routing System (45 min)

### Exercise 22.10: Build a Complete Smart System

**Goal:** Combine everything from today into one production-grade system.

**"Sunrise Wellness Smart Lead Routing"**

Architecture:
```
Lead enters system (any channel)
    |
1. LEAD SCORING WORKFLOW
   - Calculate score from custom fields + tags
   - Tag tier: hot-lead (70+), warm-lead (40-69), cold-lead (<40)
    |
2. ROUTING WORKFLOW
   - Hot leads: Assign to best-available trainer, SMS within 5 min
   - Warm leads: 24-hour email nurture, then follow-up
   - Cold leads: Long-term monthly newsletter
    |
3. SLA ENFORCEMENT
   - If hot lead not contacted within 2 hours -> alert manager
   - If warm lead not responded in 48 hours -> escalate
    |
4. GOAL-BASED NURTURE
   - Goals: trial-booked, active-member, unsubscribed
   - Any goal → exit nurture, enter appropriate next workflow
    |
5. EXPONENTIAL BACKOFF
   - No conversion in 60 days → quarterly touchpoints only
```

**Implementation steps:**

1. Create lead scoring workflow (from Day 20)
2. Create tier-based routing workflow
3. Add SLA monitor with 2-hour timer
4. Add goal events to each nurture sequence
5. Add automatic "move to long-term" after 60 days
6. Test each branch with test contacts
7. Activate

This is the kind of system that takes a solo operator to a professional agency.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Treatment Plan Acceptance

**Build a workflow for high-value treatment plans:**

```
[TRIGGER: Opportunity moved to "Treatment Proposed"]
  (Value: $1,500+)
    |
[GOAL: Tag "treatment-accepted" added]
    |
--- Day 0 ---
[Send email: Treatment plan summary + payment options]
    |
[Wait 24 hours]
    |
[IF no response]
[Send SMS: "Any questions about your treatment plan?"]
    |
[Wait 3 days]
    |
[Send email: "Let's schedule a call to discuss"]
  Include: Dentist's calendar link
    |
[Wait 7 days]
    |
[Send personal email from dentist]
  "Hi [name], this is Dr. [name]. I want to make sure you have
  everything you need to make this decision. My direct line: XXX"
    |
[Wait 14 days - final]
    |
[Close as "Not Proceeding - No Response"]
[Send survey: "What made you decide not to proceed?"]
```

Multi-stage, multi-channel, respects the patient's decision window.

### Case Scenario 2: Elevate Digital Agency Proposal Follow-Up

```
[TRIGGER: Opportunity moved to "Proposal Sent"]
    |
[GOAL: Tag "contract-signed"]
    |
--- Day 0 ---
[Send email: Proposal PDF + executive summary]
    |
[Wait 2 days]
    |
[Send check-in: "Any initial thoughts?"]
    |
[Wait 3 days]
    |
[Send: "Want to walk through the proposal together?"]
  Include: 30-min call booking link
    |
[IF "interested-in-call" tag added]
  [Assign account manager]
  [Send confirmation]
[ELSE continue nurture]
    |
[Wait 5 days]
    |
[Send: "We might have flexibility on budget"]
  Customize based on their response patterns
    |
[Wait 7 days]
    |
[Send from agency owner: "Final check-in"]
    |
[Wait 3 days]
    |
[If no response, close as "Ghosted"]
[Tag: "re-engage-90-days"]
[Move to 90-day re-engagement sequence]
```

---

## Integration Checkpoint

- [ ] Built nested If/Else with 5+ conditions
- [ ] Implemented math action (LTV tracker)
- [ ] Added goal to a nurture workflow
- [ ] Built exponential backoff sequence
- [ ] Tested workflow with test contacts
- [ ] Reviewed execution logs
- [ ] Documented testing in a log

## Day 22 Recap Questions

1. What is a goal event and why use it in nurture workflows?
2. When should you split a deep nested If/Else into multiple workflows?
3. What's exponential backoff? Give a typical sequence.
4. What 3 things should you check first when debugging a broken workflow?
5. How do you track Lifetime Value using workflows?

## Next Day Preview

**Day 23: App Marketplace & Advanced Integrations** - Final day of Phase 3. Explore the App Marketplace, connect native integrations, and build a 3-tool custom integration.
