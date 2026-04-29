# Common GoHighLevel Pitfalls - What NOT to Do

**Purpose:** Learn from others' mistakes. These are real problems agencies have run into.

---

## How to Use This Reference

- **Read before** starting any new build to avoid known traps
- **Reference when** troubleshooting — check if the issue matches a known pitfall
- **Use during audits** — many client accounts have these same problems
- **Cert exam prep** — many pitfalls map directly to exam trick questions

Hands-on drill (Phase 1 only):
- [Phase 1 Practical (BrightSmile + Elevate)](../course/phase-1/practical-brightsmile-elevate-full-build.md)

Each pitfall has:
- **What happens** — the symptom
- **Why it's bad** — the consequence
- **How to avoid** — the correct approach

---

# SETUP PITFALLS

## 1. Wrong Timezone Set

**What happens:** Every appointment reminder, workflow, scheduled message fires at the wrong local time.

**Why it's bad:**
- 9am reminders going out at 5am (3am in client's timezone)
- Appointments displayed in wrong time
- Business-hour SMS sending overnight
- "Send at 10am contact timezone" sending at 10am UTC

**How to avoid:**
- Set timezone FIRST thing in a new sub-account
- Sub-Account Settings > Business Profile > Timezone
- Match the business's physical location
- Verify with a test appointment

## 2. Custom Values Not Set

**What happens:** Business phone, name, address, booking link hardcoded in every template, workflow, and email.

**Why it's bad:**
- Phone number changes → 40 places to update
- Typo propagates across every asset
- New staff don't know which are authoritative
- Takes 10x longer to maintain

**How to avoid:**
- Create core Custom Values on Day 1 (see best practices doc)
- Use `{{custom_values.xxx}}` everywhere, never hardcode
- Audit existing templates quarterly for hardcoded strings

## 3. No Notification Plan

**What happens:** Team has no system for who gets alerted on new leads, payments, no-shows.

**Why it's bad:**
- Leads slip through cracks for weeks
- Multiple people responding to same lead (confusing)
- Urgent issues buried under spam alerts

**How to avoid:**
- Document notification matrix (event → recipient → channel)
- Different staff for different events
- Distinguish urgent (SMS) from informational (email)

## 4. No Business Hours Configured

**What happens:** Automations send messages overnight.

**Why it's bad:**
- Complaints from contacts receiving 2am SMS
- Unsubscribes spike
- Carriers may flag the number

**How to avoid:**
- Settings > Business Hours
- Enable "Business Hours Only" on all non-urgent workflows
- Use "Wait Until" to next business hour for after-hours triggers

## 5. Skipping Terms of Service / Privacy Policy Setup

**What happens:** Forms collect data without legal disclosure links.

**Why it's bad:**
- GDPR / CCPA violations
- Lost legal defense if audited
- Trust issues with contacts

**How to avoid:**
- Host ToS and Privacy Policy pages
- Link in all form footers (Custom Value for URL)
- Include opt-in checkbox where required

---

# CRM PITFALLS

## 1. Tag Explosion

**What happens:** Tags like `tag-1`, `tag2`, `tag_3`, `VIP`, `vip`, `v.i.p.`, `important`, `important!`, `important-client` accumulate over months.

**Why it's bad:**
- No one knows which tag is "real"
- Workflows fire on wrong tags
- Reports unreliable
- New staff can't learn the system

**How to avoid:**
- Tag taxonomy defined upfront (see best practices)
- Tag dictionary document shared with team
- Quarterly tag cleanup

## 2. Custom Field Duplication

**What happens:** "Birthday" field exists three times: `birthday`, `Birthday`, `date_of_birth`.

**Why it's bad:**
- Data fragmented across fields
- Workflows miss contacts (checking only one field)
- Reports show wrong counts

**How to avoid:**
- Before creating a field, search existing fields
- Naming convention: lowercase, snake_case
- Migrate duplicate field data + delete extras

## 3. Importing Without Dedup

**What happens:** 500 contact import creates 50 duplicates where the same person was already in CRM.

**Why it's bad:**
- Duplicate conversations
- Duplicate messages sent (looks spammy)
- Smart Lists have wrong counts
- Contact merge is tedious for many

**How to avoid:**
- Use HighLevel's dedup on import (match on email/phone)
- Pre-clean CSV before import
- Tag imported contacts with `import-YYYY-MM-source` for tracking

## 4. Deleting Contacts Loses Data

**What happens:** Contact deleted to "clean up." Later realize their conversation history is also gone.

**Why it's bad:**
- Lost conversation history
- Lost opportunity history
- Lost workflow membership
- Recovery window is limited; after that, gone forever

**How to avoid:**
- Never delete — use `archived-YYYY-MM` tag
- Exclude archived contacts from active Smart Lists via filter
- Exception: GDPR deletion requests (legally required)

## 5. Manual Data Entry Instead of Automation

**What happens:** Staff manually tag contacts from calls, manually add to pipelines.

**Why it's bad:**
- Inconsistent (different staff tag differently)
- Slow (takes minutes per contact)
- Errors
- Doesn't scale

**How to avoid:**
- Workflow triggers for common events
- Trigger links for email/SMS interactions
- Task automation for repetitive actions

---

# CALENDAR PITFALLS

## 1. No Buffer Time

**What happens:** Appointments booked back-to-back with no gap.

**Why it's bad:**
- Sessions run over into next appointment
- No time for notes, prep, transition
- Staff burnout
- Late appointments cascade through the day

**How to avoid:**
- Minimum 10-15 minutes buffer on every calendar
- More for service types that need cleanup

## 2. Overbooking Enabled

**What happens:** Multiple contacts book the same 2pm slot.

**Why it's bad:**
- Team scrambles to reassign
- Contacts arrive to find no available trainer
- Poor reviews

**How to avoid:**
- Verify "Allow Overbooking" is OFF for 1:1 services
- Class calendars can allow overbooking up to capacity limit

## 3. No Minimum Notice

**What happens:** Contacts book 15-minute-out appointments that no one is ready for.

**Why it's bad:**
- Staff interrupted mid-task
- Prep time zero
- Overall experience rushed

**How to avoid:**
- 2-4 hour minimum scheduling notice standard
- Exceptions for truly urgent services

## 4. Not Testing the Booking Flow

**What happens:** Booking page launched without end-to-end test. Customers find broken page.

**Why it's bad:**
- First impression = broken
- Lost bookings
- Brand damage

**How to avoid:**
- Incognito test full flow before sharing
- Mobile test
- Book real test appointment, verify confirmation email/SMS

## 5. Unclear Calendar Type Choice

**What happens:** Using "Personal" when "Round Robin" was needed. Or using "Round Robin" when "Collective" was needed.

**Why it's bad:**
- Bookings go to wrong team members
- Collective meetings missing key attendees
- Team frustration

**How to avoid:**
- Know the calendar types (see cert study guide Section 3)
- Rebuild calendar if wrong type chosen (settings can't switch type)

## 6. Booking Confirmations Not Customized

**What happens:** Default "Your appointment is confirmed" email with no specifics, no prep info.

**Why it's bad:**
- Contacts forget what they booked
- No prep instructions (show up unprepared)
- No contact info for rescheduling
- Looks unprofessional

**How to avoid:**
- Customize confirmation email with: what to bring, where to go, what to expect, how to reschedule
- SMS reminder 24h + 2h before
- Use merge fields for appointment details

---

# WORKFLOW PITFALLS

## 1. Never Testing Before Launch

**What happens:** Workflow goes live, contacts receive broken/weird messages.

**Why it's bad:**
- Unsubscribes
- Complaints
- Brand damage
- Hard to tell how many contacts were affected

**How to avoid:**
- Test contacts for every workflow
- Run end-to-end before enabling
- Shorten waits temporarily for testing

## 2. Forgetting Goal Events

**What happens:** Contact converts mid-nurture, keeps receiving "convert now!" messages.

**Why it's bad:**
- Looks automated (not in a good way)
- Converted customer feels ignored as a customer
- Unsubscribe risk even after conversion

**How to avoid:**
- Define goal event for every workflow
- On goal met, exit workflow (or transfer to onboarding)

## 3. Tag Loops (Infinite Loop)

**What happens:** Workflow adds tag `nurture-complete`. That tag triggers another workflow which adds tag `re-engage`. Which triggers another... infinite loop.

**Why it's bad:**
- Contacts hammered with messages
- API calls / send limits hit
- Silent cost spiral

**How to avoid:**
- Map workflow triggers before building
- No workflow should trigger another workflow that triggers the first
- Use explicit entry conditions ("once only") on workflows

## 4. No Error Handling / Silent Failures

**What happens:** A step fails, workflow continues without the action. Contact never gets the critical email.

**Why it's bad:**
- Silent failure = unknown count of affected contacts
- Issues compound
- Loss of trust when discovered

**How to avoid:**
- Internal notifications on unexpected branches
- Error tracking in webhooks
- Regular workflow execution report review

## 5. Too Aggressive Timing

**What happens:** New lead gets SMS + email + voicemail + SMS within 30 minutes.

**Why it's bad:**
- Feels like stalking
- Unsubscribes spike
- A2P / spam complaints

**How to avoid:**
- Space touches (1-2 hours minimum between)
- Varied channels (not 5 SMS in a row)
- "Stop on reply" enabled

## 6. Too Slow Timing

**What happens:** First follow-up sent 3 days after form submission.

**Why it's bad:**
- Lead is cold
- Competitors have responded
- Conversion rate drops

**How to avoid:**
- First touch within minutes (automated)
- Personal touch within 1 hour (task)
- Cadence: 1 hour, 4 hours, 24 hours, 3 days, 7 days, 14 days

## 7. No End State

**What happens:** Workflow runs indefinitely, or one branch has no final step.

**Why it's bad:**
- Data inconsistency
- Hard to debug
- Contacts stuck in workflow

**How to avoid:**
- Every branch terminates or loops back intentionally
- Max iterations defined for loop-risky workflows

## 8. Draft Workflows Never Published

**What happens:** Workflow built, but never toggled to "Published." Does nothing.

**Why it's bad:**
- Silent failure
- Client/staff think it's working
- Discovered weeks later

**How to avoid:**
- Checklist item: publish after testing
- Visual audit of all workflows' status monthly

---

# EMAIL PITFALLS

## 1. No Unsubscribe Link

**What happens:** Email sent without unsubscribe link.

**Why it's bad:**
- CAN-SPAM violation ($50k+ per email in fines)
- Spam complaints increase
- Domain reputation damaged
- Future emails land in spam

**How to avoid:**
- Every marketing email HAS unsubscribe link
- HighLevel auto-adds when using proper email config
- Preview every email — verify link present

## 2. Spammy Subject Lines

**What happens:** Subject lines like "FREE!!! Make $$$ Now!!!" or "URGENT: Open immediately."

**Why it's bad:**
- Spam filters trigger
- Emails land in Promotions/Spam folders
- Low open rates compound domain reputation damage

**How to avoid:**
- Avoid all-caps
- Avoid excessive punctuation (!!!, ???)
- Avoid obvious spam words ($$, FREE, URGENT)
- Subject line tests on spam checkers before send

## 3. Not Warming Up New Domains

**What happens:** Brand-new domain sends 5,000 emails day 1.

**Why it's bad:**
- Immediate deliverability damage
- ISP flags domain as suspicious
- Future emails blocked / spam-foldered

**How to avoid:**
- Gradual send ramp (50 day 1, 100 day 2, scaling up)
- Send to engaged contacts first
- Wait 2-4 weeks before mass sends
- Warm-up tools/services can accelerate

## 4. Purchased Lists

**What happens:** Agency buys a list of 10,000 "qualified leads" and blasts them.

**Why it's bad:**
- Contacts never consented = CAN-SPAM violation
- High spam complaints
- Immediate deliverability damage across ALL your email
- Usually account ban

**How to avoid:**
- NEVER buy email lists
- Build list organically (opt-ins, forms, referrals)
- Verify consent for every import

## 5. Inconsistent Sending

**What happens:** Business emails 500 on Monday, then nothing for 3 weeks, then 2000 on a Friday.

**Why it's bad:**
- ISPs see erratic patterns = suspicious
- Reputation fluctuates
- Deliverability unpredictable

**How to avoid:**
- Consistent weekly/biweekly cadence
- Smooth ramp when volume changes
- Don't "batch save" and burst

## 6. No SPF/DKIM/DMARC Setup

**What happens:** Emails sent from custom domain without proper DNS authentication.

**Why it's bad:**
- Emails marked as spoofed
- Deliverability terrible
- Some domains (Gmail, Yahoo) reject outright

**How to avoid:**
- Set up SPF record
- Set up DKIM record
- Set up DMARC record (start with p=none, monitor, tighten later)
- Test via mail-tester.com or similar

---

# SMS PITFALLS

## 1. No A2P 10DLC Registration

**What happens:** US SMS messages silently blocked by carriers.

**Why it's bad:**
- Messages don't arrive
- No clear error
- Clients think the system is broken
- Lost leads

**How to avoid:**
- Register brand + campaign before sending at volume
- Allow 1-4 weeks for approval
- Maintain compliance (don't change message type without re-approval)

## 2. No "Reply STOP" Instruction

**What happens:** SMS sent without opt-out instructions.

**Why it's bad:**
- TCPA / A2P compliance violation
- Carrier may filter messages
- Legal exposure

**How to avoid:**
- First SMS to every new contact includes "Reply STOP to opt out"
- Periodic re-inclusion in marketing messages
- HighLevel auto-honors STOP responses

## 3. Sending Without Consent

**What happens:** SMS sent to contacts who never opted in.

**Why it's bad:**
- TCPA violations ($500-$1500 per message)
- Class action lawsuit risk
- Massive fines

**How to avoid:**
- Explicit consent on every form (checkbox: "I agree to receive SMS from X")
- Record consent timestamp
- Never scrape or buy phone lists

## 4. Too Frequent SMS

**What happens:** Contact receives 4 SMS in one day.

**Why it's bad:**
- Unsubscribes spike
- Spam complaints to carriers
- Carrier may suspend number

**How to avoid:**
- Max 1-2 SMS per day per contact
- Weekly cadence for non-urgent
- Stop on reply enabled

## 5. Long Messages (Multi-Segment Cost Issue)

**What happens:** SMS is 400 characters. Sent as 3 segments (3x cost) or fragmented on older phones.

**Why it's bad:**
- Triple the cost for large sends
- Poor experience on older phones (messages appear split)
- Sometimes out-of-order delivery

**How to avoid:**
- Keep SMS under 160 chars when possible
- If longer needed, understand segment cost
- Use trigger links for details (short URL + context)

## 6. Sending to Landlines

**What happens:** SMS sent to phone numbers that don't support SMS.

**Why it's bad:**
- Wasted send (still costs)
- No delivery
- Report looks like "sent" but received is zero

**How to avoid:**
- Phone validation on form (verify mobile)
- HighLevel may flag landlines — honor the flag
- Use phone number validation service

---

# PAYMENT PITFALLS

## 1. Wrong Tax Configuration

**What happens:** Tax not applied, or wrong rate applied.

**Why it's bad:**
- Underpayment of tax (legal issue)
- Overpayment to customers (refund headaches)
- Inconsistent reporting

**How to avoid:**
- Consult local tax rules
- Set tax at product or account level
- Automated tax tools for multi-jurisdiction

## 2. Coupon Stacking Bugs

**What happens:** Customer applies two coupons, gets 50% off when only 20% intended.

**Why it's bad:**
- Revenue loss
- Can't claw back easily
- Scales if promo goes viral

**How to avoid:**
- Explicitly set "Max uses per customer" to 1
- Disable stacking where possible
- Test coupon combinations before publishing

## 3. Subscription Cancellation Gaps

**What happens:** Customer cancels, but workflow still sends "thanks for being a member."

**Why it's bad:**
- Looks automated/broken
- Customer asks: "Did my cancellation work?"
- Support tickets

**How to avoid:**
- Workflow trigger on "Subscription Cancelled"
- Remove from member-only workflows
- Send cancellation confirmation

## 4. No Invoice Numbering

**What happens:** Invoices have random IDs, no sequence.

**Why it's bad:**
- Accounting reconciliation hard
- Audit trail confusing
- Customer support can't quickly reference

**How to avoid:**
- HighLevel auto-numbers — verify enabled
- Document numbering scheme
- Match external accounting system

## 5. Not Tracking Failed Payments

**What happens:** Subscription payment fails, nothing happens, customer keeps "member" status without paying.

**Why it's bad:**
- Revenue leak
- Customer not aware their card failed
- Staff don't know to follow up

**How to avoid:**
- Workflow trigger on "Payment Failed"
- Send customer retry email/SMS
- Internal notification to billing team
- Grace period defined (e.g., 7 days)

## 6. Refund Without Service Removal

**What happens:** Customer refunded but still has member access, still receiving member-only content.

**Why it's bad:**
- Free service
- Not scalable
- Others notice and exploit

**How to avoid:**
- Workflow on "Refund Issued"
- Remove member tags
- Revoke access to member areas

---

# INTEGRATION PITFALLS

## 1. No Retry Logic

**What happens:** One API call fails (transient network issue), data is lost.

**Why it's bad:**
- Silent data loss
- Inconsistent state between systems
- Hard to detect after the fact

**How to avoid:**
- Retry with exponential backoff (1s, 2s, 4s)
- Max 3-5 retries
- Dead letter queue for failed items

## 2. Rate Limit Ignorance

**What happens:** Script hammers API at 100 req/sec. Account flagged.

**Why it's bad:**
- Account suspended
- Other integrations affected
- Customer data inaccessible

**How to avoid:**
- Read current rate limits
- `time.sleep` between calls in bulk scripts
- Monitor 429 response codes
- Back off on 429

## 3. Webhook Endpoints Unsecured

**What happens:** Anyone with the URL can POST to your webhook, triggering actions.

**Why it's bad:**
- Malicious actors trigger workflows
- Spam data injected
- Resource exhaustion

**How to avoid:**
- Require shared secret in header
- Verify HMAC signature if provided
- IP allowlist webhook source
- Log all webhook receipts

## 4. No Monitoring

**What happens:** Integration silently breaks weeks ago. No one notices until client complains.

**Why it's bad:**
- Unknown data loss
- Trust damaged
- Hard to backfill

**How to avoid:**
- Health check endpoint pinged regularly
- Dashboards (success rate, error rate)
- Alerts on error spike
- Daily "heartbeat" check

## 5. Hardcoded Credentials

**What happens:** API key pasted directly in script, committed to git.

**Why it's bad:**
- Keys leak
- Automated scrapers find them in minutes
- Account abuse
- Hard to rotate (need to find every occurrence)

**How to avoid:**
- Environment variables (`.env`)
- Never commit `.env`
- Secret manager for production (AWS Secrets Manager, Vault, etc.)

## 6. No Version Pinning

**What happens:** Integration depends on a library. Library updates, breaks integration.

**Why it's bad:**
- Unannounced failures
- Hard to reproduce old behavior
- Breaks during peak traffic

**How to avoid:**
- `requirements.txt` with pinned versions (`requests==2.31.0`)
- Test before upgrading
- Lockfile committed (`requirements.lock`, `poetry.lock`)

---

# AGENCY PITFALLS

## 1. Shared IP for High-Volume Client

**What happens:** One client sends spam. Their reputation drags down shared IP, affecting all clients.

**Why it's bad:**
- All clients' deliverability suffers
- Hard to isolate
- Reputation recovery takes weeks

**How to avoid:**
- Dedicated IPs for high-volume senders
- Monitor each client's complaint/bounce rate
- Terms of service clearly prohibit spam

## 2. No White-Label

**What happens:** Client logs in and sees "HighLevel" branding everywhere.

**Why it's bad:**
- Client questions value of agency fee
- Can bypass agency by going direct
- Brand dilution

**How to avoid:**
- Enable white-label on day 1
- Custom domain (app.youragency.com)
- Custom branded mobile app if possible
- Custom email sender

## 3. Over-Permissioning Users

**What happens:** Every user given "Admin" because "easier."

**Why it's bad:**
- One mistake by one user = account-wide damage
- Security breach affects everything
- Audit trail useless (too many admins)

**How to avoid:**
- Minimum permissions per role
- Sales rep: contacts + pipeline only
- Marketer: workflows + campaigns only
- Admin: reserved for agency staff

## 4. No Offboarding Process

**What happens:** Terminated employee retains access for months.

**Why it's bad:**
- Data theft risk
- Malicious action risk
- Compliance violation

**How to avoid:**
- Offboarding checklist (revoke access, rotate keys)
- Same-day access removal on termination
- Audit log review post-departure

## 5. No Snapshot System

**What happens:** Every new client build is from scratch.

**Why it's bad:**
- 10x more work per client
- Inconsistent quality
- Can't scale agency

**How to avoid:**
- Build reusable snapshots per industry/use case
- Update snapshots as patterns improve
- Document snapshot contents

## 6. No Contract / SLA

**What happens:** Client complains about response time. No documented expectation.

**Why it's bad:**
- Scope creep
- Over-delivery (losing money)
- Under-delivery (losing client)

**How to avoid:**
- Clear contract
- Defined SLA (response time, uptime)
- Change order process for scope changes

## 7. Letting Clients Edit Without Training

**What happens:** Client edits workflow, breaks it, demands free fix.

**Why it's bad:**
- Agency time lost
- Relationship strained
- Client frustrated at their own mistake

**How to avoid:**
- Training video on what client can/can't edit
- Permissions prevent edits in critical workflows
- "Edit mode" requires checking out a ticket

---

# CERTIFICATION EXAM PITFALLS

## 1. Confusing Custom Field vs Custom Value

**Trap:** "You need to store the same business phone across all templates." Wrong answer: Custom Field. Right answer: Custom Value.

**Remember:** Custom FIELD = per-contact. Custom VALUE = global.

## 2. Confusing Tag vs Smart List

**Trap:** "Dynamically filter contacts matching criteria." Wrong: Tag. Right: Smart List.

**Remember:** Tag = static label. Smart List = dynamic filter.

## 3. Confusing Campaign vs Workflow

**Trap:** "Send branching personalized sequence." Wrong: Campaign. Right: Workflow.

**Remember:** Campaign = scheduled blast. Workflow = event-driven with branches.

## 4. Confusing Funnel vs Website

**Trap:** "Linear conversion path with upsell." Wrong: Website. Right: Funnel.

**Remember:** Funnel = one goal, linear. Website = multi-page navigation.

## 5. Forgetting A2P 10DLC Is US-Only

**Trap:** Question assumes A2P 10DLC applies to Canadian or UK SMS.

**Remember:** A2P 10DLC = US only. Other countries have their own rules.

## 6. Not Knowing Calendar Types Precisely

**Trap:** "Multiple reps rotating" → Right answer: Round Robin (easy). But "Multiple reps attending together" → Right answer: Collective (often confused).

**Remember:** Round = rotate. Collective = all attend.

## 7. Overlooking Compliance Questions

**Trap:** Compliance feels "boring" so skimmed during study. Exam has 5% compliance — often the difference between pass and fail at 80%.

**Remember:** Know GDPR, HIPAA+BAA, CAN-SPAM, A2P, CCPA basics cold.

## 8. Misreading Scenario Questions

**Trap:** Long scenario, key detail hidden. "They want to reach EU customers" buried in paragraph 3 → answer must account for GDPR.

**Remember:** Read scenarios twice. Underline geo/compliance/scale hints.

## 9. Assuming Features Exist as They Did Before

**Trap:** HighLevel updates. Some features move or change.

**Remember:** Verify on the current platform. Don't answer from 2-year-old tutorials.

## 10. Running Out of Time

**Trap:** Spending 5 minutes per question on first pass. Run out before end.

**Remember:** Flag, move on, return. Never let one question eat 10% of your time.

---

# ROOKIE MISTAKES TO AVOID

30+ common rookie mistakes with the correct approach.

## 1. Not Reading the Docs
- **Mistake:** Jumping in without reading HighLevel's help docs
- **Fix:** Spend 2-3 hours in the help center before building anything complex

## 2. Copying Random YouTube Tutorials Blindly
- **Mistake:** Following a 2-year-old tutorial exactly
- **Fix:** Understand the WHY, adapt to current platform and your use case

## 3. Not Using Test Accounts
- **Mistake:** Testing workflows on real contacts
- **Fix:** Always have test contacts tagged `test-internal`

## 4. Building Without Requirements
- **Mistake:** Jumping to "build a workflow" without defining the goal
- **Fix:** Write down: trigger, steps, exit conditions, success metrics

## 5. Skipping Mobile Testing
- **Mistake:** Desktop-only testing
- **Fix:** Test on actual mobile device, not responsive mode only

## 6. No Version Control for Configurations
- **Mistake:** Changes made, undo not possible
- **Fix:** Export snapshots before major changes

## 7. Overcomplicating Simple Workflows
- **Mistake:** 50-step workflow for a welcome email
- **Fix:** Simplest version first. Add complexity only when needed.

## 8. Underestimating Timing
- **Mistake:** "A workflow takes 5 minutes to build"
- **Fix:** Budget 2-4x initial estimate, especially with testing

## 9. Not Documenting
- **Mistake:** "I'll remember what this does"
- **Fix:** Document every workflow, tag, custom field

## 10. Ignoring Deliverability
- **Mistake:** "Just send the emails"
- **Fix:** Warm up domain, authenticate (SPF/DKIM/DMARC), monitor bounces

## 11. Not Backing Up
- **Mistake:** Assuming platform backs up everything
- **Fix:** Monthly exports of contacts, workflows, templates

## 12. Giving Everyone Admin Access
- **Mistake:** "Easier for now"
- **Fix:** Minimum permissions per role from day 1

## 13. Using Obvious Passwords
- **Mistake:** `password123`, `business2026`
- **Fix:** Password manager, strong random passwords, 2FA

## 14. Committing API Keys
- **Mistake:** Key in git repo
- **Fix:** `.env` file, `.gitignore`, rotate quarterly

## 15. No Staging Environment
- **Mistake:** Testing in production
- **Fix:** Separate sub-account for testing changes

## 16. Not Using Merge Fields
- **Mistake:** "Hi there" generic emails
- **Fix:** `{{contact.first_name}}` with fallback

## 17. Ignoring Unsubscribes
- **Mistake:** Unsubscribed contacts still messaged
- **Fix:** HighLevel auto-honors — verify in testing

## 18. Assuming Workflow Ran
- **Mistake:** Building workflow, never verifying execution
- **Fix:** Check workflow history/stats

## 19. Not Using the Mobile App
- **Mistake:** Desktop-only workflow, miss on-the-go needs
- **Fix:** Use the LeadConnector mobile app; test mobile experience

## 20. No Error Monitoring
- **Mistake:** Silent failures pile up
- **Fix:** Dashboard for workflow errors, integration failures

## 21. Hardcoding URLs
- **Mistake:** Booking link typed in every email
- **Fix:** Custom Value for booking link

## 22. Not Using Templates
- **Mistake:** Retyping similar emails
- **Fix:** Template library for common messages

## 23. Ignoring GDPR/CCPA
- **Mistake:** "We're small, doesn't apply to us"
- **Fix:** Know the rules, comply proactively

## 24. Writing Long-Winded SMS
- **Mistake:** 400-char SMS
- **Fix:** Under 160 chars; use trigger link for details

## 25. Building in Isolation
- **Mistake:** Not consulting stakeholders
- **Fix:** Review with team/client before going live

## 26. Not Naming Things Well
- **Mistake:** "Workflow", "Workflow (1)", "Workflow (2)"
- **Fix:** Convention: `trigger-purpose-audience`

## 27. Forgetting to Publish
- **Mistake:** Workflow built, left in Draft
- **Fix:** Checklist before "done" includes publish step

## 28. Not Filtering Test Data
- **Mistake:** Test contacts in reports
- **Fix:** Tag test contacts, filter them out of reports

## 29. Copy-Paste Without Adjusting
- **Mistake:** Duplicating workflow, forgetting to change trigger
- **Fix:** Post-duplicate checklist: verify trigger, tags, names, templates

## 30. Not Tracking Metrics
- **Mistake:** Building workflows with no KPIs
- **Fix:** Define success metric per workflow (open rate, conversion, response)

## 31. Overusing AI/Automation
- **Mistake:** Automating what needs human touch (VIP clients, complaints)
- **Fix:** Manual Actions for high-value/sensitive moments

## 32. Underusing Automation
- **Mistake:** Staff manually doing repeatable tasks
- **Fix:** Identify repetitive work, automate it

## 33. Not Learning from Cancellations/Unsubscribes
- **Mistake:** Ignoring exit signals
- **Fix:** Exit survey, analyze reasons, improve

## 34. Skipping the Mock Exam
- **Mistake:** Going straight to real cert
- **Fix:** Mock exam minimum twice, 85%+ before scheduling real

## 35. Studying Passively
- **Mistake:** Just reading docs, not building
- **Fix:** Build Sunrise Wellness Studio hands-on throughout study

---

# WHEN YOU HIT A PITFALL

If you or your client fall into one of these:

1. **Don't panic.** Most are recoverable.
2. **Assess damage.** What's actually broken? What's at risk?
3. **Stop the bleeding.** Pause the affected workflow/campaign.
4. **Communicate.** Tell affected stakeholders before they find out.
5. **Fix root cause, not just symptom.**
6. **Document.** Add to your team's runbook so it doesn't recur.
7. **Postmortem.** What process would have caught this?

---

# FINAL REMINDERS

- Every mistake in this doc has been made by multiple agencies. You're not alone.
- Preventing one of these can save thousands of dollars.
- The best agencies institutionalize avoidance via checklists and reviews.
- When in doubt: test, document, monitor.

Good luck building, and good luck on the cert exam.
