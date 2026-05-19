# #07 — SMS Templates

> Three SMS messages for the review system: post-class ask, post-PT ask, and a high-score thank-you. All target under 160 chars per segment. The post-class and post-PT messages fire 30 minutes after the appointment.

---

## SMS A — Post-Class Review Ask

**Template name:** `07 — Post-Class Review Ask`

**Trigger:** Workflow 07 step 4.6, 30 minutes after group-class attendance.

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}} — Morgan ☀️ How was class today? 30 sec to tell us → {{custom_values.business.short_review_url}}

**Character count:** ~127 — single segment.

**Why this works:** Owner-voiced ("Morgan"), warm emoji (one only), specific reference to "today's class" — makes it clear this is a real follow-up, not generic spam. Single link, short, no opt-out language (not first contact — member opted in at signup). The brevity is the magic; if it asked any more it'd feel like work.

**Note on the link:** `short_review_url` should be a vanity-domain short URL (e.g., `srws.us/r`) that resolves to the Smart Review Router funnel with `?contact_id={{contact.id}}` automatically appended via redirect logic. If you don't have a short URL, use the full funnel URL — slightly longer but functional.

---

## SMS B — Post-PT Review Ask

**Template name:** `07 — Post-PT Review Ask`

**Trigger:** Workflow 07 step 4.6, 30 minutes after PT session attendance.

**From:** Same sender.

**Body:**

> {{contact.first_name}}, hope today's session with {{contact.assigned_trainer}} crushed it. How'd it feel? 30 sec to share → {{custom_values.business.short_review_url}}

**Character count:** ~159 — single segment.

**Why this works:** Names the specific trainer (`{{contact.assigned_trainer}}`) — makes the message feel personalized to the actual session the member just had. The trainer reference also creates a positive recall trigger (member just spent an hour with them). "Crushed it" matches the brand's energetic voice.

**Variant if `assigned_trainer` is null:** Use SMS A's copy instead, with "session" substituted for "class": "How was your session today? 30 sec to tell us →"

---

## SMS C — High-Score Thank You (Optional Follow-Up)

**Template name:** `07 — High-Score Thank You`

**Trigger:** Fired by Workflow 07b (high-score handler), 1 hour after a 5-star review submission. Optional — toggle off if the studio prefers no follow-up.

**From:** Same sender.

**Body:**

> {{contact.first_name}} — thank you for the kind words 🙏 Genuinely means a ton. See you next class. ☀️ — Morgan

**Character count:** ~115 — single segment.

**Why this works:** Closes the loop with gratitude that feels personal. The two emojis match the brand voice (one folded hands, one sunrise). Reinforces that a real person sees and appreciates the review — most studios go silent after a review, missing the opportunity to deepen the relationship.

**Why optional:** Some members might find acknowledgment awkward, or might miss writing the review on Google but still get this SMS (if they tapped 5 but closed the Google tab before submitting). The studio can decide based on volume. Default: ON.

---

## SMS D — Win-Back-via-Feedback (Owner-Personal — fired by Low Score Handler)

**Template name:** `07 — Private Feedback Owner SMS`

**Trigger:** Fired by Workflow 07c (low-score handler), within 1 hour of a low-score form submission. Only sent if `feedback_phone_ok` ≠ Yes (because if they said yes to phone, owner calls directly).

**From:** **Morgan's personal cell number** (not general sender — signaled by the phone number itself).

**Body:**

> {{contact.first_name}}, Morgan here. Just saw your note — I'm really sorry. Can we talk this through? I want to make it right. Reply when you've got a sec.

**Character count:** ~155 — single segment.

**Why this works:** Sent from Morgan's personal number — the same signal mechanism used in [#05 retention critical SMS](../../05-retention-and-churn-prevention/assets/sms.md). Member sees an unknown number, looks it up, realizes it's the owner's actual cell, and the message lands as "the owner cares enough to text me personally." This often converts a complaint into a saved member.

**Edge case:** If `do-not-sms` is set on the contact, this SMS is skipped — owner gets an alert to handle via email or call instead.

---

## Reply Handling

Replies to any of these SMSes route to the studio Conversations inbox. Each scenario:

### Reply to review-ask SMS (A or B)

| If they reply with... | Auto-action | Owner action |
|---|---|---|
| "Yeah it was great" / similar positive | Auto-tag `review-replied-positive`. Notify owner: "{{name}} responded positively but didn't go to the funnel — manually ask about Google review." | Owner replies personally with the funnel link: "So glad! Would you mind tapping here when you have 30 sec? Means a ton." |
| Specific feedback (positive or negative) in the reply | Auto-tag `feedback-conversational`. Notify owner. | Owner replies personally — handle as in-person feedback. If negative, may evolve into a save attempt. |
| "Not now" / similar deflection | Auto-tag `review-deferred`. Pause workflow 90 days. | None — automated. |
| Question ("how do I leave a review?") | Auto-tag `review-needs-help`. | Owner / front-desk replies with funnel link + simple instructions. |
| "Stop" / opt-out | GHL auto-handles. Tag `do-not-sms` applied. | None. |

### Reply to thank-you SMS (C)

Most replies are gratitude-acknowledgment ("you're welcome!"). Owner reads in inbox, no action needed unless conversational.

### Reply to owner-personal SMS (D)

This is a relational conversation. Owner handles 100% personally. No automation should respond. The studio's reputation depends on the owner showing up here as a human.

---

## SMS Best Practices for Reviews Specifically

**Quiet hours strict.** Review SMS goes only between **10 AM – 7 PM contact-local time**. Sending a review ask at 11 PM is annoying — and the recipient is more likely to give a low rating just because they're tired.

**Timing matters more than copy.** A perfectly-worded review ask sent at the wrong moment (the day after a missed class, while they're in the gym, in the middle of a workday) gets ignored. The 30-minute post-appointment window is the magic. Don't compromise on it.

**One review ask SMS per 90-day window.** Frequency cap enforced via `campaign-review-ask` tag. A member who attends 3 classes a week shouldn't get 3 review asks a week — they'd get annoyed and leave a bad review *out of irritation*.

**Single link, branded short domain.** If the URL looks long or sketchy, the click-through rate halves. Use the studio's branded short URL.

**Owner voice, not corporate.** "How was class?" is owner-voice. "We'd love your feedback!" is corporate-voice. The first gets replies; the second gets ignored.

**Don't bribe for reviews.** "Leave a review and get $5 off!" violates Google's review policy and damages trust. The ask should be a request, not a transaction.

---

## What Comes Next

After the SMS sequence:

- **Member taps link, rates 4-5:** Goes to Google. Workflow 07b fires the thank-you SMS and tags `referral-prompt-ready` for [#08](../../08-referral-engine/) after 7 days.
- **Member taps link, rates 1-3:** Goes to private feedback form. Owner alerted within minutes. Workflow 07c routes to retention monitoring.
- **Member doesn't tap:** Follow-up email sent 3 days later (see [emails.md](emails.md)). If still no engagement after 7 days, member is left alone for 90 days.
- **Member replies to SMS instead of tapping link:** Owner handles personally via Conversations inbox.
