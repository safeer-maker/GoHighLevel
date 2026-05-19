# #04 — SMS Templates

> Five primary SMS templates across the 30-day onboarding sequence. Tier-conditional and attendance-conditional variants noted. Every message single-segment.

---

## SMS A — Day 1 — Personal Welcome SMS

**Template name:** `04 — Day 1 — Personal Welcome SMS`

**Trigger:** Day 1 of membership at 10 AM contact-local.

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}}, Morgan here ☀️ Just wanted to say welcome personally. If anything's confusing about the app, booking, or anything else — text me here. I read everything.

**Character count:** ~190 — single segment (just under).

**Why this works:** Personal-tone owner SMS on Day 1 sets the relationship. No CTA, no link — just human. About 25% of new members reply, which gives Morgan a real conversation hook.

---

## SMS B — Day 3 — No Visit Yet (Gentle)

**Template name:** `04 — Day 3 — No Visit Yet (gentle)`

**Trigger:** Day 3 of membership at 11 AM contact-local. IF `last_visit_date` is before `membership_start_date`.

**Body:**

> {{contact.first_name}} — Morgan again. Noticed you haven't booked your first class yet. Totally normal week-1 hurdle. If schedule is the block, reply with what time of day works.

**Character count:** ~180 — single segment.

**Why this works:** Names the gap without shaming ("totally normal"). Offers concierge fallback ("reply with a time"). Pushes for engagement without sending a link they'd ignore.

---

## SMS C — Day 8 — PT Booking Nudge (Tier-Conditional)

**Template name:** `04 — Day 8 — PT Booking Nudge`

**Trigger:** Day 8 of membership at 6 PM contact-local. IF `membership_tier` IN (Premium, VIP) AND `last_pt_session_date` is empty.

**Body:**

> Hey {{contact.first_name}}, your membership includes PT sessions. Want me to set up your first one with {{contact.assigned_trainer}}? Reply with a day/time and I'll find a slot.

**Character count:** ~180 — single segment.

**Why this works:** Surfaces a benefit they may not have noticed. Conversational fallback ("reply with a day/time") avoids the "click this link" friction that often kills first-PT bookings.

---

## SMS D — Day 14 — Milestone Celebrate (Healthy version)

**Template name:** `04 — Day 14 — Milestone Celebrate`

**Trigger:** Day 14 of membership at 10 AM contact-local. IF `visits_last_30_days >= 3`.

**Body:**

> {{contact.first_name}}, 2 weeks in with {{contact.visits_last_30_days}} visits 👏 You're past the early-quitter zone. Genuinely impressed. Keep going. — Morgan

**Character count:** ~155 — single segment.

**Why this works:** Specific numbers ("with X visits") make it feel like the studio noticed. Named compliment from Morgan personally. No CTA — celebration only.

---

## SMS E — Day 21 — Goal Review Reminder

**Template name:** `04 — Day 21 — Goal Review Reminder`

**Trigger:** Day 21 of membership, 6 hours after the Day 21 email fires (so SMS lands afternoon if email lands morning).

**Body:**

> {{contact.first_name}}, your 30-min goal review with {{contact.assigned_trainer}} is open. Quick way to lock in your next 90 days: {{custom_values.business.booking_url}}

**Character count:** ~175 — single segment.

**Why this works:** Reinforces the email with a one-tap booking link. Names the trainer for warmth. Specific value prop ("lock in next 90 days").

---

## SMS F — Day 25 — Goal Review Final Nudge (if not booked)

**Template name:** `04 — Day 25 — Goal Review Final Nudge`

**Trigger:** Day 25 of membership. IF goal review not yet booked.

**Body:**

> {{first_name}}, last gentle nudge on the goal review — really the most useful 30 min you'll spend at the studio this month. Grab a slot: {{custom_values.business.booking_url}}

**Character count:** ~180 — single segment.

**Why this works:** Last touch (not a string of nudges). Honest framing ("most useful 30 min") rather than urgency.

---

## SMS G — Day 30 — Graduation

**Template name:** `04 — Day 30 — Graduation`

**Trigger:** Day 30 of membership at 11 AM contact-local. Fires alongside the Day 30 email.

**Body:**

> 30 days in, {{contact.first_name}} ☀️ Officially past the danger zone. You're part of the team now. — Morgan

**Character count:** ~110 — single segment.

**Why this works:** Short, celebratory, named. Confirms what the email said. No link — let the email carry the CTAs.

---

## SMS H — Day 17 Escalation — From Morgan (At-Risk Critical)

**Template name:** `04 — Day 17 — Owner Escalation SMS`

**Trigger:** Day 17 IF still zero visits AND tag `risk-critical` present.

**Body:**

> Hey {{first_name}}, Morgan here. 17 days in and you haven't been able to come yet. Totally happens. Anything I can do? Even a 10-min call works — text or call {{custom_values.business.phone}}.

