# Phase F2 Dependency Audit — Batch 13

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **121–130 of 173**:

- 355 — USER_SPEED_DOWN_2_HIT
- 356 — BLEAKWIND_STORM
- 357 — WILDBOLT_STORM
- 358 — SANDSEAR_STORM
- 359 — TOXIC_THREAD
- 360 — MAKE_IT_RAIN
- 361 — VENOM_DRENCH
- 362 — TEARFUL_LOOK
- 363 — CHARGE_TURN_PARALYZE_HIT
- 364 — CHARGE_TURN_BURN_HIT

Findings:
- Two direct battle-subscript dependencies appear, both already seen: ITEM_SKIP_CHARGE_TURN and CHARGE_MOVE_CLEANUP.
- Nine side-effect pointers appear; five are new to the cumulative audit: SPEED_DOWN_2_STAGES, TOXIC_THREAD, MAKE_IT_RAIN, ATK_SP_ATK_SPEED_DOWN, and ATK_SP_ATK_DOWN.
- The three storm effects expose only their secondary effects here; storm/weather accuracy behavior must be verified in engine-side accuracy logic.
- Make It Rain contains explicit Parental Bond handling so the stat-drop behavior is not duplicated incorrectly.
- Venom Drench performs its poisoned-target eligibility check directly.
- The two charge-turn effects reuse the engine's Power Herb/charge-cleanup framework before applying their status effects.

Cumulative Phase F2 audit coverage: **130/173**.

Next restart point: **Phase F2 Batch 14 — sorted required-effect positions 131–140.**
