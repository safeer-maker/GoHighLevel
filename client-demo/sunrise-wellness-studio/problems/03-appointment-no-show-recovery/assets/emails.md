# #03 — Email Templates

> Two emails for the appointment system: the 48hr reminder (proactive) and the post-no-show rebook email (recovery).

---

## Email 1 — 48hr Appointment Reminder

**Template name:** `03 — 48hr Appointment Reminder`

**Send timing:** 48 hours before appointment start.

**From:**
- Name: `{{custom_values.business.short_name}} Scheduling`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> Reminder: {{appointment.calendar_name}} on {{appointment.start_day_short}}

**Preview text:**
> Two-day heads up. Calendar add + everything you need below.

---

### Email Body

**Header band:** Sunrise gradient (coral → gold).

---

**Greeting (H1):**

> Hey {{contact.first_name}} —

**Body:**

> Quick heads up — you've got **{{appointment.calendar_name}}** on **{{appointment.start_day_short}}** at **{{appointment.start_time}}**.

---

**Appointment Details Block (gold border, centered):**

> **What:** {{appointment.calendar_name}}
> **When:** {{appointment.start_full}}
> **Where:** {{custom_values.business.address_line}}
> **With:** {{appointment.trainer_name}}
> **Duration:** {{appointment.duration}} min

---

**CTA buttons (two, side-by-side on desktop):**

> **[Add to Calendar 📅]({{appointment.calendar_invite_url}})**  **[Reschedule]({{appointment.reschedule_url}})**

---

**Sub-section: What to bring / how to prep**

(Conditional block — show different prep tips based on `appointment.calendar_name`)

**If Personal Training:**

> **Prep tips for PT:**
> - Eat something light 60–90 min before — protein + carb. Skip if you'd rather; just don't show up on an empty stomach if you're new to lifting.
> - Bring water and a towel. We have both, but yours is yours.
> - Wear what lets you move. No prescribed dress code.
> - If you have any soreness, recent injury, or sleep deprivation — text {{contact.assigned_trainer}} or the front desk before, not during, the session. They'll adjust.

**If Intro Consult:**

> **Prep tips for your consult:**
> - Come in workout-ready if you can — we may do a brief movement screen.
> - Think ahead about your top 1-2 goals. "Lose weight" is fine. "Feel like myself again" is fine. Honest is the only requirement.
> - Bring 10 minutes of mental space. We move fast in the consult — most people leave with a clear next-90-days plan.

**If Nutrition Consult:**

> **Prep tips for nutrition:**
> - If you can, log what you ate for 2-3 days before the consult. Doesn't have to be perfect — even a phone-photos-of-meals counts.
> - Bring any specific questions ("am I getting enough protein?", "is my morning smoothie too sugary?", etc.).
> - Sam doesn't do diet shame. Bring whatever you actually eat.

**If Group Class:**

> **Prep tips for class:**
> - Arrive 5-10 min early to grab a spot and ask the instructor about modifications.
> - Bring water + a towel. Mat rentals available at front desk ($2).
> - First time in this class type? Mention it to the instructor — they'll cue you through.

---

**Sub-section: Need to change something?**

> Stuff happens. If you need to reschedule or cancel:
>
> - **Reschedule:** [Tap here]({{appointment.reschedule_url}}) — pick a new time in 30 seconds.
> - **Cancel:** [Tap here]({{appointment.cancel_url}}) — just please give us 4hr notice if possible so we can offer the slot to someone on the waitlist.
> - **Text us:** {{custom_values.business.sms_number}}

---

**Closing:**

> See you {{appointment.start_day_short}}.
>
> — The Sunrise team

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email 2 — Post No-Show Rebook Email

**Template name:** `03 — Rebook Email`

**Send timing:** 24 hours after a no-show is detected, IF contact has NOT rebooked.

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> {{contact.first_name}}, let's get you back on the calendar

**Preview text:**
> Yesterday slipped — no problem. Two-tap rebook below.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Yesterday's **{{appointment.calendar_name}}** didn't happen — life, schedules, all of it. No drama from our side.
>
> The only thing I want to do is help you get the next one on the calendar before the week gets away from you. Here are the next 5 open slots for your trainer:

---

**Slot Block (dynamically populated by GHL):**

> - **{{slot_1_day}} {{slot_1_time}}** — [Book]({{slot_1_url}})
> - **{{slot_2_day}} {{slot_2_time}}** — [Book]({{slot_2_url}})
> - **{{slot_3_day}} {{slot_3_time}}** — [Book]({{slot_3_url}})
> - **{{slot_4_day}} {{slot_4_time}}** — [Book]({{slot_4_url}})
> - **{{slot_5_day}} {{slot_5_time}}** — [Book]({{slot_5_url}})

(If GHL doesn't render dynamic slots, fall back to a single CTA: **[See All Available Times →]({{custom_values.business.booking_url}})**)

---

**Sub-section: A small note (only if first no-show)**

> First-time no-show: zero charge, zero policy hit. We genuinely don't track it as a "strike" — life is a thing.

**Sub-section: A different note (only if `noshow_count_90d` >= 2)**

> Quick honest note — this is your second missed session in the last few weeks. **I'm not bringing it up to guilt-trip you** — I'm bringing it up because in my experience, members who miss two in a row are usually fighting something else (schedule shift, motivation dip, an injury). If any of that's true, reply and we'll either rejig your schedule or pause your sessions for a few weeks. We'd much rather pause and have you come back than have you ghost. — Morgan

(Use If/Else block in the template to show one or the other based on `noshow_count_90d`.)

---

**Closing:**

> Looking forward to the next one.
>
> — Morgan

---

**Footer:** {{custom_values.legal.footer}} · {{unsubscribe_link}}

---

## Email-Building Notes

**Tone:**
- 48hr reminder is transactional — useful, friendly, branded. Not a sales pitch.
- Rebook email is warm but never guilt-y. The word "missed" is intentional ("we missed you" vs "you missed your appointment").
- The repeat-no-show variant is Morgan-voiced and softer than the first-time message. Empathy over scolding.

**Conditional blocks:**
- Email 1 has 4 prep-tip variants (PT, Consult, Nutrition, Class). Use template-level If/Else against `appointment.calendar_name`.
- Email 2 has 2 footer variants based on `noshow_count_90d`.

**Mobile rendering:**
- Single column. Buttons ≥ 44px. Body 16px.
- Appointment detail block: ensure date/time are large and unmissable.

**Deliverability:**
- Subject lines avoid spam triggers (no "URGENT", "REMINDER!!!" caps).
- One emoji max in subject (the 📅 in CTA buttons doesn't count).

**Personalization fallbacks:**
- `{{contact.first_name}}` → "there"
- `{{appointment.trainer_name}}` → "your trainer"
- `{{appointment.calendar_name}}` → "your appointment"

---

## What Comes Next

The reminder cadence finishes when the appointment ends. The post-no-show recovery picks up automatically when status flips to `No-Show`.

For SMS counterparts (24hr confirm, 2hr reminder, post-noshow 2hr, post-noshow 72hr final, rebook confirmation), see **[sms.md](sms.md)**.

For the workflow that orchestrates both emails alongside the SMS, see **[workflow.md](workflow.md)**.
