# Phase F2 Dependency Audit — Batch 06

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **51–60 of 173**:

- 238 — SWAP_ATK_DEF
- 248 — HIT_FIRST_IF_TARGET_ATTACKING
- 269 — RECOIL_HALF
- 271 — LOWER_SP_DEF_2_HIT
- 272 — SHADOW_FORCE
- 276 — RAISE_SP_ATK_HIT
- 277 — ATK_ACC_UP
- 278 — GUARD_SPLIT
- 279 — POWER_SPLIT
- 280 — DOUBLE_POWER_ON_POISONED

Findings:
- One direct battle-subscript dependency occurs: `BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP`.
- Seven side-effect pointers appear; six are new to the cumulative audit.
- Effect 248 depends on the specialized `TrySuckerPunch` command.
- Effect 269 is generic damage only; half-recoil behavior is engine-side.
- Effect 272 exposes a deeper two-turn-move stack: Phantom Force state flags, vanish toggling, protection bypass through FEINT, and charge cleanup.
- Effect 280 handles poison-dependent power scaling directly.

Cumulative Phase F2 audit coverage: **60/173**.

Next restart point: **Phase F2 Batch 07 — sorted required-effect positions 61–70.**
