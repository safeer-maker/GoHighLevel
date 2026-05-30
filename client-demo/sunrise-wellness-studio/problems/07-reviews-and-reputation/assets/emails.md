# #07 — Email Templates

> One email template: the Email-non-responder follow-up. The bulk of the review system runs on Email + funnel; email is the backup for members who don't tap the Email link within 3 days.

---

## Email 1 — Review Follow-Up Email

**Template name:** `07 — Review Follow-Up Email`

**Send timing:** 3 days after the post-class/post-PT review-ask Email, IF member hasn't tapped the funnel link.

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> {{contact.first_name}}, mind sharing how class went?

**Preview text:**
> 30 seconds, single tap — no scrolling required.

---

### Email Body

**Header band:** Soft cream, minimal. Small Sunrise logo. **No** large hero — this should look like a personal email, not a marketing campaign.

---

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Morgan here. Sent you a text a couple days ago asking how class went — wanted to follow up in case the text got lost.
> 
> Here's the same thing: a single tap that takes you to a 5-emoji rating. Pick the one that matches how you felt. The whole thing takes 30 seconds.
> 
> I read every single response, good or bad. If you tap a high-end one, we'll ask if you'd be open to sharing on Google — but only if you're up for it. If you tap a low one, the form goes straight to me, never anywhere public.
> 
> It's the same flow either way: you tell us how it was, we listen.

---

**CTA button (coral, centered, medium):**

> **Rate Today's Class (30 sec) →**

(Links to `{{custom_values.business.short_review_url}}?contact_id={{contact.id}}`)

---

**Body continued — context:**

> Why does this matter? Honestly, two reasons:
> 
> 1. **For the studio:** Google reviews are how new members find us — and how we afford to keep doing things like running 6 AM classes for the early birds and keeping class sizes small. Every review helps.
> 2. **For me:** If something was off — the music, the timing, the trainer's energy, anything — I want to know now, while I can still fix it. The members who tell me when something's not working are the ones who actually help me run the studio.
> 
> So: 30 seconds, single tap. If you've got it in you.

---

**Closing:**

> Either way — glad you were in class.
> 
> — Morgan
> 
> P.S. If you'd rather just hit reply with your thoughts, that works too. A real human reads everything.

---

**Footer band:** Cream background.

- {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Unsubscribe from review requests: {{unsubscribe_link}}
- {{custom_values.legal.footer}}

---

**Why this email works:**

- Acknowledges the prior Email without scolding — "in case it got lost."
- Explains the routing transparently: high score → Google, low score → private. Removes the "what happens after I tap?" friction.
- Gives **two honest reasons** (the studio benefits + Morgan personally benefits from feedback) — reads as authentic, not manipulative.
- "Or just hit reply" P.S. handles members who hate clickthrough surveys.
- Owner-signed, conversational, single CTA.

---

## Email 2 — High-Score Thank You (Optional)

**Template name:** `07 — High-Score Thank You Email`

**Send timing:** 1 day after a 5-star Google review submission (if the studio opts to send email instead of / in addition to the Email variant).

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}} — thank you 🙏

**Preview text:**
> Genuinely means a ton.

---

### Email Body

**Greeting:**

> {{contact.first_name}} —

**Body:**

> Just saw your Google review. Thank you. Genuinely.
> 
> It's hard to overstate how much these matter for a small studio. Every review is real proof to someone who's nervous about walking in for the first time. You probably saved a future member a lot of hesitation.
> 
> I appreciate you. See you in class.
> 
> — Morgan

---

**Footer:** Same as Email 1, minimal.

---

**Why this email works:**

- Short — 5 sentences.
- Explains why the review matters in concrete terms ("you saved a future member hesitation").
- No CTA — gratitude only. The next ask (a referral prompt) comes 7 days later via [#08](../../08-referral-engine/).

**Why optional:** Some studios feel email is overkill on top of the Email thank-you. Default: ON for studios that want full-loop gratitude; OFF for studios that prefer single-channel acknowledgment.

---

## Email 3 — Low-Score Follow-Up (Owner-Personal Reply Template)

**Template name:** `07 — Low-Score Owner Personal Reply` (Owner USES this as a template when manually replying to private feedback)

**This is not an automated send — it's a starting template Morgan uses when manually replying to low-score private feedback.**

**Subject:**
> Re: your note about Sunrise

---

**Body template:**

> Hey {{contact.first_name}} —
> 
> Morgan. Got your feedback this morning and wanted to reply directly.
> 
> [PERSONALIZED RESPONSE — owner writes 2-3 sentences acknowledging the specific issue raised. Examples:]
> 
> - If it was a class issue: "You're right that the music in {{specific_class}} has been off lately — that's on us. {{trainer_name}} and I are talking through it this week and the playlist should feel better by next class."
> - If it was a facility issue: "I hear you on the locker room crowding at 6 PM — we're piloting a second locker bay starting Tuesday."
> - If it was a staff issue: "Thanks for telling me — I'm going to talk with [staff] directly. That's not who we want to be."
> 
> If you're up for it, I'd love to grab 10 minutes on the phone this week so I can hear more directly. No pressure if not — but the offer's open.
> 
> Either way, I want to thank you for telling me instead of just leaving. The members who tell us are the ones who help us actually fix things.
> 
> — Morgan

---

**Why this template works:**

- Specific to the feedback — not generic "sorry to hear that."
- Names the **concrete action** the studio is taking, with a specific timeframe.
- Offers a phone call without forcing it.
- Acknowledges and thanks the member for *not just leaving* — converts complaint energy into loyalty.

**Owner uses this as a starting point** — never sends it verbatim. The personalization is the entire mechanism.

---

## Email Building Notes

**Tone calibration for review emails:**

- The review system is fundamentally about respect — respect for the member's time, respect for their honesty, respect for their channel preference. Every email should *feel* respectful: short paragraphs, plain language, no marketing copy patterns.
- Avoid emoji-heavy subject lines. Reviews are a small ask and feel weird with too much enthusiasm.
- Owner-voice throughout. The system is personal even when it's automated.

**Mobile rendering:**

- Single column.
- Short paragraphs (2-3 sentences max).
- CTA button 48px+ tall.
- Body font 16px minimum.
- No multi-image layouts.

**Deliverability:**

- Review-ask emails go to active members with established engagement — deliverability is high.
- Avoid: "URGENT", "FINAL CHANCE", multiple exclamations, ALL CAPS.
- Include "Unsubscribe from review requests" as a separate option from full account unsubscribe — gives members a way to opt out of *this specific cadence* without leaving the studio entirely.

**Personalization fallbacks:**

- `{{contact.first_name}}` → fallback: "there"
- `{{contact.assigned_trainer}}` → if null, generic "your trainer" or skip the line
- `{{custom_values.business.short_review_url}}` → fallback: full funnel URL

**Suppression honored:**

- `do-not-email` blocks all emails system-wide.
- `do-not-ask-reviews` blocks the review-specific cadence.
- A member who replies "stop asking for reviews" gets tagged `do-not-ask-reviews` for 180 days by the inbound-reply handler.

---

## What Comes Next

After the email follow-up:

- **Member taps and rates:** Routes through the funnel as normal. Workflow 07b or 07c handles based on score.
- **Member replies to email:** Lands in studio inbox. Owner / front desk responds personally. Often converts to a feedback conversation that doesn't go through the funnel at all — that's fine, the relationship is the point.
- **No engagement after email:** Member is left alone for 90 days. `review-no-response` tag applied for visibility. Next eligible appointment after 90 days re-triggers the workflow.
