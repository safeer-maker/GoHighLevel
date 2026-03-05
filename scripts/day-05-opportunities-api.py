"""
Day 5 API Lab: Opportunities & Pipelines via GHL API
=====================================================
Manage pipelines, create/move/track opportunities.
"""

import requests
import json
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION


def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }


# --- 1. List All Pipelines ---

def list_pipelines():
    """List all pipelines in the sub-account."""
    url = f"{GHL_BASE_URL}/opportunities/pipelines"
    params = {"locationId": GHL_LOCATION_ID}

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        pipelines = response.json().get("pipelines", [])
        for p in pipelines:
            print(f"\nPipeline: {p.get('name')} (ID: {p.get('id')})")
            stages = p.get("stages", [])
            for s in stages:
                print(f"  Stage: {s.get('name')} (ID: {s.get('id')})")
        return pipelines
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 2. Create an Opportunity ---

def create_opportunity(pipeline_id, stage_id, contact_id, name, value=0, status="open"):
    """
    Create a new opportunity in a pipeline.

    Args:
        pipeline_id: Pipeline ID
        stage_id: Stage ID within the pipeline
        contact_id: Associated contact ID
        name: Opportunity/deal name
        value: Monetary value in cents (e.g., 5000 = $50.00) or dollars depending on API version
        status: open, won, lost, abandoned
    """
    url = f"{GHL_BASE_URL}/opportunities/"

    payload = {
        "pipelineId": pipeline_id,
        "locationId": GHL_LOCATION_ID,
        "pipelineStageId": stage_id,
        "contactId": contact_id,
        "name": name,
        "monetaryValue": value,
        "status": status,
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        opp = response.json().get("opportunity", response.json())
        print(f"Created opportunity: {opp.get('id')} - {name} (${value})")
        return opp
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 3. Search Opportunities ---

def search_opportunities(pipeline_id=None, stage_id=None, status=None, query=None, limit=20):
    """
    Search and filter opportunities.

    Args:
        pipeline_id: Filter by pipeline
        stage_id: Filter by stage
        status: Filter by status (open, won, lost, abandoned)
        query: Search by name
        limit: Max results
    """
    url = f"{GHL_BASE_URL}/opportunities/search"

    params = {
        "location_id": GHL_LOCATION_ID,
        "limit": limit,
    }
    if pipeline_id:
        params["pipeline_id"] = pipeline_id
    if stage_id:
        params["pipeline_stage_id"] = stage_id
    if status:
        params["status"] = status
    if query:
        params["q"] = query

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        opps = data.get("opportunities", [])
        print(f"Found {len(opps)} opportunities:")
        total_value = 0
        for opp in opps:
            value = opp.get("monetaryValue", 0)
            total_value += value
            print(f"  {opp.get('name')}: ${value} [{opp.get('status')}]")
        print(f"\nTotal pipeline value: ${total_value}")
        return opps
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 4. Update Opportunity (Move Stage, Change Status) ---

def update_opportunity(opportunity_id, stage_id=None, status=None, value=None, name=None):
    """
    Update an opportunity - move stage, change status, update value.

    Args:
        opportunity_id: The opportunity ID
        stage_id: New stage ID (to move to a different stage)
        status: New status (open, won, lost, abandoned)
        value: New monetary value
        name: New opportunity name
    """
    url = f"{GHL_BASE_URL}/opportunities/{opportunity_id}"

    payload = {}
    if stage_id:
        payload["pipelineStageId"] = stage_id
    if status:
        payload["status"] = status
    if value is not None:
        payload["monetaryValue"] = value
    if name:
        payload["name"] = name

    response = requests.put(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Updated opportunity {opportunity_id}")
        if stage_id:
            print(f"  Moved to stage: {stage_id}")
        if status:
            print(f"  Status: {status}")
        if value is not None:
            print(f"  Value: ${value}")
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 5. Delete an Opportunity ---

def delete_opportunity(opportunity_id):
    """Delete an opportunity."""
    url = f"{GHL_BASE_URL}/opportunities/{opportunity_id}"

    response = requests.delete(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Deleted opportunity {opportunity_id}")
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


# --- 6. Pipeline Value Report ---

def pipeline_value_report(pipeline_id):
    """
    Generate a pipeline value report showing value per stage.

    Args:
        pipeline_id: The pipeline to analyze
    """
    # Get pipeline stages
    pipelines = list_pipelines()
    target = None
    for p in pipelines:
        if p.get("id") == pipeline_id:
            target = p
            break

    if not target:
        print(f"Pipeline {pipeline_id} not found")
        return

    print(f"\n{'='*50}")
    print(f"Pipeline Report: {target.get('name')}")
    print(f"{'='*50}")

    stages = target.get("stages", [])
    grand_total = 0

    for stage in stages:
        stage_id = stage.get("id")
        stage_name = stage.get("name")

        # Get opportunities in this stage
        opps = search_opportunities(pipeline_id=pipeline_id, stage_id=stage_id)

        stage_value = sum(o.get("monetaryValue", 0) for o in opps)
        grand_total += stage_value

        print(f"\n  {stage_name}:")
        print(f"    Count: {len(opps)}")
        print(f"    Value: ${stage_value:,.2f}")

        if opps:
            avg = stage_value / len(opps)
            print(f"    Avg Deal: ${avg:,.2f}")

    print(f"\n{'='*50}")
    print(f"Grand Total: ${grand_total:,.2f}")
    print(f"{'='*50}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 5: Opportunities & Pipelines")
    print("=" * 60)

    # --- Exercise 1: List pipelines ---
    print("\n--- Exercise 1: List Pipelines ---")
    # list_pipelines()

    # --- Exercise 2: Create opportunity ---
    print("\n--- Exercise 2: Create Opportunity ---")
    # create_opportunity(
    #     pipeline_id="PIPELINE_ID",
    #     stage_id="STAGE_ID",
    #     contact_id="CONTACT_ID",
    #     name="API Test Deal",
    #     value=5000,
    # )

    # --- Exercise 3: Search opportunities ---
    print("\n--- Exercise 3: Search Opportunities ---")
    # search_opportunities(pipeline_id="PIPELINE_ID", status="open")

    # --- Exercise 4: Move opportunity to next stage ---
    print("\n--- Exercise 4: Move Stage ---")
    # update_opportunity("OPP_ID", stage_id="NEW_STAGE_ID")

    # --- Exercise 5: Mark as won ---
    print("\n--- Exercise 5: Mark as Won ---")
    # update_opportunity("OPP_ID", status="won")

    # --- Exercise 6: Pipeline report ---
    print("\n--- Exercise 6: Pipeline Report ---")
    # pipeline_value_report("PIPELINE_ID")

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
