# Day 11: Multi-Channel Lead Capture System

**Time Required:** 3-4 hours
**Combines:** Sites (D8) + Forms (D8) + Contacts (D2) + Conversations (D3) + Automation (D9) + Pipeline (D5)
**Level:** Intermediate

---

## Today's Mission

Welcome to Phase 2. Everything changes today.

In Phase 1, you built Sunrise Wellness Studio piece by piece: contacts on Day 2, templates on Day 3, calendars on Day 4, and so on. Each feature worked on its own, and you previewed how they would connect. But right now, a lead could fill out your Free Trial form and slip through a crack between two systems that are not fully wired together. A webchat visitor might start a conversation that nobody notices. An email subscriber might click "interested in personal training" but never get routed into the sales pipeline.

Today you will fix all of that by building a **complete multi-channel lead capture system** -- a machine where every entry point (funnel form, webchat, quick contact form, email trigger link) feeds into the SAME pipeline, the SAME workflow, and the SAME notification system. No lead will ever fall through the cracks again, regardless of how they find Sunrise Wellness Studio.

By the end of today, you will have tested the entire system end-to-end and confirmed that a stranger who discovers your studio through ANY channel is automatically captured, tagged, nurtured, and tracked.

---

## What You'll Combine

| Phase 1 Feature | Day Built | Role in Today's System |
|-----------------|-----------|----------------------|
| Free Trial Funnel | Day 8 | Primary lead capture entry point |
| Free Trial Request Form | Day 8 | Collects member info and maps to custom fields |
| Custom Fields | Day 2 | Stores fitness goals, experience level, lead source |
| Smart Lists | Day 2 | Auto-segments new leads for targeted follow-up |
| SMS/Email Templates | Day 3 | Instant follow-up messages |
| Webchat Widget | Day 3 | Catches website visitors who prefer live chat |
| Membership Sales Pipeline | Day 5 | Tracks every lead through the sales process |
| New Trial Lead Workflow | Day 9 | Automates welcome sequence and follow-up |
| Trigger Links | Day 7 | Captures interest signals from email campaigns |

---

## The System Architecture

Before you start building, study this diagram. It shows how every lead source converges into a single system. This is what "integration" means -- not just having all the features, but having them talk to each other so the output of one becomes the input of another.

```
ENTRY POINTS (how leads find you)
=================================

[Facebook/Instagram Ad] ──→ [Free Trial Landing Page]
                                      │
                               [Form Submitted]
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                [Contact Created]      [Workflow Triggered]
                - Custom fields filled  - Welcome SMS sent
                - Tags applied          - Welcome email sent
                - Smart List updated    - Owner notified
                          │                       │
                          └───────────┬───────────┘
                                      │
                          [Pipeline Opportunity Created]
                          "New Inquiry" stage ── $79
                                      │
                          [24hr Follow-Up if no booking]
                                      │
                          [48hr Final Follow-Up]


[Website Visitor] ──→ [Webchat Widget]
                            │
                    [Conversation Created]
                    [Contact Created/Matched]
                            │
                    [Webchat Workflow Triggered]
                    - Tag: "webchat-lead"
                    - Pipeline opportunity created
                    - Internal notification sent


[Email Campaign] ──→ [Trigger Link Clicked]
                            │
                    [Tag Added: "interested-*"]
                            │
                    [Interest Workflow Triggered]
                    - Move to "Contacted" stage
                    - Send targeted follow-up


[Direct/Organic Traffic] ──→ [Quick Contact Form]
                                      │
                              [Same Workflow Path]
                              [Same Pipeline Destination]


ALL PATHS CONVERGE:
===================
Every lead ends up in:
  1. Contact record (with custom fields + tags)
  2. Membership Sales Pipeline ("New Inquiry" stage)
  3. Automated nurture sequence
  4. Internal notification to you
  5. Appropriate Smart List(s)
```

The key insight: **it does not matter how someone finds you.** Whether they click a Facebook ad, chat on your website, fill out a quick form, or click a link in your email campaign -- they all end up in the same system, tracked the same way, nurtured with the same (or personalized) sequences.

---

## Part 1: Audit Your Existing Pieces (20 min)

Before you wire anything together, you need to confirm that every piece you built in Phase 1 is still in place and functional. Think of this like a mechanic checking all the parts before assembling an engine.

### Exercise 11.1: Phase 1 Integration Audit

**Purpose:** Verify that every component needed for today's system exists and is configured correctly. You will check each one and note anything that needs fixing.

Open a text file, notepad, or a piece of paper. You are going to run through a checklist and mark each item as Ready, Needs Fix, or Missing.

**Check 1: Free Trial Funnel (Day 8)**
1. Navigate to **Sites > Funnels**
2. Find "Sunrise Wellness - Free Trial" (or whatever you named it)
3. Open it and verify:
   - Landing page exists with a form embedded
   - Thank-you page exists with calendar booking link
   - The funnel is **published** (not in draft mode)
   - Copy the funnel URL -- you will need it throughout today
4. Status: Ready / Needs Fix / Missing

**Check 2: Free Trial Request Form (Day 8)**
1. Open the form embedded in your funnel (or navigate to **Sites > Forms**)
2. Verify these fields exist and are mapped to contact fields:
   - First Name, Last Name, Email, Phone
   - Fitness Goals (mapped to the custom field from Day 2)
   - Experience Level or "How did you hear about us?" (mapped to custom fields)
3. Submit a test entry in an incognito window if you are not sure the mappings work
4. Status: Ready / Needs Fix / Missing

**Check 3: Custom Fields and Tags (Day 2)**
1. Navigate to **Settings > Custom Fields** (or check via the Contacts section)
2. Confirm these custom fields exist:
   - Membership Type
   - Fitness Goals
   - How did you hear about us? (or Lead Source)
