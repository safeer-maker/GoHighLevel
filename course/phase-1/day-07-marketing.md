# Day 7: Marketing - Email Campaigns & Social

**Time Required:** 3-4 hours
**Certification Alignment:** Email Builder, Email Campaigns, Trigger Links, Affiliate Manager, Social Planner
**API Lab:** Yes - `scripts/day-07-marketing-api.py`

---

## Learning Objectives

1. Build professional email templates using the drag-and-drop builder
2. Launch targeted email campaigns to Smart Lists
3. Set up and use Trigger Links for behavioral tracking
4. Understand email compliance and deliverability best practices

---

## Part 1: Email Template Builder (60 min)

### Theory Recap

GHL's Email Builder is a drag-and-drop visual editor for creating HTML emails. Templates can include:
- Dynamic merge fields (contact data, custom values)
- Images, buttons, and layout blocks
- Trigger links for tracking
- Unsubscribe links (required by law)

### Hands-On Exercise 7.1: Build a Welcome Email Template

Navigate to **Marketing > Emails > Templates** (or Email Builder):

Click **+ Create Template** and build:

**Template: "Welcome Series - Email 1"**

Structure:
```
[HEADER]
  - Business logo (centered)
  - Background color: brand color

[HERO SECTION]
  - Headline: "Welcome to {{business.name}}, {{contact.first_name}}!"
  - Subtext: "We're thrilled to have you join us."
  - Hero image (relevant stock photo or brand image)

[BODY - 2 COLUMN]
  Left: "What to Expect"
  - Bullet points: 3-4 benefits
  Right: Image of team/product

[CTA SECTION]
  - Button: "Book Your First Session" (link to calendar)
  - Button color: contrasting/accent color

[SOCIAL PROOF]
  - Testimonial quote
  - Star rating image

[FOOTER]
  - Business name, address, phone
  - Social media icons (linked)
  - Unsubscribe link (REQUIRED)
  - "You're receiving this because you signed up at {{business.website}}"
```

**Build steps:**
1. Choose a blank template or start from a pre-built one
2. Drag sections: Image, Text, Button, Divider, Columns
3. Add merge fields by typing `{{` in text blocks
4. Style each element (fonts, colors, spacing, padding)
5. Preview on both **Desktop** and **Mobile** views
6. Save the template

### Hands-On Exercise 7.2: Build a Promotional Email

**Template: "Monthly Special Offer"**

```
[HEADER with logo]

[HERO]
  - Large text: "{{offer.discount}}"
  - Subtitle: "For a Limited Time Only"
  - Eye-catching background image/color

[OFFER DETAILS]
  - What's included
  - Regular price vs. discounted price
  - Expiry: "Offer ends [DATE]"

[CTA]
  - Button: "Claim Your Offer Now"
  - Urgency text: "Only [X] spots remaining!"

[FAQ]
  - 2-3 common questions about the offer

[FOOTER]
  - Unsubscribe link
  - Terms and conditions link
```

### Hands-On Exercise 7.3: Build a Newsletter Template

**Template: "Monthly Newsletter"**

```
[HEADER]
  - Logo + "Monthly Newsletter - {{current_month}}"

[FEATURED ARTICLE]
  - Image + headline + 2-line preview + "Read More" link

[3-COLUMN CONTENT]
  - Tip of the Month | Upcoming Events | Product Spotlight

[SPECIAL SECTION]
  - Seasonal offer or announcement

[COMMUNITY]
  - Social media highlights
  - Customer spotlight

[FOOTER]
  - Full business info
  - "Update your preferences" link
  - Unsubscribe link
```

---

## Part 2: Email Campaigns (45 min)

### Theory Recap

An **Email Campaign** sends a single email (or email series) to a specific audience (Smart List or tag-based group). Unlike workflow-triggered emails, campaigns are manually launched at a specific time.

### Hands-On Exercise 7.4: Create and Launch a Campaign

Navigate to **Marketing > Emails > Campaigns** (or Email Campaigns):

1. Click **+ Create Campaign**
2. **Campaign name:** "Welcome Campaign - March 2024"
3. **Select audience:**
   - Choose a Smart List you created on Day 2 (e.g., "Hot Leads")
   - OR select contacts by tag (e.g., "csv-import-day2")
