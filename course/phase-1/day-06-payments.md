# Day 6: Payments & Invoicing

**Time Required:** 3-4 hours
**Certification Alignment:** Invoices (One-Time, Recurring, Auto-Pay), Taxes, Products, Order Forms, Text2Pay, Coupons, Payment Settings, Orders, Subscriptions, Transactions
**API Lab:** Yes - `scripts/day-06-payments-api.py`

---

## Today's Mission

Sunrise Wellness Studio has leads flowing through the pipeline (Day 5), but none of that matters if the studio cannot collect money. Today you will build the entire payment infrastructure for the studio: every product the business sells (memberships, sessions, supplements, packages), invoices for collecting payments, coupons for promotions, and Text2Pay for sending payment links via SMS.

Here is the real-world scenario: David Kim just moved to "Closed - Member" in your sales pipeline yesterday. He chose the Premium membership at $149/mo. You need to charge him an activation fee, his first month's membership, and he wants to grab the Protein Starter Kit. That means you need products created, an invoice built, and a way to send it to him. That is what today is all about.

**Important note about Stripe:** Many of today's exercises involve creating products, invoices, and payment structures. If you do not have Stripe (or another payment processor) connected to your sub-account, you can still complete almost everything. You will build all the products, invoices, and coupons -- they just will not process live payments. The infrastructure will be fully ready for when a payment processor is connected. Exercises that specifically require Stripe will be clearly marked.

---

## Learning Objectives

1. Understand the GHL payment ecosystem: products, invoices, coupons, and payment links
2. Create all Sunrise Wellness products (one-time and recurring)
3. Build and send invoices (one-time and recurring)
4. Configure sales tax
5. Set up promotional coupons tied to the studio's marketing offers
6. Explore Text2Pay for mobile-first payment collection
7. Navigate the Orders, Subscriptions, and Transactions dashboards

---

## Part 1: Products (40 min)

### What is a Product?

A **product** in GHL is anything your business sells that has a price attached to it. It is the foundational building block of the entire payment system -- before you can create an invoice, order form, or payment link, you need products defined.

Think of it like a restaurant menu. Before a waiter can take an order, the menu needs to exist with items and prices listed. Products are your menu.

Products come in two types:

- **One-time products** -- The customer pays once and the transaction is complete. Examples: a single PT session, a supplement purchase, a setup fee.
- **Recurring products** -- The customer pays on a schedule (monthly, yearly, weekly) until they cancel. Examples: a monthly membership, an annual plan.

### Why Set Up Products First?

Products are referenced everywhere in GHL:
- **Invoices** pull from your product list
- **Order forms** on funnels and websites display your products
- **Text2Pay links** can include specific products
- **Coupons** can be restricted to specific products
- **Subscription management** tracks recurring products

If you skip product setup and manually type prices into invoices, you will have inconsistent pricing, no reporting by product, and no way to attach coupons. Define your products once, use them everywhere.

### Hands-On Exercise 6.1: Create All Sunrise Wellness Products

*This exercise teaches you to set up a complete product catalog for a business.*

Navigate to **Payments > Products** and click **+ Add Product** (or **Create Product**).

You will create 10 products. For each one, follow these steps:
1. Enter the **product name**
2. Set the **price** and **billing type** (one-time or recurring)
3. For recurring products, set the **billing interval** (monthly, yearly)
4. Add a **description** that explains what the customer is buying
5. Optionally upload a **product image**
6. Save the product

**Recurring Products (Memberships):**

| Product Name | Price | Type | Billing Interval | Description |
|-------------|-------|------|------------------|-------------|
| Free Trial - 7 Day Pass | $0.00 | One-time | N/A | Complimentary 7-day access to all classes and facilities. No payment required. |
| Basic Membership | $79.00 | Recurring | Monthly | Access to all group fitness classes (HIIT, Yoga, Pilates). Mon-Sat during studio hours. |
| Premium Membership | $149.00 | Recurring | Monthly | Everything in Basic plus 2 PT sessions/month and priority class booking. |
| VIP Membership | $249.00 | Recurring | Monthly | Unlimited everything: all classes, unlimited PT, nutrition coaching, guest passes, and retail discounts. |
| Annual Plan | $790.00 | Recurring | Yearly | Full Premium access billed annually. Save over $1,000 compared to monthly Premium pricing. |

