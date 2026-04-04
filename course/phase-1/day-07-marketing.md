# Day 7: Marketing - Email Campaigns & Social

**Time Required:** 3-4 hours
**Certification Alignment:** Email Builder, Email Campaigns, Trigger Links, Social Planner
**API Lab:** Yes - `scripts/day-07-marketing-api.py`

---

## Today's Mission

Sunrise Wellness Studio has members, templates, calendars, a pipeline, and products. Now it is time to market! Today you will build professional branded email templates for the studio, launch your first email campaign to a Smart List, and set up **Trigger Links** - special tracked URLs that tell you exactly what each member is interested in based on what they click. This is where your Smart Lists from Day 2 and templates from Day 3 evolve into actual marketing campaigns.

---

## Learning Objectives

1. Build professional email templates using the drag-and-drop email builder
2. Launch a targeted email campaign to a Smart List you created on Day 2
3. Create and use Trigger Links for behavioral tracking and contact segmentation
4. Understand email compliance requirements (CAN-SPAM, SPF/DKIM/DMARC)
5. Explore the Social Planner interface

---

## Part 1: Email Template Builder (60 min)

### What is the Email Builder?

The **Email Builder** is GHL's visual drag-and-drop tool for creating professional HTML emails - the kind of polished, branded emails you get from companies like Nike or your favorite restaurant.

Think of it like Canva, but specifically for emails. Instead of writing HTML code, you drag pre-built blocks (text, images, buttons, columns) onto a canvas, arrange them how you want, and style them with your brand colors and fonts. The builder handles all the technical formatting so your emails look great on both desktop and mobile devices.

**Why build email templates instead of just typing plain text emails?**

- **Consistent branding:** Every email from Sunrise Wellness Studio looks professional and on-brand
- **Reusability:** Build a template once, use it for every new member welcome or monthly newsletter
- **Personalization with merge fields:** Automatically insert each contact's name, membership level, or any custom value using `{{merge.fields}}` - the same custom values you set up on Day 1
- **Tracking:** The builder automatically tracks opens and clicks so you know what is working
- **Mobile responsiveness:** Templates automatically adjust for phone screens

> **Pro Tip:** Before building your first template, open 2-3 marketing emails you have received from businesses you admire. Notice their structure: logo header, hero section, body content, call-to-action button, footer. You will follow the same pattern.

---

### Exercise 7.1: Build the "New Member Welcome" Email

**Purpose:** Create a polished welcome email that every new Sunrise Wellness Studio member receives. This template will be reused in an automated workflow on Day 9.

Navigate to **Marketing > Emails > Templates** (the exact path may vary by GHL version - look for "Email Builder" or "Email Templates" under Marketing).

Click **+ Create Template** and choose a blank template (or pick a simple starter and clear it).

**Template Name:** "Sunrise Welcome Email"

Build the following layout by dragging elements onto the canvas:

**Header Section:**
1. Drag an **Image** block to the top
2. Upload or use a placeholder for the Sunrise Wellness Studio logo (a simple text block with the business name works fine if you do not have a logo image)
3. Set a background color that feels warm and energetic (orange, coral, or gold tones work well for a wellness brand)

**Hero Section:**
1. Drag a **Text** block below the header
2. Type the headline: `Welcome to Sunrise Wellness, {{contact.first_name}}!`
   - To insert the merge field, type `{{` and a dropdown will appear showing available fields - select `contact.first_name`
   - This means if Jane Smith receives this email, she will see "Welcome to Sunrise Wellness, Jane!"
3. Add a subheadline: "Your fitness journey starts now. Here is what is waiting for you."
4. Style: Make the headline large (24-28px), bold, centered

**Benefits Section (3 columns):**
1. Drag a **Columns** element and choose the 3-column layout
2. Fill each column:
   - **Column 1:** "Expert Trainers" - "Work one-on-one with certified personal trainers who build a plan around YOUR goals."
   - **Column 2:** "Group Energy" - "HIIT, Yoga, Pilates - find your crew in our high-energy group classes."
   - **Column 3:** "Nutrition Coaching" - "Fuel your results with personalized nutrition plans from our certified coaches."
3. Add a small icon or emoji above each title if you like (optional)

