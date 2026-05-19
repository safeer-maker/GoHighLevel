"""
04_pipelines.py — Provision Sunrise Wellness opportunity pipelines

Idempotent: existing pipelines (matched by name) are skipped. If a pipeline
exists but stages differ, this script reports the diff but does not modify
(safer; you decide whether to manually fix or recreate).

Pipeline CREATE endpoint: GHL v2 API support is inconsistent. This script
tries the v2 endpoint first; if blocked (403/404), it falls back to printing
manual UI instructions.

Endpoint attempted: POST /opportunities/pipelines
"""

import json
import sys
from pathlib import Path

from config import GHL_LOCATION_ID, print_config_summary
from ghl_client import GHLAPIError, GHLAPIBlocked, client, logger

DATA_FILE = Path(__file__).parent / "data" / "pipelines.json"


def load_spec() -> dict:
    with open(DATA_FILE) as f:
        return json.load(f)


def fetch_existing_pipelines() -> list:
    try:
        data = client.get("/opportunities/pipelines", params={"locationId": GHL_LOCATION_ID})
        if isinstance(data, dict):
            return data.get("pipelines", []) or []
        return data if isinstance(data, list) else []
    except GHLAPIError as e:
        logger.error(f"Failed to list pipelines: {e}")
        return []


def print_manual_instructions(pipeline_spec: dict):
    """When API blocks pipeline creation, print exact UI steps."""
    print()
    print(f"  📋 MANUAL: Create pipeline '{pipeline_spec['name']}' in GHL UI:")
    print(f"     1. Navigate to Opportunities > Pipelines > + Create Pipeline")
    print(f"     2. Name: {pipeline_spec['name']}")
    print(f"     3. Add stages in this exact order:")
    for stage in pipeline_spec["stages"]:
        print(f"        {stage['position']}. {stage['name']}")
    print()


def diff_stages(existing_stages: list, spec_stages: list) -> tuple:
    """Compare existing vs spec stages by name. Returns (missing, extra, matched)."""
    existing_names = {s.get("name") for s in existing_stages}
    spec_names = {s["name"] for s in spec_stages}
    missing = spec_names - existing_names  # in spec but not in GHL
    extra = existing_names - spec_names    # in GHL but not in spec
    matched = spec_names & existing_names
    return missing, extra, matched


def create_pipeline(pipeline_spec: dict) -> bool:
    """Attempt to create the pipeline via API. Returns True on success."""
    payload = {
        "name": pipeline_spec["name"],
        "locationId": GHL_LOCATION_ID,
        "showInFunnel": pipeline_spec.get("showInFunnel", True),
        "showInPieChart": pipeline_spec.get("showInPieChart", True),
        "stages": [
            {"name": s["name"], "position": s["position"] - 1}  # API often 0-indexed
            for s in pipeline_spec["stages"]
        ],
    }
    try:
        client.post("/opportunities/pipelines", json=payload)
        return True
    except GHLAPIBlocked as e:
        logger.warning(f"  Pipeline create API blocked: {e.message}")
        return False
    except GHLAPIError as e:
        logger.error(f"  Pipeline create failed: {e}")
        return False


def main():
    print("=" * 70)
    print("04 — Pipelines Provisioning")
    print("=" * 70)
    print_config_summary()
    print()

    spec = load_spec()
    target_pipelines = spec["pipelines"]
    logger.info(f"Loaded {len(target_pipelines)} pipelines from spec.")

    existing = fetch_existing_pipelines()
    existing_by_name = {p.get("name"): p for p in existing if p.get("name")}
    logger.info(f"Fetched {len(existing_by_name)} existing pipelines from GHL.")

    created, skipped, failed, manual_required = 0, 0, 0, 0
    stage_warnings = []

    for spec_p in target_pipelines:
        name = spec_p["name"]
        existing_p = existing_by_name.get(name)

        if existing_p:
            logger.info(f"SKIP  '{name}' (exists; checking stages…)")
            skipped += 1
            existing_stages = existing_p.get("stages", []) or []
            missing, extra, _ = diff_stages(existing_stages, spec_p["stages"])
            if missing:
                logger.warning(f"  ⚠️  Missing stages in '{name}': {sorted(missing)}")
                stage_warnings.append((name, "missing", sorted(missing)))
            if extra:
                logger.info(f"  ℹ️  Extra stages in '{name}' (not in spec, kept as-is): {sorted(extra)}")
            continue

        logger.info(f"CREATE attempting '{name}' ({len(spec_p['stages'])} stages)")
        if create_pipeline(spec_p):
            created += 1
            logger.info(f"  ✅ '{name}' created.")
        else:
            manual_required += 1
            print_manual_instructions(spec_p)

    print()
    print("=" * 70)
    logger.info(f"DONE: {created} created, {skipped} skipped, {manual_required} require manual UI creation.")

    if stage_warnings:
        print()
        logger.warning("⚠️  STAGE DIFFS — existing pipelines missing stages from spec:")
        for name, kind, stages in stage_warnings:
            print(f"  {name} ({kind}): {stages}")
        logger.warning("    Fix manually in GHL: Opportunities > Pipelines > [Pipeline] > Edit Stages")

    if manual_required:
        logger.warning(f"⚠️  {manual_required} pipeline(s) require manual UI creation. Follow instructions above.")
        sys.exit(2)  # exit code 2 = partial success, manual action needed

    print("=" * 70)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
