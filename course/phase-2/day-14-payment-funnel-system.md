# Day 14: E-Commerce & Payment Funnel System

**Time Required:** 3-4 hours
**Combines:** Sites/Funnels (D8) + Payments (D6) + Automation (D9) + Marketing (D7) + Pipeline (D5)
**Level:** Intermediate

---

## Today's Mission

Sunrise Wellness Studio has memberships, personal training, nutrition plans, class packs, and supplements. Right now, a potential member has to walk in, talk to someone at the front desk, and sign up on the spot. That works -- but it limits you to people who physically show up during business hours. What about the person scrolling Instagram at 11 PM who thinks "I should finally join a gym"? What about the member who wants to add a nutrition plan but keeps forgetting to ask at the front desk? What about the prospect who clicked your ad, looked at the pricing page, started filling out the form... and then got distracted by a text message and never came back?

Today you solve all of that. You are going to build a complete e-commerce system inside GHL: a membership sales page with a comparison of all three tiers, an order form that accepts payment, a post-purchase automation that confirms the sale, grants access, and nurtures the new member, an abandoned checkout workflow that follows up with people who started but did not finish buying, and a post-purchase upsell system that recommends relevant add-on products based on the member's goals.

Here is the product catalog you will work with today:

**Memberships (recurring monthly):**
| Tier | Price | Includes |
|------|-------|----------|
| Basic | $79/month | Unlimited group classes, locker access |
| Premium | $149/month | Everything in Basic + 2 PT sessions/month, nutrition assessment |
| VIP | $249/month | Everything in Premium + unlimited PT, priority booking, protein kit monthly |

**Products (one-time):**
| Product | Price | Description |
|---------|-------|-------------|
| Personal Training Session | $75 | Single drop-in PT session |
| Nutrition Plan | $200 | 12-week custom nutrition program |
| 10-Class Pack | $120 | Punch card for 10 group classes |
| Protein Starter Kit | $45 | Shaker, protein powder, supplement guide |

By the end of today, all of these will be purchasable online, and the entire post-purchase experience will be automated.

**Important note:** You do NOT need Stripe or any payment processor connected for today's exercises. You will build the entire system -- pages, forms, workflows, automations -- exactly as you would in production. The only difference is that the order form will not process real charges without a live payment integration. Everything else works identically. When you (or a client) later connect Stripe, the system goes live instantly.

---

## What You'll Combine

| Phase 1 Feature | Day Built | Role in Today's System |
|-----------------|-----------|----------------------|
| Funnel Builder | Day 8 | Sales page with membership comparison and order form |
| Products & Pricing | Day 6 | Membership tiers and add-on products defined in GHL |
| Coupons | Day 6 | WELCOME20 discount for first-time buyers |
| Payment Links / Order Forms | Day 6 | Embedded checkout on the sales page |
| Workflows | Day 9 | Post-purchase automation and abandoned cart recovery |
| Email Templates | Day 3 | Confirmation emails, welcome sequence, upsell offers |
| SMS Templates | Day 3 | Quick confirmations and follow-up nudges |
| Pipeline | Day 5 | Move purchased members to "Closed - Member" stage |
| Tags & Custom Fields | Day 2 | Track membership tier, purchase date, fitness goals |
| Email Campaigns | Day 7 | Upsell sequences personalized by member interests |

---

## The System Architecture

Before you start building, study this diagram. It shows every path a visitor can take -- from landing on the sales page to becoming a member with upsell products. This is the complete system you will have by the end of today.

```
[Visitor Lands on Membership Sales Page]
        |
        |  (scrolls through tier comparison,
        |   reads benefits, sees testimonials)
        |
[Clicks "Join Now" on chosen tier]
        |
[Order Form Page]
        |
  +-----+-----+
  |             |
[Completes    [Abandons
 Payment]      Checkout]
  |             |
  |        [Abandoned Cart Workflow]
  |        |  1hr: "Still thinking?" email
  |        |  24hr: FAQ + objection handling email
  |        |  72hr: TRIALCONVERT coupon email
  |        |
  |        [Completes Payment via recovery]──┐
  |                                          |
  ├──────────────────────────────────────────┘
  |
[Post-Purchase Workflow]
  |
  ├── Confirmation email + SMS
  ├── Tag: "member-[tier]" (basic/premium/vip)
  ├── Pipeline: Move to "Closed - Member"
  ├── Day 1: Welcome email (what to expect)
  ├── Day 3: "Book your first session" email
  └── Day 7: Personalized upsell
      |
      ├── Fitness Goal = Weight Loss → Nutrition Plan offer
      ├── Fitness Goal = Muscle Building → Extra PT sessions offer
      ├── Fitness Goal = General Fitness → 10-Class Pack offer
      └── All tiers below VIP → Upgrade offer

ALL PATHS CONVERGE:
===================
Every paying member ends up with:
  1. Contact record updated (membership tier, join date, tags)
  2. Pipeline opportunity moved to "Closed - Member" (Won)
  3. Automated welcome + onboarding sequence
  4. Personalized upsell offer within 7 days
  5. Community/portal access (if built on Day 10)
```

The key insight: **the sale is not the finish line -- it is the starting line.** The order form collects the payment, but everything that happens after (confirmation, onboarding, upsells) is what turns a one-time buyer into a long-term member. And the abandoned cart system catches the 60-70% of people who start checkout but do not finish.

---

## Part 1: Build the Membership Sales Page (45 min)

### Why a Dedicated Sales Page Matters

On Day 8, you built a Free Trial funnel to capture leads. Today's funnel is different -- it is designed to SELL, not just capture. The goal is not "get their email" but "get their credit card." That means the page needs to do more work: explain the value, compare options, address objections, build trust, and make it easy to buy.

A good membership sales page answers five questions every buyer has:
1. What do I get? (Features and benefits by tier)
2. How much does it cost? (Clear, transparent pricing)
3. Is it worth it? (Testimonials and social proof)
4. What if I have questions? (FAQ section)
5. How do I sign up? (Obvious call-to-action)

### Exercise 14.1: Build the Membership Sales Funnel

**Purpose:** Create a two-page funnel: a sales page that presents all three membership tiers with a comparison, and an order form page that captures payment.

Navigate to **Sites > Funnels > + Create Funnel**

**Step 1: Create the Funnel**
1. Click **Create New Funnel**
2. Select **Start from Scratch** (not a template -- you need to understand every piece)
3. **Name:** "Sunrise Wellness - Membership Sales"
4. This will create a funnel with a default page. You will customize it.

**Step 2: Build the Sales Page**

Rename the default page to "Membership Options" and open the page editor. Build the following sections from top to bottom. You do not need pixel-perfect design -- focus on the structure and content.

**Section 1: Hero**
- **Headline:** "Transform Your Body. Transform Your Life."
- **Subheadline:** "Join Sunrise Wellness Studio and get unlimited classes, expert coaching, and a community that keeps you accountable."
- **Button:** "See Membership Options" (anchor link that scrolls down to the pricing section)
- **Background:** Use a fitness-themed image or a solid color that fits the wellness brand

**Section 2: Benefits Overview**
- Add 3-4 benefit blocks (use an icon + headline + short description layout):
  - "Unlimited Group Classes" -- Yoga, HIIT, Pilates, Spin, and more. New schedule every month.
  - "Expert Personal Trainers" -- Certified coaches who build custom programs for your goals.
  - "Nutrition Guidance" -- From meal planning to supplement advice, we fuel your results.
  - "Supportive Community" -- Accountability partners, group challenges, and member events.

**Section 3: Membership Tier Comparison**

This is the most important section on the page. Build a three-column comparison layout:

