# Day 24: Admin Certification Review - Agency Features

**Time Required:** 3-4 hours
**Cert Focus:** Agency Dashboard, Phone System, Email System, User Management, White-Label, Compliance

## Today's Mission
The HighLevel Admin Certification tests knowledge of agency-level features. Even though you practice on a single sub-account, cert questions ask about agency-level controls. Today you review every agency feature, understand the "why" behind each, and take 25+ practice questions to identify gaps.

## Certification Topics Covered Today
- Agency Dashboard overview
- LC Phone (Lead Connector Phone) setup
- A2P 10DLC registration
- Email system: shared vs dedicated IP
- Agency users vs sub-account users
- Multi-sub-account access and permissions
- White-label configuration
- Snapshots
- GDPR compliance
- HIPAA compliance (BAA requirements)
- CAN-SPAM Act

---

## Part 1: Agency Dashboard (30 min)

### Agency vs Sub-Account View

**Agency admins see:**
- All sub-accounts in one view
- Agency-level KPIs (total revenue, accounts, users)
- Snapshots library
- White-label settings
- Agency billing (what clients pay you)
- Agency-level audit logs

**Sub-account users see (what you see):**
- Their single sub-account
- Sub-account KPIs only
- No agency settings access

### Snapshots

**What:** Templates that save an entire sub-account configuration.

**Use case:** Onboarded 10 dental clinics? Build once, snapshot it, apply to each new dental client.

**What gets saved:**
- Pipelines, stages
- Workflows, templates
- Custom fields, folders
- Products, coupons
- Funnels and websites
- Calendar settings (not appointments)

**What does NOT save:**
- Contacts (for privacy)
- Real data (transactions, conversations)
- API keys and integrations
- Phone numbers

### Exercise 24.1: Document What You CAN'T See

Write down:
- "Agency Dashboard" location: ___ (I cannot access)
- Snapshots menu: ___ (I cannot access)
- Multi-sub-account switcher: ___ (I cannot access)

Understanding that these exist at the agency level is certification-critical.

---

## Part 2: LC Phone System (45 min)

### What Is LC Phone?

**Lead Connector Phone** is GHL's Twilio-based phone system. It provides:
- Phone numbers (local, toll-free, vanity)
- Two-way SMS
- Voice calling
- Call recording
- Voicemail drops
- Missed call text back
- Power dialer (advanced)

### A2P 10DLC - MUST MEMORIZE

**A2P 10DLC = Application-to-Person 10-Digit Long Code**

**What:** Regulatory framework for US businesses sending SMS.

**When required:** ALL US businesses sending SMS from standard phone numbers (since June 2023).

**Why:** Carriers (AT&T, Verizon, T-Mobile) require registration to prevent spam.

**Two parts to register:**
1. **Brand Registration** - who your business is
2. **Campaign Registration** - what types of SMS you'll send (Marketing, Customer Care, 2FA, etc.)

**Fees:** One-time brand fee + per-campaign monthly fee (passed through from GHL to agency to client)

**Consequences of not registering:**
- Messages filtered to spam
- Phone numbers suspended
- Carrier violations and fines

### Trust Center

Where A2P 10DLC registration lives in GHL:
- Agency level: Agency Trust Center
- Sub-account level: Sub-Account Trust Center
- Each sub-account must register separately

### Phone Number Types

| Type | When to Use | Example |
|------|------------|---------|
| **Local** | Local business, builds trust | (213) 555-0100 for LA business |
| **Toll-Free** | National, professional | (800) 555-0100 |
| **Vanity** | Memorable, marketing | (800) FIT-GYMS |
| **Short Code** | High-volume marketing | 12345 (enterprise only) |

### International Compliance

- **UK:** Ofcom regulations, SMS sender ID rules
- **Canada:** CASL (Canadian Anti-Spam Law) - consent required
- **EU:** GDPR + country-specific rules
- **Australia:** SPAM Act requirements

---

## Part 3: Email System (45 min)

### Shared IP vs Dedicated IP

| Feature | Shared IP | Dedicated IP |
|---------|-----------|--------------|
| Cost | Free/included | Extra fee |
| Volume | Under ~50K/month | Over 50K/month |
| Sender Reputation | Shared with others | Yours alone |
| Best For | New/small agencies | Established, high-volume |
| Warmup Required | No | Yes (gradual volume ramp) |

### Email Authentication

**Three must-have DNS records:**

