# #07 — Form Spec: Private Feedback (Low Score)

> The form embedded on Page 3 of the Smart Review Router funnel. Receives feedback from any member who rated their session 1, 2, or 3. The form's job is to capture honest detail and route it to Morgan privately — without putting it on Google.

---

## Form 1 — Private Feedback (Low Score)

**Form Name:** `Review — Private Feedback (Low Score)`

**Used on:** Smart Review Router Page 3 (`03 — Private Feedback`)

**Submit behavior:** Redirect to Page 4 (`04 — Private Thank You`)

---

### Fields

| # | Field Label | Placeholder | Type | Required | Maps to Custom Field | Notes |
|---|---|---|---|---|---|---|
| 1 | What could we have done better? | The more specific you can be, the more we can actually fix. | Multi-line text | ✅ | `private_feedback_text` | Min 10 chars, max 2000 chars |
| 2 | Is there anything specific we should fix today? | If something's broken / unsafe / urgent, let us know. | Multi-line text | ❌ | `private_feedback_urgent` | Optional, max 1000 chars |
| 3 | I'd be open to a quick phone call from Morgan to talk this through. | — | Checkbox | ❌ | Sets tag `feedback-phone-ok` if checked | Pre-unchecked |
| 4 | Best way to reach you | — | Radio (Email / Text / Phone) | ❌ | `preferred_channel` | Default: Email |
| 5 | (hidden) Star rating | — | Hidden number | — | `review_star_rating` | Populated from URL param via JS |
| 6 | (hidden) Contact ID | — | Hidden text | — | (matches contact to record) | From URL param |
| 7 | (hidden) Honeypot | — | Hidden text (anti-spam) | — | — | Bots fill it; humans don't. Reject submissions with values. |
| 8 | (hidden) Source | — | Hidden text | — | (logging) | Defaults to "Smart Review Router" |

---

### Field Validation Rules

| Field | Rule |
|---|---|
| Field 1 (what could we have done better) | Required. Min 10 chars (forces at least a meaningful sentence). Max 2000 chars. Strip whitespace before validation. |
| Field 2 (urgent) | Optional. If filled, must be at least 5 chars. Max 1000. |
| Field 3 (phone OK checkbox) | Optional. |
| Field 4 (preferred channel) | Optional. If "Phone" selected, the system uses contact's phone number on file. |
| Field 5 (hidden rating) | Must be 1, 2, or 3 (matches low-score routing). If received as 4 or 5, the form should reject and redirect to the high-score page — indicates URL tampering. |
| Field 6 (hidden contact_id) | Should be present; if missing, owner notification still fires but member is logged as "Unknown Contact" — owner manually matches later. |
| Field 7 (honeypot) | Must be empty. Reject silently if filled. |

---

### Error Messages

| Field | Error |
|---|---|
| Field 1 (empty) | "Please tell us what we could've done better — even one sentence helps." |
| Field 1 (too short, <10 chars) | "A bit more detail helps a lot — even one full sentence." |
| Field 1 (too long, >2000 chars) | "That's a lot — can you trim it to under 2000 characters? (Or just hit submit — we can talk through the rest by phone.)" |
| Field 2 (too long, >1000 chars) | "Just the most urgent stuff for this field — anything longer fits better in the main field above." |
| Hidden rating invalid | (No user-facing error — silently redirect to appropriate page) |
| Network failure | "Something went wrong sending this. Please try again, or text us directly at {{custom_values.business.sms_number}} — we want to hear from you." |

---

### Submit Behavior

**On valid submit:**

1. POST form data to GHL.
2. Update contact fields:
   - `private_feedback_text` = Field 1 value
   - `private_feedback_urgent` = Field 2 value (if present)
   - `review_star_rating` = Field 5 value
   - `review_submitted_date` = today
   - `feedback_submitted_date` = today
   - `preferred_channel` = Field 4 value (if present)
3. Apply tags:
   - `feedback-received-private` (always)
   - `feedback-phone-ok` (if Field 3 checked)
   - `do-not-ask-reviews` (180-day cooldown)
   - `risk-watching` (surfaces to retention monitoring)
4. Send internal notification to `{{custom_values.business.owner_email}}` with HIGH PRIORITY flag. Subject: `URGENT: {{contact.first_name}} {{contact.last_name}} left a {{rating}}-star private feedback`. Body: full feedback text, urgent issue if any, phone-OK status, contact info, contact link.
5. Create task assigned to Owner: `Follow up with {{contact.first_name}} {{contact.last_name}} — private feedback`. Due: 48 hours.
6. Trigger Workflow 07c (low-score handler) for any additional processing.
7. Redirect to Page 4 (private thank-you).

**On submit failure:**