**One-Time Products (Services & Retail):**

| Product Name | Price | Type | Description |
|-------------|-------|------|-------------|
| PT Session - Single | $75.00 | One-time | One 60-minute Personal Training session with a certified trainer. |
| 10-Class Pack | $120.00 | One-time | Pack of 10 group fitness class credits. Use for any class (HIIT, Yoga, Pilates). No expiration. |
| Nutrition Plan | $200.00 | One-time | Personalized nutrition plan including initial consultation, meal plan, and 2-week follow-up. |
| Protein Starter Kit | $45.00 | One-time | Starter kit with protein powder, shaker bottle, and sample supplements. |
| Setup / Activation Fee | $25.00 | One-time | One-time account activation and orientation fee for new members. |

**After creating all 10 products:**
1. View your complete product list -- all 10 should appear
2. Verify the pricing is correct for each one
3. Check that recurring products show the correct billing interval
4. Note how GHL organizes products -- this list is what you will pull from when creating invoices and order forms

> **Pro Tip:** The Free Trial at $0 might seem unnecessary as a product, but creating it serves a purpose. It allows you to track trial sign-ups in the Orders dashboard, attach it to order forms, and run reports on how many trials convert to paid memberships. A $0 product is still a product.

---

## Part 2: Invoicing (60 min)

### What is an Invoice?

An **invoice** is a formal payment request you send to a customer. It lists what they owe, the amounts, any taxes or discounts, and provides a way for them to pay (usually a link to an online payment page).

In GHL, invoices can be:
- **One-time** -- A single bill for specific products/services (e.g., "Here is your bill for the PT session and Protein Kit")
- **Recurring** -- An automatic repeating charge (e.g., "$149/mo for Premium Membership, charged on the 1st of every month")

Think of a one-time invoice like a restaurant bill (you pay once and you are done), and a recurring invoice like a utility bill (it shows up every month automatically).

### Why Use Invoices Instead of Just Charging People?

Invoices create a paper trail. They are professional, trackable, and give the customer a clear breakdown of what they are paying for. They also:
- Show up in the customer's conversation history (Day 3)
- Can be tracked by status (Draft, Sent, Viewed, Paid, Overdue, Void)
- Generate records in the Transactions dashboard
- Can include taxes, discounts, and multiple line items

### Hands-On Exercise 6.2: Create a One-Time Invoice for a New VIP Member

*This exercise teaches you to build a multi-line invoice with different products.*

**Scenario:** David Kim just signed up for VIP membership. His first invoice includes the activation fee, first month's VIP membership, and the Protein Starter Kit he wants to purchase.

Navigate to **Payments > Invoices** and click **+ Create Invoice**.

**Step 1: Select the contact**
- Search for David Kim (or whichever contact you used for the "Closed - Member" opportunity in Day 5)

**Step 2: Add line items**
Click "Add Item" and select from your product catalog:

| Line Item | Qty | Price | Subtotal |
|-----------|-----|-------|----------|
| Setup / Activation Fee | 1 | $25.00 | $25.00 |
| VIP Membership (first month) | 1 | $249.00 | $249.00 |
| Protein Starter Kit | 1 | $45.00 | $45.00 |

**Step 3: Review the subtotal**
- Subtotal should be: **$319.00**

**Step 4: Set invoice details**
- **Due date:** 7 days from today
- **Notes to customer:** "Welcome to Sunrise Wellness Studio, David! This invoice covers your activation fee, first month of VIP membership, and the Protein Starter Kit. We are excited to have you on board!"
- **Payment terms:** Net 7

**Step 5: Preview the invoice**
- Click Preview to see how it will look to David
- Verify all line items, amounts, and totals are correct

**Step 6: Send the invoice**
- Send via email
- Check David's conversation record in GHL -- the invoice email should appear in his timeline

> **Pro Tip:** If you do not have a payment processor connected, the invoice will still be created and can be sent, but the customer will not be able to pay online. They would need to pay in person or via another method, and you would manually mark the invoice as paid.

