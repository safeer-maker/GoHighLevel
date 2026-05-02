# Phase 2 Testing Guide: How to Verify Your Integrated Systems

**Time Required:** 2-3 hours (can be split across multiple sessions)
**Prerequisite:** All Phase 2 exercises (Days 11-17) completed

---

## Introduction

Phase 2 built six interconnected systems for Sunrise Wellness Studio. Each system combines multiple Phase 1 features into an automated machine: lead capture flows into the sales pipeline, which flows into appointment booking, which flows into payment collection, which flows into onboarding and retention.

This guide walks you through testing EACH system individually, then testing them TOGETHER as one complete business.

**Why testing matters:** Automation bugs compound. A misspelled tag in your lead capture workflow means the nurture sequence never fires, which means leads never get a booking prompt, which means they never become members, which means onboarding never triggers. One broken link in the chain silently kills everything downstream. You will not notice until you wonder why nobody has signed up in two weeks. Testing now prevents that.

---

## Before You Start

### Prerequisites Checklist

Confirm these exist in your sub-account before testing:

**From Phase 1:**
- [ ] Custom fields: Fitness Goals, Experience Level, Lead Source, Membership Tier, Last Visit Date, Total Visits
- [ ] Tags created: `new-trial-lead`, `active-member`, `member-basic`, `member-premium`, `no-show`, `vip`
- [ ] SMS and email templates from Day 3
- [ ] Calendars: PT Session, Group Class, Nutrition Consultation (Day 4)
- [ ] Membership Sales Pipeline with stages (Day 5)
- [ ] Products: PT Session ($75), Class Pack ($120), Nutrition Plan ($200) (Day 6)
- [ ] Free Trial funnel and form (Day 8)
- [ ] Personalized Lead Nurture workflow (Day 9)
- [ ] Review Request workflow (Day 10)

**From Phase 2:**
- [ ] Multi-channel lead capture workflows (Day 11)
- [ ] Pipeline stage-triggered sales automation (Day 12)
- [ ] Appointment lifecycle workflow with show/no-show branching (Day 13)
- [ ] Sales funnel with order form (Day 14, if built)
- [ ] Onboarding Pipeline with stages: Welcome, Orientation, First Session Complete, 2-Week Check-In, 30-Day Review, Established Member (Day 15)
- [ ] Onboarding and churn detection workflows (Day 15)
- [ ] Lead magnet funnel and nurture sequence (Day 16)
- [ ] Smart Lists: "Hot Leads - Today", "Webchat Leads - Needs Response" (Day 11)

### Create Your Test Contacts

Create these contacts manually in GHL (Contacts > Add Contact). Do NOT add any tags or pipeline opportunities yet -- the point of testing is to see whether your automations do that work for you.

| # | Name | Email | Phone | Notes |
|---|------|-------|-------|-------|
| 1 | Test Funnel Lead | testfunnel@example.com | (optional) | Will enter via Free Trial form |
| 2 | Test Webchat Lead | testwebchat@example.com | (optional) | Will enter via webchat widget |
| 3 | Test Quick Contact | testquick@example.com | (optional) | Will enter via quick contact form |
| 4 | Test Trigger Link | testtrigger@example.com | (optional) | Will simulate trigger link click |
| 5 | Alex Thompson | alex.thompson.test@example.com | (optional) | Full journey test contact |
| 6 | Test No-Show | testnoshow@example.com | (optional) | Appointment no-show path |
| 7 | Test Churn Risk | testchurn@example.com | (optional) | Retention/churn detection |

**Important:** Use `@example.com` emails. These are safe -- they do not deliver to real inboxes, so you will not spam anyone. GHL will still log the "sent" action in Conversations so you can verify the workflow fired.

### Shorten Wait Steps for Testing

This is critical. Your workflows have wait steps measured in hours and days. You do not want to sit around for 24 hours waiting for a reminder to fire. Before testing, temporarily change these:

