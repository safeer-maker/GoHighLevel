# #03 — SMS Templates

> Five SMS messages across the appointment + no-show recovery flow. The SMS layer does most of the work here — email is supporting cast.

---

## SMS A — 24hr Confirmation Reminder

**Template name:** `03 — 24hr Confirm SMS`

**Trigger:** 24 hours before appointment start. Respects 8 AM – 9 PM contact-local quiet hours.

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}} — {{appointment.calendar_name}} tomorrow at {{appointment.start_time_short}} with {{appointment.trainer_name}}. Reply C to confirm or R to reschedule. ☀️

**Character count:** ~155 — single segment.

**Why this works:** The 1-letter reply (C/R) is the key. Friction-free for the member, action-rich for the workflow. About 70% of members confirm at this step, dramatically suppressing no-shows.

---

## SMS B — 2hr Final Reminder

**Template name:** `03 — 2hr Reminder SMS`

**Trigger:** 2 hours before appointment start. Skip if `apt-cancelled` or `apt-rescheduled` already set.

**Body:**

> {{contact.first_name}}, see you at {{appointment.start_time_short}} for {{appointment.calendar_name}}. We're at {{custom_values.business.address_short}} — parking out front. Reply R if you need to move it.

**Character count:** ~190 — single segment (just under).

**Why this works:** Practical (address, parking note), low-effort opt-out ("Reply R"), no emoji clutter. The 2hr window catches forgetting-the-appointment in real time.

---

## SMS C — Post No-Show, T+2 hours

**Template name:** `03 — Post No-Show — 2hr`

**Trigger:** 2 hours after appointment marked No-Show. Skip if member already rebooked.

**Body:**

> {{contact.first_name}} — we missed you at {{appointment.start_time_short}} today. No drama from us. Want to grab a new slot? {{appointment.reschedule_url}}

**Character count:** ~150 — single segment.

**Why this works:** "Missed you" — not "you missed". No guilt vocabulary. Immediate one-tap rebook. The 2hr wait (not instant) is intentional — sending while the trainer is *literally still sitting there* reads as automated guilt-trip.

---

## SMS D — Post No-Show, T+72hr Final from Morgan

**Template name:** `03 — Post No-Show — 72hr Final`

**Trigger:** 72 hours after no-show. Skip if member rebooked OR cancelled membership.

**Body:**

> Hey {{contact.first_name}}, Morgan here. Just personally checking — everything OK? If schedule shifted or you need to pause for a bit, reply here. We're flexible.

**Character count:** ~160 — single segment.

**Why this works:** This one is intentionally human-toned (no link, no CTA). Reads as a real text from a real person, not the system. About 1 in 4 silent no-shows reply — and a good chunk of those replies surface a real issue (injury, life event, money) that's solvable.

**Note:** This is the message that retains. Don't auto-fire if the owner prefers manual send — toggle in workflow.

---

## SMS E — Rebook Confirmation (auto-reply when "R" received)

**Template name:** `03 — Rebook Confirmation`

**Trigger:** Inbound SMS from contact tagged `apt-pending` containing "R" or "Reschedule".

**Body:**

