# #10 — Email Templates: Owner Reporting

> Production-ready owner-facing emails. The Monday Weekly Digest is the centerpiece. Daily summary and alert templates included.

---

## Email 1 — Weekly Digest (the centerpiece)

**Template name:** `10 — Weekly Digest`

**Send timing:** Every Monday at 7:00 AM owner-local time (Workflow `10a — Weekly Digest`)

**Recipient:** `{{custom_values.business.owner_email}}`

**From:**
- Name: `Sunrise Dashboard`
- Email: `dashboard@sunrisewellness.com`

**Reply-to:** `{{custom_values.business.owner_email}}` (replies route back to owner — used for self-notes)

**Subject:**
> Sunrise — Week of {{week_label}} (7 numbers + this week's actions)

**Preview text:**
> Net new this week: {{net_new_delta}}. {{at_risk_count}} at-risk members need a call. MRR: ${{mrr}}.

---

### Email Body

**Header band:** Sunrise gradient. Logo centered. Small white text "WEEKLY DIGEST · {{week_label}}"

---

#### Section 1: The Owner Greeting

> Good morning, Morgan ☀️
>
> Here's last week at a glance. **Two things need your eyes this week** (skip to the action items below if you're short on time).

---

#### Section 2: The 7 Headline Numbers (HTML table)

Render as a 4-column × 2-row HTML table (wraps to 2-col on mobile).

| # | Metric | This Week | Delta |
|---|---|---|---|
| 1 | New Leads | **{{new_leads_week}}** | {{trend_arrow_1}} {{new_leads_week_delta}} vs last week |
| 2 | Active Trials | **{{active_trials}}** | {{trials_needing_attention_count}} need attention |
| 3 | Trial → Paid (30d) | **{{trial_to_paid_rate_30d}}%** | {{trend_arrow_3}} {{trial_to_paid_rate_delta}}pp |
| 4 | Active Members | **{{active_members}}** | {{trend_arrow_4}} {{active_members_delta}} this week |
| 5 | Current MRR | **${{mrr}}** | {{trend_arrow_5}} ${{mrr_delta}} this week |
| 6 | At-Risk Members | **{{at_risk_count}}** | {{at_risk_critical_count}} critical |
| 7 | Net New This Month | **{{net_new_month_signed}}** | {{net_new_month_trend}} |

**Trend arrow rendering:**
- ↑ green for positive
- ↓ red for negative
- → gray for flat
- HTML uses inline SVG or Unicode arrows with colored `<span>` wrappers

**Color coding per cell:**
- Green background tint if metric is healthy
- Amber if watching
- Red if critical

---

#### Section 3: This Week's Actions (the most-important section)

**H2:**
> 🎯 This week's action items

**Numbered list — each item is specific, named, time-bounded:**

1. **{{action_1}}**
   *Example: "Call Diane K. — she's been flagged at-risk for 14 days. Last visit Oct 23."*

2. **{{action_2}}**
   *Example: "Lin H.'s trial expires Wednesday. Personal text to set up day-6 conversion call."*

3. **{{action_3}}**
   *Example: "Sarah M. brought in 2 referrals this quarter — she's eligible for top-referrer recognition. Drop a thank-you note next time she's in."*

Generation logic: workflow webhook returns a ranked list of "owner actions" pulled from:
- At-risk members not contacted in 7+ days
- Trials at day 5+ with no conversion offer
- Quarterly top referrers not yet recognized
- High-value cancellations needing a personal call (within 48h of cancel)
- Failed-payment members still unrecovered after 48h

If fewer than 3 actions exist this week, fill with positive-action items:
- "Reactivation: James K. just came back this week. Personal hello next time he's in."
- "5-star review from Marcus T. — DM him a thanks."

---

#### Section 4: Funnel Health Snapshot (compact)

**H2:**
> 📊 Funnel snapshot

**Mini-table (renders as a horizontal bar visualization in HTML, or text table fallback):**

| Funnel | Stage with biggest drop-off | Conversion this week |
|---|---|---|
| Membership Sales | {{sales_drop_stage}} | {{sales_overall_pct}}% |
| Onboarding | {{onboarding_drop_stage}} | {{onboarding_overall_pct}}% |
| Retention | {{retention_drop_stage}} | {{retention_save_pct}}% saves |

**Insight line (auto-generated, varies week to week):**

> 💡 *{{weekly_insight}}*
>
> Example: "Conversion offer step is dropping 18% — worth A/B testing the day-7 SMS subject."