**Call-to-Action Section:**
1. Drag a **Button** element
2. Button text: "Book Your First Session"
3. Button URL: paste the link to your Sunrise Wellness calendar from Day 4 (or use a placeholder URL like `#book`)
4. Style the button with a contrasting color (e.g., bright orange on a white background) so it stands out
5. Add text below: "New members get a free fitness assessment with their first booking."

**Social Proof Section:**
1. Drag a **Text** block
2. Add a testimonial: *"Sunrise Wellness changed my life. I have lost 30 pounds and gained so much confidence. The trainers actually care!"* - Sarah M., Premium Member
3. Style it in italics with a subtle background color

**Footer Section (REQUIRED for legal compliance):**
1. Drag a **Text** block for the footer
2. Include:
   - Sunrise Wellness Studio
   - `{{business.address}}` (or type your practice address)
   - `{{business.phone}}` | `{{business.email}}`
   - Hours: Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM
3. Add **Social media links** (placeholder URLs are fine: Facebook, Instagram, YouTube)
4. Add the **Unsubscribe link** - this is legally required. GHL provides an automatic unsubscribe merge field: `{{unsubscribe_link}}`. Drag it in or type "Unsubscribe" and link it to `{{unsubscribe_link}}`
5. Add: "You are receiving this email because you signed up at Sunrise Wellness Studio."

**Final Steps:**
1. Click **Preview** and toggle between Desktop and Mobile views - make sure nothing looks broken on mobile
2. Send a **test email** to yourself - check that merge fields work and links are clickable
3. **Save** the template

> **Pro Tip:** Mobile preview is critical. Over 60% of emails are opened on phones. If your button is too small to tap with a thumb, or your text is too tiny to read, you will lose engagement.

---

### Exercise 7.2: Build the "Monthly Class Schedule" Newsletter

**Purpose:** Create a monthly newsletter template that keeps members engaged and informed about what is happening at the studio. Newsletters build community and reduce membership churn.

Click **+ Create Template** again.

**Template Name:** "Sunrise Monthly Newsletter"

**Header:**
1. Logo (same as Exercise 7.1 for brand consistency)
2. Text: "Monthly Newsletter - [Month/Year]" (you will update this each month before sending)

**Featured Class Schedule Section:**
1. Use a **Text** block or **Table** (if available) to create:
   ```
   THIS MONTH'S CLASS SCHEDULE
   
   Monday:    6AM HIIT | 12PM Yoga | 6PM Pilates
   Tuesday:   7AM Spin | 12PM HIIT | 7PM Yoga
   Wednesday: 6AM HIIT | 12PM Pilates | 6PM Spin
   Thursday:  7AM Yoga | 12PM HIIT | 7PM Pilates
   Friday:    6AM HIIT | 12PM Yoga | 5PM Open Gym
   Saturday:  8AM HIIT | 10AM Yoga | 12PM Pilates
   Sunday:    9AM Yoga | 11AM Open Gym
   ```
2. Style the schedule so it is easy to scan (bold the class names, use consistent spacing)

**Member Spotlight Section:**
1. Heading: "Member Spotlight"
2. Placeholder: "[Member Name] joined 6 months ago and has already hit their goal of running a 5K. Read their story..."
3. This section humanizes the studio and motivates other members

**Tip of the Month:**
1. Heading: "Coach's Tip of the Month"
2. Placeholder: "Recovery is just as important as training. Try adding 10 minutes of stretching after every session this month."

**Special Offer Section:**
1. Heading: "This Month's Special"
2. Text: `{{offer.discount}}` - "Refer a friend and you BOTH save. Use code FRIEND20 at checkout."
   - Remember, `{{offer.discount}}` is the custom value you set on Day 1 ("20% Off Your First Month")
3. Add a CTA button: "Share With a Friend"

**Footer:**
1. Same business info and unsubscribe link as Exercise 7.1 (copy/paste for consistency)
2. Add social media links

Preview on desktop and mobile, send a test to yourself, and save.

---

### Exercise 7.3: Build the "Promotional Offer" Email

**Purpose:** Create a conversion-focused email for driving trial signups and special offer redemptions. This is the email you would send to cold or warm leads to get them in the door.

Click **+ Create Template** again.

**Template Name:** "Sunrise Promotional Offer"

**Hero Section:**
1. Large, bold headline: `{{offer.free_trial}}`
   - This will render as "Free 7-Day Trial Pass" (the custom value from Day 1)
