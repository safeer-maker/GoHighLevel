"""
Day 7 API Lab: Marketing & Campaigns via GHL API
=================================================
Campaign management, email sending, and tracking.

NOTE: Run day-02's test_api_connection() first to verify API access.
send_marketing_email() uses the conversations endpoint to send individual emails.
For actual bulk campaigns, use GHL's built-in campaign feature (UI-based).
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


# --- 1. Send a One-Off Email (via Conversations API) ---

def send_marketing_email(contact_id, subject, html_body):
    """
    Send a single email to a contact. Uses the conversations/messages endpoint.
    For bulk campaigns, use GHL's built-in campaign feature.
    """
    url = f"{GHL_BASE_URL}/conversations/messages"

    payload = {
        "type": "Email",
        "contactId": contact_id,
        "subject": subject,
        "html": html_body,
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Email sent to {contact_id}: {subject}")
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 2. Get Contacts for Targeted Sending ---

def get_contacts_by_tag(tag, limit=100):
    """Get all contacts with a specific tag for campaign targeting."""
    url = f"{GHL_BASE_URL}/contacts/"
    params = {
        "locationId": GHL_LOCATION_ID,
        "query": tag,
        "limit": limit,
    }

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        contacts = response.json().get("contacts", [])
        # Filter to those who actually have the tag
        tagged = [c for c in contacts if tag in c.get("tags", [])]
        print(f"Found {len(tagged)} contacts with tag '{tag}'")
        return tagged
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 3. Simple Email Campaign (Sequential Send) ---

def run_simple_campaign(tag, subject, html_template):
    """
    Send an email to all contacts with a specific tag.
    Personalizes with contact name.

    Args:
        tag: Target contacts with this tag
        subject: Email subject (supports {{first_name}})
        html_template: HTML body (supports {{first_name}}, {{email}})
    """
    import time

    contacts = get_contacts_by_tag(tag)

    if not contacts:
        print("No contacts found. Campaign cancelled.")
        return

    print(f"\nStarting campaign: '{subject}' to {len(contacts)} contacts")
    print("-" * 50)

    sent = 0
    failed = 0

    for contact in contacts:
        first_name = contact.get("firstName", "there")
        email = contact.get("email", "")
        contact_id = contact.get("id")

        if not email:
            print(f"  Skipping {first_name} - no email")
            failed += 1
            continue

        # Personalize
        personalized_subject = subject.replace("{{first_name}}", first_name)
        personalized_body = (
            html_template
            .replace("{{first_name}}", first_name)
            .replace("{{email}}", email)
        )

        result = send_marketing_email(contact_id, personalized_subject, personalized_body)

        if result:
            sent += 1
        else:
            failed += 1

        time.sleep(1)  # Rate limiting

    print(f"\nCampaign complete: {sent} sent, {failed} failed")


# --- 4. Tag Contacts Based on Activity ---

def tag_contact(contact_id, tags):
    """Add tags to a contact (useful for trigger link simulation)."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}/tags"

    payload = {"tags": tags}
    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Tagged {contact_id} with {tags}")
        return True
    else:
        print(f"Error: {response.status_code}")
        return False


# --- 5. Campaign Report (Basic) ---

def campaign_summary(tag):
    """
    Generate a basic campaign report for contacts targeted by tag.
    Shows who has been contacted and basic stats.
    """
    contacts = get_contacts_by_tag(tag)

    print(f"\nCampaign Summary for tag: '{tag}'")
    print("=" * 50)
    print(f"Total recipients: {len(contacts)}")

    has_email = sum(1 for c in contacts if c.get("email"))
    has_phone = sum(1 for c in contacts if c.get("phone"))

    print(f"With email: {has_email}")
    print(f"With phone: {has_phone}")
    print(f"Reachable (email or phone): {sum(1 for c in contacts if c.get('email') or c.get('phone'))}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 7: Marketing & Campaigns")
    print("=" * 60)

    # --- Exercise 1: Send single email ---
    print("\n--- Exercise 1: Send Marketing Email ---")
    # send_marketing_email(
    #     contact_id="CONTACT_ID",
    #     subject="Special Offer Just for You!",
    #     html_body="<h1>20% Off!</h1><p>Use code SAVE20 at checkout.</p>",
    # )

    # --- Exercise 2: Get contacts by tag ---
    print("\n--- Exercise 2: Get Tagged Contacts ---")
    # contacts = get_contacts_by_tag("csv-import-day2")

    # --- Exercise 3: Run a mini campaign ---
    print("\n--- Exercise 3: Simple Campaign ---")
    # run_simple_campaign(
    #     tag="csv-import-day2",
    #     subject="Welcome, {{first_name}}!",
    #     html_template="""
    #     <h1>Welcome, {{first_name}}!</h1>
    #     <p>Thanks for joining us. We're excited to have you.</p>
    #     <p><a href='YOUR_BOOKING_LINK'>Book a Free Consultation</a></p>
    #     """,
    # )

    # --- Exercise 4: Campaign report ---
    print("\n--- Exercise 4: Campaign Report ---")
    # campaign_summary("csv-import-day2")

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