| Workflow | Wait Step | Production Timing | Change To |
|----------|-----------|-------------------|-----------|
| New Trial Lead / Personalized Nurture | Follow-up if no booking | 24 hours | 2 minutes |
| New Trial Lead / Personalized Nurture | Final follow-up | 48 hours | 4 minutes |
| Appointment Lifecycle | 24hr reminder | 24 hours before | 2 minutes |
| Appointment Lifecycle | 1hr reminder | 1 hour before | 1 minute |
| Appointment Lifecycle | Post-session follow-up | 2 hours after | 2 minutes |
| Appointment Lifecycle | Review request | 2 hours after session | 3 minutes |
| Appointment Lifecycle | Review follow-up | 3 days | 5 minutes |
| Onboarding Workflow | Day 1-3 orientation nudge | 1-3 days | 2 minutes |
| Onboarding Workflow | 2-week check-in | 14 days | 5 minutes |
| Onboarding Workflow | 30-day review | 30 days | 8 minutes |
| Churn Detection | "We miss you" trigger | 14 days inactive | 2 minutes |
| Churn Detection | Escalation | 30 days inactive | 4 minutes |
| Lead Magnet Nurture | Nurture emails | 2-3 days apart | 2 minutes apart |

**Write these down.** You MUST change them back after testing. (See the "After Testing" section at the bottom.)

### Testing Log Template

Copy this table into a separate file or notebook. Fill it in as you go. Having a written record prevents you from losing track of which tests passed and which need fixes.

```markdown
| Test ID | Test Name | Status | Issue Found | Fix Applied | Re-Verified |
|---------|-----------|--------|-------------|-------------|-------------|
| 1A | Funnel Form Submission | | | | |
| 1B | Webchat Lead Capture | | | | |
| 1C | Quick Contact Form | | | | |
| 1D | Trigger Link Interest | | | | |
| 2A | Pipeline Stage Transitions | | | | |
| 2B | Pipeline-to-Pipeline Handoff | | | | |
| 3A | Appointment Booking + Reminders | | | | |
| 3B | Show Path (Payment + Review) | | | | |
| 3C | No-Show Path (Rebooking) | | | | |
| 4A | Sales Funnel Display | | | | |
| 4B | Post-Purchase Simulation | | | | |
| 5A | Onboarding Pipeline Flow | | | | |
| 5B | Churn Detection | | | | |
| 6A | Lead Magnet Capture | | | | |
| 6B | Nurture Sequence Delivery | | | | |
| 6C | Trigger Link Conversion | | | | |
| 7 | Full Journey (Alex Thompson) | | | | |
```

Status options: PASS, FAIL, PARTIAL (some checks passed, some did not), SKIPPED (cannot test without phone/Stripe/etc.)

---

## Test 1: Lead Capture System (Day 11)

**What you are testing:** Does every entry point create a contact, apply the correct tags, trigger the welcome workflow, and create a pipeline opportunity?

**Setup:** Open two browser windows side by side. Left: an incognito/private window for submitting forms. Right: your GHL dashboard with these tabs open -- Contacts, Conversations, Opportunities (Membership Sales Pipeline), Automation > Workflows.

---

### Test 1A: Free Trial Funnel Form

1. In the incognito browser, open your Free Trial landing page URL
2. Fill out the form with Test Contact #1's details:
   - Name: Test Funnel Lead
   - Email: testfunnel@example.com
   - Phone: leave blank (or add a number if you have one configured)
   - Fitness Goals: Weight Loss
   - Experience Level: Beginner
   - How did you hear about us: Google
3. Submit the form
4. Switch to your GHL dashboard. Wait 30-60 seconds for processing.

