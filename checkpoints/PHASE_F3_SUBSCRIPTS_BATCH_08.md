# Phase F3 Subscript Resolution — Batch 08

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **71–80 of 90**:

- MOVE_SUBSCRIPT_PTR_SPEED_UP_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SPICY_EXTRACT → BATTLE_SUBSCRIPT_SPICY_EXTRACT
- MOVE_SUBSCRIPT_PTR_SP_ATTACK_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_ATTACK_DOWN_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_ATTACK_UP_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_ATTACK_UP_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_DEFENSE_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_DEFENSE_DOWN_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SP_DEFENSE_UP_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_STRENGTH_SAP → BATTLE_SUBSCRIPT_STRENGTH_SAP

Collected **2 new concrete subscript files**, bringing the cumulative unique file count to **62**.

Notable dependency expansion:
- Eight pointers in this batch share the central UPDATE_STAT_STAGE implementation.
- Spicy Extract combines Attack +2 and Defense -2 through that shared stat engine.
- Strength Sap exposes the specialized `StrengthSapCalc` command plus leech-boost item scaling, Liquid Ooze reversal, Magic Guard interaction, Attack reduction, and HP recovery/update dependencies.

Cumulative Phase F3 side-effect-pointer resolution: **80/90**.

Next restart point: **Phase F3 Batch 09 — final sorted side-effect pointers 81–90.**
