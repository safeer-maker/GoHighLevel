# #06 — Email Templates

> Production-ready email copy for the four upsell offers. Each email is gated, personalized, and **shows specific behavior or math** — never a generic "upgrade today" pitch. Members tell us with their behavior that they're ready; the email reflects that.

---

## Email 1 — Basic → Premium Pitch

**Template name:** `06 — Basic to Premium Pitch`

**Send timing:** 1 day after the Basic→Premium nudge Email (Branch A, step 5)

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> {{contact.first_name}}, you attended {{contact.visits_last_30_days}} classes — let's talk Premium

**Preview text:**
> You're already using the studio like a Premium member. Here's what Premium would change.

---

### Email Body

**Header band:** Sunrise gradient (coral → gold). Logo centered.

---

**Greeting (H1, deep slate):**

> Hey {{contact.first_name}} —

**Body:**

> Morgan here. I was looking at the data this morning and you've been *crushing it* — **{{contact.visits_last_30_days}} classes in the last 30 days**. That puts you in the top 15% of our active members for attendance.
> 
> Here's the thing: at your usage level, you're already getting near-Premium-level value from your Basic membership. But there's a tier of stuff Basic doesn't include that you're probably curious about — PT, nutrition, priority booking.
> 
> So let me lay out what changes if you upgrade.

---

**Side-by-side comparison table:**

| What you get | Basic ($79/mo) | Premium ($149/mo) |
|---|---|---|
| Group classes | Unlimited ✓ | Unlimited ✓ |
| Open gym access | ✓ | ✓ |
| **Personal training sessions** | None included | **2 / month** |
| **Nutrition starter consult** | $50 separate | **Included on signup** |
| **Priority class booking** | 48hr window | **72hr window** |
| **Discount on retail / add-ons** | None | **10% off** |
| Monthly investment | $79 | $149 |

---

**Body — the soft pitch:**

> The math: it's $70 more per month. **If you bought even one PT session a month at $85, you'd already be ahead.** Most Premium members use both sessions and treat the nutrition consult as a bonus.
> 
> If that doesn't sound like you yet — totally fine, Basic is great. But if you've ever wondered "should I be doing some PT?" or "I should probably eat better, where do I even start?" — Premium is the path of least resistance.

---

**CTA button (coral, large, centered):**

> **See What Premium Looks Like for Me →**

(Links to the **Sunrise — Premium Upgrade Checkout** funnel with `?contact_id={{contact.id}}` appended so the page personalizes.)

---

**Sub-section — what to expect on the upgrade page:**

> The upgrade page has a quick calculator that takes 30 seconds — tells you exactly what you'd spend on Basic + add-ons vs Premium. No commitment, no email capture, just the numbers.
> 
> And if you do upgrade, your new tier starts immediately. We pro-rate the rest of this month so you don't pay twice for overlapping days.

---

**Closing:**

> If Premium isn't the move right now, just reply with "not yet" and I'll stop the offer. I won't ask again for 30 days. If you have questions before deciding, hit reply and I'll answer them personally.
> 
> Either way, keep doing what you're doing — you're inspiring.
> 
> — Morgan
> 
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer band:** Cream background.

- {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Unsubscribe: {{unsubscribe_link}}
- {{custom_values.legal.footer}}

---

**Why this email works:**

- Opens with the **specific behavior** that earned the offer — "you attended 14 classes." Member feels seen, not blasted.
- Comparison table does the comparison work — member doesn't have to figure out the value themselves.
- "$70 more = one PT session breakeven" is concrete math the member can verify.
- "Reply 'not yet' to stop the offer" gives a low-friction opt-out that prevents the email from feeling pushy.
- Owner-voiced, personal sign-off — not corporate.

---

## Email 2 — Premium → VIP Math Email

**Template name:** `06 — Premium to VIP Math Email`

**Send timing:** 1 day after the Premium→VIP personal Email from Morgan (Branch B, step 5)

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}} — VIP would have saved you $155 last month

**Preview text:**
> Here's the actual math from your last 3 months. No spin.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Morgan, picking up the conversation from my text.
> 
> Here's why I reached out. I ran the numbers on your last 3 months of PT bookings.

---

**The Math Box (highlighted callout, gold border):**

| Month | Premium membership | PT sessions beyond your included 2 | Cost |
|---|---|---|---|
| Last month | $149 | 3 extra @ $85 | **$404** |
| 2 months ago | $149 | 3 extra @ $85 | **$404** |
| 3 months ago | $149 | 2 extra @ $85 | **$319** |
| **Average / month** | — | — | **~$376** |

> If you'd been on VIP ($249/month, **unlimited** PT) over those 3 months, you'd have spent **$249 × 3 = $747** instead of **~$1,127**.
> 
> That's **$380 you've spent that VIP would have covered.**

---

**Body — what VIP also gets:**

