# Pilot borderline review audit — November 25, 2026

Eleven previously flagged reviews were inspected again against **actual original Steam review text**. All 11 F0–F3 judgments were retained, with reasons below. Sample `steam_pilot_024` gained a *secondary* `technical_performance` label, because its author reports high hardware requirements. This is the author's unverified claim, not our hardware benchmark.

| Review ID | Level | Rationale |
|---|---|---|
| `steam_pilot_003` | F1 | Original 2017 bug complaint is mixed with additions through 2022. Treat the current text as temporally confounded. |
| `steam_pilot_008` | F2 | Explicit desire for a fresh design direction; no implementation details. Retain F2, not F3. |
| `steam_pilot_011` | F2 | Desires smarter AI and changed tracking policy; privacy allegation remains unverified. |
| `steam_pilot_015` | F0 | Generic comparison with Civ V without an identifiable mechanism or specific defect. |
| `steam_pilot_021` | F1 | Detailed criticism of roads, units, resources and pacing, but no unambiguous request for a remedy; rewritten in 2022. |
| `steam_pilot_023` | F1 | Crashes and claimed surveillance; privacy claim coded as allegation, not independently confirmed. |
| `steam_pilot_024` | F1 | Overly tedious gameplay and claimed heavy hardware needs. Add technical_performance as a secondary *reported* issue. |
| `steam_pilot_025` | F1 | Bilingual text includes a substantive English translation; statement addresses representation, not a requested change. |
| `steam_pilot_029` | F1 | Specific failure to run after reinstall, though cause remains unknown. |
| `steam_pilot_032` | F1 | Feature omissions and critical comparison do not alone equal an explicit improvement request. |
| `steam_pilot_042` | F1 | Early-turn multiplayer rush is an identifiable complaint; later edit is not a design request. |

The accompanying [reconciled pilot coding CSV](pilot_50_adjudicated_codes.csv) preserves the 50 original rows plus adjudication status and notes. The [initial coding CSV](pilot_50_manual_codes.csv) is retained as an unmodified first pass.

**Methodological honesty:** This was a targeted same-session audit, **not** an independent, blinded or delayed code–recode study. No reliability coefficient is reported. A 15–20% blind repeat coding of the formal sample remains a separate step. Of 50 Pilot reviews, 13 were edited after their original creation; their current text cannot uncritically be attributed to the historical time window.
