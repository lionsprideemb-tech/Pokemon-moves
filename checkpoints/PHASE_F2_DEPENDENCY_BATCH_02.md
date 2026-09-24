# Phase F2 Dependency Audit — Batch 02

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **11–20 of 173**:

- 29 — MULTI_HIT
- 31 — FLINCH_HIT
- 40 — HALVE_HP
- 42 — BIND_HIT
- 43 — HIGH_CRITICAL
- 44 — HIT_TWICE
- 45 — CRASH_ON_MISS
- 51 — DEF_UP_2
- 61 — SP_ATK_DOWN_2
- 68 — LOWER_ATTACK_HIT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Four unique side-effect pointers appear: FLINCH, DEFENSE_UP_2_STAGES, SP_ATTACK_DOWN_2_STAGES, and ATTACK_DOWN_1_STAGE.
- Effects 29 and 44 require multi-hit engine handling.
- Effect 40 directly computes half-current-HP damage.
- Effect 42 (BIND_HIT) is a generic damage script; its trapping behavior must be located in engine-side handling.
- Effect 45 depends on Reckless-aware power scaling and the engine's crash-damage processing.

Cumulative Phase F2 audit coverage: **20/173**.

Next restart point: **Phase F2 Batch 03 — sorted required-effect positions 21–30.**
