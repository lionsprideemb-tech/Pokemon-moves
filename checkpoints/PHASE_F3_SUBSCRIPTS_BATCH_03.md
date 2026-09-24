# Phase F3 Subscript Resolution — Batch 03

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **21–30 of 90**:

- MOVE_SUBSCRIPT_PTR_COIL → BATTLE_SUBSCRIPT_ATK_DEF_ACC_UP
- MOVE_SUBSCRIPT_PTR_CONFUSE → BATTLE_SUBSCRIPT_CONFUSE
- MOVE_SUBSCRIPT_PTR_DECORATE → BATTLE_SUBSCRIPT_DECORATE
- MOVE_SUBSCRIPT_PTR_DEFENSE_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_DEFENSE_UP_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_DEFENSE_UP_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_DEFENSE_UP_3_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_DRAIN_FULL → BATTLE_SUBSCRIPT_DRAIN_FULL
- MOVE_SUBSCRIPT_PTR_DRAIN_HALF_DAMAGE_DEALT → BATTLE_SUBSCRIPT_DRAIN_HALF_DAMAGE_DEALT
- MOVE_SUBSCRIPT_PTR_DRAIN_THREE_QUARTERS → BATTLE_SUBSCRIPT_DRAIN_THREE_QUARTERS

Collected **6 new concrete subscript files**, bringing the cumulative unique file count to **24**.

Notable dependency expansion:
- Coil and Decorate recursively depend on UPDATE_STAT_STAGE.
- Confusion handling includes ability, Substitute, Safeguard/Infiltrator, held-item, range/failure, and berry-cure paths.
- Four separate Defense-stage pointer constants share the same core stat updater.
- All three drain fractions depend on Leech-boost item logic, Liquid Ooze, Magic Guard, and UPDATE_HP.

Cumulative Phase F3 side-effect-pointer resolution: **30/90**.

Next restart point: **Phase F3 Batch 04 — sorted side-effect pointers 31–40.**