3. Navigate to **Contacts** and check that you have at least a few test contacts with data in these fields
4. Status: Ready / Needs Fix / Missing

**Check 4: Smart Lists (Day 2)**
1. Navigate to **Contacts > Smart Lists**
2. Confirm you have lists that filter by relevant criteria (e.g., new leads, trial members, specific fitness goals)
3. If you do not have a "New Trial Leads" Smart List, create one now:
   - Filter: Tag is `new-trial-lead`
   - Save as "New Trial Leads"
4. Status: Ready / Needs Fix / Missing

**Check 5: SMS/Email Templates (Day 3)**
1. Navigate to **Marketing > Templates** (or wherever your templates live)
2. Confirm you have a welcome email and welcome SMS template
3. If you cannot find them, you will recreate them in Part 2
4. Status: Ready / Needs Fix / Missing

**Check 6: Webchat Widget (Day 3)**
1. Navigate to **Conversations > Chat Widget** (or **Sites > Chat Widget**)
2. Confirm the widget exists and is configured
3. Note: The webchat widget may not be actively deployed on a live website, and that is fine. You just need the configuration to exist so you can test it
4. Status: Ready / Needs Fix / Missing

**Check 7: Membership Sales Pipeline (Day 5)**
1. Navigate to **Opportunities > Pipelines**
2. Open "Membership Sales" pipeline
3. Confirm these stages exist (or similar):
   - New Inquiry
   - Contacted
   - Trial Booked
   - Trial Active
   - Trial Follow-Up
   - Closed - Member (Won)
   - Closed - Lost
4. Status: Ready / Needs Fix / Missing

**Check 8: New Trial Lead Workflow (Day 9)**
1. Navigate to **Automation > Workflows**
2. Find "New Trial Lead" workflow
3. Open it and verify:
   - Trigger: Form Submitted (Free Trial Request)
   - Actions include: Add tag, Send email, Send SMS (if phone), Create opportunity, Internal notification
   - The workflow is in **Published** status (or ready to publish)
4. Status: Ready / Needs Fix / Missing

**Fix anything marked "Needs Fix" or "Missing" before continuing.** If you need to rebuild something, refer back to the Phase 1 lesson for that day. Today's exercises assume all eight components are functional.

> **Pro Tip:** This audit step is something you should do in real client work too. Before building any integrated system, verify that every component works individually. It is much easier to debug a single broken piece than to debug an entire system where you do not know which piece failed.

---

## Part 2: Wire the Funnel-to-Contact-to-Pipeline Flow (45 min)

Now you will verify and strengthen the connections between your funnel form, contact records, and pipeline. This is the core spine of the lead capture system -- everything else connects to it.

### Exercise 11.2: Test the Form-to-Contact-to-Pipeline Flow

**Purpose:** Submit a real test entry through your funnel and trace it through every system to confirm the entire chain works without gaps.

**Step 1: Prepare for the test**
1. Open your funnel URL in an **incognito/private browser window** (this is critical -- you need to simulate a brand new visitor, not someone already logged into GHL)
2. In your regular browser, open three tabs:
   - **Contacts** tab (to watch for the new contact)
   - **Opportunities** tab with the Membership Sales pipeline open
   - **Automation > Workflows** with the New Trial Lead workflow open

**Step 2: Submit the form**

Fill out the Free Trial form with these test details:

| Field | Value |
|-------|-------|
| First Name | Test |
| Last Name | LeadCapture |
| Email | Use a real email you can check (your own, or a secondary address) |
| Phone | Use your real phone if you want to test SMS, otherwise leave blank |
| Fitness Goals | Weight Loss (or whichever option you have) |
| How did you hear about us? | Instagram (or whichever option you have) |

Click submit and note the time.

**Step 3: Verify each connection point**

Switch to your regular browser and check each system. Give it 1-2 minutes for everything to process.

**Connection 1: Form → Contact**
1. Go to the **Contacts** tab
2. Search for "Test LeadCapture"
3. Open the contact record and verify:
   - First Name, Last Name, Email, Phone are all populated
   - Custom field "Fitness Goals" = the value you selected
   - Custom field for lead source = the value you selected
   - If any field is blank, the form-to-contact field mapping is broken. Go back to your form settings and check the field mapping configuration

**Connection 2: Contact → Tags**
1. Still on the contact record, check the tags section
2. You should see `new-trial-lead` (added by the Day 9 workflow)
3. If the tag is missing, the workflow either did not trigger or the tag action is misconfigured

**Connection 3: Contact → Smart Lists**
1. Navigate to **Contacts > Smart Lists**
2. Open "New Trial Leads" (or your equivalent)
3. Confirm "Test LeadCapture" appears in the list
4. If it does not, check the Smart List filter criteria -- it should match the tag or field that your workflow applies

**Connection 4: Form → Workflow → Communications**
1. Check your email inbox for the welcome email
2. Check your phone for the welcome SMS (if you entered a phone number)
3. If neither arrived, open the workflow and look at the execution history for this contact. Find where it stopped or errored

**Connection 5: Workflow → Pipeline**
1. Go to the **Opportunities** tab
2. Open the Membership Sales pipeline
3. Look for a new opportunity in the "New Inquiry" stage
4. Open it and verify:
   - Contact is linked to "Test LeadCapture"
   - Value is set (e.g., $79 or whatever you configured in Day 9)
   - Stage is "New Inquiry"
5. If the opportunity is missing, check the "Create Opportunity" action in your workflow

**Connection 6: Workflow → Internal Notification**
1. Check your email (or wherever GHL sends internal notifications) for an alert about the new lead
2. If missing, verify the Internal Notification action in your workflow

