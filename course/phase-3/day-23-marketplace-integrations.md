# Day 23: App Marketplace & Advanced Integrations

**Time Required:** 3-4 hours
**Level:** Expert

## Today's Mission
GHL doesn't exist in a vacuum. Today you explore the App Marketplace, connect native integrations (Google, Facebook, Stripe), and build a custom integration chaining 3 tools together. You'll also learn white-label basics - how agencies rebrand GHL for clients. This is the final day of Phase 3 before certification prep begins.

## Learning Objectives
1. Navigate and install apps from the GHL Marketplace
2. Connect native integrations (Google, Facebook, Stripe)
3. Build a custom integration chaining 3 tools
4. Understand white-label basics from sub-account view
5. Apply integration best practices

---

## Part 1: App Marketplace Overview (30 min)

### What is the GHL Marketplace?

The Marketplace is GHL's app store. Agencies and developers build apps that extend GHL's functionality. Categories include:
- Communication enhancers
- Reporting and analytics
- Industry-specific tools
- AI and automation
- Integration connectors

### Exercise 23.1: Browse the Marketplace

1. Navigate to **App Marketplace** in your sub-account
2. Explore these categories:
   - **Messaging:** Advanced SMS tools, WhatsApp extensions
   - **CRM:** Contact enrichment, deduplication tools
   - **Reporting:** Custom dashboards, analytics
   - **Industry:** Real estate, fitness, healthcare specific
   - **AI:** Chat bots, content generators
3. Find 3 apps useful for Sunrise Wellness. Document:
   - App name
   - What it does
   - Free or paid
   - User rating

### Pre-Install Checklist

