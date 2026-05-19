# Master Problem Map — Sunrise Wellness Studio

> This is the single most important diagram in this folder. It shows **who has which pain**, and **which system we built to solve it**. Walk a prospect through this diagram and they will understand the entire build in two minutes.

---

## The Master Map

```mermaid
graph LR
    %% Personas (left column)
    P1((Cold Lead))
    P2((Trial Member))
    P3((Booked Lead<br/>or Member))
    P4((New Member<br/>Day 0-30))
    P5((Active Member<br/>90+ days))
    P6((Lapsed Member))
    P7((Studio Owner))

    %% Pains (middle column)
    I1[No fast follow-up<br/>Lead goes cold in 5 min]
    I2[Trial drifts<br/>Never converts to paid]
    I3[No-shows<br/>Wasted trainer hour]
    I4[Ghosting<br/>Quiet drop-off in first 30d]
    I5[Silent churn<br/>Quiet disengagement]
    I6[No upsell<br/>Basic stays Basic forever]
    I7[Under-asked<br/>Never asked for review]
    I8[Word-of-mouth lost<br/>Refers but unrewarded]
    I9[Forgotten<br/>Never re-engaged]
    I10[No visibility<br/>Decisions on gut feel]

    %% Solutions (right column)
    S1[#01 Lead Capture<br/>and Instant Response]
    S2[#02 Trial-to-Paid<br/>Conversion]
    S3[#03 No-Show<br/>Recovery]
    S4[#04 New Member<br/>Onboarding]
    S5[#05 Retention and<br/>Churn Prevention]
    S6[#06 Upsell and<br/>Cross-Sell]
    S7[#07 Reviews and<br/>Reputation]
    S8[#08 Referral<br/>Engine]
    S9[#09 Win-Back<br/>Lapsed Members]
    S10[#10 Owner Reporting<br/>and Visibility]

    %% Persona -> Pain
    P1 --> I1
    P2 --> I2
    P3 --> I3
    P4 --> I4
    P5 --> I5
    P5 --> I6
    P5 --> I7
    P5 --> I8
    P6 --> I9
    P7 --> I10

    %% Pain -> Solution
    I1 --> S1
    I2 --> S2
    I3 --> S3
    I4 --> S4
    I5 --> S5
    I6 --> S6
    I7 --> S7
    I8 --> S8
    I9 --> S9
    I10 --> S10

    %% Styling
    classDef persona fill:#FFE5CC,stroke:#FF8C42,stroke-width:2px,color:#5A3300
    classDef pain fill:#FFD6D6,stroke:#D9534F,stroke-width:1.5px,color:#660000
    classDef solution fill:#D4F4DD,stroke:#2E7D32,stroke-width:2px,color:#1B4D20

    class P1,P2,P3,P4,P5,P6,P7 persona
    class I1,I2,I3,I4,I5,I6,I7,I8,I9,I10 pain
    class S1,S2,S3,S4,S5,S6,S7,S8,S9,S10 solution
```

---

## How to Read This

**Left column (orange circles) — the seven personas.** Each represents a real customer state Sunrise Wellness deals with daily. See [00-business-overview.md](../00-business-overview.md) for full persona descriptions.

**Middle column (red boxes) — the pain each persona suffers.** These are the problems an owner would describe in plain English. "My leads go cold." "My trials drift." "My members quietly disappear." Note that the **Active Member** persona has four pains — because the active-member stage is where the most value lives, and the most opportunities are lost.

**Right column (green boxes) — the system we built to solve it.** Each maps to a folder in `problems/`. Click through to see the pitch and the build.

---

## Persona-to-Solution Index

| Persona | Pains | Systems that serve them |
|---|---|---|
| **P1 Cold Lead** | No fast follow-up | #01 |
| **P2 Trial Member** | Trial drifts | #02 |
| **P3 Booked Lead/Member** | No-shows | #03 |
| **P4 New Member (0–30d)** | Ghosting | #04 |
| **P5 Active Member (90d+)** | Silent churn, no upsell, under-asked for reviews, unrewarded word-of-mouth | #05, #06, #07, #08 |
| **P6 Lapsed Member** | Forgotten | #09 |
| **P7 Studio Owner** | No visibility | #10 |

The Active Member persona is the **center of gravity** — four of the ten systems serve them, because they generate the bulk of MRR, the bulk of upsell potential, and the bulk of organic growth.

---

## Related Diagrams

- **[customer-journey.md](customer-journey.md)** — shows the lifecycle from cold lead → promoter, with which systems engage them at each stage.
- **[revenue-impact.md](revenue-impact.md)** — shows the dollar impact of each system.
- **[../integration/master-automation-graph.md](../integration/master-automation-graph.md)** — shows how the ten systems connect to each other once built.