**Document your results.** If everything passed, excellent -- your core flow is working. If anything failed, fix it before moving on. The most common issues are:

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Contact created but fields blank | Form fields not mapped to contact fields | Edit form > Field Settings > Map each field to the correct contact property |
| Contact created but no tag | Workflow did not trigger | Check workflow trigger: is it set to the correct form? Is the workflow published? |
| Tag exists but no pipeline opportunity | "Create Opportunity" action missing or misconfigured | Edit workflow > verify the Create Opportunity action is linked to the correct pipeline and stage |
| No email/SMS received | Template broken or action misconfigured | Check the Send Email/SMS action > verify template is selected and merge fields are correct |
| Everything works but delayed | Wait actions in workflow | Check if there is an unnecessary Wait action before the first actions |

### Exercise 11.3: Strengthen the Form Field Mapping

**Purpose:** Ensure your form captures enough data to power personalized follow-up and accurate pipeline management.

Review your Free Trial Request form and confirm these mappings exist:

| Form Field | Maps To | Why It Matters |
|------------|---------|---------------|
| First Name | Contact: First Name | Personalizes every email and SMS with {{contact.first_name}} |
| Last Name | Contact: Last Name | Full name for pipeline and reporting |
| Email | Contact: Email | Required for email nurture sequence |
| Phone | Contact: Phone | Required for SMS follow-up (optional field for visitor, but critical for engagement) |
| Fitness Goals | Custom Field: Fitness Goals | Powers conditional branching in the Personalized Lead Nurture workflow (Day 9) |
| Lead Source | Custom Field: How did you hear about us? | Tells you which marketing channels are working |

If any mapping is missing, fix it now:
1. Open the form in the editor
2. Click on the field that is not mapped
3. In the field settings, look for "Map to Contact Field" or "Custom Field Mapping"
4. Select the correct contact field or custom field
5. Save the form

> **Pro Tip:** In real-world setups, you want to capture as much data as possible WITHOUT making the form feel long. The sweet spot for a lead capture form is 4-6 fields. You can always collect more information later through surveys (like the Member Needs Assessment you built on Day 8) after the initial capture.

---

## Part 3: Add the Webchat Channel (30 min)

Your funnel form is now the primary lead capture tool, but not everyone fills out forms. Some people prefer to ask a quick question first. The webchat widget you configured on Day 3 catches these visitors -- but right now, it probably just opens a conversation without feeding into your pipeline or workflow system. You are about to fix that.

### Exercise 11.4: Wire Webchat into the Lead Capture System

**Purpose:** Ensure that a webchat conversation creates a contact (if new), creates a pipeline opportunity, and triggers notifications -- just like a form submission would.

**Step 1: Review your webchat configuration**
1. Navigate to **Conversations > Chat Widget** (or **Sites > Chat Widget**, depending on your GHL version)
2. Open your existing webchat widget configuration
3. Note whether it asks for contact information (name, email, phone) before starting a chat. This is called a **pre-chat form**
4. If there is NO pre-chat form, you need to add one. Without contact info, the webchat creates an anonymous conversation that cannot be linked to a contact record

**Step 2: Configure the pre-chat form**

If your webchat widget does not already have a pre-chat form, configure one now:
1. Look for "Pre-Chat Form" or "Lead Capture Form" in the widget settings
2. Enable it and add these fields:
   - First Name (required)
   - Email (required)
   - Phone (optional but encouraged)
3. Set the greeting message:
   ```
   Welcome to Sunrise Wellness Studio! Before we chat,
   could you share your name and email so we can follow
   up if we get disconnected?
   ```
4. Save the widget settings

**Step 3: Build a webchat lead capture workflow**

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Webchat Lead Capture"

```
[TRIGGER: Customer Replied -- Channel: Live Chat / Chat Widget]
```

1. Click **Add New Workflow Trigger**
2. Look for a trigger related to chat/conversation events. Depending on your GHL version, this might be:
   - "Customer Replied" with a filter for channel = Live Chat
   - "Chat Widget Message Received"
   - "Conversation - New" with a chat filter
3. Select the most appropriate trigger for webchat messages

> **Access Note:** The exact trigger name varies by GHL version. If you cannot find a chat-specific trigger, use "Customer Replied" and filter to the Live Chat channel. If that is not available either, use "Contact Created" with a filter for source = Chat Widget. The important thing is that the workflow fires when someone interacts via webchat.

```
    |
    v
[CONDITION: If/Else -- Does contact already have tag "new-trial-lead"
                        OR tag "active-member"?]
  --> YES: End (they are already in the system)
  --> NO: Continue
```

4. Add an **If/Else** condition to check if this is truly a NEW lead
5. Condition: Contact does NOT have tag `new-trial-lead` AND does NOT have tag `active-member`
6. **YES branch (already in system):** End workflow. No need to create duplicate pipeline entries for existing contacts
7. **NO branch (new lead):** Continue to the next actions

```
    |
    v
[ACTION: Add Tag "webchat-lead"]
    |
    v
[ACTION: Add Tag "new-trial-lead"]
    |
    v
[ACTION: Create Opportunity]
  Pipeline: Membership Sales
  Stage: New Inquiry
  Value: $79
    |
    v
[ACTION: Internal Notification]
  "New webchat lead: {{contact.first_name}} ({{contact.email}})
   is chatting now. Respond ASAP!"
```

8. Add **Add Tag:** `webchat-lead` (identifies how this lead came in)
9. Add **Add Tag:** `new-trial-lead` (same tag the form workflow uses -- this is how the Personalized Lead Nurture workflow from Day 9 picks them up)
10. Add **Create Opportunity:**
    - Pipeline: Membership Sales
    - Stage: New Inquiry
    - Value: $79 (same as form leads)
11. Add **Internal Notification:**
    - Type: Email (and/or in-app notification if available)
    - Subject: "LIVE CHAT: {{contact.first_name}} is chatting now!"
    - Body: "A new visitor is on webchat right now. Respond in Conversations immediately. Contact: {{contact.first_name}} ({{contact.email}})"
    - WHY: Webchat is different from form submissions because the person expects a LIVE response. The notification needs to feel urgent

