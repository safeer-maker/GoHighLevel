# Day 8: Sites - Funnels & Websites

**Time Required:** 3-4 hours
**Certification Alignment:** Funnel vs Website Builder, Domain Setup, Page Builder, Forms, Surveys (with Conditional Logic)
**API Lab:** No dedicated script (Sites are visual builders; forms connect to workflows on Day 9)

---

## Today's Mission

Everything you have built for Sunrise Wellness Studio so far lives "inside" GHL - contacts, templates, calendars, pipelines, products, email campaigns. But how do potential members actually find you and sign up? Today you will build the studio's online presence: a **lead capture funnel** that turns website visitors into contacts, a detailed **intake form** that collects member information, and a **qualifying survey** that helps you understand what each prospect wants before they ever walk through the door. The form you build today will feed directly into the pipeline from Day 5 and trigger the templates from Day 3 - all automated on Day 9.

---

## Learning Objectives

1. Understand when to use a Funnel vs a Website and why the distinction matters
2. Build a multi-step lead capture funnel with landing and thank-you pages
3. Create forms with custom fields that map to contact records
4. Build surveys with conditional logic (branching paths based on answers)
5. Connect forms and surveys to workflow triggers (preview for Day 9)

---

## Part 1: Funnel vs Website - When to Use Which (20 min)

### What is a Funnel?

A **funnel** is a focused set of web pages designed around ONE specific goal - usually getting someone to take a single action like signing up, booking a call, or buying something. Funnels are linear: Page 1 leads to Page 2, which leads to Page 3. There is no navigation menu, no sidebar, no "About Us" link - nothing to distract the visitor from the one thing you want them to do.

Think of a funnel like a hallway with one door at the end. The visitor walks in and the only way forward is through that door (your call-to-action). There are no side rooms to wander into.

**Example for Sunrise Wellness:** A "Free 7-Day Trial" funnel from a Facebook ad. The visitor lands on a page that sells the free trial, fills out a form, and lands on a thank-you page. Two pages, one goal: get the signup.

### What is a Website?

A **website** is a full multi-page online presence with navigation, multiple sections, and various purposes. Visitors can browse around - read about your services, check the schedule, view pricing, read the blog, find your location.

Think of a website like a building with many rooms. Visitors can explore at their own pace and find what they are looking for.

**Example for Sunrise Wellness:** The full SunriseWellness.com site with pages for Home, Classes, Trainers, Pricing, Schedule, Blog, and Contact.

### When to Use Which?

| | Funnel | Website |
|---|--------|---------|
| **Goal** | ONE specific action (sign up, buy, book) | General business presence and information |
| **Structure** | Linear steps (Page 1 > Page 2 > Done) | Multi-page with navigation menu |
| **Navigation** | No menu - minimal distractions | Full nav bar with links to all pages |
| **Traffic Source** | Paid ads, email links, social media CTAs | Organic search (Google), direct visits |
| **SEO** | Limited - not designed for search ranking | Full SEO capabilities for search ranking |
| **Conversion Focus** | Very high - everything points to one CTA | Lower - visitors may browse without acting |
| **Best For** | Ad campaigns, promotions, lead magnets | Company presence, credibility, content |

**For Sunrise Wellness, we will use both:**
- **Funnel** for the "Free 7-Day Trial" offer (linked from ads, emails, social posts)
- **Website** for the full business presence (linked from Google, business cards, etc.)

Today we will focus on building the **funnel** because it directly captures leads and feeds your pipeline. Websites follow the same page builder - once you can build a funnel, you can build a website.

### Exercise 8.1: Explore Both Builders

**Purpose:** See the difference between the Funnel and Website builders before you start building.

Navigate to **Sites** in the left sidebar:

1. Click **Funnels** - note the interface:
   - Funnels are organized as a list of funnel projects
   - Each funnel contains one or more "steps" (pages)
   - Steps are sequential - there is a clear flow from one to the next
   
2. Click **Websites** - compare:
   - Websites have a global navigation that appears on every page
   - You can add unlimited pages with different purposes
   - There is a site-wide header and footer

3. If any templates are available, open one of each to see the structural difference

4. Note: Both use the same drag-and-drop **Page Builder** for actually designing pages. The builder is the same - the difference is in how the pages are organized and connected.

---

## Part 2: Build the "Free Trial" Funnel (60 min)

### What is a Landing Page?

A **landing page** is the first page someone "lands on" when they click your ad, email link, or social media post. It is the front door of your funnel. A good landing page does three things: (1) immediately tells the visitor what they will get, (2) explains why they should want it, and (3) makes it easy to take action.

The landing page you are about to build for Sunrise Wellness will be used in email campaigns (you built those yesterday), social media posts, and potentially paid ads.

---

### Exercise 8.2: Build a 2-Step Lead Capture Funnel

**Purpose:** Create a complete funnel that captures Free Trial signups for Sunrise Wellness Studio. This is the page you would link to from your promotional emails (Day 7), social posts, and any advertising.

