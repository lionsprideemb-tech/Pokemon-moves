# Phase F3 Subscript Resolution — Batch 05

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **41–50 of 90**:

- MOVE_SUBSCRIPT_PTR_HEAL_BLOCK_START → BATTLE_SUBSCRIPT_HEAL_BLOCK_START
- MOVE_SUBSCRIPT_PTR_HEAL_PULSE → BATTLE_SUBSCRIPT_HEAL_PULSE
- MOVE_SUBSCRIPT_PTR_HYPERSPACE_FURY → BATTLE_SUBSCRIPT_HYPERSPACE_FURY
- MOVE_SUBSCRIPT_PTR_ION_DELUGE → BATTLE_SUBSCRIPT_ION_DELUGE
- MOVE_SUBSCRIPT_PTR_LASER_FOCUS → BATTLE_SUBSCRIPT_LASER_FOCUS
- MOVE_SUBSCRIPT_PTR_LEECH_SEED_START → BATTLE_SUBSCRIPT_LEECH_SEED_START
- MOVE_SUBSCRIPT_PTR_LIFE_DEW → BATTLE_SUBSCRIPT_LIFE_DEW
- MOVE_SUBSCRIPT_PTR_LIGHT_SCREEN → BATTLE_SUBSCRIPT_LIGHT_SCREEN
- MOVE_SUBSCRIPT_PTR_MAKE_IT_RAIN → BATTLE_SUBSCRIPT_MAKE_IT_RAIN
- MOVE_SUBSCRIPT_PTR_PARALYZE → BATTLE_SUBSCRIPT_PARALYZE

Collected **10 new concrete subscript files**, bringing the cumulative unique file count to **43**.

Notable dependency expansion:
- Heal Pulse includes Mega Launcher-aware 75% healing.
- Hyperspace Fury clears Protect and then reuses the stat updater.
- Laser Focus exposes another `SetMoveConditionFlag` engine-state path.
- Leech Seed is third-type-aware.
- Light Screen relies on `TryLightScreen`.
- Make It Rain includes coin generation plus the Sp. Atk drop.
- Paralysis is another full ability/terrain/Safeguard/status pipeline.

Cumulative Phase F3 side-effect-pointer resolution: **50/90**.

Next restart point: **Phase F3 Batch 06 — sorted side-effect pointers 51–60.**