```
    |
    v
[ACTION: Wait 10 minutes]
    |
    v
[ACTION: Send Email]
  Subject: "Thanks for chatting with us!"
  Body: Welcome message + Free Trial link + booking link
```

12. Add **Wait:** 10 minutes (give yourself time to respond to the chat first)
13. Add **Send Email:**
    - Subject: "Thanks for reaching out to Sunrise Wellness!"
    - Body: "Hi {{contact.first_name}}, thanks for chatting with us! In case we got disconnected, here is everything you need to know about our Free 7-Day Trial: [funnel link]. You can also book a session directly here: [calendar booking link]. Looking forward to seeing you at the studio!"
    - WHY: Even if the live chat goes well, an email gives them something to reference later. If the chat ended abruptly (connection issues, they had to leave), the email picks up where the conversation left off

**Save and publish the workflow.**

**Step 4: Test the webchat flow**

1. Open the chat widget test/preview (or your funnel page if the widget is embedded there)
2. Start a conversation as a new visitor
3. Enter test contact info if prompted by the pre-chat form
4. Send a message like "Hi, I am interested in your free trial"
5. Switch to GHL and verify:
   - A conversation appeared in the Conversations tab
   - A new contact was created (or matched to an existing one)
   - The workflow triggered (check workflow execution history)
   - A pipeline opportunity was created in "New Inquiry"
   - You received the internal notification

> **Pro Tip:** In a real deployment, you would respond to webchat messages immediately. The 10-minute email follow-up is a safety net, not a replacement for live conversation. Webchat leads who get an instant human response convert at 3-5x the rate of those who only get automated follow-up. The automation ensures no one falls through the cracks even when you are busy coaching a session.

---

## Part 4: Add Additional Entry Points (30 min)

Your system now handles two entry points: the funnel form and webchat. But leads can find Sunrise Wellness Studio through other channels too. In this section, you will add two more entry points that all feed into the same pipeline and workflow system.

### Exercise 11.5: Build a Quick Contact Form

**Purpose:** Create a simplified contact form for situations where the full funnel is too much -- like embedding in a blog sidebar, adding to a Facebook page, or using as a "Contact Us" form on a future website.

Navigate to **Sites > Forms > + Create Form** (or wherever forms are created in your GHL version)

**Form Name:** "Quick Contact - Sunrise Wellness"

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Email | Email | Yes |
| Phone | Phone | No |
| What are you interested in? | Dropdown | No |
| | Options: Free 7-Day Trial, Personal Training, Group Classes (HIIT/Yoga/Pilates), Nutrition Coaching, General Information | |

That is it -- just 4 fields. The goal of this form is speed. Someone who does not want to fill out a full funnel page can give you their name, email, and interest in under 30 seconds.

**Connect it to the same workflow:**

You have two options here:

**Option A: Same workflow, multiple triggers**
1. Open your "New Trial Lead" workflow from Day 9
2. Add a second trigger: Form Submitted > "Quick Contact - Sunrise Wellness"
3. The rest of the workflow runs the same way

**Option B: New workflow that feeds into the same system**
1. Create a new workflow: "Quick Contact Lead Capture"
2. Trigger: Form Submitted > "Quick Contact - Sunrise Wellness"
3. Actions:
   - Add Tag: `new-trial-lead` (this is the key -- using the same tag means the Personalized Lead Nurture workflow from Day 9 picks them up automatically)
   - Add Tag: `quick-contact-form` (identifies the source)
   - Create Opportunity: Membership Sales pipeline, "New Inquiry" stage, $79
   - Send Email: Welcome message with Free Trial information
   - Internal Notification: New lead alert

Either option works. Option A is simpler (one workflow handles both forms). Option B is more maintainable (each form has its own workflow, so you can customize the response for each). For real client work, Option B is usually better because the welcome email for a "Quick Contact" submission might be different from the welcome email for a full "Free Trial Request."

**Choose one option, build it, and save.**

### Exercise 11.6: Wire Trigger Links into the Pipeline

**Purpose:** Ensure that when an existing contact clicks a trigger link in one of your email campaigns (from Day 7), it creates or updates a pipeline opportunity and alerts you.

On Day 7, you created trigger links like:
- `interested-personal-training`
- `interested-group-classes`
- `interested-nutrition-coaching`

These links add tags when clicked. But right now, that tag just sits on the contact record. Nobody is notified, and no pipeline opportunity is created. Let's fix that.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "Trigger Link Interest - Pipeline Entry"

```
[TRIGGER: Tag Added --> "interested-personal-training"
                    OR "interested-group-classes"
                    OR "interested-nutrition-coaching"]
```

1. Add a trigger for **Contact Tag Added**
2. You may need to create three separate triggers (one for each tag) or use a single trigger with an "any of these tags" filter, depending on your GHL version
3. If you can only do one tag per trigger, pick "interested-personal-training" for now and duplicate the workflow for the other tags later

```
    |
    v
[CONDITION: If/Else -- Does contact already have an OPEN
            opportunity in Membership Sales pipeline?]
  --> YES: Update existing opportunity (add note, move stage)
  --> NO: Create new opportunity
```

4. Add an **If/Else** condition to check for an existing open opportunity
5. **YES branch (existing opportunity):**
   - Add a note to the opportunity: "Contact clicked trigger link: {{trigger.tag}}" (or manually reference the tag name)
   - If they are still in "New Inquiry", move them to "Contacted" (they are showing active interest)
6. **NO branch (no existing opportunity):**
   - Create Opportunity in Membership Sales pipeline, "Contacted" stage (they are past "New Inquiry" because they already showed specific interest by clicking a trigger link)
   - Set the value based on interest if possible:
     - Personal Training interest: $149 (Premium membership likely)
     - Group Classes interest: $79 (Basic membership likely)
     - Nutrition Coaching interest: $249 (VIP membership likely)