**Character count:** ~200 — single segment (right at the edge).

**Why this works:** Personal escalation from the owner. Specific outreach offer ("10-min call"). Zero pressure language. This is the highest-reply-rate SMS in the whole onboarding sequence for at-risk members (35-45% reply rate).

---

## SMS I — Owner-Triggered Save SMS (manual fire)

**Template name:** `04 — Owner Save SMS`

**Trigger:** Tag `owner-save-sms` added manually by Morgan from the contact card.

**Body:**

> Hey {{first_name}}, Morgan here personally. I noticed you joined 2 weeks ago and haven't been able to make it in. Totally happens; life is a thing. If schedule is the block, just text me back with what time of day works for you and I'll find you a class. If something else is in the way, I'd love to know — I read every reply. — Morgan

**Character count:** ~340 — splits into 2 segments. Worth it for personal-touch save.

**Why this works:** Longer = more human. Reads like a one-off text. The "I read every reply" reassures. Used as a save shot for members the system flagged but Morgan wants to send the message at the exact right moment (e.g., after seeing a question in Conversations).

---

## Reply Handling

| Inbound reply | Workflow action |
|---|---|
| Specific day/time (e.g., "tuesday 6pm") | Internal notification to front desk. Tag `onboarding-front-desk-action`. Front desk books manually. |
| "schedule" / "time" / "busy" / "work" | Send: *"Totally — what's your typical free window? Mornings? Lunchtime? Evenings? I'll suggest 3 classes that fit."* |
| "nervous" / "scared" / "intimidated" / "anxious" | Send: *"100% normal. Want me to set you up with a trainer for the first one? They'll meet you at the door and walk you through. Reply YES and I'll book it."* |
| "pause" / "hold" | Internal notification to Morgan + front desk. Tag `member-pause-requested`. Manual pause processed within 24hr. |
| "cancel" / "not for me" / "refund" | Internal notification to Morgan. Tag `member-cancel-requested`. Manual cancel within 24hr. (Don't auto-cancel — let Morgan have one save-call attempt.) |
| General question | Internal notification to Morgan. Tag `onboarding-needs-response`. |
| "STOP" | GHL auto-handles. Tag `do-not-sms`. Onboarding emails continue. |

---

## SMS Best Practices for Onboarding

**Length:** Every message above is single-segment except SMS I (intentional). Test merge-field expansion before publishing.

**Tone:**
- Days 1 and 3: warm, personal, conversational — Morgan voice.
- Days 8, 21, 25: practical, action-oriented.
- Day 14: celebratory or empathic depending on attendance branch.
- Day 17 (at-risk): radically human, no marketing language.
- Day 30: short and warm.

**Emoji:**
- ☀️ on Day 1 and Day 30 (the brand emoji bookending the sequence).
- 👏 on Day 14 healthy version.
- All other messages: no emoji.

**Links:**
- Days 21, 25: booking URL.
- Days 1, 3, 8, 14, 17, 30: no links — the goal is reply, not click.

**Compliance:**
- Opt-out language only on the very first member SMS (the conversion-confirmation SMS from #02, not an onboarding SMS). Onboarding sequence assumes opt-in carried over.
- Marketing-class respect 8 AM – 9 PM contact-local quiet hours for all messages.
- After "STOP," tag `do-not-sms`; email sequence continues unless they also opt out of email.

**Timing precision:**
- Day 1: 10 AM (morning coffee window)
- Day 3: 11 AM (mid-morning, less inbox-noisy)
- Day 8: 6 PM (evening planning window for tomorrow's PT booking)
- Day 14: 10 AM
- Day 17 escalation: 2 PM (personal-text afternoon window)
- Day 21: 6 hr after email (afternoon)
- Day 25: noon
- Day 30: 11 AM (alongside graduation email)

---

## A/B Test Ideas

| Test | Variant A (control) | Variant B |
|---|---|---|
| Day 1 SMS opener | "Morgan here" | "{{first_name}}! Made it through Day 1 ☀️ I'm Morgan, owner here." |
| Day 14 healthy celebration | Numbers + congrats | Numbers + "Quick ask: leave us a Google review while you're feeling good? Link: ..." |
| Day 17 escalation | Morgan voice, offer call | Morgan voice, offer free PT session as save: "...want me to comp you a PT with {{contact.assigned_trainer}} to break the seal?" |

Run for 30 days per variant, target 30+ new members per variant.

---

## What Comes Next

After Day 30, the contact handoffs to **[#05 Retention](../../05-retention-and-churn-prevention/)**. The retention SMS cadence is much sparser (monthly check-ins, attendance-pattern-triggered nudges) vs. onboarding's weekly cadence.

For the workflow that orchestrates these SMS alongside emails and the pipeline transitions, see **[workflow.md](workflow.md)**.
