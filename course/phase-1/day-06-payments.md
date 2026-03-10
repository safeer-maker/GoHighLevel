# Day 6: Payments & Invoicing

**Time Required:** 3-4 hours
**Certification Alignment:** Invoices (One-Time, Recurring, Auto-Pay), Taxes, Products, Order Forms, Text2Pay, Coupons, Payment Settings, Orders, Subscriptions, Transactions
**API Lab:** Yes - `scripts/day-06-payments-api.py`

---

## Learning Objectives

1. Create and manage products (one-time and recurring)
2. Generate invoices with taxes, discounts, and recurring billing
3. Set up Text2Pay links and coupon codes
4. Navigate Orders, Subscriptions, and Transactions dashboards

---

## Part 1: Products Setup (30 min)

### Theory Recap

Products are the foundation of GHL's payment system. Before creating invoices or order forms, you need products defined. Products can be:
- **One-time:** Single purchase (e.g., consultation fee, setup fee)
- **Recurring:** Subscription-based (e.g., monthly membership, retainer)

### Hands-On Exercise 6.1: Create Products

Navigate to **Payments > Products** (or Products section):

Create these products:

| Product Name | Type | Price | Description |
|-------------|------|-------|-------------|
| Initial Consultation | One-time | $150.00 | 60-minute initial consultation |
| Basic Membership | Recurring/Monthly | $99.00/mo | Basic monthly membership |
| Premium Membership | Recurring/Monthly | $199.00/mo | Premium monthly membership with all features |
| VIP Day Package | One-time | $2,500.00 | Full-day VIP intensive session |
| Setup Fee | One-time | $500.00 | One-time onboarding and setup |
| Annual Plan | Recurring/Yearly | $999.00/yr | Annual membership (discounted) |

For each product:
1. Set the name and description
2. Set the price and billing frequency
3. Add a product image (optional but recommended)
4. Save and note the product ID

### Hands-On Exercise 6.2: Import Products (if applicable)

If GHL supports product import:
1. Prepare a CSV with product data
2. Import products
3. Verify all products imported correctly

---

## Part 2: Invoicing (60 min)

### Hands-On Exercise 6.3: Create a One-Time Invoice

Navigate to **Payments > Invoices > + Create Invoice**:

1. **Select contact:** Choose a test contact
2. **Add line items:**
   - Initial Consultation: $150.00 x 1
   - Setup Fee: $500.00 x 1
3. **Add tax** (Exercise 6.4 below first, then come back)
4. **Set due date:** 7 days from today
5. **Add notes:** "Thank you for choosing our services!"
6. **Set payment terms:** Net 7
7. **Preview** the invoice
8. **Send** the invoice via email

**Observe:** Check the contact's conversation - did they receive the invoice email?

### Hands-On Exercise 6.4: Set Up Taxes

Navigate to **Payments > Settings > Taxes** (or Invoices > Tax Settings):

1. Create a tax rate:
   - Name: "Sales Tax"
   - Rate: 8.25% (or your local rate)
   - Type: Percentage
2. Create a second tax (if applicable):
   - Name: "Service Tax"
   - Rate: 5%
3. Set a default tax for invoices
4. Go back to your invoice and apply the tax

### Hands-On Exercise 6.5: Create a Recurring Invoice (Auto-Pay)

1. Create a new invoice
2. Select a contact
3. Add line item: "Premium Membership - $199.00/mo"
4. Enable **Recurring/Auto-Pay:**
   - Billing frequency: Monthly
   - Start date: Today
   - End date: None (ongoing) or set a term (12 months)
5. Send the invoice
6. Verify the recurring schedule is set up correctly

### Hands-On Exercise 6.6: Invoice Management

1. View all invoices in the Invoices list
2. Filter by status: Draft, Sent, Paid, Overdue, Void
3. Open a sent invoice:
   - Check if the client has viewed it
   - Record a manual payment (mark as paid)
   - Void an invoice
4. Resend an unpaid invoice with a reminder message

---

## Part 3: Text2Pay (30 min)

### Theory Recap

Text2Pay sends a payment link via SMS. The customer clicks the link, enters their card info, and pays - all from their phone. Great for:
- Service-based businesses (pay after service)
- Quick invoicing without email
- Mobile-first customers

### Hands-On Exercise 6.7: Send a Text2Pay Link

Navigate to **Payments > Text2Pay** (or create from Invoices):

1. Select a contact
2. Set the amount: $150.00
3. Add a description: "Initial Consultation - Jan 2024"
4. Choose products or enter custom amount
5. Send the Text2Pay SMS
6. Check the contact's conversation for the payment link
7. Click the link yourself (in incognito) to see the payment page
8. Review the payment page appearance and branding

---

## Part 4: Coupons & Discounts (20 min)

### Hands-On Exercise 6.8: Create Coupons

Navigate to **Payments > Coupons** (or Marketing > Coupons):

Create these coupons:

| Coupon Code | Type | Value | Restrictions |
|------------|------|-------|-------------|
| WELCOME20 | Percentage | 20% off | First-time customers only, single use |
| SAVE50 | Fixed Amount | $50 off | Orders over $200, unlimited uses |
| ANNUAL10 | Percentage | 10% off | Annual plans only, expires in 30 days |
| VIPFRIEND | Percentage | 15% off | Referral coupon, 50 total uses |

