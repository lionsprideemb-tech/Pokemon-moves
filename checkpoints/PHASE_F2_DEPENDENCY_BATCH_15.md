# Phase F2 Dependency Audit — Batch 15

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **141–150 of 173**:

- 375 — ADD_THIRD_TYPE_GHOST
- 376 — CHANGE_TO_PSYCHIC_TYPE
- 377 — SET_AURORA_VEIL
- 378 — STRENGTH_SAP
- 379 — HEAL_TARGET
- 380 — POLLEN_PUFF
- 381 — COACHING
- 382 — DOUBLE_POWER_IF_FASTER
- 383 — LIFE_DEW
- 384 — ENTRAINMENT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Nine side-effect pointer dependencies appear, all new to the cumulative audit.
- Pollen Puff branches on `CheckTargetIsPartner` to select damage versus ally healing.
- Coaching has an explicit engine-side dependency: pinned hg-engine contains `MOVE_EFFECT_COACHING` fail-condition logic in `src/individual/BattleController_BeforeMove.c`.
- Double Power If Faster is generic damage only; its speed comparison and power modifier are engine-side.
- Aurora Veil, Strength Sap, Life Dew, and Entrainment all rely on dedicated side-effect handlers.

Cumulative Phase F2 audit coverage: **150/173**.

Next restart point: **Phase F2 Batch 16 — sorted required-effect positions 151–160.**