2. Subheadline: "Experience everything Sunrise Wellness has to offer - no commitment, no risk."
3. Use an energetic background color or image

**Benefits Section:**
1. Three short bullet points:
   - "Unlimited group classes for 7 full days"
   - "Free fitness assessment with a certified trainer"
   - "Full access to all studio amenities"

**Urgency Section:**
1. Text: "This offer expires [DATE]. Only 15 trial spots remaining this month."
2. Why urgency works: People procrastinate. A deadline and limited availability create a reason to act now instead of "later" (which usually means never)

**CTA Button:**
1. Button text: "Claim Your Free Trial"
2. Link: Your funnel landing page (you will build this on Day 8) or your calendar booking link from Day 4
3. Make this button large and impossible to miss

**Secondary CTA:**
1. Text: "Not ready for a trial? Check out our class schedule and pricing:"
2. Button: "View Membership Options" with link to your pricing page or funnel (placeholder URL is fine)

**Footer:**
1. Same branded footer with unsubscribe link

Preview, test, save.

---

## Part 2: Email Campaigns (45 min)

### What is an Email Campaign?

An **Email Campaign** is a one-time email send to a specific group of contacts. Think of it as a broadcast - you pick who receives it, choose which email template to send, and either send it immediately or schedule it for later.

This is different from the automated workflow emails you will build on Day 9. A campaign is something you manually decide to send ("Let me email all our new leads about the January special"), while a workflow email fires automatically when something happens ("When someone fills out a form, send them a welcome email").

**When to use campaigns:**
- Monthly newsletters
- Seasonal promotions
- Event announcements
- One-time offers or updates

**When to use workflows instead (Day 9):**
- Welcome sequences triggered by signup
- Follow-ups after a booking
- Drip sequences over multiple days

---

### Exercise 7.4: Create and Launch Your First Campaign

**Purpose:** Send your welcome email template to the "New Leads" Smart List you built on Day 2. This is your first real marketing send.

Navigate to **Marketing > Emails > Campaigns** (or Email Campaigns):

1. Click **+ Create Campaign**
2. **Campaign name:** "New Member Welcome - [Today's Date]"
3. **Select your audience:**
   - Choose the **"New Leads"** Smart List you created on Day 2
   - If you do not have that Smart List, select contacts by tag (e.g., "new-lead" or "csv-import-day2")
   - You should see a recipient count - even 3-5 contacts is fine for practice
4. **Select template:** Choose your "Sunrise Welcome Email" from Exercise 7.1
5. **Configure the sender:**
   - From name: "Sunrise Wellness Studio"
   - From email: Your configured sending email
   - Reply-to: Same email (so replies come to you)
6. **Subject line:** "Welcome to Sunrise Wellness, {{contact.first_name}}!"
   - **Preview text:** "Here is what is waiting for you as a new member..."
   - Preview text is the gray snippet that appears after the subject line in an inbox - it is valuable real estate, so make it compelling
7. **Schedule:**
   - Choose **Send Immediately** for this exercise (in real campaigns you would schedule for optimal times - typically Tuesday-Thursday, 9-11 AM)
8. **Review:**
   - Double-check the recipient count
   - Preview the email one final time
   - **Send a test email to yourself first** - always do this before a real send
9. **Launch** the campaign

> **Pro Tip:** Always send a test to yourself AND open it on your phone before launching to your full list. What looks great on a desktop preview can sometimes break on actual mobile email clients.

---

### Exercise 7.5: Monitor Campaign Performance

**Purpose:** Learn to read campaign metrics so you can improve future sends.

After your campaign sends (give it a few minutes):

1. Navigate to the campaign dashboard (click into your campaign)
2. Review these key metrics:

| Metric | What It Means | Healthy Benchmark |
|--------|--------------|-------------------|
| **Sent** | Total emails sent | Should match your list size |
| **Delivered** | Successfully landed in inboxes | 95%+ is good |
| **Open Rate** | % who opened the email | 20-30% is average |
| **Click Rate** | % who clicked any link | 2-5% is average |
| **Bounce Rate** | Emails that could not be delivered | Under 2% is healthy |
| **Unsubscribe Rate** | % who opted out | Under 0.5% is normal |