Navigate to **Sites > Funnels > + Create Funnel**:

1. Select **"Start from Scratch"** (or pick a simple lead capture template and modify it)
2. **Funnel Name:** "Sunrise Wellness - Free Trial"

**Step 1: Landing Page**

Click into the first step (or add one) and name it "Free Trial Landing Page". Open the page builder.

Build the following sections by dragging elements from the builder sidebar:

**Hero Section (the first thing visitors see):**
1. Add a **Section** with a full-width background (use a fitness-related stock image or a solid brand color - warm orange or gold)
2. Drag a **Headline** element:
   - Text: "Get Your Free 7-Day Trial at Sunrise Wellness Studio"
   - Style: Large (32-40px), bold, white text if on a dark background
3. Add a **Sub-headline:**
   - Text: "Unlimited group classes. Free fitness assessment. No commitment required."
4. Add a **Button** element:
   - Text: "Claim Your Free Trial"
   - Link: Set this to scroll down to the form section (anchor link) or link to `#form`
   - Style: Large, high-contrast color (e.g., bright white button on orange background)

**Benefits Section (3 columns):**
1. Add a new **Section** with a white or light background
2. Add a **Heading:** "Why Sunrise Wellness?"
3. Drag a **Columns** element - select 3 columns
4. Fill each column:
   - **Column 1:** 
     - Icon or small image (a dumbbell icon or trainer image)
     - Heading: "Expert Training"
     - Text: "Our certified personal trainers create customized programs for your specific goals - whether you are a total beginner or a seasoned athlete."
   - **Column 2:**
     - Icon or small image (a group class image)
     - Heading: "Group Classes"
     - Text: "HIIT, Yoga, Pilates, Spin - choose from 30+ weekly classes. The group energy keeps you motivated and accountable."
   - **Column 3:**
     - Icon or small image (a nutrition image)
     - Heading: "Nutrition Coaching"
     - Text: "Exercise is only half the equation. Our nutrition coaches help you fuel your results with a plan that fits your life."

**Form Section:**
1. Add a new **Section** with a slightly different background color to make it stand out
2. Add a **Heading:** "Start Your Free 7-Day Trial"
3. Add a **Sub-heading:** "Fill out the form below and we will get you set up. It takes less than 2 minutes."
4. Add a **Form** element - you will build the actual form in Part 3 (Exercise 8.4) and come back to embed it here
5. For now, leave a placeholder or add a temporary simple form

**Social Proof Section:**
1. Add a new **Section**
2. Add a **Heading:** "Trusted by 500+ Members"
3. Add 2-3 **testimonial blocks** (use placeholder text):
   - *"I was nervous to start, but the trainers made me feel right at home. I have been coming 4 times a week for 3 months and I have never felt better!"* - Maria R.
   - *"The group classes are addictive. HIIT on Monday, Yoga on Wednesday, Pilates on Friday - it is the best part of my week."* - David K.
   - *"I tried other gyms but nothing stuck. Sunrise Wellness is different because of the community. People actually know your name here."* - James T.

**FAQ Section:**
1. Add a new **Section**
2. Add a **Heading:** "Frequently Asked Questions"
3. Add text blocks for each FAQ (or use an accordion element if available):
   - **"What is included in the free trial?"** - "Full access to all group classes, one free fitness assessment with a trainer, and use of all studio amenities for 7 days."
   - **"Do I need to bring anything?"** - "Just wear comfortable workout clothes and bring a water bottle. We provide towels, mats, and all equipment."
   - **"What happens after the 7 days?"** - "No automatic charges. If you love it (and we think you will), your trial host will walk you through membership options. No pressure."
   - **"I am a total beginner. Is this for me?"** - "Absolutely. Over 40% of our members started with zero gym experience. Every class offers modifications for all fitness levels."

**Footer:**
1. Add a minimal footer:
   - Sunrise Wellness Studio | `{{business.address}}`
   - `{{business.phone}}` | `{{business.email}}`
   - Hours: Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM
   - Privacy Policy link (placeholder is fine)

**Final Landing Page Steps:**
1. Set the page **URL path** (e.g., `/free-trial`)
2. Set the **SEO title:** "Free 7-Day Trial | Sunrise Wellness Studio"
3. Set the **Meta description:** "Try Sunrise Wellness Studio free for 7 days. Unlimited group classes, free fitness assessment, no commitment."
4. **Preview** on Desktop, Tablet, and Mobile - adjust any elements that look off on smaller screens
5. Save

---

**Step 2: Thank You Page**

Add a second step to your funnel and name it "Thank You". Open the page builder.

**Confirmation Section:**
1. Add a **Heading:** "You are All Set, {{contact.first_name}}!"
   - The `{{contact.first_name}}` merge field will display the name they just entered in the form
2. Add text: "Your Free 7-Day Trial pass is confirmed. Here is what happens next:"

