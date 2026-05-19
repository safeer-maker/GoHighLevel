# #09 — Email Templates: Win-Back Lapsed Members

> Five emails covering the full 90-day voluntary win-back sequence plus the failed-payment intervention. Each email has subject, preview text, full body, and merge fields. Paste into GHL email builder.

---

## Email 1 — Day-1 Gentle Goodbye

**Template name:** `09 — Day-1 Gentle Goodbye`

**Send timing:** Immediately on `member-cancelled` tag, voluntary track (Workflow `09b`)

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> {{contact.first_name}} — sorry to see you go. Door's always open.

**Preview text:**
> No pitch. Just a real goodbye, and a real thank-you for the time you spent here.

---

### Email Body

**Header band:** Cream background (softer than the usual coral). Logo centered.

---

**Greeting (H1, deep slate):**

> Hey {{contact.first_name}} —

**Body:**

> Morgan here. I got the note that you're cancelling — and I just want to say a real thank-you for the time you spent at Sunrise.
>
> {{contact.days_as_member}} days. That's not nothing.
>
> I won't pitch you on coming back today, and I won't put you in a "win-back drip" of weekly emails. If you decide you want to come back someday — next month, next year, whenever — your account stays here, your member history stays here, and the door's open. No re-enrollment fees, no "where have you been" lecture. Just walk in.
>
> If there's something we did poorly that drove you out, I want to know. Hit reply and tell me — it goes to my inbox, not a help desk. We can't fix what we don't hear about.
>
> Either way: wishing you well.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer band:** Cream background.