> And that's just the PT math. VIP also includes:
> 
> - **Monthly nutrition coaching** (1 hour with {{custom_values.team.nutritionist}}, normally $50/session)
> - **Recovery suite access** — sauna, cold plunge, massage gun room
> - **Quarterly InBody composition scan** ($75 value each)
> - **2 free guest passes per month** — bring a friend, free
> - **20% off retail + all add-ons**
> 
> So even on the conservative math, VIP pays for itself if you keep using PT the way you've been.

---

**CTA button (coral, large, centered):**

> **Upgrade to VIP →**

(Links to **Sunrise — VIP Upgrade Checkout** funnel with `?contact_id={{contact.id}}`.)

---

**Soft alternative:**

> If you want to talk it through before committing, just hit reply or email me. I can also pull up your full PT history and we can look at it together — sometimes the math looks different on paper than what feels right.
> 
> No urgency on this one. VIP will be here when you're ready.

---

**Closing:**

> Either way — I love watching you go this hard. Sunrise is better with you here.
> 
> — Morgan

---

**Footer:** Same as Email 1.

---

**Why this email works:**

- The **specific dollar math** is irrefutable — not "save money on Premium," but "you've spent $380 you didn't need to."
- VIP non-PT benefits are listed *after* the PT math, so the math anchors the value and the benefits are bonus.
- "Hit reply, let's pull up your history" — a real conversational offer, not a fake one. Premium members who decline often book a call instead and convert that way.
- No urgency or deadlines. VIP members are long-term relationships; manufactured urgency damages trust.

---

## Email 3 — Nutrition Starter Offer

**Template name:** `06 — Nutrition Starter Offer`

**Send timing:** Day 1 of Branch C — sent the same day the day-21 trigger fires.

**From:** Personalized from the nutritionist:
- Name: `{{custom_values.team.nutritionist}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}` (replies route to studio inbox, monitored by nutritionist + front desk)

**Subject:**
> {{contact.first_name}}, want to talk nutrition? 45 min, $50

**Preview text:**
> The fitness side is one half. The food side is the other. Curious?

---

### Email Body

**Header band:** Soft cream, with a small photo of the nutritionist (Sam) — friendly, warm.

---

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> I'm Sam — the nutritionist at {{custom_values.business.short_name}}. We haven't met yet but Morgan mentioned you've been crushing your workouts and might be open to talking nutrition.
> 
> Here's what I do: a **45-minute one-on-one consult** where we talk through your goals, what you're currently eating, what might be sabotaging your progress, and what one or two changes would actually move the needle.
> 
> Not a diet pitch. Not a meal-plan-in-a-binder. A real conversation about your food — like talking to a trainer, but for the half of the day you spend outside the gym.

---

**3-card block: What we cover**

| Card | Topic | Time |
|---|---|---|
| 🎯 | **Your goal mapped to food** | What you're aiming for, what your current food is doing for or against it |
| 📊 | **Quick assessment** | A few easy questions about your habits — no food logs, no judgment |
| 🛠️ | **2–3 specific changes** | Actionable, low-effort changes you can start this week. No "eliminate all sugar" nonsense. |

---

**CTA button (coral, large, centered):**

> **Book My Nutrition Starter — $50 →**

(Links to the nutrition calendar booking: `{{custom_values.business.booking_url}}/nutrition-starter`)

---

**Body — the pricing reassurance:**

> A few things to know:
> 
> - **$50 one-time.** Not a recurring add-on, not a long-form commitment.
> - **Included free if you're Premium or VIP** — and if you're thinking about upgrading anyway, ask Morgan about that path.
> - **No follow-up obligation.** Some people do one consult and run with what they learned. Others book the 4-week plan after. Whatever fits.
> - **45 minutes, in-person or video.** Whichever works for your schedule.

---

**Sub-section — quick testimonial:**

> "I'd been training hard for two years and stuck at the same body comp. One consult with Sam, two changes — pre-workout snack timing and protein at breakfast — and three months later I'd hit my goal. The fitness was working all along; the food was the missing piece."
> 
> — **Marcus T., Premium member**

---

**Closing:**

> If now isn't the moment, no worries. The offer's open whenever. And if you have any questions about what the consult covers or whether it'd be useful for you — reply to this email and I'll write back.
> 
> Looking forward to meeting you.
> 
> — Sam
> 
> {{custom_values.team.nutritionist}} · Nutritionist, {{custom_values.business.name}}

---

**Footer:** Same as Email 1, with addition: "Reply to opt out of nutrition offers."

---

**Why this email works:**

- From the nutritionist directly, not from Morgan — feels like an introduction, not a sales play.
- Explicitly says **"not a diet pitch, not a meal-plan-in-a-binder"** — names and dismisses the two most common objections.
- Pricing is upfront — $50 one-time, with the Premium/VIP inclusion mentioned as a soft upsell hook.
- Testimonial focuses on the *specific outcome* (body comp progress after a plateau), not generic praise.

