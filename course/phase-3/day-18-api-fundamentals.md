# Day 18: GHL API Deep Dive - Authentication & Contacts

**Time Required:** 3-4 hours
**Level:** Expert
**Certification Alignment:** Agency API access, API authentication methods, Private Apps, Marketplace apps

---

## Today's Mission

After 17 days of building Sunrise Wellness Studio through the GHL UI, you have seen every feature the platform offers. Today you graduate from clicking to coding. You will learn how to talk to GHL programmatically through its REST API - authenticate requests, create contacts, search with filters, handle pagination, and build your first Python scripts that automate what you previously did manually. By the end of today, you will have a working Python toolkit for contact management that you can extend for any integration.

---

## Learning Objectives

1. Understand REST API fundamentals and why they matter for GHL
2. Set up API authentication via Private Apps in the GHL Marketplace
3. Perform full CRUD operations on contacts using Python
4. Handle pagination, rate limits, and errors gracefully
5. Map CSV data to GHL custom fields programmatically

---

## Part 1: Understanding GHL's API (30 min)

### What is a REST API?

A **REST API** is how two computer systems talk to each other over the internet using HTTP requests. Think of it like ordering at a restaurant:

- **You (the client)** tell the waiter what you want ("I'll have the GET /contacts")
- **The waiter (HTTP)** delivers your order to the kitchen
- **The kitchen (GHL's server)** prepares your response
- **The waiter brings it back** as JSON data

Every API interaction follows this pattern. You send a request, you get a response.

### The Four Main HTTP Methods

| Method | What It Does | Restaurant Analogy |
|--------|-------------|-------------------|
| **GET** | Retrieve data | "What's on the menu?" |
| **POST** | Create new data | "I'd like to order the salmon" |
| **PUT** | Update existing data | "Change my order to chicken" |
| **DELETE** | Remove data | "Cancel my order" |

### Why Use the API Instead of the UI?

The GHL UI is great for daily operations, but the API unlocks superpowers:

1. **Bulk operations** - Import 10,000 contacts in 10 minutes (vs hours clicking)
2. **Integrations** - Connect GHL to any other tool (Stripe, Calendly, your own app)
3. **Custom dashboards** - Build reports the UI doesn't offer
4. **Automation beyond workflows** - Logic too complex for the workflow builder
5. **Data migration** - Move contacts between sub-accounts
6. **Scheduled tasks** - Run scripts nightly, weekly, on cron

### GHL API Architecture

- **Base URL:** `https://services.leadconnectorhq.com`
- **Version header:** `Version: 2021-07-28` (required on every request)
- **Content type:** `application/json`
- **Auth:** Bearer token in `Authorization` header
- **Documentation:** https://highlevel.stoplight.io/docs/integrations

### Authentication Methods

GHL offers three authentication approaches:

| Method | When to Use | Pros | Cons |
|--------|------------|------|------|
| **Private App (recommended)** | Your own scripts, single sub-account | Simple, stable | Per sub-account |
| **OAuth 2.0 (Marketplace App)** | Public apps, multi-tenant tools | Scalable, official | Complex setup |
| **Location API Key (legacy)** | Old integrations only | Simple | Being deprecated |

Today we use Private Apps - the modern, simple path for your own work.

### Rate Limits

GHL enforces rate limits to protect the platform:
- **100 requests per 10 seconds per location**
- **200,000 requests per day per location**

Exceed these and you get a `429 Too Many Requests` response. Your scripts should include `time.sleep(0.1)` between calls to stay safe.

> **Pro Tip:** Never hit the API in a tight loop without delays. One runaway script can lock you out for 10 minutes.

---

## Part 2: Getting API Access (45 min)

### What is a Private App?

A **Private App** is like creating an ID card for your Python script. GHL issues a unique Access Token that your script uses to prove it has permission to interact with your sub-account.

### Exercise 18.1: Create a Private App in the Marketplace

1. Go to **https://marketplace.gohighlevel.com/**
2. Sign up (free developer account) using the SAME email you use for your GHL sub-account
3. Go to **Apps > My Apps > + Create App**
4. Choose **Private** (not Public/Marketplace)
5. Fill in:
   - **App Name:** "Sunrise Wellness API Tools"
   - **Description:** "Internal automation scripts for Sunrise Wellness Studio"
   - **Distribution Type:** Private (Sub-Account)
6. Click **Create**

### Exercise 18.2: Select API Scopes (Permissions)

**Scopes** are permissions - exactly what your app is allowed to do. Enable only what you need.

For today's lesson, enable these scopes:

| Scope | Purpose |
|-------|---------|
| `contacts.readonly` | Read contact data |
| `contacts.write` | Create/update/delete contacts |
| `locations.readonly` | Access location info |
| `custom-fields.readonly` | Read custom field definitions |
| `custom-fields.write` | Create custom fields |
| `conversations.readonly` | Read messages (for Day 19) |
| `conversations.write` | Send messages (for Day 19) |

Save the scopes.

### Exercise 18.3: Generate Access Token

1. In your app settings, find **Access Token** or **Credentials**
2. Click **Generate Token** (or copy if already shown)
3. Select your sub-account (location) to install the app into
4. Copy the Access Token - it looks like: `pit-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
5. **CRITICAL:** Store this securely. Anyone with this token can control your sub-account.

> **Security Warning:** Never commit API tokens to git, post in Slack, or share via email. Use a password manager or `.env` file that is gitignored.

### Exercise 18.4: Find Your Location ID

You also need your sub-account's Location ID:

**Method 1 - From URL:**
- Log into your sub-account
- Look at the URL: `app.gohighlevel.com/v2/location/ABC123XYZ/...`
- The part after `/location/` is your Location ID

**Method 2 - From Settings:**
- Settings > Company (or Business Profile)
- Look for "Location ID" or check the URL

**Method 3 - Via API (after you have the token):**
```python
import requests
response = requests.get(
    "https://services.leadconnectorhq.com/locations/search",
    headers={"Authorization": "Bearer YOUR_TOKEN", "Version": "2021-07-28"}
)
print(response.json())
```

### Exercise 18.5: Test Your Credentials with Postman or curl

Before writing Python, verify your credentials work with a simple tool:

**Using curl:**
```bash
curl -X GET "https://services.leadconnectorhq.com/contacts/?locationId=YOUR_LOCATION_ID&limit=1" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Version: 2021-07-28"
```

**Expected response:** JSON with a contacts array (possibly empty if you have no contacts yet).

**If you get errors:**
| Error Code | Meaning | Fix |
|-----------|---------|-----|
| 401 Unauthorized | Bad token | Regenerate token, check you copied it fully |
| 403 Forbidden | Missing scope | Add the scope, reinstall app |
| 404 Not Found | Wrong location ID | Verify location ID |
| 422 Unprocessable | Bad request data | Check parameters |

---

## Part 3: Python Environment Setup (20 min)

### Exercise 18.6: Install Dependencies

Your course repo already has a `scripts/` folder with `requirements.txt`. Update it if needed:

```bash
cd /home/hex/Documents/devops/GoHighLevel/scripts
pip install -r requirements.txt
```

Required packages:
```
requests>=2.31.0
python-dotenv>=1.0.0
```

### Exercise 18.7: Secure Your Credentials with .env

Create a `.env` file in the scripts folder:

```bash
# scripts/.env (NEVER commit this file)
GHL_API_TOKEN=pit-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GHL_LOCATION_ID=abc123xyz
```

Verify `.gitignore` includes `.env` and `config.py`:
```
config.py
.env
__pycache__/
*.pyc
```

### Exercise 18.8: Update config.py to Use .env

```python
# scripts/config.py
import os
from dotenv import load_dotenv

load_dotenv()

GHL_API_KEY = os.getenv("GHL_API_TOKEN", "your-token-here")
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID", "your-location-here")
GHL_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"
```

### Exercise 18.9: Verify with test_api_connection()

Run the test function from `scripts/day-02-contacts-api.py`:

```python
python -c "from day_02_contacts_api import test_api_connection; test_api_connection()"
```

You should see "SUCCESS! API connection working." If not, debug with the error table above.

---

## Part 4: Contact CRUD Operations (90 min)

### Exercise 18.10: Create a Contact (POST)

**The Endpoint:** `POST /contacts/`

```python
import requests
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION

def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }

def create_contact(first_name, last_name, email, phone, tags=None):
    """Create a new contact in GHL."""
    url = f"{GHL_BASE_URL}/contacts/"
    
    payload = {
        "locationId": GHL_LOCATION_ID,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "phone": phone,
    }
    
    if tags:
        payload["tags"] = tags
    
    response = requests.post(url, headers=get_headers(), json=payload)
    
    if response.status_code == 200:
        contact = response.json().get("contact", {})
        print(f"Created: {contact.get('id')} - {first_name} {last_name}")
        return contact
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Test it:
new_contact = create_contact(
    first_name="API",
    last_name="Test",
    email=f"api.test{int(time.time())}@yopmail.com",
    phone="+12024567999",
    tags=["api-created", "day18-test"]
)
```

**Key points:**
- `locationId` is required on every request
- Email format must be valid
- Phone should include country code
- `tags` is a list, not a string
- Response includes the new contact's auto-generated ID

### Exercise 18.11: Search/Read Contacts (GET)

**The Endpoint:** `GET /contacts/`

```python
def search_contacts(query=None, email=None, limit=20):
    """Search contacts with optional filters."""
    url = f"{GHL_BASE_URL}/contacts/"
    
    params = {"locationId": GHL_LOCATION_ID, "limit": limit}
    if query:
        params["query"] = query
    if email:
        params["email"] = email
    
    response = requests.get(url, headers=get_headers(), params=params)
    
    if response.status_code == 200:
        contacts = response.json().get("contacts", [])
        return contacts
    return []