4. **Select template:** Use your "Welcome Series - Email 1" template
5. **Configure sender:**
   - From name: Your business name
   - From email: Your configured email
   - Reply-to: Your reply email
6. **Subject line:** "Welcome to {{business.name}}, {{contact.first_name}}!"
   - Preview text: "Here's what you can expect from us..."
7. **Schedule:**
   - Send immediately OR
   - Schedule for a specific date/time
8. **Review:**
   - Check recipient count
   - Preview the email one more time
   - Send a test email to yourself
9. **Launch** the campaign

### Hands-On Exercise 7.5: Monitor Campaign Performance

After sending (or after a test send):

1. Go to the campaign dashboard
2. Review metrics:
   - **Sent:** Number of emails sent
   - **Delivered:** Successfully delivered (sent - bounces)
   - **Open rate:** Percentage who opened
   - **Click rate:** Percentage who clicked a link
   - **Bounce rate:** Hard bounces + soft bounces
   - **Unsubscribe rate:** Percentage who unsubscribed
3. Click into individual contact activity:
   - Who opened?
   - Who clicked?
   - Which links got the most clicks?

### Email Compliance Checklist

Before any campaign, verify:
- [ ] Unsubscribe link is present and working
- [ ] Physical business address is in the footer (CAN-SPAM requirement)
- [ ] From address is authenticated (SPF, DKIM, DMARC)
- [ ] Contact list is opt-in (no purchased lists)
- [ ] Subject line is not misleading
- [ ] Content matches the subject line

---

## Part 3: Trigger Links (45 min)

### Theory Recap

**Trigger Links** are special tracked URLs that, when clicked, can:
1. Track which contacts clicked
2. Trigger a workflow/automation
3. Add/remove tags on the contact
4. Move contacts to a pipeline stage
5. Subscribe/unsubscribe from lists

They're powerful for behavioral segmentation - knowing what a contact is interested in based on what they click.

### Hands-On Exercise 7.6: Create Trigger Links

Navigate to **Marketing > Trigger Links** (or Settings > Trigger Links):

Create these trigger links:

**Trigger Link 1: "Interested in Premium"**
- Name: interested-premium
- Redirect URL: Your website pricing page
- Action: Add tag "interested-premium"

**Trigger Link 2: "Download Case Study"**
- Name: download-case-study
- Redirect URL: Link to a PDF or download page
- Action: Add tag "downloaded-case-study"

**Trigger Link 3: "Unsubscribe from Promotions"**
- Name: unsubscribe-promotions
- Redirect URL: Confirmation page
- Action: Remove tag "subscribed-promotions"

**Trigger Link 4: "Book a Call"**
- Name: book-call-from-email
- Redirect URL: Your calendar booking link
- Action: Add tag "clicked-book-call", move to pipeline stage "Interested"

### Hands-On Exercise 7.7: Use Trigger Links in Emails

1. Open your "Monthly Special Offer" email template
2. Replace the CTA button URL with Trigger Link #1 ("Interested in Premium")
3. Add a text link "Read our case study" with Trigger Link #2
4. Add "Update your email preferences" link with Trigger Link #3
5. Save the template
6. Send a test email to yourself
7. Click the trigger links in the test email
8. Check your contact record - verify the tags were applied

### Hands-On Exercise 7.8: Trigger Links for Segmentation

Design a "preference center" email:

Subject: "What interests you most?"

Body includes multiple trigger links:
- "I'm interested in [Service A]" → tag: "interest-service-a"
- "I'm interested in [Service B]" → tag: "interest-service-b"
- "I'm interested in [Service C]" → tag: "interest-service-c"

This lets contacts self-segment by clicking what they care about, which you can use for targeted follow-ups.

---

## Part 4: Email Compliance (20 min)

### Hands-On Exercise 7.9: Email Compliance Setup

**Certification Topic: Making Email Compliant**

Navigate to **Settings > Email Services**:

1. **Email domain setup:**
   - Set up a dedicated sending domain (if not done)
   - Verify DNS records (SPF, DKIM, DMARC)
   - Understand the difference between shared and dedicated domains