```
    |
    v
[ACTION: Internal Notification]
  "{{contact.first_name}} just clicked {{trigger.tag}} in an email
   campaign. They are interested in [service]. Follow up today!"
```

7. Add **Internal Notification** with details about what they clicked
8. This is a high-intent signal -- someone reading your email and clicking a specific interest link is warmer than a cold form submission

**Save and publish the workflow.**

> **Pro Tip:** Trigger link clicks are one of the strongest buying signals in marketing. Someone who opens your email and clicks "I'm interested in Personal Training" is telling you exactly what they want. These contacts should be prioritized over cold form submissions. In a real setup, you might assign these to a specific sales person or send them a more personalized follow-up.

### Exercise 11.7: Document Your External Channel Strategy

**Purpose:** Plan (but not fully build) how external lead sources like Facebook Lead Ads, Google Ads, and referral programs would connect to your system.

You are not going to build these today because they require external ad accounts and additional setup. But documenting the plan ensures you understand how the integrated system scales.

Open a note or document and write out the following:

**Facebook/Instagram Lead Ads:**
- Facebook Lead Ads submit form data directly to GHL through an integration (Settings > Integrations > Facebook)
- When connected, a Facebook Lead Ad submission creates a contact in GHL automatically
- Workflow trigger: "Facebook Lead Ad Submitted" (or the contact creation triggers your existing workflow via the `new-trial-lead` tag)
- The contact enters the same Membership Sales pipeline at "New Inquiry"
- You would create a specific tag like `source-facebook-ad` to track ROI from Facebook advertising

**Google Ads:**
- Google Ads typically drive traffic to your funnel landing page (the one you built on Day 8)
- The lead fills out the same Free Trial Request form
- The form workflow handles everything -- no additional integration needed
- To track Google Ads specifically, add a UTM parameter to the URL and map it to a custom field

**Referral Program:**
- When a member refers someone, you would create a form or landing page specifically for referrals
- The form includes a "Who referred you?" field
- The workflow applies the REFERRAL coupon from Day 6 and tags both the referrer and the new lead
- The referrer gets notified that their friend signed up

You do not need to build any of these right now. The point is that your system is **designed to scale** -- every new channel feeds into the same pipeline and workflow infrastructure you are building today.

---

## Part 5: Notification System (20 min)

You have multiple entry points now, and leads are being captured and tracked. But what good is a lead capture system if you do not know a lead came in until you happen to check GHL? This section ensures you are notified immediately, every time, through every channel.

### Exercise 11.8: Build a Comprehensive Notification System

**Purpose:** Ensure that every new lead -- regardless of entry point -- triggers an immediate notification so you can respond quickly.

**Step 1: Audit your existing notifications**

Open each workflow you have built (or modified) today and verify that every one includes an Internal Notification action:

| Workflow | Should Notify About |
|----------|-------------------|
| New Trial Lead (Day 9) | Form submission + contact details |
| Webchat Lead Capture (today) | Live chat started + urgency to respond |
| Quick Contact Lead Capture (today) | Quick form submission + interest area |
| Trigger Link Interest (today) | Email engagement + specific interest |

If any workflow is missing a notification action, add one now.

**Step 2: Configure notification channels**

GHL can send internal notifications through several channels. Configure the ones available to you:

1. **Email notifications:** Check that your notification email address is correct in Settings > My Profile (or wherever your GHL version stores it)
2. **In-app notifications:** These appear in the GHL bell icon. Most workflow notification actions send these automatically
3. **Mobile push notifications:** If you have the GHL mobile app installed, ensure push notifications are enabled for new contacts and conversations

**Step 3: Create a "Hot Leads" Smart List**

This gives you a real-time dashboard of today's new leads without digging through the full contact list.

Navigate to **Contacts > Smart Lists > + Create Smart List**

**Name:** "Hot Leads - Today"

Set these filters:
- Tag is `new-trial-lead`
- AND Date Added is "Today" (or "Last 24 hours" depending on available filter options)

Save the Smart List.

Now create a second one:

**Name:** "Webchat Leads - Needs Response"

Set these filters:
- Tag is `webchat-lead`
- AND Tag is NOT `responded-to` (you would add this tag manually after responding, or via a workflow when you send a reply)

Save the Smart List.

> **Pro Tip:** Make these Smart Lists the first thing you check every morning. Open "Hot Leads - Today" to see who came in overnight. Open "Webchat Leads - Needs Response" to see if anyone is waiting for a reply. In a real business, you might check these multiple times per day.

---

## Part 6: End-to-End Testing (30 min)

This is the most important part of the day. You are going to simulate real leads coming through every entry point and verify that the entire system works as designed. Do not skip this section -- integration bugs only reveal themselves when you test the full flow.

### Exercise 11.9: Full System Test

**Purpose:** Walk through every lead capture channel and verify that each one correctly creates a contact, triggers the workflow, creates a pipeline opportunity, sends notifications, and updates Smart Lists.

**Preparation:**
1. Open an incognito/private browser window for testing
2. In your regular browser, open tabs for: Contacts, Opportunities (Membership Sales pipeline), Conversations, Automation (Workflows), and your "Hot Leads - Today" Smart List
3. Use a real email address you can check for each test. If you only have one email, you can use the Gmail "+" trick: `yourname+test1@gmail.com`, `yourname+test2@gmail.com` -- they all arrive in the same inbox but create separate contacts in GHL

**Test 1: Funnel Form Submission**

1. Open your Free Trial funnel URL in the incognito window
2. Fill out the form:
   - Name: "Funnel Test One"
   - Email: `yourname+funneltest@gmail.com`
   - Phone: (optional)
   - Fitness Goals: Muscle Building
   - Lead Source: Google Search
