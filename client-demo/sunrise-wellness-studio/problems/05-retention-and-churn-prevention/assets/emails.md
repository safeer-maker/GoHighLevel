# #05 — Email Templates

> Production-ready email copy for the retention intervention sequence. Each email is sent by the **owner**, Morgan, from her personal-feeling reply-to address. Tone: warm, specific, not pitchy. The point is the relationship, not the offer.

---

## Email 1 — At-Risk Personal from Morgan

**Template name:** `05 — At-Risk Personal from Morgan`

**Send timing:** 4 hours after the At-Risk warm-hello Email (Branch B, step 5)

**From:**
- Name: `Morgan from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.owner_email}}`

**Reply-to:** `{{custom_values.business.owner_email}}` (replies go straight to Morgan)

**Subject:**
> {{contact.first_name}}, I noticed you've been quiet

**Preview text:**
> Just a personal check-in from me — no pitch, promise.

---

### Email Body

**Header band:** Soft cream `#FFF8F0`, minimal. Small Sunrise logo top-left. **No** big hero image — this is supposed to feel like a personal email, not a marketing one.

---

**Greeting (regular paragraph, no big H1):**

> Hey {{contact.first_name}} —

**Body:**

> Morgan here. I run Sunrise.
> 
> This isn't an automated "we miss you" email (well, technically it is — but I wrote it myself and I'm the one who reads the replies). I noticed your check-ins have slowed down the last few weeks and I wanted to reach out personally before the system did anything else.
> 
> Most of the time when this happens, it's one of three things:
> 
> - **Life got busy.** Work, kids, travel, that thing you've been putting off. Completely normal. Happens to all of us. If that's it, no action needed from you — I just want you to know your spot is here when you're ready.
> - **Something's off with the studio.** A class time stopped working, the new instructor isn't your vibe, the locker rooms have been crowded, *whatever*. I want to know. I can almost always fix it.
> - **You're rethinking whether this is right for you.** Also fair. If that's where you're at, let's talk. Sometimes a different class mix, a different trainer, or even a different membership tier changes everything. Sometimes it doesn't and that's okay too.

---

**CTA button (coral, centered, medium):**

> **Just hit reply →**

(No link — the button is symbolic. The CTA action is to reply to the email.)

---

**Body continued:**

> Whichever it is, I'd genuinely love a one-line reply. Doesn't need to be a paragraph. "I'm good, just busy" is a perfect answer.
> 
> And if it's been hard to come back because life's been heavy — I see you and we're here for you. No pressure, no judgment, no expiring offers in this email.
> 
> Just me, reaching out.

---

**Signature:**

> — Morgan
> 
> Morgan Riley · Owner, {{custom_values.business.name}}
> 
> P.S. If replying to an email feels like too much work, just email me back at {{custom_values.business.sms_number}}. Either works.

---

**Footer band:** Cream background, minimal.

- {{custom_values.business.address_line}} · {{custom_values.business.phone}}
- Hours: {{custom_values.hours.full}}
- Unsubscribe: {{unsubscribe_link}}
- {{custom_values.legal.footer}}

---

**Why this email works:**

- No hero image, no sales banner — looks personal.
- Three named possibilities ("life / studio / rethinking") give the reader a low-friction way to identify with one and reply.
- No offer, no link, no urgency. The CTA is a reply, not a click.
- P.S. with the Email fallback handles inbox-resistant repliers.
- Replies route to Morgan's inbox directly — she actually answers them.

---

## Email 2 — Win-Them-Back Free PT Offer

**Template name:** `05 — Win-Them-Back Free PT Offer`

**Send timing:** 2 days after Email 1 IF no reply and no visit (Branch B, step 8)

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, want to try something different on me?

**Preview text:**
> A free one-on-one session with one of our trainers — no strings, no upsell.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Morgan again. I sent you a check-in a few days ago and didn't hear back — totally fine, no judgment. But before I let the system go quiet on you, I wanted to make one more offer.
> 
> A lot of times when members drift, it's because their routine got stale. The same classes, the same time, the same energy. I get it — I do it too.
> 
> So here's what I'd like to do: **give you a free 1-on-1 personal training session.** Not a sales call disguised as a session. An actual PT session with {{custom_values.team.lead_trainer}} (or whichever trainer you pick) where you can:
> 
> - Try a workout style you've never tried (mobility? strength block? recovery?)
> - Get a fresh-eyes assessment on form and progress
> - Map a 4-week plan that doesn't bore you
> 
> No expectation that you do anything afterward except show up to a class that feels new.

---

**CTA button (coral, centered, large):**

> **Book My Free PT Session →**

(Links to `{{custom_values.business.booking_url}}` with coupon code `RETAIN-PT` pre-applied, which redeems one free PT-SINGLE.)

---

**Body continued — "what to know":**

> A few notes so this feels easy:
> 
> - **No expiration.** This stays open for you for 30 days. Book it whenever you can.
> - **Pick any trainer.** {{custom_values.team.lead_trainer}}, {{custom_values.team.trainer_2}}, {{custom_values.team.trainer_3}} — all great, slightly different styles. Bio on the booking page.
> - **You don't have to do anything different after.** Show up to one PT session, then go back to your regular thing. Or don't. The offer's on me either way.

---

**Closing:**

