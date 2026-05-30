# #08 — Email Templates: Referral Engine

> Production-ready email copy for the referral engine. Each email has subject, preview text, full body, and merge fields. Paste into GHL email builder.

---

## Email 1 — Referrer Notification: "Your friend just signed up!"

**Template name:** `08 — Referrer Notification — Conversion`

**Send timing:** ~5 minutes after `trial-converted` tag applied to the referee (via Workflow `08b — Referral Conversion Credit`)

**Recipient:** The referrer (looked up via `referred_by_contact_id` on the new member)

**From:**
- Name: `{{custom_values.team.owner_first}} from {{custom_values.business.short_name}}`
- Email: `{{custom_values.business.email}}`

**Reply-to:** `{{custom_values.business.owner_email}}`

**Subject:**
> {{referrer.first_name}}, {{contact.first_name}} just joined Sunrise — your free PT session is on us ☀️

**Preview text:**
> A heads up: your friend signed up and your PT credit is in your account.

---

### Email Body

**Header band:** Sunrise gradient. Logo centered.

---

**Greeting (H1, deep slate):**

> Hey {{referrer.first_name}} —

**Body:**

> Quick celebration text — **{{contact.first_name}} {{contact.last_name}} just signed up for a Sunrise membership** because you sent them the link. That's a big deal.
>
> A few things:

**3-card block (stack on mobile):**

| Card | Title | Body |
|---|---|---|
| 🎁 | **Your free PT session is loaded** | Your PT credit balance is now **{{referrer.pt_credit_balance}}**. Book whenever — no expiration, no catch. |
| 📊 | **Your running total: {{referrer.referrals_converted_count}} referrals** | You're officially building the Sunrise community. Quarterly top referrers get a Sunrise sweatshirt and a hand-written note from me. |
| 💛 | **Want to tell {{contact.first_name}} you're glad they came?** | They'll get a "welcome from {{referrer.first_name}}'s recommendation" note from us too — so they know it came from you. |

---

**CTA button (large, coral, centered):**

> **Book My Free PT Session →**

(Links to `{{custom_values.business.booking_url}}/pt`)

---

**Sub-section: Want to refer more friends?**

> If you know anyone else who'd love it here, your link is still active and ready to share:
>
> **{{referrer.referral_share_url}}**
>
> Every friend who signs up = another free PT session for you. There's no cap.

---

**Closing:**

> Genuinely — thank you. Members who refer friends are how this studio grows. You're the engine.
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

## Email 2 — Member Referral Invite: "Here's your link"

**Template name:** `08 — Member Referral Invite`

**Send timing:** 24 hours after `member-active` tag applied (via Workflow `08a — Referral Code Generation`)

**Recipient:** Newly active member

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}}, here's your Sunrise referral link (free PT for you, $20 off for them)

**Preview text:**
> Welcome to the community. Want to bring a friend? Your link's inside.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Welcome to Sunrise — I'm so glad you're here. Quick thing while you're settling in.
>
> Every member gets a personal referral link. When a friend uses it:
>
> - **They get $20 off their first month** + a free 7-day trial first.
> - **You get a free 1-on-1 PT session** the moment they convert to a paid membership.

---

**Your Personal Link block (gold panel, centered):**

> **Your link:**
>
> **{{contact.referral_share_url}}**
>
> Your code: **{{contact.referral_code}}**

---

**CTA button (coral):**

> **Share My Link →**

(Links to a pre-filled Email share intent: `sms:?&body=Hey%20—%20I%27ve%20been%20going%20to%20Sunrise%20Wellness%20and%20it%27s%20genuinely%20the%20best%20studio%20I%27ve%20found.%20Use%20my%20link%20for%20%2420%20off%20your%20first%20month%20%2B%20a%20free%20week%3A%20{{contact.referral_share_url}}`)

---

**Sub-section: How to share it (no pressure)**

> Most members share it one of three ways:
>
> 1. **Text the link directly to a specific friend** — easiest. The tap above pre-writes the text.
> 2. **Post it in your Instagram story** — paste the link with a quick "love this place, $20 off if you wanna try" caption.
> 3. **Bring a friend to your next class** — tell them at the door, we'll honor the credit when they sign up.

---

**Sub-section: No quotas, no pressure**

> Genuinely no expectation here. Some members refer a dozen friends, some refer none. Either is fine. We just want you to have the link in case it comes up.
>
> Questions? Just hit reply.
>
> — Morgan

---

**Footer:** Same as Email 1.

---

## Email 3 — Referee Welcome: "Welcome — and thanks for trusting {{referrer.first_name}}"

**Template name:** `08 — Referee Welcome (post-conversion)`

**Send timing:** ~10 minutes after `trial-converted` tag on the referee (via Workflow `08b`)

**Recipient:** The referee (the friend who just converted)

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}}, welcome — and thanks for trusting {{referrer.first_name}}'s recommendation ☀️

**Preview text:**
> A real welcome. Plus, your $20 was applied — you're not getting any "surprise charges" email.

---

### Email Body

**Greeting:**

> Hey {{contact.first_name}} —

**Body:**

