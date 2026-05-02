# Advanced Challenge 2: Seasonal Program Launch Campaign

**Difficulty:** Advanced
**Time Required:** 4-6 hours
**Prerequisites:** Phase 1 (Days 1-10) + Phase 2 (Days 11-16)

---

## The Challenge

It's January. Sunrise Wellness Studio is launching a "New Year, New You" 6-week transformation program. Price: $497 (one-time). Includes: 3 PT sessions/week, nutrition plan, weekly group accountability class, body composition tracking, private community group, and a final "reveal" event.

Your job: build the ENTIRE launch system in GHL - from teaser campaign to enrollment to delivery to post-program upsell. This simulates a real product launch that agencies and businesses do multiple times per year.

This challenge gives you the WHAT and the WHY, but not step-by-step HOW. Figure out which GHL features to combine and how to wire them together.

---

## The Program Details

**"New Year, New You" 6-Week Transformation**
- **Price:** $497 one-time (or 2 payments of $275)
- **Capacity:** 20 spots maximum
- **Includes:**
  - 18 PT sessions (3/week for 6 weeks)
  - Custom nutrition plan
  - Weekly group accountability class (Saturday 10AM)
  - Private community group access
  - Before/after body composition tracking
  - Final reveal event + awards
- **Early bird:** $397 if enrolled by Jan 10 (save $100)
- **Alumni:** Past program graduates get 15% off

---

## What You Need to Build

### Phase A: Pre-Launch (Teaser & Waitlist)

Build a teaser campaign that starts 2 weeks before enrollment opens.

**1. Teaser Funnel Page**
- Headline: "Something big is coming to Sunrise Wellness in January..."
- Waitlist form captures: Name, Email, Phone, "What would you want most from a transformation program?" (open text)
- No pricing or program specifics revealed yet - build anticipation
- Thank-you page: "You're on the list. We'll let you know first."

**2. Teaser Email Sequence (3 emails over 7 days)**
- **Email 1 (Day 1):** "Big announcement coming..." - pure curiosity, no details
- **Email 2 (Day 4):** "Here's a hint..." - reveal it's a transformation program, share a success story from a past participant
- **Email 3 (Day 7):** "Tomorrow we open enrollment..." - urgency, waitlist members get 24-hour early access before the general list

**3. Smart List:** "Transformation Waitlist" - built from tag assignment, not manual adds

**4. Pipeline:** "Transformation Program" with stages:
- Waitlist → Enrolled → In Program → Completed → Alumni

---

### Phase B: Launch (Enrollment)

Open enrollment with full details. Waitlist gets 24 hours head start.

**1. Sales Funnel**
- **Page 1:** Full program details - schedule, what's included, testimonials section, FAQ accordion, coach bios
- **Order form:** $497 one-time OR 2x $275 payment plan
- **Coupons:** EARLYBIRD ($100 off, expiration date Jan 10) and ALUMNI (15% off, restricted to contacts tagged "transformation-alumni")
- **Spots counter:** Display "X of 20 spots remaining" - use a custom value or custom field you update as enrollments come in

**2. Launch Email Sequence (5 emails over 5 days)**
- **Email 1:** "Enrollment is OPEN" - sent to waitlist ONLY, 24 hours before general list
- **Email 2:** "Meet your coaches" - sent to full list the next day
- **Email 3:** "Success stories" - social proof, before/after highlights
- **Email 4:** "Early bird ends tomorrow" - urgency for EARLYBIRD coupon expiry
- **Email 5:** "Final spots remaining" - scarcity, hard deadline

**3. Enrollment Workflow (triggered by payment)**
- Payment received → Add tag "transformation-enrolled"
- Move contact to "Enrolled" stage in Transformation pipeline
- Send confirmation email: program start date, session schedule, what to bring day one, parking info
- Add to private community group
- Send calendar booking link for first PT session
- Internal notification to studio manager: "New enrollment! [Contact Name] - [X] of 20 spots now filled"
- If 20th enrollment → trigger "SOLD OUT" email to remaining waitlist and general list, update funnel page

**4. Waitlist Non-Enrollment Workflow**
- 3 days after launch: if waitlist member does NOT have "transformation-enrolled" tag → send personal follow-up ("We noticed you haven't signed up yet - any questions?")
- 5 days after launch: "Only [X] spots left - we'd hate for you to miss this"
- After enrollment window closes (or sold out): "Sorry you missed this round. Want first access to the next one?" → re-tag for future launch priority

---

### Phase C: Program Delivery (6 Weeks)

Automate the participant experience so the studio delivers a premium feel without manual work.

