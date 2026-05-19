# #06 — SMS Templates

> SMS messages for the four upsell sequences plus the celebration message after a conversion. Each SMS is short, behavior-specific, and links to a single CTA. Premium → VIP uses Morgan's personal number; the others use the general sender.

---

## SMS A — Basic → Premium Nudge

**Template name:** `06 — Basic to Premium Nudge`

**Trigger:** Day 0 of Branch A in Workflow 06.

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}}, Morgan ☀️ Saw you hit {{contact.visits_last_30_days}} classes last month — you're killing it. Want to see what Premium would look like for you? {{custom_values.business.booking_url}}/premium

**Character count:** ~178 — 2 segments.

**Why this works:** Names the specific behavior earning the offer ("you hit 14 classes"). Short, owner-voiced, single link. The CTA is exploratory ("want to see") not committal ("upgrade now").

**Variant if `visits_last_30_days` is unavailable:** "Hey {{contact.first_name}}, Morgan ☀️ Been seeing you in class a lot — you're using us like a Premium member. Want a quick look at what that tier includes? {{link}}"

---

## SMS B — Basic → Premium Last Nudge

**Template name:** `06 — Basic to Premium Last Nudge`

**Trigger:** Branch A step 8 — 4 days after the email if no upgrade.

**From:** Same.

**Body:**

> {{contact.first_name}} — Morgan. Last quick note on Premium. If now isn't the moment, reply "later" and I'll stop. Otherwise here's the link: {{custom_values.business.booking_url}}/premium

**Character count:** ~159 — single segment.

**Why this works:** "Last quick note" sets the no-more-pestering expectation. Explicit opt-out language ("reply 'later'") gives a low-friction off-ramp. Single link, no fluff. After this SMS, the workflow exits if no conversion — frequency cap respected.

---

## SMS C — Premium → VIP Personal SMS

**Template name:** `06 — Premium to VIP Personal SMS`

**Trigger:** Day 0 of Branch B in Workflow 06.

**From:** **Morgan's personal cell number** — not the general SMS line. This is signaled to the recipient by the phone number itself.

**Body:**

> Hey {{contact.first_name}}, it's Morgan from Sunrise — using my number for this one. Quick note about your PT usage. Mind if I send you the math? ☀️

**Character count:** ~150 — single segment.

**Why this works:** The "using my number for this one" line is the headline — signals immediately that this is a high-priority personal message. Asks permission ("mind if I send you the math?") rather than dumping a link. Frequently gets a "yes" reply, which makes the follow-up email feel invited rather than intrusive.

**Note:** If the member replies "yes" the email goes as planned. If they reply "no" or "not now," the workflow exits and tags `upsell-declined-premium-vip-30d`.

---

## SMS D — Premium → VIP Soft Follow-Up

**Template name:** `06 — Premium to VIP Soft Follow-Up`

**Trigger:** Branch B step 8 — 5 days after the math email if no upgrade.

**From:** Morgan's number (same as SMS C — keep the conversation in one thread).

**Body:**

> {{contact.first_name}} — no pressure on VIP, just wanted to make sure the email made sense. Want to talk it through on the phone or in person? Either works.

**Character count:** ~155 — single segment.

**Why this works:** Opens a real conversation. Some Premium members can't justify VIP via email reasoning but absolutely will after a 5-minute live conversation with the owner. The SMS converts the offer into a relationship moment.

---

## SMS E — Nutrition Starter SMS Nudge

**Template name:** `06 — Nutrition Starter SMS Nudge`

**Trigger:** Branch C step 4 — 2 days after the email.

**From:** General sender.

**Body:**

> {{contact.first_name}}, Sam (nutritionist) here. Sent you a note about a $50 starter consult — interested? Reply YES and I'll grab a time. {{custom_values.business.booking_url}}/nutrition-starter

**Character count:** ~178 — 2 segments.

**Why this works:** From Sam directly — reinforces that the offer is from a specific human, not a marketing bot. "Reply YES" is a conversational invite; many members reply yes who wouldn't have clicked a link. Includes the link as a backup for those who prefer self-service.

---

## SMS F — 4-Week Plan SMS Nudge

**Template name:** `06 — 4-Week Plan SMS Nudge`

**Trigger:** Branch D step 4 — 2 days after the email.

**From:** General sender.

**Body:**

> {{contact.first_name}} — Sam. Saw the 4-week plan email might've gotten buried. Quick recap: $199, 4 weeks, real coaching not a PDF. Want in? {{custom_values.business.booking_url}}/nutrition-plan

**Character count:** ~189 — 2 segments.

**Why this works:** Acknowledges the email might've been missed ("might've gotten buried") — disarming and honest. "Real coaching not a PDF" calls out the most common skepticism. Single link. Conversational.

---

## SMS G — Upgrade Celebration (Member-Facing, Post-Conversion)

**Template name:** `06 — Upgrade Celebration`

**Trigger:** 1 hour after successful upgrade (conversion path in Workflow 06).

