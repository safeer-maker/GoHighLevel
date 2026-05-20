"""
99_verify_foundation.py — Verify the full Sunrise Wellness foundation

Reads every resource from GHL and compares against the JSON specs.
Produces a clear pass/warn/fail report.

Run this after 01-06 scripts. Re-run anytime to confirm nothing has drifted.

Exit codes:
  0  — all checks passed
  1  — some checks failed (missing resources)
  2  — checks passed with warnings (e.g., extra resources, manual items)
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, client, logger

DATA_DIR = Path(__file__).parent / "data"

# --- Status symbols ----------------------------------------------------------

PASS = "✅"
WARN = "⚠️ "
FAIL = "❌"


def load_json(name: str) -> dict:
    with open(DATA_DIR / name) as f:
        return json.load(f)


# --- Per-asset verification --------------------------------------------------

def verify_custom_values():
    spec = load_json("custom_values.json")
    target_names = {v["name"] for v in spec["values"]}

    try:
        data = client.get(f"/locations/{GHL_LOCATION_ID}/customValues")
        existing = data.get("customValues", []) if isinstance(data, dict) else (data or [])
        existing_names = {v.get("name") for v in existing if v.get("name")}
    except GHLAPIError as e:
        return FAIL, f"Custom Values: ERROR fetching ({e})", []

    missing = target_names - existing_names
    if not missing:
        return PASS, f"Custom Values: {len(target_names)}/{len(target_names)} present", []
    return FAIL, f"Custom Values: {len(target_names) - len(missing)}/{len(target_names)} present", sorted(missing)


def verify_custom_fields():
    spec = load_json("custom_fields.json")
    target_keys = set()
    folder_names = set()
    for folder in spec["folders"]:
        folder_names.add(folder["name"])
        for field in folder["fields"]:
            target_keys.add(field["fieldKey"])

    try:
        data = client.get(f"/locations/{GHL_LOCATION_ID}/customFields")
        existing = data.get("customFields", []) if isinstance(data, dict) else (data or [])
        existing_keys = set()
        for f in existing:
            fk = f.get("fieldKey", "")
            existing_keys.add(fk)
            # also index without 'contact.' prefix
            if fk.startswith("contact."):
                existing_keys.add(fk[len("contact."):])
    except GHLAPIError as e:
        return FAIL, f"Custom Fields: ERROR fetching ({e})", []

    missing = target_keys - existing_keys
    folder_count = len(folder_names)
    if not missing:
        return PASS, f"Custom Fields: {len(target_keys)}/{len(target_keys)} present ({folder_count} folders expected)", []
    return FAIL, f"Custom Fields: {len(target_keys) - len(missing)}/{len(target_keys)} present", sorted(missing)


def verify_tags():
    spec = load_json("tags.json")
    target_tags = set(spec["tags"])

    # Tags are only visible through contacts. We fetch the scaffold contact and check its tags.
    scaffold_email = spec["scaffold_contact"]["email"]
    try:
        resp = client.get("/contacts/", params={"locationId": GHL_LOCATION_ID, "query": scaffold_email, "limit": 1})
        contacts = resp.get("contacts", [])
        if not contacts:
            return FAIL, "Tags: scaffold contact not found — run 03_tags.py first", []
        scaffold_tags = set(contacts[0].get("tags", []))
    except GHLAPIError as e:
        return FAIL, f"Tags: ERROR fetching scaffold ({e})", []

    missing = target_tags - scaffold_tags
    if not missing:
        return PASS, f"Tags: {len(target_tags)}/{len(target_tags)} present", []
    return FAIL, f"Tags: {len(target_tags) - len(missing)}/{len(target_tags)} present on scaffold", sorted(missing)


def verify_pipelines():
    spec = load_json("pipelines.json")
    target = {p["name"]: {s["name"] for s in p["stages"]} for p in spec["pipelines"]}

    try:
        data = client.get("/opportunities/pipelines", params={"locationId": GHL_LOCATION_ID})
        existing = data.get("pipelines", []) if isinstance(data, dict) else (data or [])
    except GHLAPIError as e:
        return FAIL, f"Pipelines: ERROR fetching ({e})", []

    existing_by_name = {p.get("name"): p for p in existing if p.get("name")}
    pipelines_missing = []
    stages_missing_total = 0
    stages_total = 0
    pipelines_found = 0

    for name, target_stages in target.items():
        stages_total += len(target_stages)
        if name not in existing_by_name:
            pipelines_missing.append(name)
            continue
        pipelines_found += 1
        existing_stages = {s.get("name") for s in existing_by_name[name].get("stages", [])}
        missing_stages = target_stages - existing_stages
        if missing_stages:
            stages_missing_total += len(missing_stages)
            pipelines_missing.append(f"{name}: missing stages {sorted(missing_stages)}")

    stages_present = stages_total - stages_missing_total
    pipeline_label = f"{pipelines_found}/{len(target)} present, {stages_present}/{stages_total} stages"

    if not pipelines_missing:
        return PASS, f"Pipelines: {pipeline_label}", []
    return FAIL, f"Pipelines: {pipeline_label}", pipelines_missing


def verify_products():
    spec = load_json("products.json")
    target_names = {p["name"] for p in spec["products"]}

    try:
        data = client.get("/products/", params={"locationId": GHL_LOCATION_ID, "limit": 100})
        existing = data.get("products", []) if isinstance(data, dict) else (data or [])
        existing_names = {p.get("name") for p in existing if p.get("name")}
    except GHLAPIError as e:
        return FAIL, f"Products: ERROR fetching ({e})", []

    missing = target_names - existing_names
    if not missing:
        return PASS, f"Products: {len(target_names)}/{len(target_names)} present", []
    return FAIL, f"Products: {len(target_names) - len(missing)}/{len(target_names)} present", sorted(missing)


def verify_coupons():
    spec = load_json("products.json")
    target_codes = {c["code"] for c in spec["coupons"]}

    try:
        data = client.get("/payments/coupon/list", params={"altId": GHL_LOCATION_ID, "altType": "location", "limit": 100})
        existing = data.get("data", []) if isinstance(data, dict) else (data or [])
        existing_codes = {c.get("code") for c in existing if c.get("code")}
    except GHLAPIError:
        existing_codes = set()

    missing = target_codes - existing_codes
    if not missing:
        return PASS, f"Coupons: {len(target_codes)}/{len(target_codes)} present", []
    return WARN, f"Coupons: {len(target_codes) - len(missing)}/{len(target_codes)} present", sorted(missing)


def verify_calendars():
    spec = load_json("calendars.json")
    target_names = {c["name"] for c in spec["calendars"]}

    try:
        data = client.get("/calendars/", params={"locationId": GHL_LOCATION_ID})
        existing = data.get("calendars", []) if isinstance(data, dict) else (data or [])
        existing_names = {c.get("name") for c in existing if c.get("name")}
    except GHLAPIError as e:
        return FAIL, f"Calendars: ERROR fetching ({e})", []

    missing = target_names - existing_names
    if not missing:
        return PASS, f"Calendars: {len(target_names)}/{len(target_names)} present", []
    return WARN, f"Calendars: {len(target_names) - len(missing)}/{len(target_names)} present", sorted(missing)


# --- Main --------------------------------------------------------------------

CHECKS = [
    ("Custom Values", verify_custom_values),
    ("Custom Fields", verify_custom_fields),
    ("Tags", verify_tags),
    ("Pipelines", verify_pipelines),
    ("Products", verify_products),
    ("Coupons", verify_coupons),
    ("Calendars", verify_calendars),
]


def main():
    print("=" * 70)
    print("SUNRISE WELLNESS — FOUNDATION VERIFICATION REPORT")
    print("=" * 70)
    print_config_summary()
    print()

    results = []
    for label, fn in CHECKS:
        logger.info(f"Verifying {label}…")
        try:
            symbol, summary, details = fn()
        except Exception as e:
            symbol, summary, details = FAIL, f"{label}: UNEXPECTED ERROR ({e})", []
        results.append((symbol, summary, details))

    # ---- Report ----
    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    has_fail = False
    has_warn = False
    for symbol, summary, details in results:
        print(f"{symbol} {summary}")
        if symbol == FAIL:
            has_fail = True
        if symbol == WARN:
            has_warn = True
        if details:
            for item in details[:10]:
                print(f"      - {item}")
            if len(details) > 10:
                print(f"      … and {len(details) - 10} more")

    print()
    print("=" * 70)
    if has_fail:
        print("❌ FAILURES DETECTED — re-run the relevant 0N_*.py script to fix.")
        print("=" * 70)
        sys.exit(1)
    if has_warn:
        print("⚠️  WARNINGS — some items require manual UI creation (see above).")
        print("    Re-run this verification after manual fixes to confirm all green.")
        print("=" * 70)
        sys.exit(2)
    print("✅ ALL CHECKS PASSED — foundation is fully provisioned.")
    print("=" * 70)
    sys.exit(0)


if __name__ == "__main__":
    main()