For each coupon:
1. Set the code, type, and value
2. Configure restrictions (minimum order, specific products, expiry date)
3. Set usage limits (per customer, total)
4. Test the coupon on an order form or invoice

### Hands-On Exercise 6.9: Apply Coupon to an Invoice

1. Create a new invoice with a VIP Day Package ($2,500)
2. Apply the WELCOME20 coupon
3. Verify the discount is calculated correctly ($2,500 - 20% = $2,000)
4. Add tax to the discounted amount
5. Review the final total

---

## Part 5: Order Forms & Funnel Integration (30 min)

### Hands-On Exercise 6.10: Add Product to a Funnel Order Form

Navigate to **Sites > Funnels** (you'll create a full funnel on Day 8, but let's preview):

1. Create a simple funnel page or find an existing one
2. Add an **Order Form** element to the page
3. Connect a product to the order form:
   - Select "Basic Membership - $99/mo"
   - Configure the checkout form fields
   - Add the coupon field (allow coupon entry)
4. Preview the page and test the order form flow
5. **Payment processor note:** If Stripe/PayPal is connected, test a payment in test mode. If no payment processor is connected, you can still build the entire order form - it just won't process actual payments. Explore Settings > Payments to see integration options and understand what's required.

---

## Part 6: Payment Dashboards (20 min)

### Hands-On Exercise 6.11: Review Payment Dashboards

Navigate to **Payments** and explore each tab:

**Orders:**
- View all completed orders
- Filter by date range, product, status
- Check order details (products, customer, payment method)

**Subscriptions:**
- View active subscriptions
- Check subscription status (active, paused, cancelled)
- Understand subscription management options

**Transactions:**
- View all payment transactions
- Filter by type (charge, refund, failed)
- Understand transaction details (amount, fee, net)

### Hands-On Exercise 6.12: Payment Settings

Navigate to **Payments > Settings** (or Settings > Payments):

1. Review payment processor integration (Stripe, PayPal, etc.)
2. Check business information (appears on receipts)
3. Review notification settings (payment received, failed, refunded)
4. Understand currency settings
5. Check payout schedule (when you receive the money)

---

## Part 7: API Lab - Payment Operations

```bash
python scripts/day-06-payments-api.py
```

The script covers:
1. List products
2. Create an invoice via API
3. Get invoice details and status
4. List transactions

---

## Case Scenarios

### Case Scenario 1: Coaching Business Setup

**Situation:** "Elevate Coaching" offers:
- VIP Day: $5,000 (one-time, includes lunch and materials)
- Group Coaching: $497/month (recurring, 6-month minimum)
- 1-on-1 Coaching: $997/month (recurring, 3-month minimum)
- Strategy Session: $250 (one-time consultation)
- Course Access: $1,997 (one-time, lifetime access)

**Your Task:**
1. Create all 5 products with correct pricing
2. Create a coupon: "EARLYBIRD" - 20% off, valid for next 14 days, applies to Group and 1-on-1 only
3. Create an invoice for a client:
   - 1-on-1 Coaching setup: $997/mo recurring
   - Strategy Session: $250 one-time
   - Apply EARLYBIRD coupon to the coaching line
   - Add 8% tax
4. Calculate the first invoice total manually and verify against GHL
5. Send the invoice and send a Text2Pay as backup

### Case Scenario 2: Landscaping Company

**Situation:** "Green Thumb Landscaping" provides:
- Lawn Mowing: $75/visit
- Full Service (mow + edge + blow): $125/visit
- Weekly Maintenance Contract: $400/month
- One-time Cleanup: $500-$2,000 (variable)
- Spring/Fall Aeration: $250

**Your Task:**
1. Create products for standard services
2. After a job, send a Text2Pay to the customer for $125 (Full Service)
3. Set up a recurring invoice for a Weekly Maintenance client ($400/mo)
4. Create a coupon: "NEIGHBOR" - $25 off first service (for referrals)
5. Design the payment flow: How does the crew mark a job done and trigger payment?

### Case Scenario 3: Multi-Product Invoice

**Situation:** A client is purchasing a bundled package:
- VIP Day Package: $2,500
- 3 months of Premium Membership: $199/mo x 3 = $597
- Setup Fee: $500
- Coupon: VIPFRIEND (15% off total)
- Tax: 8.25%

**Your Task:**
1. Create the invoice with all line items
2. Apply the coupon
3. Calculate the expected total:
   - Subtotal: $3,597
   - Discount (15%): -$539.55
   - After discount: $3,057.45
   - Tax (8.25%): $252.24
   - **Total: $3,309.69**
4. Verify your calculation matches GHL
5. Send the invoice and document the experience

---

## Day 6 Recap Questions

1. What's the difference between a one-time product and a recurring product?
2. How do you set up auto-pay for a recurring invoice?
3. What is Text2Pay and when would you use it instead of a regular invoice?
4. How do coupon restrictions work (usage limits, minimum order, product-specific)?
5. Where do you view all transactions and their statuses?
6. A client says "my payment failed." Where do you look in GHL to investigate?

---

## Next Day Preview

**Day 7: Marketing - Email Campaigns** - You'll build email templates, launch campaigns to Smart Lists, set up trigger links, and use the API for marketing automation.
