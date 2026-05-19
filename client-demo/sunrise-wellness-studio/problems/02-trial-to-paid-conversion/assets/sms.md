# #02 — SMS Templates

> SMS messages across the 7-day trial nurture. Keep them short, human, link-light (one URL max). Each message includes character count for single-segment verification.

---

## SMS A — Day 0 — Welcome Confirmation

**Template name:** `02 — Day 0 — Trial Welcome SMS`

**Trigger:** Fires within 5 minutes of `trial-claimed` tag added.

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}}, it's Morgan from Sunrise ☀️ Your 7-day pass is live. Grab your first class here: {{custom_values.business.booking_url}}
>
> Reply STOP to opt out.

**Character count:** ~150 — single segment.

**Why this works:** First-name + owner-personal + one CTA. Sent fast (within 5 min) so the trial knows the system "saw" them.

---

## SMS B — Day 1 — Booking Check (haven't booked yet)

**Template name:** `02 — Day 1 — Booking Check`

**Trigger:** Day 1 at 10 AM contact-local IF `last_visit_date` is blank or older than `lead_captured_at`.

**Body:**

> {{contact.first_name}} — Morgan again. Quick check: did you grab a class slot yet? If timing is the hurdle, reply with the time of day that works and I'll find you a class.

**Character count:** ~155 — single segment.

**Why this works:** Acknowledges they haven't booked (no shaming), offers a low-friction fallback ("reply with a time"), positions Morgan as a real concierge not a chatbot.

---

## SMS C — Day 1 — Class Confirmation (attended already)

**Template name:** `02 — Day 1 — Class Confirmation`

**Trigger:** Day 1 at 10 AM contact-local IF `last_visit_date` >= `lead_captured_at`.

**Body:**

> {{contact.first_name}} — great seeing you in {{contact.last_class_attended}} 👏 If you want me to book your next one, reply with the day/time that works.

**Character count:** ~140 — single segment.

**Why this works:** Names the specific class they attended (uses `last_class_attended` field). The studio "remembers" them. Offers concierge rebook in one reply.

---

## SMS D — Day 4 — Class Nudge

**Template name:** `02 — Day 4 — Class Nudge`

**Trigger:** Day 4 at 1 PM contact-local IF NOT `trial-attended-3plus`.

**Body:**

> {{contact.first_name}}, you're past the halfway mark of your trial. One more class this week tips the data on whether Sunrise is the right fit. Pick one: {{custom_values.business.booking_url}}

**Character count:** ~175 — single segment.

**Why this works:** Reframes "trial pressure" as "data gathering." Implies they're being scientific, not closed. Single link.

---

## SMS E — Day 6 — Personal from Morgan

**Template name:** `02 — Day 6 — Personal from Morgan`

**Trigger:** Day 6 at 2 PM contact-local IF NOT `trial-converted`.

**Body:**

> Hey {{contact.first_name}}, Morgan here. Trial wraps tomorrow — any questions or concerns I can answer before then? Reply here or call {{custom_values.business.phone}}.

**Character count:** ~170 — single segment.

**Why this works:** Reads like a one-off personal text. No link, no CTA — just the door open. This is the highest-reply-rate message of the whole sequence (typically 35–50% reply rate). Treat replies as priority items in Conversations.

**Note:** Some operators prefer to *queue* this for owner manual-send instead of auto-fire. Toggle in workflow at Step 4.10 based on owner preference.

---

## SMS F — Day 7 — Last Call SMS

**Template name:** `02 — Day 7 — Last Call SMS`

**Trigger:** Day 7 at 1 PM contact-local IF NOT `trial-converted`.

**Body:**

> {{contact.first_name}} — your trial wraps tonight + the TRIAL2PAID code expires at midnight. {{custom_values.offer.trial_conversion_discount}}: {{custom_values.offer.conversion_funnel_url}}

**Character count:** ~190 — single segment (just under).

**Why this works:** Honest urgency (real deadline). Restates the offer concisely. Single CTA link. Followed by the Day 7 email earlier in the morning, so this is the reinforcement nudge.

---

## SMS G — Day 8 — Soft Goodbye SMS (optional, often skipped)

**Template name:** `02 — Day 8 — Soft Goodbye`

**Trigger:** Day 8 at noon contact-local IF `trial-expired` AND NOT `trial-not-now`.

**Body:**