3. Submit the form
4. Wait 1-2 minutes, then verify:
   - [ ] Contact "Funnel Test One" exists in Contacts
   - [ ] Custom fields are populated (Fitness Goals = Muscle Building)
   - [ ] Tag `new-trial-lead` is applied
   - [ ] Welcome email received
   - [ ] Welcome SMS received (if phone provided)
   - [ ] Pipeline opportunity exists in "New Inquiry" stage
   - [ ] Internal notification received
   - [ ] Contact appears in "Hot Leads - Today" Smart List

**Test 2: Webchat Conversation**

1. Open the webchat widget (either via your funnel page or the widget test URL)
2. Enter contact info if the pre-chat form appears:
   - Name: "Chat Test Two"
   - Email: `yourname+chattest@gmail.com`
3. Send a message: "Hi, I saw your free trial offer and have a few questions"
4. Wait 1-2 minutes, then verify:
   - [ ] Contact "Chat Test Two" exists in Contacts
   - [ ] Tag `webchat-lead` is applied
   - [ ] Tag `new-trial-lead` is applied
   - [ ] Conversation appears in the Conversations tab
   - [ ] Pipeline opportunity exists in "New Inquiry" stage
   - [ ] Internal notification received (should feel urgent -- "chatting now!")
   - [ ] After 10 minutes, follow-up email received

**Test 3: Quick Contact Form**

1. Open the Quick Contact form (you may need to get its direct URL from the form settings, or create a simple test page with it embedded)
2. Fill it out:
   - Name: "Quick Test Three"
   - Email: `yourname+quicktest@gmail.com`
   - Interest: Personal Training
3. Submit
4. Wait 1-2 minutes, then verify:
   - [ ] Contact "Quick Test Three" exists in Contacts
   - [ ] Tag `new-trial-lead` is applied
   - [ ] Tag `quick-contact-form` is applied (if you used Option B)
   - [ ] Pipeline opportunity exists in "New Inquiry" stage
   - [ ] Internal notification received
   - [ ] Contact appears in "Hot Leads - Today" Smart List

**Test 4: Pipeline Convergence Check**

1. Open the **Opportunities** tab and view the Membership Sales pipeline
2. In the "New Inquiry" stage, you should see all three test opportunities:
   - Funnel Test One
   - Chat Test Two
   - Quick Test Three
3. Each should have a value assigned and be linked to the correct contact
4. This is the proof that ALL entry points converge into the SAME pipeline

**Test 5: Smart List Verification**

1. Open "Hot Leads - Today" Smart List
2. All three test contacts should appear
3. Open each contact and verify:
   - Tags are correct
   - Custom fields are populated (where applicable)
   - Timeline shows the workflow actions that executed

**Document any failures.** For each failure:
1. Identify which step failed (contact creation? tag? pipeline? notification?)
2. Open the relevant workflow and check the execution history for that contact
3. Look for errors or skipped steps
4. Fix the issue and re-test

### Exercise 11.10: Clean Up Test Data

**Purpose:** Remove test contacts so they do not clutter your system.

After verifying everything works:
1. Navigate to **Contacts**
2. Find each test contact (Funnel Test One, Chat Test Two, Quick Test Three, and any earlier test contacts from Exercise 11.2)
3. Delete them (or tag them as "test-contact" and keep them for future reference)
4. Go to **Opportunities** and delete the test opportunities from the pipeline
5. Go to **Conversations** and delete any test conversations

> **Important:** Do NOT delete your permanent test contact ("TEST - Do Not Delete" from Day 9). That one stays for ongoing workflow testing.

---

## Integration Checkpoint

Before moving on, verify that your complete multi-channel lead capture system meets these criteria:

**Lead Capture:**
- [ ] Free Trial funnel form creates a contact with all custom fields mapped
- [ ] Quick Contact form creates a contact and feeds into the same system
- [ ] Webchat creates contacts for new visitors (via pre-chat form)
- [ ] All entry points apply the `new-trial-lead` tag

**Automation:**
- [ ] Every new lead triggers a welcome email
- [ ] Every new lead triggers an SMS (if phone number provided)
- [ ] The Personalized Lead Nurture workflow from Day 9 fires for all new leads (via the shared `new-trial-lead` tag)
- [ ] Trigger link clicks from email campaigns create or update pipeline opportunities

**Pipeline:**
- [ ] Every new lead (regardless of source) creates an opportunity in Membership Sales at "New Inquiry"
- [ ] Opportunity values are set appropriately
- [ ] Pipeline gives you a single view of ALL leads

**Notifications:**
- [ ] Every new lead triggers an internal notification
- [ ] Webchat leads trigger an urgent notification (they expect a live response)
- [ ] You can see all of today's leads in the "Hot Leads" Smart List

**Data Quality:**
- [ ] Every contact has the correct tags identifying their source (form, webchat, quick contact, trigger link)
- [ ] Custom fields are populated when the data was collected
- [ ] No duplicate contacts are created when the same person uses multiple channels

If any item is unchecked, go back and fix it. A lead capture system with gaps is worse than no system at all -- it gives you false confidence that leads are being handled when they are actually falling through the cracks.

---

## Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental (2 dentists, procedures from $150 cleanings to $3,000 cosmetic work) needs a multi-channel lead capture system for new patients. Patients find BrightSmile through Google searches, insurance directory listings, Facebook ads, and word-of-mouth referrals. The practice currently relies on phone calls and a basic website -- leads who call after hours or visit the website on weekends are lost entirely.

**Your Task:** Design and build a complete "New Patient" lead capture system using the same integration approach you used for Sunrise Wellness. Build everything in your existing sub-account with "BrightSmile" in the naming.

### Entry Point 1: "Free Dental Exam" Funnel

You already built this funnel on Day 8. Today, verify it is fully wired:

