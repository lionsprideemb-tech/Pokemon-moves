# Phase F3 Subscript Resolution — Batch 04

Status: **PASS**

Verified on 2026-09-24.

Resolved sorted side-effect pointers **31–40 of 90**:

- MOVE_SUBSCRIPT_PTR_ENTRAINMENT → BATTLE_SUBSCRIPT_ENTRAINMENT
- MOVE_SUBSCRIPT_PTR_EVASION_UP_1_STAGE → BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE
- MOVE_SUBSCRIPT_PTR_FEINT → BATTLE_SUBSCRIPT_FEINT
- MOVE_SUBSCRIPT_PTR_FILLET_AWAY → BATTLE_SUBSCRIPT_ATK_SP_ATK_SPEED_UP_2_LOSE_HALF_MAX_HP
- MOVE_SUBSCRIPT_PTR_FLINCH → BATTLE_SUBSCRIPT_FLINCH_MON
- MOVE_SUBSCRIPT_PTR_FREEZE → BATTLE_SUBSCRIPT_FREEZE
- MOVE_SUBSCRIPT_PTR_GIVE_HELD_ITEM → BATTLE_SUBSCRIPT_GIVE_HELD_ITEM
- MOVE_SUBSCRIPT_PTR_GIVE_TARGET_SIMPLE → BATTLE_SUBSCRIPT_GIVE_TARGET_SIMPLE
- MOVE_SUBSCRIPT_PTR_GUARD_SPLIT → BATTLE_SUBSCRIPT_GUARD_SPLIT
- MOVE_SUBSCRIPT_PTR_HEAL_BELL → BATTLE_SUBSCRIPT_HEAL_BELL

Collected **9 new concrete subscript files**, bringing the cumulative unique file count to **33**.

Notable dependency expansion:
- Fillet Away chains HP loss plus three +2 stat-stage updates.
- Freeze exposes another full modern status/immunity pipeline.
- Bestow performs real held-item transfer in its subscript.
- Simple Beam carries an explicit protected-ability/Ability Shield exclusion list.
- Guard Split directly mutates averaged defensive stats.
- Heal Bell exposes the party-status refresh command.

Cumulative Phase F3 side-effect-pointer resolution: **40/90**.

Next restart point: **Phase F3 Batch 05 — sorted side-effect pointers 41–50.**
