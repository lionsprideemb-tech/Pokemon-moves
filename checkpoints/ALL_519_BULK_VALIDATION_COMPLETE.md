# All 519 candidate moves — bulk validation pass complete

Date: 2026-09-24

The 11-batch fast validation sweep is complete.

## Catalog integrity

- **519/519** candidate rows present
- compact provisional ID range: **923–1441**
- IDs are unique, ordered, and contiguous
- symbolic move IDs are unique
- source-native custom types are preserved for explicit Mercury review
- special Rejuvenation Intercept/Z-Move 0-PP records are recognized rather than misclassified as missing data

## Mechanics status after the sweep

- **515/519 complete**
- **3 source-limited**
- **1 source-conflict**
- **4 total mechanics blockers**

Remaining blockers:
- **1013 — Airborne Slam (MOVE_AIRBORNE_SLAM)** — source-limited
- **1160 — Hunter's Wilds (HUNTERSWILDS)** — source-limited
- **1162 — Terrestrial Claw (TERRESTRIALCLAW)** — source-limited
- **1219 — Shuffle (SHUFFLE)** — source-conflict

## Visual workload classification

- **362** defer until move approval
- **60** unique post-Gen-4 donor certifications after Platinum-native porting
- **93** Platinum/base-era donor spot-check cases
- **4** blocked by unresolved mechanics

This completes the candidate-library bulk validation stage. It does **not** mean all 519 moves have been imported into the Platinum runtime. Runtime implementation remains a separate stage after approval/source-gap handling.