1. **SPF** (Sender Policy Framework) - "These servers can send email for my domain"
2. **DKIM** (DomainKeys Identified Mail) - Cryptographic signature
3. **DMARC** (Domain-based Message Authentication) - Policy for handling failed authentication

**Without these:** Emails land in spam.

### Domain Warmup

For dedicated IPs, gradual volume ramp:
- Week 1: 1,000/day
- Week 2: 5,000/day
- Week 3: 15,000/day
- Week 4+: Full volume

**Why:** Brand new IP has no reputation. Sending 50K on day 1 = spam folder.

### Email Compliance (CAN-SPAM Act)

US law requires every commercial email to have:
1. Accurate sender info (no fake names)
2. Truthful subject line
3. Clear identification as advertisement (or clearly commercial)
4. Valid physical postal address
5. Clear unsubscribe mechanism
6. Honor unsubscribe within 10 business days

**Violations:** Up to $51,744 per email.

---

## Part 4: User Management (45 min)

### Agency Users vs Sub-Account Users

**Agency users:**
- Access multiple sub-accounts
- Created by agency admin
- Billed at agency level
- Roles: Admin, User, Restricted

**Sub-account users:**
- Access one specific sub-account
- Created by sub-account admin
- Billed per sub-account
- Roles: Admin, User

### Permission Levels

| Role | Capabilities |
|------|-------------|
| **Admin** | Full access to sub-account settings |
| **User** | Full operational access, no settings |
| **Custom Role** | Specific permissions you define |

### "Only Assigned Data" Toggle

When enabled for a user:
- They only see contacts assigned to them
- Their pipeline shows only their opportunities
- Their calendar shows only their appointments
- Other users' data is hidden

**Use case:** Trainer Jordan should only see his clients, not Alex's.

### Multi-Sub-Account Access

Agency users can be granted access to:
- All sub-accounts (default for agency admin)
- Specific sub-accounts only
- Mix of admin/user roles across accounts

---

## Part 5: White-Label (60 min)

### Every White-Label Touchpoint

| Touchpoint | DNS Required | Visible To |
|-----------|--------------|-----------|
| **Login Domain** | CNAME to app.leadconnectorhq.com | All users |
| **API Domain** | CNAME | Developers only |
| **Email Domain** | SPF, DKIM, DMARC | Email recipients |
| **Zap URL** | CNAME | Zapier users |
| **Mobile App** | Apple/Google submission | All users |
| **Support Widget** | Toggle | All users |
| **Marketplace** | Toggle | All users |

### Login Domain Setup (Critical!)

1. Agency owns "myagency.com"
2. Create subdomain "app.myagency.com"
3. Add CNAME: `app.myagency.com` → `app.leadconnectorhq.com`
4. Configure in GHL agency settings
5. Wait for SSL provisioning (auto)
6. Clients log in at app.myagency.com - see YOUR brand

### Exercise 24.2: Audit Your Sub-Account

Check:
- What URL do you log in at? White-labeled or default?
- What brand appears in email notifications?
- What brand appears in support widget?
- What brand on mobile app (if any)?

Document your findings - this is what your agency's white-label setup looks like from the inside.

---

## Part 6: Compliance Deep Dive (45 min)

### GDPR (EU Data Protection)

**Applies to:** Any business processing EU residents' data (regardless of where your business is).

**Rights it grants:**
1. **Right to be informed** - Tell users what data you collect
2. **Right of access** - Users can request their data
3. **Right to rectification** - Fix incorrect data
4. **Right to erasure** ("Right to be forgotten") - Delete their data
5. **Right to restrict processing** - Stop using but keep
6. **Right to data portability** - Export data in machine-readable format
7. **Right to object** - Stop marketing, processing
8. **Rights around automated decision making** - Human review

**GHL's role:**
- Processor (on behalf of the agency)
- Agency is the Controller
- Agency must have privacy policy, consent mechanisms, data processing agreements

### HIPAA (Healthcare Data)

**Applies to:** Covered entities handling Protected Health Information (PHI).

**Requirements:**
1. **BAA (Business Associate Agreement)** - signed between agency and HighLevel
2. **BAA between agency and client** - covered entity
3. **Encryption** - at rest and in transit
4. **Access controls** - minimum necessary
5. **Audit logs** - who accessed what
6. **Breach notification** - 60 days

**Without BAA:** Cannot legally store PHI in GHL. Violations = huge fines ($100-$50K per violation, capped at $1.5M/year).

