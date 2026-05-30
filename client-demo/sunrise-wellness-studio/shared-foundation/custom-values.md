# Shared Foundation — Custom Values

> Global variables reused everywhere — emails, funnels, workflow messages. Set them once here. When the studio's phone number changes (or the trial offer changes, or the owner's name changes), you update **one place** and every template propagates automatically.

---

## Build Path

Navigate to **Settings > Custom Values** in your GHL sub-account. Add each value below by clicking **+ Add Custom Value**.

Reference syntax in templates: `{{custom_values.value_name}}` — GHL's editor will autocomplete.

---

## Group 1: Business Identity

| Custom Value | Value | Notes |
|---|---|---|
| `business.name` | Sunrise Wellness Studio | The studio's full name |
| `business.short_name` | Sunrise | Used in casual Email ("Hey Sarah, it's Sunrise!") |
| `business.tagline` | Rise. Move. Glow. | Brand tagline |
| `business.phone` | (555) 723-1900 | Main number — replace with real |
| `business.sms_number` | (555) 723-1901 | GHL number for outbound Email |
| `business.email` | hello@sunrisewellness.com | General inbox |
| `business.owner_email` | morgan@sunrisewellness.com | Owner inbox for high-priority alerts |
| `business.address_line` | 123 Wellness Way, Springfield, IL 62701 | Street address |
| `business.address_short` | 123 Wellness Way | For Email where space matters |
| `business.website` | https://sunrisewellness.com | Public site URL |
| `business.booking_url` | https://book.sunrisewellness.com | Main booking funnel |
| `business.google_review_url` | https://g.page/r/SunriseWellnessStudio/review | Direct link to Google review form |
| `business.timezone` | America/Chicago | Used for scheduled messages |

---

## Group 2: Hours

| Custom Value | Value |
|---|---|
| `hours.weekday` | Mon–Fri 6AM–9PM |
| `hours.saturday` | Saturday 8AM–4PM |
| `hours.sunday` | Sunday 9AM–1PM |
| `hours.full` | Mon–Fri 6AM–9PM, Sat 8AM–4PM, Sun 9AM–1PM |
| `hours.holiday_note` | Closed major holidays — see website for current calendar |

---

## Group 3: Team

| Custom Value | Value |
|---|---|
| `team.owner_name` | Morgan Riley |
| `team.owner_first` | Morgan |
| `team.owner_signature` | Morgan Riley, Owner & Head Coach |
| `team.lead_trainer` | Alex Chen |
| `team.trainer_2` | Jordan Patel |
| `team.trainer_3` | Casey Brooks |
| `team.nutritionist` | Sam Rivera |
| `team.front_desk` | Taylor Kim |

---

## Group 4: Offers (the rotation slots — change these without touching any template)

| Custom Value | Value |
|---|---|
| `offer.free_trial` | Free 7-Day All-Access Pass |
| `offer.free_trial_short` | Free 7-Day Pass |
| `offer.trial_conversion_discount` | 20% off your first month + waived $49 enrollment fee |
| `offer.first_pt_session` | Your first PT session — on us |
| `offer.referral_reward_referrer` | A free 1-on-1 PT session |
| `offer.referral_reward_referee` | $20 off your first month |
| `offer.winback_d30` | We miss you — first month back at 50% off |
| `offer.winback_d60` | Welcome back package: $39 first month + waived enrollment |
| `offer.winback_d90` | Last chance — $29 first month, this week only |
| `offer.nutrition_starter` | One-on-one nutrition consult, normally $50, free for members |
| `offer.upgrade_basic_to_premium` | Upgrade to Premium for $70/mo more — gets you 2 PT sessions + nutrition |
| `offer.spring_launch` | Spring Reset: 30-day challenge + meal plan + 2 PT sessions, $99 |

When the studio runs a new campaign, the *only* place that updates is the `offer.*` value here. Every emails, and funnel pulling `{{custom_values.offer.spring_launch}}` updates instantly.

---

## Group 5: Brand Voice & Copy Snippets

