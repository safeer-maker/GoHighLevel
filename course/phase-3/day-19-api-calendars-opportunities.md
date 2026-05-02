# Day 19: GHL API - Calendars, Opportunities & Conversations

**Time Required:** 3-4 hours
**Level:** Expert

## Today's Mission
Yesterday you mastered contact CRUD via API. Today you tackle the three most complex API surfaces: Calendars (with time slots and timezone handling), Opportunities (with pipeline relationships), and Conversations (with message threading). You will build an appointment booking tool, a pipeline reporting script, and a conversation auto-responder - all in Python.

## Learning Objectives
1. List calendars and find available time slots via API
2. Create, update, and cancel appointments programmatically
3. Manage pipelines and move opportunities through stages
4. Send SMS and emails via the Conversations API
5. Set up webhooks for real-time event handling

---

## Part 1: Calendar API (60 min)

### What You Can Do

The Calendar API lets you:
- List all calendars in your sub-account
- Find free slots for booking
- Create/update/cancel appointments
- Mark appointments as showed/no-show

### Exercise 19.1: List Calendars

```python
import requests
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION

def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }

def list_calendars():
    """List all calendars."""
    url = f"{GHL_BASE_URL}/calendars/"
    params = {"locationId": GHL_LOCATION_ID}
    
    response = requests.get(url, headers=get_headers(), params=params)
    
    if response.status_code == 200:
        calendars = response.json().get("calendars", [])
        for c in calendars:
            print(f"{c.get('id')}: {c.get('name')} ({c.get('calendarType')})")
        return calendars
    return []
```

### Exercise 19.2: Find Free Slots for Sunrise Wellness PT Calendar

```python
from datetime import datetime, timedelta

def get_free_slots(calendar_id, days_ahead=7):
    """Get available slots for the next N days."""
    url = f"{GHL_BASE_URL}/calendars/{calendar_id}/free-slots"
    
    start = datetime.now()
    end = start + timedelta(days=days_ahead)
    
    params = {
        "startDate": start.strftime("%Y-%m-%d"),
        "endDate": end.strftime("%Y-%m-%d"),
    }
    
    response = requests.get(url, headers=get_headers(), params=params)
    
    if response.status_code == 200:
        slots = response.json().get("slots", {})
        print(f"Available slots in next {days_ahead} days:")
        for date, times in slots.items():
            if times:
                print(f"\n  {date}: {len(times)} slots")
                for t in times[:3]:
                    print(f"    {t}")
        return slots
    return {}
```

**Timezone note:** All times are returned in UTC. Convert to the business timezone before displaying to users.

### Exercise 19.3: Create an Appointment

```python
def create_appointment(calendar_id, contact_id, start_time_iso, end_time_iso, title=""):
    """Create an appointment on a calendar."""
    url = f"{GHL_BASE_URL}/calendars/events/appointments"
    
    payload = {
        "calendarId": calendar_id,
        "locationId": GHL_LOCATION_ID,
        "contactId": contact_id,
        "startTime": start_time_iso,  # ISO 8601: "2024-03-15T10:00:00-05:00"
        "endTime": end_time_iso,
        "title": title or "API-Created Appointment",
        "appointmentStatus": "confirmed",
    }
    
    response = requests.post(url, headers=get_headers(), json=payload)
    
    if response.status_code in [200, 201]:
        return response.json()
    print(f"Error: {response.text}")
    return None

# Example: Book David Kim for tomorrow 10am
tomorrow_10am = (datetime.now() + timedelta(days=1)).replace(hour=10, minute=0, second=0).isoformat()
tomorrow_11am = (datetime.now() + timedelta(days=1)).replace(hour=11, minute=0, second=0).isoformat()

create_appointment(
    calendar_id="YOUR_PT_CALENDAR_ID",
    contact_id="DAVID_KIM_CONTACT_ID",
    start_time_iso=tomorrow_10am,
    end_time_iso=tomorrow_11am,
    title="PT Session - David Kim"
)
```

### Exercise 19.4: Update Appointment Status

```python
def mark_appointment(event_id, status):
    """Mark appointment as showed, noshow, cancelled, or confirmed."""
    url = f"{GHL_BASE_URL}/calendars/events/appointments/{event_id}"
    response = requests.put(
        url, 
        headers=get_headers(),
        json={"appointmentStatus": status}
    )
    return response.status_code == 200

# Mark as showed after the session
mark_appointment("EVENT_ID", "showed")

# Or mark no-show
mark_appointment("EVENT_ID", "noshow")
```

### Exercise 19.5: Smart Booking Function

