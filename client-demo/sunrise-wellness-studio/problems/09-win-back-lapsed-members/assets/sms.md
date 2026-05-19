# #09 — SMS Templates: Win-Back Lapsed Members

> Four SMS messages used across the win-back sequences. Same rules as #01: under 160 chars target, one link max, low-pressure tone, opt-out on first contact of a new sequence.

---

## SMS A — Day-30 Light Check-In

**Template name:** `09 — Day-30 Light Check-In`

**Trigger:** Day 30 of voluntary win-back sequence (Workflow `09b` Step 3.6). Only for cancel_reason ≠ Moved/Injury/Failed Payment.

**From:** `{{custom_values.business.sms_number}}`

**Recipient:** Lapsed member (30 days post-cancel)

**Body:**

> Hey {{contact.first_name}}, it's Morgan ☀️ Just checking in — been about a month. If you ever want to come back, first month's 50% off: book.sunrisewellness.com/comeback?wb=30
>
> Reply STOP to opt out.

**Character count:** ~187 — single segment.

**Why this works:** First-person from owner, soft check-in framing ("just checking in" not "we miss you!!"), specific offer at the end (not buried), opt-out on first contact in this re-engagement sequence (legally cleaner since they're now in marketing mode again, not transactional). The link is short and brand-clean.

**Tone notes:** Resist the urge to add "we miss you" — too many studios use that phrase and it lands as performative. "Just checking in" is more honest and lands warmer.

---

## SMS B — Day-60 Comeback Offer

**Template name:** `09 — Day-60 Comeback Offer`

**Trigger:** Day 60 of voluntary win-back sequence (Workflow `09b` Step 3.10)

**From:** Same number.

**Recipient:** Lapsed member (60 days post-cancel)

**Body:**

> {{contact.first_name}} — comeback offer: $39 first month + waived enrollment ($89 savings). Auto-applied here: book.sunrisewellness.com/comeback?wb=60

**Character count:** ~150 — single segment.

**Why this works:** Direct, specific, dollar-quantified. No "miss you" softness — by Day 60 we're being honest that this is an offer, not a check-in. The "$89 savings" framing is the hook. No opt-out language (already given consent in SMS A).

---

## SMS C — Day-90 Last Call

**Template name:** `09 — Day-90 Last Call`

**Trigger:** Day 90 of voluntary win-back sequence (Workflow `09b` Step 3.13)

**From:** Same number.

**Recipient:** Lapsed member (90 days post-cancel)

**Body:**

> {{contact.first_name}}, final note from me: $29 first month + waived enrollment, this week only. After that I'll stop reaching out. book.sunrisewellness.com/comeback?wb=90

**Character count:** ~177 — single segment.

**Why this works:** Honest urgency ("final note from me" + "this week only" + "I'll stop reaching out") — calls out the marketing pattern explicitly, which removes the manipulative edge. Personal voice ("from me") instead of corporate "we." Strong offer paired with a real deadline.

---

## SMS D — Failed-Payment Immediate Intervention

**Template name:** `09 — Failed Payment Intervention`

**Trigger:** Within 1 hour of `payment-failed-pending` tag (Workflow `09c` Step 4.3). Fires during business-hours window (8 AM – 9 PM contact-local).

**From:** Same number.

**Recipient:** Member whose payment just failed

**Body:**

> Hey {{contact.first_name}}, it's Morgan ☀️ Your card on file just declined — probably expired. One tap to update, takes 30 sec: {{contact.payment_update_url}}
>
> Reply STOP to opt out.

**Character count:** ~180 — single segment.

**Why this works:** Low-alarm, normalizes the event ("probably expired"), one-tap fix, time estimate ("30 sec") removes the "this will be annoying" friction. Personal voice. The link goes straight to the Stripe customer portal — no login, no support ticket, just update.

**Note on the link:** `{{contact.payment_update_url}}` is a per-contact merge field that should be configured to generate a tokenized one-time-use link to the Stripe customer portal for that contact's account. If GHL doesn't support per-contact one-time links natively, use a generic portal URL (`https://billing.sunrisewellness.com/update`) that requires the member to sign in — slightly more friction but works universally.

---

## Bonus SMS — Day-2 Failed-Payment Reminder (sent only if no recovery in 24h)

**Template name:** `09 — Failed Payment Day-2 Reminder`

**Trigger:** 24 hours after SMS D if recovery hasn't occurred (Workflow `09c` Step 4.6)

**Body:**

> {{contact.first_name}}, quick heads up — your card's still declining. One more tap to fix: {{contact.payment_update_url}} (after 48h we'll pause your account, but it's recoverable)

**Character count:** ~189 — single segment (close to limit).

**Why this works:** Acknowledges the previous message, adds *real* but gentle consequence info ("we'll pause"), reassures recoverability ("but it's recoverable"). Doesn't shame or pressure.

---

## Bonus SMS — Failed-Payment Recovered Confirmation (fires on successful retry)

**Template name:** `09 — Failed Payment Recovered`

**Trigger:** `payment-failed-pending` tag removed (Workflow `09c` Step 4.5 YES branch)

**Body:**

> {{contact.first_name}} — fixed! Card updated, you're good to go ☀️ Thanks for sorting that out fast.

**Character count:** ~95 — single segment.

**Why this works:** Closes the loop. Acknowledges *they* fixed it (agency-affirming). Warm. No CTA needed — they don't need to do anything else.

---

## Bonus SMS — Reactivation Welcome (fires from Workflow `09d`)

**Template name:** `09 — Reactivation Welcome`

**Trigger:** `member-reactivated` tag applied (Workflow `09d` Step 8)

**Body:**

> {{contact.first_name}} — welcome back ☀️ Your account's loaded and ready. Book your first class back: {{custom_values.business.booking_url}}

**Character count:** ~135 — single segment.

**Why this works:** Quiet welcome — no fireworks, no "WE MISSED YOU!" — just a warm "you're back, here's the link." Treats them like a member, not a returning customer.

---

## Reply Handling

When a lapsed member replies to any win-back SMS:

| If they reply... | Response |
|---|---|
| Any acknowledgment / interest | Front-desk handoff via Conversations inbox. Personal owner reply within 4 business hours. |
| "Stop sending me this" or similar | Add `do-not-market` tag. Workflow continues but skips all SMS/email sends. Exit at next branch check. |
| "I might come back later but not now" | Reply: "Totally fine — door's always open. I'll stop the messages now. Whenever you're ready, just text me." Apply `do-not-market` tag. Note: their account is still recoverable forever. |
| A real concern ("I had a bad experience with...") | Escalate to owner immediately. Personal phone call same day. Document the feedback. |
| "Already at another studio" | Reply: "Glad you found a fit. If it changes, you know where we are." Apply `do-not-market`. |
| "STOP" | GHL auto-handles. Add `do-not-sms`. They still get email unless they also email-opt-out. |

When a member replies to the failed-payment SMS (D):

| If they reply... | Response |
|---|---|
| "On it" / "Thanks" | No automated response needed — front desk acknowledges via Conversations inbox if appropriate. |
| "I want to cancel instead" | Manual escalation. Owner reaches out to acknowledge and process cancellation cleanly (with reason capture) instead of letting it die as a failed payment. |
| "I can't afford it right now" | Owner-personal reply. Offer paused-membership ($0/mo for up to 3 months, account preserved). This is in the playbook even though it's not automated — failed-payment members who can't afford ARE the win-back targets you save with empathy. |
| "Card is fine on my end" | Owner replies, opens a Stripe support ticket. Sometimes legit bank-side issues block charges. Don't let the member's account die because of a Stripe edge case. |

---

## SMS Best Practices for This Studio (win-back specific)

**Pacing:** SMS arrives ~30 min BEFORE the matching email at each stage. Why: the SMS is the immediate signal ("oh, Sunrise"), the email is the deeper detail. Reversing the order (email first) wastes the email's open-window — by the time they read the SMS, the email is buried.

**Tone progression:**
- Day 30: soft check-in
- Day 60: direct offer
- Day 90: honest last-call with acknowledged urgency
- Failed payment: low-alarm helpful

Each stage's SMS *and* email match the same tonal beat — don't have a soft SMS and a hard-sell email at the same stage.

**Compliance:**
- Day-30 SMS includes opt-out language (re-entering marketing contact after cancellation requires fresh consent reminder).
- Day-60 and Day-90 don't repeat opt-out (continuing sequence, member already had opportunity to opt out at Day 30).
- Failed-payment SMS includes opt-out (operationally sensitive but a payment update is borderline transactional — safer to include).

**Quiet hours:** All win-back SMS respect 8 AM – 9 PM contact-local. Failed-payment intervention is sensitive but not transactional in the strict sense — accept the 1-hour wait extension if it lands at 11 PM. (Sending a "your payment failed" message at midnight breeds panic; the 5-day recovery window absorbs the delay easily.)

**Link strategy:** All links go to `book.sunrisewellness.com/comeback?wb=XX` — the auto-coupon-applying funnel. Members never have to type a coupon code. This is the single biggest conversion-rate lever in the system.

---

## A/B Test Ideas (after baseline)

| Test | Variant A (control) | Variant B |
|---|---|---|
| Day-30 angle | "Just checking in — first month 50% off if you want" | "Sarah — quick question: anything we could have done better?" (curiosity + soft offer) |
| Day-60 offer framing | "$39 first month + waived enrollment ($89 savings)" | "$89 less than your last month here" (loss-aversion framing) |
| Failed-payment opener | "Hey {{first_name}}, it's Morgan ☀️" | "Quick: your card on file declined — 30sec to fix" (urgency-first) |
| Day-90 urgency | "this week only" | "the offer expires Friday" (specific deadline date) |

Test one at a time, 2-week minimum runs, target 30+ sends per variant.

---

## What Comes Next

After a member reactivates via the comeback funnel, they're handed off to **[#04 New Member Onboarding](../../04-new-member-onboarding/)** for a fresh 30-day flow.

Members who reach Day 120 without reactivating get tagged `member-permanent-loss` and exit to the long-tail nurture (quarterly "what's new at Sunrise" emails, opt-out respected).

Failed-payment members who recover stay in the regular member lifecycle — no further win-back contact, no tag of shame, treated as normal.
