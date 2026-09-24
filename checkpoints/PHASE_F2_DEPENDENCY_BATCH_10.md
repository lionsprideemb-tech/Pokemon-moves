# Phase F2 Dependency Audit — Batch 10

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **91–100 of 173**:

- 312 — SET_REFLECT_HIT
- 313 — RESET_STAT_CHANGES_HIT
- 314 — CURE_PARTY_STATUS_HIT
- 315 — RECOVER_FULL_DAMAGE_DEALT
- 316 — RAISE_EVA_HIT
- 317 — RAISE_DEF_2_HIT
- 318 — CHARGE_TURN_ATK_SP_ATK_SPEED_UP_2
- 319 — WEATHER_SNOW
- 320 — HIT_AND_PREVENT_HEALING
- 321 — BURN_HIT_DOUBLE_POWER_ON_STATUS

Findings:
- Four direct battle-subscript dependencies appear in this batch: ITEM_SKIP_CHARGE_TURN, UPDATE_STAT_STAGE, CHARGE_MOVE_CLEANUP, and HANDLE_SNOW_TEMPORARY.
- Eleven side-effect pointers appear; nine are new to the cumulative audit.
- Effect 318 exposes a complex charge/Power Herb/stat-update flow and is a high-priority Mercury integration dependency.
- Snow is delegated to a dedicated temporary-weather subscript.
- Effect 321 handles both burn and status-dependent power scaling, including Comatose awareness.

Cumulative Phase F2 audit coverage: **100/173**.

Next restart point: **Phase F2 Batch 11 — sorted required-effect positions 101–110.**