**Next Steps Section:**
1. Use a numbered list or icon list:
   - **Step 1:** "Check your email - we just sent your trial confirmation and a welcome guide."
   - **Step 2:** "Book your free fitness assessment below (this is the best way to start)."
   - **Step 3:** "Show up! Bring workout clothes and a water bottle. We handle the rest."

**Calendar Embed:**
1. Add a **Calendar widget** or **iframe** element
2. Embed your Sunrise Wellness calendar from Day 4 (the one for initial assessments or PT consultations)
   - In the element settings, paste your GHL calendar link or use the calendar embed widget
3. Add text above: "Book Your Free Fitness Assessment"
4. If the calendar embed is not available in the builder, add a large button: "Book Your First Session" linked to your calendar URL

**Social Links:**
1. Add: "Follow us for daily motivation and class updates:"
2. Add social media icon links (Facebook, Instagram, YouTube - placeholder URLs are fine)

**Footer:** Same as the landing page.

Save the Thank You page.

> **Pro Tip:** The Thank You page is underrated. Most people build a boring "Thanks, we'll be in touch" page and waste the moment when the prospect is MOST excited. Use it to get them to take the next action (book a session) while their motivation is high.

---

### How a Visitor Moves From Step 1 to Step 2 (Important Concept)

You have now built both pages in your funnel, but they are not yet connected. There is no automatic rule that says "Step 1 leads to Step 2." A visitor only moves from the Landing Page to the Thank You Page when ONE of two things happens:

**1. The form on Step 1 is submitted.** This is the main mechanism for lead capture funnels. Every GHL form has an "On Submit" setting (sometimes called "After Submit" or "Thank You Action") that controls what happens next. The option you want is **"Go to next step in funnel"** - this tells GHL to automatically advance the visitor to Step 2 as soon as they click submit. You will configure this setting in Exercise 8.4.

**2. A button or link is clicked.** Buttons can be configured to go to the next funnel step, an external URL, or scroll to a section on the same page (anchor link).

**For your Free Trial funnel, here is the actual flow:**
- The **hero button** at the top of the landing page scrolls DOWN to the form section (anchor link on the same page). It does NOT go to Step 2.
- The **form submission** is what takes the visitor to Step 2 (Thank You Page).

**Common student confusion:** "My hero button does not take users to Step 2!" It does not need to. The button's job is to get the visitor to the form. The form's job is to capture their info AND send them to Step 2. You are building a chain: **button → form → next step**.

**Where the setting lives:** The "Go to next step" option is NOT in the funnel settings or the page builder. It is inside the **form's own settings** (the form you built in Exercise 8.4). This trips up almost every new user - they look in the funnel settings and cannot find it.

---

### Exercise 8.3: Domain Setup

**Purpose:** Understand how custom domains work with GHL funnels so you can set this up for real clients.

Navigate to **Sites > Domains** (or Settings > Domains):

**For this course, use the GHL default subdomain.** When you created your funnel, GHL automatically assigned it a URL like `yoursubdomain.msgsndr.com/free-trial` or similar. This works perfectly for testing.

**Understanding custom domains (for reference):**

In a real business, you would connect a custom domain so the funnel URL looks like `offer.sunrisewellness.com/free-trial` instead of a generic GHL subdomain. Here is the process:

1. **Purchase a domain** (or use a subdomain of one you own) from a registrar like Namecheap, GoDaddy, or Cloudflare
2. **Add the domain in GHL** - go to Sites > Domains > Add Domain
3. **Add a CNAME DNS record** at your domain registrar:
   - Host/Name: The subdomain (e.g., `offer` for `offer.sunrisewellness.com`)
   - Points to: The GHL CNAME target (GHL will show you the exact value)
4. **Wait for DNS propagation** (usually 5-30 minutes, sometimes up to 48 hours)
5. **Assign the domain** to your funnel in the funnel settings
6. **SSL certificate** is automatically provisioned by GHL (your site will load over HTTPS)

For now, use the default GHL subdomain. Test your funnel by opening the funnel URL in an **incognito/private browser window** (this simulates a new visitor who is not logged into GHL).

---

## Part 3: Forms (45 min)

### What is a Form?

A **form** is the primary way you capture contact information from people who visit your funnels, websites, or any web page. When someone fills out a form and clicks submit, GHL automatically:

1. Creates a new contact (or updates an existing one if the email/phone matches)
2. Maps the form fields to contact record fields
3. Can trigger a workflow (which you will build on Day 9)

Forms are the bridge between "anonymous website visitor" and "contact in your CRM." Without forms, your funnel is just a pretty page that does not generate leads.

**Why spend time on form design?**

The fields you include (and exclude) directly impact two things:
- **Conversion rate:** More fields = fewer completions. Only ask for what you truly need.
- **Lead quality:** More qualifying questions = better information for follow-up.

The art is balancing these two forces. For a free trial, you want it easy (fewer fields). For a $249/month VIP membership application, you can ask more because the prospect is already committed.

---

### Exercise 8.4: Build the "Free Trial Request" Form

**Purpose:** Create the form that captures Free Trial signups on your funnel landing page. This form creates a contact record and will trigger an automated welcome sequence on Day 9.

