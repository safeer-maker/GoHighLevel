# #01 — Form Specs

> Two forms used in lead capture: the main funnel form and the walk-in tablet form. Both feed the same Instant Response workflow.

---

## Form 1 — Lead Capture (Funnel)

**Form Name:** `Lead Capture — Free 7-Day Pass`

**Used on:** Funnel Page 2 (`02 — Claim`)

**Submit behavior:** Redirect to Thank-You Page (`03 — Welcome`)

### Fields

| # | Field Label | Placeholder | Type | Required | Maps to | Notes |
|---|---|---|---|---|---|---|
| 1 | First name | Sarah | Text (single line) | ✅ | `contact.first_name` | Max 50 chars |
| 2 | Last name | Chen | Text (single line) | ✅ | `contact.last_name` | Max 50 chars |
| 3 | Phone number | (555) 555-1234 | Phone | ✅ | `contact.phone` | E.164 format validated |
| 4 | Email | sarah@email.com | Email | ✅ | `contact.email` | Standard email validation |
| 5 | What's your main goal? | Pick the closest match | Dropdown | ✅ | `fitness_goal_primary` (custom field) | Options below |
| 6 | When do you prefer to work out? | Pick a time window | Dropdown | ❌ | `preferred_workout_time` (custom field) | Options below |
| 7 | (hidden) Lead source | — | Hidden text | — | `lead_source` (custom field) | Populated from URL param, defaults to "Web Search" |
| 8 | (hidden) Source detail | — | Hidden text | — | `lead_source_detail` (custom field) | UTM campaign / keyword |
| 9 | Consent | "I agree to receive texts and emails from Sunrise. Standard rates apply. Reply STOP to opt out." | Checkbox | ✅ | `sms_opt_in` = Yes AND `email_opt_in` = Yes when checked | Must be pre-unchecked (TCPA compliance) |

### Dropdown options

**Field 5 — Primary Goal:**

| Display | Stored value |
|---|---|
| Lose weight | Lose Weight |
| Build muscle / strength | Build Muscle |
| Improve overall fitness | Improve Fitness |
| Manage stress / feel better | Manage Stress |
| Recover from an injury | Recover from Injury |
| Train for a specific event | Train for Event |
| Just exploring / general wellness | General Wellness |

**Field 6 — Preferred Workout Time:**

| Display | Stored value |
|---|---|
| Early morning (5–8 AM) | Early Morning (5-8AM) |
| Morning (8–11 AM) | Morning (8-11AM) |
| Midday (11 AM – 2 PM) | Midday (11AM-2PM) |
| Afternoon (2–5 PM) | Afternoon (2-5PM) |
| Evening (5–8 PM) | Evening (5-8PM) |
| Late evening (8 PM+) | Late Evening (8PM+) |

### Validation rules

- **Phone:** Must be 10+ digits, country code optional (auto-prepend +1 for US).
- **Email:** Standard regex validation. Reject obviously fake (`asdf@asdf.com`, `test@test.com` is allowed for testing — flag for production).
- **First name + last name:** Reject if matches a stopword list (`asdf`, `test`, `xxx`, `none`).
- **Consent:** Must be checked or form rejects with: "We can't text you without your permission — please check the box."

### Error messages

| Field | Error |
|---|---|
| Phone (invalid format) | "Please enter a valid phone number we can text." |
| Email (invalid format) | "That email doesn't look right — double-check?" |
| Consent (unchecked) | "We can't text you without your permission — please check the box." |
| Network failure | "Something went wrong on our end. Please try again or text us at {{custom_values.business.sms_number}}." |

### Anti-spam

- **Honeypot field:** Add a hidden `website` field; bots fill it, humans don't. Reject any submission with a value in this field (silent — don't notify the bot).
- **Time-on-form check:** Reject submissions that complete in <3 seconds (bot indicator).
- **reCAPTCHA v3:** Optional. Add if spam volume becomes a problem; not required for launch.

---

## Form 2 — Walk-In Quick Capture (Tablet)

**Form Name:** `Lead Capture — Walk-In Tablet`

**Used on:** Walk-in funnel (`Sunrise — Walk-In Quick Capture`)

**Mounted on:** iPad at front desk, locked to the funnel URL.

**Submit behavior:** Redirect to a "You're in! Hand the tablet back to front desk." confirmation.

### Fields

Stripped-down — 4 visible fields. Speed matters at the desk.

| # | Field Label | Type | Required | Maps to |
|---|---|---|---|---|
| 1 | First name | Text | ✅ | `contact.first_name` |
| 2 | Phone number | Phone | ✅ | `contact.phone` |
| 3 | Email | Email | ✅ | `contact.email` |
| 4 | What brought you in today? | Dropdown | ✅ | `fitness_goal_primary` |
| 5 | (hidden) Lead source | Hidden | — | `lead_source` — DEFAULT VALUE: `Walk-in` |
| 6 | (hidden) Consent | Hidden checkbox pre-checked + verbal confirmation by front desk | — | `sms_opt_in` = Yes, `email_opt_in` = Yes |

Front desk verbally confirms with the walk-in: *"Cool if we text you a booking link?"* If they say no, front desk uses the studio's contact-create-without-form flow instead.

**Dropdown options for Field 4:** same as Form 1 Field 5.

---

## Form 3 — Referral Capture (Built in #08, referenced here)

Referred leads use a variant of Form 1 with one extra hidden field:

- `lead_source` = `Referral` (default)
- `referred_by_contact_id` = pre-populated from referral link URL parameter
- `referral_code_used` = pre-populated from URL parameter

Built in [../../08-referral-engine/build.md](../../08-referral-engine/build.md). Mentioned here so the form architecture stays consistent.

---

## Form Builder Settings (apply to both)

- **Show progress bar:** No (too short to need one)
- **Allow multiple submissions per contact:** No
- **Send notification on submission:** No (workflow handles notifications)
- **Pixel tracking:** Yes — fire Meta Pixel and Google Ads conversion events on successful submission. Setup outside scope of this file; configured in **Sites > Tracking Codes**.
- **Embed style:** Inline (not popup). Popups depress conversion 15–25% for this audience.

---

## Form Accessibility

- All inputs have proper `<label>` association (handled automatically by GHL but verify in preview).
- Color contrast: WCAG AA minimum. Coral CTA on cream background passes; verify with WebAIM checker.
- Keyboard navigation: tab order matches visual order; submit button reachable.
- Screen reader text: error messages announced via `aria-live`.
- Mobile keyboard: phone field triggers numeric keyboard, email field triggers email keyboard, name fields default to capitalized words.

---

## Conversion Tracking

Hook the form submission to:

| Platform | Event |
|---|---|
| Meta Pixel | `Lead` event with value $948 (projected LTV) |
| Google Ads | `Conversion` event, label `lead_capture`, value $948 |
| GHL native analytics | Automatic — visible in Funnel Analytics tab |

These conversion events let the studio see true cost-per-lead by channel — which feeds the [#10 Owner Reporting](../../10-owner-reporting-and-visibility/) ad-spend efficiency calculations.

---

## Build Verification

After creating both forms:

1. Submit Form 1 with test data — confirm all fields save to the right contact fields.
2. Submit Form 1 with a UTM URL — confirm hidden `lead_source` populates correctly.
3. Submit Form 2 — confirm `lead_source` defaults to "Walk-in" without UTM.
4. Submit Form 1 without consent — confirm form blocks with error message.
5. Open the contact detail in GHL — confirm all 6 visible field values stored correctly, plus the two hidden source fields.
6. Confirm the Instant Response workflow fires (check workflow execution history).