| | Basic - $79/mo | Premium - $149/mo | VIP - $249/mo |
|---|---|---|---|
| Unlimited Group Classes | Yes | Yes | Yes |
| Locker Access | Yes | Yes | Yes |
| 2 PT Sessions/Month | -- | Yes | Yes |
| Nutrition Assessment | -- | Yes | Yes |
| Unlimited PT Sessions | -- | -- | Yes |
| Priority Booking | -- | -- | Yes |
| Monthly Protein Kit | -- | -- | Yes |
| **Best For** | Budget-conscious beginners | Serious about results | Maximum support and convenience |

Implementation options in the GHL page editor:
- **Option A (Columns):** Use a 3-column row. Each column is a card with the tier name, price, feature list, and a "Join Now" button. This is the most common approach.
- **Option B (Table):** Use a table element if available in your editor. Some GHL editor versions have a table block.
- **Option C (Rows):** Use individual rows with check/X icons for each feature. More mobile-friendly but takes more vertical space.

> **Design Tip:** Visually highlight the Premium tier as the "Most Popular" or "Best Value" option. Most pricing pages use a different background color, a "POPULAR" badge, or a slightly larger card for the recommended tier. This is called "anchoring" -- it guides the visitor toward the option you want them to choose.

Each tier card should have a **"Join Now - $X/mo"** button. For now, have all three buttons link to the order form page (you will create it in the next step). You can pass the selected tier via URL parameter or handle it on the order form page itself.

**Section 4: Testimonials**
- Add 2-3 testimonial blocks with placeholder content:
  - "I joined as a Basic member and upgraded to Premium within a month. The PT sessions alone are worth it." -- Sarah M.
  - "The VIP membership changed everything. Having unlimited PT means I never have an excuse to skip. Down 30 pounds and counting." -- James R.
  - "I was nervous to start, but the community here is incredible. Everyone is so supportive." -- Maya T.

**Section 5: FAQ**
- Build an FAQ section that addresses common objections:
  - "Can I cancel anytime?" -- Yes. All memberships are month-to-month with no long-term contract. Cancel with 30 days notice.
  - "Can I upgrade or downgrade my tier?" -- Absolutely. Changes take effect on your next billing date.
  - "Is there a free trial?" -- Yes! We offer a 7-day free trial. [Link to your Day 8 Free Trial funnel]
  - "What if I'm a total beginner?" -- Perfect. Most of our members started as beginners. Our trainers scale every workout to your level.
  - "Do I need to bring anything?" -- Just a water bottle and athletic shoes. We provide towels and lockers.

**Section 6: Final Call-to-Action**
- **Headline:** "Ready to Start?"
- **Subheadline:** "Pick your membership and join the Sunrise Wellness family today."
- Three buttons, one for each tier, linking to the order form page

**Step 3: Create the Order Form Page**

1. In the funnel editor, click **+ Add New Step** to create a second page
2. **Name:** "Order Form"
3. **Path:** /order
4. Open this page in the editor

For now, add a heading: "Complete Your Membership" and a subheadline: "You're one step away from joining Sunrise Wellness Studio." You will add the actual order form in Exercise 14.2.

**Step 4: Create the Thank You Page**

1. Add a third funnel step
2. **Name:** "Welcome"
3. **Path:** /welcome
4. Build a simple confirmation page:
   - **Headline:** "Welcome to Sunrise Wellness Studio!"
   - **Body:** "Your membership is confirmed. Check your email for your welcome package and next steps. We cannot wait to see you in the studio!"
   - **Button:** "Book Your First Session" (link to your Day 4 calendar booking page)

**Step 5: Save and Preview**

Save all three pages and preview the funnel. Click through the flow: Sales Page > Order Form > Thank You. The order form is empty right now, but you should be able to navigate the complete path.

> **Pro Tip:** In real client work, you would spend significantly more time on design -- custom images, brand colors, mobile responsiveness testing, and copywriting refinement. For today, focus on the structure and the integration. A well-structured page with average design will always outperform a beautiful page with broken integrations.

---

## Part 2: Add the Order Form and Products (30 min)

### How Order Forms Work in GHL

On Day 6, you created products and payment links. An order form is similar to a payment link, but it is embedded directly into a funnel page. The visitor never leaves your page to pay -- the form is right there, inline with the sales content. This reduces friction and increases conversions.

An order form in GHL can:
- Display one or more products
- Accept one-time and recurring payments
- Apply coupon codes
- Offer payment plans (e.g., split $249 into 3 payments of $83)
- Redirect to a thank-you page after successful payment
- Trigger workflows via the "Order Form Submitted" or "Payment Received" event

### Exercise 14.2: Configure the Order Form

**Purpose:** Add a fully configured order form to the funnel's Order Form page, connected to the products you created on Day 6.

**Step 1: Verify Your Products Exist**

Before building the order form, confirm your products are set up in GHL:

1. Navigate to **Payments > Products** (or **Settings > Products** depending on your version)
2. Verify these products exist:

| Product Name | Price | Type | Created On |
|---|---|---|---|
| Basic Membership | $79/month | Recurring | Day 6 |
| Premium Membership | $149/month | Recurring | Day 6 |
| VIP Membership | $249/month | Recurring | Day 6 |
| Personal Training Session | $75 | One-time | Day 6 |
| Nutrition Plan | $200 | One-time | Day 6 |
| 10-Class Pack | $120 | One-time | Day 6 |
| Protein Starter Kit | $45 | One-time | Day 6 |

3. If any product is missing, create it now. Refer back to Day 6 for the setup steps. At minimum, you need the three memberships for today's exercises.

**Step 2: Verify Your Coupons Exist**

1. Navigate to **Payments > Coupons** (or the coupon section within your payment settings)
2. Confirm the **WELCOME20** coupon exists (20% off, created on Day 6)
3. If it does not exist, create it:
   - **Code:** WELCOME20
   - **Discount:** 20% off
   - **Applies to:** All products (or specifically to membership products)
   - **Usage limit:** One per customer
4. Also confirm or create the **TRIALCONVERT** coupon:
   - **Code:** TRIALCONVERT
   - **Discount:** 15% off first month (or $15 off, or whatever you configured on Day 6)
   - **Applies to:** Membership products
   - **Usage limit:** One per customer

**Step 3: Add the Order Form to the Funnel Page**

1. Open the "Order Form" page in the funnel editor
2. Look for the **Order Form** element in the elements panel (it may be under "Forms" or "Payments" depending on your editor version)
3. Drag the Order Form element onto the page, below the headline

**Step 4: Configure the Order Form**

Once the order form element is on the page, configure it:

1. **Products:** Add all three membership tiers:
   - Basic Membership - $79/month
   - Premium Membership - $149/month
   - VIP Membership - $249/month
   - Configure them as selectable options (radio buttons or cards) so the visitor picks one

2. **Bump Offer (Optional Upsell at Checkout):**
   - If your GHL version supports order bumps, add one:
   - **Product:** Protein Starter Kit - $45
   - **Bump Text:** "Add a Protein Starter Kit to your first month? Includes premium protein powder, a shaker bottle, and our supplement guide. Only $45 -- 40% less than buying separately."
   - The bump appears as a checkbox near the payment button. It is the easiest upsell because the buyer is already in a purchasing mindset.

3. **Coupon Field:**
   - Enable the coupon code field so buyers can enter WELCOME20
   - This field should be visible but not required

4. **Contact Information Fields:**
   - First Name
   - Last Name
   - Email
   - Phone
   - These should map to contact fields automatically