---

#### Section 5: Source Attribution Snapshot

**H2:**
> 📍 Where leads came from (last 30d)

**Horizontal bar list (text in monospace for inbox compatibility):**

```
Instagram    ████████████ 38 leads · 42% conversion → $1,290 LTV/lead
Google       ████████ 24 leads · 51% conversion → $1,565 LTV/lead
Referral     ██████ 17 leads · 67% conversion → $2,060 LTV/lead
Facebook     █████ 14 leads · 35% conversion → $1,076 LTV/lead
Walk-in      ███ 9 leads · 58% conversion → $1,780 LTV/lead
Web Search   ██ 6 leads · 30% conversion → $922 LTV/lead
```

**Insight line:**

> 💡 *{{attribution_insight}}*
>
> Example: "Referral converts at 67% vs Instagram's 42%. Doubling referral attention pays back faster than scaling IG spend."

---

#### Section 6: Wins of the Week (positive momentum section)

**H2:**
> ☀️ Wins this week

**Bulleted list — auto-pulled:**

- 🎉 **{{reactivations_week}}** reactivations: {{reactivation_names}}
- 💛 **{{conversions_week}}** new paid members: {{new_member_names}}
- ⭐ **{{reviews_week}}** new 5-star reviews
- 🤝 **{{referrals_week}}** referral conversions: {{referrer_names}} brought in {{referee_names}}
- 🛟 **{{saves_week}}** at-risk members saved (back to risk-healthy)

