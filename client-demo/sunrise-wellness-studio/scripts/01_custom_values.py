"""
01_custom_values.py — Provision Sunrise Wellness custom values

Idempotent: safe to re-run. Existing values are skipped.

Endpoint: POST /locations/{locationId}/customValues  (GHL v2 API)
Reference: https://highlevel.stoplight.io/docs/integrations/12d7d1d6e80c3-create-custom-value
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, GHLAPIBlocked, client, logger

DATA_FILE = Path(__file__).parent / "data" / "custom_values.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def fetch_existing() -> list:
    """Fetch all existing custom values for this location."""
    try:
        data = client.get(f"/locations/{GHL_LOCATION_ID}/customValues")
        # API may return either {customValues: [...]} or just [...]
        if isinstance(data, dict):
            return data.get("customValues", []) or data.get("custom_values", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIBlocked as e:
        logger.error(f"API blocked custom values list: {e}")
        return []


def main():
    print("=" * 70)
    print("01 — Custom Values Provisioning")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    values_to_create = spec["values"]
    logger.info(f"Loaded {len(values_to_create)} values from spec.")

    try:
        existing = fetch_existing()
    except GHLAPIError as e:
        logger.error(f"Failed to fetch existing custom values: {e}")
        sys.exit(1)

    existing_by_name = {v.get("name"): v for v in existing if v.get("name")}
    logger.info(f"Fetched {len(existing_by_name)} existing custom values from GHL.")

    created, skipped, failed = 0, 0, 0
    failed_items = []

    for spec_value in values_to_create:
        name = spec_value["name"]
        value = spec_value["value"]

        if name in existing_by_name:
            logger.debug(f"SKIP  {name}  (already exists)")
            skipped += 1
            continue

        try:
            payload = {"name": name, "value": value}
            client.post(f"/locations/{GHL_LOCATION_ID}/customValues", json=payload)
            logger.info(f"CREATE {name}  = '{value[:60]}{'...' if len(value) > 60 else ''}'")
            created += 1
        except GHLAPIBlocked as e:
            logger.error(f"FAILED {name}  (API blocked: {e.message})")
            failed += 1
            failed_items.append((name, str(e)))
        except GHLAPIError as e:
            logger.error(f"FAILED {name}  ({e})")
            failed += 1
            failed_items.append((name, str(e)))

    print()
    print("=" * 70)
    logger.info(f"DONE: {created} created, {skipped} skipped, {failed} failed (of {len(values_to_create)} total)")
    if failed:
        print()
        logger.error("FAILED ITEMS — create these manually in Settings > Custom Values:")
        for name, err in failed_items:
            print(f"  - {name}  ({err})")
    print("=" * 70)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
