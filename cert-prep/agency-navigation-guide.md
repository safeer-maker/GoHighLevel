# GHL Agency Navigation Quick Reference
## Part B Exam Cheat Sheet — Where to Find Everything

> Print this or keep it open during practice drills. The goal is to NOT need it by exam day.

---

## The Golden Rule

**Top-left corner tells you where you are:**
- Shows your agency name → you are in **Agency view**
- Shows a client name → you are in **Sub-Account view**

**To switch:** Click the name top-left → picker appears → select where to go.

---

## Agency View — Left Sidebar Map

| What You Want | Where to Click |
|---|---|
| List of all sub-accounts | **Accounts** (or Sub-Accounts) |
| Create a new sub-account | Accounts → **+ New Sub-Account** (top-right) |
| Create a snapshot | **Snapshots** → + New Snapshot |
| Load snapshot into a sub-account | Snapshots → find snapshot → **⋮ menu → Push to Account** |
| Agency company info / timezone | **Settings** (gear) → Company |
| Your agency staff (employees) | Settings → **Team** |
| Agency integrations | Settings → **Integrations** |
| API keys | Settings → **API Keys** |
| Your GHL subscription billing | Settings → **Billing** |
| Pause / edit a sub-account | Accounts → find sub-account → **⋮ menu** |

---

## Sub-Account View — Left Sidebar Map

| What You Want | Where to Click |
|---|---|
| **Business profile** (name, address, hours) | Settings (gear) → **Business Info** |
| **Custom values** (global variables like `{{business.name}}`) | Settings → **Custom Values** |
| **Sub-account team / users** | Settings → **Team** |
| **Integrations** (Zoom, Google, Stripe) | Settings → **Integrations** |
| **Custom fields** (contact data fields) | Settings → **Custom Fields** |
| **Tags** management | Settings → **Tags** |
| **Contacts / CRM** | **Contacts** in left nav |
| **Smart Lists** | Contacts → **Smart Lists** tab |
| **Conversations inbox** | **Conversations** in left nav |
| **Templates** (SMS and Email) | **Marketing** → Templates |
| **Campaigns** | Marketing → **Campaigns** |
| **Trigger Links** | Marketing → **Trigger Links** |
| **Calendars** | **Calendars** in left nav |
| **Calendar connections** (Zoom/Google Meet) | Calendars → select calendar → **Edit** → **Connections** tab |
| **Workflows** | **Automation** → Workflows |
| **Funnels** | **Sites** → Funnels |
| **Websites** | Sites → **Websites** |
| **Forms** | Sites → **Forms** |
| **Surveys** | Sites → **Surveys** |
| **Pipelines** | **Opportunities** → Pipelines (or Pipeline Settings) |
| **Opportunities** (deal cards) | Opportunities |
| **Products** | **Payments** → Products |
| **Invoices** | Payments → Invoices |
| **Coupons** | Payments → **Coupons** |
| **Subscriptions** | Payments → **Subscriptions** |
| **Reputation / Reviews** | **Reputation** in left nav |
| **Community** | **Memberships** → Communities |
| **Reporting** | **Reporting** in left nav |

---

## Zoom / Google Meet Calendar Integration — Step by Step

This is the most commonly failed Part B task. Do it in under 5 minutes:

1. Go to **Calendars** in the sub-account left nav
2. Find the calendar → click **Edit** (pencil icon)
3. Click the **Connections** tab (or Integrations tab — label varies by GHL version)
4. Click **+ Add Integration** or find the Zoom / Google Meet option
5. Click **Connect** → authenticate with your Zoom (or Google) account
6. Set **Meeting Location** to: Zoom (or Google Meet)
7. Click **Save**
8. Test: open the calendar booking link → book a test appointment
9. Verify: check the confirmation email — it must contain the meeting link

**If you don't see a Connections tab:**
- Some GHL versions have this under Settings → Integrations (sub-account level) → then link it to the calendar
- The path varies slightly by GHL version but the end result is the same: Zoom/Meet link in booking confirmation

---

## Workflow — Publish Checklist

The #3 Part B failure: building a workflow but not publishing it.

1. Open **Automation → Workflows** in the sub-account
2. Click into your workflow
3. Look for the toggle in the top-right area: **"Draft" vs "Published"**
4. Click the toggle to set it to **Published**
5. Confirm: the toggle shows green / "Published" — not just "Saved"

A workflow that is SAVED but not PUBLISHED will NOT fire. Always verify the Published state before the proctor checks.

---

## Snapshot — Quick Steps

**Create (< 2 min):**
Agency view → Snapshots → + New Snapshot → select source sub-account → name it → Save

**Load (< 2 min):**
Agency view → Snapshots → find snapshot → ⋮ menu → Push to Account → select target → Add/Merge → Load → verify in sub-account

---

## Part B Task Sequence (Recommended Order)

1. **Business profile + custom values** (sub-account) — 5 min
2. **Add contact + tag** (sub-account → Contacts → + New) — 2 min
3. **Pipeline + opportunity** (sub-account → Opportunities) — 5 min
4. **Calendar + Zoom/Meet** (sub-account → Calendars → Edit → Connections) — 7 min
5. **Workflow** (sub-account → Automation → Workflows → Build → Publish) — 8 min
6. **Snapshot** (switch to Agency → Snapshots → Create) — 3 min

Total target: **< 30 minutes** for exam readiness. Under 25 to pass confidently.

---

## Common Navigation Mistakes

| Mistake | How to Catch It |
|---|---|
| In Agency Settings instead of Sub-Account Settings | Top-left shows agency name (you're in wrong level) |
| Workflow saved but not published | Check the toggle: must say "Published" not "Draft" |
| Calendar created but Zoom not linked | Re-check: book a test appointment, see if meeting link is in confirmation |
| Snapshot created but not verified it loaded | Always enter the target sub-account and check one asset (e.g. Workflows) |
| Created team member in Agency Settings instead of Sub-Account | Agency team = your staff; sub-account team = client's staff |