```python
def book_next_available_pt_slot(contact_id):
    """Find the next open PT slot and book the contact into it."""
    calendars = list_calendars()
    pt_calendar = next((c for c in calendars if "Personal Training" in c.get("name", "")), None)
    
    if not pt_calendar:
        print("PT calendar not found")
        return None
    
    slots = get_free_slots(pt_calendar["id"], days_ahead=14)
    
    for date, times in sorted(slots.items()):
        if times:
            start = times[0]
            # End = start + 60 minutes (parse and add)
            from dateutil import parser
            start_dt = parser.parse(start)
            end_dt = start_dt + timedelta(hours=1)
            
            return create_appointment(
                calendar_id=pt_calendar["id"],
                contact_id=contact_id,
                start_time_iso=start_dt.isoformat(),
                end_time_iso=end_dt.isoformat(),
                title="PT Session (auto-booked)"
            )
    
    print("No available slots in 14 days")
    return None
```

---

## Part 2: Opportunities API (60 min)

### Exercise 19.6: List Pipelines with Stages

```python
def list_pipelines():
    """List all pipelines with their stages."""
    url = f"{GHL_BASE_URL}/opportunities/pipelines"
    response = requests.get(url, headers=get_headers(), params={"locationId": GHL_LOCATION_ID})
    
    if response.status_code == 200:
        pipelines = response.json().get("pipelines", [])
        for p in pipelines:
            print(f"\nPipeline: {p.get('name')} (id: {p.get('id')})")
            for s in p.get("stages", []):
                print(f"  Stage: {s.get('name')} (id: {s.get('id')})")
        return pipelines
    return []
```

### Exercise 19.7: Create Opportunity in Membership Sales Pipeline

```python
def create_opportunity(pipeline_id, stage_id, contact_id, name, value):
    """Create an opportunity."""
    url = f"{GHL_BASE_URL}/opportunities/"
    payload = {
        "pipelineId": pipeline_id,
        "locationId": GHL_LOCATION_ID,
        "pipelineStageId": stage_id,
        "contactId": contact_id,
        "name": name,
        "monetaryValue": value,
        "status": "open",
    }
    
    response = requests.post(url, headers=get_headers(), json=payload)
    if response.status_code in [200, 201]:
        return response.json()
    print(f"Error: {response.text}")
    return None
```

### Exercise 19.8: Pipeline Report Script

```python
def pipeline_report(pipeline_id):
    """Generate a pipeline value report grouped by stage."""
    pipelines = list_pipelines()
    target = next((p for p in pipelines if p["id"] == pipeline_id), None)
    
    if not target:
        return
    
    print(f"\n{'='*60}")
    print(f"Pipeline: {target['name']}")
    print(f"{'='*60}\n")
    
    grand_total = 0
    
    for stage in target.get("stages", []):
        url = f"{GHL_BASE_URL}/opportunities/search"
        params = {
            "location_id": GHL_LOCATION_ID,
            "pipeline_id": pipeline_id,
            "pipeline_stage_id": stage["id"],
            "limit": 100,
        }
        
        response = requests.get(url, headers=get_headers(), params=params)
        opps = response.json().get("opportunities", [])
        
        total = sum(o.get("monetaryValue", 0) for o in opps)
        grand_total += total
        
        print(f"  {stage['name']:25} {len(opps):3} deals   ${total:>10,.2f}")
    
    print(f"\n  {'TOTAL':25}         ${grand_total:>10,.2f}")
```

### Exercise 19.9: Stage Mover - Auto-Advance Stale Opps

```python
from datetime import datetime, timedelta

def advance_stale_trial_deals():
    """Move opportunities from 'Trial Active' to 'Trial Follow-Up' if in stage 5+ days."""
    # Get pipeline and stage IDs
    pipelines = list_pipelines()
    sales = next((p for p in pipelines if "Membership Sales" in p["name"]), None)
    
    if not sales:
        return
    
    trial_active = next((s for s in sales["stages"] if "Trial Active" in s["name"]), None)
    trial_followup = next((s for s in sales["stages"] if "Trial Follow-Up" in s["name"]), None)
    
    # Search for opps in Trial Active
    params = {
        "location_id": GHL_LOCATION_ID,
        "pipeline_id": sales["id"],
        "pipeline_stage_id": trial_active["id"],
        "limit": 100,
    }
    response = requests.get(f"{GHL_BASE_URL}/opportunities/search", headers=get_headers(), params=params)
    opps = response.json().get("opportunities", [])
    
    cutoff = datetime.now() - timedelta(days=5)
    moved = 0
    
    for opp in opps:
        updated_at = datetime.fromisoformat(opp.get("updatedAt", "").replace("Z", "+00:00"))
        if updated_at < cutoff:
            # Move to Trial Follow-Up
            url = f"{GHL_BASE_URL}/opportunities/{opp['id']}"
            requests.put(url, headers=get_headers(), json={"pipelineStageId": trial_followup["id"]})
            moved += 1
    
    print(f"Moved {moved} stale Trial Active opps to Trial Follow-Up")
```

