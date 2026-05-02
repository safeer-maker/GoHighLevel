# Day 20: Workflows, Campaigns & Custom Integrations

**Time Required:** 3-4 hours
**Level:** Expert

## Today's Mission
Sunrise Wellness runs in GHL, but real businesses run on multiple tools. Today you connect GHL to the outside world: trigger workflows via webhooks, sync data to Google Sheets, build a reporting dashboard with Flask, and implement a lead scoring system. By end of today, GHL becomes one node in a larger automated ecosystem.

## Learning Objectives
1. Trigger GHL workflows externally via inbound webhooks
2. Build a Flask server to receive outbound GHL webhooks
3. Sync GHL data to Google Sheets automatically
4. Create a live reporting dashboard
5. Implement custom lead scoring with API

---

## Part 1: Triggering GHL Workflows via API (45 min)

### Inbound Webhook Triggers

GHL workflows can be triggered by HTTP POST requests. Perfect for:
- External form submissions
- Third-party systems signaling events
- Scheduled triggers from your scripts

### Exercise 20.1: Create Inbound Webhook Workflow

1. In GHL: Automation > Workflows > + Create Workflow
2. Trigger: "Inbound Webhook"
3. GHL generates a unique URL like: `https://services.leadconnectorhq.com/hooks/abc123...`
4. Copy this URL
5. Actions: Send SMS "Welcome from webhook trigger!" + Add tag "webhook-triggered"
6. Save and activate

### Exercise 20.2: Trigger It with Python

```python
import requests

WEBHOOK_URL = "YOUR_GHL_INBOUND_WEBHOOK_URL"

def trigger_welcome_workflow(first_name, email, phone):
    """Trigger the GHL workflow externally."""
    payload = {
        "first_name": first_name,
        "last_name": "From External",
        "email": email,
        "phone": phone,
        "custom_field_1": "Value from your system",
    }
    
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        print(f"Triggered workflow for {email}")
    else:
        print(f"Error: {response.status_code}")

trigger_welcome_workflow("External", "external@yopmail.com", "+12024567100")
```

Watch the workflow execution log in GHL - you'll see it fired with your data.

---

## Part 2: Outbound Webhooks from GHL (60 min)

### Exercise 20.3: Flask Webhook Server with Multiple Routes

```python
# scripts/webhook_server.py
from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
LOG_FILE = "webhook-events.log"

def log_event(event_type, data):
    """Append event to log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{datetime.now().isoformat()}] {event_type}\n")
        f.write(json.dumps(data, indent=2))
        f.write("\n" + "="*60 + "\n")

@app.route("/webhook/new-lead", methods=["POST"])
def new_lead():
    """Handle new lead events."""
    data = request.json
    contact = data.get("contact", {})
    
    log_event("new-lead", data)
    
    # Simulate Slack notification
    print(f"🔔 NEW LEAD: {contact.get('firstName')} {contact.get('lastName')}")
    print(f"   Email: {contact.get('email')}")
    print(f"   Source: {contact.get('source', 'unknown')}")
    
    return jsonify({"received": True}), 200

@app.route("/webhook/payment", methods=["POST"])
def payment_received():
    """Log payments to revenue file."""
    data = request.json
    log_event("payment", data)
    
    # Update local revenue log
    amount = data.get("amount", 0)
    with open("revenue-log.json", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "amount": amount,
            "contact": data.get("contact", {}).get("email"),
        }) + "\n")
    
    print(f"💰 PAYMENT: ${amount}")
    return jsonify({"received": True}), 200

@app.route("/webhook/appointment", methods=["POST"])
def appointment_event():
    """Handle appointment events."""
    data = request.json
    appt = data.get("appointment", {})
    log_event("appointment", data)
    
    print(f"📅 APPOINTMENT: {appt.get('title')} at {appt.get('startTime')}")
    return jsonify({"received": True}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "time": datetime.now().isoformat()}), 200

if __name__ == "__main__":
    print("Webhook server: http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Exercise 20.4: Connect GHL Workflows to Your Webhooks

For each endpoint:

**New Lead Webhook:**
- Trigger: "Contact Created"
- Action: "Webhook" with URL `https://YOUR-NGROK-URL/webhook/new-lead`

**Payment Webhook:**
- Trigger: "Payment Received"
- Action: "Webhook" to `/webhook/payment`

**Appointment Webhook:**
- Trigger: "Appointment Created"
- Action: "Webhook" to `/webhook/appointment`

Test each by creating a contact, appointment, or marking an invoice paid.

### Securing Webhooks

Anyone who knows your webhook URL can send data. Secure it:

```python
import hmac
import hashlib

WEBHOOK_SECRET = "your-secret-token"

@app.route("/webhook/secure", methods=["POST"])
def secure_webhook():
    # Option 1: Check for custom header
    token = request.headers.get("X-Webhook-Token")
    if token != WEBHOOK_SECRET:
        return jsonify({"error": "Unauthorized"}), 401
    
    # Process...
    return jsonify({"received": True}), 200
```

In GHL workflow webhook action, add header `X-Webhook-Token: your-secret-token`.

---

## Part 3: GHL ↔ Google Sheets Integration (45 min)

### Why Google Sheets?

Many clients live in Sheets. They want their GHL data there for:
- Custom reports
- Leadership dashboards
- Data team analysis

### Exercise 20.5: Set Up Google Sheets API

```bash
pip install gspread google-auth
```

1. Go to https://console.cloud.google.com/
2. Create a project, enable Google Sheets API
3. Create a service account
4. Download the credentials JSON file
5. Share your target Google Sheet with the service account email (as editor)

### Exercise 20.6: Export Members to Sheet

```python
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS_FILE = "google-creds.json"
SPREADSHEET_ID = "your-sheet-id"

def export_members_to_sheet():
    """Pull all active members, write to Google Sheet."""
    # 1. Get data from GHL
    contacts = list_all_contacts()  # From Day 18
    active_members = [c for c in contacts if "active-member" in c.get("tags", [])]
    
    # 2. Connect to Google Sheets
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.sheet1
    
    # 3. Clear and write data
    worksheet.clear()
    headers = ["Name", "Email", "Phone", "Membership", "Join Date", "Monthly Rate"]
    worksheet.append_row(headers)
    
    for m in active_members:
        row = [
            f"{m.get('firstName', '')} {m.get('lastName', '')}",
            m.get("email", ""),
            m.get("phone", ""),
            # Get membership type from custom fields
            next((cf.get("value") for cf in m.get("customFields", []) if "Membership Type" in str(cf)), ""),
            "",  # Join date
            "",  # Monthly rate
        ]
        worksheet.append_row(row)
    
    print(f"Exported {len(active_members)} members to sheet")

# Schedule with cron: 0 7 * * * python /path/to/export.py
```

---

## Part 4: Reporting Dashboard (60 min)

### Exercise 20.7: Flask + HTML Dashboard

```python
# scripts/dashboard.py
from flask import Flask, render_template_string
from datetime import datetime, timedelta
import requests
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION

app = Flask(__name__)

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sunrise Wellness Dashboard</title>
    <style>
        body { font-family: -apple-system, sans-serif; max-width: 1200px; margin: 40px auto; padding: 20px; }
        h1 { color: #FF6B35; }
        .metric-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0; }
        .metric-card { background: #f9f9f9; padding: 20px; border-radius: 8px; border-left: 4px solid #FF6B35; }
        .metric-value { font-size: 2em; font-weight: bold; color: #FF6B35; }
        .metric-label { color: #666; margin-top: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #FF6B35; color: white; }
    </style>
</head>
<body>
    <h1>🌅 Sunrise Wellness Dashboard</h1>
    <p>Last updated: {{ updated }}</p>
    
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">{{ new_leads_today }}</div>
            <div class="metric-label">New Leads Today</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{{ appointments_today }}</div>
            <div class="metric-label">Today's Appointments</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${{ pipeline_value }}</div>
            <div class="metric-label">Pipeline Value</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${{ mrr }}</div>
            <div class="metric-label">Monthly Recurring Revenue</div>
        </div>
    </div>
    
    <h2>Pipeline by Stage</h2>
    <table>
        <tr><th>Stage</th><th>Count</th><th>Value</th></tr>
        {% for stage in stages %}
        <tr><td>{{ stage.name }}</td><td>{{ stage.count }}</td><td>${{ stage.value }}</td></tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }

def get_metrics():
    # New leads today
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    contacts_resp = requests.get(
        f"{GHL_BASE_URL}/contacts/",
        headers=get_headers(),
        params={"locationId": GHL_LOCATION_ID, "limit": 100}
    )
    contacts = contacts_resp.json().get("contacts", [])
    
    new_today = sum(1 for c in contacts 
                    if datetime.fromisoformat(c.get("dateAdded", "").replace("Z", "+00:00")) > today)
    
    # Pipeline
    pipelines_resp = requests.get(
        f"{GHL_BASE_URL}/opportunities/pipelines",
        headers=get_headers(),
        params={"locationId": GHL_LOCATION_ID}
    )
    pipelines = pipelines_resp.json().get("pipelines", [])
    
    stages = []
    total_pipeline = 0
    if pipelines:
        sales = pipelines[0]
        for s in sales.get("stages", []):
            opps_resp = requests.get(
                f"{GHL_BASE_URL}/opportunities/search",
                headers=get_headers(),
                params={
                    "location_id": GHL_LOCATION_ID,
                    "pipeline_id": sales["id"],
                    "pipeline_stage_id": s["id"],
                }
            )
            opps = opps_resp.json().get("opportunities", [])
            value = sum(o.get("monetaryValue", 0) for o in opps)
            total_pipeline += value
            stages.append({"name": s["name"], "count": len(opps), "value": f"{value:,.0f}"})
    
    # MRR calculation (simplified)
    active_members = [c for c in contacts if "active-member" in c.get("tags", [])]
    mrr = len(active_members) * 149  # Assume average
    
    return {
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "new_leads_today": new_today,
        "appointments_today": 0,  # TODO: Implement calendar lookup
        "pipeline_value": f"{total_pipeline:,.0f}",
        "mrr": f"{mrr:,.0f}",
        "stages": stages,
    }

@app.route("/")
def dashboard():
    metrics = get_metrics()
    return render_template_string(DASHBOARD_TEMPLATE, **metrics)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
```