2. **Default unsubscribe settings:**
   - Navigate to LC Email settings
   - Enable default unsubscribe link
   - Customize the unsubscribe page text

3. **Reply and Forward settings:**
   - Configure reply-to address
   - Set up email forwarding rules
   - Test reply handling

4. **Unsubscribe via Trigger Links:**
   - Create a trigger link for custom unsubscribe
   - Test the unsubscribe flow
   - Verify the contact is properly opted out

---

## Part 5: Social Planner (15 min)

### Hands-On Exercise 7.10: Explore Social Planner

Navigate to **Marketing > Social Planner**:

1. Review the interface and capabilities
2. **If you have business social accounts:** Connect them (Facebook, Instagram, Google Business, LinkedIn)
3. **If no social accounts to connect:** Explore the connection interface, note what platforms are supported, and understand the setup flow. You can still explore the post composer and calendar view without connected accounts.
4. Create a test social post (draft mode):
   - Write post copy
   - Add an image
   - Schedule for a future time
   - Select platforms (or note which you'd select)
5. Review the social calendar view

---

## Part 6: API Lab

```bash
python scripts/day-07-marketing-api.py
```

---

## Case Scenarios

### Case Scenario 1: E-Commerce Product Launch

**Situation:** An online store is launching a new product line. They need a 3-email campaign sequence.

**Your Task:**
1. Build 3 email templates:
   - **Teaser** (3 days before launch): "Something exciting is coming..."
   - **Launch Day**: "It's here! Introducing [Product Name]"
   - **Last Chance** (3 days after launch): "Don't miss out - limited stock remaining"
2. Each email should have:
   - Professional design matching the brand
   - Trigger links on CTAs to track interest
   - Mobile-responsive layout
   - Unsubscribe link
3. Create a Smart List of "Engaged Subscribers" (opened email in last 30 days)
4. Schedule the campaign: Teaser on Monday, Launch on Thursday, Last Chance on Sunday
5. Set up trigger links so anyone who clicks "Shop Now" gets tagged "launch-interested"

### Case Scenario 2: Real Estate Newsletter

**Situation:** Build a newsletter template as if you were a real estate agent. Use placeholder/sample data.

**Your Task:**
1. Build a newsletter template with:
   - 3 featured listings (use placeholder images from free stock photo sites, make up prices/details)
   - Market update section (use sample stats)
   - "Just Sold" section
   - Agent bio/contact section
2. Each listing should have a trigger link: "I'm interested in this property"
   - When clicked: Add tag "interested-listing-1", "interested-listing-2", etc.
3. Create the campaign targeting your existing contacts (even if only 5-20 contacts)
4. Send a test to yourself, click the trigger links, verify tags are applied
5. Design the follow-up: What workflow SHOULD trigger when someone clicks a property trigger link?

### Case Scenario 3: Re-Engagement Campaign

**Situation:** Build a re-engagement email campaign. Even with few contacts, the template and flow design is what matters.

**Your Task:**
1. Create a Smart List: "Disengaged - 60 Days" (no email opens in 60 days, still subscribed). With a new account this may return 0 results - that's fine, the filter logic is the learning goal.
2. Build a re-engagement email:
   - Subject line ideas: "We miss you!", "Still interested?", "Should we stop emailing?"
   - Include a clear CTA: "Yes, keep me subscribed" (trigger link)
   - Include: "No thanks, unsubscribe me" (trigger link unsubscribe)
3. Send a test campaign to yourself and 2-3 test contacts
4. Click the trigger links and verify they work
5. Document: In production, what would you do with contacts who don't click after 7 days?

---

## Day 7 Recap Questions

1. What are the key elements every marketing email must include for legal compliance?
2. How do Trigger Links differ from regular hyperlinks in an email?
3. What metrics should you monitor after launching an email campaign?
4. How do you set up email domain authentication (SPF, DKIM, DMARC)?
5. Explain how you'd use Trigger Links to create a self-segmenting email.
6. A client's email open rate is 5%. What troubleshooting steps would you take?

---

## Next Day Preview

**Day 8: Sites - Funnels & Websites** - You'll build landing pages, funnels, forms, and surveys in GHL's page builder.
