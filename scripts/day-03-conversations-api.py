"""
Day 3 API Lab: Conversations & Messaging via GHL API
=====================================================
Send SMS, emails, and retrieve conversation history.
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


# --- 1. Send SMS to a Contact ---

def send_sms(contact_id, message):
    """
    Send an SMS message to a contact.

    Args:
        contact_id: GHL contact ID
        message: Text message content
    """
    url = f"{GHL_BASE_URL}/conversations/messages"

    payload = {
        "type": "SMS",
        "contactId": contact_id,
        "message": message,
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        data = response.json()
        print(f"SMS sent successfully! Message ID: {data.get('messageId', 'N/A')}")
        return data
    else:
        print(f"Error sending SMS: {response.status_code}")
        print(response.text)
        return None


# --- 2. Send Email to a Contact ---

def send_email(contact_id, subject, body, from_email=None, from_name=None):
    """
    Send an email to a contact.

    Args:
        contact_id: GHL contact ID
        subject: Email subject line
        body: HTML body content
        from_email: Sender email (optional, uses default)
        from_name: Sender name (optional)
    """
    url = f"{GHL_BASE_URL}/conversations/messages"

    payload = {
        "type": "Email",
        "contactId": contact_id,
        "subject": subject,
        "html": body,
        "message": body,  # Plain text fallback
    }

    if from_email:
        payload["emailFrom"] = from_email
    if from_name:
        payload["emailFromName"] = from_name

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        data = response.json()
        print(f"Email sent successfully! Message ID: {data.get('messageId', 'N/A')}")
        return data
    else:
        print(f"Error sending email: {response.status_code}")
        print(response.text)
        return None


# --- 3. Get Conversation History ---

def get_conversations(contact_id, limit=20):
    """
    Get conversation messages for a specific contact.

    Args:
        contact_id: GHL contact ID
        limit: Max messages to retrieve
    """
    url = f"{GHL_BASE_URL}/conversations/search"

    params = {
        "locationId": GHL_LOCATION_ID,
        "contactId": contact_id,
        "limit": limit,
    }

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        conversations = data.get("conversations", [])
        print(f"Found {len(conversations)} conversations for contact {contact_id}")
        for conv in conversations:
            print(f"  ID: {conv.get('id')}")
            print(f"  Type: {conv.get('type')}")
            print(f"  Last Message: {conv.get('lastMessageBody', 'N/A')[:80]}")
            print(f"  Unread: {conv.get('unreadCount', 0)}")
            print()
        return conversations
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []


# --- 4. Get Messages in a Conversation ---

def get_messages(conversation_id, limit=20):
    """
    Get individual messages within a conversation thread.

    Args:
        conversation_id: The conversation ID (not contact ID)
        limit: Max messages to return
    """
    url = f"{GHL_BASE_URL}/conversations/{conversation_id}/messages"

    params = {"limit": limit}

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        messages = data.get("messages", {}).get("messages", [])
        print(f"Messages in conversation {conversation_id}:")
        for msg in messages:
            direction = msg.get("direction", "unknown")
            msg_type = msg.get("type", "unknown")
            body = msg.get("body", "")[:100]
            date = msg.get("dateAdded", "")
            print(f"  [{direction}] [{msg_type}] {date}: {body}")
        return messages
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []


# --- 5. Send Bulk SMS to Tagged Contacts ---

def send_bulk_sms_to_tagged(tag, message):
    """
    Send an SMS to all contacts with a specific tag.
    First searches for contacts, then sends SMS to each.

    Args:
        tag: Tag to filter contacts by
        message: SMS message to send
    """
    # Step 1: Get contacts with the tag
    url = f"{GHL_BASE_URL}/contacts/"
    params = {
        "locationId": GHL_LOCATION_ID,
        "query": tag,
        "limit": 100,
    }

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code != 200:
        print(f"Error fetching contacts: {response.status_code}")
        return

    contacts = response.json().get("contacts", [])
    tagged_contacts = [c for c in contacts if tag in c.get("tags", [])]

    print(f"Found {len(tagged_contacts)} contacts with tag '{tag}'")

    # Step 2: Send SMS to each
    import time
    for contact in tagged_contacts:
        contact_id = contact.get("id")
        name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}"

        # Personalize message
        personalized = message.replace("{{contact.first_name}}", contact.get("firstName", "there"))

        print(f"Sending SMS to {name} ({contact_id})...")
        send_sms(contact_id, personalized)
        time.sleep(1)  # Rate limiting


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 3: Conversations & Messaging")
    print("=" * 60)

    # --- Exercise 1: Send SMS ---
    print("\n--- Exercise 1: Send SMS ---")
    # send_sms("CONTACT_ID_HERE", "Hi! This is a test message from the GHL API.")

    # --- Exercise 2: Send Email ---
    print("\n--- Exercise 2: Send Email ---")
    # send_email(
    #     contact_id="CONTACT_ID_HERE",
    #     subject="Welcome to Our Service!",
    #     body="<h1>Welcome!</h1><p>Thanks for signing up. We're excited to have you.</p>",
    # )

    # --- Exercise 3: Get Conversations ---
    print("\n--- Exercise 3: Get Conversations ---")
    # get_conversations("CONTACT_ID_HERE")

    # --- Exercise 4: Get Messages ---
    print("\n--- Exercise 4: Get Messages ---")
    # get_messages("CONVERSATION_ID_HERE")

    # --- Exercise 5: Bulk SMS ---
    print("\n--- Exercise 5: Bulk SMS to Tagged Contacts ---")
    # send_bulk_sms_to_tagged("new-lead", "Hi {{contact.first_name}}, welcome aboard!")

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
