# #08 — Form Specs: Referral Capture

> One form used in the referral landing funnel. Mirrors the #01 Lead Capture form with three extra hidden fields for attribution.

---

## Form 1 — Referral Capture

**Form Name:** `Referral Capture`

**Used on:** Referral funnel Page 2 (`02 — Claim`)

**Submit behavior:** Redirect to Thank-You Page (`03 — Welcome`)

**Downstream workflow:** Triggers the **same** `01 — Instant Response — Lead Capture` workflow (already configured in [#01](../../01-lead-capture-and-instant-response/build.md)). Add this form to the workflow's trigger filter as part of the #08 build.

---

### Visible Fields

| # | Field Label | Placeholder | Type | Required | Maps to | Notes |
|---|---|---|---|---|---|---|
| 1 | First name | Sarah | Text (single line) | ✅ | `contact.first_name` | Max 50 chars |
| 2 | Last name | Chen | Text (single line) | ✅ | `contact.last_name` | Max 50 chars |
| 3 | Phone number | (555) 555-1234 | Phone | ✅ | `contact.phone` | E.164 format validated |
| 4 | Email | sarah@email.com | Email | ✅ | `contact.email` | Standard email validation |
| 5 | What's your main goal? | Pick the closest match | Dropdown | ✅ | `fitness_goal_primary` | Same options as #01 form |
| 6 | Consent | "I agree to receive texts and emails from Sunrise. Standard rates apply. Reply STOP to opt out." | Checkbox | ✅ | `sms_opt_in` = Yes AND `email_opt_in` = Yes | Must be pre-unchecked (TCPA) |

### Hidden Fields (the attribution wiring)

| # | Field Key | Default Value | URL Param | Notes |
|---|---|---|---|---|
| 7 | `lead_source` | `Referral` | n/a | Always `Referral` for this form |
| 8 | `referred_by_contact_id` | (empty) | `ref_id` | Reads from URL — the referrer's GHL contact ID |
| 9 | `referral_code_used` | (empty) | `ref_code` | Reads from URL — e.g., `SARAH-42` |
| 10 | `lead_source_detail` | (empty) | `ref_name` | Reads from URL — referrer's first name, for owner readability in lead detail |

---

### Dropdown options (Field 5) — same as #01

| Display | Stored value |
|---|---|
| Lose weight | Lose Weight |
| Build muscle / strength | Build Muscle |
| Improve overall fitness | Improve Fitness |
| Manage stress / feel better | Manage Stress |
| Recover from an injury | Recover from Injury |
| Train for a specific event | Train for Event |
| Just exploring / general wellness | General Wellness |

(Field 6 — preferred workout time — is **omitted from the referral form** to keep it shorter than the main lead form. Referred leads have higher commitment signal, so we sacrifice one data field for speed.)

---

### Validation rules — same as #01

- **Phone:** Must be 10+ digits, country code optional (auto-prepend +1 for US).
- **Email:** Standard regex validation.
- **First name + last name:** Reject stopwords (`asdf`, `test`, `xxx`, `none`).
- **Consent:** Required.

### Error messages — same as #01

| Field | Error |
|---|---|
| Phone (invalid) | "Please enter a valid phone number we can text." |
| Email (invalid) | "That email doesn't look right — double-check?" |
| Consent (unchecked) | "We can't text you without your permission — please check the box." |
| Network failure | "Something went wrong on our end. Please try again or text us at {{custom_values.business.sms_number}}." |

---

### URL Parameter Reading — GHL Hidden Field Configuration

For each hidden field in the GHL form builder:

1. Drag a **Hidden Text** field into the form.
2. Set the **Field Key** to match the column above (`lead_source`, `referred_by_contact_id`, etc.).
3. In the field's settings, find **"Pre-fill from URL parameter"** (sometimes labeled "Default value source").
4. Set the URL parameter name to match the column above (`ref_id`, `ref_code`, `ref_name`).
5. Set the literal default value where applicable (e.g., `lead_source` default = `Referral`).

If the GHL form builder doesn't expose URL-param pre-fill natively, embed this JavaScript on the funnel page **above** the form:

```html
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const fieldMap = {
      'ref_id': 'referred_by_contact_id',
      'ref_code': 'referral_code_used',
      'ref_name': 'lead_source_detail'
    };
    Object.entries(fieldMap).forEach(([urlParam, fieldKey]) => {
      const value = params.get(urlParam);
      if (value) {
        const input = document.querySelector(`input[name="${fieldKey}"]`);
        if (input) input.value = value;
      }
    });
  });
</script>
```

---

### Anti-spam

- **Honeypot field:** Hidden `website` field; reject any submission with a value here.
- **Time-on-form check:** Reject submissions completing in < 3 seconds (bot indicator).
- **Referrer integrity check:** If `referred_by_contact_id` is present but does NOT match an existing contact in GHL, log to an "invalid referral attempts" smart list and notify owner (someone might be spoofing referrals to game the reward).

---

## Form 2 — (Not built — single form handles all referral capture)

The referral landing funnel uses only the `Referral Capture` form. If referrals come from non-link sources (e.g., front-desk says "Sarah sent me" verbally), front-desk uses the standard #01 walk-in form and manually sets the `referred_by_contact_id` and `referral_code_used` fields in the contact's detail view post-creation. The #08 conversion workflow fires correctly from there.

---

## Form Builder Settings

- **Show progress bar:** No
- **Allow multiple submissions per contact:** No (prevents a referrer from "re-submitting" themself)
- **Send notification on submission:** No (the #01 Instant Response Workflow handles notifications)
- **Pixel tracking:** Yes — Meta Pixel `Lead` event with value $948 (LTV projection)
- **Embed style:** Inline (matches #01)

---

## Conversion Tracking

Hook the form submission to:

| Platform | Event | Notes |
|---|---|---|
| Meta Pixel | `Lead` event with value $948 | Same as #01 |
| Google Ads | `Conversion` label `lead_capture_referral`, value $948 | Distinct label so referral conversions show separately in Google Ads |
| GHL native analytics | Automatic — visible in Funnel Analytics |

---

## Form Accessibility — same as #01

- All inputs have proper `<label>` association (verify in preview).
- Color contrast: WCAG AA minimum.
- Keyboard navigation: tab order matches visual order.
- Mobile keyboard: phone field triggers numeric keyboard, email triggers email keyboard.

---

## Build Verification

After creating the form:

1. Submit the form with full URL params (`?ref_name=TEST&ref_id=xyz&ref_code=TEST-99`). Open the contact in GHL.
   - Confirm all 4 visible fields stored.
   - Confirm all 4 hidden fields populated correctly.
2. Submit the form WITHOUT URL params (raw funnel URL).
   - Confirm `lead_source` defaults to `Referral`.
   - Confirm `referred_by_contact_id`, `referral_code_used`, `lead_source_detail` are empty.
   - Confirm the contact is still created (the form should not require referrer attribution to submit).
3. Submit with consent unchecked → confirm form blocks.
4. Confirm the `01 — Instant Response — Lead Capture` workflow fires (check workflow execution history).
5. If the contact has `referred_by_contact_id` populated AND later gets `trial-converted` tag → confirm `08b — Referral Conversion Credit` workflow fires.
