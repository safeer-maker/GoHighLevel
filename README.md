# GoHighLevel Hands-On Mastery Course

**Intermediate to Expert + Admin Certification Prep**

A 28-day hands-on course designed to complement the HighLevel Certifications Program by Michael Johnson. Each day focuses on practical exercises, real-world case scenarios, and API programming labs.

## Course Structure

| Phase | Days | Focus | Level |
|-------|------|-------|-------|
| **Phase 1** | 1-10 | Core Platform Features | Intermediate |
| **Phase 2** | 11-17 | Integration & Combined Scenarios | Advanced |
| **Phase 3** | 18-23 | Expert + API Programming | Expert |
| **Phase 4** | 24-28 | Certification Prep & Capstone | Certification |

## Phase 1: Core Platform Mastery

| Day | Topic | API Lab |
|-----|-------|---------|
| [Day 1](course/phase-1/day-01-dashboard.md) | Dashboard & Settings Configuration | - |
| [Day 2](course/phase-1/day-02-contacts.md) | Contacts & CRM Foundations | [Script](scripts/day-02-contacts-api.py) |
| [Day 3](course/phase-1/day-03-conversations.md) | Conversations & Communication | [Script](scripts/day-03-conversations-api.py) |
| [Day 4](course/phase-1/day-04-calendars.md) | Calendars & Booking Systems | [Script](scripts/day-04-calendars-api.py) |
| [Day 5](course/phase-1/day-05-opportunities.md) | Opportunities & Pipelines | [Script](scripts/day-05-opportunities-api.py) |
| [Day 6](course/phase-1/day-06-payments.md) | Payments & Invoicing | [Script](scripts/day-06-payments-api.py) |
| [Day 7](course/phase-1/day-07-marketing.md) | Marketing - Email Campaigns | [Script](scripts/day-07-marketing-api.py) |
| [Day 8](course/phase-1/day-08-sites.md) | Sites - Funnels & Websites | - |
| [Day 9](course/phase-1/day-09-automation.md) | Automation & Workflows | [Script](scripts/day-09-automation-api.py) |
| [Day 10](course/phase-1/day-10-reputation.md) | Reputation, Memberships & Reporting | - |

## API Setup

```bash
cd scripts/
pip install -r requirements.txt
cp config.py.example config.py  # Add your API key
```

## How to Use This Course

1. Read the day's lesson file
2. Complete all hands-on exercises in your GHL sub-account
3. Work through the case scenarios
4. Complete the API lab (if applicable)
5. Review with the recap questions at the end

## Practice Environment

This course is designed for a **single GHL sub-account** (no agency/admin access required). Here's how we handle common constraints:

| Constraint | How We Handle It |
|-----------|-----------------|
| **Single user (no team members)** | You practice all features solo. Multi-user features (Round Robin, permissions) are explored for interface knowledge + documented for when you manage real teams. |
| **No phone number** | SMS exercises are optional. All core workflows have email alternatives. Templates are still created for practice. |
| **No Stripe/payment processor** | Products, invoices, and order forms can be built without processing real payments. Payment dashboards explored for interface familiarity. |
| **No Google Business / Facebook Page** | Reputation interface explored. Review request workflows built using tags + email (work independently of connected platforms). |
| **No custom domain** | GHL's default subdomain is used for funnels/websites. |
| **No paid ads** | Funnels tested by visiting URLs directly in incognito - no Facebook/Google Ads needed. |

Each lesson marks exercises that depend on optional resources, so you always know what's fully testable vs. what's a design/planning exercise.

## Prerequisites

- Active GHL sub-account (even practice/limited access works)
- Python 3.8+ installed
- Basic understanding of CRM/marketing automation concepts
- Companion: HighLevel Certifications Program by Michael Johnson
