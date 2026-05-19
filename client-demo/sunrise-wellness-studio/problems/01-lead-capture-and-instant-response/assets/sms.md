# #01 — SMS Templates

> Three SMS messages used in the lead capture flow. Keep them short, human, and link-light (one URL max). Resolve merge fields at send time.

---

## SMS A — Instant Response (the critical 5-min message)

**Template name:** `01 — Instant Lead Response`

**Trigger:** Sent within 60 seconds of form submission, via #01 Instant Response Workflow.

**From:** `{{custom_values.business.sms_number}}`

**Body (160 chars target):**

> Hey {{contact.first_name}}, it's Morgan from Sunrise ☀️ Welcome! Pick a time that fits your week and we'll see you soon: {{custom_values.business.booking_url}}
> 
> Reply HELP for anything, STOP to opt out.

**Character count:** ~165 — fits in 1 SMS segment.

**Why this works:** First-name, owner-personal ("Morgan"), warm emoji (one only), single CTA link, short. Sent fast enough that the lead's still on the thank-you page — feels magical.

---

## SMS B — 2hr Nudge (if no reply, no booking)

**Template name:** `01 — 2hr Nudge`

**Trigger:** Sent 2 hours after submission IF contact has not booked AND has not replied.

**From:** Same number.

**Body:**

> {{contact.first_name}}, no rush — just making sure you got the booking link. Here it is again: {{custom_values.business.booking_url}}
> 
> Or reply with what time of day works best and I'll find you a class.

**Character count:** ~175 — single segment.

**Why this works:** Acknowledges no-pressure ("no rush"), gives the link again (lower friction than scrolling back to the first text), offers a conversational fallback ("reply with what time works"). The fallback often gets a response when the link doesn't.

---

## SMS C — Day-3 Last Touch (handed off to long-tail nurture, included here for completeness)

**Template name:** `01 — Day 3 Last Touch`

**Trigger:** Day 3 after submission IF still no booking AND no reply. After this SMS, contact exits the #01 workflow and enters the long-tail "Lead Nurture — 30-Day Drip."

**From:** Same number.

**Body:**

> Hey {{contact.first_name}} — last quick text from me. Your 7-day pass is still open if you change your mind: {{custom_values.business.booking_url}}
> 
> If you want me to stop, reply STOP. Otherwise, see you soon hopefully :)

**Character count:** ~190 — single segment.

**Why this works:** "Last quick text" sets expectation that we won't keep nagging. Direct opt-out language reduces complaints. Lighthearted close keeps the door open without being needy.

---

## Reply Handling (manual + auto)

When a lead replies to any of the above SMS messages, GHL routes the reply to the Conversations inbox AND triggers a "reply received" workflow event. Setup:

### Auto-tag on reply

- **Trigger:** Inbound SMS received from contact with tag `lead-contacted` AND NOT `lead-responded`
- **Action:** Add tag `lead-responded`
- **Action:** Exit any active #01 workflow steps (so no 2hr nudge or 24hr email fires)
- **Action:** Internal notification to front desk: "{{contact.first_name}} {{contact.last_name}} just replied — check Conversations"

### Common replies and front-desk response scripts

| If they reply... | Front-desk response |
|---|---|
| A specific time (e.g., "tomorrow 6pm") | Book them via Calendar, reply with confirmation. |
| A question about cost/membership | Send the pricing PDF + reiterate the trial is free. |
| "STOP" or unsubscribe language | GHL auto-handles the STOP keyword. Mark contact `do-not-sms`. |
| "Just looking, not ready" | Reply: "Totally fine — your pass stays active. Text me anytime." Add tag `lead-soft-interest`. |
| Anything emotionally heavy (injury story, anxiety, etc.) | Escalate to owner. Personal reply, not templated. |

---

## SMS Best Practices for This Studio

**Length:** Under 160 chars per message → 1 segment → 1 carrier charge. Over 160 splits into 2 segments and looks worse.

**Tone:** Warm and concrete. Avoid "we" — use "I" (Morgan). Avoid corporate-sounding words ("kindly," "please advise," "in regards to").

**Emoji:** Max one per message. Sunrise emoji ☀️ is the brand emoji of choice. Skip thumbs-up, smileys, etc. — they read younger than the brand target.

**Links:** Maximum one link per SMS. Long URLs degrade trust — use the short branded booking URL (`{{custom_values.business.booking_url}}` which should be a vanity domain like `book.sunrisewellness.com`).

**Compliance:**
- Every SMS includes opt-out language at first contact ("Reply STOP to opt out").
- After STOP is received, tag contact `do-not-sms` immediately — every other workflow checks this tag before sending.
- Marketing-class messages (promotional, not transactional) respect quiet hours: do not send between 9 PM and 8 AM contact-local time. Lead-capture instant-response is **transactional** and exempt from quiet hours (the lead just initiated contact).

**Timing:**
- Instant response: immediate (no delay).
- Subsequent nudges: respect contact's `preferred_workout_time` if known — e.g., for early-morning preference, send 2hr nudge at 6 AM, not 11 PM.
- Default: business hours 8 AM – 9 PM contact-local time.

---

## A/B Test Ideas (after baseline is set)

Hold these for after 30 days of baseline data:

| Test | Variant A (control) | Variant B |
|---|---|---|
| Instant SMS — opener | "Hey {{first_name}}, it's Morgan from Sunrise ☀️" | "{{first_name}}! Got your trial request — welcome ☀️" |
| 2hr nudge — angle | Soft check-in | Specific class invitation ("Tomorrow's 6 PM HIIT has 3 spots — want me to save you one?") |
| Day-3 touch — vibe | Lighthearted close | Loss-aversion close ("Your pass expires in 4 days — here if you want it") |

Test one at a time, run for 2 weeks each, target 50+ leads per variant before declaring a winner.

---

## What Comes Next

Once the lead replies or books a trial, they're handed off to **[#02 Trial-to-Paid Conversion](../02-trial-to-paid-conversion/)** which runs its own 7-day SMS + email sequence to drive conversion to paid membership.

For leads who never engage after the day-3 SMS — they enter the long-tail Lead Nurture drip (separate workflow, monthly cadence, out of scope here).
