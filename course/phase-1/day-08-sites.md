# Day 8: Sites - Funnels & Websites

**Time Required:** 3-4 hours
**Certification Alignment:** Funnel vs Website Builder, Domain Setup, Page Builder, Forms, Surveys (with conditional logic), Workflow Triggers from Forms/Surveys
**API Lab:** No dedicated API lab (Sites are primarily visual; API work integrates via forms + workflows)

---

## Learning Objectives

1. Understand when to use a Funnel vs a Website
2. Build a multi-step funnel with landing pages and thank-you pages
3. Create forms and surveys with custom fields and conditional logic
4. Connect forms and surveys to workflows for automated follow-up

---

## Part 1: Funnel vs Website (20 min)

### Theory Recap

| Feature | Funnel | Website |
|---------|--------|---------|
| **Purpose** | Specific goal (lead capture, sales, booking) | General business presence |
| **Structure** | Linear steps (Page 1 > Page 2 > ...) | Multi-page with navigation menu |
| **Navigation** | No menu bar, minimal distractions | Full navigation, multiple pages |
| **SEO** | Limited SEO focus | Full SEO capabilities |
| **Use Case** | Ad campaigns, launch pages, opt-ins | Company website, blog, resource center |

### When to use what:
- **Funnel:** When you have ONE clear goal (get the lead, make the sale, book the call)
- **Website:** When you need a full business presence with multiple sections

### Hands-On Exercise 8.1: Explore Both Builders

Navigate to **Sites**:

1. Click **Funnels** - note the interface and options
2. Click **Websites** - compare with funnels
3. Open an existing template (if available) for each
4. Note the differences in layout, navigation options, and structure

---

## Part 2: Build a Lead Capture Funnel (60 min)

### Hands-On Exercise 8.2: Create a 2-Step Funnel

Navigate to **Sites > Funnels > + Create Funnel**:

**Funnel Name:** "Free Consultation Funnel"

**Step 1: Landing Page**

Build this layout:
```
[HERO SECTION]
  - Headline: "Get Your Free 30-Minute Strategy Consultation"
  - Subheadline: "Discover how we can help grow your business"
  - Background: Gradient or high-quality image

[BENEFITS SECTION - 3 columns]
  - Column 1: Icon + "Personalized Strategy"
  - Column 2: Icon + "Expert Guidance"
  - Column 3: Icon + "Proven Results"

[FORM SECTION]
  - Headline: "Claim Your Free Consultation"
  - Form (built in Exercise 8.4)
  - Submit button: "Get My Free Consultation"

[SOCIAL PROOF]
  - 3 testimonials with photos
  - Star ratings
  - "Trusted by 500+ businesses"

[FAQ SECTION]
  - 4-5 common questions with answers
  - Accordion style if available

[FOOTER]
  - Business info
  - Privacy policy link
  - Terms of service link
```

**Build steps:**
1. Choose a blank template or starter
2. Add sections using the page builder
3. Add elements: Text, Image, Button, Form, Columns
4. Style each element (fonts, colors, spacing)
5. Set the page URL path (e.g., /free-consultation)
6. Preview on Desktop, Tablet, and Mobile

**Step 2: Thank You Page**

```
[CONFIRMATION]
  - Headline: "You're All Set, {{contact.first_name}}!"
  - Subtext: "We'll be in touch within 24 hours to schedule your consultation."

[NEXT STEPS]
  - "While you wait, here are some resources:"
  - Link to blog/resources
  - Social media follow buttons

[CALENDAR EMBED]
  - Optionally embed your calendar widget
  - "Or skip the wait - book your slot now!"
```

### Hands-On Exercise 8.3: Set Up a Custom Domain

Navigate to **Sites > Domains** (or Settings > Domains):

1. Add a custom domain or subdomain
2. Follow the DNS setup instructions:
   - Add CNAME record pointing to GHL
   - Wait for DNS propagation (can take 5-60 minutes)
3. Assign the domain to your funnel
4. Test: Visit your custom domain and verify the funnel loads
5. Enable SSL (should be automatic)

**If you don't have a domain:** Use the default GHL subdomain for practice.