**BrightSmile Dental context:** Patient names + treatment = PHI. MUST be HIPAA-enabled setup.

### SOC 2 (Enterprise Clients)

**What:** Security framework for service organizations.

**Type I vs Type II:**
- Type I: Point-in-time audit
- Type II: Over 6-12 months

HighLevel is SOC 2 Type II certified.

### CCPA (California Consumer Privacy Act)

Similar to GDPR but for California residents:
- Right to know
- Right to delete
- Right to opt out of data sale
- Right to non-discrimination

**Applies to:** Businesses with $25M+ revenue, OR 50K+ CA residents, OR 50%+ revenue from selling data.

---

## Part 7: Practice Quiz - 25 Questions

### Q1
A dental clinic wants to send SMS appointment reminders to 500 patients in the US. What must be registered first?
a) SOC 2 Type II certification
b) A2P 10DLC brand and campaign
c) GDPR compliance
d) HIPAA BAA (for messaging specifically)

**Answer: b)** A2P 10DLC registration is required for all US-based SMS at scale since June 2023.

### Q2
An agency has a client sending 100,000 marketing emails per month. What's the best email infrastructure?
a) Shared IP
b) Dedicated IP with warmup
c) SMTP relay
d) Gmail API

**Answer: b)** Over 50K/month = dedicated IP for sender reputation control. Must warmup gradually.

### Q3
What does DKIM do?
a) Specifies authorized senders
b) Cryptographically signs emails
c) Sets authentication failure policy
d) Routes email to the right server

**Answer: b)** DKIM = cryptographic signature. SPF specifies authorized senders. DMARC sets policy.

### Q4
A healthcare client wants to use GHL. What's required?
a) Nothing special
b) SOC 2 certification
c) BAA signed with HighLevel + between agency and client
d) GDPR compliance

**Answer: c)** HIPAA requires BAA chain: HighLevel → Agency → Covered Entity.

### Q5
What's the difference between an Agency user and a Sub-Account user?
a) Agency users see all sub-accounts; sub-account users see one
b) Agency users can't access sub-accounts
c) Sub-account users have more permissions
d) They're the same thing

**Answer: a)**

### Q6
What does "Only Assigned Data" do?
a) Assigns data randomly
b) Users only see contacts/opportunities assigned to them
c) Deletes unassigned data
d) Auto-assigns new leads

**Answer: b)**

### Q7
CAN-SPAM violations cost up to how much per email?
a) $500
b) $5,000
c) $51,744
d) No penalty

**Answer: c)** Up to $51,744 per email (2024 adjusted).

### Q8
A snapshot saves:
a) Contacts and their data
b) Sub-account configuration (templates, pipelines, workflows)
c) API keys
d) All of the above

**Answer: b)** Configuration only, never contacts or credentials.

### Q9
GDPR "Right to Erasure" means:
a) User can request their data be deleted
b) Agency can delete any user
c) HighLevel deletes inactive users automatically
d) Email marketing lists auto-expire

**Answer: a)**

### Q10
What must be on EVERY marketing email per CAN-SPAM?
a) Unsubscribe link
b) Physical postal address
c) Truthful subject line
d) All of the above

**Answer: d)**

### Q11
A client wants to log in at "portal.theiragency.com" instead of GHL's default. What's required?
a) Nothing, just tell them the URL
b) CNAME DNS record + agency white-label setup
c) New GHL account
d) Custom mobile app

**Answer: b)** White-label login requires CNAME pointing to app.leadconnectorhq.com.

### Q12
A2P 10DLC registration has two parts. What are they?
a) Phone and email
b) Brand and Campaign
c) User and Account
d) Setup and Verification

**Answer: b)**

### Q13
What's the max fine under HIPAA (per year)?
a) $100,000
b) $1,500,000
c) $5,000,000
d) Unlimited

**Answer: b)** $1.5M/year cap per violation type.

### Q14
GHL is what under GDPR?
a) Data Controller
b) Data Processor
c) Data Subject
d) Neither

**Answer: b)** HighLevel processes data on behalf of the agency (Controller).

### Q15
Which DNS records are needed for email authentication?
a) A, AAAA, CNAME
b) MX only
c) SPF, DKIM, DMARC
d) TXT, A, MX

**Answer: c)**

### Q16
A new dedicated IP requires warmup because:
a) It needs testing
b) No sender reputation yet, ramp slowly to avoid spam
c) Twilio requires it
d) HIPAA compliance