5. **Payment Fields:**
   - Card Number, Expiration, CVC (these appear automatically when a payment integration is connected)
   - Without Stripe connected, these fields may show as disabled or not appear. That is fine for today.

6. **Redirect After Purchase:**
   - Set the success redirect to the "Welcome" (thank-you) page of this funnel
   - The URL will be something like: `your-funnel-url/welcome`

7. **Button Text:** "Start My Membership"

> **Payment Plan Option:** Some GHL plans allow you to offer payment plans on the order form. If available, you could offer the VIP membership as "$249/month or 3 payments of $89 to get started." This lowers the barrier to entry for the highest-tier option. Check your order form settings for a "Payment Plan" or "Installment" option.

**Step 5: Style the Order Form Page**

Add supporting content around the order form:

1. **Above the form:** "Complete Your Membership" heading + a brief reassurance line: "Secure checkout. Cancel anytime. No long-term contracts."
2. **To the left or below the form:** A summary of what they are getting:
   - "Your membership includes:"
   - Bullet list of key benefits
   - "Questions? Call us at (555) 123-4567"
3. **Trust indicators near the submit button:**
   - "256-bit SSL encrypted"
   - "30-day money-back guarantee"
   - "Cancel anytime -- no questions asked"

**Save the page.**

> **Real-World Note:** Without a connected Stripe (or other payment processor), the order form will not actually process payments. However, the form submission event will still fire in some GHL configurations, which means your workflows CAN still be tested using test mode or manual triggers. If the form does not fire an event without Stripe, you can test your workflows by manually adding the trigger tags to a test contact.

---

## Part 3: Post-Purchase Automation (45 min)

### Why Post-Purchase Matters More Than the Sale

Here is a number that should change how you think about e-commerce: **the average business loses 20-30% of new customers within 30 days.** Not because the product is bad -- because the follow-up is bad. The customer buys, gets a generic receipt, and hears nothing until the next billing cycle. They never fully onboard. They never see the value. They cancel.

A good post-purchase workflow does three things:
1. **Confirms** -- reassures the buyer that the purchase went through and they made a good decision
2. **Activates** -- gets them to take their first action (book a session, visit the studio, use the product)
3. **Expands** -- once they are engaged, offers relevant upgrades or add-ons

You are about to build all three.

### Exercise 14.3: Build the "New Member" Post-Purchase Workflow

**Purpose:** Create a workflow that fires when someone purchases a membership and guides them through their first week as a member.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "E-Commerce - New Member Onboarding"

**Step 1: Set the Trigger**
1. Click **Add New Workflow Trigger**
2. Select one of these (depending on your GHL version and setup):
   - **Payment Received** -- fires when a payment is processed (ideal if Stripe is connected)
   - **Order Form Submitted** -- fires when the order form is submitted
   - **Invoice Paid** -- fires when an invoice is marked as paid
3. If available, filter the trigger to only fire for membership products (not one-time product purchases)
4. Click **Save Trigger**

> **No Stripe? No Problem.** If you cannot set a Payment Received trigger because no payment processor is connected, use one of these alternatives for testing:
> - **Tag Added** trigger: Tag = `purchased-membership`. You will manually add this tag to test contacts to simulate a purchase.
> - **Form Submitted** trigger: If your order form can submit without payment processing.
> Choose whichever works in your setup. The workflow logic is identical regardless of trigger type.

**Step 2: Determine Membership Tier**

Add an **If/Else** branch immediately after the trigger.

1. Name it: "Which Membership Tier?"
2. You need to identify which product was purchased. Depending on your trigger type, you can branch on:
   - **Product Name** contains "Basic" / "Premium" / "VIP"
   - **Order Amount** = $79 / $149 / $249
   - **Product ID** (if you know the specific product IDs from Day 6)
3. **Branch 1 (Basic):** Product contains "Basic" OR amount = $79
4. **Branch 2 (Premium):** Product contains "Premium" OR amount = $149
5. **Branch 3 (VIP / Else):** Default branch catches VIP and anything unexpected

**Step 3: Apply Tags by Tier**

In each branch, add an **Add Tag** action:

- **Basic branch:** Add tags: `purchased-membership`, `member-basic`
- **Premium branch:** Add tags: `purchased-membership`, `member-premium`
- **VIP branch:** Add tags: `purchased-membership`, `member-vip`

> **Why tier-specific tags?** These tags power everything downstream: Smart List segmentation, conditional email content, upsell targeting, and community access levels. A `member-premium` tag tells every other workflow in your system exactly what this person is paying for.

**Step 4: Update Custom Fields**

After the tags (still inside each branch), add **Update Contact Field** actions:

- Set **Membership Type** = "Basic" / "Premium" / "VIP" (depending on branch)
- Set **Membership Start Date** = `{{current_date}}` (or the appropriate date variable)

**Step 5: Move Pipeline to "Closed - Member"**

After the branches converge (or at the end of each branch), add an **Update Opportunity** action:

1. Pipeline: Membership Sales
2. Stage: **Closed - Member** (or "Closed Won" -- whatever you named your final positive stage on Day 5)
3. Status: **Won**
4. This marks the lead as converted in your pipeline reporting

> **What if there is no existing opportunity?** If someone buys directly from the sales page without going through your lead capture system first, there may not be a pipeline opportunity to update. Two options: (1) Add a "Create Opportunity" action before the "Update Opportunity" action, with a condition that checks if an opportunity already exists. (2) Accept that direct buyers will not have pipeline records -- they bypass the sales process entirely. Option 1 is cleaner for reporting.

**Step 6: Send Confirmation Email**

Add a **Send Email** action (after the branches converge):

- **Subject:** "Welcome to Sunrise Wellness, {{contact.first_name}}!"
- **Body:**
  ```
  Hey {{contact.first_name}},

  You are officially a Sunrise Wellness Studio member! Here is
  your membership summary:

  Membership: [Tier Name]
  Monthly Rate: [Price]
  Start Date: Today
  Billing: Recurring monthly

  YOUR NEXT STEPS:
  1. Book your first session: [Calendar booking link]
  2. Download our app: [App link if applicable]
  3. Check the class schedule: [Schedule link]

  If you have any questions, just reply to this email or
  call us at (555) 123-4567.

  Welcome to the family!
  -- The Sunrise Wellness Team
  ```

> **Personalizing by Tier:** If you want different email content per tier, keep the confirmation email inside each branch instead of after convergence. Basic members get the group class schedule. Premium members get their PT session booking link. VIP members get their personal concierge contact info. The more personalized, the better -- but a single email that works for all tiers is fine for now.

**Step 7: Send Confirmation SMS**

Add a **Send SMS** action:

- **Message:** "Welcome to Sunrise Wellness, {{contact.first_name}}! Your membership is confirmed. Book your first session here: [booking link]. Questions? Reply to this text!"

**Step 8: Wait 1 Day, Then Send Welcome Email**

1. Add a **Wait** action: 1 day
2. Add a **Send Email** action:
   - **Subject:** "Your first week at Sunrise Wellness -- here's what to expect"
   - **Body:**
     ```
     Hi {{contact.first_name}},

     Welcome to Day 1 as a Sunrise Wellness member! Here is what
     your first week will look like:

     DAY 1-2: EXPLORE
     - Drop by the studio for a tour (no appointment needed)
     - Try a group class -- here's this week's schedule: [link]
     - Meet the front desk team (they know you're coming!)

     DAY 3-4: GET STARTED
     - Book your first PT session or consultation: [booking link]
     - Check out the member portal: [portal link]
     - Set your fitness goals in your member profile

     DAY 5-7: BUILD THE HABIT
     - Aim for 2-3 visits this week
     - Join our member community group: [community link]
     - Ask questions -- no question is too basic

     The first week is all about getting comfortable. There is no
     pressure to have a perfect routine yet. Just show up.

     See you at the studio!
     -- The Sunrise Wellness Team
     ```

