# Phase F3 Subscript Resolution — Batch 02

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **11–20 of 90**:

- MOVE_SUBSCRIPT_PTR_AUTOTOMIZE → BATTLE_SUBSCRIPT_AUTOTOMIZE
- MOVE_SUBSCRIPT_PTR_BADLY_POISON → BATTLE_SUBSCRIPT_BADLY_POISON
- MOVE_SUBSCRIPT_PTR_BOOST_ALL_STATS → BATTLE_SUBSCRIPT_BOOST_ALL_STATS
- MOVE_SUBSCRIPT_PTR_BREAK_SCREENS → BATTLE_SUBSCRIPT_BREAK_SCREENS
- MOVE_SUBSCRIPT_PTR_BURN → BATTLE_SUBSCRIPT_BURN
- MOVE_SUBSCRIPT_PTR_BURN_AND_DRAIN_HEALTH → BATTLE_SUBSCRIPT_BURN_AND_DRAIN_HEALTH
- MOVE_SUBSCRIPT_PTR_CHANGE_TARGET_TO_PSYCHIC_TYPE → BATTLE_SUBSCRIPT_CHANGE_TARGET_TO_PSYCHIC_TYPE
- MOVE_SUBSCRIPT_PTR_CHANGE_TARGET_TO_WATER_TYPE → BATTLE_SUBSCRIPT_CHANGE_TARGET_TO_WATER_TYPE
- MOVE_SUBSCRIPT_PTR_CLANGOROUS_SOUL → BATTLE_SUBSCRIPT_RAISE_ALL_STATS_LOSE_THIRD_MAX_HP
- MOVE_SUBSCRIPT_PTR_COACHING → BATTLE_SUBSCRIPT_COACHING

Collected **10 new concrete subscript files**, bringing the cumulative unique file count to **18**.

Notable dependency expansion:
- Autotomize exposes `ReduceWeight`.
- Badly Poison and Burn are full status-resolution pipelines rather than simple flag setters.
- Burn + drain composes two existing battle subscripts.
- Type-changing effects rely on specialized engine commands.
- Clangorous Soul chains HP modification and multi-stat boosting.

Cumulative Phase F3 side-effect-pointer resolution: **20/90**.

Next restart point: **Phase F3 Batch 03 — sorted side-effect pointers 21–30.**
