"""
06_calendars.py — Provision Sunrise Wellness calendars

Idempotent: existing calendars (matched by name) are skipped.

Endpoint: POST /calendars/                (GHL v2 API)

Calendar type support varies:
  - 'round_robin'    — usually API-creatable
  - 'class_booking'  — sometimes blocked
  - 'event'          — usually API-creatable
  - 'service'        — usually API-creatable

This script attempts each via API; falls back to clear manual UI instructions
for blocked types.
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, GHLAPIBlocked, client, logger

DATA_FILE = Path(__file__).parent / "data" / "calendars.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def fetch_location_users() -> list:
    """Fetch users in this location to get IDs for team member assignment."""
    try:
        data = client.get("/users/", params={"locationId": GHL_LOCATION_ID})
        if isinstance(data, dict):
            return data.get("users", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.warning(f"Could not fetch users: {e}")
        return []


def fetch_existing_calendars() -> list:
    try:
        data = client.get("/calendars/", params={"locationId": GHL_LOCATION_ID})
        if isinstance(data, dict):
            return data.get("calendars", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.error(f"Failed to list calendars: {e}")
        return []


def create_calendar(cal_spec: dict, default_user_id: str = "") -> tuple:
    """Attempt to create the calendar via API. Returns (calendar_dict, status)."""
    team_members = []
    if default_user_id:
        team_members = [{"userId": default_user_id, "priority": 0}]

    payload = {
        "locationId": GHL_LOCATION_ID,
        "name": cal_spec["name"],
        "description": cal_spec.get("description", ""),
        "calendarType": cal_spec.get("calendarType", "round_robin"),
        "slotDuration": cal_spec.get("slotDuration", 30),
        "slotDurationUnit": cal_spec.get("slotDurationUnit", "mins"),
        "slotInterval": cal_spec.get("slotInterval", 30),
        "slotIntervalUnit": cal_spec.get("slotIntervalUnit", "mins"),
        "appoinmentPerSlot": cal_spec.get("appoinmentPerSlot", 1),
        "teamMembers": team_members,
    }
    try:
        resp = client.post("/calendars/", json=payload)
        calendar = resp.get("calendar", resp)
        return calendar, "created"
    except GHLAPIBlocked as e:
        return {}, f"blocked: {e.message}"
    except GHLAPIError as e:
        return {}, f"failed: {e}"


def print_manual_instructions(cal_spec: dict):
    print()
    print(f"  📋 MANUAL: Create calendar '{cal_spec['name']}' in GHL UI:")
    print(f"     1. Calendars > + Create Calendar > {cal_spec.get('calendarType', 'round_robin')}")
    print(f"     2. Name: {cal_spec['name']}")
    print(f"     3. Description: {cal_spec.get('description', '')}")
    print(f"     4. Duration: {cal_spec.get('slotDuration', 30)} {cal_spec.get('slotDurationUnit', 'mins')}")
    print(f"     5. Per-slot capacity: {cal_spec.get('appoinmentPerSlot', 1)}")
    print(f"     6. Set availability per the schedule in the spec")
    print(f"     7. Assign team members (Alex, Jordan, Casey for PT; Sam for nutrition)")
    print()


def main():
    print("=" * 70)
    print("06 — Calendars Provisioning")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    target_calendars = spec["calendars"]
    logger.info(f"Loaded {len(target_calendars)} calendars from spec.")

    users = fetch_location_users()
    default_user_id = users[0].get("id", "") if users else ""
    if default_user_id:
        logger.info(f"Using user '{users[0].get('name', default_user_id)}' as placeholder team member.")
    else:
        logger.warning("No users found in location — calendars may fail (team member required by API).")

    existing = fetch_existing_calendars()
    existing_by_name = {c.get("name"): c for c in existing if c.get("name")}
    logger.info(f"Fetched {len(existing_by_name)} existing calendars from GHL.")

    created, skipped, failed, manual = 0, 0, 0, 0
    manual_items = []

    for cal_spec in target_calendars:
        name = cal_spec["name"]
        if name in existing_by_name:
            logger.debug(f"  SKIP   {name}  (exists)")
            skipped += 1
            continue

        logger.info(f"  CREATE {name}  ({cal_spec.get('calendarType', 'round_robin')})")
        cal, status = create_calendar(cal_spec, default_user_id=default_user_id)
        if status == "created":
            created += 1
            logger.info(f"    ✅ Created (you still need to assign team members in UI)")
        elif status.startswith("blocked"):
            manual += 1
            manual_items.append(cal_spec)
            logger.warning(f"    ⚠️  {status}")
        else:
            failed += 1
            logger.error(f"    ❌ {status}")

    print()
    print("=" * 70)
    logger.info(f"DONE: {created} created, {skipped} skipped, {failed} failed, {manual} require manual UI.")

    if created > 0:
        print()
        logger.warning("⚠️  REMINDER: API-created calendars have no team members assigned.")
        logger.warning("    Go to each calendar in the UI and assign trainers/staff.")

    if manual_items:
        print()
        logger.warning(f"⚠️  {len(manual_items)} CALENDAR(S) REQUIRE MANUAL CREATION:")
        for cs in manual_items:
            print_manual_instructions(cs)

    print("=" * 70)
    exit_code = 0
    if failed > 0:
        exit_code = 1
    elif manual > 0:
        exit_code = 2  # partial success, manual action needed
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
