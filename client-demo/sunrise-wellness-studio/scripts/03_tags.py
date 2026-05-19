"""
03_tags.py — Scaffold the Sunrise Wellness tag taxonomy

GHL doesn't have a dedicated "create tag" endpoint. Tags are created implicitly
on first application to a contact. This script:

  1. Creates (or finds) a single internal "scaffold" contact
  2. Applies every tag from the spec to that scaffold contact
  3. Tags become part of the location's taxonomy and visible in Settings > Tags

The scaffold contact remains in the system — safe to keep (it's tagged
distinctly so it never matches marketing workflows). If you want it gone,
delete it manually after this script runs.

Idempotent: re-runs find the existing scaffold and skip already-applied tags.
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, client, logger

DATA_FILE = Path(__file__).parent / "data" / "tags.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def find_or_create_scaffold(scaffold: dict) -> str:
    """Find existing scaffold contact by email, or create new. Returns contact ID."""
    email = scaffold["email"]
    try:
        # Search by email
        resp = client.get(
            "/contacts/search/duplicate",
            params={"locationId": GHL_LOCATION_ID, "email": email},
        )
        existing = resp.get("contact") if isinstance(resp, dict) else None
        if existing and existing.get("id"):
            logger.info(f"Found existing scaffold contact: {existing['id']}")
            return existing["id"]
    except GHLAPIError as e:
        # 404 means not found - that's fine
        if e.status != 404:
            logger.debug(f"Search returned {e.status}, proceeding to create.")

    # Create new
    payload = {
        "locationId": GHL_LOCATION_ID,
        "firstName": scaffold["firstName"],
        "lastName": scaffold["lastName"],
        "email": email,
        "phone": scaffold["phone"],
        "tags": ["scaffold-internal", "do-not-market", "do-not-sms", "do-not-email"],
    }
    try:
        resp = client.post("/contacts/", json=payload)
        contact = resp.get("contact", resp)
        contact_id = contact.get("id") or contact.get("_id")
        if not contact_id:
            logger.error(f"Created contact but no ID in response: {resp}")
            sys.exit(1)
        logger.info(f"Created scaffold contact: {contact_id}")
        return contact_id
    except GHLAPIError as e:
        # If duplicate email error, try searching again with broader endpoint
        if e.status in (400, 409):
            logger.info("Contact already exists. Attempting alternative lookup...")
            resp = client.get(
                "/contacts/",
                params={"locationId": GHL_LOCATION_ID, "query": email, "limit": 1},
            )
            contacts = resp.get("contacts", [])
            if contacts:
                return contacts[0]["id"]
        logger.error(f"Failed to create or find scaffold contact: {e}")
        sys.exit(1)


def get_contact_tags(contact_id: str) -> set:
    """Fetch the current tag list for the scaffold contact."""
    try:
        resp = client.get(f"/contacts/{contact_id}")
        contact = resp.get("contact", resp)
        tags = contact.get("tags", []) or []
        return set(tags)
    except GHLAPIError as e:
        logger.warning(f"Could not fetch existing tags: {e}")
        return set()


def apply_tags(contact_id: str, tags: list) -> bool:
    """Apply a batch of tags to the contact. Returns True on success."""
    if not tags:
        return True
    try:
        client.post(f"/contacts/{contact_id}/tags", json={"tags": tags})
        return True
    except GHLAPIError as e:
        logger.error(f"Failed to apply tags batch: {e}")
        return False


def main():
    print("=" * 70)
    print("03 — Tag Taxonomy Scaffolding")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    target_tags = spec["tags"]
    scaffold = spec["scaffold_contact"]
    logger.info(f"Loaded {len(target_tags)} tags from spec.")

    scaffold_id = find_or_create_scaffold(scaffold)
    existing_tags = get_contact_tags(scaffold_id)
    logger.info(f"Scaffold contact has {len(existing_tags)} tag(s) already applied.")

    missing = [t for t in target_tags if t not in existing_tags]
    logger.info(f"{len(missing)} tag(s) to apply ({len(target_tags) - len(missing)} already present).")

    if not missing:
        print()
        print("=" * 70)
        logger.info("DONE: 0 created, all tags already present.")
        print("=" * 70)
        return

    # Apply in batches of 20 to avoid payload size issues
    BATCH = 20
    created_count = 0
    failed_batches = 0
    for i in range(0, len(missing), BATCH):
        batch = missing[i:i + BATCH]
        if apply_tags(scaffold_id, batch):
            created_count += len(batch)
            logger.info(f"  Applied batch of {len(batch)}  ({i + len(batch)}/{len(missing)})")
        else:
            failed_batches += 1
            logger.error(f"  Batch starting at index {i} failed.")

    print()
    print("=" * 70)
    logger.info(f"DONE: {created_count} tags applied (of {len(missing)} attempted).")
    if failed_batches:
        logger.warning(f"⚠️  {failed_batches} batch(es) failed — re-run this script to retry.")
    print(f"Scaffold contact ID: {scaffold_id}")
    print("(Safe to keep this contact; it has do-not-market tags so won't get messaged.)")
    print("=" * 70)


if __name__ == "__main__":
    main()