**From:** General sender (or Morgan's number for VIP upgrades — bigger moment).

**Body for Basic → Premium:**

> {{contact.first_name}} 🎉 Welcome to Premium! Your tier is live. I'll text tomorrow about booking your first PT session + nutrition consult. So glad you're here. — Morgan

**Character count:** ~170 — 2 segments.

**Body for Premium → VIP:**

> {{contact.first_name}} 🎉 You're VIP now! Unlimited PT, recovery suite, nutrition coaching — all unlocked. Tomorrow I'll text about your InBody scan booking. Welcome to the inner circle. — Morgan

**Character count:** ~189 — 2 segments.

**Body for Nutrition Starter:**

> {{contact.first_name}} — locked in for your nutrition consult with Sam. You'll get a calendar confirmation + reminders. Excited for you. ☀️ — Morgan

**Character count:** ~145 — single segment.

**Body for 4-Week Plan:**

> {{contact.first_name}} 🎉 You're in! Sam will reach out within 24hr to schedule your week-1 strategy session. Big move. — Morgan

**Character count:** ~125 — single segment.

**Why these work:** Celebrate the decision — members who feel acknowledged for choosing more *use* more, which drives retention and referral. Each tier gets a specific note about what happens next, removing the "what now?" anxiety that often follows a purchase.

---

## Reply Handling

Inbound replies route to the studio Conversations inbox and trigger automation as follows:

### Auto-tag on reply

| If contact replies with... | Auto-tag applied | Workflow action |
|---|---|---|
| "yes" / "interested" / "tell me more" | `upsell-interest-confirmed` | Pause auto-workflow. Notify owner: "Member said yes to upsell — engage personally." |
| "no" / "not now" / "not interested" | `upsell-decline-explicit` | Pause auto-workflow. Add `upsell-declined-*-30d`. Owner sees in inbox but no urgent action. |
| "stop" / "unsubscribe" | `do-not-market` (and per SMS rules, `do-not-sms`) | Halt all marketing automation. Owner alerted. |
| Substantive question ("how does the PT scheduling work?") | `upsell-question-pending` | Notify owner / front desk to reply personally. Workflow pauses. |
| Anything else | (no auto-tag) | Owner reviews in normal inbox flow. |

### Common replies and response scripts

| Reply | Owner/staff response |
|---|---|
| "What's the difference between Premium and VIP?" | Send the comparison table from [emails.md](emails.md). Offer a 10-min call. |
| "Can I try Premium for a month and downgrade if it's not for me?" | "Yes — pro-rated either way. Want me to upgrade you today?" |
| "I want VIP but the price is a stretch right now" | "Totally fair. Want me to flag your account so we revisit at month-end?" Tag `upsell-revisit-pending`. |
| "I'm not sure I'd use the PT in Premium" | "Honest answer — most members don't use both sessions consistently for the first 2 months. That's normal. Want me to set you up with {{custom_values.team.lead_trainer}} for the first one to make it easy?" |
| "Just send me the nutrition info" | Send the nutrition starter email content as a follow-up, or book the consult directly if they're ready. |

---

## SMS Best Practices for Upsells Specifically

**Single link maximum.** Multiple links in an upsell SMS degrade trust ("is this spam?"). Always one URL, branded short-link domain.

**Behavior-specific opener.** "Hey {{first_name}}, I have an offer" feels generic. "Hey {{first_name}}, you hit 14 classes last month" feels personal. Always lead with the *reason* the offer is being made.

**Quiet hours strict.** Upsell SMS goes between **9 AM – 7 PM contact-local time, weekdays preferred**. Friday morning is the sweet spot (members in weekend-decision-making mode but not yet checked out for the weekend). Saturday morning works for the casual offers. Never after 7 PM.

**Frequency cap.** A member should receive at most **one upsell SMS in any 30-day window**. The `upsell-recent` tag enforces this — every SMS in the upsell workflow checks for that tag at trigger.

**Owner number vs general number.** Use Morgan's personal number for the high-value Premium → VIP path. Use the general number for everything else. The personal-number signal is powerful but loses meaning if overused. Don't degrade it by texting from her number for nutrition consult offers.

**Compliance.** Upsell SMS is marketing, not transactional. Respect `do-not-market` and `do-not-sms` tags. The conversion celebration SMS is *transactional* (responding to a purchase) and bypasses `do-not-market` but not `do-not-sms`.

---

## A/B Test Ideas (after baseline is set)

Hold these for after 60 days of baseline:

| Test | Variant A (control) | Variant B |
|---|---|---|
| Basic → Premium opener | "Saw you hit 14 classes" | "Looking at your usage, Premium would actually save you money over time" |
| Premium → VIP framing | Math-led (how much you'd save) | Status-led ("you've earned the inner circle") |
| Nutrition starter pitch | From Sam directly | Co-signed by Morgan + Sam |
| Celebration SMS timing | 1 hour post-purchase | 24 hours post-purchase (day-after dopamine) |

Run each test for 4 weeks minimum, 25+ recipients per variant.

---

## What Comes Next

After the SMS sequence:

- **Conversion happens:** Celebration SMS lands 1 hour after purchase. Member is enrolled in tier-specific onboarding (Premium / VIP). Owner gets a Win notification.
- **No conversion, no decline:** Decline cooldown tag applied. Workflow re-evaluates after 30 days.
- **Reply received:** Auto-tag applied, workflow pauses, owner / staff handles personally.
- **30 days post-conversion:** `referral-prompt-ready` tag applied — member is now a high-priority referral candidate per [#08 Referral Engine](../../08-referral-engine/).