- Display the network-failure error message above.
- Log the attempt to `failed_submissions_log` (a backend table) so the owner can manually retrieve the feedback if needed.
- The member's tag and field changes do NOT apply (failed submission = no state change).

---

### Anti-Spam

- **Honeypot field (Field 7):** A hidden text field named `website`. Bots fill all fields; humans skip hidden ones. Reject silently if filled.
- **Time-on-form check:** Reject submissions that complete in <3 seconds (bot indicator).
- **Same-contact rate limit:** Same `contact_id` can submit only once per 24 hours (prevents accidental double-submits and prevents griefing).
- **reCAPTCHA v3:** Optional. Add if spam becomes a problem; not required for launch.

---

### Form Builder Settings

| Setting | Value |
|---|---|
| Show progress bar | No (one-page form) |
| Allow multiple submissions per contact | Yes, but rate-limited (see anti-spam above) |
| Send notification on submission | Yes — HIGH PRIORITY to owner |
| Pixel tracking | Yes — fire a custom "PrivateFeedbackReceived" event in GHL analytics for reporting |
| Embed style | Inline (not popup) |
| Auto-save partial responses | No (privacy — don't auto-save anything sensitive) |

---

### Accessibility

- All inputs have proper `<label>` association
- Color contrast WCAG AA minimum (cream background + deep-slate labels passes)
- Keyboard navigation: tab order matches visual order; submit button reachable via Tab + Enter
- Screen reader text: error messages announced via `aria-live`
- Mobile keyboard: text fields default to standard keyboard (not numeric)
- Multi-line text fields: minimum 4 visible rows on mobile, 6 on desktop

---

## Form-Field Wording Philosophy

Every word in this form is calibrated:

- **"What could we have done better?"** — frames the question as constructive, not as a complaint vent. Members write more useful feedback when prompted this way.
- **"The more specific you can be, the more we can actually fix"** — explicitly invites detail, gives a *reason* (we can fix it), short and earnest.
- **"Is there anything specific we should fix today?"** — separate field for urgent items (broken equipment, safety issue) — so the owner can triage immediately without reading the whole long feedback first.
- **"I'd be open to a quick phone call from Morgan"** — pre-unchecked checkbox respects autonomy. The "quick" and "from Morgan" specifics make it feel less daunting than "we'll call you back."
- **"Send to Morgan"** as submit button — names the recipient, makes the submission feel personal not bureaucratic.

---

## What Happens After Submission

The form's downstream is handled by Workflow 07c (defined in [workflow.md](workflow.md)):

1. **Within 1 minute:** Owner gets HIGH PRIORITY email with full feedback details.
2. **Within 1 minute:** Owner sees task in their GHL task list, due in 48hr.
3. **Within 1 hour:** If `feedback_phone_ok` ≠ Yes AND `do-not-email` not set, member gets the personal-from-Morgan Email asking to talk it through (template `07 — Private Feedback Owner Email` from []()).
4. **Within 48 hours:** Owner has personally replied via email or called the member.
5. **Tag persistence:** `do-not-ask-reviews` stays for 180 days. `risk-watching` stays until the retention scoring workflow moves it. `feedback-received-private` persists for owner reference.

---

## Owner Operating Procedure (when a low-score feedback arrives)

This isn't part of the form spec per se, but the form is useless if the owner doesn't act on it. Recommended owner workflow:

| Within | Action |
|---|---|
| 1 hour | Read the full feedback. Decide if it's urgent (safety, broken equipment) or relational (something the member experienced). |
| 4 hours | If urgent: address the operational issue first (fix the equipment, talk to the staff, post a sign). |
| 24 hours | Reply personally — email if member said Email, text if Text, call if Phone. Use the template from [emails.md](emails.md) as a starting point but personalize. |
| 48 hours | If member responded, continue the conversation. If member didn't respond, send one more soft follow-up — then leave them alone. |
| 7 days | Mark the task complete. Note in CRM what was done. Tag `feedback-owner-resolved` if appropriate. |

The form succeeds when the member who left 1-3 stars *doesn't cancel and doesn't write a public review* — both metrics tracked in [#10 Owner Reporting](../../10-owner-reporting-and-visibility/).

---

## Build Verification

After creating the form:

1. Submit the form with valid test data. Confirm all fields save to the contact correctly.
2. Submit with empty required field. Confirm validation blocks submission with the right error.
3. Submit from the live funnel (with rating=2 URL param). Confirm:
   - Form receives the rating
   - Owner notification fires with correct subject and body
   - All tags apply
   - Member is redirected to Page 4 thank-you
4. Submit with invalid rating (e.g., manually set rating=5 via URL). Confirm the form rejects or redirects appropriately.
5. Submit twice within 1 hour for same contact. Confirm second submission is rate-limited (no duplicate owner alert).
6. Submit with honeypot field filled (simulate a bot). Confirm silent rejection.
