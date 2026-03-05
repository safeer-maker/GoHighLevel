"""
Day 9 API Lab: Automation & Workflows via GHL API
==================================================
Trigger workflows, add contacts to workflows, and webhook handling.
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


# --- 1. List Workflows ---

def list_workflows():
    """List all workflows in the sub-account."""
    url = f"{GHL_BASE_URL}/workflows/"
    params = {"locationId": GHL_LOCATION_ID}

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        workflows = response.json().get("workflows", [])
        print(f"Found {len(workflows)} workflows:")
        for wf in workflows:
            status = wf.get("status", "unknown")
            print(f"  {wf.get('id')}: {wf.get('name')} [{status}]")
        return workflows
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 2. Add Contact to Workflow ---

def add_contact_to_workflow(workflow_id, contact_id):
    """
    Manually add a contact to a workflow (triggers it for that contact).

    Args:
        workflow_id: The workflow ID
        contact_id: The contact to add
    """
    url = f"{GHL_BASE_URL}/contacts/{contact_id}/workflow/{workflow_id}"

    payload = {"eventStartTime": ""}

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Added contact {contact_id} to workflow {workflow_id}")
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


# --- 3. Remove Contact from Workflow ---

def remove_contact_from_workflow(workflow_id, contact_id):
    """Remove a contact from a workflow (stops it for that contact)."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}/workflow/{workflow_id}"

    response = requests.delete(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Removed contact {contact_id} from workflow {workflow_id}")
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


# --- 4. Trigger Workflow via Webhook ---

def create_webhook_trigger_example():
    """
    Example of setting up a webhook-triggered workflow.

    In GHL:
    1. Create a workflow with trigger type: "Inbound Webhook"
    2. GHL provides a webhook URL
    3. POST data to that URL to trigger the workflow

    This function shows how to call such a webhook.
    """
    # Replace with your actual GHL webhook URL from the workflow trigger
    webhook_url = "YOUR_GHL_WORKFLOW_WEBHOOK_URL"

    payload = {
        "first_name": "Webhook",
        "last_name": "Test",
        "email": "webhook.test@example.com",
        "phone": "+15551234999",
        "custom_field_1": "Value from external system",
    }

    print("Webhook Trigger Example")
    print(f"  URL: {webhook_url}")
    print(f"  Payload: {json.dumps(payload, indent=2)}")
    print()
    print("To use this:")
    print("1. Create a workflow in GHL with 'Inbound Webhook' trigger")
    print("2. Copy the webhook URL from the trigger settings")
    print("3. Replace YOUR_GHL_WORKFLOW_WEBHOOK_URL above")
    print("4. Uncomment the requests.post line below")

    # response = requests.post(webhook_url, json=payload)
    # if response.status_code == 200:
    #     print("Webhook triggered successfully!")
    # else:
    #     print(f"Error: {response.status_code} - {response.text}")


# --- 5. Build a Simple Webhook Receiver (Flask) ---

def webhook_receiver_example():
    """
    Example Flask app that receives webhooks FROM GHL.

    When you set up outbound webhooks in GHL workflows (HTTP action),
    this server receives and processes the data.

    To run: Save as webhook_server.py and run `python webhook_server.py`
    Use ngrok to expose locally: `ngrok http 5000`
    """

    code = '''
# webhook_server.py - Save and run separately
# pip install flask

from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook/ghl", methods=["POST"])
def ghl_webhook():
    """Receive webhooks from GHL workflows."""
    data = request.json

    # Log the incoming webhook
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\\n[{timestamp}] Webhook received!")
    print(f"  Data: {json.dumps(data, indent=2)}")

    # Process based on event type
    event_type = data.get("type", "unknown")
    contact = data.get("contact", {})

    if event_type == "ContactCreate":
        name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}"
        print(f"  New contact created: {name}")

    elif event_type == "AppointmentCreate":
        print(f"  New appointment booked!")

    elif event_type == "OpportunityStageUpdate":
        print(f"  Opportunity moved to new stage!")

    # Return 200 to acknowledge receipt
    return jsonify({"status": "received", "timestamp": timestamp}), 200


@app.route("/webhook/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    print("GHL Webhook Receiver running on http://localhost:5000")
    print("Endpoint: POST /webhook/ghl")
    print("Use ngrok to expose: ngrok http 5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
'''

    print("Webhook Receiver Example")
    print("=" * 50)
    print(code)
    print()
    print("Save the above code as 'webhook_server.py' and run it.")
    print("Use ngrok to make it accessible from the internet.")
    print("Then add the ngrok URL as an HTTP webhook action in your GHL workflow.")


# --- 6. Bulk Add Contacts to Workflow ---

def bulk_add_to_workflow(workflow_id, contact_ids):
    """
    Add multiple contacts to a workflow with rate limiting.

    Args:
        workflow_id: Target workflow ID
        contact_ids: List of contact IDs
    """
    import time

    print(f"Adding {len(contact_ids)} contacts to workflow {workflow_id}")
    success = 0
    failed = 0

    for contact_id in contact_ids:
        if add_contact_to_workflow(workflow_id, contact_id):
            success += 1
        else:
            failed += 1
        time.sleep(0.5)  # Rate limiting

    print(f"\nComplete: {success} added, {failed} failed")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 9: Automation & Workflows")
    print("=" * 60)

    # --- Exercise 1: List workflows ---
    print("\n--- Exercise 1: List Workflows ---")
    # list_workflows()

    # --- Exercise 2: Add contact to workflow ---
    print("\n--- Exercise 2: Add to Workflow ---")
    # add_contact_to_workflow("WORKFLOW_ID", "CONTACT_ID")

    # --- Exercise 3: Remove from workflow ---
    print("\n--- Exercise 3: Remove from Workflow ---")
    # remove_contact_from_workflow("WORKFLOW_ID", "CONTACT_ID")

    # --- Exercise 4: Webhook trigger example ---
    print("\n--- Exercise 4: Webhook Trigger ---")
    # create_webhook_trigger_example()

    # --- Exercise 5: Webhook receiver example ---
    print("\n--- Exercise 5: Webhook Receiver ---")
    # webhook_receiver_example()

    # --- Exercise 6: Bulk add to workflow ---
    print("\n--- Exercise 6: Bulk Add ---")
    # bulk_add_to_workflow("WORKFLOW_ID", ["CONTACT_1", "CONTACT_2", "CONTACT_3"])

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
