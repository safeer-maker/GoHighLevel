"""
02_custom_fields.py — Provision Sunrise Wellness custom contact fields

Idempotent: safe to re-run. Existing fields (matched by fieldKey) are skipped.

Endpoint: POST /locations/{locationId}/customFields  (GHL v2 API)

Field folders: GHL v2 API folder support varies. This script attempts to:
  1. Create each folder via POST /locations/{locationId}/customFields/folder
  2. Pass folder ID when creating each field
  3. Fall back to creating fields without folder if folder API is unavailable
     (fields land in 'Default' folder; user moves them in UI)
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, GHLAPIBlocked, client, logger

DATA_FILE = Path(__file__).parent / "data" / "custom_fields.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def fetch_existing_fields() -> list:
    try:
        data = client.get(f"/locations/{GHL_LOCATION_ID}/customFields")
        if isinstance(data, dict):
            return data.get("customFields", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.error(f"Failed to fetch existing custom fields: {e}")
        return []


def fetch_existing_folders() -> list:
    """Try to fetch existing folders. GHL doesn't always expose a folder list endpoint —
    we infer folders from existing fields' folderName property."""
    try:
        # Try direct folder endpoint first
        data = client.get(f"/locations/{GHL_LOCATION_ID}/customFields/folder")
        if isinstance(data, dict):
            return data.get("folders", []) or data.get("data", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError:
        # Fallback: infer from existing fields
        return []


def create_folder(folder_name: str) -> str:
    """Create a folder; return its ID. Returns empty string if API blocked."""
    try:
        payload = {"name": folder_name, "model": "contact"}
        resp = client.post(f"/locations/{GHL_LOCATION_ID}/customFields/folder", json=payload)
        folder_id = resp.get("id") or resp.get("_id", "")
        if folder_id:
            logger.info(f"  Folder created: {folder_name}  ({folder_id})")
        return folder_id
    except GHLAPIBlocked:
        logger.warning(f"  Folder API blocked — fields will land in Default folder. Manually move to '{folder_name}' in UI.")
        return ""
    except GHLAPIError as e:
        logger.warning(f"  Folder create failed for '{folder_name}' ({e}) — fields will land in Default.")
        return ""


def find_folder_id(folders: list, name: str) -> str:
    for f in folders:
        if f.get("name") == name:
            return f.get("id") or f.get("_id", "")
    return ""


def main():
    print("=" * 70)
    print("02 — Custom Fields Provisioning")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    spec_folders = spec["folders"]
    total_fields = sum(len(f["fields"]) for f in spec_folders)
    logger.info(f"Loaded {len(spec_folders)} folders containing {total_fields} fields from spec.")

    existing_fields = fetch_existing_fields()
    existing_by_key = {f.get("fieldKey"): f for f in existing_fields if f.get("fieldKey")}
    # GHL sometimes prefixes fieldKey with 'contact.' — index both
    for f in existing_fields:
        fk = f.get("fieldKey", "")
        if fk.startswith("contact."):
            existing_by_key[fk[len("contact."):]] = f
    logger.info(f"Fetched {len(existing_by_key)} existing custom fields from GHL.")

    existing_folders = fetch_existing_folders()
    folder_id_map = {f.get("name"): (f.get("id") or f.get("_id", "")) for f in existing_folders}
    if existing_folders:
        logger.info(f"Fetched {len(existing_folders)} existing folders.")

    created, skipped, failed = 0, 0, 0
    failed_items, folder_warnings = [], []

    for folder in spec_folders:
        folder_name = folder["name"]
        logger.info(f"--- Folder: {folder_name} ---")

        # Ensure folder exists
        folder_id = folder_id_map.get(folder_name)
        if not folder_id:
            folder_id = create_folder(folder_name)
            if folder_id:
                folder_id_map[folder_name] = folder_id

        for field_spec in folder["fields"]:
            key = field_spec["fieldKey"]
            if key in existing_by_key:
                logger.debug(f"  SKIP   {key}  (already exists)")
                skipped += 1
                continue

            payload = {
                "name": field_spec["name"],
                "dataType": field_spec["dataType"],
                "fieldKey": key,
                "model": "contact",
            }
            if "options" in field_spec:
                payload["options"] = field_spec["options"]
            if folder_id:
                payload["parentId"] = folder_id

            try:
                client.post(f"/locations/{GHL_LOCATION_ID}/customFields", json=payload)
                logger.info(f"  CREATE {key}  ({field_spec['dataType']})")
                created += 1
            except GHLAPIError as e:
                logger.error(f"  FAILED {key}  ({e})")
                failed += 1
                failed_items.append((f"{folder_name}/{key}", str(e)))

    print()
    print("=" * 70)
    logger.info(f"DONE: {created} created, {skipped} skipped, {failed} failed (of {total_fields} total)")

    # Folder verification reminder
    fields_without_folders = sum(1 for f in spec_folders if not folder_id_map.get(f["name"]))
    if fields_without_folders:
        print()
        logger.warning(f"⚠️  {fields_without_folders} folder(s) could not be created via API.")
        logger.warning("    Open Settings > Custom Fields in GHL and verify folder organization.")

    if failed:
        print()
        logger.error("FAILED FIELDS — create these manually in Settings > Custom Fields:")
        for name, err in failed_items:
            print(f"  - {name}  ({err})")

    print("=" * 70)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
