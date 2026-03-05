"""
Day 6 API Lab: Payments & Invoicing via GHL API
================================================
List products, create invoices, check transactions.
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


# --- 1. List Products ---

def list_products():
    """List all products/prices in the sub-account."""
    url = f"{GHL_BASE_URL}/products/"
    params = {"locationId": GHL_LOCATION_ID}

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        products = response.json().get("products", [])
        print(f"Found {len(products)} products:")
        for p in products:
            price_info = p.get("prices", [{}])
            price = price_info[0].get("amount", 0) if price_info else 0
            print(f"  {p.get('name')}: ${price/100:.2f} (ID: {p.get('_id')})")
        return products
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 2. Create an Invoice ---

def create_invoice(contact_id, name, items, due_date, send=False):
    """
    Create a new invoice.

    Args:
        contact_id: GHL contact ID
        name: Invoice name/title
        items: List of dicts with {"name", "amount", "qty"}
        due_date: Due date (YYYY-MM-DD format)
        send: Whether to send immediately
    """
    url = f"{GHL_BASE_URL}/invoices/"

    line_items = []
    for item in items:
        line_items.append({
            "name": item["name"],
            "amount": item["amount"],  # In cents
            "qty": item.get("qty", 1),
        })

    payload = {
        "locationId": GHL_LOCATION_ID,
        "contactId": contact_id,
        "name": name,
        "dueDate": due_date,
        "items": line_items,
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        invoice = response.json()
        print(f"Invoice created: {invoice.get('_id', 'N/A')}")
        print(f"  Name: {name}")
        total = sum(i["amount"] * i.get("qty", 1) for i in items)
        print(f"  Total: ${total/100:.2f}")
        return invoice
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 3. Get Invoice Details ---

def get_invoice(invoice_id):
    """Get details of a specific invoice."""
    url = f"{GHL_BASE_URL}/invoices/{invoice_id}"

    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        inv = response.json()
        print(f"Invoice: {inv.get('name', 'N/A')}")
        print(f"  Status: {inv.get('status', 'N/A')}")
        print(f"  Due: {inv.get('dueDate', 'N/A')}")
        print(f"  Total: ${inv.get('total', 0)/100:.2f}")
        return inv
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 4. List Invoices ---

def list_invoices(status=None, limit=20):
    """
    List invoices with optional status filter.

    Args:
        status: Filter by status (draft, sent, paid, overdue, void)
        limit: Max results
    """
    url = f"{GHL_BASE_URL}/invoices/"
    params = {
        "locationId": GHL_LOCATION_ID,
        "limit": limit,
    }
    if status:
        params["status"] = status

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        invoices = response.json().get("invoices", [])
        print(f"Found {len(invoices)} invoices:")
        for inv in invoices:
            print(f"  {inv.get('_id')}: {inv.get('name')} - ${inv.get('total', 0)/100:.2f} [{inv.get('status')}]")
        return invoices
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 5. List Transactions ---

def list_transactions(limit=20):
    """List recent payment transactions."""
    url = f"{GHL_BASE_URL}/payments/transactions"
    params = {
        "locationId": GHL_LOCATION_ID,
        "limit": limit,
    }

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        transactions = data.get("transactions", data.get("data", []))
        print(f"Found {len(transactions)} transactions:")
        for tx in transactions:
            print(f"  {tx.get('_id', 'N/A')}: ${tx.get('amount', 0)/100:.2f} [{tx.get('status', 'N/A')}]")
        return transactions
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 6: Payments & Invoicing")
    print("=" * 60)

    # --- Exercise 1: List products ---
    print("\n--- Exercise 1: List Products ---")
    # list_products()

    # --- Exercise 2: Create invoice ---
    print("\n--- Exercise 2: Create Invoice ---")
    # create_invoice(
    #     contact_id="CONTACT_ID",
    #     name="Consultation + Setup",
    #     items=[
    #         {"name": "Initial Consultation", "amount": 15000, "qty": 1},  # $150
    #         {"name": "Setup Fee", "amount": 50000, "qty": 1},  # $500
    #     ],
    #     due_date="2024-04-01",
    # )

    # --- Exercise 3: List invoices ---
    print("\n--- Exercise 3: List Invoices ---")
    # list_invoices()
    # list_invoices(status="paid")

    # --- Exercise 4: Get invoice details ---
    print("\n--- Exercise 4: Invoice Details ---")
    # get_invoice("INVOICE_ID")

    # --- Exercise 5: List transactions ---
    print("\n--- Exercise 5: Transactions ---")
    # list_transactions()

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
