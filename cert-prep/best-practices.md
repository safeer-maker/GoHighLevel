# GoHighLevel Best Practices Reference

**Purpose:** What experts do differently from beginners. Quality standards for real-world GHL implementations.

---

## How to Use This Reference

- **While building** Sunrise Wellness Studio (Phase 1 onwards) — check against each section as you work
- **When auditing** real client accounts — use as a review checklist
- **Before delivery** — run through relevant sections before handoff
- **Onboarding team** — share specific sections as training

Hands-on drill (Phase 1 only):
- [Phase 1 Practical (BrightSmile + Elevate)](../course/phase-1/practical-brightsmile-elevate-full-build.md)

### How These Were Selected

Each practice here is a pattern that:
1. Experienced agencies consistently follow
2. Solves a real problem that beginners hit
3. Scales from one account to many
4. Is testable (you can tell if it was done or not)

---

# SETTINGS BEST PRACTICES

## 1. Timezone FIRST, Before Anything Else

**Why:** Timezone affects every appointment, reminder, workflow, and timestamp. Changing it later means auditing everything.

**How:**
- Set in Sub-Account Settings > Business Profile > Timezone
- Match the physical business location (not the owner's location if different)
- For multi-location businesses, use location-specific calendars
- Verify via a test appointment

**Anti-pattern:** Leaving it as the default (often UTC) and setting other things first.

## 2. Custom Values for Every Piece of Repeated Data

**Why:** Hardcoded strings in templates and workflows become a maintenance nightmare. Change the phone number once in Custom Values instead of 40 places.

**Custom Values to Create Day 1:**
- `business_name` — "Sunrise Wellness Studio"
- `business_phone` — main phone line
- `business_email` — main contact email
- `business_address` — physical address (required for CAN-SPAM)
- `owner_name` — main contact person
- `owner_email` — owner direct email
- `booking_link` — primary booking URL
- `website_url` — main website
- `support_url` — help/FAQ URL
- `privacy_policy_url` — privacy policy
- `terms_url` — terms of service
- `social_facebook` — FB page URL
- `social_instagram` — IG URL
- `review_request_url` — where to leave reviews

**Anti-pattern:** Retyping the business phone number in every email/SMS template.

## 3. Notification Plan Documented Per Role

**Why:** Leads slip through cracks when no one knows who gets notified.

**Create a doc:**
| Event | Who Gets Notified | Channel |
|-------|-------------------|---------|
| New lead form submission | Sales rep on-duty | SMS + in-app |
| Appointment booked | Assigned staff | Email + calendar invite |
| Payment failed | Owner + billing lead | Email |
| Support inquiry | Support team | Slack webhook |
| VIP contact activity | Owner | SMS |

**Anti-pattern:** "Everyone gets everything" — alert fatigue sets in, real alerts get ignored.

## 4. Audit Log Review Cadence

**Why:** Catch mistakes, bad actors, or accidental changes before they cause problems.

**Cadence:**
- Weekly: spot check recent changes
- Monthly: full audit log export and review
- Quarterly: user access audit (anyone still need access?)

---

# CRM BEST PRACTICES

## 1. Custom Field Naming Convention

**Rule:** lowercase, snake_case or dashes, NO spaces, NO conflicts.

**Good examples:**
- `membership_tier`
- `tshirt_size`
- `referred_by`
- `emergency_contact_phone`

**Bad examples:**
- `Membership Tier` (spaces break merge fields)
- `Email` (conflicts with built-in email)
- `phone2` (what's phone1? ambiguous)
- `field1` (what is it?)

## 2. Custom Folder Organization

**Why:** 50+ fields without folders becomes unusable.

**Pattern: group by purpose.**
- `Personal Info` — birthday, address, tshirt size
- `Membership` — tier, start date, billing status
- `Preferences` — communication channel, class preference
- `Health Intake` — goals, medical notes, injuries (HIPAA-compliant if needed)
- `Source Attribution` — referred_by, source_channel, campaign
- `Internal` — lead score, notes, staff flags

## 3. Tag Taxonomy: Category-Purpose Format

**Rule:** Every tag follows `category-purpose` pattern.

| Category | Examples |
|----------|----------|
| `source-` | source-facebook, source-google-ads, source-referral, source-walkin |
| `interest-` | interest-pt, interest-yoga, interest-nutrition |
| `lifecycle-` | lifecycle-lead, lifecycle-trial, lifecycle-member, lifecycle-churned |
| `status-` | status-vip, status-at-risk, status-reactivated |
| `behavior-` | behavior-clicked-pricing, behavior-booked-consult |
| `campaign-` | campaign-newyear-2026, campaign-referral-q1 |

**Anti-pattern:** "good lead", "important", "hot", "maybe" — subjective, useless for automation.

## 4. Smart List Naming: Action-Outcome Format

**Rule:** Name tells you what action to take on those contacts.

| Good | Bad |
|------|-----|
| `trial-converting-2days` | `trial list 2` |
| `members-at-risk-60day` | `inactive` |
| `leads-hot-called-no-response` | `untouched` |
| `birthday-this-week` | `birthdays` |

Smart Lists are for driving action — the name should hint at what to do.

## 5. Never Delete — Archive or Tag

**Why:** Deletion loses history, conversations, workflow memberships. Recoverable only briefly.

**Pattern:**
- Tag contact as `archived-YYYY-MM` (e.g., `archived-2026-04`)
- Remove from active Smart Lists via filter (exclude archived tag)
- If truly must delete: export first, then delete

**Exception:** GDPR deletion requests — must fully delete on request.

---

# COMMUNICATIONS BEST PRACTICES

## 1. Templates for Every Repeated Message

**Why:** Reusable, consistent, editable from one place.

**Templates to build:**
- Welcome SMS/Email (after opt-in)
- Appointment confirmation
- Appointment reminder (24h, 2h)
- No-show follow-up
- Review request (post-service)
- Win-back (inactive)
- Payment receipt thank-you
- Payment failed notification
- Referral ask

## 2. SMS Under 160 Characters When Possible

**Why:** One segment = one cost. Over 160 chars = multi-segment (double cost, or fragmented on older phones).

**Tight SMS example:**
```
Hi {{contact.first_name}}! Your 4pm session is tomorrow at Sunrise Wellness. Reply C to confirm or R to reschedule. Reply STOP to opt out.
```

**Techniques:**
- Use contractions (you're, we're)
- Drop filler words
- Short URLs (use trigger links with short domain)
- Don't sign with business name every time (use Custom Value only when needed)

## 3. Email: Mobile-First Design

**Why:** 60%+ of emails are read on mobile. Desktop-optimized designs break.

**Rules:**
- Single column layout
- Font 16px minimum body, 22px+ headings
- Buttons tappable (44px min height)
- CTAs above the fold
- Preview text set (shows in inbox before open)
- Alt text on images (for when images block)

## 4. Always Use Merge Fields for Personalization

**Why:** Generic "Hi there" feels spammy. Personalized performs 2-5x better.

**Standard merge fields to know:**
- `{{contact.first_name}}`
- `{{contact.last_name}}`
- `{{contact.email}}`
- `{{contact.phone}}`
- `{{custom_values.business_name}}`
- `{{custom_values.booking_link}}`
- Appointment merge fields (when in appointment workflow)

**Fallback pattern:**
```
Hi {{contact.first_name|friend}}, ...
```
If first_name is empty, shows "friend" instead of blank or "null".

## 5. Every Email MUST Have Unsubscribe Link

**Why:** CAN-SPAM law requirement. Also prevents spam complaints.

**How:**
- HighLevel auto-includes when using LC Email / Mailgun properly
- Verify in preview — if missing, add manually
- Physical mailing address required in footer too

## 6. SMS Must Have "Reply STOP" for Compliance

**Why:** A2P 10DLC + TCPA compliance. Carriers expect this in at least the first message.

**Pattern:**
- Include "Reply STOP to opt out" in initial contact SMS
- Re-include in periodic marketing blasts
- Transactional SMS (receipts, confirmations) has lighter requirements but include it anyway

---

# CALENDAR BEST PRACTICES

## 1. Buffer Time = 15 Min Minimum

**Why:** Staff need time to prep, document, transition. Back-to-back = burnout and errors.

**Set in:** Calendar > Settings > Buffer Time (Before + After)

**Recommendations:**
- Consultations: 15 min buffer after
- Training sessions: 10 min before + 15 min after
- Group classes: 30 min before + 15 min after
- Video consults: 5 min before + 10 min after

## 2. Minimum Scheduling Notice: 2-4 Hours

**Why:** Last-minute bookings disrupt schedule and reduce quality.

**By type:**
- Urgent services: 1-2 hours
- Standard consults: 2-4 hours
- Specialized services: 24 hours
- Group classes: 1 hour (last-minute fillable is good here)

## 3. Clear Booking Form with Intake Questions

**Why:** Collect useful info upfront. Reduces prep time.

**Typical intake questions:**
- Goal for session
- Prior experience
- Injuries or restrictions
- How did you hear about us (source attribution)

**Map to custom fields** — don't leave info in the Notes field only.

## 4. Mobile Preview Before Go-Live

**Why:** 70%+ of bookings happen on mobile. Broken mobile = lost bookings.

**Test:**
- Open booking link on actual phone (not desktop responsive mode)
- Book a test appointment end-to-end
- Verify confirmation email/SMS received

## 5. Test in Incognito Before Sharing

**Why:** Logged-in view shows you data that public users won't see.

**Pattern:**
- Open booking link in Incognito / Private window
- Complete a full booking with a test contact
- Verify everything works as a new user would experience it

---

# PIPELINE BEST PRACTICES

## 1. 4-7 Stages Optimal

**Why:** Too few = no granularity. Too many = stage fatigue, unclear transitions.

**Example (sales):**
1. New Lead
2. Contacted
3. Qualified
4. Proposal Sent
5. Negotiation
6. Won / Lost

**Example (fitness membership):**
1. Interested
2. Trial Scheduled
3. Trial Attended
4. Consultation
5. Member
6. Churned / Declined

## 2. Clear Criteria for Each Stage Transition

**Why:** Ambiguous criteria = deals stuck in wrong stage.

**Document:**
- "New Lead → Contacted": first outreach made (SMS, call, or email)
- "Contacted → Qualified": confirmed interest + budget
- "Qualified → Proposal Sent": proposal document delivered
- etc.

## 3. Both Won AND Lost End States

**Why:** You need to track WHY deals lost to improve.

**Pattern:**
- Won stage: success stage (e.g., Member)
- Lost stage(s): Declined — too expensive / Declined — wrong fit / Declined — no response
- Use tags to capture loss reason

## 4. Regular Stale Deal Review (Weekly)

**Why:** Deals sitting 30+ days in one stage are probably dead.

**Process:**
- Smart List: Opportunities in Stage X > 14 days, no activity
- Weekly review: move forward, move to Lost, or re-engage
- Auto-workflow can tag `stale-opportunity` for review

## 5. Weighted Value Reporting

**Why:** Raw pipeline value is misleading. Weight by stage probability.

**Pattern:**
- Contacted: 10% * deal value
- Qualified: 30% * deal value
- Proposal: 60% * deal value
- Negotiation: 80% * deal value
- Report true pipeline value

---

# PAYMENT BEST PRACTICES

## 1. Products First, Then Invoices

**Why:** Invoices pulling from products auto-populate correctly. Ad-hoc invoices drift.

**Order:**
1. Define products with clear names and prices
2. Build invoices FROM products
3. Exception: one-off bespoke work → ad-hoc line item

## 2. Descriptive Product Descriptions

**Why:** Customers (and future you) need to know what they're paying for.

**Bad:** "Monthly membership"
**Good:** "Sunrise Wellness Monthly Premium — unlimited classes, 2 PT sessions, nutrition consult"

## 3. Clear Coupon Rules

**Why:** Stacking coupons, forgotten expiration, wrong-product application = refund headaches.

**Every coupon needs:**
- Max uses total
- Max uses per customer
- Expiration date
- Product restrictions
- Minimum order amount (if applicable)
- Clear name: `LAUNCH25-2026-Q1` not `save`

## 4. Tax Applied Automatically

**Why:** Manually adding tax per invoice = errors and compliance risk.

**Set:**
- Tax rate at product level OR
- Tax rules at sub-account level
- Use automated tax tools if multi-jurisdiction

## 5. Recurring Products with Clear Billing Schedule

**Why:** Customers need to know the schedule. Staff need to answer billing questions.

**For each recurring product:**
- Billing frequency (monthly, yearly)
- Billing start date logic
- Grace period for failed payment
- Cancellation policy
- Document all in product description

---

# FUNNEL BEST PRACTICES

## 1. One Goal per Funnel

**Why:** Multiple CTAs = split attention = lower conversion.

**Pattern:**
- Lead magnet funnel: one CTA (get the PDF)
- Consultation funnel: one CTA (book the call)
- Upsell funnel: one CTA (add the product)

**Anti-pattern:** "Get the guide OR book a call OR call us OR..." — paralysis.

## 2. Mobile Responsive Testing

**Why:** See Calendar Section 4 — most traffic is mobile.

**Check:**
- Open on actual device
- Check loading speed
- Buttons clickable without zooming
- Forms usable with thumb (not pinch-zoom)

## 3. Fast Page Load (< 3 Seconds)

**Why:** Every second of load time drops conversion ~7%.

**Optimize:**
- Compress images (WebP, under 200KB each)
- Limit video autoplay (use thumbnails)
- Minimize third-party scripts
- Test with PageSpeed Insights or GTmetrix

## 4. Clear CTA (One Primary)

**Why:** Covered in #1 — one goal.

**Design:**
- Contrasting color (stands out from page)
- Action verb ("Get", "Start", "Book", "Download")
- Above the fold
- Repeated every 2-3 sections on long pages

## 5. Social Proof Visible

**Why:** Trust signals increase conversion 10-30%.

**Include:**
- Client logos
- Testimonials with names, photos, specifics
- Reviews / ratings
- Numbers ("500+ members", "10,000 classes taught")
- Press mentions

## 6. Testimonials Specific (Not Generic)

**Why:** "Great service!" persuades no one.

**Pattern:**
- Name + photo + role/context
- Specific outcome: "Lost 15 lbs in 12 weeks with Sunrise's PT program"
- Specific timeframe
- Specific dollar amount or number

---

# FORMS / SURVEYS BEST PRACTICES

## 1. Minimal Fields (Only Required Info)

**Why:** Every field added drops conversion 3-7%.

**Pattern:**
- Lead capture: name + email (sometimes phone if urgent)
- Consultation intake: above + relevant qualifying questions
- Application form: more acceptable (higher-intent users)

## 2. Progressive Profiling (Collect More Later)

**Why:** You don't need everything day 1. Collect over time.

**Phases:**
- Opt-in: email, first name
- First appointment: full name, phone, goals
- After session: feedback, preferences
- After 30 days: referrals, deeper preferences

Each phase's form can use conditional logic — skip fields already filled.

## 3. Conditional Logic for Relevance

**Why:** Showing irrelevant fields feels broken.

**Example (Sunrise intake survey):**
- Q: "Primary goal?" → Weight loss / Strength / Flexibility
- If Weight loss: show "Current weight?" + "Target weight?"
- If Strength: show "Current lifting experience?"
- If Flexibility: show "Any injuries?"

## 4. Custom Field Mapping (Not Everything in Notes)

**Why:** "Notes" field can't be filtered, can't drive automations.

**Map intake answers to typed custom fields:**
- Goal → `primary_goal` dropdown
- Injuries → `injuries` text field
- Emergency contact → `emergency_contact_name` + `emergency_contact_phone`

## 5. Always Trigger a Workflow

**Why:** A form submission with no follow-up = wasted lead.

**Pattern:**
- Every form submission → workflow
- Workflow: welcome message, internal notification, task assignment
- Even "Contact Us" forms need auto-acknowledgment

---

# WORKFLOW BEST PRACTICES

## 1. Name Convention: Trigger-Purpose

**Pattern:** `[trigger]-[purpose]-[audience]`

**Examples:**
- `form-welcome-trial-lead`
- `tag-reactivation-churned-members`
- `appointment-reminder-24h-all`
- `payment-failed-recovery-members`
- `birthday-wishes-all-contacts`

**Anti-pattern:** "Workflow 1", "New Workflow (copy)", "test".

## 2. Always Have an End State

**Why:** Workflows that loop or never end leak into data issues.

**Pattern:**
- Every branch ends (explicitly or via goal)
- Consider "max iterations" for loop-risky workflows
- Add internal notification on unexpected paths

## 3. Test with Test Contacts Before Going Live

**Why:** Real contacts receiving a broken workflow = complaints + unsubscribes.

**Pattern:**
- Create test contacts: `Test-01`, `Test-02`, etc.
- Run workflow on test first
- Check every step fires correctly
- Remove test contacts from main lists (tag `test-internal`)

## 4. Shorten Wait Times for Testing, Restore After

**Why:** Waiting 7 days to verify step 3 = slow dev cycle.

**Pattern:**
- Design with real wait times (24h, 3 days, etc.)
- Temporarily change to 1 minute for test
- Run through entire workflow in minutes
- Restore real times before publishing

## 5. Use If/Else for Personalization

**Why:** One-size-fits-all emails feel generic.

**Pattern:**
- If `custom_field.goal = weight_loss` → weight loss track
- If `custom_field.goal = strength` → strength track
- Else → generic wellness track

Branch each persona into tailored messaging.

## 6. Goal Events to Prevent Duplicates

**Why:** Contact who converted shouldn't keep getting "convert!" emails.

**Pattern:**
- Workflow: Lead Nurture Sequence
- Goal: `became_member` (tag or custom field)
- When goal met: exit workflow, don't continue sequence
- Optionally: enter `Member Onboarding` workflow

## 7. Internal Notifications for Edge Cases

**Why:** Silent failures = worst failures.

**Notify staff on:**
- Payment failed
- VIP contact action
- High-value form submission
- Appointment no-show (second in a row)
- Workflow error / unexpected path

---

# TAG STRATEGY

## Tag Categories (Comprehensive)

### Source Tags
- `source-facebook-ads`
- `source-google-ads`
- `source-google-organic`
- `source-referral`
- `source-walkin`
- `source-partner-[name]`
- `source-event-[name]`

### Interest Tags
- `interest-pt`
- `interest-yoga`
- `interest-nutrition`
- `interest-group-class`
- `interest-massage`

### Lifecycle Tags
- `lifecycle-lead`
- `lifecycle-trial`
- `lifecycle-member`
- `lifecycle-churned`
- `lifecycle-ex-member-winback`

### Status Tags
- `status-vip`
- `status-at-risk`
- `status-reactivated`
- `status-do-not-contact`

### Behavior Tags
- `behavior-clicked-pricing`
- `behavior-booked-consult`
- `behavior-watched-video`
- `behavior-downloaded-guide`

### Campaign Tags
- `campaign-newyear-2026`
- `campaign-referral-q1`
- `campaign-reactivation-spring`

## NEVER Use

- `good`, `bad`, `hot`, `cold` (subjective)
- `important`, `priority` (everyone thinks their contact is important)
- `tag1`, `test`, `temp` (will live forever)
- Duplicates with different cases (`VIP` vs `vip`)

## Tag Lifecycle

- Document all tags in a `tag-dictionary.md`
- Quarterly review — retire unused tags
- Archive campaign tags after campaign ends (don't delete — historical)

---

# DATA HYGIENE

## 1. Monthly Audit for Duplicates

**Why:** Duplicates corrupt reports, messaging, Smart Lists.

**Process:**
- Run Smart List: contacts with same email (if possible)
- Manual review for same-name / similar emails
- Merge duplicates (keeps history)

## 2. Quarterly Smart List Review

**Why:** Smart Lists built over time get stale — filters no longer match business needs.

**Process:**
- List all Smart Lists
- Open each: verify filter, verify count makes sense
- Retire unused lists
- Rename inconsistent names

## 3. Annual Tag Cleanup

**Why:** Tags accumulate faster than anyone realizes.

**Process:**
- Export tag list with usage counts
- Retire tags with 0 contacts
- Merge duplicates (e.g., `vip` and `VIP`)
- Update tag dictionary

## 4. Test Account Pollution Prevention

**Why:** Test contacts in production reports skew metrics.

**Prevention:**
- All test contacts get `test-internal` tag
- All reports filter out `test-internal`
- Delete test contacts quarterly (or tag `archived-test`)

## 5. Backup Export Monthly

**Why:** Platform issues, accidental deletions, audit needs.

**Export:**
- Contacts (CSV)
- Workflows (JSON/snapshot)
- Custom fields/values structure
- Pipelines structure
- Store in secure backup (not just laptop)

---

# SECURITY BEST PRACTICES

## 1. Never Commit API Keys

**Why:** Anyone with repo access gets your keys. Public repos = instant abuse.

**Pattern:**
- API keys in `.env` file
- `.env` in `.gitignore`
- Use `os.environ.get("GHL_API_KEY")` in Python
- Document required env vars in README

## 2. Rotate Keys Quarterly

**Why:** Leaked keys happen. Rotation limits blast radius.

**Process:**
- Schedule rotation on calendar (quarterly)
- Generate new key
- Update all integrations
- Revoke old key
- Log the rotation

## 3. Minimum Permissions for Each User

**Why:** Over-permissioned users = bigger accident/breach surface.

**Pattern:**
- Sales rep: access to contacts + pipeline only
- Marketer: workflows + campaigns only
- Admin: full access
- Never give admin "just in case"

## 4. Review Audit Logs Weekly

**Why:** Catch unusual activity early.

**Check for:**
- Unexpected logins (location, time)
- Mass changes (bulk deletes, mass updates)
- Settings changes by unexpected users
- New user creation

## 5. Enable 2FA If Available

**Why:** Password-only accounts are breached via credential stuffing regularly.

**Apply to:**
- Every agency admin
- Every sub-account admin
- Any user with payment or export access

---

# API BEST PRACTICES

## 1. Rate Limiting (`time.sleep` Between Calls)

**Why:** Hitting rate limits = errors, blocks, account flags.

**Pattern (Python):**
```python
import time

for contact in contacts:
    response = requests.post(url, ...)
    time.sleep(0.2)  # 5 req/sec max
```

Check HighLevel current rate limits and stay well under.

## 2. Error Handling (Try/Except Everywhere)

**Why:** One bad response shouldn't crash the whole script.

**Pattern:**
```python
try:
    response = requests.post(url, json=data, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    log_error(f"API call failed: {e}")
    continue  # or retry
```

## 3. Retry Logic with Exponential Backoff

**Why:** Transient failures happen. Retry intelligently.

**Pattern:**
```python
for attempt in range(3):
    try:
        response = requests.post(url, ...)
        response.raise_for_status()
        break
    except requests.exceptions.RequestException:
        wait = 2 ** attempt  # 1, 2, 4 seconds
        time.sleep(wait)
```

## 4. Webhook Authentication

**Why:** Unauthenticated webhooks = anyone can trigger your automation.

**Pattern:**
- Require a shared secret in header
- Verify signature (HMAC) if platform supports
- IP allowlist where possible
- Log all webhook receipts for audit

## 5. Never Log Sensitive Data (PII, Tokens)

**Why:** Logs leak. PII in logs = compliance violation.

**Never log:**
- API keys, tokens
- Passwords
- Full credit card numbers
- SSNs, government IDs
- Full email bodies if they contain PII
- Phone numbers (log last 4 only if needed)

**Pattern:**
```python
log.info(f"Processing contact id={contact.id}")  # OK
log.info(f"Processing contact email={contact.email}")  # BAD
```

---

# CLIENT HANDOFF BEST PRACTICES

## 1. Documentation of Every Workflow

**Why:** Clients (and future you) need to understand what's running.

**Per workflow doc:**
- Name and purpose
- Trigger(s)
- Key actions
- Dependencies (tags, custom fields, integrations)
- How to pause/edit
- How to test safely
- Known edge cases

Store in a `workflows.md` or Notion doc alongside the account.

## 2. Tag Dictionary Shared with Client

**Why:** Client adds their own tags — without dictionary, they break conventions.

**Include:**
- Every tag currently used
- What each one means
- How each one is applied (manual vs workflow)
- Which workflows depend on each
- Naming convention rules

## 3. Video Walkthrough of Main Features

**Why:** Written docs aren't read. Videos are watched.

**5-10 min video covering:**
- How to find things (CRM, Calendar, Pipeline)
- How to add a contact manually
- How to check inbox
- How to view reports
- Who to call if something breaks

Loom or similar — embed in onboarding doc.

## 4. Access Credentials via Password Manager

**Why:** Sharing via email or Slack = security breach.

**Pattern:**
- 1Password, Bitwarden, LastPass shared vaults
- Time-limited shares where possible
- Client's own password for their account (don't share yours)
- Audit log of who accessed what

## 5. 30-Day Support Period Standard

**Why:** First 30 days reveal issues. Budget support.

**Include in contract:**
- 30-day post-launch support included
- Defined response time (business hours, 24h)
- Defined scope (bug fixes, not new features)
- Path to extend (retainer, hourly)

---

# FINAL CHECKLIST BEFORE DELIVERY

Run through this checklist before handing any GHL build to a client.

## Settings
- [ ] Timezone correct
- [ ] Business hours set
- [ ] Address filled (required for CAN-SPAM)
- [ ] Custom Values complete
- [ ] Notification plan documented

## CRM
- [ ] Custom Fields follow naming convention
- [ ] Custom Folders organize fields logically
- [ ] Tag taxonomy documented
- [ ] Test contacts removed or tagged

## Communications
- [ ] Templates created for all repeated messages
- [ ] SMS includes "Reply STOP"
- [ ] Email includes unsubscribe + address
- [ ] A2P 10DLC registered (US SMS)

## Calendars
- [ ] Buffer times set
- [ ] Minimum notice set
- [ ] Intake questions map to custom fields
- [ ] Mobile tested
- [ ] Incognito tested

## Pipelines
- [ ] 4-7 stages
- [ ] Clear transition criteria documented
- [ ] Won + Lost end states
- [ ] Stale deal review scheduled

## Payments
- [ ] Products defined first
- [ ] Descriptive product descriptions
- [ ] Coupon rules clear
- [ ] Tax configured
- [ ] Recurring billing documented

## Funnels/Sites
- [ ] One primary CTA per page
- [ ] Mobile tested
- [ ] Load under 3 seconds
- [ ] Social proof visible
- [ ] Specific testimonials

## Forms/Surveys
- [ ] Minimum fields only
- [ ] Conditional logic where appropriate
- [ ] Custom field mapping (not Notes)
- [ ] Triggers a workflow

## Workflows
- [ ] Naming convention followed
- [ ] All end states defined
- [ ] Tested with test contacts
- [ ] Internal notifications on edge cases
- [ ] Goal events prevent duplicates

## Security & Handoff
- [ ] API keys not committed
- [ ] Minimum permissions set
- [ ] 2FA enabled on all admins
- [ ] Documentation delivered
- [ ] Tag dictionary shared
- [ ] Walkthrough video recorded
- [ ] Credentials in password manager
- [ ] 30-day support defined

---

**Remember:** Best practices are guidelines, not laws. Know why each exists. When a client's situation calls for deviation, document WHY and proceed intentionally.