**Verify:**
- [ ] Contact "Test Funnel Lead" appears in Contacts
- [ ] Custom fields populated: Fitness Goals = Weight Loss, Experience Level = Beginner, Lead Source = Google
- [ ] Tag `new-trial-lead` applied (check the contact's Tags section)
- [ ] Smart List: Contact appears in "Hot Leads - Today"
- [ ] Conversations tab: Welcome email appears as sent (even though @example.com will not receive it, GHL logs the send)
- [ ] Conversations tab: Welcome SMS appears as sent (only if phone number was provided and SMS is configured)
- [ ] Workflow execution: Go to Automation > Workflows > your lead capture workflow > click "Execution Logs" or check the contact's Activity tab. Confirm the workflow triggered.
- [ ] Pipeline: Go to Opportunities > Membership Sales Pipeline. An opportunity for "Test Funnel Lead" should exist in the "New Inquiry" stage with a value of $79
- [ ] Internal notification: Check if you received an email/SMS/in-app notification about the new lead

**If something fails, check:**

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Contact created but no tags | Workflow trigger not matching the form | Open the workflow, verify trigger is set to "Form Submitted" and the correct form is selected |
| Tags applied but no pipeline opportunity | "Create Opportunity" action missing from workflow | Edit workflow, add a Create Opportunity action after the tagging step |
| Workflow shows "not triggered" | Workflow is in Draft mode | Publish the workflow (toggle to Active/Published) |
| Custom fields empty | Form field mapping broken | Open form settings > field mapping, reconnect each form field to its custom field |
| Contact not created at all | Form is not connected to the funnel page | Check funnel editor, verify the form element is placed and the correct form is selected |

---

### Test 1B: Webchat Widget

1. Open your funnel page or any page where the webchat widget is enabled
2. Click the chat bubble
3. If the widget asks for name/email, enter: Test Webchat Lead / testwebchat@example.com
4. Type a message: "Hi, I am interested in joining your studio. What membership options do you have?"
5. Send the message

**Verify:**
- [ ] Conversation appears in GHL Conversations tab under "Unassigned" or your name
- [ ] Contact "Test Webchat Lead" created (or matched if you pre-created them)
- [ ] Tag `webchat-lead` applied
- [ ] Tag `new-trial-lead` applied
- [ ] Pipeline opportunity created in "New Inquiry" stage
- [ ] Internal notification about the webchat lead
- [ ] You can type a reply from GHL and it appears in the webchat widget

**If something fails, check:**

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No conversation appears | Webchat widget not installed on the page | Check Sites > Chat Widget settings, verify it is enabled for the correct funnel/page |
| Contact created but no tags | Webchat workflow not triggered | Verify the "Customer Replied" or "Chat Widget Message" trigger is set on your webchat workflow |
| Duplicate contact created | Contact matching not working | GHL matches on email or phone. If the webchat does not collect email, it may create a separate record. Check your widget settings to require email collection |

---

### Test 1C: Quick Contact Form

1. Navigate to wherever you placed your Quick Contact form (footer of funnel, separate page, etc.)
2. Fill out with Test Contact #3:
   - Name: Test Quick Contact
   - Email: testquick@example.com
   - Message: "I would like more information about personal training"
3. Submit

**Verify:**
- [ ] Contact created with name and email
- [ ] Tag `new-trial-lead` applied
- [ ] Tag `quick-contact-form` applied (if you used a separate workflow per Day 11, Exercise 11.4)
- [ ] Pipeline opportunity created in "New Inquiry" stage, value $79
- [ ] Welcome/acknowledgment email sent

**Note:** If you used Option A from Day 11 (same workflow for both forms), the tags will match Test 1A exactly. If you used Option B (separate workflow), verify the quick-contact-specific tags.

---

### Test 1D: Trigger Link Interest

This test simulates what happens when an existing contact clicks a trigger link in an email (e.g., "I am interested in Personal Training").

1. Open Test Contact #4 ("Test Trigger Link") in Contacts
2. Manually add the tag `interested-personal-training` (this simulates clicking the trigger link)
3. Wait 30-60 seconds

**Verify:**
- [ ] Workflow "Trigger Link Interest - Pipeline Entry" fires (check the contact's Activity tab)
- [ ] Pipeline opportunity created in "Contacted" stage (not "New Inquiry" -- trigger link contacts have already shown specific interest, per Day 11 Exercise 11.5)
- [ ] Internal notification about the interested lead
- [ ] Personalized follow-up email sent referencing personal training

**If something fails, check:**
- Workflow trigger must be "Tag Added" with the tag `interested-personal-training`
- If using multiple trigger link tags, verify each one has a corresponding trigger or the workflow accepts "any of these tags"

---

## Test 2: Sales Pipeline Automation (Day 12)

**What you are testing:** Do leads progress through the Membership Sales Pipeline with the correct automated communications at each stage? Does the handoff from Sales Pipeline to Onboarding Pipeline work?

**Setup:** Open the Membership Sales Pipeline view and your test contact's record side by side.

---

### Test 2A: Pipeline Stage Transitions

Use Test Contact #1 (who should already have an opportunity in "New Inquiry" from Test 1A).

**Stage 1 to 2: "New Inquiry" to "Contacted"**
1. Drag the opportunity card from "New Inquiry" to "Contacted"
2. Wait 30-60 seconds

**Verify:**
- [ ] Outreach sequence workflow triggers (check Activity tab)
- [ ] First outreach email or SMS sent
- [ ] If you shortened wait steps, the follow-up should arrive within 2-4 minutes

**Stage 2 to 3: "Contacted" to "Trial Booked"**
1. Move the opportunity to "Trial Booked"

**Verify:**
- [ ] Trial management workflow triggers
- [ ] Confirmation/welcome email sent with details about what to expect at the trial
- [ ] Previous outreach sequence stops (contacts should not keep getting "are you interested?" emails after they have booked a trial)

**Stage 3 to 4: "Trial Booked" to "Trial Active"**
1. Move to "Trial Active"

**Verify:**
- [ ] Any mid-trial communications trigger
- [ ] Contact record updated appropriately

**Stage 4 to 5: "Trial Active" to "Trial Follow-Up"**
1. Move to "Trial Follow-Up"

**Verify:**
- [ ] Conversion offer sent (look for the TRIALCONVERT coupon or equivalent offer in Conversations)
- [ ] Follow-up sequence begins

**If something fails, check:**
- Each stage transition should have a corresponding workflow with trigger "Pipeline Stage Changed" or "Opportunity Stage Changed"
- Verify the workflow is filtering for the correct pipeline AND the correct stage
- Check that previous-stage workflows have "Stop on stage change" logic or use workflow goals to exit contacts who move forward

---

### Test 2B: Pipeline-to-Pipeline Handoff

This is one of the most important tests. It verifies that when a lead becomes a member, the system automatically transitions them from the Sales Pipeline to the Onboarding Pipeline.

1. Move Test Contact #1's opportunity to "Closed - Won" (or "Closed - Member")

**Verify:**
- [ ] Tag `active-member` applied to the contact
- [ ] Congratulations/welcome-to-the-family email sent
- [ ] A NEW opportunity is automatically created in the **Onboarding Pipeline** at the "Welcome" stage
- [ ] The Sales Pipeline opportunity is marked as Won
- [ ] Smart Lists update: contact should now appear in member-related lists, not lead-related lists
- [ ] Any "Trial Follow-Up" or sales nurture sequences STOP

**If the Onboarding Pipeline opportunity is NOT created:**
- Open the workflow triggered by "Closed - Won" stage change
- Verify it contains a "Create Opportunity" action pointed at the Onboarding Pipeline
- Verify the pipeline name and stage name are spelled exactly right (GHL is case-sensitive for pipeline/stage references in some contexts)

---

## Test 3: Appointment Lifecycle (Day 13)

**What you are testing:** The complete cycle from booking through reminders, show/no-show branching, payment, and review request.

---

### Test 3A: Booking and Reminders

1. Open the calendar booking page for PT Sessions
2. Book an appointment for Test Contact #1 (use their email to match the existing contact)
3. Select a time slot

**Verify:**
- [ ] Appointment appears on the GHL calendar
- [ ] Confirmation email sent immediately (check Conversations)
- [ ] Confirmation SMS sent immediately (if phone is configured)
- [ ] Reminder workflow begins executing (check Automation > workflow execution logs)
- [ ] With shortened wait times: "24hr" reminder arrives within 2 minutes
- [ ] With shortened wait times: "1hr" reminder arrives within 1 minute after that

**What to check in the confirmation email:**
- [ ] Contact's first name is correctly merged (not showing `{{contact.first_name}}` literally)
- [ ] Session type is correct (PT Session, not Group Class)
- [ ] Date and time are correct
- [ ] Location or parking details are included

---

### Test 3B: Show Path -- Payment and Review

1. In GHL, find the appointment for Test Contact #1
2. Mark the appointment status as "Showed"
3. Wait for the automated sequence to fire (with shortened wait times)

**Verify (in order):**
- [ ] Custom field "Last Visit Date" updated to today's date
- [ ] Custom field "Total Visits" incremented by 1
- [ ] Post-session follow-up message sent ("Great session today, {{first_name}}!")
- [ ] Payment request sent: Text2Pay link or invoice for $75 (PT Session price). **Note:** If you do not have Stripe connected, you may see the workflow action fail at this step. That is expected -- mark it as SKIPPED and note "Stripe not configured" in your log.
- [ ] Review request sent after the post-session delay (with shortened wait, within 3 minutes)
- [ ] Review request contains a link to leave a Google review (or whatever you configured in Day 10)

**If Text2Pay fails without Stripe:**
This is normal. The workflow action will show an error in the execution log. The important thing is that the workflow ATTEMPTED to send it. In production with Stripe connected, this would work. Tag this test as PARTIAL and move on.

---

### Test 3C: No-Show Path

1. Book a new appointment for Test Contact #6 ("Test No-Show")
2. After the appointment time passes (or immediately, for testing), mark the appointment as "No-Show"

**Verify:**
- [ ] Tag `no-show` applied to the contact
- [ ] Gentle rebooking message sent: "We missed you today! Here is a link to rebook..." (check Conversations)
- [ ] The rebooking message includes a calendar booking link
- [ ] No payment request sent (no-shows should NOT get an invoice)
- [ ] No review request sent
- [ ] If this is marked as a second no-show, verify: a different, more serious tone in the message AND/OR the tag `no-show-risk` is applied AND/OR a manual follow-up task is created for VIP contacts

**The critical check:** Make sure the show path and no-show path are mutually exclusive. A contact marked as "Showed" should NEVER get the no-show sequence, and vice versa. Check the workflow's If/Else branching logic if both paths fire.

---

## Test 4: Payment and E-Commerce (Day 14)

**What you are testing:** Can a prospect navigate the sales funnel, view products, and (simulated) complete a purchase that triggers post-purchase automation?

---

### Test 4A: Sales Funnel Walkthrough

1. Open your membership sales funnel in an incognito browser
2. Walk through every page:
   - Landing page loads correctly
   - Product/membership options display with correct pricing
   - "Join Now" or CTA buttons work and navigate to the order form
3. On the order form page:

**Verify:**
- [ ] Products display with correct names and prices
- [ ] Coupon code field is present
- [ ] Try entering WELCOME20 (or whatever coupon you created) -- discount applies correctly
- [ ] Try entering an invalid coupon -- appropriate error message appears
- [ ] Form fields are logical and not duplicated
- [ ] If Stripe test mode is available: complete a test purchase with Stripe test card (4242 4242 4242 4242, any future date, any CVC)
- [ ] If Stripe is NOT configured: stop here and proceed to Test 4B for simulation

---

### Test 4B: Post-Purchase Automation (Simulated)

If you cannot process a real payment, simulate the result manually. This tests whether your post-purchase workflows fire correctly regardless of how the purchase event occurs.

1. Open Test Contact #5 ("Alex Thompson") in Contacts
2. Manually add these tags:
   - `active-member`
   - `member-premium` (or `member-basic`, depending on what you want to test)
3. Go to the Membership Sales Pipeline and either:
   - Create a new opportunity for this contact and move it directly to "Closed - Won", OR
   - If an opportunity already exists, move it to "Closed - Won"
4. Wait 60-90 seconds

**Verify:**
- [ ] Onboarding workflow triggers (from the "Closed - Won" stage change)
- [ ] Welcome/congratulations email sent
- [ ] Community access logic fires (if membership/community is configured)
- [ ] Onboarding Pipeline opportunity created at "Welcome" stage
- [ ] Previous sales/nurture sequences stop

---

## Test 5: Onboarding and Retention (Day 15)

**What you are testing:** Does the new member onboarding sequence guide them through their first 30 days? Does the churn detection system catch members who stop engaging?

---

### Test 5A: Onboarding Pipeline Progression

Use Test Contact #5 (Alex Thompson), who should now have an Onboarding Pipeline opportunity at "Welcome" from Test 4B.

**Verify the Welcome stage:**
- [ ] Welcome email sent with membership guide or onboarding information
- [ ] Community access granted (tag-based, e.g., `member-premium` unlocks premium community content)
- [ ] Tag `onboarding` applied
- [ ] "Book your first session" prompt sent (within shortened wait time)

**Move to "Orientation" stage** (manually, or wait for the workflow to auto-advance):
- [ ] Class schedule or session recommendations sent (should reference the contact's Fitness Goals field)
- [ ] Community introduction prompt sent

**Move to "First Session Complete" stage:**
- [ ] Post-first-session check-in sent: "How was your first session?"
- [ ] Recommendation for next class/session sent

**Move to "2-Week Check-In" stage:**
- [ ] Check-in email sent
- [ ] If engaged (3+ sessions): celebration message + referral program invitation
- [ ] If not engaged: re-engagement offer

**Move to "30-Day Review" stage:**
- [ ] Satisfaction survey sent
- [ ] Upgrade offer sent (Basic to Premium path, if applicable)
- [ ] Referral program invitation sent

**Move to "Established Member" stage:**
- [ ] Transition to ongoing engagement monitoring
- [ ] Onboarding tag removed, `established-member` or equivalent tag applied

---

### Test 5B: Churn Detection

1. Open Test Contact #7 ("Test Churn Risk")
2. Add tags: `active-member`, `member-basic`
3. Set the custom field "Last Visit Date" to a date **16 days ago** (this simulates a member who has not visited in over 2 weeks)
4. If your churn detection workflow triggers on a Smart List or a scheduled check, you may need to:
   - Manually add the tag that your churn workflow watches for, OR
   - Wait for the workflow's scheduled trigger to run

**Verify 14-day inactivity trigger:**
- [ ] "We miss you" email sent: friendly, encouraging tone, includes a booking link
- [ ] Tag `churn-risk` applied

**Simulate 30-day inactivity** (change "Last Visit Date" to 32 days ago, or manually add the escalation tag):
- [ ] Escalation email sent with a stronger offer (e.g., free session, discount)
- [ ] Internal alert or task created for manual follow-up
- [ ] Tag updated to `churn-risk-high` or equivalent

**If churn detection does not fire:**
- Check if the workflow trigger depends on a Smart List or a scheduled/recurring trigger
- Smart List-based churn detection requires the Smart List filter to use "Last Visit Date is more than 14 days ago"
- Some churn workflows use a "Date Timer" trigger on the Last Visit Date field -- verify the field is correctly referenced

---

## Test 6: Marketing Campaign System (Day 16)

**What you are testing:** Does the lead magnet funnel capture leads, deliver the magnet, and run the nurture-to-conversion sequence?

---

### Test 6A: Lead Magnet Capture

1. Open your lead magnet funnel in an incognito browser (e.g., "Free 7-Day Meal Plan" or whatever you built)
2. Fill out the form:
   - Name: Test Lead Magnet
   - Email: testleadmagnet@example.com
3. Submit

**Verify:**
- [ ] Thank-you/confirmation page displayed
- [ ] Contact created in GHL
- [ ] Tag applied: `lead-magnet-meal-plan` (or your lead magnet tag)
- [ ] Lead magnet delivery email sent (check Conversations -- should contain the download link or attachment)
- [ ] Pipeline opportunity created (if configured to feed into the Membership Sales Pipeline)
- [ ] Nurture workflow begins executing

---

### Test 6B: Nurture Sequence Delivery

After Test 6A, the nurture workflow should be running. With shortened wait times (2 minutes between emails instead of 2-3 days), you can watch the entire sequence fire.

**Verify each nurture email (wait 2 minutes between each):**
- [ ] Email 1: Value-add content related to the lead magnet (e.g., nutrition tip)
- [ ] Email 2: More value + soft introduction to Sunrise Wellness Studio services
- [ ] Email 3: Testimonial or case study + stronger CTA
- [ ] Each email contains trigger links for interest areas (e.g., "Interested in Personal Training?", "Want to try a Group Class?")
- [ ] Emails are correctly personalized with `{{first_name}}`

---

### Test 6C: Trigger Link Conversion

1. On Test Contact #4 (or create a new test contact), manually add the tag that simulates clicking a trigger link in a nurture email, e.g., `interested-personal-training`
2. Wait 30-60 seconds

**Verify:**
- [ ] Tag is recorded on the contact
- [ ] Personalized follow-up workflow triggers (the "Trigger Link Interest - Pipeline Entry" workflow from Day 11)
- [ ] Pipeline opportunity created or updated
- [ ] Follow-up email references the specific interest (personal training, not generic)

---

## Test 7: Full Journey Test (Day 17)

**The Ultimate Test.** One contact walks through every system, end to end. This is where you find the integration bugs -- the gaps between systems that individual tests do not catch.

Use Test Contact #5: **Alex Thompson** (alex.thompson.test@example.com). If Alex already has tags and opportunities from Test 4B, delete those first -- remove all tags, delete all opportunities, clear the Activity tab if possible. You want a clean slate.

**Before starting:** Confirm all workflows are published/active. Open the following GHL tabs: Contacts, Conversations, Membership Sales Pipeline, Onboarding Pipeline, Automation.

---

### The Journey

| Step | Action | What to Check | Time to Wait |
|------|--------|---------------|-------------|
| 1 | Fill out Free Trial form in incognito browser with Alex's details. Fitness Goals: Muscle Building. Experience: Intermediate. Source: Instagram. | Contact created. Tags: `new-trial-lead`. Custom fields populated. Pipeline: "New Inquiry" at $79. Welcome email in Conversations. | 60 seconds |
| 2 | Watch for the welcome/nurture sequence to begin firing. | Welcome email sent. Follow-up emails queued (check workflow execution). Internal notification received. | 2-4 minutes (shortened waits) |
| 3 | Move the pipeline opportunity from "New Inquiry" to "Contacted". | Outreach workflow fires. First outreach email/SMS sent. | 60 seconds |
| 4 | Move from "Contacted" to "Trial Booked". | Trial welcome email sent. Outreach sequence stops. | 60 seconds |
| 5 | Book a PT session on Alex's behalf (use the calendar). | Confirmation email sent with session details. Reminder workflow begins. | 60 seconds |
| 6 | Wait for appointment reminders to fire. | "24hr" reminder arrives (shortened to 2 min). "1hr" reminder arrives (shortened to 1 min). Both are personalized. | 3-4 minutes |
| 7 | Mark the appointment as "Showed". | "Last Visit Date" updated. "Total Visits" incremented. Post-session email sent. | 60 seconds |
| 8 | Wait for payment request. | Text2Pay or invoice sent for $75 (or workflow attempts it -- SKIPPED if no Stripe). | 2-3 minutes |
| 9 | Wait for review request. | Review request SMS/email sent with link. | 3-4 minutes |
| 10 | Move pipeline opportunity from "Trial Follow-Up" to "Closed - Won". | Tag `active-member` applied. Congratulations email sent. Onboarding Pipeline opportunity created at "Welcome". Sales nurture sequences stop. | 60 seconds |
| 11 | Watch the onboarding sequence. | Welcome email with membership guide. "Book your first session" prompt. Community access logic fires. | 2-5 minutes |
| 12 | Wait for the 2-week check-in (shortened to 5 min). | Check-in email fires. Engagement assessment logic runs. | 5-6 minutes |
| 13 | Wait for the 30-day review (shortened to 8 min). | Survey sent. Upgrade offer sent. Referral invitation sent. | 8-9 minutes |

**Total estimated time for the full journey test:** 25-35 minutes (with shortened wait times).

### What Integration Bugs Look Like

These are the problems that only show up in the full journey test:

- **Duplicate emails:** Alex gets two welcome emails because both the lead capture workflow and the pipeline stage-change workflow send one. Fix: Add a condition to one workflow ("If tag `welcome-sent` exists, skip") or remove the duplicate send action.
- **Competing workflows:** The nurture sequence keeps sending "are you interested?" emails even after Alex books a trial. Fix: Add a workflow goal or "stop on tag" condition (e.g., stop if tag `trial-booked` is added).
- **Missing handoff:** The Sales Pipeline marks Alex as "Won" but no Onboarding Pipeline opportunity is created. Fix: Verify the "Closed - Won" workflow has a Create Opportunity action for the Onboarding Pipeline.
- **Tag accumulation:** Alex ends up with 15+ tags by the end of the journey, including contradictory ones like `new-trial-lead` and `active-member`. Review which tags should be REMOVED at each lifecycle stage (e.g., remove `new-trial-lead` when `active-member` is added).
- **Wrong pipeline stage:** Alex's opportunity jumps back to an earlier stage because a delayed workflow action fires after you manually moved the card forward. Fix: Add "If opportunity is in stage X" conditions before stage-change actions.

---

## Common Issues and Troubleshooting

### Top 10 Problems You Will Encounter

**1. Workflow does not fire at all**
- Is the workflow Published/Active? (Draft workflows do not execute)
- Is the trigger correct? ("Form Submitted" vs "Contact Created" vs "Tag Added" -- these are different triggers)
- Does the trigger filter match? (Correct form name, correct tag name, correct pipeline)
- Has the contact already been through this workflow? (Some workflows have "once per contact" settings)

**2. Email not sending**
- Does the contact have an email address?
- Is the email action using a template or inline content? Is the template published?
- Check the workflow execution log -- does it show "Email Sent" or an error?
- Is your sending domain verified? (Settings > Email Services)

**3. SMS not sending**
- Does the contact have a phone number?
- Is there a phone number (Twilio/LC Phone) configured on the sub-account?
- Check your messaging compliance settings
- If you do not have a phone number, mark all SMS tests as SKIPPED -- this is expected

**4. Pipeline opportunity not created**
- Open the workflow and verify the "Create Opportunity" action exists
- Verify it references the correct pipeline name and stage name (exact match required)
- Check if the opportunity value is set
- Look at the workflow execution log for errors

**5. Tags not applied**
- Tag names are case-sensitive in some contexts. Verify spelling matches exactly between the workflow action and what you expect
- Check that the "Add Tag" action is present in the workflow and is in the correct position (not after a failing step)

**6. Smart List shows no contacts or wrong contacts**
- Open the Smart List and review filter logic
- Common mistake: using AND when you mean OR (or vice versa)
- Verify the filter references the correct tag/field name
- Click "Refresh" -- Smart Lists are not always real-time

**7. Form fields not mapping to custom fields**
- Open the form in the editor
- Click on each field and check "Map to Field" in the right panel
- The form field and the custom field must be explicitly linked -- GHL does not auto-map by name

**8. Webhook not working (API scripts)**
- Check the webhook URL is correct and accessible
- Verify the payload format matches what GHL sends
- Test the webhook with a tool like webhook.site first
- Check your script logs for errors

**9. Wait steps causing confusion during testing**
- If a workflow seems stuck, check the execution log -- the contact may be sitting in a Wait step
- Remember: you shortened wait times. If you see "Waiting for 2 minutes," that is correct during testing
- If you forgot to shorten a wait and a contact is stuck at "Wait 24 hours," you can either: (a) remove the contact from the workflow, shorten the wait, and re-trigger, or (b) manually push the contact past the wait step in the workflow builder

**10. Contact enters the wrong workflow or enters the same workflow twice**
- Check trigger conditions: a contact with both `new-trial-lead` and `interested-personal-training` tags might trigger multiple workflows simultaneously
- Use "If tag exists" conditions at the start of workflows to filter out contacts who should not be there
- Check the "Allow re-entry" setting on workflows that should only fire once per contact

---

## After Testing: Restore Production Settings

Testing is only useful if you clean up afterward. An account full of test data and shortened timers will cause real problems when actual leads start coming in.

### Restore Wait Times

Go back to every workflow you modified and restore the original timing:

- [ ] New Trial Lead / Nurture: 24-hour follow-up restored
- [ ] New Trial Lead / Nurture: 48-hour final follow-up restored
- [ ] Appointment Lifecycle: 24-hour reminder restored
- [ ] Appointment Lifecycle: 1-hour reminder restored
- [ ] Appointment Lifecycle: 2-hour post-session follow-up restored
- [ ] Appointment Lifecycle: Review request timing restored
- [ ] Appointment Lifecycle: Review follow-up (3 days) restored
- [ ] Onboarding Workflow: Day 1-3 orientation timing restored
- [ ] Onboarding Workflow: 14-day check-in restored
- [ ] Onboarding Workflow: 30-day review restored
- [ ] Churn Detection: 14-day inactivity trigger restored
- [ ] Churn Detection: 30-day escalation restored
- [ ] Lead Magnet Nurture: 2-3 day spacing between emails restored

### Clean Up Test Data

- [ ] Delete all test contacts (search for "@example.com"), OR tag them with `test-contact` and create a Smart List filter to exclude them from all future campaigns
- [ ] Delete all test opportunities from both the Membership Sales Pipeline and Onboarding Pipeline
- [ ] Clear test conversations from the Conversations tab (or leave them -- they will not affect real leads)
- [ ] Remove any manually-added tags from contacts you used for simulation

### Final Verification

- [ ] All workflows are Published/Active
- [ ] No workflows are stuck in a "paused" or "draft" state
- [ ] Pipelines show only real opportunities (or are empty, ready for real leads)
- [ ] Smart Lists return correct results (no test contacts polluting the data)
- [ ] Calendar booking pages are accessible and functional
- [ ] Funnel pages load correctly in incognito

### Record Your Results

Save your completed testing log somewhere you can reference it. When you build systems for real clients (or when something breaks in three months), this log will tell you exactly what was tested and what was skipped. Anything marked SKIPPED or PARTIAL should be retested once you have the required integration (Stripe, phone number, etc.).

---

## Quick Reference: Test Coverage Summary

| System | Tests | Covers |
|--------|-------|--------|
| Lead Capture (Day 11) | 1A, 1B, 1C, 1D | Form, webchat, quick contact, trigger links |
| Sales Pipeline (Day 12) | 2A, 2B | Stage transitions, pipeline handoff |
| Appointments (Day 13) | 3A, 3B, 3C | Booking, reminders, show, no-show, payment, review |
| E-Commerce (Day 14) | 4A, 4B | Funnel display, post-purchase automation |
| Onboarding/Retention (Day 15) | 5A, 5B | 30-day onboarding, churn detection |
| Marketing Campaigns (Day 16) | 6A, 6B, 6C | Lead magnet, nurture sequence, trigger conversion |
| Full Integration (Day 17) | 7 | End-to-end journey, cross-system integration |

**Total: 17 individual tests + 1 full journey test.**

If all 17 pass and the full journey completes without duplicate messages, missed handoffs, or stalled workflows -- your Sunrise Wellness Studio systems are production-ready.
