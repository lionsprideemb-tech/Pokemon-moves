# Phase F2 Dependency Audit — Batch 01

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **1–10 of 173**:

- 0 — HIT
- 2 — POISON_HIT
- 3 — RECOVER_HALF_DAMAGE_DEALT
- 4 — BURN_HIT
- 5 — FREEZE_HIT
- 6 — PARALYZE_HIT
- 7 — HALVE_DEFENSE
- 17 — BYPASS_ACCURACY
- 18 — ATK_DOWN
- 27 — CONTINUE_AND_CONFUSE_SELF

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Seven unique side-effect pointer dependencies are used: POISON, DRAIN_HALF_DAMAGE_DEALT, BURN, FREEZE, PARALYZE, ATTACK_DOWN_1_STAGE, and THRASH.
- Effects 7 (HALVE_DEFENSE) and 17 (BYPASS_ACCURACY) are byte-identical to the generic HIT script. Their named special behavior must therefore be located in engine-side handling.
- Effect 27 depends on the attacker's `STATUS2_RAMPAGE` state before installing the THRASH side effect.

Cumulative Phase F2 audit coverage: **10/173**.

Next restart point: **Phase F2 Batch 02 — sorted required-effect positions 11–20.**
