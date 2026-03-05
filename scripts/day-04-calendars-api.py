"""
Day 4 API Lab: Calendars & Appointments via GHL API
====================================================
List calendars, check availability, create/manage appointments.
"""

import requests
import json
from datetime import datetime, timedelta
from config import GHL_API_KEY, GHL_LOCATION_ID, GHL_BASE_URL, API_VERSION


def get_headers():
    return {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
    }


# --- 1. List All Calendars ---

def list_calendars():
    """List all calendars in the sub-account."""
    url = f"{GHL_BASE_URL}/calendars/"
    params = {"locationId": GHL_LOCATION_ID}

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        calendars = response.json().get("calendars", [])
        print(f"Found {len(calendars)} calendars:")
        for cal in calendars:
            print(f"  - {cal.get('id')}: {cal.get('name')} ({cal.get('calendarType', 'N/A')})")
        return calendars
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# --- 2. Get Calendar Free Slots ---

def get_free_slots(calendar_id, start_date=None, end_date=None):
    """
    Get available time slots for a calendar.

    Args:
        calendar_id: GHL calendar ID
        start_date: Start of range (ISO format). Defaults to tomorrow.
        end_date: End of range (ISO format). Defaults to 7 days from start.
    """
    url = f"{GHL_BASE_URL}/calendars/{calendar_id}/free-slots"

    if not start_date:
        start_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    if not end_date:
        end_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    params = {
        "startDate": start_date,
        "endDate": end_date,
    }

    response = requests.get(url, headers=get_headers(), params=params)

    if response.status_code == 200:
        data = response.json()
        slots = data.get("slots", {})
        total = sum(len(v) for v in slots.values())
        print(f"Available slots from {start_date} to {end_date}: {total}")
        for date, times in slots.items():
            if times:
                print(f"\n  {date}:")
                for slot in times[:5]:  # Show first 5 per day
                    print(f"    {slot}")
                if len(times) > 5:
                    print(f"    ... and {len(times) - 5} more")
        return slots
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return {}


# --- 3. Create an Appointment ---

def create_appointment(calendar_id, contact_id, start_time, end_time, title="", notes=""):
    """
    Create an appointment on a calendar.

    Args:
        calendar_id: GHL calendar ID
        contact_id: GHL contact ID
        start_time: ISO format datetime (e.g., "2024-03-15T10:00:00-05:00")
        end_time: ISO format datetime
        title: Appointment title
        notes: Additional notes
    """
    url = f"{GHL_BASE_URL}/calendars/events/appointments"

    payload = {
        "calendarId": calendar_id,
        "locationId": GHL_LOCATION_ID,
        "contactId": contact_id,
        "startTime": start_time,
        "endTime": end_time,
        "title": title or "API-Created Appointment",
        "notes": notes,
        "appointmentStatus": "confirmed",
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        appt = response.json()
        print(f"Appointment created: {appt.get('id', 'N/A')}")
        print(f"  Time: {start_time} - {end_time}")
        print(f"  Status: confirmed")
        return appt
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 4. Get Appointment Details ---

def get_appointment(event_id):
    """Get details of a specific appointment."""
    url = f"{GHL_BASE_URL}/calendars/events/appointments/{event_id}"

    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        appt = response.json()
        print(f"Appointment: {appt.get('title', 'N/A')}")
        print(f"  Status: {appt.get('appointmentStatus', 'N/A')}")
        print(f"  Start: {appt.get('startTime', 'N/A')}")
        print(f"  End: {appt.get('endTime', 'N/A')}")
        print(f"  Contact: {appt.get('contactId', 'N/A')}")
        return appt
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 5. Update Appointment Status ---

def update_appointment(event_id, status=None, notes=None):
    """
    Update an appointment's status or notes.

    Args:
        event_id: Appointment/event ID
        status: New status (confirmed, showed, noshow, cancelled, invalid)
        notes: Updated notes
    """
    url = f"{GHL_BASE_URL}/calendars/events/appointments/{event_id}"

    payload = {}
    if status:
        payload["appointmentStatus"] = status
    if notes:
        payload["notes"] = notes

    response = requests.put(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print(f"Appointment {event_id} updated successfully")
        if status:
            print(f"  New status: {status}")
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# --- 6. Delete/Cancel Appointment ---

def delete_appointment(event_id):
    """Cancel/delete an appointment."""
    url = f"{GHL_BASE_URL}/calendars/events/appointments/{event_id}"

    response = requests.delete(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Appointment {event_id} cancelled/deleted")
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


# --- 7. Get Tomorrow's Appointments Summary ---

def get_tomorrows_appointments():
    """Get a summary of all appointments scheduled for tomorrow."""
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    day_after = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

    # First get all calendars
    calendars = list_calendars()

    print(f"\nAppointments for {tomorrow}:")
    print("-" * 40)

    # For each calendar, check for appointments
    # Note: The actual endpoint may vary - check GHL API docs
    for cal in calendars:
        cal_id = cal.get("id")
        cal_name = cal.get("name")
        print(f"\n  Calendar: {cal_name}")

        # Get booked slots (opposite of free slots)
        slots = get_free_slots(cal_id, tomorrow, day_after)
        # The actual booked appointments would need a different endpoint
        # This is a demonstration of the concept


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GHL API Lab - Day 4: Calendars & Appointments")
    print("=" * 60)

    # --- Exercise 1: List calendars ---
    print("\n--- Exercise 1: List Calendars ---")
    # calendars = list_calendars()

    # --- Exercise 2: Get free slots ---
    print("\n--- Exercise 2: Get Free Slots ---")
    # slots = get_free_slots("CALENDAR_ID_HERE")

    # --- Exercise 3: Create appointment ---
    print("\n--- Exercise 3: Create Appointment ---")
    # tomorrow_10am = (datetime.now() + timedelta(days=1)).replace(hour=10, minute=0).isoformat()
    # tomorrow_1030am = (datetime.now() + timedelta(days=1)).replace(hour=10, minute=30).isoformat()
    # create_appointment(
    #     calendar_id="CALENDAR_ID_HERE",
    #     contact_id="CONTACT_ID_HERE",
    #     start_time=tomorrow_10am,
    #     end_time=tomorrow_1030am,
    #     title="Sales Consultation",
    #     notes="Interested in premium membership",
    # )

    # --- Exercise 4: Update appointment status ---
    print("\n--- Exercise 4: Update Status ---")
    # update_appointment("EVENT_ID_HERE", status="showed")

    # --- Exercise 5: Tomorrow's summary ---
    print("\n--- Exercise 5: Tomorrow's Summary ---")
    # get_tomorrows_appointments()

    print("\n" + "=" * 60)
    print("Uncomment exercises above to run them.")
    print("=" * 60)
