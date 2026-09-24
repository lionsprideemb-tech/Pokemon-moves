# Phase F3 Subscript Resolution — Batch 07

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **61–70 of 90**:

- MOVE_SUBSCRIPT_PTR_RECHARGE_TURN → BATTLE_SUBSCRIPT_RECHARGE_TURN
- MOVE_SUBSCRIPT_PTR_REFLECT → BATTLE_SUBSCRIPT_REFLECT
- MOVE_SUBSCRIPT_PTR_RESET_ALL_STAT_STAGES → BATTLE_SUBSCRIPT_RESET_ALL_STAT_STAGES
- MOVE_SUBSCRIPT_PTR_SHED_TAIL → BATTLE_SUBSCRIPT_HANDLE_SHED_TAIL
- MOVE_SUBSCRIPT_PTR_SHELL_SMASH → BATTLE_SUBSCRIPT_ATK_SP_ATK_SPEED_UP_2_DEF_SP_DEF_DOWN
- MOVE_SUBSCRIPT_PTR_SHIFT_GEAR → BATTLE_SUBSCRIPT_SHIFT_GEAR
- MOVE_SUBSCRIPT_PTR_SLEEP → BATTLE_SUBSCRIPT_FALL_ASLEEP
- MOVE_SUBSCRIPT_PTR_SPEED_DOWN_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SPEED_DOWN_2_STAGES → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_SPEED_UP_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE

Collected **7 new concrete subscript files**, bringing the cumulative unique file count to **60**.

Notable dependency expansion:
- Recharge state is explicitly stored and move-locked.
- Reflect relies on `TryReflect`.
- Shed Tail combines HP payment, Substitute creation, switching eligibility, stat reset, Leech Seed cleanup, and Baton Pass state.
- Shell Smash and Shift Gear are multi-stat wrappers around the shared updater.
- Sleep exposes one of the deepest status pipelines so far, including terrain and semi-invulnerable-state handling.

Cumulative Phase F3 side-effect-pointer resolution: **70/90**.

Next restart point: **Phase F3 Batch 08 — sorted side-effect pointers 71–80.**
