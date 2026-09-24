# Phase F2 Dependency Audit — Batch 07

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **61–70 of 173**:

- 281 — AUTOTOMIZE
- 282 — ALWAYS_CRITICAL
- 283 — SP_ATK_SP_DEF_SPEED_UP
- 284 — CHANGE_TO_WATER_TYPE
- 285 — RAISE_SPEED_HIT
- 286 — ATK_DEF_ACC_UP
- 287 — DOUBLE_DAMAGE_ON_STATUS
- 288 — SPEED_UP_2_ATK_UP
- 289 — DOUBLE_DAMAGE_WITHOUT_ITEM
- 290 — ATK_SP_ATK_SPEED_UP_2_DEF_SP_DEF_DOWN

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Seven side-effect pointers appear, all new to the cumulative audit.
- Effect 282 is generic crit/damage only; its always-critical behavior is engine-side.
- Effect 287 handles status/Comatose power doubling directly.
- Effect 289 handles itemless power doubling directly.
- Autotomize, Quiver Dance, Coil, Shift Gear, and Shell Smash all depend on dedicated side-effect handlers.

Cumulative Phase F2 audit coverage: **70/173**.

Next restart point: **Phase F2 Batch 08 — sorted required-effect positions 71–80.**