If a category has 0, skip the line entirely (don't render empty bullets).

---

#### Section 7: Footer / Quick Links

> ---
>
> **Quick links:**
> - 📊 Full dashboard: [open in GHL](https://app.gohighlevel.com/dashboards/sunrise-owner-headlines)
> - 🚨 At-risk member list: [open](https://app.gohighlevel.com/smartlists/all-at-risk-members)
> - 🆕 Active trials needing attention: [open](https://app.gohighlevel.com/smartlists/active-trials-needing-attention)
> - ⏸ Snooze alerts for a few days: [edit](https://app.gohighlevel.com/custom-values/reporting-alerts-snoozed-until)
>
> ---
>
> *This digest is generated by your Sunrise GHL system every Monday at 7AM. Reply to this email if any of these numbers look wrong — replies go to you (Morgan).*
>
> ☀️ Have a great week.

---

**Footer band:** Cream background.

- Studio: {{custom_values.business.address_line}}
- Footer disclaimer: {{custom_values.legal.footer}}

---

### Mobile-First Notes

- The 7-number table MUST render cleanly on mobile (Gmail iOS, Outlook iOS, Apple Mail).
- Use HTML table with explicit pixel widths and `style="display:block"` on mobile to wrap to 2-column.
- Test in [Litmus](https://litmus.com) before launch — mobile email rendering is notoriously fragile.
- The "Wins this week" emoji bullets render universally; safe choice.

---

### Personalization Fallbacks

- `{{new_leads_week}}` → fallback: 0 (with note "no leads this week — investigate")
- `{{trial_to_paid_rate_30d}}` → fallback: "N/A — insufficient data"
- `{{action_1}}/2/3` → fallback: "No urgent actions this week — focus on retention check-ins"
- `{{weekly_insight}}` → fallback: "Numbers stable week-over-week. Hold the course."

---

---

## Email 2 — Daily Activity Summary (optional, opt-in)

**Template name:** `10 — Daily Activity Summary`

**Send timing:** Daily at 6:00 PM owner-local (Workflow `10b — Daily Lead Summary`, gated by toggle)

**Recipient:** Owner

**Subject:**
> Sunrise today: {{leads_today}} leads · {{trials_today}} trials · {{saves_today}} saves

**Preview text:**
> Quick end-of-day. Numbers from today.

---

### Email Body

**Greeting:**

> Hey Morgan —
>
> Today at a glance:

**Compact table:**

| Activity | Today | Yesterday |
|---|---|---|
| New leads in | {{leads_today}} | {{leads_yesterday}} |
| Trials booked | {{trials_booked_today}} | {{trials_booked_yesterday}} |
| Conversions to paid | {{conversions_today}} | {{conversions_yesterday}} |
| At-risk members saved | {{saves_today}} | {{saves_yesterday}} |
| Cancellations | {{cancellations_today}} | {{cancellations_yesterday}} |
| Failed payments | {{failed_payments_today}} | {{failed_payments_yesterday}} |

---

**If any urgent items:**

> ⚠️ **Needs your eyes:**
> - {{urgent_item_1}}
> - {{urgent_item_2}}

(Skip this section entirely if no urgent items.)

---

**Closing:**

> Good day or rough day — either way, that's it for today.
>
> — Your Sunrise Dashboard
>
> *Don't want this daily? [Turn off here](https://app.gohighlevel.com/custom-values/reporting-daily-digest-enabled). The Monday digest will still come.*

---

### Design notes
- This email should be MAX 12 lines of body text. The owner is reading it on her phone at 6 PM in the parking lot. Brevity wins.
- No header image, no fancy graphics — just the table and the closing.
- Subject line is the most important part — many owners read the subject and don't open unless something stands out.

---

---

## Email 3 — Critical Alert: Trial Day-6 No Booking

**Template name:** `10 — Alert · Trial Day-6 No Booking`

**Send timing:** Triggered (Workflow `10c`, Trigger A)

**Recipient:** Owner

**Subject:**
> [ALERT] Trial day-6, no booking yet: {{contact.first_name}} {{contact.last_name}}

---

### Email Body

> Morgan —
>
> **{{contact.first_name}} {{contact.last_name}}** is on day 6 of their trial and hasn't booked their first class.
>
> Their trial expires {{trial_expiry_date}} ({{days_until_expiry}} days).
>
> | Detail | Value |
> |---|---|
> | Source | {{contact.lead_source}} |
> | Goal | {{contact.fitness_goal_primary}} |
> | Preferred time | {{contact.preferred_workout_time}} |
> | Phone | {{contact.phone}} |
> | Email | {{contact.email}} |
>
> **Suggested action:** Personal text or call. Day-7 conversion window closes fast.
>
> Open contact: [{{contact.first_name}}'s profile](https://app.gohighlevel.com/contact/{{contact.id}})
>
> — Your Sunrise Dashboard

---

## Email 4 — Critical Alert: VIP At-Risk

**Template name:** `10 — Alert · VIP At-Risk`

**Send timing:** Triggered (Workflow `10c`, Trigger B)

**Subject:**
> [ALERT] VIP member at-risk: {{contact.first_name}} {{contact.last_name}}

---

### Email Body

> Morgan — this one needs you specifically.
>
> **{{contact.first_name}} {{contact.last_name}}** ({{contact.membership_tier}}, ${{contact.monthly_rate}}/mo) was just flagged **{{contact.at_risk_flag}}**.
>
> | Signal | Value |
> |---|---|
> | Engagement score | {{contact.engagement_score}} (was {{contact.engagement_score_30d_ago}} 30d ago) |
> | Visits last 30d | {{contact.visits_last_30_days}} (was {{contact.visits_last_30_days_prior}} prior 30d) |
> | Last visit | {{contact.last_visit_date}} |
> | Trainer | {{contact.assigned_trainer}} |
> | Member since | {{contact.membership_start_date}} ({{contact.days_as_member}} days) |
> | LTV to date | ${{contact.ltv_to_date}} |
>
> **Why this matters:** VIP at-risk = highest-value save in the studio. A personal call from you within 48 hours saves these at ~60%.
>
> **Suggested approach:** Don't pitch. Just check in. "Hey {{contact.first_name}} — was thinking about you. Coffee or session this week, on me."
>
> Open contact: [{{contact.first_name}}'s profile](https://app.gohighlevel.com/contact/{{contact.id}})
>
> — Your Sunrise Dashboard

---

## Email 5 — Critical Alert: 3+ At-Risk This Week (Pattern Alert)

**Template name:** `10 — Alert · At-Risk Pattern`

**Send timing:** Weekly check (Workflow `10c`, Trigger C)

**Subject:**
> [ALERT] {{count}} at-risk members flagged this week — pattern check

---

### Email Body

> Morgan —
>
> **{{count}} members were newly flagged at-risk in the last 7 days.** That's above normal baseline (usually 1–2/week).
>
> This week's flagged members:
> {{at_risk_names_list}}
>
> **Possible patterns to check:**
> - Did a class schedule change recently?
> - Trainer turnover?
> - New class times that don't work for the morning crowd?
> - Seasonal slump (holidays, summer travel)?
>
> The pattern isn't always actionable — sometimes it's just a slow week. But 4+ flagged in 7 days usually means *something* in the experience shifted.
>
> Open the At-Risk smart list: [view](https://app.gohighlevel.com/smartlists/all-at-risk-members)
>
> — Your Sunrise Dashboard

---

## Email 6 — Critical Alert: Failed Payment Not Recovered

**Template name:** `10 — Alert · Failed Payment Unrecovered`

**Send timing:** Triggered 24h after `payment-failed-pending` (Workflow `10c`, Trigger D)

**Subject:**
> [ALERT] Failed payment unrecovered after 24h: {{contact.first_name}} {{contact.last_name}}

---

### Email Body

> Morgan —
>
> **{{contact.first_name}} {{contact.last_name}}**'s payment failed 24 hours ago and hasn't been recovered yet.
>
> | Detail | Value |
> |---|---|
> | Tier | {{contact.membership_tier}} (${{contact.monthly_rate}}/mo) |
> | Payment failed at | {{contact.payment_failed_at}} |
> | Member since | {{contact.membership_start_date}} ({{contact.days_as_member}} days) |
> | LTV to date | ${{contact.ltv_to_date}} |
> | Phone | {{contact.phone}} |
>
> Automated SMS + email both sent. Day-2 reminder fires today.
>
> **Suggested action:** Personal text or call. Most failed-payment members fix it within 48h if reminded — but a personal touch from you closes the rest.
>
> Open contact: [{{contact.first_name}}'s profile](https://app.gohighlevel.com/contact/{{contact.id}})
>
> — Your Sunrise Dashboard

---

## Email 7 — Critical Alert: High-Value Cancellation

**Template name:** `10 — Alert · High-Value Cancellation`

**Send timing:** Triggered on `member-cancelled` for VIP or `monthly_rate ≥ 200` (Workflow `10c`, Trigger E)

**Subject:**
> [ALERT] High-value cancellation: {{contact.first_name}} {{contact.last_name}} — reason: {{contact.cancel_reason}}

---

### Email Body

> Morgan —
>
> **{{contact.first_name}} {{contact.last_name}}** just cancelled. This is a high-value member — recommended you reach out personally before the win-back sequence takes over.
>
> | Detail | Value |
> |---|---|
> | Tier | {{contact.membership_tier}} (${{contact.monthly_rate}}/mo) |
> | LTV to date | ${{contact.ltv_to_date}} |
> | Member since | {{contact.membership_start_date}} ({{contact.days_as_member}} days) |
> | Cancel reason | **{{contact.cancel_reason}}** |
> | Cancel notes | "{{contact.cancel_notes}}" |
> | Phone | {{contact.phone}} |
>
> **Suggested action:** Phone call (not text) within 24 hours. Goal: understand the *real* reason and offer a paused-membership option if appropriate. Save rate on high-value voluntary cancels with same-day owner outreach: ~30%.
>
> Don't pitch. Listen. Save options:
> - Paused membership ($0/mo for up to 3 months)
> - Downgrade to Basic instead of cancel
> - One-month break with auto-resume
>
> Open contact: [{{contact.first_name}}'s profile](https://app.gohighlevel.com/contact/{{contact.id}})
>
> — Your Sunrise Dashboard

---

## Email-Building Notes

**Tone calibration (owner-facing):**
- Owner is operator, not customer. Drop warm-fuzzy. Be useful and brief.
- Numbers first, narrative second.
- Action items must be specific (named contact, specific suggestion) — never "follow up on at-risk members."
- Insight lines should reveal something the owner doesn't already know.

**Subject line conventions:**
- Weekly digest: starts with "Sunrise —" (brand recognizable in busy inbox)
- Daily summary: starts with "Sunrise today:"
- Alerts: starts with "[ALERT]" — filterable

**Reply handling:**
- Replies to dashboard emails route back to the owner's own address. Useful for self-notes ("remember to call Diane Wed") — Gmail filters can auto-route to a "self-notes" label.

**Deliverability:**
- All dashboard emails come from `dashboard@sunrisewellness.com` — a dedicated subdomain so transactional patterns don't pollute marketing-send reputation.
- Verify SPF/DKIM/DMARC for `sunrisewellness.com` and the `dashboard.` subdomain.
- Open rate baseline target: 95%+ for the weekly digest (it goes to one person). If it drops below 80%, the owner has stopped reading and the system is failing — investigate.

**What we deliberately don't include:**
- No "you're doing great!" filler — wastes owner attention
- No marketing copy or upsell of GHL features
- No corporate sign-off — the dashboard's voice is functional, not branded
- No banner ads or sponsor logos (it's an internal tool)