Before installing ANY app:
- [ ] Read reviews (4+ stars, 10+ reviews)
- [ ] Check developer (established agency vs unknown)
- [ ] Review permissions requested (does it need access to data it shouldn't?)
- [ ] Check pricing model (free? freemium? per-contact?)
- [ ] Check uninstall impact (does removing break anything?)
- [ ] Verify GDPR/HIPAA compliance if relevant

---

## Part 2: Native Integrations (60 min)

### The Big Six Native Integrations

These integrations are built into GHL (no marketplace app needed):

| Integration | What It Enables |
|-------------|----------------|
| **Google** | Gmail, Calendar, Google Business Profile, Analytics, Ads |
| **Facebook/Meta** | Pages, Ads, Lead Forms, Messenger, Instagram |
| **Stripe** | Payment processing |
| **QuickBooks** | Accounting sync |
| **Zoom/Google Meet** | Video calls on appointments |
| **Twilio** | Advanced SMS/voice |

### Exercise 23.2: Connect Google Calendar

1. Settings > Integrations > Google
2. Click Connect
3. Authorize via Google OAuth
4. Select which calendar(s) to sync
5. Enable 2-way sync:
   - GHL appointments appear in Google Calendar
   - Google Calendar busy time blocks GHL availability

**Verify:** Book an appointment in GHL, check Google Calendar. Block time in Google Calendar, verify GHL hides that slot.

### Exercise 23.3: Connect Facebook Page for Messenger

1. Settings > Integrations > Facebook
2. Connect to your Facebook Business page
3. Enable Messenger integration
4. Test: Send a message to your FB page, verify it appears in GHL Conversations

**For Sunrise Wellness:** This means members messaging your FB page get replied to from GHL like any other channel.

### Exercise 23.4: Stripe Connection (Document If Unavailable)

If Stripe isn't connected on your practice sub-account:

1. Document the connection process:
   - Settings > Payments > Connect Stripe
   - OAuth to Stripe account
   - Select products to sync
   - Verify webhook receivers configured

2. Understand what it enables:
   - Live payment processing on order forms
   - Auto-billing recurring subscriptions
   - Failed payment handling
   - Refund management

### Exercise 23.5: Zoom/Google Meet Integration

1. Settings > Integrations > Zoom (or Google Meet)
2. Connect your account
3. Edit a calendar (e.g., Nutrition Consultation)
4. Set appointment type to "Zoom Meeting"
5. Book an appointment
6. Verify: Email contains Zoom link automatically

**For Sunrise Wellness:** Virtual nutrition consultations need this. Let remote clients book and receive meeting links automatically.

---

## Part 3: Install and Test a Free App (30 min)

### Exercise 23.6: Install a Marketplace App

1. In Marketplace, find a free app with good reviews
   - Suggestions: A review aggregator, a task management enhancer
2. Read the install instructions
3. Click Install
4. Grant permissions
5. Configure the app's settings
6. Test its functionality
7. Document: What did it add? Is it useful? Would you pay for it?

**Pro Tip:** Install apps on a test account first. Some apps add custom fields or tags that pollute data.

---

## Part 4: Build a 3-Tool Custom Integration (90 min)

### The Scenario

**Sunrise Wellness needs:** When a new PT session is booked, automatically:
1. Create a Zoom meeting
2. Send SMS with Zoom link to the member
3. Log the booking in a Google Sheet for reporting

### Exercise 23.7: Architecture Design

```
[GHL Workflow]
    |
    Trigger: Appointment Booked (PT calendar)
    |
    Action: HTTP Request to our Flask middleware
    |
    v
[Flask Middleware Server]
    |
    +---> [Zoom API]
    |       POST /users/me/meetings
    |       Create meeting, return URL
    |
    +---> [GHL API]
    |       POST /conversations/messages
    |       Send SMS with Zoom link
    |
    +---> [Google Sheets API]
            Append row to "PT Bookings" sheet
```

### Exercise 23.8: Build the Flask Middleware

```python
# scripts/integration_server.py
from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Config (use .env in production)
GHL_API_KEY = os.getenv("GHL_API_KEY")
ZOOM_JWT_TOKEN = os.getenv("ZOOM_JWT_TOKEN")  # Or OAuth
GOOGLE_SHEETS_CREDS = "google-creds.json"
SHEET_ID = "your-sheet-id"

@app.route("/webhook/pt-booked", methods=["POST"])
def handle_pt_booking():
    """Chain: GHL → Zoom → SMS → Sheets."""
    data = request.json
    appointment = data.get("appointment", {})
    contact = data.get("contact", {})
    
    print(f"New PT booking: {contact.get('firstName')}")
    
    # 1. Create Zoom meeting
    zoom_url = create_zoom_meeting(
        topic=f"PT Session - {contact.get('firstName')}",
        start_time=appointment.get("startTime"),
        duration_minutes=60
    )
    
    if not zoom_url:
        return jsonify({"error": "Zoom creation failed"}), 500
    
    # 2. Send SMS via GHL API
    sms_sent = send_sms_with_zoom_link(
        contact_id=contact.get("id"),
        zoom_url=zoom_url,
        appointment_time=appointment.get("startTime")
    )
    
    # 3. Log to Google Sheets
    log_to_sheets(
        member_name=f"{contact.get('firstName')} {contact.get('lastName')}",
        email=contact.get("email"),
        appointment_time=appointment.get("startTime"),
        zoom_url=zoom_url
    )
    
    return jsonify({
        "zoom_url": zoom_url,
        "sms_sent": sms_sent,
        "logged": True
    }), 200


def create_zoom_meeting(topic, start_time, duration_minutes):
    """Create a Zoom meeting via API."""
    url = "https://api.zoom.us/v2/users/me/meetings"
    headers = {
        "Authorization": f"Bearer {ZOOM_JWT_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "topic": topic,
        "type": 2,  # Scheduled meeting
        "start_time": start_time,
        "duration": duration_minutes,
        "settings": {
            "host_video": True,
            "participant_video": True,
            "join_before_host": False,
            "waiting_room": True
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return response.json().get("join_url")
    print(f"Zoom error: {response.text}")
    return None


def send_sms_with_zoom_link(contact_id, zoom_url, appointment_time):
    """Send SMS via GHL API."""
    url = "https://services.leadconnectorhq.com/conversations/messages"
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }
    
    message = f"Your PT session at Sunrise Wellness is confirmed! Join via Zoom at {appointment_time}: {zoom_url}"
    
    payload = {
        "type": "SMS",
        "contactId": contact_id,
        "message": message
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code == 200


def log_to_sheets(member_name, email, appointment_time, zoom_url):
    """Append row to Google Sheets."""
    import gspread
    from google.oauth2.service_account import Credentials
    
    creds = Credentials.from_service_account_file(
        GOOGLE_SHEETS_CREDS,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    gc = gspread.authorize(creds)
    sheet = gc.open_by_key(SHEET_ID).sheet1
    
    sheet.append_row([
        datetime.now().isoformat(),
        member_name,
        email,
        appointment_time,
        zoom_url
    ])


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(port=5002, debug=True)
```

### Exercise 23.9: Connect GHL Workflow

1. Expose your server with ngrok: `ngrok http 5002`
2. In GHL, create workflow:
   - Trigger: "Appointment Created" (filtered to PT calendar)
   - Action: "Webhook" HTTP POST to `https://YOUR-NGROK/webhook/pt-booked`
3. Include contact and appointment data in the payload
4. Save and activate

### Exercise 23.10: Test End-to-End

1. Book a test PT appointment
2. Watch your Flask server logs
3. Verify:
   - Zoom meeting created (check Zoom dashboard)
   - SMS received (check GHL conversations or phone)
   - Row added to Google Sheet

**Debugging checklist:**
- Flask server running?
- ngrok URL still valid (ngrok URLs expire)?
- Zoom token not expired?
- Google Sheets service account has access to sheet?
- GHL workflow actually triggering?

---

## Part 5: Zapier/Make vs Custom Integration (30 min)

### When to Use Each

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **Zapier** | Easy, no code, many integrations | $$ at scale, slower, limits | MVPs, non-technical users |
| **Make.com** | More flexible than Zapier, cheaper at scale | Steeper learning curve | Complex multi-step flows |
| **Custom Code** | Maximum flexibility, fastest, cheapest long-term | Requires developer time | Unique requirements, high volume |

### Exercise 23.11: Build a Zap (If You Have Zapier Access)

Build: When new GHL contact → Add row to Airtable + Send Slack notification

1. Zap Trigger: GHL "New Contact"
2. Action 1: Airtable "Create Record"
3. Action 2: Slack "Send Channel Message"

**What Zapier does well:** Quick, visual, reliable for simple 1-1 or 1-2 flows.

**What Zapier struggles with:** Complex conditional logic, high volume (gets expensive), unique business logic.

---

## Part 6: White-Label Basics (30 min)

### What Is White-Label?

Agencies resell GHL to their clients under their own brand. The client sees "YourAgency.com" - not "GoHighLevel.com" - throughout their experience.

### White-Label Touchpoints (Memorize for Certification!)

| Touchpoint | What's White-Labeled |
|-----------|---------------------|
| **Login Domain** | app.youragency.com instead of app.gohighlevel.com |
| **API Domain** | api.youragency.com |
| **Email Domain** | notifications from @youragency.com |
| **Mobile App** | Agency's logo, name in app stores |
| **Support Widget** | Agency support instead of GHL support |
| **Client-Facing Emails** | Invoices, receipts from agency brand |
| **Zap URL** | Zapier integration branded |

### Exercise 23.12: Audit Your Account's White-Label

1. Note the URL you use to log in - is it custom or default?
2. Check an email sent FROM your sub-account - what's the sender?
3. Check client-facing pages (funnels, calendars) - any GHL branding?
4. Note what IS and IS NOT white-labeled

**For certification:** Understand that as a sub-account user, your experience depends on what your agency has configured. Agency admins have control over all touchpoints.

### Sub-Account vs Agency Perspective

**As sub-account user (you):**
- See what agency configured
- Can use white-labeled resources
- Cannot change white-label settings

**As agency admin (future you):**
- Configure every touchpoint
- Maintain DNS records for domains
- Provide branded support to clients

---

## Part 7: Integration Best Practices (30 min)

### Idempotency

**Idempotent** = safe to retry. Running twice has same result as running once.

**Bad:** "Add contact to list" - running twice adds duplicates
**Good:** "Set contact's list membership" - running twice = same state

For GHL integrations:
- Use "upsert" patterns (update if exists, create if not)
- Check for existing records before creating
- Use unique identifiers (email, phone) for dedup

### Error Handling

```python
def safe_api_call(func, *args, max_retries=3, **kwargs):
    """Retry with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                # Log to error tracking (Sentry, etc.)
                print(f"All retries failed: {e}")
                raise
```

### Monitoring

Every production integration needs:
- **Logs** - What happened, when
- **Alerts** - Notify when something breaks
- **Health checks** - Is the service running?
- **Metrics** - How many calls, how many failures?

### Documentation

For every integration, document:
- What it does
- What tools it connects
- Credentials needed (where stored)
- How to restart if crashed
- Who to call if breaks

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental 3-Tool Integration

**Build:** When a dental appointment is booked:
1. Create Google Calendar event in the assigned dentist's calendar
2. Post to internal Slack channel #appointments for team awareness
3. Send SMS confirmation to patient with directions

**Architecture:**
```
GHL Workflow (Appointment Created)
    ↓
Flask Middleware
    ├→ Google Calendar API (create event)
    ├→ Slack Webhook (post message)
    └→ GHL API (send SMS with Google Maps link)
```

Sketch the code, identify tools/credentials needed, and document the error recovery plan.

### Case Scenario 2: Elevate Digital Agency Client Reporting

**Build:** Monthly automated client reports combining multiple data sources.

Architecture:
```
Cron Job (1st of month)
    ↓
Python Report Generator
    ├→ GHL API (contacts, conversations, opportunities for this client)
    ├→ Google Analytics API (website traffic)
    ├→ Google Ads API (ad performance)
    ├→ Facebook Ads API (FB ad performance)
    ↓
Generate PDF Report
    ↓
GHL Conversations API (email PDF to client)
    ↓
Google Sheets (log report delivery for audit)
```

Sketch the technical architecture with:
- API endpoints needed
- Data transformations
- Error handling
- Scheduling approach (cron, cloud scheduler)

---

## Integration Checkpoint

- [ ] Browsed Marketplace, identified 3 useful apps
- [ ] Connected at least 2 native integrations
- [ ] Installed a free Marketplace app
- [ ] Built 3-tool custom integration (Flask + Zoom + GHL + Sheets)
- [ ] Tested end-to-end
- [ ] Understood white-label touchpoints
- [ ] Applied idempotency to at least one integration

## Day 23 Recap Questions

1. What should you check before installing any Marketplace app?
2. Name 5 white-label touchpoints.
3. What's idempotency and why does it matter?
4. When should you use Zapier vs custom code?
5. How do you secure a webhook endpoint?

## Phase 3 Complete!

You've mastered:
- GHL REST API (Days 18-19)
- Webhooks and custom integrations (Day 20)
- AI Agents (Day 21)
- Advanced automation patterns (Day 22)
- Marketplace and white-label (Day 23)

You can now do what 95% of GHL users cannot: extend GHL with custom code.

## Next Phase Preview

**Phase 4: Certification Prep** - Days 24-28 prepare you for the HighLevel Admin Certification with focused review, 100+ practice questions, a capstone project, and a full mock exam.