**Step 9: Wait 2 More Days, Then Prompt Session Booking**

1. Add a **Wait** action: 2 days (this puts us at Day 3 after purchase)
2. Add an **If/Else** condition: Check if the contact has the tag `first-session-booked`
   - **If tag exists:** Skip this step (they already booked)
   - **If tag does NOT exist:** Send the nudge
3. In the "no tag" branch, add a **Send Email** action:
   - **Subject:** "Have you booked your first session yet, {{contact.first_name}}?"
   - **Body:**
     ```
     Hey {{contact.first_name}},

     Quick check-in: have you booked your first session yet?

     Members who work out within their first 3 days are 4x more
     likely to stick with their fitness routine long-term. (That
     is an actual stat, and we want you to be on the right side
     of it.)

     Book now -- it takes 30 seconds:
     [Calendar booking link]

     Not sure which class or trainer to start with? Here are
     our recommendations for new members:

     - If you want a low-key start: Tuesday 9 AM Yoga with Sarah
     - If you want to jump right in: Thursday 6 PM HIIT with Coach Mike
     - If you want one-on-one guidance: Book a PT session (included
       in Premium and VIP memberships)

     We are here whenever you are ready.
     -- The Sunrise Wellness Team
     ```
4. Add a **Send SMS** action in the same branch:
   - **Message:** "Hey {{contact.first_name}}, have you booked your first session at Sunrise Wellness yet? Grab a spot: [booking link]. Members who start in their first 3 days see the best results!"

**Step 10: Wait 4 More Days, Then Send Upsell**

1. Add a **Wait** action: 4 days (this puts us at Day 7 after purchase)
2. This is where the personalized upsell fires -- you will build it in Exercise 14.5
3. For now, add a placeholder **Add Tag** action: `ready-for-upsell`
4. You will replace this placeholder in Exercise 14.5

**Save the workflow. Do not publish yet.**

---

## Part 4: Abandoned Checkout Recovery (40 min)

### The Biggest Leak in Online Sales

Across all industries, approximately 70% of online shopping carts are abandoned before purchase. For service businesses like gyms and studios, the rate is somewhat lower (around 50-60%) because the purchase is more considered. But even at 50%, that means for every person who buys, another person ALMOST bought and walked away.

Those almost-buyers are the easiest revenue you will ever recover. They already visited your page, read the benefits, chose a membership, and started filling out the form. They are not cold leads -- they are warm buyers who got interrupted, got nervous about the price, or decided to "think about it." A well-timed follow-up sequence can recover 10-20% of abandoned carts.

### How Abandoned Checkout Works in GHL

GHL tracks when someone starts an order form but does not complete payment. The exact mechanism depends on your setup:

- **With Stripe connected:** GHL can detect when a form is partially filled out but no payment goes through. The trigger is typically "Order Form Submitted" with payment status = incomplete, or a "Cart Abandoned" trigger if available.
- **Without Stripe:** You may need to use an alternative approach -- for example, triggering a workflow when a contact visits the order form page (tracked via page visit) but does not receive the `purchased-membership` tag within a certain timeframe.

For today, you will build the workflow using whichever trigger is available. The follow-up logic is the same regardless.

### Exercise 14.4: Build the Abandoned Cart Recovery Workflow

**Purpose:** Create a 3-email recovery sequence for people who start checkout but do not complete their purchase.

Navigate to **Automation > Workflows > + Create Workflow > Start from Scratch**

**Name:** "E-Commerce - Abandoned Cart Recovery"

**Step 1: Set the Trigger**

Choose the trigger that works for your setup:

- **Option A (Best):** **Order Form Submission** with payment status = incomplete or failed
- **Option B:** **Page Visit** trigger for the order form page URL
- **Option C (Manual for testing):** **Tag Added** = `started-checkout` (you will manually add this tag to test contacts)

> **If using Option B (Page Visit):** You will need to add a condition early in the workflow that checks whether the contact completed the purchase. If they visited the order form page AND have the `purchased-membership` tag, they are a buyer -- not an abandoner. Exit them from the workflow immediately.

1. Click **Add New Workflow Trigger**
2. Select your trigger option
3. Click **Save Trigger**

**Step 2: Wait and Verify They Did NOT Purchase**

This step is critical. You do not want to send "come back and finish!" emails to someone who already bought.

1. Add a **Wait** action: **1 hour**
   - Why 1 hour? It gives someone time to complete the purchase if they were just experiencing a technical issue or stepped away briefly. It also creates a natural sense of "we noticed you were here."
2. Add an **If/Else** condition:
   - **If** contact has tag `purchased-membership` --> **Go To End** (exit the workflow -- they bought)
   - **Else** --> continue to the recovery emails

**Step 3: Recovery Email 1 -- "Still Thinking?" (1 Hour After Abandonment)**

Add a **Send Email** action:

- **Subject:** "You left something behind, {{contact.first_name}}"
- **Body:**
  ```
  Hey {{contact.first_name}},

  We noticed you were checking out our membership options at
  Sunrise Wellness Studio but did not finish signing up. No
  worries -- it happens!

  In case you got pulled away, here is a quick link to pick
  up where you left off:

  [Button: "Complete My Membership" --> Order Form URL]

  Your selected membership is waiting for you. And remember,
  all memberships are month-to-month -- no long-term contracts,
  cancel anytime.

  Questions? Reply to this email and we will get back to you
  within a few hours.

  -- The Sunrise Wellness Team
  ```

> **Tone Check:** Notice how this email is helpful, not pushy. It assumes the person got interrupted (which is true most of the time) rather than implying they do not want to buy. "We noticed you were checking out" is much better than "You abandoned your cart!"

**Step 4: Wait and Check Again**

1. Add a **Wait** action: **23 hours** (this brings us to 24 hours total after abandonment)
2. Add another **If/Else** condition:
   - **If** contact has tag `purchased-membership` --> **Go To End**
   - **Else** --> continue

**Step 5: Recovery Email 2 -- FAQ and Objection Handling (24 Hours)**

Add a **Send Email** action:

- **Subject:** "Quick answers about joining Sunrise Wellness"
- **Body:**
  ```
  Hi {{contact.first_name}},

  We know joining a new studio is a big decision, so we put
  together answers to the questions we hear most:

  Q: What if I'm not fit enough?
  A: Every workout is scalable. Our trainers modify exercises
  for all levels. Truly -- beginners are our favorite people
  to work with because the progress is incredible.

  Q: What if I can't make it regularly?
  A: That's the beauty of unlimited classes. Come once a week
  or five times a week -- the membership works either way.
  There are no "use it or lose it" sessions.

  Q: Can I really cancel anytime?
  A: Yes. 100%. No contracts. No cancellation fees. No hoops
  to jump through. Just 30 days notice.

  Q: What's the difference between the tiers?
  A: Basic ($79) = unlimited classes. Premium ($149) = classes
  + 2 PT sessions/month + nutrition assessment. VIP ($249) =
  everything unlimited + priority booking + monthly protein kit.

  Ready to get started?
  [Button: "Join Sunrise Wellness" --> Order Form URL]

  Still not sure? Reply to this email and let's talk about
  what's holding you back. We're real people, not robots.

  -- The Sunrise Wellness Team
  ```

> **Why FAQ format?** By 24 hours, the initial excitement of finding the studio has faded. The person is now in "evaluation mode" -- weighing pros and cons. An FAQ email directly addresses the most common objections (too intimidating, too expensive, locked into a contract) and removes them. This is not pushy sales -- it is genuinely helpful information that makes the decision easier.

