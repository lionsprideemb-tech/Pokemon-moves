# Phase F2 Dependency Audit — Batch 05

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **41–50 of 173**:

- 186 — REMOVE_SCREENS
- 190 — DECREASE_POWER_WITH_LESS_USER_HP
- 198 — RECOIL_THIRD
- 202 — BADLY_POISON_HIT
- 204 — USER_SP_ATK_DOWN_2
- 218 — USER_SPEED_DOWN_HIT
- 223 — REMOVE_PROTECT
- 227 — METAL_BURST
- 228 — SWITCH_HIT
- 229 — USER_DEF_SP_DEF_DOWN_HIT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Six unique side-effect pointers appear; four are new to the cumulative audit: BREAK_SCREENS, BADLY_POISON, FEINT, and USER_DEF_AND_SPDEF_DOWN_1_STAGE.
- Effect 190 depends on the specialized `CalcHPFalloffPower` command.
- Effect 198 is generic damage only; one-third recoil is engine-side.
- Effect 223 depends on both `TryFeint` and the FEINT side-effect handler.
- Effect 227 depends on `TryMetalBurst` and engine battle-status processing.
- Effect 228 is generic damage only; its switch-out behavior is engine-side.

Cumulative Phase F2 audit coverage: **50/173**.

Next restart point: **Phase F2 Batch 06 — sorted required-effect positions 51–60.**