---

## Part 3: Forms (45 min)

### Theory Recap

Forms are the primary way to capture lead information in GHL. Forms can be:
- Embedded in funnels/websites
- Standalone (shared via link)
- Triggered to fire workflows on submission

### Hands-On Exercise 8.4: Build a Lead Capture Form

Navigate to **Sites > Forms > + Create Form**:

**Form Name:** "Free Consultation Request"

**Fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First Name | Text | Yes | Standard field |
| Last Name | Text | Yes | Standard field |
| Email | Email | Yes | Standard field |
| Phone | Phone | Yes | Standard field |
| Company Name | Text | No | Maps to Company custom field |
| Service Interest | Dropdown | Yes | Options: Marketing, Sales, Operations, Other |
| Budget Range | Dropdown | No | Options: <$1K, $1K-$5K, $5K-$10K, $10K+ |
| How did you hear about us? | Dropdown | No | Options: Google, Social Media, Referral, Other |
| Message | Textarea | No | "Tell us about your needs" |

**Configure:**
1. Set each field as required or optional
2. Map fields to GHL contact fields (standard + custom)
3. Set the submit button text: "Request My Free Consultation"
4. Set the success message: "Thank you! We'll contact you within 24 hours."
5. Style the form (colors, font, button style)

### Hands-On Exercise 8.5: Embed the Form in Your Funnel

1. Go back to your "Free Consultation Funnel" landing page
2. Find the form section you created
3. Add a Form element and select your "Free Consultation Request" form
4. Adjust the form styling to match the funnel page
5. Preview and test:
   - Fill out the form with test data
   - Submit
   - Verify the contact is created in Contacts
   - Verify custom fields are populated
   - Check that you're redirected to the Thank You page

### Hands-On Exercise 8.6: Form Workflow Trigger

Navigate to **Automation > Workflows > + Create Workflow**:

Create a workflow triggered by form submission:

**Trigger:** Form Submitted > "Free Consultation Request"

**Steps:**
1. **Wait 1 minute** (gives time for contact record to populate)
2. **Send SMS:** "Hi {{contact.first_name}}, thanks for requesting a consultation with {{business.name}}! We'll be in touch within 24 hours. Reply to this text if you have any immediate questions."
3. **Send Email:** Use your "Welcome Email" template
4. **Internal notification:** Send email to admin: "New consultation request from {{contact.first_name}} {{contact.last_name}} - {{contact.email}}"
5. **Add tag:** "consultation-requested"
6. **Create opportunity:** Add to Sales Pipeline > "New Lead" stage

Save and activate the workflow. Test by submitting the form again.

---

## Part 4: Surveys with Conditional Logic (45 min)

### Theory Recap

Surveys differ from forms in that they:
- Can span multiple pages/steps
- Support **conditional logic** (branching based on answers)
- Are great for qualifying leads or gathering detailed information
- Can be longer and more detailed than a simple form

### Hands-On Exercise 8.7: Build a Survey with Conditional Logic

Navigate to **Sites > Forms/Surveys > + Create Survey**:

**Survey Name:** "Client Needs Assessment"

**Page 1: Basic Info**
- Name (text, required)
- Email (email, required)
- Phone (phone, required)
- "What best describes your business?" (Dropdown: Service-Based, Product-Based, SaaS, Non-Profit, Other)

**Page 2: Service Interest (Conditional)**

IF "Service-Based" was selected:
- "What services do you offer?" (Multi-select)
- "How many clients do you serve monthly?" (Dropdown: 1-10, 11-50, 51-100, 100+)
- "What's your biggest challenge?" (Textarea)

IF "Product-Based" was selected:
- "What products do you sell?" (Textarea)
- "Average order value?" (Dropdown: <$50, $50-200, $200-500, $500+)
- "Where do you sell? (Multi-select: Online, Retail, Wholesale, Marketplace)

IF "SaaS" was selected:
- "Monthly recurring revenue?" (Dropdown: Pre-revenue, <$10K, $10K-$50K, $50K+)
- "Number of active users?" (Number)
- "Tech stack?" (Textarea)