### Hands-On Exercise 6.3: Create a Recurring Invoice

*This exercise teaches you to set up automatic monthly billing.*

**Scenario:** Priya Sharma (from your onboarding pipeline) has a Premium membership at $149/mo. She needs a recurring invoice that charges her automatically every month.

Navigate to **Payments > Invoices > + Create Invoice**.

1. **Select contact:** Priya Sharma
2. **Add line item:** Premium Membership - $149.00
3. **Enable Recurring / Auto-Pay:**
   - **Billing frequency:** Monthly
   - **Start date:** Today (or the 1st of the month)
   - **End date:** Leave blank for ongoing (or set to 12 months if you want a fixed term)
4. **Send the invoice**
5. **Verify:** Check that the recurring schedule appears correctly -- GHL should show the next billing date

**Understanding recurring invoice behavior:**
- The first invoice is sent immediately (or on the start date)
- Subsequent invoices are generated and sent automatically on the billing cycle
- If a payment fails, GHL tracks it as "Failed" and can retry
- The customer can cancel or you can void the recurring invoice to stop future charges

### Hands-On Exercise 6.4: Invoice Management

*This exercise teaches you to handle the day-to-day administration of invoices.*

Go to **Payments > Invoices** and explore the invoice list:

1. **Filter by status** -- Click the status filters to view:
   - **Draft** -- Created but not yet sent (still editable)
   - **Sent** -- Delivered to the customer, awaiting payment
   - **Viewed** -- The customer opened the invoice email or clicked the payment link
   - **Paid** -- Payment received (automatically marked if processor is connected, or manually marked)
   - **Overdue** -- Past the due date and still unpaid
   - **Void** -- Cancelled invoice (use this if an invoice was sent in error)

2. **Record a manual payment** -- Open David's invoice and mark it as "Paid" manually. This is how you handle cash, check, or in-person card payments that do not go through GHL's online payment system.

3. **Void an invoice** -- Create a test invoice, then void it. Note how voided invoices remain in the system for record-keeping but are clearly marked as void.

4. **Resend an invoice** -- Open Priya's invoice and click "Resend." Add a note: "Friendly reminder -- your Premium membership invoice is ready for payment!" This is useful for overdue invoices.

---

## Part 3: Taxes (15 min)

### What Are Taxes in GHL?

If your business is required to collect sales tax (most are, depending on your state/country and what you sell), GHL lets you define tax rates and apply them to invoices and products. This ensures every invoice automatically calculates the correct tax amount.

### Why Set This Up?

Without tax configuration, you would need to manually calculate tax for every invoice -- error-prone and time-consuming. Setting it up once means every future invoice automatically includes the correct tax.

### Hands-On Exercise 6.5: Configure Sales Tax

*This exercise teaches you to set up tax rates that auto-apply to invoices.*

Navigate to **Payments > Settings > Taxes** (or look for Tax Settings within the Invoices section):

1. **Create a tax rate:**
   - **Name:** "Sales Tax"
   - **Rate:** 8.25% (or use your actual local rate)
   - **Type:** Percentage
   - Save the tax rate

2. **Set as default** (if the option exists) -- This auto-applies the tax to new invoices so you do not have to add it manually each time.

3. **Apply tax to David's invoice:**
   - Go back to David's invoice (or create a new test invoice)
   - Apply the Sales Tax to the line items
   - Verify the calculation:
     - Subtotal: $319.00
     - Tax (8.25%): $26.32
     - **Total: $345.32**

> **Pro Tip:** Not all products may be taxable. In many jurisdictions, services (like PT sessions) are taxed differently from physical goods (like the Protein Starter Kit). Check your local tax laws. GHL allows you to apply tax selectively per line item if needed.

---

## Part 4: Text2Pay (20 min)

### What is Text2Pay?

**Text2Pay** is exactly what it sounds like: you send a payment link via text message (SMS), and the customer taps the link on their phone, enters their card info, and pays. Done.

Think of it like Venmo or Cash App, but professional and tied to your business. The customer does not need to download anything -- they just tap a link in a text message.

### Why Use Text2Pay?