# Find Sunrise Wellness members
members = search_contacts(query="Chen")
for m in members:
    print(f"{m.get('firstName')} {m.get('lastName')} - {m.get('email')}")
```

### Exercise 18.12: Full Pagination - Fetch ALL Contacts

GHL returns max 100 per page. To get everything:

```python
def list_all_contacts():
    """Get every contact using pagination."""
    all_contacts = []
    start_after = None
    page = 1
    
    while True:
        params = {"locationId": GHL_LOCATION_ID, "limit": 100}
        if start_after:
            params["startAfterId"] = start_after
        
        response = requests.get(
            f"{GHL_BASE_URL}/contacts/",
            headers=get_headers(),
            params=params
        )
        
        if response.status_code != 200:
            print(f"Error on page {page}: {response.status_code}")
            break
        
        contacts = response.json().get("contacts", [])
        if not contacts:
            break
        
        all_contacts.extend(contacts)
        print(f"Page {page}: {len(contacts)} contacts (total: {len(all_contacts)})")
        
        start_after = contacts[-1].get("id")
        page += 1
        
        import time
        time.sleep(0.2)  # Rate limiting
    
    return all_contacts
```

### Exercise 18.13: Update a Contact (PUT)

```python
def update_contact(contact_id, updates):
    """Update fields on a contact."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"
    response = requests.put(url, headers=get_headers(), json=updates)
    
    if response.status_code == 200:
        print(f"Updated {contact_id}")
        return response.json().get("contact")
    else:
        print(f"Error: {response.text}")
        return None

# Example: Mark Maria Chen as VIP
update_contact("CONTACT_ID_HERE", {
    "tags": ["vip", "premium-member", "updated-via-api"],
    "firstName": "Maria"  # Can update any field
})
```

### Exercise 18.14: Delete a Contact (DELETE)

```python
def delete_contact(contact_id):
    """Permanently delete a contact. Use carefully."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"
    response = requests.delete(url, headers=get_headers())
    
    if response.status_code == 200:
        print(f"Deleted {contact_id}")
        return True
    return False
```

> **Pro Tip:** Prefer tagging as "archived-YYYYMMDD" over deleting. Deleted data is hard to recover and can break workflow history.

### Exercise 18.15: Batch Import from CSV

Combining everything:

```python
import csv
import time

def bulk_import_from_csv(csv_file):
    """Import all contacts from a CSV file."""
    created = []
    failed = []
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        
        for i, row in enumerate(reader, 1):
            print(f"Importing row {i}: {row['First Name']} {row['Last Name']}")
            
            contact = create_contact(
                first_name=row['First Name'],
                last_name=row['Last Name'],
                email=row['Email'],
                phone=row['Phone'],
                tags=["bulk-import", f"source-{row.get('Lead Source', 'unknown').lower()}"]
            )
            
            if contact:
                created.append(contact.get('id'))
            else:
                failed.append(row['Email'])
            
            time.sleep(0.3)  # Respect rate limits
    
    print(f"\nImport complete: {len(created)} created, {len(failed)} failed")
    return created, failed

# Run it on the sample CSV
bulk_import_from_csv("/home/hex/Documents/devops/GoHighLevel/course/phase-1/sample-contacts.csv")
```

---

## Part 5: Working with Custom Fields (30 min)

### Exercise 18.16: Get Your Custom Field IDs

Custom fields are referenced by their ID in the API, not their display name:

```python
def get_custom_fields():
    """Retrieve all custom field definitions for the location."""
    url = f"{GHL_BASE_URL}/locations/{GHL_LOCATION_ID}/customFields"
    response = requests.get(url, headers=get_headers())
    
    if response.status_code == 200:
        fields = response.json().get("customFields", [])
        print(f"Found {len(fields)} custom fields:")
        for f in fields:
            print(f"  {f.get('name')}: {f.get('id')} (type: {f.get('dataType')})")
        return fields
    return []