---

## Part 3: Conversations API (45 min)

### Exercise 19.10: Send SMS

```python
def send_sms(contact_id, message):
    """Send SMS to a contact."""
    url = f"{GHL_BASE_URL}/conversations/messages"
    payload = {
        "type": "SMS",
        "contactId": contact_id,
        "message": message,
    }
    response = requests.post(url, headers=get_headers(), json=payload)
    return response.status_code == 200
```

### Exercise 19.11: Send Email

```python
def send_email(contact_id, subject, html_body):
    """Send email to a contact."""
    url = f"{GHL_BASE_URL}/conversations/messages"
    payload = {
        "type": "Email",
        "contactId": contact_id,
        "subject": subject,
        "html": html_body,
    }
    response = requests.post(url, headers=get_headers(), json=payload)
    return response.status_code == 200
```

### Exercise 19.12: Bulk Welcome Email Sender

```python
import time

def send_bulk_welcome_to_new_leads():
    """Send welcome email to all contacts tagged 'new-trial-lead' from last 24 hours."""
    url = f"{GHL_BASE_URL}/contacts/"
    params = {"locationId": GHL_LOCATION_ID, "limit": 100}
    response = requests.get(url, headers=get_headers(), params=params)
    contacts = response.json().get("contacts", [])
    
    yesterday = datetime.now() - timedelta(hours=24)
    new_leads = [
        c for c in contacts
        if "new-trial-lead" in c.get("tags", [])
        and datetime.fromisoformat(c.get("dateAdded", "").replace("Z", "+00:00")) > yesterday
    ]
    
    print(f"Sending welcome to {len(new_leads)} new leads")
    
    html_template = """
    <h1>Welcome to Sunrise Wellness Studio, {{first_name}}!</h1>
    <p>Thanks for requesting your free trial. Your 7-day pass is ready!</p>
    <p><a href="https://yourcalendar.com">Book your first session</a></p>
    """
    
    for lead in new_leads:
        personalized = html_template.replace("{{first_name}}", lead.get("firstName", "there"))
        send_email(
            lead["id"],
            f"Welcome to Sunrise Wellness, {lead.get('firstName', 'there')}!",
            personalized
        )
        time.sleep(0.5)
    
    print(f"Sent {len(new_leads)} welcome emails")
```

### Exercise 19.13: Keyword Auto-Responder Bot

```python
def keyword_responder(conversation_id, message_body, contact_id):
    """Respond to common keywords in inbound messages."""
    msg_lower = message_body.lower()
    
    responses = {
        "hours": "Sunrise Wellness is open Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM.",
        "price": "We have 3 membership tiers: Basic $79/mo, Premium $149/mo, VIP $249/mo. Try us free with a 7-day trial!",
        "schedule": "View our class schedule here: [schedule_link]. Book online or reply CLASS NAME to book.",
        "trial": "Great! Book your free 7-day trial here: [trial_link]",
        "cancel": "We're sorry to hear that. Can we help you with anything first? Reply YES to talk to our team.",
    }
    
    for keyword, reply in responses.items():
        if keyword in msg_lower:
            send_sms(contact_id, reply)
            return True
    
    # No keyword matched - create task for human review
    return False
```

---

## Part 4: Webhooks - Real-Time Events (45 min)

### What Are Webhooks?

Webhooks are the inverse of APIs. Instead of you asking GHL "what changed?", GHL proactively POSTs to your server when something happens.

### Exercise 19.14: Build webhook_server.py