> If a PT session isn't the thing, and the real issue is the membership doesn't fit anymore — that's also fair. Reply to this email and we'll figure out what *would* fit. Sometimes the answer is pausing for a month while life calms down. Sometimes it's switching tiers. Sometimes it's something I haven't thought of yet.
> 
> Either way, you matter to us.
> 
> — Morgan

---

**Footer band:** Same as Email 1.

---

**Why this email works:**

- Real offer with real value ($85). Not a "10% off your next class" gimmick.
- Specific named trainers — gives the member a concrete choice instead of an abstract "PT session."
- "No expiration" removes urgency anxiety — a member who's been distant doesn't need a deadline pushing them.
- Acknowledges the membership might not be the right fit, *normalizes* leaving. Counter-intuitive, but builds trust and surfaces honest replies.

---

## Email 3 — Watching Soft Check-In (Email)

**Template name:** `05 — Watching Soft Check-In`

**Send timing:** Only used when Email is suppressed (`do-not-email` tag). Otherwise Branch A is Email-only.

**From:** Same as Email 1.

**Subject:**
> {{contact.first_name}}, all good?

**Preview text:**
> Quick check-in — no agenda.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Morgan — quick one. I saw your check-ins have slowed a bit this month. Nothing alarming, just my noticing.
> 
> If everything's fine and life's just busy — no need to reply. Your spot's here.
> 
> If something at the studio is off, or you want to mix things up — hit reply and tell me. I'm easy to reach.
> 
> See you soon hopefully.
> 
> — Morgan
> 
> P.S. Try the 7 AM yoga this week. {{custom_values.team.trainer_2}} is teaching it now and it's a totally different vibe.

---

**Footer:** Same as Email 1, smaller version.

---

**Why this email works:**

- Six lines. Reads in 8 seconds.
- No CTA button — pure relational.
- The P.S. seeds a specific concrete reason to come back this week — a low-effort nudge that often works better than the email itself.

---

## Email 4 — Save Win Celebration (Internal — to Owner)

**Template name:** `05 — Save Win Celebration (Owner Internal)`

**Send timing:** Fired by Workflow 05c when a member moves from saved-pending to risk-healthy.

**To:** `{{custom_values.business.owner_email}}`

**Subject:**
> Win — {{contact.first_name}} {{contact.last_name}} is back to healthy

---

### Email Body

> {{contact.first_name}} {{contact.last_name}} just moved from at-risk back to healthy.
> 
> **The save:**
> - Was at risk for: ~{{custom_values.placeholder.days_in_risk}} days (replace with actual computed days)
> - Triggered intervention: {{contact.placeholder.save_branch}}  (Watching / At-Risk / Critical)
> - Current engagement score: {{contact.engagement_score}}
> - Monthly rate retained: ${{contact.monthly_rate}}
> - Annualized save value: ${{contact.placeholder.annual_value}}
> 
> They're now in the Retention pipeline's **Saved** stage and have the `member-saved` tag.
> 
> In 30 days, the system will mark them `save-mature-30d` and they'll be eligible for the next upsell wave (see [#06 Upsell & Cross-Sell](../../06-upsell-and-cross-sell/)).
> 
> Nice work — you (or the system on your behalf) just kept this member from walking.

---

**Why this email works:**

- The owner deserves a moment of dopamine for the saves the system makes on her behalf. It also reinforces that retention is *working*, which makes her trust the system more and check the Critical kanban more often.

---

## Email Building Notes

**Tone calibration for at-risk emails:**
- Slower than marketing emails. Use spaces. Use paragraph breaks. Read it out loud — does it sound like a friend or a brand? It should sound like a friend.
- Never use "we miss you" as a subject line — it's the most-burned phrase in retention email. Use specificity instead.
- Never reference the algorithm directly ("our system noticed..."). Always frame it as Morgan personally noticing.
- Never include an offer in the first at-risk email. First email is relational. Offer comes only on email 2 if relational didn't work.

**Mobile rendering:**
- Single column.
- Body font 16px minimum, line-height 1.6 for readability.
- CTA buttons 48px+ tall.
- No multi-image collages — the personal-feel only survives if the layout looks like a normal email.

**Deliverability:**
- Send from a real human address (owner's email), not noreply@.
- Sending domain SPF/DKIM/DMARC verified.
- Avoid spammy at-risk subject patterns: "ACT NOW", "FINAL CHANCE", multiple exclamations, ALL CAPS.

**Personalization fallbacks:**
- `{{contact.first_name}}` → fallback: "there"
- `{{contact.fitness_goal_primary}}` → omit the line if missing
- `{{contact.assigned_trainer}}` → fallback: `{{custom_values.team.lead_trainer}}`

---

## What Comes Next

After the retention email sequence:

- **If the member re-engages:** Workflow 05c moves them to Saved. 30 days later, the `save-mature-30d` tag opens them up for [#06 Upsell & Cross-Sell](../../06-upsell-and-cross-sell/) reconnect offers.
- **If the member cancels anyway:** Workflow 05d routes them to [#09 Win-Back Lapsed Members](../../09-win-back-lapsed-members/) for the 90-day reactivation sequence.
- **Replies to Morgan's email:** Land in her inbox. She handles personally. No automation on reply (intentional — these conversations need human nuance).