Navigate to **Sites > Forms > + Create Form** (some GHL versions put forms under Sites, others under Forms/Surveys):

1. Click **+ Create Form**
2. **Form Name:** "Free Trial Request - Sunrise Wellness"

**Add the following fields:**

| Field Label | Field Type | Required? | Maps To | Why Include It |
|------------|-----------|-----------|---------|----------------|
| First Name | Text (Short) | Yes | `contact.first_name` | Personalization in all future communication |
| Last Name | Text (Short) | Yes | `contact.last_name` | Full name for records |
| Email | Email | Yes | `contact.email` | Primary communication channel |
| Phone | Phone | Yes | `contact.phone` | SMS follow-ups and appointment reminders |
| Fitness Goals | Multi-Select Checkbox | No | Custom Field | Helps trainers prepare; enables segmentation |
| | | | | Options: Weight Loss, Muscle Gain, Flexibility & Mobility, Endurance & Cardio, General Health & Wellness |
| Experience Level | Dropdown | No | Custom Field | Determines which classes to recommend |
| | | | | Options: Complete Beginner, Some Experience (worked out occasionally), Regular Exerciser (2-3x/week), Athlete/Advanced |
| How did you hear about us? | Dropdown | No | Custom Field | Tracks which marketing channels are working |
| | | | | Options: Google Search, Instagram, Facebook, Friend or Referral, Walked/Drove By, Other |
| Preferred Class Time | Dropdown | No | Custom Field | Helps with scheduling and class demand planning |
| | | | | Options: Early Morning (6-8 AM), Mid-Morning (8-10 AM), Midday (11 AM-1 PM), Afternoon (3-5 PM), Evening (5-8 PM) |

**Configure the form:**

1. **Field mapping:** For standard fields (First Name, Last Name, Email, Phone), GHL automatically maps them. For the custom fields (Fitness Goals, Experience Level, etc.), you will need to create corresponding **Custom Fields** in Settings > Custom Fields if you have not already, then map each form field to the matching custom field.

2. **Submit button text:** "Start My Free Trial"

3. **On-Submit action (this is what actually moves the visitor to Step 2):**
   
   Open the form settings and find the section labeled **"On Submit"**, **"After Submit"**, or **"Thank You Action"** (the label varies by GHL version - it may be a tab, an accordion, or a button in the form builder toolbar). You will see three possible options:
   
   - **"Go to next step in funnel"** (sometimes shown as "Open next step" or "Navigate to next funnel step") - **CHOOSE THIS ONE.** GHL will automatically advance the visitor to Step 2 (Thank You Page) when they submit. This option is smart: if you ever rename or rearrange your funnel steps later, the link updates automatically. You do NOT need to paste any URL.
   
   - **"Redirect to URL"** - only use this if you want submissions to go somewhere OTHER than the next step (e.g., to a different funnel or an external page). If you pick this option, paste the full public URL of your Thank You page.
   
   - **"Show a message"** / **"Open message"** - displays a text message on the same page instead of redirecting. Do NOT use this inside a funnel - it defeats the entire purpose of having a Thank You page as Step 2. Only use this for standalone forms that are not part of a funnel.
   
   > **Troubleshooting:** If you cannot find the "Go to next step" option, it usually means you are editing the form from the standalone form builder (Sites > Forms) rather than from inside the funnel. You can still select "Redirect to URL" and paste your Thank You page URL - the result is the same, just less elegant. Or, you can save the form, embed it into the funnel step (Exercise 8.5), and then edit the on-submit setting from within the funnel context, which will show the "Go to next step" option.

4. **Form styling:**
   - Match the colors to your Sunrise Wellness brand
   - Make the submit button large and high-contrast
   - Ensure adequate spacing between fields (cramped forms feel overwhelming)

5. **Save** the form

> **Pro Tip:** Notice we made the qualifying fields (Fitness Goals, Experience Level, etc.) optional while keeping contact fields required. This is intentional. If someone is in a hurry, they can submit with just name/email/phone and you still get the lead. The extra info is a bonus, not a barrier.

---

### Exercise 8.5: Embed the Form in Your Funnel

**Purpose:** Connect your form to the funnel landing page so visitors can actually sign up.

1. Go back to **Sites > Funnels** and open your "Sunrise Wellness - Free Trial" funnel
2. Open the **Landing Page** (Step 1) in the page builder
3. Scroll to the Form Section you created in Exercise 8.2
4. If you placed a temporary placeholder, delete it
5. Drag a **Form** element into the section (or click the form placeholder to configure it)
6. Select your "Free Trial Request - Sunrise Wellness" form
7. The form fields should appear on the page
8. **Verify the form's on-submit action points to Step 2** (this is the transition wiring):
   - Click on the embedded form element to open its settings panel (it may appear on the right side or in a popup)
   - Look for the **"On Submit"** / **"After Submit"** / **"Thank You Action"** setting
   - Confirm it is set to **"Go to next step in funnel"** (or "Redirect to URL" with your Thank You page URL pasted in)
   - If it is set to "Show a message," change it now - otherwise the visitor will never reach Step 2
