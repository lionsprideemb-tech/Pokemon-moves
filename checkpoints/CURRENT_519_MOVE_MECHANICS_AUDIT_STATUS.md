# Current 519-Move Mechanics Audit — Status Checkpoint

Status: **SOURCE RECOVERY COMPLETE — FOUR MERCURY DESIGN DECISIONS REMAIN**

Date: 2026-09-24

## Current coverage

- Master catalog: **519 unique moves**
- Audit-detail records: **519/519**
- Fully source-resolved mechanics records: **515**
- Source-limited records: **3**
- Source-conflict records: **1**
- Total unresolved/design-decision blockers: **4**

The 11-batch validation sweep is complete. Additional public-source recovery was then attempted for every remaining blocker.

## Remaining design-decision blockers

### MOVE_AIRBORNE_SLAM — Airborne Slam
Elite Redux never supplies power, accuracy, or PP in the audited public config/history. Its Normal/Physical identity, hammer flag, ignores-Protect behavior, 20% confusion intent, and Gigaton Hammer animation reference are source-supported. A downstream implementation supplies 85/100/10 but changes the type to Fighting, so those numbers are fallback design evidence rather than authoritative ER recovery.

### HUNTERSWILDS — Hunter's Wilds
Vanguard's public PBS references custom function `EffectDependsOnHigherDamage`, but the public repository contains no matching runtime script. The exact Attack-higher and Sp. Atk-higher branches are not recoverable.

### TERRESTRIALCLAW — Terrestrial Claw
Vanguard's public PBS says terrain changes which stat is raised, but its assigned function name matches standard Terrain Pulse semantics and the custom override is absent. The terrain-to-stat mapping is not recoverable.

### SHUFFLE — Shuffle
Uranium's public row is internally inconsistent: 60 BP Normal/Special damage data, Present-like healing prose, Roost's function code, and a 100% chance field. The public repository contains no runtime scripts to reconcile those fields.

## Recommended next step

Use `checkpoints/MERCURY_RECOMMENDED_RESOLUTIONS_FOR_4_BLOCKERS.md` as the explicit Mercury design proposal. Once those four behaviors are accepted (or adjusted), promote them to `complete`, regenerate the compact plan, run full-catalog QA, and begin the approval/import stage.