3. Click into individual contact activity:
   - Who opened your email? (These are your most engaged members)
   - Who clicked? What did they click?
   - Did anyone bounce? (Bad email addresses to clean up)

4. With a small test list, your numbers may look unusual (1 open out of 3 contacts = 33% open rate). That is normal - these benchmarks apply to lists of 100+ contacts.

> **Pro Tip:** If your open rate is below 15%, the problem is usually your subject line or sender reputation. If opens are good but clicks are low, the problem is your email content or call-to-action.

---

### Email Compliance Checklist

Before sending ANY campaign, verify all of the following. These are not suggestions - they are legal requirements under the CAN-SPAM Act (US) and similar laws worldwide:

- [ ] **Unsubscribe link** is present and functional (every marketing email must have one)
- [ ] **Physical business address** is in the footer (required by CAN-SPAM)
- [ ] **From address** is not misleading (must accurately identify the sender)
- [ ] **Subject line** is not deceptive (must relate to the email content)
- [ ] **Contact list is opt-in** (recipients agreed to receive emails - never use purchased lists)
- [ ] **Content matches** what subscribers signed up for (do not bait-and-switch)

Violating CAN-SPAM can result in fines of up to $51,744 per email. GHL includes unsubscribe handling automatically, but it is your responsibility to make sure it is in every template.

---

## Part 3: Trigger Links (45 min)

### What are Trigger Links?

A **Trigger Link** is a special tracked URL that does two things when a contact clicks it:

1. **Redirects** the contact to a destination (like a normal link)
2. **Triggers an action** on that contact's record - such as adding a tag, moving them to a pipeline stage, or starting a workflow

Think of it like a trip wire. A normal link in an email just takes someone to a page. A Trigger Link takes them to a page AND secretly records what they were interested in.

**Why are Trigger Links powerful?**

Imagine you send a newsletter to 500 Sunrise Wellness members with three links:
- "Learn about Personal Training" (trigger link)
- "See Group Class Schedule" (trigger link)  
- "Explore Nutrition Coaching" (trigger link)

After the send, you know exactly which members are interested in which services - without asking them directly. Their clicks told you. Now you can:
- Send targeted follow-up emails about personal training ONLY to people who clicked that link
- Have your sales pipeline automatically updated
- Trigger a phone call task for high-value leads

This is **behavioral segmentation** - grouping contacts by what they DO, not just what they say.

---

### Exercise 7.6: Create Trigger Links for Sunrise Wellness

**Purpose:** Build trigger links that will track which services each member is interested in. You will insert these into your email templates next.

Navigate to **Marketing > Trigger Links** (some GHL versions put this under Settings > Trigger Links):

Create each of the following trigger links:

**Trigger Link 1: "Interested in Personal Training"**
1. Click **+ Create Trigger Link**
2. **Name:** `interested-personal-training`
3. **Redirect URL:** Your calendar booking link from Day 4 (the PT consultation calendar) or a placeholder URL
4. **Action:** Add tag `interested-personal-training`
5. Save

**Trigger Link 2: "Interested in Group Classes"**
1. **Name:** `interested-group-classes`
2. **Redirect URL:** A page with your class schedule (or placeholder)
3. **Action:** Add tag `interested-group-classes`
4. Save

**Trigger Link 3: "Interested in Nutrition Coaching"**
1. **Name:** `interested-nutrition`
2. **Redirect URL:** A page about your nutrition services (or placeholder)
3. **Action:** Add tag `interested-nutrition`
4. Save

**Trigger Link 4: "Clicked Book Trial"**
1. **Name:** `clicked-book-trial`
2. **Redirect URL:** Your calendar booking link or funnel page
3. **Actions (multiple):**
   - Add tag `clicked-book-trial`
   - Move opportunity to pipeline stage: "Interested" in your Sunrise Wellness pipeline from Day 5
4. Save

You should now have 4 trigger links. Each one has a unique URL that GHL generated - you will use these URLs in your emails instead of regular links.

> **Pro Tip:** Name your trigger links with a clear, consistent convention like `interested-[service]` or `clicked-[action]`. When you have 50+ trigger links someday, good naming saves hours of confusion.

---

### Exercise 7.7: Insert Trigger Links into Email Templates

**Purpose:** Replace regular links in your email templates with trigger links so every click is tracked and actionable.