9. Adjust styling to match the page design:
   - Field label colors
   - Input field border style
   - Button color and size
   - Spacing and alignment
10. **Preview** the page and make sure the form looks good on both desktop and mobile
11. **Save** the funnel page

**Test the complete flow:**
1. Open your funnel URL in an **incognito/private browser window**
2. Fill out the form with test data (use a real email you can check):
   - First Name: Test
   - Last Name: Member
   - Email: your test email
   - Phone: your phone number
   - Select some fitness goals and an experience level
3. Click "Start My Free Trial"
4. Verify you are redirected to the Thank You page
5. Go back to GHL and check:
   - Does a new contact appear in **Contacts** with the name "Test Member"?
   - Are the custom fields (Fitness Goals, Experience Level) populated on the contact record?
   - Did the contact get the correct tags (if any were configured)?

If the contact was created with all the correct data, your funnel-to-CRM pipeline is working.

---

### Exercise 8.6: Preview the Form-to-Workflow Connection

**Purpose:** Understand how form submissions will trigger automated follow-up. You will build the full workflow on Day 9, but let us set up the trigger now so you understand the connection.

Navigate to **Automation > Workflows > + Create Workflow**:

1. Name the workflow: "Free Trial - New Signup"
2. **Set the trigger:** 
   - Trigger type: "Form Submitted"
   - Select form: "Free Trial Request - Sunrise Wellness"
3. Add a few placeholder steps (you will flesh these out on Day 9):
   - **Add Tag:** `new-trial-member`
   - **Send Email:** Select your "Sunrise Welcome Email" template from Day 7
   - **Create Opportunity:** Add to your Sunrise Wellness pipeline (from Day 5) at the "New Lead" stage with a value of $79 (Basic membership as the initial target)
   - **Internal Notification:** Send an email to yourself: "New trial signup: {{contact.first_name}} {{contact.last_name}} - {{contact.email}}"
4. **Save** the workflow (keep it in Draft mode - you will activate it on Day 9)

This preview shows you the power of connecting everything: a stranger visits your funnel (Day 8) > fills out a form (Day 8) > gets a welcome email (Day 7 template) > becomes a pipeline opportunity (Day 5) > all automatically (Day 9).

> **Pro Tip:** Notice we added the tag `new-trial-member` as the first step. Tags are the thread that connects everything in GHL. On Day 9 you will build more sophisticated workflows that branch based on tags, but this simple tagging step is the foundation.

---

## Part 4: Surveys with Conditional Logic (45 min)

### What is a Survey?

A **survey** in GHL is like a form's more sophisticated sibling. While a form is typically a single page with a set list of fields, a survey can:

- **Span multiple pages** (multi-step experience)
- **Use conditional logic** (show different questions based on previous answers)
- **Branch into different paths** (personalized experience for each respondent)
- **Collect more detailed information** without feeling overwhelming (because it is broken into steps)

Think of it as a "choose your own adventure" form. If someone says they are interested in weight loss, they see weight loss questions. If they say muscle building, they see completely different questions. This means you collect relevant, specific information instead of forcing everyone through the same generic fields.

### Why Use Surveys Instead of (or In Addition to) Forms?

- **Forms** are for quick capture: name, email, phone - get the lead fast
- **Surveys** are for deep qualification: understand needs, goals, budget, timeline

For Sunrise Wellness, the funnel form (Exercise 8.4) captures the lead quickly. The survey (this exercise) digs deeper to help trainers prepare the perfect first session. You might send the survey link in the welcome email or have new members fill it out on an iPad when they arrive.

---

### Exercise 8.7: Build the "Member Needs Assessment" Survey

**Purpose:** Create a multi-page survey with conditional logic that gathers detailed information about each new member's goals, experience, and needs. This information helps trainers personalize the experience and helps you recommend the right membership tier.

Navigate to **Sites > Forms/Surveys** (or wherever surveys live in your GHL version) > **+ Create Survey**:

**Survey Name:** "Sunrise Wellness - Member Needs Assessment"

---

**Page 1: Basic Information** (everyone sees this)

Add these fields:

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Last Name | Text | Yes |
| Email | Email | Yes |
| Phone | Phone | Yes |
| **"What is your primary fitness goal?"** | Single Select (Radio Buttons) | Yes |
| | Options: | |
| | - Weight Loss | |
| | - Muscle Building | |
| | - Flexibility & Recovery | |
| | - Sports Performance | |
| | - General Wellness | |

The last question is the **branching question** - the answer determines which Page 2 the respondent sees.

---

**Page 2: Goal-Specific Questions** (conditional - different questions based on Page 1 answer)

Set up **conditional logic** so each version of Page 2 only appears for the matching answer:

**IF "Weight Loss" was selected:**