- **Speed** -- Faster than emailing an invoice. The customer pays in 30 seconds from their phone.
- **Higher payment rates** -- People open texts faster than emails (98% open rate for SMS vs. ~20% for email).
- **Perfect for in-the-moment charges** -- A member just finished a PT session? Text them the payment link before they leave the parking lot.
- **Mobile-first customers** -- Many Sunrise Wellness members are active, on-the-go people who live on their phones.

### Hands-On Exercise 6.6: Send a Text2Pay Link

*This exercise teaches you to create and send a mobile payment link. If you do not have a phone number configured in your sub-account, read through the steps to understand the process -- you will still learn the concept.*

**Scenario:** James Rodriguez just completed a drop-in PT session ($75). Instead of making him wait at the front desk, you text him a payment link.

Navigate to **Payments > Text2Pay** (or create one from the contact's conversation):

1. **Select the contact:** James Rodriguez
2. **Set the amount:** $75.00
3. **Select the product:** PT Session - Single (from your product catalog)
4. **Add a description:** "Personal Training Session - [today's date]"
5. **Send the Text2Pay SMS**
6. **Check the contact's conversation** -- the payment link message should appear in the SMS thread
7. If possible, **open the payment link** in an incognito browser to see the payment page from the customer's perspective. Note the branding, amount, and payment form.

**When to use Text2Pay vs. Invoice:**

| Situation | Use Text2Pay | Use Invoice |
|-----------|-------------|-------------|
| Quick, simple payment (one item) | Yes | Overkill |
| Multiple line items with breakdown | No | Yes |
| Need a formal document for records | No | Yes |
| Customer prefers mobile/SMS | Yes | Maybe also |
| Recurring monthly charges | No | Yes (recurring) |
| After an in-person service | Yes | Too slow |

> **Pro Tip:** Text2Pay is perfect for Sunrise Wellness's drop-in services. PT sessions, single class purchases, and retail product sales can all be collected via Text2Pay right after the service is delivered. No awkward "please check your email" -- just a quick text.

---

## Part 5: Coupons & Promotions (25 min)

### What is a Coupon?

A **coupon** (also called a discount code or promo code) is a code that customers enter to receive a discount on their purchase. In GHL, coupons can offer percentage discounts or fixed dollar amounts, and they can be restricted to specific products, usage limits, and expiration dates.

### Why Do You Need Coupons?

Coupons drive specific business behaviors:
- **Acquire new members** -- "20% off your first month" lowers the barrier to sign up
- **Reward referrals** -- "Free PT session for referring a friend" incentivizes word-of-mouth
- **Reduce price sensitivity** -- "10% off annual plan" nudges people toward a higher-commitment (and higher-value) plan
- **Re-engage lapsed leads** -- "$20 off first month for trial members" converts people sitting in the "Closed - Not Now" stage

### Hands-On Exercise 6.7: Create Sunrise Wellness Coupons

*This exercise teaches you to create coupons with different discount types and restrictions.*

Navigate to **Payments > Coupons** and click **+ Create Coupon** (or **Add Coupon**).

Create these 4 coupons:

**Coupon 1: WELCOME20**

| Setting | Value |
|---------|-------|
| **Code** | WELCOME20 |
| **Discount type** | Percentage |
| **Discount value** | 20% |
| **Applies to** | All membership products (Basic, Premium, VIP) |
| **Usage limit per customer** | 1 (single use) |
| **Total usage limit** | Unlimited |
| **Expiration** | None (always available) |
| **Description** | 20% off your first month -- our standard welcome offer |

This is the coupon that matches the `{{offer.discount}}` custom value you created on Day 1. When the studio runs a "20% Off Your First Month" campaign, this is the code customers use.

**Coupon 2: REFERRAL**

| Setting | Value |
|---------|-------|
| **Code** | REFERRAL |
| **Discount type** | Fixed amount |
| **Discount value** | $75.00 |
| **Applies to** | PT Session - Single only |
| **Usage limit per customer** | 1 |
| **Total usage limit** | Unlimited |
| **Expiration** | None |
| **Description** | Free PT session for members who refer a new member |

This ties into a referral program: when a current member refers someone who signs up, the referring member gets a free PT session. The coupon covers the full $75 cost.

**Coupon 3: ANNUAL10**

| Setting | Value |
|---------|-------|
| **Code** | ANNUAL10 |
| **Discount type** | Percentage |
| **Discount value** | 10% |
| **Applies to** | Annual Plan only |
| **Usage limit per customer** | 1 |
| **Total usage limit** | 50 (limited promotion) |
| **Expiration** | 30 days from today |
| **Description** | 10% off the annual plan -- limited-time promotion to drive annual commitments |

The Annual Plan is already a great deal ($790/yr vs. $1,788/yr for monthly Premium). This coupon stacks an extra 10% to create urgency during a promotional period.

**Coupon 4: TRIALCONVERT**

| Setting | Value |
|---------|-------|
| **Code** | TRIALCONVERT |
| **Discount type** | Fixed amount |
| **Discount value** | $20.00 |
| **Applies to** | Basic Membership, Premium Membership, VIP Membership |
| **Usage limit per customer** | 1 |
| **Total usage limit** | Unlimited |
| **Expiration** | None |
| **Description** | $20 off first month for members converting from a free trial |

This coupon is specifically for people in the "Trial Follow-Up" stage of your pipeline. When you are trying to convert Emma Thompson or James Rodriguez from their trial to a paid membership, offering $20 off the first month can tip the decision.

**After creating all 4 coupons:**
1. Review your coupon list -- all 4 should appear with their codes, discount values, and statuses
2. Verify the restrictions are set correctly (product-specific, usage limits, expiration)
3. Test a coupon: create a test invoice, add a membership product, and apply the WELCOME20 coupon to see the discount calculate correctly

> **Pro Tip:** Track coupon usage over time. If WELCOME20 is used 100 times but ANNUAL10 is used 3 times, that tells you the annual promotion needs better visibility or a bigger discount. Coupons are not just discounts -- they are data.

---

## Part 6: Order Forms Preview (15 min)

### What is an Order Form?

An **order form** is an embedded checkout experience on a website or funnel page. Instead of sending an invoice to a specific person, an order form is public-facing -- anyone who visits the page can purchase.

Think of invoices as "you go to the customer" and order forms as "the customer comes to you."

### Why Does This Matter?

On Day 8 (Sites & Funnels), you will build full funnel pages with embedded order forms for Sunrise Wellness. Today is a preview so you understand how products connect to order forms.

### Hands-On Exercise 6.8: Preview Order Form Setup

*This exercise gives you a preview of how products connect to funnels. You will build the full funnel on Day 8.*

Navigate to **Sites > Funnels** (or **Funnels** in the left sidebar):

1. **Create a simple test funnel** (or open an existing one if available)
2. Look for the **Order Form** element in the page builder
3. If you can add one, connect it to a product:
   - Select "Basic Membership - $79/mo"
   - Note how the price, name, and billing type auto-populate from your product catalog
   - Toggle the "Coupon" field on -- this allows visitors to enter a coupon code at checkout
4. **Preview the page** to see the checkout form from the customer's perspective
5. **Do not publish** -- this is just a preview for today. You will build the real funnel on Day 8.

**Key takeaway:** This is why you created products first. The order form pulls from your product catalog. If you had not defined your products, you would have to manually enter pricing on every order form, which creates inconsistency and errors.

> **Pro Tip:** If you do not have a payment processor connected, the order form will display correctly but will not process payments. You can still build and preview the entire checkout experience. Connect Stripe later and it works immediately because the infrastructure is already built.

---

## Part 7: Payment Dashboards (20 min)

### What Are the Payment Dashboards?

GHL provides three dashboards that give you visibility into all payment activity. Think of them as three different lenses for viewing the same financial data:

- **Orders** -- Individual purchases (who bought what, when, and for how much)
- **Subscriptions** -- Recurring payment tracking (who is on a monthly plan, is it active or cancelled)
- **Transactions** -- Raw payment records (charges, refunds, failures -- the bank-level view)

### Why Do These Matter?

Without dashboards, you would need to log into Stripe (or your payment processor) separately to check payment status. GHL centralizes this so you can see everything alongside your contacts, conversations, and pipeline data.

### Hands-On Exercise 6.9: Explore the Payment Dashboards

*This exercise teaches you to navigate the three payment views and understand what each one shows.*

Navigate to **Payments** and explore each tab:

**Orders Tab:**
- View all completed orders (if you have any from test payments)
- Filter by date range, product, and status
- Click into an order to see: which products were purchased, the customer, payment method, and timestamp
- In production, this is where the front desk would check if a member's payment went through

**Subscriptions Tab:**
- View all active subscriptions (recurring invoices you created show up here)
- Check subscription statuses:
  - **Active** -- Payments are current, membership is running
  - **Paused** -- Member requested a temporary hold (e.g., vacation, injury)
  - **Cancelled** -- Member cancelled, no more charges
  - **Past Due** -- Payment failed, needs attention
- This tab answers the question: "How many paying members do we have right now?"

**Transactions Tab:**
- View all payment transactions at the raw level
- Filter by type:
  - **Charge** -- Successful payment collected
  - **Refund** -- Money returned to customer
  - **Failed** -- Payment attempt that did not go through
- Each transaction shows: amount, processing fee, net amount received, and date
- This tab answers the question: "How much money actually came in today/this week/this month?"

### Hands-On Exercise 6.10: Payment Settings Review

*This exercise teaches you to configure the business-level payment settings.*

Navigate to **Payments > Settings** (or **Settings > Payments**):

1. **Payment processor integration** -- Check if Stripe, PayPal, or another processor is connected. If not, review what is required to connect one. (You do not need to connect one for this course.)
2. **Business information** -- Verify the business name and details that appear on receipts and invoices. This should match the Sunrise Wellness Studio branding from Day 1.
3. **Notification settings** -- Configure who gets notified when:
   - A payment is received (the owner wants to know)
   - A payment fails (someone needs to follow up)
   - A refund is issued
4. **Currency settings** -- Verify the correct currency is set (USD, or your local currency)

---

## Part 8: API Lab - Payment Operations

### Run the Payments API Lab

```bash
python scripts/day-06-payments-api.py
```

The script covers:
1. List all products in your sub-account
2. Create an invoice via API
3. Get invoice details and status
4. List transactions

### API Exercises

1. **Invoice generator** -- Build a script that creates a "New Member Welcome Invoice" given a contact ID and membership type. It should automatically add the activation fee + first month's membership + Protein Starter Kit and calculate the total.

2. **Subscription monitor** -- Write a function that lists all active subscriptions and flags any that are past due. This is the kind of script the studio owner would run weekly.

3. **Revenue report** -- Create a script that pulls all transactions for the current month and calculates: total revenue, number of transactions, average transaction value, and total refunds.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental - Patient Billing

**Situation:** BrightSmile Dental Clinic (2 dentists, 1 hygienist, 1 front desk) needs to set up their payment infrastructure. Dental billing is different from fitness: it involves per-procedure pricing, insurance copays, and payment plans for expensive treatments.

**Your Task:**

**1. Create BrightSmile's products:**

| Product Name | Price | Type | Description |
|-------------|-------|------|-------------|
| Dental Exam | $200 | One-time | Comprehensive dental examination with X-rays |
| Professional Cleaning | $150 | One-time | Dental hygienist cleaning and polishing |
| Teeth Whitening Package | $450 | One-time | Professional in-office whitening treatment (2 sessions) |
| Crown / Cap | $1,200 | One-time | Porcelain crown restoration per tooth |
| Emergency Visit | $300 | One-time | Same-day emergency dental assessment and initial treatment |

**2. Create an invoice for a whitening patient with insurance:**

Maria Garcia (from the Day 5 dental pipeline) wants the Whitening Package. Her insurance covers 50% of cosmetic procedures.

| Line Item | Amount |
|-----------|--------|
| Teeth Whitening Package | $450.00 |
| Insurance Adjustment (50% covered) | -$225.00 |
| **Patient Responsibility** | **$225.00** |

Create this invoice, noting how you handle the insurance adjustment. (GHL does not have a native insurance module -- you would add a negative line item or manually adjust the amount.)

**3. Create a payment plan for orthodontics:**

Bob Wilson needs full orthodontics at $4,500. He cannot pay that in one lump sum. Design a payment plan:
- **Option:** $375/mo for 12 months
- Create a recurring invoice for $375/mo
- Add a note to the invoice: "Orthodontic treatment plan -- month [X] of 12"
- How would you track whether Bob has completed all 12 payments?

**Reflection questions:**
- How does dental billing differ from fitness billing? (Hint: insurance, per-procedure vs. subscription, payment plans)
- Why might a dental clinic need both invoices AND Text2Pay? (Think: routine billing vs. after an emergency visit)

---

### Case Scenario 2: Elevate Digital Agency - Client Invoicing

**Situation:** Elevate Digital Agency needs to set up billing for their clients. Agency billing typically involves monthly retainers (recurring), one-time project fees, and setup costs for new clients.

**Your Task:**

**1. Create Elevate Digital's products:**

| Product Name | Price | Type | Billing | Description |
|-------------|-------|------|---------|-------------|
| SEO Retainer | $3,000 | Recurring | Monthly | Monthly SEO management: keyword research, content optimization, link building, reporting |
| PPC Management | $4,000 | Recurring | Monthly | Google Ads + Meta Ads management, optimization, and monthly reporting |
| Social Media Management | $2,000 | Recurring | Monthly | Content creation, scheduling, engagement, and analytics for 3 platforms |
| Website Build | $8,000 | One-time | N/A | Custom website design and development (WordPress or Shopify) |
| Brand Audit | $1,500 | One-time | N/A | Comprehensive brand positioning, competitor analysis, and strategy report |

**2. Create a new client onboarding invoice:**

FitGear Online (from the Day 5 agency pipeline) just signed a PPC management contract. Their first invoice includes:

| Line Item | Amount |
|-----------|--------|
| Brand Audit (one-time onboarding) | $1,500.00 |
| PPC Management - First Month | $4,000.00 |
| **Total** | **$5,500.00** |

After the first invoice, set up a recurring invoice for $4,000/mo for the ongoing PPC management.

**3. Create a referral partner coupon:**

| Setting | Value |
|---------|-------|
| **Code** | PARTNER |
| **Discount type** | Percentage |
| **Discount value** | 15% |
| **Applies to** | All one-time products (Website Build, Brand Audit) |
| **Usage limit per customer** | 1 |
| **Total usage limit** | 20 |
| **Expiration** | 90 days from today |
| **Description** | 15% off project fees for clients referred by agency partners |

**Reflection questions:**
- Elevate Digital sends invoices to businesses (B2B), not individuals. How might invoice formatting and payment terms differ? (Hint: Net 30 vs. Net 7, purchase order numbers, company name on invoice)
- Would Text2Pay make sense for an agency? Why or why not? (Think: $4,000/mo charges via text vs. formal invoice)
- How would you handle a client who wants to pay for 3 months upfront at a discount?

---

## Day 6 Recap Questions

1. What is the difference between a one-time product and a recurring product? Give one Sunrise Wellness example of each.
2. When would you use Text2Pay instead of a formal invoice? Give a specific Sunrise Wellness scenario.
3. You created 4 coupons today. Which one specifically targets people in the "Trial Follow-Up" pipeline stage, and why is that strategically important?
4. A member says "my payment failed." Walk through the steps you would take in GHL to investigate (which dashboard, what to look for, what actions to take).
5. Why did we create the Setup / Activation Fee as a separate $25 product instead of just adding $25 to the first month's membership price?
6. How do the products you created today connect to the order forms you will build on Day 8?

---

## Next Day Preview

**Day 7: Marketing - Email Campaigns** -- You will build email campaigns, send them to the Smart Lists you created on Day 2, set up trigger links for tracking engagement, and learn how marketing connects to your pipeline. The WELCOME20 coupon you created today will feature in your first promotional email campaign.

Make sure you have:
- All 10 products created with correct pricing and billing types
- At least 2 invoices created (one-time and recurring)
- All 4 coupons configured and tested
- Sales tax set up and applied to at least one invoice
- A clear understanding of the Orders, Subscriptions, and Transactions dashboards