1. Open your **"Sunrise Promotional Offer"** email template from Exercise 7.3
2. Find the "Claim Your Free Trial" CTA button
3. Replace the button URL with your **Trigger Link 4** (`clicked-book-trial`) URL
   - GHL may let you select trigger links from a dropdown, or you may need to paste the trigger link URL directly
4. Add a text section below the CTA with three links:
   - "Explore Personal Training" - link to **Trigger Link 1** URL
   - "Browse Group Classes" - link to **Trigger Link 2** URL
   - "Learn About Nutrition Coaching" - link to **Trigger Link 3** URL
5. Save the template
6. Send a **test email to yourself**
7. Open the test email and click one of the trigger links
8. Go to **Contacts** and find your own contact record - verify the tag was applied

If the tag appeared on your contact record, your trigger links are working correctly.

---

### Exercise 7.8: Build a "What Interests You?" Preference Email

**Purpose:** Create a self-segmentation email that lets members tell you what they care about simply by clicking. This is one of the most powerful email marketing techniques - and it requires zero manual work after setup.

Click **+ Create Template**.

**Template Name:** "Sunrise - What Interests You?"

**Subject Line (for when you send it):** "Quick question, {{contact.first_name}} - what are you most interested in?"

**Body Layout:**

**Header:**
- Logo
- "Help us personalize your experience!"

**Introduction:**
- "Hi {{contact.first_name}},"
- "We want to make sure you are getting the most out of your Sunrise Wellness membership. Click on anything below that interests you, and we will send you more information about it:"

**Interest Options (each linked to a trigger link):**

Use a visually appealing layout - either large buttons or image cards for each option:

| Option | Trigger Link | Tag Applied |
|--------|-------------|-------------|
| "Personal Training - Get a custom workout plan" | Trigger Link 1 | `interested-personal-training` |
| "Group Classes - HIIT, Yoga, Pilates & more" | Trigger Link 2 | `interested-group-classes` |
| "Nutrition Coaching - Fuel your results" | Trigger Link 3 | `interested-nutrition` |
| "Free 7-Day Trial - Share with a friend" | Trigger Link 4 | `clicked-book-trial` |

**Closing:**
- "Click as many as you like. We will tailor your experience based on what matters to you."
- "See you at the studio!"
- "- The Sunrise Wellness Team"

**Footer:**
- Standard branded footer with unsubscribe link

Save the template. In a real business, you would send this as a campaign to your entire active member list. The clicks automatically segment your audience - members who click "Nutrition Coaching" get tagged, and you can then create a Smart List of everyone with the `interested-nutrition` tag for targeted campaigns.

---

## Part 4: Email Compliance & Deliverability (20 min)

### What is Email Deliverability?

**Email deliverability** is whether your emails actually land in the inbox vs. the spam folder. You can write the perfect email, but if it goes to spam, nobody will ever see it. Deliverability depends on technical setup (authentication records) and sending behavior (not spamming).

### What are SPF, DKIM, and DMARC?

These are three **DNS records** (technical settings on your domain) that prove to email providers like Gmail and Outlook that you are authorized to send email from your domain. Think of them as ID badges:

- **SPF** (Sender Policy Framework): Lists which servers are allowed to send email on behalf of your domain. Like saying "only these mail trucks can deliver mail with my return address."
- **DKIM** (DomainKeys Identified Mail): Adds a digital signature to your emails proving they were not tampered with in transit. Like a wax seal on a letter.
- **DMARC** (Domain-based Message Authentication): Tells receiving servers what to do if SPF or DKIM checks fail (report it, quarantine it, or reject it).

### Exercise 7.9: Review Email Authentication Settings

Navigate to **Settings > Email Services** (or Settings > Domains):

1. **Check your sending domain configuration:**
   - Is a dedicated sending domain set up, or are you using GHL's shared domain?
   - If using a shared domain (default for most sub-accounts), you are sharing reputation with other GHL users
   - A dedicated domain gives you full control over reputation but requires DNS setup
   
2. **Review DNS records** (if you have domain access):
   - Look for SPF, DKIM, and DMARC record status
   - GHL will show you whether these are configured and verified
   - If you do not have domain access, note what records WOULD need to be set up