Visit http://localhost:5001 - you'll see a live dashboard pulling from GHL.

---

## Part 5: Lead Scoring System (30 min)

### Exercise 20.8: Lead Scorer

```python
# scripts/lead_scorer.py
import requests
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION

def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }

SCORING_RULES = {
    "has_phone": 10,
    "has_fitness_goals": 10,
    "interested_pt": 20,
    "interested_nutrition": 15,
    "interested_classes": 15,
    "trial_booked": 40,
    "trial_showed": 30,
}

def calculate_score(contact):
    """Calculate lead score based on attributes/tags."""
    score = 0
    tags = contact.get("tags", [])
    
    if contact.get("phone"):
        score += SCORING_RULES["has_phone"]
    
    # Check custom fields for fitness goals
    custom_fields = contact.get("customFields", [])
    has_goals = any("goal" in str(cf).lower() for cf in custom_fields)
    if has_goals:
        score += SCORING_RULES["has_fitness_goals"]
    
    # Tag-based scoring
    if "interested-personal-training" in tags:
        score += SCORING_RULES["interested_pt"]
    if "interested-nutrition" in tags:
        score += SCORING_RULES["interested_nutrition"]
    if "interested-group-classes" in tags:
        score += SCORING_RULES["interested_classes"]
    if "trial-booked" in tags:
        score += SCORING_RULES["trial_booked"]
    if "trial-showed" in tags:
        score += SCORING_RULES["trial_showed"]
    
    return score

def score_all_leads():
    """Score all leads and tag hot ones."""
    url = f"{GHL_BASE_URL}/contacts/"
    params = {"locationId": GHL_LOCATION_ID, "limit": 100}
    response = requests.get(url, headers=get_headers(), params=params)
    contacts = response.json().get("contacts", [])
    
    leads = [c for c in contacts if "new-trial-lead" in c.get("tags", []) 
             and "active-member" not in c.get("tags", [])]
    
    print(f"Scoring {len(leads)} leads")
    
    for lead in leads:
        score = calculate_score(lead)
        
        # Tag hot leads (70+)
        if score >= 70 and "hot-lead" not in lead.get("tags", []):
            tags_url = f"{GHL_BASE_URL}/contacts/{lead['id']}/tags"
            requests.post(tags_url, headers=get_headers(), json={"tags": ["hot-lead"]})
            print(f"  🔥 HOT LEAD: {lead.get('firstName')} ({score} pts)")
        elif score >= 40:
            print(f"  🟡 Warm: {lead.get('firstName')} ({score} pts)")
        else:
            print(f"  🔵 Cold: {lead.get('firstName')} ({score} pts)")

# Run daily via cron
if __name__ == "__main__":
    score_all_leads()
```

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental Treatment History Export

Build integration that pushes completed dental treatment records to a "Treatment History" Google Sheet. Each row: Patient, Date, Procedure, Dentist, Cost, Insurance Status. Run nightly.

### Case Scenario 2: Elevate Digital Agency Client Portal Sync

Build a REST API endpoint (Flask) that clients can query to see their own data from GHL. Endpoint: `GET /client/<client_id>/summary` returns: current contract value, monthly report date, recent conversations count, open tasks. Secured with API key per client.

---

## Integration Checkpoint

- [ ] Created inbound webhook workflow in GHL
- [ ] Triggered it externally via Python
- [ ] Flask webhook server receives GHL events
- [ ] Webhook events logged to file
- [ ] Google Sheets integration working
- [ ] Dashboard displays live GHL data
- [ ] Lead scorer tags hot leads (70+)

## Day 20 Recap Questions
1. What's an inbound webhook trigger?
2. How do you secure a webhook endpoint?
3. Why sync to Google Sheets?
4. What's lead scoring and why is it useful?

## Next Day Preview
**Day 21: AI Agents in GHL** - Build a 24/7 AI receptionist using GHL's AI Employee feature.
