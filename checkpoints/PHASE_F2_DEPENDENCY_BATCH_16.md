# Phase F2 Dependency Audit — Batch 16

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **151–160 of 173**:

- 386 — DECORATE
- 387 — END_TERRAIN
- 388 — FELL_STINGER
- 389 — PARTING_SHOT
- 390 — CLEAR_SMOG
- 391 — ION_DELUGE
- 392 — ION_DELUGE_HIT
- 393 — REMOVE_USER_FIRE_TYPE_HIT
- 394 — REMOVE_USER_ELECTRIC_TYPE_HIT
- 395 — FORCE_SWITCH_HIT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Three side-effect pointers appear; DECORATE and ION_DELUGE are new to the cumulative audit.
- Six effects are generic damage-only scripts whose defining mechanic is implemented outside the effect file.
- Decorate has confirmed BeforeMove failure-condition handling.
- Fell Stinger, Parting Shot, Clear Smog, Burn Up, Double Shock, terrain-ending moves, and damaging forced-switch effects all expose concrete engine-side dependencies in the pinned hg-engine source.
- Burn Up and Double Shock require both pre-move type validation and post-move type removal.

Cumulative Phase F2 audit coverage: **160/173**.

Next restart point: **Phase F2 Batch 17 — sorted required-effect positions 161–170.**