**Step 6: Wait and Check One More Time**

1. Add a **Wait** action: **48 hours** (this brings us to 72 hours total)
2. Add another **If/Else** condition:
   - **If** contact has tag `purchased-membership` --> **Go To End**
   - **Else** --> continue to the final email

**Step 7: Recovery Email 3 -- Incentive Offer (72 Hours)**

Add a **Send Email** action:

- **Subject:** "A little nudge (and a thank-you discount), {{contact.first_name}}"
- **Body:**
  ```
  Hey {{contact.first_name}},

  This is our last email about this (we promise we are not
  going to keep bugging you).

  We would really love to have you at Sunrise Wellness. And
  since you took the time to check us out, we want to make
  it a little easier to say yes.

  Use code TRIALCONVERT at checkout for 15% off your first
  month:

  [Button: "Claim My Discount" --> Order Form URL]

  Basic: $79 --> $67.15/first month
  Premium: $149 --> $126.65/first month
  VIP: $249 --> $211.65/first month

  This code expires in 48 hours.

  No pressure. If now is not the right time, we will be here
  whenever you are ready.

  -- The Sunrise Wellness Team
  ```

**Step 8: Final Tag and Exit**

After the third email:
1. Add a **Wait** action: **48 hours** (to see if the coupon converts them)
2. Add a final **If/Else**:
   - **If** contact has tag `purchased-membership` --> **Go To End** (they converted)
   - **Else** --> Add tag: `abandoned-cart-complete` (the full recovery sequence ran without conversion)
3. This tag lets you identify people who saw all three recovery emails and still did not buy. Useful for future re-engagement campaigns or paid retargeting.

**Save the workflow. Do not publish yet.**

> **Pro Tip:** In production, you would add an **SMS** alongside emails 1 and 3 (not email 2 -- three SMS messages in 72 hours feels aggressive). The SMS would be short: "Hey {{contact.first_name}}, you were so close to joining Sunrise Wellness! Finish signing up here: [link]". SMS has a 98% open rate vs. email's 20-25%, so even one SMS can significantly boost recovery rates.

---

## Part 5: Post-Purchase Upsell System (30 min)

### The Right Offer to the Right Person

Generic upsells ("Hey, want to buy more stuff?") feel spammy. Personalized upsells ("Since you're focused on weight loss, our 12-week Nutrition Plan would accelerate your results") feel helpful. The difference is data -- and you have been collecting it since Day 2.

The **Fitness Goals** custom field (created on Day 2 and collected via forms on Day 8) tells you exactly what each member cares about. Today you will use that data to send the right upsell offer to each person.

### Exercise 14.5: Build the Personalized Upsell Workflow

**Purpose:** Send a personalized product recommendation on Day 7 of membership, based on the member's stated fitness goals.

Navigate back to the "E-Commerce - New Member Onboarding" workflow you built in Exercise 14.3.

**Step 1: Replace the Placeholder**

Find the placeholder tag action you added in Step 10 of Exercise 14.3 (`ready-for-upsell`). You are going to replace it with a branching upsell system.

1. Delete the `ready-for-upsell` tag action
2. In its place, add an **If/Else** branch

**Step 2: Branch by Fitness Goals**

1. Name the branch: "Upsell by Fitness Goal"
2. **Branch 1:** Custom Field "Fitness Goals" **contains** "Weight Loss" (or "weight-loss" or however the value is stored)
3. **Branch 2:** Custom Field "Fitness Goals" **contains** "Muscle" (catches "Muscle Building," "Build Muscle," "Muscle Gain," etc.)
4. **Branch 3:** Custom Field "Fitness Goals" **contains** "General" OR "Fitness" (catches "General Fitness," "Get Fit," etc.)
5. **Else (default):** Catches anyone whose fitness goal does not match the above, or who did not specify a goal

**Step 3: Weight Loss Path -- Nutrition Plan Offer**

In Branch 1, add a **Send Email** action:

- **Subject:** "The missing piece in your weight loss plan, {{contact.first_name}}"
- **Body:**
  ```
  Hey {{contact.first_name}},

  You have been a Sunrise Wellness member for a week now --
  how is it going? We hope you are loving the classes and
  the community!

  Since your goal is weight loss, we want to share something
  that could seriously accelerate your results:

  THE 12-WEEK CUSTOM NUTRITION PLAN ($200)

  Here is the truth: exercise is 30% of the equation. Nutrition
  is the other 70%. Our certified nutritionist will build a
  plan around YOUR lifestyle -- not a generic diet that expects
  you to eat chicken and broccoli five times a day.

  What you get:
  - Personalized macro targets based on your body and goals
  - A 12-week meal plan with grocery lists
  - Bi-weekly check-ins to adjust as you progress
  - Access to our recipe library (200+ meals)
  - Supplement recommendations

  Members who add the Nutrition Plan lose an average of 2x
  more weight in their first 90 days.

  [Button: "Get My Nutrition Plan" --> Product purchase link]

  Use code WELCOME20 for 20% off: just $160.

  Questions? Book a free 15-minute nutrition chat: [link]

  -- The Sunrise Wellness Team
  ```

**Step 4: Muscle Building Path -- Extra PT Sessions**

In Branch 2, add a **Send Email** action:

- **Subject:** "Want to build muscle faster, {{contact.first_name}}?"
- **Body:**
  ```
  Hey {{contact.first_name}},

  A week into your Sunrise Wellness journey -- how are you
  feeling? Ready to level up?

  Since muscle building is your goal, here is what the research
  says: members who train with a personal trainer build lean
  muscle 47% faster than those who train alone. That is because
  a trainer pushes you past the point where most people stop,
  and ensures every rep counts with proper form.

  ADD PERSONAL TRAINING TO YOUR ROUTINE:

  Single PT Session: $75
  Already included in Premium (2/month) and VIP (unlimited)

  If you are on the Basic plan, adding even one PT session
  per week can transform your results. Your trainer will build
  a progressive overload program specifically for your body
  and your goals.

  [Button: "Book a PT Session" --> Calendar or product link]

  Want to upgrade instead? Premium ($149/mo) includes 2 PT
  sessions per month -- that is a $150 value for just $70 more
  than Basic.

  [Button: "Upgrade to Premium" --> Order form or upgrade link]

  -- The Sunrise Wellness Team
  ```

**Step 5: General Fitness Path -- 10-Class Pack**

In Branch 3, add a **Send Email** action:

- **Subject:** "A smarter way to keep showing up, {{contact.first_name}}"
- **Body:**
  ```
  Hey {{contact.first_name}},

  One week in! How are you liking Sunrise Wellness so far?

  Since you are focused on general fitness, here is a tip:
  variety is key. Mixing yoga, HIIT, spin, and strength keeps
  your body guessing and your brain from getting bored.

  We have something that makes it easy to try everything:

  10-CLASS PACK ($120)

  Pick any 10 classes from our schedule -- mix and match
  however you want. That is just $12 per class. Use them
  at your own pace (they never expire).

  Great for:
  - Trying a different class every week
  - Bringing a friend to a session (use one of your classes)
  - Stacking on top of your membership for extra visits

  [Button: "Get the 10-Class Pack" --> Product purchase link]

  Use code WELCOME20 for 20% off: just $96!

  -- The Sunrise Wellness Team
  ```

**Step 6: Default Path -- Tier Upgrade Offer**

In the Else/Default branch, add a **Send Email** action:

- **Subject:** "Getting the most out of Sunrise Wellness, {{contact.first_name}}"
- **Body:**
  ```
  Hey {{contact.first_name}},

  You have been a member for a week now -- how is everything
  going? We hope you are settling in!

  We wanted to make sure you know about everything available
  to you as a member. Depending on your goals, you might
  benefit from an upgrade:

  BASIC --> PREMIUM ($149/mo):
  + 2 PT sessions/month (a $150 value)
  + Nutrition assessment
  = Your own trainer + eating plan for just $70 more

  PREMIUM --> VIP ($249/mo):
  + Unlimited PT sessions (train every day if you want)
  + Priority booking (never wait for a spot)
  + Monthly Protein Starter Kit delivered ($45 value)
  = Maximum support for maximum results

  [Button: "Explore Upgrade Options" --> Sales page URL]

  No pressure at all. Your current membership is great.
  But if you are thinking "I wish I had more support,"
  upgrading is the easiest way to get it.

  -- The Sunrise Wellness Team
  ```

**Step 7: Tag the Upsell**

After all branches, add an **Add Tag** action: `upsell-sent-week-1`

This tag serves two purposes:
- Prevents the member from accidentally receiving the upsell again if the workflow is re-triggered
- Lets you build a Smart List of members who received the upsell but did not convert (for future follow-up)

**Save the workflow.**

---

## Part 6: End-to-End System Test (20 min)

### Exercise 14.6: Test the Complete E-Commerce System

**Purpose:** Walk through the entire system as a simulated buyer, verify every step fires correctly, and document any issues.

**Preparation:**
1. Open your test funnel in an **incognito/private browser window**
2. In your main browser, open these tabs:
   - **Contacts** (to watch for new/updated contact records)
   - **Opportunities** (Membership Sales pipeline open)
   - **Automation > Workflows** (to monitor execution)
3. Create or identify a test contact you can use. Use a real email address you can check.

**Test Path 1: Successful Purchase**

1. **Visit the sales page.** Scroll through all sections. Verify:
   - All three tiers display correctly with accurate pricing and features
   - "Join Now" buttons link to the order form page
   - FAQ section is readable and all answers display
   - The page looks reasonable on mobile (shrink your browser window to test)

2. **Click "Join Now" on Premium ($149/mo).** Verify:
   - The order form page loads
   - The order form displays with product options
   - The coupon code field is visible

3. **Fill out the order form.** Use your test contact's details.
   - If Stripe is connected: Complete a test payment
   - If no Stripe: Submit the form if possible, OR manually add the tags `purchased-membership` and `member-premium` to your test contact to simulate the purchase

4. **Check the post-purchase workflow:**
   - Does the confirmation email arrive? Check subject line, content, and links
   - Does the confirmation SMS arrive?
   - Is the correct tag applied? (`member-premium`)
   - Is the Membership Type custom field updated?
   - Is the pipeline opportunity moved to "Closed - Member"?

5. **Fast-forward the onboarding sequence for testing:**
   - Change the Wait times in the workflow temporarily to 5 minutes (instead of 1 day, 2 days, 4 days)
   - Verify the Day 1 welcome email arrives
   - Verify the Day 3 booking nudge fires (and check the If/Else logic -- add or remove the `first-session-booked` tag to test both paths)
   - Verify the Day 7 upsell email arrives with the correct personalization based on the contact's Fitness Goals custom field

**Test Path 2: Abandoned Cart**

1. Open the sales page in a fresh incognito window
2. Navigate to the order form page
3. Simulate abandonment:
   - If using a Page Visit trigger: simply visit the order form page and then close the window
   - If using a manual trigger: add the `started-checkout` tag to a DIFFERENT test contact (not the one who "purchased")
4. Wait for the first recovery email (or temporarily shorten the 1-hour wait to 5 minutes)
5. Verify:
   - Email 1 arrives after 1 hour with "left something behind" messaging
   - Email 2 arrives after 24 hours with FAQ content
   - Email 3 arrives after 72 hours with the TRIALCONVERT coupon code
   - At each checkpoint, confirm the If/Else condition properly exits the workflow if you add the `purchased-membership` tag (simulating a mid-sequence conversion)

**Test Path 3: Upsell Personalization**

1. Test with three different contacts, each with a different Fitness Goals value:
   - Contact A: Fitness Goals = "Weight Loss" --> should receive Nutrition Plan offer
   - Contact B: Fitness Goals = "Muscle Building" --> should receive PT sessions offer
   - Contact C: Fitness Goals = "General Fitness" --> should receive 10-Class Pack offer
2. Add the appropriate Fitness Goals value to each contact's custom field
3. Trigger the onboarding workflow for each (or fast-forward to the upsell step)
4. Verify each contact receives the correct personalized email

**After Testing:**

- Reset all Wait times back to production values (1 day, 2 days, 4 days for onboarding; 1 hour, 23 hours, 48 hours for abandoned cart)
- Remove test tags if you want a clean slate
- Note any issues and fix them before moving on
- **Publish both workflows** once everything passes

> **Debugging Checklist:** If something does not fire, check these in order:
> 1. Is the workflow **Published** (not Draft)?
> 2. Does the trigger match the event? (Check trigger configuration carefully)
> 3. Does the contact meet the If/Else conditions? (Check custom field values and tags)
> 4. Is there a Wait action holding things up? (Check the workflow execution timeline for the contact)
> 5. Is the email/SMS template correctly configured? (Check for merge field errors like `{{contact.fist_name}}` -- a typo that silently fails)

---

## Integration Checkpoint

You have now built a complete e-commerce and payment funnel system. Verify each piece is in place:

- [ ] **Membership Sales Page** exists with tier comparison (Basic/Premium/VIP), benefits, testimonials, and FAQ
- [ ] **Order Form Page** has the order form element with all three membership products
- [ ] **Coupon field** is enabled on the order form (WELCOME20 and TRIALCONVERT coupons exist)
- [ ] **Order bump** for Protein Starter Kit is configured (if your plan supports it)
- [ ] **Thank You / Welcome Page** exists with confirmation message and "Book First Session" button
- [ ] **Post-purchase workflow** fires on payment/submission and correctly:
  - [ ] Branches by membership tier
  - [ ] Applies tier-specific tags (`member-basic`, `member-premium`, `member-vip`)
  - [ ] Updates Membership Type custom field
  - [ ] Moves pipeline opportunity to "Closed - Member"
  - [ ] Sends confirmation email + SMS
  - [ ] Sends Day 1 welcome email
  - [ ] Sends Day 3 session booking nudge (with conditional check for `first-session-booked`)
  - [ ] Sends Day 7 personalized upsell
- [ ] **Abandoned cart workflow** fires for incomplete checkouts and correctly:
  - [ ] Waits 1 hour, then checks for purchase before sending Email 1
  - [ ] Waits 24 hours, then checks and sends FAQ email
  - [ ] Waits 72 hours, then checks and sends TRIALCONVERT coupon email
  - [ ] Exits the workflow if purchase is detected at any checkpoint
  - [ ] Tags `abandoned-cart-complete` if all 3 emails sent without conversion
- [ ] **Upsell branching** sends the correct offer based on Fitness Goals:
  - [ ] Weight Loss --> Nutrition Plan
  - [ ] Muscle Building --> PT Sessions
  - [ ] General Fitness --> 10-Class Pack
  - [ ] Default --> Tier Upgrade
- [ ] **All workflows** are published and tested end-to-end

**Total workflows built today:** 2 (New Member Onboarding, Abandoned Cart Recovery)
**Total funnel pages built today:** 3 (Sales Page, Order Form, Thank You)

---

## Case Scenario 1: BrightSmile Dental -- Whitening Package Sales Page

