# Phase F3 Subscript Resolution — Batch 01

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **1–10 of 90**:

- MOVE_SUBSCRIPT_PTR_ACCURACY_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_ADD_TYPE_GHOST → BATTLE_SUBSCRIPT_ADD_TYPE_GHOST
- MOVE_SUBSCRIPT_PTR_ADD_TYPE_GRASS → BATTLE_SUBSCRIPT_ADD_TYPE_GRASS
- MOVE_SUBSCRIPT_PTR_AFTER_YOU → BATTLE_SUBSCRIPT_HANDLE_AFTER_YOU
- MOVE_SUBSCRIPT_PTR_ATK_DEF_SPEED_UP → BATTLE_SUBSCRIPT_ATK_DEF_SPEED_UP
- MOVE_SUBSCRIPT_PTR_ATK_SP_ATK_DOWN → BATTLE_SUBSCRIPT_ATK_SP_ATK_DOWN
- MOVE_SUBSCRIPT_PTR_ATK_SP_ATK_SPEED_DOWN → BATTLE_SUBSCRIPT_ATK_SP_ATK_SPEED_DOWN
- MOVE_SUBSCRIPT_PTR_ATTACK_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_ATTACK_UP_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_AURORA_VEIL → BATTLE_SUBSCRIPT_AURORA_VEIL

Collected **8 unique concrete subscript files** under `mechanics/hg-engine/subscripts/`.

Notable findings:
- Three distinct stat pointers resolve to the same UPDATE_STAT_STAGE implementation.
- UPDATE_STAT_STAGE itself depends on Defiant/Competitive handling.
- After You exposes execution-order manipulation.
- Aurora Veil exposes `TryAuroraVeil`, so its weather/side-condition logic remains part of the command/engine dependency graph.

Cumulative Phase F3 side-effect-pointer resolution: **10/90**.

Next restart point: **Phase F3 Batch 02 — sorted side-effect pointers 11–20.**
