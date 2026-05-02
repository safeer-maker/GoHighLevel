# Advanced Challenge 1: Build a Complete Referral Engine

**Difficulty:** Advanced
**Time Required:** 4-6 hours
**Prerequisites:** Phase 1 (Days 1-10) + Phase 2 (Days 11-16)

---

## The Challenge

Sunrise Wellness Studio's best leads come from referrals - members who love the studio and tell their friends. But right now, referrals happen randomly and nobody tracks them. Your job: build a **complete automated referral system** that:

1. Makes it dead-simple for members to refer friends
2. Tracks every referral from source to conversion
3. Rewards both the referrer AND the new member automatically
4. Reports on referral performance

This challenge gives you the WHAT and the WHY, but not step-by-step HOW. You need to figure out which GHL features to combine and how to wire them together.

---

## Business Requirements

### The Offer
- **Referrer reward:** Free PT session ($75 value) for every friend who signs up
- **New member reward:** $20 off first month (TRIALCONVERT coupon or a new REFERRAL coupon)
- **Double reward:** If 3 friends sign up in one month, referrer gets a free month

### The Experience

**For the existing member (referrer):**
1. Gets a unique referral link or code
2. Shares it with friends via text, email, or social
3. Gets notified when a friend signs up
4. Automatically receives their reward

**For the new prospect (referred friend):**
1. Clicks the referral link and lands on a special "Referred by a Friend" funnel page
2. Sees the $20-off offer
3. Signs up for a free trial
4. When they convert to paid, the referrer gets rewarded

### Tracking Requirements
- Know WHO referred WHO (contact-to-contact relationship)
- Track: referrals sent, trials started, conversions, rewards earned
- Monthly report: top referrers, total referral revenue, referral conversion rate

---

## What You Need to Build

### 1. Referral Landing Page & Form
- A dedicated funnel page: "Your friend [Referrer Name] thinks you'd love Sunrise Wellness!"
- Form that captures the new lead's info AND who referred them
- Think about: How do you pass the referrer's name/ID to the form? (Hint: URL parameters, hidden fields, or a "Who referred you?" dropdown/text field)

### 2. Referral Tracking in the CRM
- How do you link the referrer to the referred contact?
- What custom fields or tags do you need?
- How do you count referrals per member?
- Design the tag structure and custom fields BEFORE building

### 3. Referral Workflow
- When a referred friend fills out the form, what happens?
- When the referred friend converts to a paid member, what triggers the referrer's reward?
- How do you handle the "3 referrals = free month" bonus?
- Think about timing, conditions, and edge cases

### 4. Referrer Notification & Reward System
- How does the referrer know their friend signed up?
- How is the reward delivered? (Email with code? Auto-applied credit? Manual task?)
- How do you prevent gaming the system? (Self-referral, fake sign-ups)

### 5. Referral Campaign
- Build an email campaign to existing members announcing the referral program
- Include: How it works, what they get, their unique link/process
- Follow up: Monthly "Referral Leaderboard" email showing top referrers

### 6. Reporting
- Smart List: "Members Who Have Referred"
- Smart List: "Referred Leads - Not Yet Converted"
- Pipeline view: Referral leads in the Membership Sales Pipeline (tagged for tracking)
- Monthly metrics: # referrals, # conversions, $ revenue attributed to referrals

---

## Hints (only read if stuck)

<details>
<summary>Hint 1: Tracking the referrer</summary>

Create a custom field called "Referred By" (text) on the contact record. When the referred friend fills out the form, include a "Who referred you?" text field that maps to this custom field. You can also use URL parameters on the funnel: `?ref=JohnSmith` and map that to a hidden form field.
</details>

<details>
<summary>Hint 2: Triggering the referrer reward</summary>

When the referred contact's opportunity moves to "Closed - Member", trigger a workflow. Use the "Referred By" custom field to look up the referrer. Send the referrer a notification email. For the free PT session reward, you could: create a coupon, send them an email with booking instructions, or create a task for the front desk to add a credit.
</details>

<details>
<summary>Hint 3: Counting referrals</summary>

Create a custom field "Referral Count" (number) on the referrer's contact. Each time a referral converts, update this field +1 via workflow. When it reaches 3, trigger the "free month" bonus workflow.
</details>

<details>
<summary>Hint 4: The referral email campaign</summary>

Use Day 7's email campaign skills. Create a trigger link "Share My Referral Link" that tags the member as "referral-program-active". Send them a follow-up with their personalized referral instructions.
</details>

---

## Evaluation Criteria

When you're done, verify:
- [ ] A friend can sign up through the referral funnel and the referrer is tracked
- [ ] The referred friend gets their $20-off incentive
- [ ] The referrer gets notified AND rewarded when the friend converts
- [ ] The referral count is tracked on the referrer's contact
- [ ] 3 referrals triggers the free month bonus
- [ ] An email campaign can be sent to announce the program
- [ ] Reporting shows referral metrics

---

## Apply to Other Businesses

### BrightSmile Dental Version
Same concept: "Refer a friend, both get $50 off." Dental twist: referral tracked via patient intake form question, reward applied as credit on next visit invoice, referrer gets a thank-you card email + credit notification.

### Elevate Digital Agency Version
"Partner Referral Program" - existing clients refer other businesses. Reward: 10% discount on next month's retainer per referral (up to 30% max). Track via custom field "Referred By Client", create a "Partner Referrals" pipeline to track referred leads separately, monthly partner report email.

---

## Bonus Extension
If you finish the basic referral engine, add:
1. A **referral leaderboard page** (funnel page showing top referrers this month)
2. **Automated milestone emails**: "You've referred 5 friends! You're a Sunrise Ambassador!" with a special tag and community badge
3. **Referral expiry**: If the referred friend doesn't sign up within 30 days, close the referral opportunity as "Expired" and notify the referrer to nudge their friend