**1. Weekly Program Emails (6-week drip)**
- **Week 1:** "Welcome! Here's your week 1 schedule, nutrition plan PDF, and community group link"
- **Week 2:** "Week 1 is done! Here's what to focus on this week + a quick tip"
- **Week 3:** "Halfway point check-in - how are you feeling? Take a progress photo"
- **Week 4:** "Past halfway - push through! Here's a motivation boost from past alumni"
- **Week 5:** "One more week - finish strong! Reminder: take your 'after' measurements"
- **Week 6:** "The reveal event is THIS Saturday! Here's what to expect, what to wear, invite a guest"

**2. Weekly Check-In Automation**
- Every Friday at 6PM, enrolled participants get a check-in message
- Three trigger links in the email/SMS: "How's your week going?" → Great / Okay / Struggling
- **If "Great"** → log it, no action needed
- **If "Okay"** → log it, send encouragement email with tips
- **If "Struggling"** → immediately alert the assigned coach via internal notification, send a supportive email, and offer a free one-on-one check-in session (calendar link)

**3. Community Engagement Prompts**
- Automated weekly discussion prompts posted or emailed to the group:
  - Week 1: "What's your #1 goal for this program?"
  - Week 2: "Share a small win from this week"
  - Week 3: "Post your halfway progress photo"
  - Week 4: "What's been the hardest part so far?"
  - Week 5: "Who's been your biggest support?"
  - Week 6: "Describe this experience in one word"

---

### Phase D: Post-Program (Upsell & Retention)

Convert program participants into long-term recurring members. This is where the money is.

**1. Completion Workflow**
- Move pipeline stage to "Completed"
- Remove tag "transformation-enrolled", add tag "transformation-alumni"
- Congratulations email with a results summary template (they fill in their numbers)
- Certificate of completion (email with designed image or PDF)
- Google review request (direct link to your GMB listing, wait 2 days after completion)
- Testimonial request via trigger link: "Share your transformation story" → routes to a simple form, response gets tagged for marketing use

**2. Membership Upsell Sequence (starts 3 days post-completion)**
- **Email 1:** "Don't lose your momentum - your body is in its best rhythm right now. Continue with a membership."
  - Special offer: 30% off first 3 months of ANY membership tier ($79 / $149 / $249)
  - Unique coupon: ALUMNI30
- **Email 2 (Day 5):** "Your transformation group misses you" - community/belonging angle, emphasize the group classes they'd lose access to
- **Email 3 (Day 8):** "Alumni pricing expires in 48 hours" - hard deadline, direct order form link

**3. Alumni Long-Term Management**
- Tag "transformation-alumni" persists permanently for segmentation
- Quarterly "Alumni check-in" email: "How are you maintaining your results? Here's a free workout plan"
- Future program launches: alumni get first-access email (before waitlist, before general) + automatic ALUMNI discount code
- Track alumni-to-member conversion rate via pipeline reporting

---

## Constraints & Realism

These constraints reflect what you'd face in a real build:

1. **You only have one sub-account** - all contacts (waitlist, enrolled, alumni, regular members) live in the same CRM. Your tagging and segmentation must be airtight so the wrong people don't get the wrong emails.
2. **The program has a hard start date** - your delivery emails must fire based on calendar dates, not relative to enrollment date. Everyone starts Week 1 together.
3. **Capacity is real** - you need a reliable way to stop enrollments at 20. What happens if payment #21 comes through? Plan for it.
4. **Payment plans complicate things** - someone on a 2-payment plan who misses payment #2 is still in the program. How do you handle failed payments? Do they lose community access?
5. **The reveal event needs RSVPs** - you need to know how many guests are coming. Build a simple RSVP mechanism.

---

## Hints (only read if stuck)

<details>
<summary>Hint 1: Managing limited capacity</summary>
Create a custom value like {{transformation.spots_remaining}} and decrement it manually (or via webhook) with each enrollment. Reference it in emails and on the funnel page. When it hits 0, have a workflow swap the funnel page to a "Sold Out - Join Waitlist for Next Round" version, or redirect to a waitlist form. For the overflow problem: add a condition at the start of the enrollment workflow that checks if spots > 0 before processing.
</details>

<details>
<summary>Hint 2: Payment plan setup</summary>
Create two products in Payments: "Transformation - Full Pay" ($497 one-time) and "Transformation - Payment Plan" ($275 recurring, 2 installments). Both products, when purchased, should trigger the same enrollment workflow via a shared tag. For failed second payments, set up a separate "Payment Failed" workflow that sends a reminder, retries in 3 days, and alerts the manager if still unpaid after 7 days.
</details>