| Field | Type |
|-------|------|
| "What is your current activity level?" | Dropdown: Sedentary (little to no exercise), Lightly Active (1-2x/week), Moderately Active (3-4x/week), Very Active (5+/week) |
| "Any dietary restrictions or preferences?" | Multi-Select: None, Vegetarian, Vegan, Gluten-Free, Dairy-Free, Keto, Other |
| "What is your target timeline?" | Dropdown: 1-3 months, 3-6 months, 6-12 months, No specific timeline |
| "Have you worked with a trainer or nutritionist before?" | Radio: Yes / No |

**IF "Muscle Building" was selected:**

| Field | Type |
|-------|------|
| "How long have you been strength training?" | Dropdown: Never, Less than 6 months, 6 months - 2 years, 2+ years |
| "Do you have access to equipment at home?" | Radio: Yes (home gym), Some basics (dumbbells, bands), No - studio only |
| "Any competition or specific physique goals?" | Dropdown: General muscle gain, Bodybuilding competition, Strength/Powerlifting, Athletic performance, Just want to look and feel stronger |
| "Any current injuries or limitations?" | Text (optional) |

**IF "Flexibility & Recovery" was selected:**

| Field | Type |
|-------|------|
| "Any current injuries or chronic pain?" | Text (describe) |
| "Have you practiced yoga or Pilates before?" | Dropdown: Never, A few times, Regularly (1-2x/week), Experienced practitioner |
| "Any specific mobility concerns?" | Multi-Select: Lower back, Shoulders, Hips, Knees, Neck, Hamstrings, General stiffness |
| "Are you recovering from a surgery or injury?" | Radio: Yes / No / Prefer not to say |

**IF "Sports Performance" was selected:**

| Field | Type |
|-------|------|
| "What sport(s) do you play?" | Text |
| "What level do you compete at?" | Dropdown: Recreational, Club/League, College, Semi-Pro/Pro |
| "What performance areas do you want to improve?" | Multi-Select: Speed, Power, Endurance, Agility, Injury prevention, Sport-specific skills |
| "Do you have a coach or training program already?" | Radio: Yes / No |

**IF "General Wellness" was selected:**

| Field | Type |
|-------|------|
| "What does 'wellness' mean to you?" | Multi-Select: More energy, Better sleep, Stress relief, Improved mood, Healthy aging, Social connection |
| "How often would you like to work out?" | Dropdown: 1-2x/week, 3-4x/week, 5+/week, Not sure yet |
| "Any health conditions we should be aware of?" | Text (optional) |
| "Are you interested in nutrition coaching as well?" | Radio: Yes / Maybe later / No |

**Setting up the conditional logic:**
1. In the survey builder, look for a **"Logic"** or **"Conditional"** setting on Page 2
2. Set the condition: "Show this page IF [Primary Fitness Goal] = [specific answer]"
3. You will need to create separate Page 2 variants OR use field-level conditional logic depending on your GHL version
4. Some GHL versions handle this through "question logic" (show/hide individual fields) rather than "page logic" (show/hide entire pages). Either approach works.

> **Pro Tip:** If your GHL version does not support page-level branching, you can achieve a similar result with field-level conditional logic: put ALL the questions on one Page 2, but set each group to only show when the matching goal was selected on Page 1. The respondent only sees the relevant questions either way.

---

**Page 3: Preferences & Budget** (everyone sees this regardless of their path)

| Field | Type |
|-------|------|
| "What membership level interests you?" | Dropdown: Free Trial (just exploring), Basic ($79/mo - 3 classes/week), Premium ($149/mo - unlimited classes + 1 PT session), VIP ($249/mo - unlimited everything + weekly PT + nutrition) |
| "What times work best for you?" | Multi-Select: Early Morning (6-8 AM), Mid-Morning (8-10 AM), Midday (11-1 PM), Afternoon (3-5 PM), Evening (5-8 PM), Weekends |
| "Is there anything else you would like us to know?" | Textarea (optional) |

**Survey completion settings:**
- Thank you message: "Thank you, {{contact.first_name}}! Your trainer will review your assessment before your first session so we can hit the ground running. See you at the studio!"
- Redirect (optional): Back to your calendar booking page

Save the survey.

**Test your survey:**
1. Copy the survey link (GHL generates a shareable URL)
2. Open it in an incognito window
3. Fill it out selecting "Weight Loss" as the goal - verify you see the weight loss questions on Page 2
4. Go back and fill it out again selecting "Muscle Building" - verify you see different questions
5. Check that the contact was created in GHL with the survey responses mapped to fields

---

### Exercise 8.8: Survey Workflow Trigger

**Purpose:** Set up automation so that when someone completes the survey, they are automatically tagged based on their fitness goal and assigned to the right follow-up path.

Navigate to **Automation > Workflows > + Create Workflow**:

1. **Workflow Name:** "Needs Assessment - Auto-Tag"
2. **Trigger:** Survey Submitted > "Sunrise Wellness - Member Needs Assessment"
3. **Add an If/Else branch** based on the "Primary Fitness Goal" answer:

   **Branch 1: Weight Loss**
   - Add tag: `goal-weight-loss`
   - Add tag: `recommend-nutrition-coaching`
   - (In a real setup, you might also notify the nutrition coaching team)

   **Branch 2: Muscle Building**
   - Add tag: `goal-muscle-building`
   - Add tag: `recommend-personal-training`

   **Branch 3: Flexibility & Recovery**
   - Add tag: `goal-flexibility`
   - Add tag: `recommend-yoga-pilates`

   **Branch 4: Sports Performance**
   - Add tag: `goal-sports-performance`
   - Add tag: `recommend-personal-training`

   **Branch 5: General Wellness**
   - Add tag: `goal-general-wellness`

4. **After all branches converge**, add:
   - Internal notification to the appropriate trainer/coach
   - (Optional) Send the member a follow-up email: "We have reviewed your assessment and are preparing a personalized plan for you."

5. **Save** the workflow (keep in Draft mode - activate on Day 9)

This workflow means that when a new member fills out the survey, they are automatically categorized. You can then build Smart Lists (like on Day 2) based on these tags - for example, all members tagged `recommend-nutrition-coaching` could receive targeted nutrition content.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental

**Situation:** BrightSmile Dental (2 dentists, general and cosmetic procedures from $150 cleanings to $3,000 cosmetic work) needs a "Free Dental Exam" funnel to attract new patients, plus an intake form that collects essential medical and dental history, and a survey that routes patients to the right dentist based on their needs.

**Your Task:**

**Build a 2-Step "Free Dental Exam" Funnel:**

*Landing Page:*
- Hero: "Your First Dental Exam is On Us - New Patients Only"
- Benefits section: "Gentle, Modern Care" / "Two Experienced Dentists" / "Family-Friendly Office"
- Patient intake form (see below)
- Social proof: "Serving 2,000+ happy patients since [year]"
- FAQ: "Does it really cost nothing?", "What does the exam include?", "Do you accept my insurance?"
- Footer with office hours and address

*Thank You Page:*
- "Welcome to the BrightSmile Family, {{contact.first_name}}!"
- What to bring to your first appointment (ID, insurance card, list of medications)
- Calendar embed to book the exam appointment
- Map/directions to the office

**Build the Patient Intake Form:**

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Last Name | Text | Yes |
| Email | Email | Yes |
| Phone | Phone | Yes |
| Date of Birth | Date | Yes |
| Insurance Provider | Dropdown: Aetna, Blue Cross Blue Shield, Cigna, Delta Dental, MetLife, United Healthcare, No Insurance, Other | No |
| When was your last dental visit? | Dropdown: Within 6 months, 6-12 months ago, 1-2 years ago, 2+ years ago, I cannot remember | No |
| Any current dental concerns? | Textarea | No |
| Medical conditions we should know about? | Textarea ("e.g., diabetes, heart conditions, medications, allergies") | No |

Embed this form in the funnel landing page.

**Build a "Patient Needs" Survey with Conditional Logic:**

*Page 1:* Contact info + "What brings you in today?" (Radio: General Checkup & Cleaning, Cosmetic Improvement, Pain or Emergency, Orthodontics/Alignment)

*Page 2 (conditional):*
- IF General Checkup: "How often do you floss?", "Any sensitivity to hot or cold?", "Interested in whitening?"
- IF Cosmetic: "What would you like to improve?" (multi-select: Whitening, Veneers, Bonding, Gum Reshaping), "Budget range for cosmetic work?" (dropdown: Under $500, $500-$1,500, $1,500-$3,000, Flexible)
- IF Pain/Emergency: "Where is the pain?" (diagram or dropdown), "How long has this been going on?", "Rate the pain 1-10", "Are you currently taking anything for it?"
- IF Orthodontics: "Who is the patient?" (Me, My child), "Have you had braces before?", "Main concern?" (Crowding, Spacing, Bite alignment, Appearance)

*Page 3 (all paths):* "Preferred appointment times?", "How did you hear about BrightSmile?", "Anything else?"

Set up a workflow trigger that tags patients based on their needs (e.g., `needs-cosmetic`, `needs-orthodontics`) and creates an opportunity in a dental pipeline.

---

### Case Scenario 2: Elevate Digital Agency

**Situation:** Elevate Digital Agency (SEO, PPC, Social Media Management, Email Marketing, Web Design, retainers from $2,000-$10,000/month) needs a "Free Strategy Session" funnel to capture qualified business leads, a client intake form, and a needs assessment survey that routes prospects to the right service team.

**Your Task:**

**Build a 2-Step "Free Strategy Session" Funnel:**

*Landing Page:*
- Hero: "Get a Free Digital Marketing Strategy Session - See Exactly Where You are Leaving Money on the Table"
- Results section with placeholder metrics: "Average client sees 3.2x ROI in 90 days"
- 3 benefit columns: "Custom Strategy (not a cookie-cutter template)" / "Data-Driven Insights (we audit your current performance)" / "No Obligation (walk away with actionable ideas either way)"
- Intake form (see below)
- Case study snippet: placeholder client success story
- Footer with agency info