```

### Exercise 18.17: Update Contact with Custom Field

```python
def set_fitness_goals(contact_id, fitness_goals_field_id, goals):
    """Update a contact's Fitness Goals custom field."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}"
    
    payload = {
        "customFields": [
            {
                "id": fitness_goals_field_id,
                "value": goals  # Multi-select as array: ["Weight Loss", "Flexibility"]
            }
        ]
    }
    
    response = requests.put(url, headers=get_headers(), json=payload)
    return response.status_code == 200

# Update Maria Chen
set_fitness_goals("MARIA_CONTACT_ID", "fitness_goals_field_id", ["Weight Loss", "Flexibility"])
```

---

## Part 6: Tags and Bulk Operations (20 min)

### Exercise 18.18: Add Tags

```python
def add_tags(contact_id, tags):
    """Add tags to an existing contact."""
    url = f"{GHL_BASE_URL}/contacts/{contact_id}/tags"
    response = requests.post(
        url,
        headers=get_headers(),
        json={"tags": tags}
    )
    return response.status_code == 200
```

### Exercise 18.19: Bulk Tag All Premium Members

```python
def bulk_tag_premium_members(new_tag):
    """Find all Premium members and add a tag."""
    contacts = list_all_contacts()
    
    premium_members = [
        c for c in contacts
        if any("Premium" in str(cf.get("value", "")) for cf in c.get("customFields", []))
    ]
    
    print(f"Found {len(premium_members)} Premium members")
    
    for contact in premium_members:
        add_tags(contact["id"], [new_tag])
        time.sleep(0.2)
    
    print(f"Tagged all Premium members with '{new_tag}'")

# Tag them for an upcoming campaign
bulk_tag_premium_members("spring-challenge-invite")
```

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Patient Sync

**Situation:** BrightSmile uses an external dental practice management system. Weekly, they export a CSV of patient updates that need to sync into GHL.

**Your Task:** Build `dental_sync.py` that:

1. Reads `dental-patients.csv` (columns: Patient ID, First, Last, Email, Phone, Last Visit, Next Appointment, Insurance Provider, Treatment Plan)
2. For each row:
   - Search GHL by email to see if patient exists
   - If NOT exists: Create with dental custom fields populated
   - If exists: Update with latest visit date, appointment, treatment plan
3. Dedupe by email (never create duplicates)
4. Log results to `dental-sync-YYYY-MM-DD.log`:
   - Count created, count updated, count failed
   - Each failed patient and reason
5. Email summary to admin (via GHL conversations API - preview for Day 19)

Build this as a reusable script the dental team can run every Monday.

### Case Scenario 2: Elevate Digital Agency MRR Calculator

**Situation:** Elevate Digital has 30+ clients, each with a monthly retainer. The agency owner wants a daily report of total Monthly Recurring Revenue (MRR).

**Your Task:** Build `mrr_report.py` that:

1. Fetches all contacts tagged `active-client`
2. Reads each contact's "Monthly Retainer" custom field
3. Calculates:
   - Total MRR
   - MRR by service package (SEO, PPC, Social, etc.)
   - MRR by account manager
   - Client count
   - Average contract value
4. Generates `mrr-report-YYYY-MM-DD.csv` with breakdown
5. Generates `mrr-summary.md` with markdown-formatted summary

Bonus: Post summary to Slack via webhook when MRR drops >5% week-over-week.

---

## Integration Checkpoint

- [ ] Created Private App in GHL Marketplace
- [ ] Generated Access Token and stored in `.env`
- [ ] Verified API connection (200 response)
- [ ] Successfully created a contact via API
- [ ] Successfully read contacts via API
- [ ] Successfully updated a contact via API
- [ ] Understood pagination (fetched more than 100 contacts)
- [ ] Bulk imported from CSV without duplicates
- [ ] Retrieved custom field IDs
- [ ] Updated a custom field value via API
- [ ] Added tags to contacts via API

---

## Day 18 Recap Questions

1. What HTTP methods map to Create, Read, Update, Delete?
2. What's the difference between a Private App and a Marketplace/OAuth App?
3. Why should you never commit your API token to git?
4. How do you stay within the 100-requests-per-10-seconds rate limit?
5. Why use pagination instead of requesting all contacts at once?
6. If you get a 401 error, what's wrong?
7. If you get a 403 error, what's wrong?
8. Why use tag-based "archival" instead of deleting contacts?

---

## Next Day Preview

**Day 19: API for Calendars, Opportunities & Conversations** - Tomorrow you will work with the three most complex API surfaces: booking appointments, moving deals through pipelines, and sending SMS/emails programmatically. You'll also set up webhooks for real-time event handling.

Make sure you have:
- Your Private App and Access Token working
- At least 10 contacts in your sub-account (for testing pipeline operations)
- ngrok installed (for webhook testing): `brew install ngrok` or download from ngrok.com
