# Phase F3 Subscript Resolution — Batch 06

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **51–60 of 90**:

- MOVE_SUBSCRIPT_PTR_POISON → BATTLE_SUBSCRIPT_POISON
- MOVE_SUBSCRIPT_PTR_POLLEN_PUFF_HEAL → BATTLE_SUBSCRIPT_POLLEN_PUFF_HEAL
- MOVE_SUBSCRIPT_PTR_POWDER → BATTLE_SUBSCRIPT_POWDER
- MOVE_SUBSCRIPT_PTR_POWER_SPLIT → BATTLE_SUBSCRIPT_POWER_SPLIT
- MOVE_SUBSCRIPT_PTR_PRESENT_HEAL → BATTLE_SUBSCRIPT_PRESENT_HEAL
- MOVE_SUBSCRIPT_PTR_PRINT_MESSAGE_AND_PLAY_ANIMATION → BATTLE_SUBSCRIPT_PRINT_MESSAGE_AND_PLAY_ANIMATION
- MOVE_SUBSCRIPT_PTR_PROTECT → BATTLE_SUBSCRIPT_PROTECT
- MOVE_SUBSCRIPT_PTR_QUASH → BATTLE_SUBSCRIPT_HANDLE_QUASH
- MOVE_SUBSCRIPT_PTR_QUIVER_DANCE → BATTLE_SUBSCRIPT_SP_ATK_SP_DEF_SPEED_UP
- MOVE_SUBSCRIPT_PTR_RAISE_ATTACK_AND_ACCURACY → BATTLE_SUBSCRIPT_RAISE_ATTACK_AND_ACCURACY

Collected **10 new concrete subscript files**, bringing the cumulative unique file count to **53**.

Notable dependency expansion:
- Poison exposes another complete ability/terrain/status-immunity pipeline and is explicitly Toxic-Spikes-aware.
- Powder adds another `SetMoveConditionFlag` path.
- Power Split directly mutates averaged offensive stats.
- Protect depends on `TryProtection`.
- Quash depends on execution-order mutation.
- Quiver Dance and Attack+Accuracy reuse the common stat-stage engine.

Cumulative Phase F3 side-effect-pointer resolution: **60/90**.

Next restart point: **Phase F3 Batch 07 — sorted side-effect pointers 61–70.**