```python
# scripts/webhook_server.py
from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/webhook/ghl", methods=["POST"])
def ghl_webhook():
    """Receive webhook events from GHL."""
    data = request.json
    event_type = data.get("type", "unknown")
    timestamp = datetime.now().isoformat()
    
    print(f"\n[{timestamp}] Event: {event_type}")
    print(f"  Data: {json.dumps(data, indent=2)[:500]}")
    
    # Route based on event type
    if event_type == "ContactCreate":
        handle_new_contact(data)
    elif event_type == "AppointmentCreate":
        handle_new_appointment(data)
    elif event_type == "OpportunityStageUpdate":
        handle_stage_change(data)
    
    # Always return 200 quickly
    return jsonify({"received": True, "type": event_type}), 200


def handle_new_contact(data):
    contact = data.get("contact", {})
    name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}"
    print(f"  NEW CONTACT: {name}")
    # TODO: Log to database, notify Slack, etc.


def handle_new_appointment(data):
    appt = data.get("appointment", {})
    print(f"  NEW APPOINTMENT: {appt.get('title')}")


def handle_stage_change(data):
    opp = data.get("opportunity", {})
    print(f"  STAGE CHANGE: {opp.get('name')} -> {opp.get('pipelineStageId')}")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    print("Webhook server starting on http://localhost:5000")
    print("Endpoint: POST /webhook/ghl")
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Exercise 19.15: Expose with ngrok

```bash
# Terminal 1: Run Flask
pip install flask
python webhook_server.py

# Terminal 2: Expose with ngrok
ngrok http 5000

# Copy the ngrok URL: https://abc123.ngrok-free.app
```

### Exercise 19.16: Connect GHL to Your Webhook

1. In GHL, go to Automation > Workflows
2. Create workflow with trigger: "Contact Created"
3. Add action: "Webhook"
4. URL: `https://YOUR-NGROK-URL.ngrok-free.app/webhook/ghl`
5. Method: POST
6. Send a test event
7. Watch your Flask server receive it

---

## Part 5: Error Handling & Retry Logic (30 min)

### Exercise 19.17: Wrap API Calls with Retry

```python
import time
from functools import wraps

def with_retry(max_retries=3, base_delay=1):
    """Retry decorator with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except requests.exceptions.RequestException as e:
                    last_error = e
                    if attempt < max_retries - 1:
                        delay = base_delay * (2 ** attempt)
                        print(f"Attempt {attempt+1} failed, retrying in {delay}s...")
                        time.sleep(delay)
            
            print(f"All {max_retries} attempts failed")
            raise last_error
        return wrapper
    return decorator

# Use it:
@with_retry(max_retries=3)
def robust_create_contact(*args, **kwargs):
    return create_contact(*args, **kwargs)
```

### Rate Limit Handling

```python
def api_call_with_rate_limit(url, method="GET", **kwargs):
    """Handle 429 rate limit responses."""
    while True:
        response = requests.request(method, url, headers=get_headers(), **kwargs)
        
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 10))
            print(f"Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
            continue
        
        return response
```

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental "Tomorrow's Appointments" Script

**Situation:** Every morning, each dentist should get an email of their upcoming appointments for the day.

**Your Task:** Build `daily_schedule.py` that:
1. Pulls all calendars for BrightSmile Dental
2. For each calendar, gets appointments for TODAY
3. Groups appointments by assigned dentist
4. For each dentist, sends email via GHL Conversations API:
   - Subject: "Your Schedule for [DATE]"
   - Body: List of appointments with patient name, time, procedure
5. Run via cron at 7am daily

### Case Scenario 2: Elevate Digital Agency Client Health Dashboard

**Situation:** Agency owner wants daily visibility into client health metrics.

**Your Task:** Build `client_health.py` that:
1. Fetches all contacts tagged `active-client`
2. For each client:
   - Last conversation date
   - Current pipeline stage (Onboarding/Active/At-Risk)
   - Days since last communication
3. Output markdown report flagging:
   - Red: No contact in 14+ days
   - Yellow: No contact in 7-13 days
   - Green: Recent contact
4. Email report to agency owner daily

---

## Integration Checkpoint

- [ ] Listed all calendars via API
- [ ] Retrieved free slots for a calendar
- [ ] Created an appointment via API
- [ ] Updated appointment status (showed/noshow)
- [ ] Listed pipelines with stages
- [ ] Created an opportunity
- [ ] Built a pipeline report script
- [ ] Sent SMS via API
- [ ] Sent email via API
- [ ] Set up webhook server (Flask + ngrok)
- [ ] Received test webhook event
- [ ] Wrapped calls with retry logic

---

## Day 19 Recap Questions

1. What format must `startTime` be in for creating appointments? (ISO 8601)
2. What are the 4 valid appointment statuses?
3. How do you find a pipeline stage ID?
4. Why is webhook processing different from API calls (who initiates)?
5. What HTTP status code indicates rate limiting? (429)
6. What's exponential backoff and why use it?

## Next Day Preview

**Day 20: Custom Integrations** - Connect GHL to Google Sheets, build a reporting dashboard, and implement a lead scoring system via webhooks.