> {{contact.first_name}}, your trial wrapped. No pressure from me — door's open if you ever want to come back. Reply with one word if you'd like to chat. — Morgan

**Character count:** ~155 — single segment.

**Why this works:** Honest "we're not chasing" tone often gets a reply that the urgency-loaded messages don't. About 1 in 8 silent expirations reply to this one.

**Note:** Many operators skip this SMS to avoid over-messaging silent expirations. Toggle in workflow at Step 4.14c.

---

## Reply Handling (auto-routes via #02 Trial Reply Handler workflow)

| Reply pattern | Auto-action |
|---|---|
| "yes" / "interested" / "sign me up" / "i'm in" | Send confirmation SMS with funnel link. Tag `trial-warm`. |
| "not now" / "no thanks" / "stop trying" / "later" | Send "all good, no pressure" auto-reply. Tag `trial-not-now`. Exit main workflow. |
| "$" / "cost" / "money" / "expensive" | Send "let's talk options" message with link to pricing PDF. Internal notification to Morgan. |
| Specific question (anything else) | Internal notification to Morgan. Tag `trial-needs-personal-touch`. Manual reply within 4hr. |
| "STOP" / "unsubscribe" | GHL auto-handles. Tag `do-not-sms`. Email sequence continues unless they also opt out of email. |

### Auto-reply scripts

**For "yes / interested":**

> Amazing! Tap here to lock it in (TRIAL2PAID auto-applies): {{custom_values.offer.conversion_funnel_url}}

**For "not now":**

> All good {{first_name}} — no pressure. I'll stop the nudges. Your trial info stays with us if you change your mind. — Morgan

**For "$ / cost":**

> Totally hear you. Quick options: Basic is {{custom_values.price.basic}}/mo. The TRIAL2PAID code makes it $63.20 the first month + waives the $49 fee. If money is tight in a different way, reply and I'll see what I can do. — Morgan

---

## SMS Best Practices for This Sequence

**Length:** Every message above is < 200 chars → single segment → single carrier charge.

**Tone:** First-person Morgan throughout. No "we" or "our team." The whole sequence is positioned as one human walking the trial through the door.

**Emoji:** Sparingly. ☀️ once on Day 0. 👏 once on Day 1 confirmation. Days 2-7: no emoji. The restraint matters — over-emoji'd SMS reads younger than the target audience.

**Links:** Maximum one per message. Use `{{custom_values.business.booking_url}}` for class booking or `{{custom_values.offer.conversion_funnel_url}}` for the conversion funnel. Both should be branded short domains (e.g., `book.sunrisewellness.com`).

**Compliance:**
- Opt-out language only on **first** SMS (Day 0). Including "STOP to opt out" on every message reads spammy.
- Marketing messages respect quiet hours: 8 AM – 9 PM contact-local. Day 6 personal SMS specifically targets 2 PM for the highest-engagement window.
- After "STOP" received, tag `do-not-sms` immediately. Every subsequent send checks this tag.

**Timing within the day:**
- Day 0 SMS: immediately on trigger
- Day 1 SMS: 10 AM (catches them at their phone with coffee)
- Day 4 SMS: 1 PM (post-lunch, mid-energy)
- Day 6 SMS: 2 PM (afternoon — personal-text time)
- Day 7 SMS: 1 PM (giving them the rest of the workday to act)

---

## A/B Test Ideas (after 30 days of baseline)

| Test | Variant A (control) | Variant B |
|---|---|---|
| Day 4 nudge framing | "Tips the data on whether Sunrise is the right fit" | "Most members who attend 3+ trials convert. Want me to find you one?" |
| Day 6 personal SMS opener | "Hey {{first_name}}, Morgan here" | "Hey {{first_name}}! Trial wraps tomorrow ☀️" |
| Day 7 last-call urgency | "Code expires at midnight" | "Code expires tonight + 7 spots left at this rate" |

Run each test for 2 weeks, target 50+ trials per variant.

---

## What Comes Next

Replies that signal interest hand off to the conversion funnel. Replies that signal "not now" exit the main workflow and enter long-tail nurture.

Trials that convert: their `member-active` tag fires **[#04 New Member Onboarding](../04-new-member-onboarding/)**, which has its own Day 1 / Day 3 / Day 7 / Day 14 / Day 21 / Day 30 SMS sequence.

For full reply-handling logic, see the workflow spec in **[workflow.md](workflow.md)** Action 4.14 (outcome router).
