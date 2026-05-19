# Sunrise Wellness — Foundation Provisioning Scripts

Idempotent Python scripts that provision the Sunrise Wellness Studio foundation (custom fields, tags, custom values, pipelines, products, calendars) into your GoHighLevel sub-account.

**Status:** Phase 1 of 2. Phase 1 builds the foundation via API. Phase 2 (later) will add per-problem test scripts.

---

## What These Scripts Do

| Script | Provisions |
|---|---|
| `01_custom_values.py` | 72 custom values across 8 groups (business identity, hours, team, offers, voice, classes, pricing, legal) |
| `02_custom_fields.py` | 64 contact custom fields across 5 folders (Lead Info, Fitness Profile, Membership Info, Engagement & Activity, Communication Preferences) |
| `03_tags.py` | 117 tags applied via a single scaffold contact (GHL creates tags on first use) |
| `04_pipelines.py` | 3 pipelines (Membership Sales, Onboarding, Retention) with all stages |
| `05_products_and_coupons.py` | 10 products (Basic/Premium/VIP memberships, PT packages, nutrition, trial, seasonal) + 7 coupons |
| `06_calendars.py` | 9 calendars (Intro Consult, PT, Nutrition, Goal Review, 5 group class calendars) |
| `99_verify_foundation.py` | Reads everything back and asserts it matches the spec |

Source-of-truth data lives in `data/*.json` files. Edit the JSON to change *what* gets provisioned; the scripts are *how*.

---

## What These Scripts Do NOT Do

The GHL API doesn't expose everything. You'll do these in the UI:

- **Workflows** — build in UI following `../problems/*/assets/workflow.md`
- **Funnels and landing pages** — build in UI following `../problems/*/assets/funnel.md`
- **Email/SMS templates** — build in UI following `../problems/*/assets/emails.md` and `sms.md`
- **Forms** — build in UI following `../problems/*/assets/forms.md`
- **Smart Lists** — build in UI (spec in `../problems/10-owner-reporting-and-visibility/build.md`)

---

## Setup

### 1. Get your sandbox sub-account credentials

In GHL:

1. Create a fresh sandbox sub-account (Agency Dashboard > + Add Sub-Account)
2. Inside the sub-account, go to **Settings > Business Profile**
3. Scroll down to **API Key** — copy it
4. The **Location ID** is in the URL: `https://app.gohighlevel.com/location/{LOCATION_ID}/...`