<details>
<summary>Hint 3: Calendar-based delivery emails</summary>
Since all participants start together, use a single workflow with "Wait until date" steps tied to the actual program calendar. Week 1 email sends Jan 15 (program start), Week 2 sends Jan 22, etc. This is simpler than relative waits and ensures everyone gets the same email on the same day. Enroll all "transformation-enrolled" contacts into this workflow on program start day, or set it up so the tag addition triggers entry and the first Wait step holds them until Jan 15.
</details>

<details>
<summary>Hint 4: Trigger links for check-ins</summary>
Trigger links are URLs that, when clicked, apply a tag or fire a workflow. Create three trigger links: "checkin-great", "checkin-okay", "checkin-struggling". Put them in your weekly check-in email as the three response buttons. Each one fires a different branch in your check-in workflow. Remove the previous week's check-in tags before sending the next week's check-in so tags stay current.
</details>

---

## Evaluation Criteria

Rate yourself honestly. A working build hits at least 6 of 8.

- [ ] Teaser funnel captures waitlist leads and builds anticipation with a 3-email sequence
- [ ] Sales funnel includes order form with payment plan, coupons (EARLYBIRD + ALUMNI), and spots counter
- [ ] Enrollment workflow handles payment → tag → pipeline → confirmation → scheduling → internal alert
- [ ] Waitlist non-enrollers get follow-up nudges and a "next round" capture
- [ ] 6-week delivery emails fire on correct calendar dates for all participants
- [ ] Weekly check-in system catches struggling participants and alerts coaches
- [ ] Post-program workflow handles completion → alumni tag → review request → testimonial capture
- [ ] Upsell sequence drives membership conversion with time-limited alumni pricing

---

## Apply to Other Businesses

Don't just read these - actually think through how the mechanics change for each business.

### BrightSmile Dental Version
**"Smile Makeover Package"** - $2,500 cosmetic dentistry bundle (professional whitening + deep cleaning + cosmetic consultation + follow-up).
- **Teaser campaign:** "New year, new smile" - target existing patients who've asked about cosmetic work (use past appointment notes or tags)
- **Capacity:** Limited to 10 patients per month (dentist chair time is the constraint)
- **Delivery:** 3-visit program with automated scheduling between visits (visit 1: consultation + cleaning, visit 2: whitening session 1, visit 3: whitening session 2 + final photos)
- **Payment plan:** 3x $867 monthly
- **Post-program upsell:** Maintenance plan subscription ($49/month for quarterly touch-ups), referral to orthodontic partner
- **Key difference:** Scheduling is appointment-based, not class-based. Your delivery automation revolves around booking confirmations and pre-visit reminders rather than weekly group emails.

### Elevate Digital Agency Version
**"90-Day Growth Sprint"** - $7,500 intensive marketing engagement for new clients.
- **Teaser campaign:** "We're taking on 5 new clients for an intensive growth sprint" - target warm prospects from past discovery calls who didn't close
- **Capacity:** 5 clients maximum (agency bandwidth is the constraint)
- **Delivery:** Weekly strategy calls + full marketing implementation (ads, email, SEO). Automated weekly report emails, monthly milestone check-ins, Slack/community group for sprint clients
- **Payment plan:** 3x $2,700 monthly
- **Post-sprint upsell:** Convert to ongoing retainer ($2K-$10K/month depending on services). "You've seen what 90 days can do - imagine 12 months"
- **Key difference:** B2B sales cycle is longer. Your enrollment workflow probably includes a qualifying call before payment. The "check-in" system tracks client satisfaction AND campaign performance metrics, not physical progress.

---

## Bonus Extensions

Only attempt these after the core build is solid.

1. **Results Showcase Funnel Page**
   Build a public-facing "Transformation Results" page that displays before/after stories. Pull content from testimonial trigger link responses. This becomes a permanent sales asset for future program launches.

2. **Alumni Community Tier**
   Create a separate "Transformation Alumni" group or channel in your community. Alumni get exclusive content: advanced workout plans, nutrition deep-dives, early access to events. This keeps them engaged even if they don't convert to a full membership immediately.

3. **Automated NPS + Feedback Survey**
   At program end, send an NPS survey (0-10 scale). Route responses:
   - **9-10 (Promoters):** Immediate testimonial request + referral program invite
   - **7-8 (Passives):** "What would have made it a 10?" follow-up, still send upsell sequence
   - **0-6 (Detractors):** Alert manager immediately, personal outreach within 24 hours, delay upsell sequence, offer a make-good (free month of membership)

4. **Relaunch Template**
   Document your entire build so you can duplicate it for "Spring Shred" (April), "Summer Body" (June), and "Holiday Reset" (November). The funnel pages, workflows, and email sequences should be copy-and-tweak, not rebuild-from-scratch. Think about what you'd templatize vs. what changes each round.