1. **Form → Contact mapping:**
   - Patient intake fields (Date of Birth, Insurance Provider, Last Dental Visit, Current Concerns) map to custom fields
   - If these custom fields do not exist yet, create them:
     - "Insurance Provider" (Dropdown)
     - "Last Dental Visit" (Dropdown)
     - "Dental Concerns" (Long Text)

2. **Workflow:** "BrightSmile - New Patient Inquiry"
   - Trigger: Form Submitted > "New Patient Intake" (or whatever you named the dental form on Day 8)
   - Add Tag: `new-patient-inquiry`
   - Send Email: Welcome to BrightSmile -- what to expect at your first visit, what to bring (ID, insurance card, medication list), office hours
   - Create Opportunity: Patient Pipeline (create this if you have not already) > "New Inquiry" stage > Value: $150 (initial exam)
   - Internal Notification: "New patient inquiry: {{contact.first_name}} -- Insurance: {{contact.insurance_provider}}"
   - Wait 24 hours > If no tag `appointment-booked` > Follow-up email with patient testimonials and booking link
   - Wait 48 hours > If still no booking > "Limited availability" email + tag `needs-manual-followup`

### Entry Point 2: Webchat for After-Hours Inquiries

Dental practices lose a significant number of leads after hours. Someone has a toothache at 9 PM, searches "dentist near me," finds BrightSmile's website, and has questions. Without webchat, they leave and call the first dentist they find the next morning.

1. **Configure webchat with dental-specific greeting:**
   ```
   Welcome to BrightSmile Dental! Our office is open Mon-Fri
   8 AM - 5 PM. If you need to schedule an appointment or have
   a question, please share your name and email and we will
   respond as soon as possible.

   For dental emergencies, please call 911 or visit your
   nearest emergency room.
   ```

2. **Build "BrightSmile - Webchat Lead" workflow:**
   - Same structure as the Sunrise Wellness webchat workflow
   - Tag: `webchat-patient-lead`
   - Tag: `new-patient-inquiry` (shared tag for pipeline entry)
   - Create Opportunity: Patient Pipeline > "New Inquiry" > $150
   - Notification: "New webchat inquiry -- respond ASAP!"
   - 10-minute email follow-up with booking link and "what to bring" information

### Entry Point 3: Quick Appointment Request Form

A simplified form for the "Contact Us" page:

| Field | Type | Required |
|-------|------|----------|
| Name | Text | Yes |
| Phone | Phone | Yes |
| Email | Email | No |
| Reason for Visit | Dropdown: Routine Cleaning, Toothache/Pain, Cosmetic Consultation, Orthodontics, Other | No |

This form feeds into the same "BrightSmile - New Patient Inquiry" workflow (add as a second trigger) or a parallel workflow that applies the same `new-patient-inquiry` tag.

### Entry Point 4: Insurance Directory Referrals

Many patients find dentists through their insurance company's website. These patients often call directly rather than filling out forms.

- The Missed Call Text-Back workflow from Day 9 handles this automatically
- Add an additional tag: `source-insurance-directory` when a patient mentions they found BrightSmile through their insurance
- This tag helps track which insurance companies drive the most patients

### Smart Lists for BrightSmile:
- "New Patient Inquiries - Today" (tag `new-patient-inquiry`, added today)
- "Needs Callback" (tag `missed-call`, no tag `appointment-booked`)
- "After-Hours Inquiries" (tag `webchat-patient-lead`, contact created outside 8 AM - 5 PM)

### Test the complete system:
Run the same 4-test protocol as Exercise 11.9, but for the dental workflows. Submit the dental form, send a webchat message, submit the quick form, and verify all three appear in the Patient Pipeline.

---

## Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media, Web Design, retainers $2,000-$10,000/month) needs a lead capture system for potential clients. Agency leads come from Google searches, LinkedIn, industry conferences, referrals from existing clients, and content marketing (blog posts, case studies). The sales cycle is longer (2-4 weeks) and the leads need more qualification before entering the pipeline.

**Your Task:** Design and build a complete "Strategy Session" lead capture system. Build everything in your existing sub-account with "Elevate" in the naming.

### Entry Point 1: "Free Strategy Session" Funnel

You already built this funnel on Day 8. Today, verify it is fully wired:

1. **Form → Contact mapping:**
   - Business fields (Business Name, Website URL, Industry, Monthly Revenue, Current Marketing Channels) map to custom fields
   - Create any missing custom fields:
     - "Business Name" (Text)
     - "Website URL" (Text)
     - "Industry" (Dropdown)
     - "Monthly Revenue Range" (Dropdown)
     - "Current Marketing Channels" (Multi-Select or Tags)

2. **Workflow:** "Elevate - New Strategy Lead"
   - Trigger: Form Submitted > "Free Strategy Session"
   - Add Tag: `new-agency-lead`
   - Send Email: Professional welcome -- introduce the agency, mention results ("We have helped 50+ businesses increase organic traffic by an average of 187%"), include strategy session booking link
   - Create Opportunity: Agency Sales Pipeline > "New Lead" stage
   - **Dynamic opportunity value based on revenue range:**
     - If Monthly Revenue < $50K: Value = $2,000/mo
     - If Monthly Revenue $50K-$200K: Value = $5,000/mo
     - If Monthly Revenue > $200K: Value = $10,000/mo
     - (Use If/Else branching on the "Monthly Revenue Range" custom field to set different opportunity values)
   - Internal Notification: "New agency lead: {{contact.first_name}} from {{contact.business_name}} -- Revenue: {{contact.monthly_revenue_range}}"
   - Wait 1 day > Send case study email
   - Wait 3 days > If no tag `strategy-call-booked` > Send "5 Questions to Ask Any Digital Agency" email
   - Wait 4 more days > If still no booking > "Limited spots" email + tag `needs-manual-followup`

### Entry Point 2: Webchat for Website Visitors