**Answer: b)**

### Q17
What's a vanity phone number?
a) Fancy area code
b) Memorable letters (like 800-FLOWERS)
c) Premium number
d) Toll-free number

**Answer: b)**

### Q18
Agency Trust Center is for:
a) Managing trust scores
b) A2P 10DLC brand registration
c) Security settings
d) Credit card vault

**Answer: b)**

### Q19
CCPA applies to businesses with:
a) Any revenue
b) $25M+ revenue OR 50K+ CA residents OR 50% rev from data sales
c) Only $100M+ companies
d) No specific threshold

**Answer: b)**

### Q20
For EU customers, consent must be:
a) Pre-checked boxes OK
b) Explicit opt-in (affirmative action)
c) Implied from signup
d) Purchased from broker

**Answer: b)** GDPR requires affirmative consent.

### Q21
The Snapshots library is at:
a) Sub-account level
b) Agency level
c) Both levels
d) User profile

**Answer: b)**

### Q22
If CNAME for white-label login isn't set up, what happens?
a) Client sees HighLevel branding
b) Login fails
c) Account locked
d) Default to gohighlevel.com URL

**Answer: a)**

### Q23
SOC 2 Type II audit covers:
a) One point in time
b) 6-12 months of controls
c) The physical office
d) Code quality

**Answer: b)**

### Q24
A carrier flags your A2P 10DLC campaign as violating rules. What happens?
a) Warning only
b) Messages filtered or blocked
c) Phone number suspended
d) b and c

**Answer: d)**

### Q25
Multi-sub-account access is granted:
a) Automatically to all agency users
b) Per user, per sub-account, configurable
c) Only to agency admin
d) By HighLevel support

**Answer: b)**

---

## Part 8: Mock Setup Exercise

**Scenario:** You're onboarding "Smile Dental Group" - a new dental practice client.

**Their requirements:**
- HIPAA compliance (patient data)
- 5 staff members need access (2 dentists, 2 hygienists, 1 front desk)
- Phone system for appointment reminders (need A2P registered)
- White-labeled portal ("portal.smiledentalgroup.com")
- Gmail integration for each dentist's inbox

**Document the agency-level setup you would perform (you don't have access, but describe the process):**

1. **Snapshot selection:** Which existing dental snapshot would you apply?
2. **User creation:** What roles for each staff member?
3. **HIPAA setup:**
   - BAA between HighLevel and your agency: [already in place]
   - BAA between your agency and Smile Dental: [sign before going live]
   - HIPAA-enabled sub-account: [request from HighLevel]
4. **A2P 10DLC:**
   - Brand registration for Smile Dental
   - Campaign: "Customer Care - Appointment Reminders"
5. **White-label:**
   - CNAME setup for portal.smiledentalgroup.com
   - DNS: SPF, DKIM, DMARC for their email
6. **Gmail integration:** Each dentist connects their personal Gmail

---

## Quick Reference Cheat Sheet

| Topic | Must-Know Fact |
|-------|----------------|
| A2P 10DLC | Required for US SMS since June 2023, Brand + Campaign registration |
| HIPAA | BAA required HighLevel → Agency → Covered Entity |
| Shared IP threshold | Under ~50K emails/month |
| Dedicated IP threshold | Over 50K emails/month + warmup needed |
| White-label login | CNAME to app.leadconnectorhq.com |
| CAN-SPAM fine | Up to $51,744 per email |
| HIPAA fine | Up to $50K/violation, $1.5M/year cap |
| Email auth records | SPF, DKIM, DMARC |
| Phone number types | Local, Toll-Free, Vanity, Short Code |
| Snapshots save | Configuration (NOT contacts, data, keys) |
| Agency Trust Center | A2P 10DLC registration location |
| "Only Assigned Data" | User sees only their assigned contacts |
| Agency users | Multi-sub-account access |
| Sub-account users | Single sub-account access |
| GDPR rights | 8 core rights for EU residents |
| CCPA threshold | $25M+ revenue OR 50K+ CA residents |

---

## Day 24 Recap

You reviewed all agency-level features that appear on the certification. Tomorrow is sub-account core features - where you have the most hands-on experience from Phase 1.

## Next Day Preview

**Day 25: Sub-Account Mastery Review** - Communications, CRM, Calendars, Pipelines, Payments. 25+ more practice questions.