If you don't see an API Key field, your sub-account doesn't have API access enabled. Contact your agency admin, or create a Private App via [marketplace.gohighlevel.com](https://marketplace.gohighlevel.com).

### 2. Create your `.env` file

```bash
cd client-demo/sunrise-wellness-studio/scripts
cp .env.example .env
```

Edit `.env` and paste in your `GHL_API_KEY` and `GHL_LOCATION_ID`.

### 3. Install dependencies

```bash
cd ../../..   # back to repo root
pip install -r scripts/requirements.txt
```

Or install directly:

```bash
pip install requests python-dotenv
```

### 4. Smoke test — verify credentials work

```bash
cd client-demo/sunrise-wellness-studio/scripts
python ghl_client.py
```

Expected output:

```
======================================================================
Sunrise Wellness Provisioning — Configuration
======================================================================
GHL Base URL:    https://services.leadconnectorhq.com
GHL API Version: 2021-07-28
Location ID:     abcd...wxyz
API Key:         pk_l...3xj9
Log Level:       INFO
Dry Run:         False
Rate Limit:      0.2s between calls
======================================================================
HH:MM:SS [INFO] Running smoke test against GHL API…
HH:MM:SS [INFO] Connection OK. Account has at least 0 contact(s) visible.
```

If you see `401 Unauthorized` or `403 Forbidden`, see [Troubleshooting](#troubleshooting) below.

---

## Running the Provisioning Scripts

All commands assume you are inside the `scripts/` directory:

```bash
cd client-demo/sunrise-wellness-studio/scripts
```

### First — Dry-Run Everything

Set `DRY_RUN=true` in your `.env` file. Then run scripts in order; they'll print what they *would* do without making any changes.

```bash
python 01_custom_values.py
python 02_custom_fields.py
python 03_tags.py
python 04_pipelines.py
python 05_products_and_coupons.py
python 06_calendars.py
```

Expected dry-run output for each: counts of what would be created. No errors.

### Then — Real Run

Set `DRY_RUN=false` in your `.env`. Re-run the scripts in the same order.

Each script is **idempotent** — safe to re-run. On a fresh sub-account, the first run creates everything. On subsequent runs, items that already exist are skipped.

Example real-run output:

```
HH:MM:SS [INFO] === 01_custom_values.py ===
HH:MM:SS [INFO] Fetched 0 existing custom values.
HH:MM:SS [INFO] Creating 'business.name' = 'Sunrise Wellness Studio'
HH:MM:SS [INFO] Creating 'business.short_name' = 'Sunrise'
... [66 more]
HH:MM:SS [INFO] Summary: 68 created, 0 updated, 0 skipped, 0 failed
```

### Finally — Verify

```bash
python 99_verify_foundation.py
```

Expected:

```
======================================================================
SUNRISE WELLNESS — FOUNDATION VERIFICATION REPORT
======================================================================
✅ Custom Values: 68/68 present
✅ Custom Fields: 61/61 present (5 folders verified)
✅ Tags: 82/82 present
✅ Pipelines: 3/3 present, 27/27 stages verified
✅ Products: 10/10 present
✅ Coupons: 7/7 present
✅ Calendars: 9/9 present
======================================================================
ALL CHECKS PASSED ✅
```

If any check fails (⚠️ or ❌), the script prints exactly what's missing and what to do.

---

## Troubleshooting

### `401 Unauthorized`

Your `GHL_API_KEY` is wrong or expired. Double-check:
- Copied from the right sub-account
- No leading/trailing whitespace in `.env`
- API key hasn't been regenerated (regenerating invalidates old keys)

### `403 Forbidden`

Your sub-account doesn't have API access enabled.
- **Easiest fix:** Ask your agency admin to enable API on this sub-account.
- **Alternative:** Create a Private App at `marketplace.gohighlevel.com` and use its OAuth token instead.

### `429 Rate Limited`

GHL is throttling you. The client auto-retries with backoff. If it persists:
- Bump `RATE_LIMIT_DELAY` in `.env` from `0.2` to `0.5` or `1.0`
- Re-run; the script is idempotent so no harm done

### `Pipelines / Coupons / Calendars: ⚠️ API Blocked`

Some GHL plans restrict create endpoints for these. The script will print exact UI instructions to create the blocked items manually. After creating them in UI, re-run `99_verify_foundation.py` to confirm.

### "Custom fields keep getting created in 'Default' folder, not the folders I want"

GHL API folder support varies by API version. If field folders don't materialize via API, the script will:
1. Still create all 61 fields (so they're usable)
2. Print a manual instruction: "Go to Settings > Custom Fields and drag fields into folders X, Y, Z."

---

## File Reference

```
scripts/
├── README.md                          ← you are here
├── .env.example                       ← template; copy to .env
├── .env                               ← (you create this; gitignored)
├── config.py                          ← env loader + validation
├── ghl_client.py                      ← HTTP wrapper (auth, retry, logging, dry-run)
├── 01_custom_values.py                ← provisioning scripts
├── 02_custom_fields.py
├── 03_tags.py
├── 04_pipelines.py
├── 05_products_and_coupons.py
├── 06_calendars.py
├── 99_verify_foundation.py
└── data/                              ← source-of-truth JSON
    ├── custom_values.json
    ├── custom_fields.json
    ├── tags.json
    ├── pipelines.json
    ├── products.json
    └── calendars.json
```

---

## Safety Notes

1. **Always run in a sandbox first.** Never run for the first time against a production sub-account with real members.
2. **`.env` is gitignored.** Your API key never lands in git.
3. **Scripts log redacted keys.** The API key is masked in all output (`pk_l...3xj9`).
4. **Dry-run is your friend.** When in doubt, set `DRY_RUN=true` and inspect output before mutating.
5. **Re-runs are safe.** Every script is idempotent. Re-running won't create duplicates.

---

## What's Next After Phase 1

Once `99_verify_foundation.py` is all green:

1. **Manual UI verification** (15 min) — log into the sub-account and visually confirm Settings > Custom Fields, Custom Values, Pipelines, Products, Calendars all look right.
2. **Start Phase 2** — workflows, funnels, emails. Build in UI following `../problems/*/build.md` files.
