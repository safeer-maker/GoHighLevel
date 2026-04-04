# GoHighLevel Hands-On Mastery Course

**From Zero to Expert + Admin Certification Prep**

A 28-day hands-on course designed to complement the HighLevel Certifications Program by Michael Johnson. Each day builds on the previous one with real exercises in your GHL sub-account, real-world business case scenarios, and Python API labs.

---

## What Makes This Course Different

Most GHL courses teach features in isolation. This course is different:

- **One continuous project:** You build a complete GHL system for **Sunrise Wellness Studio** across all 10 days of Phase 1. Every day adds a new layer, and by Day 10 you have a fully automated business.
- **Consistent case studies:** Every day includes scenarios for the same two businesses - **BrightSmile Dental Clinic** and **Elevate Digital Agency** - so you see how the same GHL features apply differently across industries.
- **Beginner-friendly explanations:** Each feature is explained in plain English with "What is it?" and "Why do you need it?" before diving into exercises.
- **Practice-first:** Every concept has a hands-on exercise you do in your actual GHL sub-account - not just reading or watching.

## The Three Businesses You'll Work With

| Business | Role in Course | Industry |
|----------|---------------|----------|
| **Sunrise Wellness Studio** | Primary - all hands-on exercises | Fitness & Wellness |
| **BrightSmile Dental Clinic** | Case Scenario 1 - every day | Healthcare / Dental |
| **Elevate Digital Agency** | Case Scenario 2 - every day | Marketing Agency |

**Sunrise Wellness Studio** offers personal training, group fitness classes (HIIT, Yoga, Pilates), nutrition coaching, and retail products. It has memberships (Free Trial, Basic $79/mo, Premium $149/mo, VIP $249/mo) and needs every GHL feature. You'll build this from scratch.

---

## Course Structure

| Phase | Days | Focus | Level |
|-------|------|-------|-------|
| **Phase 1** | 1-10 | Core Platform Features | Beginner to Intermediate |
| **Phase 2** | 11-17 | Integration & Combined Scenarios | Intermediate to Advanced |
| **Phase 3** | 18-23 | Expert + API Programming | Advanced to Expert |
| **Phase 4** | 24-28 | Certification Prep & Capstone | Certification Ready |

## Phase 1: Core Platform Mastery

Each day builds on the last. By Day 10, Sunrise Wellness Studio is a fully automated business:

| Day | Topic | What You Build for Sunrise Wellness | API Lab |
|-----|-------|-------------------------------------|---------|
| [Day 1](course/phase-1/day-01-dashboard.md) | Dashboard & Settings | Business profile, custom values, dashboard | - |
| [Day 2](course/phase-1/day-02-contacts.md) | Contacts & CRM | Member database, custom fields, smart lists | [Script](scripts/day-02-contacts-api.py) |
| [Day 3](course/phase-1/day-03-conversations.md) | Conversations | SMS/email templates, webchat widget | [Script](scripts/day-03-conversations-api.py) |
| [Day 4](course/phase-1/day-04-calendars.md) | Calendars & Booking | PT, group class, and nutrition calendars | [Script](scripts/day-04-calendars-api.py) |
| [Day 5](course/phase-1/day-05-opportunities.md) | Opportunities & Pipelines | Sales pipeline + onboarding pipeline | [Script](scripts/day-05-opportunities-api.py) |
| [Day 6](course/phase-1/day-06-payments.md) | Payments & Invoicing | Products, invoices, coupons, Text2Pay | [Script](scripts/day-06-payments-api.py) |
| [Day 7](course/phase-1/day-07-marketing.md) | Marketing & Email | Email campaigns, trigger links | [Script](scripts/day-07-marketing-api.py) |
| [Day 8](course/phase-1/day-08-sites.md) | Sites & Funnels | Free trial funnel, intake form, survey | - |
| [Day 9](course/phase-1/day-09-automation.md) | Automation & Workflows | New lead, no-show, reminder workflows | [Script](scripts/day-09-automation-api.py) |
| [Day 10](course/phase-1/day-10-reputation.md) | Reputation & Community | Review system, member community, reporting | - |

## Practice Environment

This course is designed for a **single GHL sub-account** (no agency/admin access required):

| Constraint | How We Handle It |
|-----------|-----------------|
| **Single user (no team)** | All features practiced solo. Multi-user features (Round Robin, permissions) are explored for interface knowledge and documented for when you manage real teams. |
| **No phone number** | SMS exercises are optional. All workflows have email alternatives. Templates are still created for writing practice. |
| **No Stripe/payment processor** | Products, invoices, and order forms are fully built. Payment processing is explored but not required. |
| **No Google Business / Facebook** | Reputation interface explored. Review request workflows built with tags + email. |
| **No custom domain** | GHL's default subdomain used for funnels/websites. |
| **No paid ads** | Funnels tested by visiting URLs directly in incognito. |

Each lesson clearly marks what's fully testable vs. what's a design/planning exercise.

## API Setup (Optional for Phase 1, Required for Phase 3)

```bash
cd scripts/
pip install -r requirements.txt
cp config.py.example config.py  # Add your API key (see file for instructions)
```

Not all sub-accounts have API access. If you get 401/403 errors, focus on the UI exercises - they're the priority. Phase 3 (Days 18-23) covers API access setup in depth.

## How to Use This Course

1. **Read the "Today's Mission"** section to understand what you're building
2. **Complete all hands-on exercises** in your GHL sub-account
3. **Work through both case scenarios** (BrightSmile Dental + Elevate Digital)
4. **Try the API lab** if you have API access (optional in Phase 1)
5. **Answer the recap questions** to test your understanding
6. **Review the Next Day Preview** to prepare for tomorrow

## Prerequisites

- Active GHL sub-account (even practice/limited access works)
- Python 3.8+ installed (for optional API labs)
- Basic understanding of what a CRM is (if not, Day 1 explains it)
- Companion: HighLevel Certifications Program by Michael Johnson