**Scenario:** BrightSmile Dental wants to sell their most popular cosmetic service -- a Professional Teeth Whitening Package -- directly online. The package costs $450 and includes an in-office whitening session, a take-home maintenance kit, and a 30-day follow-up check. Currently, patients have to call the office and schedule a consultation before they can even discuss pricing. BrightSmile wants to let people buy online and book their appointment in one flow.

**Your Task:** Design and build (or map out on paper) a complete e-commerce system for the whitening package. Build everything in your existing sub-account with "BrightSmile" in the naming.

### Sales Page: "BrightSmile Professional Whitening"

Build a funnel: **BrightSmile - Whitening Package**

**Page 1: Sales Page**

Structure the page to answer the specific concerns of someone considering teeth whitening:

- **Hero Section:**
  - Headline: "A Brighter Smile in Just One Visit"
  - Subheadline: "Professional-grade teeth whitening at BrightSmile Dental. Walk in with stains. Walk out 8 shades whiter."
  - Button: "See the Package Details"

- **Before/After Section:**
  - Placeholder for before/after photos (in a real build, these would be actual patient photos with consent)
  - Stats: "Average improvement: 6-8 shades lighter in one 90-minute session"

- **What's Included:**
  - In-Office Professional Whitening Session (90 minutes, $350 value)
  - Take-Home Maintenance Kit with custom trays ($100 value)
  - 30-Day Follow-Up Check ($75 value)
  - **Total Package: $450** (vs. $525 if purchased separately)

- **FAQ Section:**
  - "Does it hurt?" -- Most patients experience little to no discomfort. Mild sensitivity for 24-48 hours is normal and resolves on its own.
  - "How long does it last?" -- Results typically last 6-12 months depending on diet and habits. The take-home kit extends your results.
  - "Is it safe?" -- Yes. Professional whitening is FDA-approved and performed by a licensed dental hygienist.
  - "What if I have crowns or veneers?" -- Whitening works on natural teeth only. We will evaluate your specific situation during the pre-treatment check.
  - "Can I eat normally after?" -- You will need to avoid coffee, wine, tea, and dark-colored foods for 48 hours. We provide a complete "white diet" guide.

- **Testimonials:**
  - Placeholder testimonials about whitening results and the experience
  - Include a "comfort" testimonial: "I was nervous about sensitivity, but it was completely painless!"

**Page 2: Order Form**
- Product: Professional Whitening Package ($450 one-time)
- Contact fields: First Name, Last Name, Email, Phone
- Additional field: "Any dental concerns we should know about?" (textarea, maps to a custom field)
- Coupon field enabled (create a **BRIGHTSTART** coupon: $50 off, code expires in 30 days)
- Button: "Book My Whitening Session"
- Redirect to Thank You page

**Page 3: Thank You**
- Headline: "Your Brighter Smile Awaits!"
- Body: "Your whitening package is confirmed. We will email you with pre-appointment instructions and a link to book your session."
- Button: "Book Your Whitening Appointment" (link to a BrightSmile Whitening calendar, if you created one on Day 4, or a generic booking link)

### Post-Purchase Workflow: "BrightSmile - Whitening Onboarding"

Build this workflow:

1. **Trigger:** Payment Received (or tag `purchased-whitening` for testing)
2. **Immediate:**
   - Add tags: `purchased-whitening`, `patient-cosmetic`
   - Send confirmation email with receipt summary and "what happens next"
   - Send confirmation SMS: "Your BrightSmile whitening package is confirmed! Check your email for next steps. Questions? Call (555) 234-5678."
3. **Day 1 -- Pre-Appointment Instructions:**
   - Send email: "Preparing for Your Whitening Session"
     - Avoid whitening toothpaste for 7 days before the appointment
     - Brush and floss normally the morning of
     - Eat a normal meal before your appointment (the session is 90 minutes)
     - Wear comfortable clothes (you will be reclined the entire time)
     - "Book your session if you have not already: [booking link]"
4. **Day 3 -- What to Expect:**
   - Send email: "What Your Whitening Session Looks Like"
     - Step-by-step walkthrough of the procedure (gum protection, gel application, UV light, rinse, repeat)
     - Expected duration: 90 minutes total
     - "Most patients watch a show on their phone or just relax!"
5. **Day after appointment (triggered by appointment completion):**
   - Send aftercare email:
     - 48-hour white diet (avoid coffee, wine, tomato sauce, berries, dark chocolate)
     - How to use the take-home maintenance kit
     - "Mild sensitivity is normal and should fade within 24-48 hours"
     - "If anything feels off, call us immediately: (555) 234-5678"
6. **Day 7 -- Review request:**
   - "How is your new smile? We would love to hear about your experience: [Google review link]"
7. **Day 30 -- Maintenance upsell:**
   - "It has been a month since your whitening session! Here is how to keep your results lasting:"
   - Upsell: "Maintenance Whitening Touch-Up -- $150 (recommended every 6 months)"
   - Upsell: "Whitening Maintenance Plan -- $25/month for custom whitening gel refills, shipped to your door"

### Abandoned Cart for Whitening

Adapt the abandoned cart workflow:
- Email 1 (1 hour): "You were looking at our whitening package -- any questions we can answer?"
- Email 2 (24 hours): Address whitening-specific concerns (sensitivity, safety, results longevity)
- Email 3 (72 hours): Offer the BRIGHTSTART coupon ($50 off --> $400 for the full package)

**Design Challenge:** What is the biggest difference between selling a service package online vs. a monthly membership? Think about how the post-purchase flow changes when the product is a one-time service with a specific appointment vs. an ongoing subscription with recurring engagement. How does the "activation" step differ?

---

## Case Scenario 2: Elevate Digital Agency -- Digital Audit Product Page

**Scenario:** Elevate Digital Agency wants to sell a "Comprehensive Digital Audit" as a standalone product for $1,500. The audit includes a full analysis of a business's website, SEO, paid ads, social media, and competitor landscape, delivered as a 30-page report with an action plan. Currently, the audit is only offered as part of a sales conversation. Elevate wants to let business owners buy it directly online -- and then use the audit delivery process to convert them into monthly retainer clients.

**Your Task:** Design and build the complete e-commerce system for the Digital Audit. Build everything with "Elevate" in the naming.

### Sales Page: "Elevate - Digital Audit"

**Page 1: Sales Page**

This is a B2B sales page, so the tone and structure differ from a wellness studio or dental office. Business owners care about ROI, credibility, and specificity.

- **Hero Section:**
  - Headline: "Find Out Exactly Where Your Marketing Is Leaking Money"
  - Subheadline: "Our Comprehensive Digital Audit analyzes your website, SEO, ads, and social media -- then gives you a prioritized action plan to fix what is broken."
  - Button: "Get Your Digital Audit - $1,500"

- **What's Included:**
  - Website Performance Analysis (speed, UX, conversion rate optimization)
  - SEO Health Check (rankings, backlink profile, technical SEO, content gaps)
  - Paid Advertising Audit (Google Ads, Facebook/Instagram Ads, wasted spend analysis)
  - Social Media Assessment (engagement rates, content performance, competitor comparison)
  - Competitor Landscape Report (what your top 3 competitors are doing better)
  - 30-Page Custom Report with prioritized action plan
  - 60-Minute Strategy Call to walk through findings and answer questions
  - "Delivered within 10 business days of receiving your access credentials"

- **Who This Is For:**
  - Businesses spending $2,000+/month on marketing who are not sure if it is working
  - Companies thinking about switching agencies who want an independent assessment
  - Business owners who handle their own marketing but want an expert opinion
  - Startups preparing for a growth phase who need a baseline

