# Phase F2 Dependency Audit — Batch 11

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **101–110 of 173**:

- 322 — POISON_HIT_DOUBLE_POWER_ON_POISONED
- 323 — SET_ABILITY_TO_SIMPLE
- 324 — CHARGE_TURN_SP_ATK_UP
- 325 — CHARGE_TURN_SP_ATK_UP_RAIN_SKIPS
- 326 — STICKY_WEB
- 328 — DEF_UP_3
- 341 — HURRICANE
- 342 — USER_DEF_DOWN_HIT
- 343 — USER_DEF_DOWN_HIT_REMOVE_PROTECT
- 344 — ATK_DEF_SPEED_UP

Findings:
- Three direct battle-subscript dependencies appear: POWER_HERB_METEOR_BEAM, SP_ATK_UP_RAIN_SKIP, and CHARGE_MOVE_CLEANUP.
- Eight side-effect pointers appear; five are new to the cumulative audit.
- Meteor Beam/Electro Shot-style charge behavior depends on item, weather, and cleanup subsystems.
- Sticky Web requires both specialized validation and the entry-hazard queue.
- Hurricane sets HIT_FLY in-script, while its weather-dependent accuracy still requires engine-side verification.
- Hyperspace Fury behavior is delegated to a dedicated handler rather than expressed in this effect script.

Cumulative Phase F2 audit coverage: **110/173**.

Next restart point: **Phase F2 Batch 12 — sorted required-effect positions 111–120.**
