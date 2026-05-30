# #01 — Form Specs — Email-Only Version

> Two forms used in lead capture: the main funnel form and the walk-in tablet form. Both feed the same Instant Response workflow. This version assumes no GHL phone number is connected, so **email is the required communication channel**.

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
| 3 | Email | sarah@email.com | Email | ✅ | `contact.email` | Primary communication channel |
| 4 | What's your main goal? | Pick the closest match | Dropdown | ✅ | `fitness_goal_primary` | Used for segmentation and email personalization |
| 5 | When do you prefer to work out? | Pick a time window | Dropdown | ❌ | `preferred_workout_time` | Helps recommend class times |
| 6 | (hidden) Lead source | — | Hidden text | — | `lead_source` | Populated from URL param, defaults to `Web Search` |
| 7 | (hidden) Source detail | — | Hidden text | — | `lead_source_detail` | UTM campaign / keyword |
| 8 | Consent | "I agree to receive emails from Sunrise Wellness Studio. I can unsubscribe anytime." | Checkbox | ✅ | `email_opt_in` = Yes | Must be unchecked by default |

### Dropdown options

**Field 4 — Primary Goal:**

| Display | Stored value |
|---|---|
| Lose weight | Lose Weight |
| Build muscle / strength | Build Muscle |
| Improve overall fitness | Improve Fitness |
| Manage stress / feel better | Manage Stress |
| Recover from an injury | Recover from Injury |
| Train for a specific event | Train for Event |
| Just exploring / general wellness | General Wellness |

**Field 5 — Preferred Workout Time:**

| Display | Stored value |
|---|---|
| Early morning (5–8 AM) | Early Morning (5-8AM) |
| Morning (8–11 AM) | Morning (8-11AM) |
| Midday (11 AM – 2 PM) | Midday (11AM-2PM) |
| Afternoon (2–5 PM) | Afternoon (2-5PM) |
| Evening (5–8 PM) | Evening (5-8PM) |
| Late evening (8 PM+) | Late Evening (8PM+) |

### Validation rules

- **Email:** Standard email validation. Reject obviously fake entries in production.
- **First name + last name:** Reject if matches a stopword list (`asdf`, `test`, `xxx`, `none`).
- **Consent:** Must be checked or the form rejects with: "Please confirm we can email you your trial details."

### Error messages

| Field | Error |
|---|---|
| Email invalid | "That email doesn't look right — double-check?" |
| Consent unchecked | "Please confirm we can email you your trial details." |
| Network failure | "Something went wrong on our end. Please try again or email us at {{custom_values.business.email}}." |

### Anti-spam

- **Honeypot field:** Add a hidden `website` field; bots fill it, humans do not. Reject any submission with a value in this field.
- **Time-on-form check:** Reject submissions completed in less than 3 seconds.
- **reCAPTCHA v3:** Optional. Add only if spam volume becomes a problem.

---

## Form 2 — Walk-In Quick Capture (Tablet)

**Form Name:** `Lead Capture — Walk-In Tablet`

**Used on:** Walk-in funnel (`Sunrise — Walk-In Quick Capture`)

**Mounted on:** iPad at front desk, locked to the funnel URL.

**Submit behavior:** Redirect to a "You're in! Hand the tablet back to front desk." confirmation.

### Fields

Stripped-down form. Speed matters at the desk.

| # | Field Label | Type | Required | Maps to |
|---|---|---|---|---|
| 1 | First name | Text | ✅ | `contact.first_name` |
| 2 | Email | Email | ✅ | `contact.email` |
| 3 | What brought you in today? | Dropdown | ✅ | `fitness_goal_primary` |
| 4 | (hidden) Lead source | Hidden | — | `lead_source` = `Walk-in` |
| 5 | (hidden) Consent | Hidden checkbox / front-desk confirmation | — | `email_opt_in` = Yes |

Front desk verbally confirms: *"Cool if we email you the booking link and trial details?"*

If they say no, the contact should be created manually without automation enrollment.

---

## Form 3 — Referral Capture — Phase 2 Reference

Referral capture is part of the future Phase 2 referral engine. It is not required for the active demo.

When Phase 2 is built, the referral form can reuse the same email-only structure with two hidden fields:

- `lead_source` = `Referral`
- `referred_by_contact_id` = pre-populated from referral link URL parameter

For the active demo, mention referrals only as future roadmap logic in `PHASE-2-ROADMAP.md`.

---

## Form Builder Settings

- **Show progress bar:** No.
- **Allow multiple submissions per contact:** No.
- **Send notification on submission:** No. Workflow handles notifications.
- **Pixel tracking:** Yes — fire Meta Pixel and Google Ads conversion events on successful submission.
- **Embed style:** Inline, not popup.

---

## Form Accessibility

- All inputs have proper `<label>` association.
- Color contrast meets WCAG AA minimum.
- Keyboard navigation follows visual order.
- Submit button is reachable by keyboard.
- Error messages are announced via `aria-live`.
- Mobile keyboard: email field triggers email keyboard, name fields default to capitalized words.

---

## Conversion Tracking

Hook the form submission to:

| Platform | Event |
|---|---|
| Meta Pixel | `Lead` event with projected LTV value |
| Google Ads | `Conversion` event, label `lead_capture` |
| GHL native analytics | Automatic in Funnel Analytics |

These conversion events let the studio see true cost-per-lead by channel, which feeds Section 10 owner reporting.

---

## Build Verification

After creating both forms:

1. Submit Form 1 with test data and confirm all fields save correctly.
2. Submit Form 1 with a UTM URL and confirm hidden `lead_source` populates correctly.
3. Submit Form 2 and confirm `lead_source` defaults to `Walk-in`.
4. Submit Form 1 without consent and confirm the form blocks submission.
5. Open the contact detail in GHL and confirm visible/hidden field values.
6. Confirm the Instant Response workflow fires.
7. Confirm the contact receives an email, not SMS.