Agency websites get a lot of tire-kickers. The webchat needs to qualify visitors while being welcoming:

1. **Configure webchat with agency-specific greeting:**
   ```
   Hey there! Looking to grow your business with digital marketing?
   I can answer quick questions or help you book a free strategy
   session with our team.

   What's your name and business email so we can follow up?
   ```

2. **Build "Elevate - Webchat Lead" workflow:**
   - Tag: `webchat-agency-lead`
   - Tag: `new-agency-lead` (shared tag)
   - Create Opportunity: Agency Sales Pipeline > "New Lead" > $3,000 (average retainer as default)
   - Urgent notification: "Potential client on webchat -- respond now!"
   - 10-minute email follow-up: link to case studies + strategy session booking

### Entry Point 3: Quick "Get a Quote" Form

A simplified form for LinkedIn ads, conference follow-ups, and content CTAs:

| Field | Type | Required |
|-------|------|----------|
| Name | Text | Yes |
| Business Email | Email | Yes |
| Website URL | Text | No |
| What service are you interested in? | Dropdown: SEO, PPC/Google Ads, Social Media Management, Web Design, Full Marketing Package, Not Sure Yet | No |

**Workflow for this form:**
- Same `new-agency-lead` tag to trigger the shared nurture sequence
- Additional tag based on selected service: `interested-seo`, `interested-ppc`, `interested-social`, `interested-web-design`, `interested-full-package`
- Pipeline opportunity value varies by service:
  - SEO: $2,000/mo
  - PPC: $3,000/mo
  - Social Media: $2,500/mo
  - Web Design: $7,500 (one-time project)
  - Full Package: $10,000/mo
  - Not Sure: $3,000/mo (default average)

### Entry Point 4: Trigger Links from Content Marketing

Elevate sends monthly email newsletters with links to blog posts and case studies. Each piece of content has trigger links:

- "Read our SEO guide" → Tag: `interested-seo`
- "See our PPC case study" → Tag: `interested-ppc`
- "View our social media portfolio" → Tag: `interested-social`

Build the same trigger link workflow you built for Sunrise Wellness, but with agency-specific tags and opportunity values.

### Smart Lists for Elevate:
- "New Agency Leads - This Week" (tag `new-agency-lead`, added in last 7 days)
- "High-Value Prospects" (opportunity value >= $5,000)
- "Needs Strategy Call" (tag `new-agency-lead`, no tag `strategy-call-booked`, added more than 3 days ago)
- "Service Interest Breakdown" (create separate lists for each service interest tag to see demand)

### Test the complete system:
Run the same 4-test protocol, adapted for agency workflows. Verify that all entry points converge into the Agency Sales Pipeline and that opportunity values are set correctly based on service interest and revenue range.

---

## Day 11 Recap

**What You Built Today:**
- Audited and verified all Phase 1 components needed for integration
- Tested and strengthened the Funnel → Contact → Pipeline flow
- Added webchat as a lead capture channel with its own workflow
- Built a Quick Contact form as a lightweight alternative entry point
- Wired trigger links from email campaigns into the pipeline system
- Built a notification system that alerts you to every new lead
- Created "Hot Leads" and "Webchat Needs Response" Smart Lists for daily monitoring
- Tested the entire system end-to-end with 3-4 simulated leads

**Key Integration Concepts:**

1. **Shared tags are the glue.** The `new-trial-lead` tag is what connects all your entry points to the shared Personalized Lead Nurture workflow. Every entry point applies this tag, and the nurture workflow triggers on this tag. Change the tag in one place and everything breaks -- so choose your tag naming convention carefully and stick with it.

2. **One pipeline, many entry points.** Every lead lands in the Membership Sales pipeline regardless of how they found you. This gives you a single source of truth for "how many leads are in the system right now?" and "how are they moving through the sales process?"

3. **Source tags for attribution.** While the shared `new-trial-lead` tag connects everyone to the same workflow, source-specific tags (`webchat-lead`, `quick-contact-form`, `source-facebook-ad`) let you track where leads come from. This is marketing attribution -- and it tells you which channels are worth investing in.

4. **Automation handles the routine, you handle the human.** The system sends welcome emails, creates pipeline opportunities, and follows up automatically. But webchat conversations, phone calls, and closing the sale still need a human. The automation buys you time and ensures nothing falls through the cracks.

**Certification Review Questions:**

1. Why is it important that all lead capture channels feed into the SAME pipeline rather than separate pipelines for each channel?
2. How do shared tags enable workflow chaining (one workflow triggering another)?
3. What is the difference between a "source tag" (like `webchat-lead`) and a "status tag" (like `new-trial-lead`)? Why do you need both?
4. Why does the webchat workflow check if the contact already has the `new-trial-lead` or `active-member` tag before creating a new opportunity?
5. What would happen if you forgot to add the Internal Notification action to one of your lead capture workflows?
6. How would you modify this system if Sunrise Wellness hired a dedicated sales person who should handle all new leads?

---

## Next Day Preview

**Day 12: Automated Sales Pipeline** -- Today you built the system that gets leads INTO the pipeline. Tomorrow you will automate what happens INSIDE the pipeline. When a lead moves from stage to stage, automated sequences will fire: outreach emails, trial management messages, conversion offers, and even automatic hand-off from the Sales pipeline to the Onboarding pipeline when someone becomes a member. The pipeline will essentially run itself.

**Before Day 12, make sure you have:**
- All lead capture entry points working (verified by today's end-to-end tests)
- The Membership Sales Pipeline with all stages from Day 5
- The New Member Onboarding Pipeline from Day 5
- Your email and SMS templates from Day 3 (you will use them in stage-triggered workflows)
- Your calendar booking links from Day 4 (workflows will include these for scheduling)
- Your coupons from Day 6 (the TRIALCONVERT coupon will be used in the conversion workflow)
