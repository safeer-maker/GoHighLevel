# #08 — SMS Templates: Referral Engine

> Three SMS messages used in the referral engine. Same rules as #01: under 160 chars target, one link max, opt-out on first contact.

---

## SMS A — Member Referral Invite (sent to newly active members)

**Template name:** `08 — Member Referral Invite`

**Trigger:** Sent 24 hours after `member-active` tag, via Workflow `08a — Referral Code Generation`.

**From:** `{{custom_values.business.sms_number}}`

**Recipient:** Newly active member

**Body (160 chars target):**

> Hey {{contact.first_name}}, it's Morgan ☀️ Your Sunrise referral link is live — friends get $20 off, you get a free PT session: {{contact.referral_share_url}}
>
> Reply STOP to opt out.

**Character count:** ~178 — single segment.

**Why this works:** First-name, owner-personal, includes the *exact* link they need to forward (no "click here to find your link" friction), explicitly states both rewards in one line. The opt-out language is required (first contact in this workflow).

**Note on link length:** the `referral_share_url` will be ~80 chars by itself. If it pushes the SMS over 160, drop the brand emoji and shorten the intro: "Hey {{first_name}}, your Sunrise referral link is live — $20 off for friends, free PT for you: {{url}}"

---

## SMS B — Referrer Got A Conversion (sent to referrer when referee converts)

**Template name:** `08 — Referrer Conversion Notification`

**Trigger:** Sent immediately when `trial-converted` tag applied to referee with `referred_by_contact_id` populated, via Workflow `08b — Referral Conversion Credit`.

**From:** Same number.

**Recipient:** The referrer (looked up via `referred_by_contact_id`)

**Body:**

> {{referrer.first_name}} ☀️ Big news: {{contact.first_name}} just joined Sunrise because of your link. Your free PT session is loaded — book anytime: {{custom_values.business.booking_url}}/pt

**Character count:** ~178 — single segment.

**Why this works:** Celebrates the moment instantly — referrer is on the phone within seconds of the referee's checkout. Names both parties (specific, not generic). One CTA: redeem the credit. No opt-out needed here (continuing contact with an active member who already consented).

---

## SMS C — Referee Welcome (sent to referee post-conversion)

**Template name:** `08 — Referee Welcome (post-conversion)`

**Trigger:** Sent immediately when `trial-converted` tag applied to referee with `referred_by_contact_id` populated, via Workflow `08b`.

**From:** Same number.

**Recipient:** The new member (referee)

**Body:**

> Hey {{contact.first_name}}, it's Morgan ☀️ Welcome to Sunrise — your $20 credit's applied and {{referrer.first_name}} got a free PT session for sending you. We're glad you're here.

**Character count:** ~187 — single segment (close to limit; tested).

**Why this works:** Affirms the credit was applied (no "did it work?" anxiety), names the referrer (closes the social loop), warm welcome from owner. No CTA — this is a relationship message, not a transactional one. The booking-link CTA already lives in the matching welcome email.

---

## Reply Handling

When a referrer replies to **SMS A** (the invite), common responses:

| If they reply... | Front-desk / owner response |
|---|---|
| "Thanks!" or any acknowledgment | No automated response needed — front desk reads and moves on. Optional: add tag `engagement-replied` for retention scoring. |
| "How do I share it?" | Reply with: "Easiest way — tap your link and forward the text to a specific friend. Or paste it in your Instagram story. Want me to text you a pre-written one?" |
| A friend's phone number | Front-desk action: send the friend a direct SMS with the link, attributing to the referrer. (Manual until you build a "refer a friend by typing their number" funnel, which is out of scope here.) |
| "I don't really refer people" | Reply: "Totally fine — the link's there if it ever comes up. No pressure." Add tag `referral-passive` so future referral reminders don't re-target them. |
| "STOP" | GHL auto-handles. Add `do-not-sms`. They still get email referral content unless they also opt out of email. |

When a referrer replies to **SMS B** (the conversion notification):

| If they reply... | Response |
|---|---|
| "🎉" or similar | Front-desk reply: "Pumped for both of you! Come grab your PT session whenever." |
| "Already had a PT this week!" | Reply: "All good — the credit doesn't expire. Save it for whenever you want a bonus session." |
| Question about the credit | Reply with how-to-redeem instructions. |

When a referee replies to **SMS C** (their welcome):

| If they reply... | Response |
|---|---|
| Any acknowledgment | Same handling as any new-member welcome reply — route to onboarding (#04). |
| Booking questions | Front-desk handles via Conversations inbox. |

---

## SMS Best Practices for This Studio (referral-specific)

**Link length:** The personalized referral URL is long (~80 chars). Two options:

1. **Accept the length** — modern SMS clients render long URLs as tappable links, so visual length doesn't break the experience.
2. **Use a URL shortener** (Bitly, GHL native shortener) per-member — generates `sunr.is/sarah42` which is cleaner. Cost: one more system to maintain, and short-link analytics overlap with GHL's native tracking.

For launch: accept the length, ship it. Add shortener in v2 if click-tracking analytics need it.

**Tone:** Same brand voice as #01 — warm, first-person, no corporate "we." Sunrise emoji ☀️ allowed sparingly (one per SMS max). Avoid generic celebration emoji (🎉🙌) — they read younger than the brand target.

**Timing:**
- SMS A (member invite): scheduled for 24 hours after `member-active`, in the contact's local-time **late morning window (10 AM – 12 PM)** for highest open + share rate. (Skip the early-morning window — members don't want to think about referring at 6 AM.)
- SMS B & C (conversion notifications): immediate. These are transactional moments — delay kills the magic. Bypass quiet-hours respect for these (they're responsive to an action the referee just took).

**Compliance:**
- Opt-out language on SMS A (first contact in this workflow).
- Members already consented at signup, so SMS B & C don't need fresh opt-out language but every workflow checks the `do-not-sms` tag before sending.

---

## A/B Test Ideas (after baseline is set)

| Test | Variant A (control) | Variant B |
|---|---|---|
| SMS A — opener | "Hey {{first_name}}, it's Morgan ☀️ Your Sunrise referral link is live…" | "{{first_name}} — quick gift for you: your personal referral link to share with friends" |
| SMS B — emphasis | Leads with referee's name ("{{contact.first_name}} just joined…") | Leads with reward ("Your free PT session is loaded — {{contact.first_name}} just signed up!") |
| SMS A — CTA framing | "friends get $20 off, you get a free PT session" | "$20 for them, free PT for you — both happen automatically" |

Test one at a time, 2-week minimum runs, target 40+ sends per variant before declaring a winner.

---

## What Comes Next

Once the referee converts via SMS C, they're handed off to **[#04 New Member Onboarding](../../04-new-member-onboarding/)** for the 30-day flow.

The referrer's free PT credit lives in `pt_credit_balance` — consumed when they next book PT (front-desk checks balance before charging).

Top quarterly referrers receive a separate email (no SMS) for the recognition campaign — see [emails.md](emails.md) Email 4.

If a member shares the link but no one converts after 30 days, no penalty and no nudge — referral is opt-in behavior; we never guilt members into recruiting.