**Page 3: Budget & Timeline (All paths)**
- "What's your marketing budget?" (Dropdown: <$1K/mo, $1K-$5K/mo, $5K-$10K/mo, $10K+/mo)
- "When do you want to start?" (Dropdown: Immediately, 1-2 Weeks, 1 Month, Just Researching)
- "Anything else we should know?" (Textarea)

**Configure Conditional Logic:**
1. On Page 1, set the branching based on "business type" answer
2. Set which Page 2 variant shows based on the selection
3. Ensure Page 3 shows for everyone regardless of path
4. Set a thank-you message on completion

### Hands-On Exercise 8.8: Survey Workflow Trigger

Create a workflow triggered by survey completion:

**Trigger:** Survey Submitted > "Client Needs Assessment"

**Steps:**
1. **Tag based on business type:** If/Else branch
   - If Service-Based → add tag "biz-service"
   - If Product-Based → add tag "biz-product"
   - If SaaS → add tag "biz-saas"
2. **Tag based on budget:**
   - If $5K+/mo → add tag "high-budget", create opportunity with $5000 value
   - If $1K-$5K → add tag "mid-budget", create opportunity with $2500 value
   - If <$1K → add tag "low-budget", create opportunity with $500 value
3. **Send personalized follow-up** based on tags
4. **Notify sales team** with survey summary

---

## Case Scenarios

### Case Scenario 1: Dentist Lead Generation Funnel

**Situation:** A dental clinic wants a "Free Whitening Consultation" funnel for their Facebook ad campaign.

**Your Task:**
1. Build a 2-step funnel:
   - **Landing Page:** Compelling headline, benefits of whitening, before/after photos, form
   - **Thank You Page:** Confirmation, what to expect, calendar embed for booking
2. Form fields: Name, Phone, Email, "Have you had teeth whitening before?" (Yes/No), "What's your biggest concern about whitening?" (Dropdown)
3. Workflow: Form submission → SMS confirmation → Email with whitening info → Tag "whitening-interest" → Create opportunity in pipeline
4. Mobile-optimize the entire funnel (most FB ad clicks are mobile)

### Case Scenario 2: Client Intake Survey

**Situation:** A marketing agency needs a detailed client intake survey with conditional logic for different service needs.

**Your Task:**
1. Build a multi-page survey:
   - Page 1: Contact info + business overview
   - Page 2: Service interest (conditional branches for SEO, PPC, Social Media, Email Marketing)
   - Page 3: Budget + timeline + competitor info
   - Page 4: Goals and success metrics
2. Each service branch should ask different qualifying questions
3. On submission:
   - Route to the correct team member based on service interest
   - Create an opportunity with estimated value based on budget answer
   - Send a "thank you + next steps" email
4. The survey should work embedded on their website AND as a standalone link

### Case Scenario 3: Complete Lead Gen System

**Situation:** Build a complete lead generation system that combines everything from this lesson.

**Your Task:**
1. Landing page funnel with form (from Facebook ads)
2. Survey for detailed qualification (sent after initial contact)
3. Workflow that:
   - Captures the lead from the funnel form
   - Sends an immediate SMS + email
   - Creates a pipeline opportunity
   - After 2 hours, sends the detailed survey link
   - When survey is completed, updates the opportunity with details
   - Notifies the assigned sales rep
4. Test the entire flow end-to-end

---

## Day 8 Recap Questions

1. When would you choose a Funnel over a Website, and vice versa?
2. What DNS record type do you need to connect a custom domain to GHL?
3. How do you map form fields to custom fields in GHL contacts?
4. Explain conditional logic in surveys - how do you create branching paths?
5. How do you trigger a workflow when a form is submitted?
6. What's the difference between a Form and a Survey in GHL?

---

## Next Day Preview

**Day 9: Automation & Workflows** - The most powerful feature in GHL. You'll build complete automated sequences, implement workflow recipes, and create complex conditional automation.

Make sure you have:
- At least 5 contacts with varied data (from Day 2)
- Your form and survey from today (we'll trigger workflows from them)
- Templates from Day 3 (we'll use them in workflows)
