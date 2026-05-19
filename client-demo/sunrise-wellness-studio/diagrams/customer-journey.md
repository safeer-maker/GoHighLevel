# Customer Journey — Cold Lead → Promoter

> The same person, walking through every stage of the relationship with Sunrise Wellness — and the systems that engage them at each point.

---

## The Full Journey

```mermaid
graph TD
    Start((Stranger<br/>sees Sunrise ad))

    Stage1[Stage 1: COLD LEAD<br/>Click ad / fill form / walk in]
    Stage2[Stage 2: TRIAL MEMBER<br/>Claims free 7-day trial]
    Stage3[Stage 3: NEW MEMBER<br/>Day 0-30 after signup]
    Stage4[Stage 4: ACTIVE MEMBER<br/>Day 31-90, settling in]
    Stage5[Stage 5: ENGAGED MEMBER<br/>90+ days, regular attender]
    Stage6a[Stage 6a: PROMOTER<br/>Refers, reviews, upgrades]
    Stage6b[Stage 6b: AT-RISK<br/>Attendance drops]
    Stage7a[Stage 7a: VIP / VETERAN<br/>Multi-year member]
    Stage7b[Stage 7b: LAPSED<br/>Cancelled]
    Stage8[Stage 8: WIN-BACK<br/>Reactivated lapsed]

    Start --> Stage1
    Stage1 -->|trial claimed| Stage2
    Stage1 -.->|never converts| END1((Lost lead))
    Stage2 -->|paid conversion| Stage3
    Stage2 -.->|never converts| END2((Lost trial))
    Stage3 --> Stage4
    Stage4 --> Stage5
    Stage5 --> Stage6a
    Stage5 --> Stage6b
    Stage6a --> Stage7a
    Stage6b -.->|saved| Stage5
    Stage6b -->|not saved| Stage7b
    Stage7b --> Stage8
    Stage8 -->|reactivates| Stage3
    Stage8 -.->|stays lapsed| END3((Permanent loss))

    %% Systems engaging at each stage
    Stage1 -.->|engaged by| Sys1[/#01 Lead Capture/]
    Stage2 -.->|engaged by| Sys2[/#02 Trial Conversion/]
    Stage3 -.->|engaged by| Sys4[/#04 Onboarding/]
    Stage4 -.->|engaged by| Sys4
    Stage5 -.->|engaged by| Sys5[/#05 Retention/]
    Stage5 -.->|engaged by| Sys6[/#06 Upsell/]
    Stage5 -.->|engaged by| Sys7[/#07 Reviews/]
    Stage6a -.->|engaged by| Sys8[/#08 Referral/]
    Stage6b -.->|engaged by| Sys5
    Stage7b -.->|engaged by| Sys9[/#09 Win-Back/]

    %% All stages contribute to
    Stage1 -.->|tracked in| Sys10[/#10 Owner Reporting/]
    Stage7a -.->|tracked in| Sys10

    %% Cross-cutting: appointments at any stage
    Apt{{Any booked<br/>appointment}}
    Stage2 -.-> Apt
    Stage3 -.-> Apt
    Stage4 -.-> Apt
    Stage5 -.-> Apt
    Apt -.->|protected by| Sys3[/#03 No-Show Recovery/]

    classDef stage fill:#FFE5CC,stroke:#FF8C42,stroke-width:2px,color:#5A3300
    classDef good fill:#D4F4DD,stroke:#2E7D32,stroke-width:2px,color:#1B4D20
    classDef bad fill:#FFD6D6,stroke:#D9534F,stroke-width:1.5px,color:#660000
    classDef system fill:#E0E7FF,stroke:#3F51B5,stroke-width:1.5px,color:#1A237E
    classDef neutral fill:#F5F5F5,stroke:#757575,stroke-width:1px

    class Stage1,Stage2,Stage3,Stage4,Stage5 stage
    class Stage6a,Stage7a,Stage8 good
    class Stage6b,Stage7b,END1,END2,END3 bad
    class Sys1,Sys2,Sys3,Sys4,Sys5,Sys6,Sys7,Sys8,Sys9,Sys10 system
    class Start,Apt neutral
```

---

## Stage-by-Stage Narrative

| Stage | Who they are | What happens | Which system carries them |
|---|---|---|---|
| **Stranger** | Hasn't heard of Sunrise yet | Sees Meta ad, Google search result, or hears from a friend | (acquired by marketing — outside this build's scope) |
| **1. Cold Lead** | Clicked, scrolled, filled a form, called, or walked in | First touch with Sunrise — must be greeted within 5 min or they go cold | **#01** Lead Capture & Instant Response |
| **2. Trial Member** | Claimed the free 7-day trial | Has 7 days to fall in love or wander off | **#02** Trial-to-Paid Conversion |
| **3. New Member (0–30d)** | Paid, signed up | The fragile period — the first 30 days predict everything | **#04** New Member Onboarding |
| **4. Settling-In Member (31–90d)** | Past the cliff | Building routine, attendance stabilizing or wobbling | **#04** continues; **#05** starts watching |
| **5. Engaged Member (90d+)** | Steady-state | The bulk of MRR lives here; bulk of growth opportunity too | **#05** Retention, **#06** Upsell, **#07** Reviews |
| **6a. Promoter** | Loves the studio, tells people | Convert love into measurable referrals | **#08** Referral Engine |
| **6b. At-Risk** | Engagement dropping | Window to intervene before cancellation | **#05** Retention (saves ~30–40%) |
| **7a. VIP / Veteran** | Multi-year, often upgraded to Premium/VIP | Recognize, retain, leverage | **#06** Upsell, **#08** Referral, **#10** Reporting flags |
| **7b. Lapsed** | Cancelled (voluntary or involuntary) | Don't write off — most valuable lead pool | **#09** Win-Back |
| **8. Win-Back** | Reactivated lapsed member | Re-enters at Stage 3 (new member onboarding restart) | Loops back into **#04** |
| **All appointments** | Any stage that books PT, class, nutrition | Reminder cadence + no-show recovery | **#03** No-Show Recovery |
| **All stages** | Owner needs visibility into all of the above | Dashboard + weekly digest | **#10** Owner Reporting |

---

## Key Loops & Branches

**The successful loop:** Stage 1 → 2 → 3 → 4 → 5 → 6a → 7a — the prospect becomes a multi-year VIP who refers friends. Every system in the build is biased toward keeping members on this path.

**The save loop:** Stage 5 → 6b (at-risk) → back to Stage 5 — system #05 catches the at-risk member and saves them. Industry-standard save rate is 30–40% with a good system; without one it's near zero.

**The reactivation loop:** Stage 7b (lapsed) → 8 → re-enters at Stage 3 — system #09 brings cancelled members back into onboarding. 15–25% reactivation rate is realistic.

**The fatal branches** (dashed gray):
- Cold lead never converts (filtered by #01 + nurture)
- Trial never converts (filtered by #02)
- At-risk member not saved (best effort by #05)
- Lapsed member stays gone (best effort by #09)

These losses are unavoidable in any business. The systems minimize them; they don't eliminate them.

---

## Related Diagrams

- **[problem-map.md](problem-map.md)** — pains by persona.
- **[revenue-impact.md](revenue-impact.md)** — dollar value per stage transition.
- **[../integration/master-automation-graph.md](../integration/master-automation-graph.md)** — the technical wiring between systems.
