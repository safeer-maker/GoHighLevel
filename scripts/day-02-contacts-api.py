"""
Day 2 API Lab: Contact Management via GHL API
================================================
This script demonstrates CRUD operations on contacts using the GHL API.

GHL API Docs: https://highlevel.stoplight.io/docs/integrations

Before running:
1. cp config.py.example config.py
2. Fill in your GHL_API_KEY and GHL_LOCATION_ID (see config.py.example for instructions)

IMPORTANT - Sub-Account API Access:
- Not all sub-accounts have API access enabled by default.
- If you get 401 (Unauthorized) or 403 (Forbidden) errors, your account may
  need API access enabled by the agency admin, or you may need to create a
  Private App via the GHL Developer Marketplace.
- If API access isn't available yet, READ through this script to understand the
  concepts. The UI exercises in the lesson are the priority. You'll get deep
  into API work during Phase 3 (Days 18-20).
- Run the "test_api_connection()" function first to verify your setup.
"""

import requests
import json
import csv
import time
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION


# --- Helper ---

def get_headers():
    """Standard headers for GHL API requests."""
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }


# --- 0. Test API Connection ---

def test_api_connection():
    """
    Test that your API key and Location ID are working.
    Run this FIRST before any other exercises.
    """
    url = f"{GHL_BASE_URL}/contacts/"
    params = {"locationId": GHL_LOCATION_ID, "limit": 1}

    print("Testing API connection...")
    print(f"  Base URL: {GHL_BASE_URL}")
    print(f"  Location ID: {GHL_LOCATION_ID[:8]}..." if len(GHL_LOCATION_ID) > 8 else f"  Location ID: {GHL_LOCATION_ID}")

    try:
        response = requests.get(url, headers=get_headers(), params=params)

        if response.status_code == 200:
            data = response.json()
            count = len(data.get("contacts", []))
            print(f"\n  SUCCESS! API connection working.")
            print(f"  Found contacts in account: {'Yes' if count > 0 else 'No (empty account)'}")
            return True
        elif response.status_code == 401:
            print(f"\n  FAILED: 401 Unauthorized")
            print("  Your API key is invalid or expired.")
            print("  Check config.py and verify your GHL_API_KEY.")
            return False
        elif response.status_code == 403:
            print(f"\n  FAILED: 403 Forbidden")
            print("  Your sub-account may not have API access enabled.")
            print("  Options:")
            print("    1. Ask your agency admin to enable API access")
            print("    2. Create a Private App at marketplace.gohighlevel.com")
            print("    3. Skip API labs for now - focus on UI exercises")
            return False
        else:
            print(f"\n  UNEXPECTED: Status {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"\n  FAILED: Cannot connect to {GHL_BASE_URL}")
        print("  Check your internet connection.")
        return False


# --- 1. Create a Contact ---

def create_contact(first_name, last_name, email, phone, custom_fields=None, tags=None):
    """
    Create a new contact in GHL.

    Args:
        first_name: Contact's first name
        last_name: Contact's last name
        email: Contact's email address
        phone: Contact's phone number (include country code, e.g., +15551234567)
        custom_fields: List of dicts with {"id": "field_key", "value": "field_value"}
        tags: List of tag strings

    Returns:
        dict: API response with created contact data
    """
    url = f"{GHL_BASE_URL}/contacts/"

    payload = {
        "locationId": GHL_LOCATION_ID,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "phone": phone,
    }

    if custom_fields:
        payload["customFields"] = custom_fields

    if tags:
        payload["tags"] = tags

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        contact = response.json().get("contact", {})
        print(f"Created contact: {contact.get('id')} - {first_name} {last_name}")
        return contact
    else:
        print(f"Error creating contact: {response.status_code}")
        print(response.text)
        return None


# --- 2. Search Contacts ---

def search_contacts(query=None, email=None, phone=None, limit=20):
    """
    Search for contacts using various filters.

    Args:
        query: General search query (searches name, email, phone)
        email: Search by exact email
        phone: Search by exact phone
        limit: Max results to return (default 20)

    Returns:
        list: List of matching contacts
    """
    url = f"{GHL_BASE_URL}/contacts/"

    params = {
        "locationId": GHL_LOCATION_ID,
        "limit": limit,
    }

    if query:
        params["query"] = query
    if email:
        params["email"] = email
    if phone:
        params["phone"] = phone

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        contacts = data.get("contacts", [])
        print(f"Found {len(contacts)} contacts")
        for c in contacts:
            print(f"  - {c.get('id')}: {c.get('firstName', '')} {c.get('lastName', '')} ({c.get('email', 'no email')})")
        return contacts
    else:
        print(f"Error searching contacts: {response.status_code}")
        print(response.text)
        return []


# --- 3. Get a Single Contact ---

def get_contact(contact_id):
    """
    Retrieve a single contact by ID.

    Args:
        contact_id: The GHL contact ID

    Returns:
        dict: Contact data
    """
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"

    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        contact = response.json().get("contact", {})
        print(f"Contact: {contact.get('firstName')} {contact.get('lastName')}")
        print(f"  Email: {contact.get('email')}")
        print(f"  Phone: {contact.get('phone')}")
        print(f"  Tags: {contact.get('tags', [])}")
        print(f"  Custom Fields: {json.dumps(contact.get('customFields', []), indent=2)}")
        return contact
    else:
        print(f"Error getting contact: {response.status_code}")
        return None


# --- 4. Update a Contact ---

def update_contact(contact_id, updates):
    """
    Update an existing contact.

    Args:
        contact_id: The GHL contact ID
        updates: Dict of fields to update (e.g., {"firstName": "New Name", "tags": ["vip"]})

    Returns:
        dict: Updated contact data
    """
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"

    response = requests.put(url, headers=get_headers(), json=updates)

    if response.status_code == 200:
        contact = response.json().get("contact", {})
        print(f"Updated contact: {contact_id}")
        return contact
    else:
        print(f"Error updating contact: {response.status_code}")
        print(response.text)
        return None


# --- 5. Delete a Contact ---

def delete_contact(contact_id):
    """
    Delete a contact by ID.

    Args:
        contact_id: The GHL contact ID

    Returns:
        bool: True if deleted successfully
    """
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"

    response = requests.delete(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Deleted contact: {contact_id}")
        return True
    else:
        print(f"Error deleting contact: {response.status_code}")
        print(response.text)
        return False


# --- 6. Add Tags to a Contact ---

def add_tags(contact_id, tags):
    """
    Add tags to an existing contact.

    Args:
        contact_id: The GHL contact ID
        tags: List of tag strings to add
    """
    url = f"{GHL_BASE_URL}/contacts/{contact_id}/tags"

    payload = {"tags": tags}

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Added tags {tags} to contact {contact_id}")
        return response.json()
    else:
        print(f"Error adding tags: {response.status_code}")
        print(response.text)
        return None


# --- 7. List All Contacts with Pagination ---

def list_all_contacts(limit_per_page=100):
    """
    Retrieve ALL contacts using pagination.
    GHL API returns max 100 contacts per page.

    Returns:
        list: All contacts
    """
    url = f"{GHL_BASE_URL}/contacts/"
    all_contacts = []
    start_after = None
    page = 1

    while True:
        params = {
            "locationId": GHL_LOCATION_ID,
            "limit": limit_per_page,
        }
        if start_after:
            params["startAfter"] = start_after

        response = requests.get(url, headers=get_headers(), params=params)

        if response.status_code != 200:
            print(f"Error on page {page}: {response.status_code}")
            break

        data = response.json()
        contacts = data.get("contacts", [])

        if not contacts:
            break

        all_contacts.extend(contacts)
        print(f"Page {page}: Retrieved {len(contacts)} contacts (total: {len(all_contacts)})")

        # Get the ID of the last contact for pagination
        start_after = contacts[-1].get("id")
        page += 1

        # Rate limiting - be nice to the API
        time.sleep(0.5)

    print(f"\nTotal contacts retrieved: {len(all_contacts)}")
    return all_contacts


# --- 8. Export Contacts to CSV ---

def export_contacts_to_csv(filename="exported_contacts.csv"):
    """
    Export all contacts to a CSV file.

    Args:
        filename: Output CSV file path
    """
    contacts = list_all_contacts()

    if not contacts:
        print("No contacts to export")
        return

    # Define CSV columns
    fieldnames = ["id", "firstName", "lastName", "email", "phone", "tags", "dateAdded"]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()

        for contact in contacts:
            contact["tags"] = ", ".join(contact.get("tags", []))
            writer.writerow(contact)

    print(f"Exported {len(contacts)} contacts to {filename}")


# --- 9. Bulk Create Contacts ---

def bulk_create_contacts(contacts_data):
    """
    Create multiple contacts with a delay between each to respect rate limits.

    Args:
        contacts_data: List of dicts, each with keys: firstName, lastName, email, phone, tags

    Returns:
        list: Created contact IDs
    """
    created_ids = []

    for i, data in enumerate(contacts_data):
        print(f"\nCreating contact {i+1}/{len(contacts_data)}...")
        contact = create_contact(
            first_name=data.get("firstName", ""),
            last_name=data.get("lastName", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            tags=data.get("tags", []),
            custom_fields=data.get("customFields"),
        )

        if contact:
            created_ids.append(contact.get("id"))

        # Rate limiting
        time.sleep(0.3)

    print(f"\nCreated {len(created_ids)} contacts successfully")
    return created_ids


# ============================================================
# MAIN - Uncomment the sections you want to run
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 2: Contact Management")
    print("=" * 60)

    # --- Exercise 0: Test connection (RUN THIS FIRST) ---
    print("\n--- Exercise 0: Test API Connection ---")
    test_api_connection()
    # If this fails, fix your config.py before proceeding.
    # If you get 403, API access may not be available on your sub-account.
    # In that case, read through the script to understand the concepts,
    # and focus on the UI exercises in the lesson.

    # --- Exercise 1: Create a single contact ---
    print("\n--- Exercise 1: Create Contact ---")
    # new_contact = create_contact(
    #     first_name="Alex",
    #     last_name="Johnson",
    #     email="alex.johnson@example.com",
    #     phone="+15551234567",
    #     tags=["api-created", "day2-lab"],
    # )

    # --- Exercise 2: Search contacts ---
    print("\n--- Exercise 2: Search Contacts ---")
    # results = search_contacts(query="Alex")
    # results = search_contacts(email="alex.johnson@example.com")

    # --- Exercise 3: Get a single contact ---
    print("\n--- Exercise 3: Get Contact ---")
    # contact = get_contact("CONTACT_ID_HERE")

    # --- Exercise 4: Update a contact ---
    print("\n--- Exercise 4: Update Contact ---")
    # updated = update_contact("CONTACT_ID_HERE", {
    #     "tags": ["api-created", "day2-lab", "updated-via-api"],
    #     "customFields": [
    #         {"id": "membership_type", "value": "Premium"},
    #     ]
    # })

    # --- Exercise 5: Add tags ---
    print("\n--- Exercise 5: Add Tags ---")
    # add_tags("CONTACT_ID_HERE", ["vip", "high-priority"])

    # --- Exercise 6: List all contacts with pagination ---
    print("\n--- Exercise 6: List All Contacts ---")
    # all_contacts = list_all_contacts()

    # --- Exercise 7: Export to CSV ---
    print("\n--- Exercise 7: Export to CSV ---")
    # export_contacts_to_csv("my_contacts_export.csv")

    # --- Exercise 8: Bulk create contacts ---
    print("\n--- Exercise 8: Bulk Create ---")
    # sample_contacts = [
    #     {"firstName": "Test1", "lastName": "User", "email": "test1@example.com", "phone": "+15550001001", "tags": ["bulk-import"]},
    #     {"firstName": "Test2", "lastName": "User", "email": "test2@example.com", "phone": "+15550001002", "tags": ["bulk-import"]},
    #     {"firstName": "Test3", "lastName": "User", "email": "test3@example.com", "phone": "+15550001003", "tags": ["bulk-import"]},
    # ]
    # bulk_create_contacts(sample_contacts)

    # --- Exercise 9: Delete a contact ---
    print("\n--- Exercise 9: Delete Contact ---")
    # delete_contact("CONTACT_ID_HERE")

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them one at a time.")
    print("Replace CONTACT_ID_HERE with actual IDs from your account.")
    print("=" * 60)