- Studio: {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Unsubscribe: {{unsubscribe_link}}
- Footer disclaimer: {{custom_values.legal.footer}}

---

**Design notes:** No CTA button. No hero image. No "join again" link anywhere. This is a respect message. Adding any "but here's an offer..." undermines the entire point.

---

## Email 2 — Day-30 We Miss You

**Template name:** `09 — Day-30 We Miss You`

**Send timing:** Day 30 post-cancellation, voluntary track only (Workflow `09b` Step 3.7)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — how have the last few weeks been?

**Preview text:**
> Just a check-in. A small welcome-back offer inside if you want it.

---

### Email Body

**Header band:** Sunrise gradient (back to warm brand colors — signaling the door is genuinely open).

---

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> It's been about a month since you cancelled — figured I'd check in and see how the new routine is treating you.
>
> Genuinely no agenda here. Some folks who leave us go on to do amazing things on their own. Some realize they miss the group energy and come back. Some just need a different season of life. All of those are fine.
>
> If you've been thinking about coming back, I made it easy: **first month back at 50% off, no enrollment fee, no awkwardness.** Use the link below — your member history is already loaded.

---

**CTA button (coral, centered):**

> **Come Back at 50% Off →**

(Links to `https://book.sunrisewellness.com/comeback?wb=30`)

**Below button (small):**
> Coupon WB30 auto-applied. Valid 14 days from today.

---

**Body continued:**

> If now isn't the time, no problem — I'll check in once more in a couple months and then leave you alone. You won't be on a marketing list.
>
> And if you've found a routine that works without us, genuinely glad. That's the real win.
>
> — Morgan
>
> P.S. The 6 AM Saturday HIIT crowd still asks about you. Just saying.

---

**Footer:** Same as Email 1, with full brand footer.

---

## Email 3 — Day-60 Comeback Offer

**Template name:** `09 — Day-60 Comeback Offer`

**Send timing:** Day 60 post-cancellation (Workflow `09b` Step 3.10)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — a real comeback offer ({{custom_values.offer.winback_d60}})

**Preview text:**
> The strongest offer we'll send. After this, we go quiet for a while.

---

### Email Body

**Header band:** Coral gradient.

---

**Greeting:**

> {{contact.first_name}} —

**Body:**

> Two months out, and I'm checking in one more time with something better.
>
> Here's the deal:

---

**Offer block (gold panel, centered):**

> 🌅 **{{custom_values.offer.winback_d60}}**
>
> **First month back: $39** (normally $79)
> **Enrollment fee: waived** (normally $49)
> **Total savings: $89 your first month**
>
> *Coupon WB60 auto-applied. Valid 21 days from today.*

---

**CTA button (coral, large, centered):**

> **Reactivate My Membership →**

(Links to `https://book.sunrisewellness.com/comeback?wb=60`)

---

**Body continued:**

> Three things to know:
>
> - **Your account is already there.** Your trainer history, your goal notes, your member ID — all preserved. You log in like you never left.
> - **No commitment beyond month 1.** Cancel any time after, no questions, no fees. (We hope you stay — but if a month is all you need, that's fine too.)
> - **Your goals from before are still here.** Last time you logged in, your primary goal was **{{contact.fitness_goal_primary}}**. If that's changed, your trainer will recalibrate on Day 1.

---

**Sub-section: What's changed at the studio**

(Optional — refresh per season; update at quarterly review.)

> A couple things since you've been gone:
>
> - Two new trainers joined the team — Jordan (Strength specialist) and Casey (HIIT and Mobility).
> - We added a new Saturday morning yoga slot at 8 AM that's been packed.
> - The recovery suite (sauna, cold plunge) is open to all members now, not just VIP.

---

**Closing:**

> If the timing isn't right, I get it. I'll send one more note in a month and then I'll genuinely stop. You won't end up in a forever-drip.
>
> Looking forward to seeing you again.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer:** Same as Email 1, full brand.

---

## Email 4 — Day-90 Last Call

**Template name:** `09 — Day-90 Last Call`

**Send timing:** Day 90 post-cancellation (Workflow `09b` Step 3.13)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — last note from me. $29 first month, this week only.

**Preview text:**
> The final win-back offer. After this, I really do stop reaching out.

---

### Email Body

**Header band:** Coral gradient with a small "LAST CALL" badge (gold).

---

**Greeting:**

> {{contact.first_name}} —

**Body:**

> Real talk: this is the last email I'll send in this win-back sequence. Three months out, my marketing playbook tells me to stop — and I respect that.
>
> One final offer before I go quiet:

---

**Offer block (gold panel, centered, bold):**

> 🌅 **{{custom_values.offer.winback_d90}}**
>
> **First month back: $29** (normally $79)
> **Enrollment fee: waived**
> **Total savings: $99 your first month**
>
> *Coupon WB90LAST. Valid 7 days from today. After that, the offer expires for good.*

---

**CTA button (coral, large, centered):**

> **Take the $29 Comeback Deal →**

(Links to `https://book.sunrisewellness.com/comeback?wb=90`)

---

**Body continued:**

> The 7-day window is real — not a fake urgency tactic. After it expires, you're welcome to come back at any time, but at standard pricing. The coupon doesn't reactivate.
>
> If $29 still isn't the right call for you right now, no hard feelings whatsoever. I'd rather you skip than feel pressured.
>
> And whether you take this or not — door's open. Always.
>
> — Morgan
>
> P.S. If life threw you a curveball in the last 90 days (and god knows it does), and you want to talk about a custom restart (paused membership, partial-month, whatever) — just hit reply. I'll personally figure something out.

---

**Footer:** Same as Email 1.

---

## Email 5 — Failed-Payment Intervention

**Template name:** `09 — Failed Payment Intervention`

**Send timing:** Within 60 minutes of `payment-failed-pending` tag (Workflow `09c`)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — quick: your Sunrise payment didn't go through

**Preview text:**
> Probably an expired card. One tap to fix. No urgency — just a heads up.

---

### Email Body

**Header band:** Cream background (low-alarm visual — this is friendly, not scary).

---

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Quick heads up: your card on file just declined when we ran your monthly charge. **No big deal** — usually means the card expired or got replaced after a fraud alert.
>
> One tap below to update it and we're good.

---

**CTA button (coral, large, centered):**

> **Update My Card (30 seconds) →**

(Links to the Stripe customer portal / GHL payment-method-update URL for the contact.)

---

**Body continued:**

> A few things:
>
> - **Your membership is still active.** We won't cancel anything for at least 5 days. You've got time.
> - **Your access continues uninterrupted** as long as we get it sorted within the window.
> - **If the card on file isn't right anymore** (lost it, switched banks, switched accounts) — the update link above handles all of that.
> - **If you actually want to pause or cancel,** that's totally fine — just hit reply and let me know. We'll handle it the right way (not via a silent failed-payment).

---

**Reassurance line:**

> This happens to about 1 in 30 members every month — it's almost always a card-renewal thing, not anything dramatic. We've got you.

---

**Closing:**

> Any questions, just hit reply. A real human reads everything.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer:** Same as Email 1.

---

**Design notes:**
- Low-alarm tone is critical. Members in failed-payment status often *think* they did something wrong, or feel embarrassed. The email's job is to remove shame and friction.
- The "1 in 30 every month" stat normalizes the event.
- Reply-to is the owner's personal address — sends a signal that this isn't a billing-bot message.

---

## Email 6 — (Reactivation Welcome Back — fires from Workflow `09d`, included here for completeness)

**Template name:** `09 — Welcome Back (Reactivation)`

**Send timing:** Immediately on `member-reactivated` tag (Workflow `09d`)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — welcome back ☀️

**Preview text:**
> Genuinely glad you're here. Your account is loaded and ready.

---

### Email Body

**Header band:** Sunrise gradient.

---

**Greeting:**

> {{contact.first_name}} —

**Body:**

> Welcome back. I mean that.
>
> Your account is reactivated, your member history is preserved, and your first class is one tap away.

---

**CTA button (coral):**

> **Book My First Class Back →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Body continued:**

> A few logistics:
>
> - Your tier: **{{contact.membership_tier}}** at **${{contact.monthly_rate}}/month**
> - Next billing date: **{{contact.membership_renewal_date}}**
> - Your trainer from last time, {{contact.assigned_trainer}}, will check in this week.
>
> When you walk in next, look for me. I want to say hi in person.
>
> — Morgan
>
> P.S. We don't make a big deal about reactivations publicly (no announcement, no awkward "look who's back" moment). Just a quiet welcome and a real hello. You're not a returning customer — you're a member.

---

**Footer:** Same as Email 1.

---

## Email-Building Notes

**Tone calibration by stage:**

| Stage | Tone |
|---|---|
| Day 1 (goodbye) | Soft, respectful, no pitch. The most important email — sets the tone for everything after. |
| Day 30 (check-in) | Light, friendly, soft offer. Treats them like a former friend, not a sales target. |
| Day 60 (offer) | Direct, generous, confident. The strongest offer of the sequence. |
| Day 90 (last call) | Honest urgency. Calls out the marketing playbook directly. Removes the manipulative edge. |
| Failed payment | Low-alarm, helpful, friction-free. Normalizes the event. |
| Reactivation welcome | Quiet, warm, no theatrics. Treats them like they never left. |

**Personalization fallbacks:**
- `{{contact.days_as_member}}` → fallback: "a while"
- `{{contact.fitness_goal_primary}}` → fallback: skip that paragraph entirely
- `{{contact.assigned_trainer}}` → fallback: "one of our trainers"
- `{{contact.membership_tier}}` → fallback: "your tier"

**Deliverability:**
- Failed-payment email is the most likely to be flagged as spam by aggressive filters ("payment failed" triggers some). Test deliverability before launch.
- Day-90 "Last Call" subject can also trigger filters — consider A/B with softer variant: "{{first_name}} — one more note before I stop."

**What we deliberately don't include:**
- No "we'll personally call you" promises (we can't always deliver — and breaking that promise is worse than not making it).
- No urgency tactics on Day 30 or Day 60. Only Day 90 has real urgency (the 7-day coupon window).
- No member-shaming language ("you haven't been to classes in X weeks" — we know, they know, mentioning it is salt in the wound).