*Thank You Page:*
- "Great Move, {{contact.first_name}}. Your Strategy Session is Almost Ready."
- "Before our call, we will audit your website and current marketing. Here is what to prepare..."
- Calendar embed to book the strategy session
- "While you wait:" links to agency blog posts or case studies

**Build the Client Intake Form:**

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Last Name | Text | Yes |
| Email | Email | Yes |
| Phone | Phone | Yes |
| Business Name | Text | Yes |
| Website URL | URL/Text | No |
| Industry | Dropdown: E-commerce, SaaS, Professional Services, Healthcare, Real Estate, Hospitality, Manufacturing, Nonprofit, Other | No |
| Monthly Revenue Range | Dropdown: Pre-revenue/Startup, Under $10K, $10K-$50K, $50K-$200K, $200K-$1M, $1M+ | No |
| Current Marketing Channels | Multi-Select: SEO, Google Ads (PPC), Facebook/Instagram Ads, Social Media (organic), Email Marketing, Content Marketing, None yet | No |

**Build a "Marketing Needs Assessment" Survey with Conditional Logic:**

*Page 1:* Business info + "What is your PRIMARY marketing goal?" (Radio: More Website Traffic, More Leads/Sales, Better Brand Awareness, Improve Existing Campaigns, Full Marketing Overhaul)

*Page 2 (conditional):*
- IF More Traffic: "Current monthly website visitors?", "Do you have a blog/content strategy?", "Have you done any SEO work before?", "Top 3 keywords you want to rank for?" (text)
- IF More Leads/Sales: "Current cost per lead?", "Monthly ad spend?" (dropdown ranges), "Which platforms are you advertising on?", "What is your target cost per lead?"
- IF Brand Awareness: "Target audience description" (textarea), "Which social platforms matter most?" (multi-select), "Current social following size?" (dropdown ranges), "Content creation capacity?" (dropdown)
- IF Improve Existing: "What is working?" (textarea), "What is not working?" (textarea), "Current monthly marketing spend?", "Who manages marketing now?" (In-house, Freelancer, Another agency, Nobody)
- IF Full Overhaul: "Why are you looking for a change?" (textarea), "Biggest marketing frustration?", "How soon do you need results?", "Budget range for full-service?" (dropdown: $2K-$5K/mo, $5K-$10K/mo, $10K+/mo)

*Page 3 (all paths):* "Decision timeline?" (Dropdown: ASAP, 1-2 weeks, 1 month, Just researching), "Who else is involved in this decision?", "What would make this engagement a success for you?" (textarea)

Set up a workflow trigger that tags prospects based on their goal (e.g., `goal-more-traffic` maps to the SEO team, `goal-more-leads` maps to the PPC team) and creates a pipeline opportunity with estimated value based on the budget range answer.

---

## Day 8 Recap

**What You Built Today:**
- A 2-step lead capture funnel for Sunrise Wellness Studio (Landing Page + Thank You Page)
- A "Free Trial Request" form with qualifying custom fields
- Embedded the form in your funnel and tested the complete flow
- A "Member Needs Assessment" survey with conditional logic branching by fitness goal
- Workflow triggers for both form and survey (ready to activate on Day 9)

**Key Concepts to Remember:**
1. **Funnels** are focused (one goal, no distractions); **Websites** are comprehensive (many pages, full navigation)
2. **Forms** capture leads quickly; **Surveys** qualify leads deeply with branching logic
3. Every form field should map to a contact field in GHL - this is how visitor data becomes CRM data
4. The Thank You page is a conversion opportunity, not an afterthought - use it to get the next action
5. Form submissions and survey completions can trigger workflows that automate your entire follow-up process
6. Always test in an incognito window to see what a real visitor experiences

**Recap Questions:**
1. When would you choose a Funnel over a Website for a client, and why?
2. What is the trade-off between having more form fields vs fewer form fields?
3. How does conditional logic in surveys improve the data you collect?
4. What happens in GHL when someone submits a form - what is automatically created?
5. How do you connect a form submission to a workflow so follow-up happens automatically?
6. Why should you test your funnel in an incognito browser window instead of the preview mode?

---

## Next Day Preview

**Day 9: Automation & Workflows** - The most powerful feature in GHL. Tomorrow you will activate the workflow triggers you previewed today and build complete automated sequences: welcome series, appointment reminders, lead nurture drips, and missed-call follow-ups. Everything you have built over the last 8 days comes together into hands-free automation.

**Before Day 9, make sure you have:**
- At least 5 contacts with varied data (from Day 2) - you need real contacts for workflows to act on
- Your funnel form and survey from today (you will activate their workflow triggers)
- Your email templates from Day 3 and Day 7 (workflows will send these automatically)
- Your pipeline from Day 5 (workflows will create and move opportunities)
- Your calendar from Day 4 (workflows will reference booking links)