3. **Default unsubscribe settings:**
   - Check that the default unsubscribe link is enabled
   - Customize the unsubscribe confirmation page text if possible
   - Test the unsubscribe flow by clicking the unsubscribe link in your test email

4. **Reply-to configuration:**
   - Verify your reply-to address is correct
   - Send a test email to yourself and try replying - make sure the reply goes where expected

> **Pro Tip:** If you are just practicing in a sub-account, the shared domain is perfectly fine. But for a real business, setting up a dedicated sending domain with proper SPF/DKIM/DMARC is one of the most impactful things you can do for email performance.

---

## Part 5: Social Planner Overview (15 min)

### What is the Social Planner?

The **Social Planner** is GHL's built-in social media management tool. It lets you create, schedule, and publish posts to multiple social media platforms from one place - similar to tools like Hootsuite or Buffer.

Supported platforms include Facebook, Instagram, Google Business Profile, LinkedIn, and TikTok (platform availability may vary).

### Exercise 7.10: Explore the Social Planner Interface

**Purpose:** Familiarize yourself with the Social Planner so you know what is available. Connecting social accounts is optional for this course since it requires business social media accounts.

Navigate to **Marketing > Social Planner**:

1. **Explore the interface:**
   - Note the calendar view (monthly, weekly, daily)
   - Find the post composer
   - Look at the platform connection options
   
2. **If you have business social accounts to connect:** Go ahead and connect them. Follow the OAuth prompts for each platform.

3. **If you do not have social accounts to connect (totally fine):** Explore the connection interface and note which platforms are supported. You can still explore the post composer.

4. **Create a draft social post** (does not require connected accounts):
   - Click to create a new post
   - Write sample copy: "Start your week strong! Monday morning HIIT class at 6AM. First class free for new members. #SunriseWellness #FitnessMotivation"
   - Add an image (any stock photo or placeholder)
   - Note the scheduling options (date, time, platform selection)
   - Save as draft (do not publish)

5. **Review the calendar view** to see your draft post on the scheduled date

---

## Part 6: API Lab

Run the Day 7 marketing API script to practice managing email campaigns and trigger links programmatically:

```bash
python scripts/day-07-marketing-api.py
```

This script covers:
1. Creating and managing email templates via API
2. Listing campaigns and campaign statistics
3. Working with trigger links programmatically
4. Retrieving email delivery and engagement data

Review the script output and compare the API results with what you see in the GHL dashboard.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental (2 dentists, procedures ranging from $150 cleanings to $3,000 cosmetic work) needs an email marketing system to stay in touch with patients, encourage regular visits, and promote high-value cosmetic services.

**Your Task:**

**Build 4 Email Templates:**

1. **"New Patient Welcome"**
   - Warm welcome with dentist photos and bios
   - "What to expect at your first visit" section
   - Office hours and location with map link
   - CTA: "Complete Your Patient Forms Online" (link to intake form - you will build this on Day 8)

2. **"Cleaning Recall Reminder"**
   - Friendly reminder: "Hi {{contact.first_name}}, it has been 6 months since your last cleaning!"
   - Why regular cleanings matter (brief educational content)
   - CTA Button: "Book Your Cleaning" - use a **trigger link** named `clicked-book-cleaning` that adds the tag `due-for-cleaning-responded`
   - Include: "Can't make it this month? Reply to this email and we will find a time that works."

3. **"Post-Procedure Care Instructions"**
   - Heading: "Your After-Care Guide"
   - Personalized with procedure type (use placeholder text since you will not have procedure-specific custom fields yet)
   - Clear numbered care steps
   - "When to call us" emergency section
   - CTA: "Questions? Call us at {{business.phone}}"

4. **"Referral Request"**
   - "Love your smile? Share the love!"
   - Referral offer: "Refer a friend and you both receive $50 off your next visit"
   - CTA: "Refer a Friend" button
   - Easy sharing: include a shareable link or referral code placeholder

**Create a Campaign:**
- Send the "Cleaning Recall Reminder" to a Smart List called "Patients Due for Cleaning" (create this Smart List with filter: tag contains `patient` AND last activity older than 90 days - adjust filters based on your test data)
- Schedule it as if it were going out Tuesday at 10 AM

**Create Trigger Links:**
- `interested-whitening` - tag: `interested-whitening`, redirect to a page about whitening services
- `interested-orthodontics` - tag: `interested-orthodontics`, redirect to orthodontics info page
- Insert both trigger links into the New Patient Welcome email as "Learn about our cosmetic services" section