- **Social Proof:**
  - "We have audited 200+ businesses across 15 industries"
  - Case study snapshot: "We found $3,200/month in wasted ad spend for a SaaS company. Our audit paid for itself 2x in the first month."
  - Testimonial placeholders from business owners

- **FAQ:**
  - "What access do you need from me?" -- Google Analytics, Google Ads, Facebook Business Manager, social media accounts, and website admin. We provide a secure credential sharing form.
  - "How long does the audit take?" -- 10 business days from when we receive all access credentials.
  - "What if I don't have ads running?" -- We will focus on organic opportunities (SEO, content, social) and provide a paid advertising strategy recommendation.
  - "Is this a sales pitch for your agency?" -- The audit stands on its own. You get a complete report and action plan you can execute yourself or with any provider. If you want our help implementing, we can discuss that on the strategy call.
  - "What's the ROI?" -- Our average audit client identifies 3-5 immediate improvements worth $2,000-$10,000 per month in savings or new revenue.

**Page 2: Order Form**
- Product: Comprehensive Digital Audit ($1,500 one-time)
- Contact fields: First Name, Last Name, Business Email, Phone
- Additional fields:
  - "Business Name" (maps to custom field)
  - "Website URL" (maps to custom field)
  - "Primary marketing challenge" (dropdown: Not Enough Leads, High Ad Spend / Low ROI, Low Website Traffic, Poor Social Media Engagement, Don't Know What's Working, Other)
- No coupon field on this one (premium pricing, no discounts -- maintain perceived value)
- Button: "Purchase My Digital Audit"

**Page 3: Thank You**
- Headline: "Your Digital Audit Is Underway!"
- Body: "Thank you for investing in your business's marketing. Here is what happens next:"
- Next Steps:
  1. "Check your email -- we just sent a secure credential sharing form"
  2. "Share your access credentials within 48 hours"
  3. "Your audit will be delivered within 10 business days of receiving access"
  4. "We will schedule your 60-minute strategy call when the report is ready"

### Post-Purchase Workflow: "Elevate - Audit Onboarding"

1. **Trigger:** Payment Received (or tag `purchased-audit` for testing)
2. **Immediate:**
   - Add tags: `purchased-audit`, `audit-client`
   - Update custom fields: "Product Purchased" = "Digital Audit", "Purchase Date" = today
   - Create opportunity: Agency Sales Pipeline > "Audit Purchased" stage > $1,500
   - Send confirmation email with receipt and timeline overview
   - Internal notification to the audit team: "New audit purchased: {{contact.business_name}} -- {{contact.website_url}}"
3. **30 minutes after purchase:**
   - Send the credential sharing form email:
     - Subject: "Next Step: Share Your Marketing Access (Secure Form)"
     - Body: Explains what access is needed (Google Analytics, Google Ads, Facebook Business Manager, social media accounts, website admin), provides a secure form link or document, and assures all credentials are handled with strict confidentiality
4. **48 hours -- Credential reminder (if not received):**
   - Add a condition: if tag `credentials-received` does NOT exist, send a gentle reminder
   - "Hey {{contact.first_name}}, just a friendly heads-up -- we need your access credentials to get started on your audit. The sooner we receive them, the sooner you get your report! Here is the form again: [link]"
5. **Day 10 (or when audit is complete) -- Delivery:**
   - This step would be manually triggered by adding a tag `audit-complete` when the team finishes the report
   - Automated email: "Your Digital Audit Is Ready!"
     - Attach or link to the 30-page report
     - "Schedule your 60-minute strategy call to walk through the findings: [calendar booking link]"
     - Move pipeline to "Audit Delivered" stage
6. **After the strategy call -- Retainer upsell sequence:**
   - This is the key revenue moment. The strategy call is where the audit findings become a conversation about ongoing work.
   - Day 1 after call: "Thanks for the great conversation, {{contact.first_name}}. As discussed, here is a summary of the top 3 priorities from your audit."
   - Day 3: "What would it look like if someone handled all of this for you?" -- introduce monthly retainer options ($3,000-$10,000/month depending on scope)
   - Day 7: "Our retainer clients see an average 3.2x ROI within 6 months. Here is how we could work together." -- formal proposal link or scheduling link for a follow-up call
   - Move pipeline to "Proposal Sent" when the retainer offer is sent

### Abandoned Cart for Digital Audit

At $1,500, abandoned carts are common -- this is a significant purchase decision. The recovery sequence should be more consultative and less promotional:

- Email 1 (2 hours -- longer initial wait for B2B): "Still evaluating whether a Digital Audit makes sense for your business? Here are 3 questions to help you decide." (Is your marketing spending growing but results are not? Do you know your actual cost per lead? When did you last get an outside perspective on your marketing?)
- Email 2 (48 hours): Case study email. "How [Company Name] discovered $3,200/month in wasted ad spend." Full case study with before/after metrics and a clear narrative.
- Email 3 (7 days -- much longer for B2B buying cycles): "Would a quick 15-minute call help? Let me walk you through exactly what the audit covers and whether it makes sense for your business." Include a calendar booking link for a short pre-sale call. No discount -- maintain premium positioning.

**Design Challenge:** Compare the three abandoned cart sequences (Sunrise Wellness, BrightSmile, Elevate). Notice how the timing, tone, and incentive strategy change based on price point and buyer type. A $79/month gym membership gets a 72-hour sequence with a coupon. A $1,500 B2B product gets a 7-day sequence with a consultation offer. Why? Because the buying psychology is completely different. The gym buyer needs a nudge. The B2B buyer needs trust.

---

## What You Built Today

You started the day with products defined in a settings menu and a basic funnel page. Now you have a complete e-commerce machine:

- A **membership sales page** that presents, compares, and sells three membership tiers
- An **order form** with embedded checkout, coupon support, and an order bump
- A **post-purchase workflow** that confirms the sale, tags the member, updates the pipeline, and runs a 7-day onboarding sequence
- An **abandoned cart workflow** that recovers lost sales with a 3-email sequence escalating from helpful to incentivized
- A **personalized upsell system** that recommends the right add-on product based on each member's fitness goals

These five components work together as a single system. A stranger can discover Sunrise Wellness, choose a membership, buy it at 11 PM on a Sunday night, get instantly confirmed and onboarded, and receive a personalized upsell within a week -- all without you touching anything.

And for the people who start but do not finish? The abandoned cart workflow follows up three times, removing objections and offering an incentive, before gracefully letting go.

This is what a real e-commerce system looks like inside GHL. Not just a checkout page -- a complete sales and onboarding machine.

---

## Next Day Preview

**Day 15: Client Onboarding & Retention System** -- Today you automated the first 7 days after purchase. Tomorrow you automate the first 90 days and beyond. You will build the complete member lifecycle: 2-week and 30-day check-ins, engagement scoring, churn detection when a member starts slipping, win-back campaigns for cancellations, and a loyalty program that rewards long-term members. If today's system turns strangers into members, tomorrow's system keeps them as members for years.

**Before Day 15, make sure you have:**
- The post-purchase onboarding workflow from today (published and tested)
- The Membership Sales Pipeline with a "Closed - Member" stage (from Day 5)
- The New Member Onboarding Pipeline (from Day 5, if you created one)
- Your community/member portal setup from Day 10 (if applicable)
- Smart Lists from Day 2 (you will create new ones for engagement tracking)
- Custom fields for "Last Visit Date" and "Total Visits" (create these if they do not exist)
- Your email and SMS templates from Day 3

---

*Phase 2 continues with Day 15: Client Onboarding & Retention System*