| Custom Value | Value |
|---|---|
| `voice.greeting_warm` | Hey {{contact.first_name}} — |
| `voice.greeting_casual` | Hi {{contact.first_name}}! |
| `voice.greeting_morning` | Good morning, {{contact.first_name}} ☀️ |
| `voice.signature_owner` | — Morgan & the Sunrise team |
| `voice.signature_short` | — The Sunrise team |
| `voice.tagline_close` | Rise. Move. Glow. |
| `voice.cta_book` | Book your spot in 30 seconds 👉 {{custom_values.business.booking_url}} |
| `voice.cta_reply` | Reply to this text anytime — a real human reads it. |

The voice values are *prewritten brand-voice snippets*. Including them by reference means every welcome email, every Email, every reminder, every win-back uses the **same** tone — even when written by different people across different problems.

---

## Group 6: Class & Service Names

| Custom Value | Value |
|---|---|
| `class.hiit` | Sunrise HIIT |
| `class.yoga` | Sunrise Flow Yoga |
| `class.pilates` | Sunrise Pilates Reformer |
| `class.strength` | Sunrise Strength Lab |
| `class.recovery` | Sunrise Recovery & Mobility |
| `service.pt_drop_in` | 1-on-1 Personal Training |
| `service.pt_5pack` | PT 5-Pack |
| `service.pt_10pack` | PT 10-Pack |
| `service.nutrition_starter` | Nutrition Starter Consult |
| `service.nutrition_plan` | 4-Week Custom Nutrition Plan |

---

## Group 7: Pricing (DRY — pricing referenced in many templates)

| Custom Value | Value |
|---|---|
| `price.basic` | $79/month |
| `price.premium` | $149/month |
| `price.vip` | $249/month |
| `price.pt_single` | $85 |
| `price.pt_5pack` | $375 |
| `price.pt_10pack` | $700 |
| `price.nutrition_plan` | $199 |
| `price.enrollment_fee` | $49 |

When the studio runs a price increase, all three membership templates (welcome email, upsell offer, win-back) refresh by updating one value here.

---

## Group 8: Legal & Footer

| Custom Value | Value |
|---|---|
| `legal.footer` | Sunrise Wellness Studio · 123 Wellness Way, Springfield IL 62701 · (555) 723-1900 |
| `legal.unsubscribe` | Reply STOP to opt out of texts. Email: unsubscribe link below. |
| `legal.privacy_url` | https://sunrisewellness.com/privacy |
| `legal.terms_url` | https://sunrisewellness.com/terms |

---

## Total Count

**60 custom values across 8 groups.** A new operator hitting `{{` in any template editor sees the entire catalog and can compose on-brand copy without ever guessing a phone number, an offer, or a class name.

---

## Build Verification

After creating all custom values:

1. Open **Conversations** and start composing a test message.
2. Type `{{` — GHL should autocomplete with all your custom values.
3. Type `{{custom_values.offer.free_trial}}` — verify it resolves to "Free 7-Day All-Access Pass" in the preview.
4. Repeat for at least one value from each group.

---

---

## Extensions Added by Specific Problem Builds

Custom values introduced by individual problems. Add these to your sub-account when you build the relevant problem.

### From #02 Trial-to-Paid Conversion

| Custom Value | Value |
|---|---|
| `offer.conversion_funnel_url` | https://book.sunrisewellness.com/join (trial conversion checkout) |

### From #06 Upsell & Cross-Sell

| Custom Value | Value |
|---|---|
| `business.upgrade_url` | https://book.sunrisewellness.com/upgrade |

### From #07 Reviews & Reputation

| Custom Value | Value |
|---|---|
| `business.short_review_url` | https://sunrise.studio/review (vanity short URL for the smart review router) |

### From #10 Owner Reporting & Visibility

| Custom Value | Value |
|---|---|
| `reporting.last_weekly_digest_sent` | (Date, auto-updated each Monday by the digest workflow) |
| `reporting.daily_digest_enabled` | No (toggle Yes if owner wants 6 PM daily summaries) |
| `reporting.alerts_snoozed_until` | (Date, for temporary alert suppression) |
| `reporting.alerts_enabled_at` | (Date) |
| `api.dashboard_key` | (Auth header value for any custom external dashboard integrations) |

**Updated total custom value count with extensions: 68 values.**

---

## Related Foundation

- **[custom-fields.md](custom-fields.md)** — per-contact data (different mechanism, different purpose).
- **[products-and-pricing.md](products-and-pricing.md)** — actual GHL products for billing (these custom values mirror them in display copy).
