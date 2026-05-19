# #05 — SMS Templates

> Four SMS messages used in the retention intervention sequence. Each is sent at a different risk threshold with a different tone — lighter for Watching, warmer for At-Risk, owner-personal for Critical. All target under 160 chars per segment.

---

## SMS A — Watching Soft Check-In

**Template name:** `05 — Watching Soft Check-In`

**Trigger:** Branch A of Workflow 05b, fired on transition to `risk-watching` (engagement score 50–69).

**From:** `{{custom_values.business.sms_number}}`

**Body:**

> Hey {{contact.first_name}}, Morgan from {{custom_values.business.short_name}} ☀️ Noticed you've been a bit quiet lately. Everything good? Try our 7 AM yoga this week — it's been a vibe.

**Character count:** ~159 — fits in 1 SMS segment.

**Why this works:** Acknowledges the silence without making it a thing. Asks a genuine question (often gets a real reply). Closes with a specific actionable suggestion that makes coming back this week easy. No link, no offer — just human.

**Note on opt-out language:** This is NOT first contact (the member opted in at signup), so no STOP language required. Adding it would feel oddly cold given the warm-personal tone.

---

## SMS B — At-Risk Warm Hello

**Template name:** `05 — At-Risk Warm Hello`

**Trigger:** Branch B of Workflow 05b, fired on transition to `risk-at-risk` (engagement score 30–49).

**From:** Same.

**Body:**

> {{contact.first_name}} — Morgan here. Haven't seen you at the studio in a bit and I just wanted to say hi. No agenda — reply with anything, even just "busy."

**Character count:** ~158 — single segment.

**Why this works:** More direct than Watching but still warm. The "no agenda" phrase disarms — people who've been avoiding the studio out of guilt feel permission to engage without committing. "Reply with anything, even just 'busy'" gives them a permission slip to say something small, which often opens the door to saying something real.

---

## SMS C — Critical Owner-Personal SMS

**Template name:** `05 — Critical Owner-Personal SMS`

**Trigger:** Branch C of Workflow 05b, fired 2 hours after Critical transition (after the owner has been alerted but before the owner has manually called).

**From:** `{{custom_values.team.owner_first}}`'s personal cell, **not** the general SMS number. This is signaled to the member by the phone number itself — when they look up who texted them, it's Morgan's actual number.

**Body:**

> Hey {{contact.first_name}}, it's Morgan — using my own number this time. Been thinking about you. Can we talk? No sales pitch, I promise. Just want to make sure you're okay. ☀️

**Character count:** ~178 — splits into 2 segments. Acceptable for this critical-tier message; the slightly longer length matches the personal tone.

**Why this works:** The "using my own number this time" phrase is doing massive work — it signals that this is *not* an automated message, that the owner physically picked up her phone, that this member matters enough to warrant the personal channel. For a member 14 days from cancelling, this is often the moment they call back and tell Morgan what's actually going on.

**Edge case:** If the contact has tag `vip-do-not-disturb`, this SMS is **skipped** — the owner handles 100% via direct call/visit. The auto-SMS would feel intrusive to a high-touch member.

---

## SMS D — Save Confirmed (Optional — Member-Facing)

**Template name:** `05 — Save Confirmed Thank You`

**Trigger:** Fired by Workflow 05c, 24 hours after a member transitions from saved-pending to `risk-healthy`. This is optional — toggle off if the studio prefers no acknowledgment.

**From:** Same as Watching SMS (general number).

**Body:**

> {{contact.first_name}} — great seeing you back this week. Whatever brought you in, glad you're here. — Morgan

**Character count:** ~110 — single segment.

**Why this works:** Closes the loop. A saved member who knows they were *noticed coming back* feels more attached than one who returned silently. Sets up the next 30 days for #06 upsell readiness.

**Why this is optional:** Some members find acknowledgment of their absence awkward. The owner should toggle this on for the studio's culture or off if it feels off-brand.

---

## Reply Handling

Replies to any of these SMSes route to the studio's Conversations inbox. The owner sees them in priority, since these are flagged retention conversations.

### Auto-tag on reply

- **Trigger:** Inbound SMS from contact with tag `risk-watching` OR `risk-at-risk` OR `risk-critical`
- **Action:** Add tag `retention-reply-received`
- **Action:** Notify owner: "{{contact.first_name}} {{contact.last_name}} just replied to retention SMS. Engagement score: {{contact.engagement_score}}."
- **Action:** Pause any further automated retention messages for 14 days (relationship is live, system should stay out of the way)

### Common replies and owner-response scripts

| If they reply... | Owner response |
|---|---|
| "Just busy" | "Totally fair — see you when life clears up. No deadline on your end. ☀️" |
| Specific reason — work, kids, travel | Empathetic + specific. Example: "Oh man, that sounds like a stretch. Whenever you're back, your spot's here. If you need to pause billing for a month, just say the word." |
| A complaint about the studio | Listen, apologize, offer to talk on the phone if it's substantial. Tag contact `feedback-received` for [#07 Reviews](../../07-reviews-and-reputation/) follow-up. |
| Asking to pause/cancel | Acknowledge, route to retention save script. Tag `member-pause-requested` or `member-cancel-requested`. Do not auto-process cancellation — owner reviews. |
| Asking for a different class/trainer | "Yes — let's. Try {{recommendation}} this week, on me." Issue a free class credit. |
| Silence (no reply) | System continues per workflow. Owner can still manually reach out if they want. |

---

## SMS Best Practices for Retention Specifically

**Sender identity matters more here than anywhere else.** A retention SMS that looks like marketing (sent from a 5-digit shortcode, signed "The Sunrise Team") gets ignored. A retention SMS that looks like a friend (sent from Morgan's number, signed "Morgan") gets answered. The Critical-tier message uses Morgan's actual cell — that's not a copy quirk, it's the entire mechanism.

**Don't include offers in retention SMS.** Offers belong in email where they can be explained. SMS with an offer ("Free PT! Click here!") reads as a sales pitch and breaks the relational tone the SMS is supposed to set.

**Quiet hours are STRICT here.** These are non-urgent emotional messages. Sending one at 11 PM destroys the "personal note" framing. Limit sends to **9 AM – 6 PM contact-local time**, weekdays preferred. Saturday morning works; Sunday evening does not.

**Frequency cap.** A member should never receive more than **one retention SMS per 14-day period**. If they go Watching → At-Risk → Critical in rapid succession, the workflow should *only fire the most severe message*, not all three. The transition-tag mechanism in the workflow handles this — verify in testing.

---

## What Comes Next

After the SMS sequence:

- **Reply received:** Pauses automation, escalates to Morgan personally.
- **Member visits within follow-up window:** Workflow 05c fires the save-success path.
- **No reply, no visit:** Member continues under nightly scoring. If score keeps falling, next severity tier fires. If score recovers, save success path.
- **Member cancels:** Routed to [#09 Win-Back Lapsed Members](../../09-win-back-lapsed-members/) by Workflow 05d.