---

## Email 4 — 4-Week Custom Nutrition Plan Offer

**Template name:** `06 — 4-Week Plan Offer`

**Send timing:** Day 1 of Branch D — sent after member has booked 2+ nutrition consults.

**From:** Same as Email 3 (Sam).

**Subject:**
> {{contact.first_name}}, ready to take this to the next level?

**Preview text:**
> A real, custom 4-week plan — built around your actual life.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Sam again. We've done a couple of consults now, and based on where you are — your goals, your habits, what's been working and what hasn't — I want to offer you the next thing.
> 
> The **4-Week Custom Nutrition Plan**. It's the most concentrated coaching I offer, and honestly the place where members see the biggest changes.

---

**What it includes (3-card layout):**

| Card | What | Detail |
|---|---|---|
| 🍳 | **A real plan, built for your life** | Custom 4-week meal framework based on your schedule, preferences, dislikes, and budget. Not a meal-plan PDF. |
| 📞 | **Weekly check-ins** | 20-min video or in-person every week to adjust, troubleshoot, and keep momentum |
| 📈 | **2 deep-dive consults** | Front-loaded — week 1 strategy session, week 4 progress + what's next |

---

**Pricing callout (gold border box):**

> **$199 — one-time payment**
> 
> Includes the plan, 4 weekly check-ins, and 2 consults. Nothing recurs after week 4. **No autopay surprises.**
> 
> *(For comparison: 2 standalone consults at $50 each = $100. The 4-week plan delivers ~$400 worth of coaching for $199.)*

---

**CTA button (coral, large, centered):**

> **Start My 4-Week Plan →**

(Links to checkout for product SKU `NUT-PLAN-4WK`.)

---

**Body continued — who this is for:**

> This isn't for everyone — and I want to be honest about that. The 4-week plan is for you if:
> 
> - You've done a consult or two and want to actually *implement* what we talked about
> - You're at a point where you're tired of half-trying things and want a structured month
> - You have ~15 minutes/week for check-ins (low effort relative to results)
> 
> If you're not sure whether you're ready, just reply — I'll be straight with you about whether it'd be the right fit right now.

---

**Closing:**

> Whatever you decide, glad we've been talking.
> 
> — Sam

---

**Footer:** Same as Email 3.

---

**Why this email works:**

- Comes after **demonstrated interest** (2+ consults already booked). The offer is the natural next step, not a cold pitch.
- "$400 of coaching for $199" — anchored against the standalone-consult price, which the member already knows is fair.
- "This isn't for everyone" — counter-intuitive but builds trust. Members who *are* ready respond more strongly because they feel chosen, not pitched.
- "Reply if you're not sure" — invites consultation rather than pure transaction.

---

## Email Building Notes

**Tone calibration for upsell emails:**
- Open with the **specific behavior or stat** that earned the offer. Never start with "We have a special offer for you."
- Use comparison tables and math callouts — visual proof beats prose.
- Always offer a low-friction opt-out ("reply 'not yet'") within the body — reduces unsubscribes and complaints.
- The owner (Morgan) or relevant specialist (Sam) signs every email. No "The Sunrise Team" corporate voice.

**Mobile rendering:**
- Comparison tables must be readable on mobile — stack columns to rows if needed (GHL handles this with the "stack on mobile" toggle).
- Math callouts use border + background highlight so they survive small-screen scanning.
- CTA buttons 48px+ tall.

**Deliverability:**
- Upsell emails go to active members who've previously engaged — deliverability is naturally high.
- Avoid spammy subject patterns: "$$$", "FREE", excessive emojis, multiple punctuation marks.
- Include a clear "unsubscribe from upsell offers" link distinct from full account unsubscribe.

**Personalization fallbacks:**
- `{{contact.first_name}}` → fallback: "there"
- `{{contact.visits_last_30_days}}` → if null/0, **skip the email** (the trigger condition shouldn't have matched anyway)
- `{{contact.id}}` → must populate for the funnel personalization to work; verify in test sends

**Suppression honored:**
- `do-not-market` tag suppresses all upsell emails system-wide.
- `do-not-email` blocks emails specifically; Email branch can still fire.
- A contact who replies "stop sending upsell offers" gets tagged `do-not-market` automatically by the inbound-handler workflow.

---

## What Comes Next

After the email sequence:

- **Member converts:** Tag `upsell-converted-*` applied. Workflow 06 conversion path fires. Celebration Email lands 1 hour after purchase. Owner gets a Win notification. Member enters relevant onboarding mini-flow.
- **Member declines or ignores:** Tag `upsell-declined-*-30d` applied. 30-day cooldown enforced. Workflow re-evaluates after cooldown clears.
- **Member replies:** Reply routes to studio inbox. Owner / specialist handles personally. Auto-workflow pauses to avoid stepping on the conversation.