> Officially welcome to the Sunrise community — and a real thank-you for trusting {{referrer.first_name}}'s recommendation enough to walk in.
>
> A few logistics:

**Mini table:**

| Item | Status |
|---|---|
| Your $20 credit | Applied to your first month — already done |
| Your tier | {{contact.membership_tier}} ($**{{contact.monthly_rate}}**/month) |
| First billing date | {{contact.membership_start_date}} |
| Welcome to {{referrer.first_name}} | We're letting them know you joined — they got a free PT session for it |

---

**Sub-section: What happens next**

> You're now in our 30-day onboarding flow (it's gentle — I promise). Here's what to expect:
>
> - **Day 1 (today):** Front desk gets you set up with the app, locker, and studio tour.
> - **Day 3:** I'll text to make sure your first class worked out.
> - **Day 7:** Your trainer checks in with a quick goal-setting note.
> - **Day 14:** Two-week milestone — most members hit their groove around now.
> - **Day 30:** Goal review with your trainer. We adjust based on what's working.

---

**CTA button (coral):**

> **Book My First Class →**

(Links to `{{custom_values.business.booking_url}}`)

---

**Sub-section: A genuine thanks**

> Members who join because a friend recommended them stay with us longer, hit goals faster, and tell more friends. It's not a coincidence — there's something different about walking in already knowing someone.
>
> If anything's confusing or you want a real human to text with, just reply or text us at {{custom_values.business.sms_number}}.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer:** Same as Email 1.

---

## Email 4 — Quarterly Top-Referrer Recognition

**Template name:** `08 — Quarterly Top Referrer Recognition`

**Send timing:** Q1 start (Jan 1), Q2 start (Apr 1), Q3 start (Jul 1), Q4 start (Oct 1), 9 AM owner-local. Sent to top 3 referrers in trailing 90 days. (Workflow `08c`.)

**Recipient:** Top 3 referrers

**From:** Same as Email 1

**Subject:**
> {{contact.first_name}} — you're one of Sunrise's top referrers this quarter ☀️

**Preview text:**
> A genuine thank-you, a bonus PT session, and something coming to you in person.

---

### Email Body

**Header band:** Sunrise gradient with a gold "Top Referrer — {{quarter_label}}" badge graphic at top.

---

**Greeting (H1):**

> {{contact.first_name}} —

**Body:**

> Quick celebration: you're officially one of Sunrise's **top 3 referrers** for {{quarter_label}}.
>
> Over the last 90 days, you've personally brought **{{contact.referrals_converted_count}} new members** into this community. That's not a small thing. Members like you are how this studio exists.

---

**3-card block:**

| Card | Title | Body |
|---|---|---|
| 🎁 | **Bonus 2 PT sessions** | We added 2 more PT credits to your account. Your current balance is **{{contact.pt_credit_balance}}**. |
| 👕 | **Sunrise sweatshirt + handwritten card** | I'm bringing one by the studio for you next time you're in. (Yes, a real handwritten note. No corporate fluff.) |
| 💛 | **Founding-member tier respect** | When we add member-only perks (early class access, member events, etc.), top referrers get them first. |

---

**Sub-section: Your impact, in numbers**

> Just for context:
>
> - **{{contact.referrals_converted_count}}** members joined Sunrise because of you in the last 90 days.
> - That's projected **${{calculation: contact.referrals_converted_count * 1100}}** in lifetime value to the studio.
> - More importantly — those are real people who walked into a workout community because you opened the door.

---

**CTA button (coral):**

> **Keep Sharing My Link →**

(Links to a pre-filled Email share intent with their referral URL.)

---

**Sub-section: Stop by**

> Genuinely, come find me at the studio this week. Coffee or tea on me. I want to thank you in person.
>
> — Morgan
>
> Morgan Riley · Owner, {{custom_values.business.name}}

---

**Footer:** Same as Email 1.

---

## Email-Building Notes

**Tone calibration:**
- Genuine over hyped. "Thank you" lands harder than "amazing!!"
- First-person from Morgan. No corporate "we appreciate your business."
- Specific numbers over vague praise. "{{contact.referrals_converted_count}} new members" beats "you're a top supporter."
- For the top-referrer email especially: the *physical sweatshirt + handwritten card* is the differentiator. The email is just the appetizer.

**Personalization fallbacks:**
- `{{referrer.first_name}}` → fallback: "your friend" (used in Email 3 if for any reason the referrer lookup fails)
- `{{contact.referral_share_url}}` → fallback: the generic referral funnel URL `{{custom_values.business.booking_url}}/refer` (link works but won't auto-attribute)
- `{{contact.pt_credit_balance}}` → fallback: numeric `1` (assume at least this one credit was awarded)
- `{{quarter_label}}` → resolved by workflow as `Q1 2026`, `Q2 2026`, etc.

**Mobile rendering:** Same standards as #01 — single-column, 16px body min, 44px CTA min, header image graceful degradation.

**Deliverability notes:**
- The "$20 off" subject line of Email 1 (referrer notification) can trip spam filters that hate dollar signs. Consider variant: "20 dollars off" or "your friend just signed up — your credit is loaded".
- Email 4 (top referrer) is high-engagement and rarely flagged; safe to use the celebration emoji in subject.
