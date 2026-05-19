# #01 — Email Templates

> Production-ready email copy. Each email has subject, preview text, full body, and merge fields. Paste into GHL email builder.

---

## Email 1 — Welcome / Your Free 7-Day Pass

**Template name:** `01 — Welcome — Free 7-Day Pass`

**Send timing:** 2 minutes after form submission (gives the SMS a head start)

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> Welcome, {{contact.first_name}} — your free 7-day pass is ready ☀️

**Preview text (inbox snippet):**
> 7 days, every class, no credit card. Here's how to claim it.

---

### Email Body

**Header band:** Sunrise gradient (coral → gold). Logo centered. White text "SUNRISE WELLNESS STUDIO" small caps.

---

**[Hero image]** — Wide photo of the studio interior, morning light, someone smiling mid-class.

---

**Greeting (H1, deep slate):**

> Hey {{contact.first_name}} —

**Body (regular paragraph):**

> Welcome to Sunrise. I'm Morgan — the owner here — and I'm genuinely excited you're trying us out.
> 
> Quick heads up: I just texted you a booking link too, but here's the same thing in case the text got lost.

---

**CTA button (large, coral, centered):**

> **Book My First Class →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Sub-section: What you can do this week**

**H2:** Your 7 days, your way.

**3-card block (stack on mobile):**

| Card | Title | Body |
|---|---|---|
| ☀️ | **Group classes** | HIIT, Yoga, Pilates, Strength, Recovery. Try whatever fits your week. |
| 💪 | **Open gym** | Use the floor whenever we're open. Bring headphones. |
| 🌱 | **30-min intro consult** | Sit down with a trainer, map out where you want to go. Free, no strings. |

---

**Sub-section: Based on what you told us**

> You told us your main goal is **{{contact.fitness_goal_primary}}** — perfect. Here's where I'd start:
> 
> - If you're new to working out: **Sunrise Flow Yoga** (Tue/Thu 7 AM, Sat 9 AM) is a gentle way in.
> - If you want to push hard fast: **Sunrise HIIT** (Mon/Wed/Fri 6 AM and 5:30 PM).
> - If you want one-on-one attention: book your **free intro consult** with the link above and we'll match you with a trainer.

(Note: this section is dynamic — use If/Else logic in the email template to show goal-specific recommendations based on `fitness_goal_primary`.)

---

**Sub-section: What to know before you walk in**

> A few things that'll save you time:
> 
> - **Address:** {{custom_values.business.address_line}}
> - **Hours this week:** {{custom_values.hours.full}}
> - **What to bring:** Workout clothes, sneakers, water bottle, a towel. We have showers, lockers, mat rentals if needed.
> - **First time:** Arrive 10 minutes early so we can show you around.

---

**Closing:**

> If anything's confusing or you want a real human to text with — just reply to this email or text us at {{custom_values.business.sms_number}}. We mean it. A real person reads everything.
> 
> Looking forward to meeting you.
> 
> — Morgan
> 
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer band:** Cream background.

- Studio: {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Social icons: Instagram · Facebook · Google
- Unsubscribe: {{unsubscribe_link}}
- Footer disclaimer: {{custom_values.legal.footer}}

---

## Email 2 — 24hr Soft Follow-Up

**Template name:** `01 — 24hr Soft Follow-Up`

**Send timing:** 24 hours after submission, IF contact has not booked AND has not replied

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}}, did the link work?

**Preview text:**
> Quick check-in. No pressure — just making sure you got everything.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Morgan again. Just doing a quick check — sometimes our texts get lost in the void of crowded inboxes and notification panels.
> 
> Your free 7-day pass is still active and ready whenever you are.

---

**CTA button (coral):**

> **Book a Time That Works →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Body continued:**

> If you've been on the fence — that's totally normal. Most people who walk in for the first time tell me they were nervous for weeks. Here's what I tell them: just come once. One class, one consult, one quiet hour on the gym floor. You'll know after that whether we're the right fit.
> 
> If you've decided we're not — also totally fine. Just hit reply with "not now" and I'll stop bugging you (and won't add you to a mailing list, promise).
> 
> Whatever you decide — I'm here.

---

**Signature:**

> — Morgan
> 
> P.S. If timing is the only thing in the way, we have a 6 AM class, a 7 PM class, and a Saturday 9 AM class. There's a slot.

---

**Footer:** Same as Email 1.

---

## Email 3 — (Held in reserve — handed off to longer drip nurture)

After 24hr soft follow-up, the contact exits the #01 workflow and is enrolled in the long-tail lead nurture (out of scope for this problem folder — handled by a separate "Lead Nurture — 30-Day Drip" workflow that pings monthly with class highlights, member stories, and seasonal offers).

---

## Email-Building Notes

**Tone calibration:**
- Warm but not gushy. Treat the lead like a smart adult.
- First-person from the owner ("I'm Morgan", "I tell them") — not corporate "we".
- Concrete, not aspirational ("Tue/Thu 7 AM" beats "convenient class times").
- Respect attention: short paragraphs, scannable lists, one CTA per email.

**Mobile rendering:**
- Single-column layout always.
- CTA buttons minimum 44px tall.
- Body font 16px minimum.
- Header image: max 600px wide, but degrades gracefully (alt text required).

**Deliverability:**
- Avoid CAPS in subject, no excessive emoji (one is fine, three is spammy).
- Include text version (GHL auto-generates from HTML).
- Verify SPF/DKIM/DMARC set on the sending domain.

**Personalization fallbacks:**
- `{{contact.first_name}}` → fallback: "there"
- `{{contact.fitness_goal_primary}}` → fallback: "your goal" (and skip the goal-specific section)
- `{{custom_values.team.owner_first}}` → fallback: "the Sunrise team"