---

### Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media, Email Marketing, Web Design, retainers from $2,000-$10,000/month) needs email marketing to nurture prospects, keep current clients informed, and position the agency as a thought leader.

**Your Task:**

**Build 3 Email Templates:**

1. **"Prospect Nurture - Case Study"**
   - Subject line idea: "How we helped [Industry] company grow 340% in 6 months"
   - Brief case study summary (2-3 paragraphs with placeholder metrics)
   - Key results in a highlight box (e.g., "+340% organic traffic", "5.2x ROAS", "$1.2M revenue generated")
   - CTA: "Want Results Like These?" - trigger link `download-case-study` (tag: `downloaded-case-study`)
   - Secondary CTA: "Book a Free Strategy Session" - trigger link to calendar

2. **"Monthly Client Report Notification"**
   - Clean, professional header
   - "Hi {{contact.first_name}}, your monthly performance report for [Month] is ready."
   - Summary highlights: "Here is a quick snapshot..." with placeholder metrics
   - CTA: "View Full Report" (link to reporting dashboard or shared document)
   - "Questions about your results? Reply to this email or book a call with your account manager."

3. **"Agency Newsletter - Industry Tips"**
   - Header: "The Digital Edge - [Month] Edition"
   - 3 industry tips/trends (e.g., "Google's latest algorithm update", "Why short-form video is dominating", "Email open rates by industry")
   - Each tip has a brief summary and "Read More" link
   - Agency spotlight: Recent win or new service offering
   - CTA: "Need help implementing these strategies? Let's talk."

**Create a Campaign:**
- Send the "Prospect Nurture - Case Study" email to a Smart List called "Active Leads" (create with filter: tag contains `lead` AND pipeline stage is NOT "Closed - Won" or "Closed - Lost")

**Create Trigger Links:**
- `interested-seo` - tag: `interested-seo`
- `interested-ppc` - tag: `interested-ppc`
- `interested-social-media` - tag: `interested-social-media`
- `download-case-study` - tag: `downloaded-case-study`

Insert service-specific trigger links into the newsletter template. Add a section: "Which services are you most interested in?" with clickable links for SEO, PPC, and Social Media. This lets prospects self-segment just like the Sunrise Wellness preference email.

---

## Day 7 Recap

**What You Built Today:**
- 3 professional email templates for Sunrise Wellness Studio (Welcome, Newsletter, Promotional)
- 1 preference/self-segmentation email with trigger links
- Your first email campaign sent to a Smart List
- 4 trigger links for behavioral tracking
- Reviewed email compliance and deliverability fundamentals

**Key Concepts to Remember:**
1. Every marketing email MUST include an unsubscribe link and physical business address
2. Trigger Links track clicks AND trigger actions (tags, pipeline moves) - they are your behavioral segmentation engine
3. Campaigns are one-time sends to a list; workflow-triggered emails are automatic (Day 9)
4. SPF, DKIM, and DMARC are the three DNS records that authenticate your sending domain
5. The preference/self-segmentation email (Exercise 7.8) is one of the highest-ROI email techniques because contacts tell you what they want through their clicks

**Recap Questions:**
1. What is the legal difference between a marketing email and a transactional email in terms of CAN-SPAM requirements?
2. How do Trigger Links differ from regular hyperlinks, and why does that matter for marketing?
3. What three metrics would you check first if a campaign underperformed?
4. How would you use trigger links and Smart Lists together to send targeted follow-ups?
5. A client's email open rate is 5%. What are the first three things you would investigate?

---

## Next Day Preview

**Day 8: Sites - Funnels & Websites** - Tomorrow you will build Sunrise Wellness Studio's online presence: a lead capture funnel that turns website visitors into contacts, a detailed intake form, and a qualifying survey with conditional logic. The form you build will feed directly into the pipeline from Day 5 and trigger the templates from Day 3 - connecting everything you have built so far.

**Before Day 8, make sure you have:**
- Your 3 email templates from today (we will link to them from funnel pages)
- Your trigger links (we will use them in funnel CTAs)
- Your calendar from Day 4 (we will embed it in the thank-you page)
- Your pipeline from Day 5 (form submissions will create opportunities)