> Got it. Pick a new time here: {{appointment.reschedule_url}} — takes 30 seconds. (Or reply with the day/time you want and I'll find a slot.)

**Character count:** ~150 — single segment.

**Why this works:** Provides two paths (self-serve link OR conversational fallback). Members who hate clicking links can reply "tuesday 6pm" and the front desk handles it.

---

## SMS F — Post-Show Thank You (bonus — Step 7 of build.md)

**Template name:** `03 — Post-Appointment Thank You`

**Trigger:** Appointment status → Showed. Calendar is PT-60 or Intro Consult. Wait 1 hour after marked.

**Body:**

> Hey {{contact.first_name}}, great work today 👏 {{contact.assigned_trainer}} said you crushed it. Want to lock in next week? {{custom_values.business.booking_url}}

**Character count:** ~160 — single segment.

**Why this works:** Endorphin-high window. Highest rebook rate of any SMS in the studio. Names the trainer (uses `assigned_trainer` field).

---

## Reply Handling Summary

| Inbound reply | Workflow action |
|---|---|
| "C" / "Confirm" / "yes" / "y" | Add tag `apt-confirmed`. Auto-reply: *"Confirmed, {{first_name}}! See you {{appointment.start_time_short}} ☀️"* |
| "R" / "Reschedule" / "move" | Send SMS E (rebook confirmation). Tag `apt-needs-reschedule`. |
| "cancel" / "can't make it" / "X" | Mark appointment cancelled. Auto-reply: *"Got it — cancelled. Reply BOOK when you're ready for the next one."* |
| Day/time text (e.g., "thursday 5pm") | Internal notification to front desk. Tag `apt-front-desk-action`. Front desk books manually. |
| General question | Internal notification to Morgan. Tag `apt-needs-response`. |
| "STOP" | GHL auto-handles. Tag `do-not-sms`. (Appointment reminders are arguably transactional — but respect the opt-out anyway.) |

---

## SMS Best Practices for Appointment Flow

**Length:** Every message above is single-segment. Don't let merge-field expansion push you over — test with the longest possible trainer name + class name.

**Tone:**
- Reminders: useful, friendly, low-energy.
- No-show recovery: warm, no guilt, name the member's experience ("we missed you" not "you missed us").
- Morgan's 72hr personal SMS: zero corporate language. Reads like a friend.

**Emoji:**
- 24hr reminder: ☀️ once.
- Post-show thank you: 👏 once.
- Everything else: no emoji. Restraint matters.

**Links:**
- Use `{{appointment.reschedule_url}}` where GHL supports per-appointment deep-links (member name + appointment pre-filled).
- Fallback to `{{custom_values.business.booking_url}}` for generic.
- Never two links in one SMS. Pick one path.

**Compliance:**
- Reminders are arguably transactional (member booked, expects reminder). Quiet hours: respect anyway, 8 AM – 9 PM contact-local. Override only if the appointment itself is before 8 AM or after 9 PM.
- Post-no-show recovery: marketing-class (re-engagement). Strict quiet hours.
- "STOP" opt-out: tag `do-not-sms`. Future appointment reminders still suppressed.

**Timing precision:**
- 24hr reminder: at exactly T-24hr OR 8 AM contact-local (whichever is later).
- 2hr reminder: at exactly T-2hr. If T-2hr falls before 8 AM, send at 8 AM (this means the 2hr reminder may actually be 0-2hr away — but it still beats no reminder).
- Post no-show 2hr: at exactly T+2hr after no-show stamp. No quiet-hour override (waiting until next morning is too late).
- 72hr final: between 10 AM and 4 PM contact-local. Tweak per studio's audience.

---

## A/B Test Ideas

| Test | Variant A (control) | Variant B |
|---|---|---|
| 24hr confirm reply prompt | "Reply C to confirm or R to reschedule" | "👍 to confirm, 🔄 to reschedule" (emoji reply test — easier on phone) |
| Post-noshow 2hr opener | "We missed you at..." | "Hey — quick question, was the time off for you today?" |
| 72hr personal SMS | Morgan voice, no link | Morgan voice WITH soft CTA at end: *"...or grab the next slot here: [link]"* |

Run for 4 weeks per variant, target 100+ appointments per variant.

---

## What Comes Next

Replies handled by **`03 — Appointment Reply Handler`** workflow (see [workflow.md](workflow.md)).

Successful rebooks loop back into the reminder cadence for the new appointment (new appointment booked → new workflow run).

Repeated no-shows (`apt-noshow-repeat`) surface in [#05 Retention](../../05-retention-and-churn-prevention/) as an engagement-score factor, and in [#10 Owner Reporting](../../10-owner-reporting-and-visibility/) as a watchlist item in the Monday digest.
