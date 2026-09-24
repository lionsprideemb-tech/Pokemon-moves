# Mechanics Dependency Audit

Phase F2 extracts the dependencies hidden behind the 173 battle-effect scripts collected in Phase F1.

This audit tracks:
- direct `BATTLE_SUBSCRIPT_*` calls;
- `MOVE_SUBSCRIPT_PTR_*` side-effect handlers;
- battle-script commands used by each effect;
- explicit references to engine-side C hooks;
- effect scripts that are generic damage stubs even though the named effect requires additional engine behavior.

## Progress

- Required effect scripts: **173**
- Audited in F2: **173/173**
- Current batch: final sorted required-effect positions **171–173**
- Direct battle-subscript dependencies found in this batch: **2 unique**
- Side-effect pointer dependencies found in this batch: **0**
- Cumulative unique direct battle subscripts observed: **9**
- Cumulative unique side-effect pointers observed: **90**
- Generic-damage-only scripts in this batch: **2** (effects 406 and 408)

## Final batch dependency notes

- Effect 406 (SMACK_DOWN) is generic damage only. Pinned upstream confirms pre-move Fly-state hit allowance and post-move grounding/fall-down processing.
- Effect 407 (MAGIC_ROOM) manipulates the field-condition flag directly and calls `BATTLE_SUBSCRIPT_ATTACK_MESSAGE_AND_ANIMATION` plus `BATTLE_SUBSCRIPT_MAGIC_ROOM_END`. Field-condition processing also invokes MAGIC_ROOM_END when the room expires.
- Effect 408 (STEEL_BEAM) is generic damage only. Pinned upstream sets and tracks the Steel Beam/Mind Blown recoil condition outside the effect script and dispatches `BATTLE_SUBSCRIPT_HEAVY_RECOIL` post-move, with Magic Guard suppression.

## Phase F2 status

**Effect-script dependency audit complete: 173/173.**

The dependency manifest is `manifests/mechanics_dependencies.csv`.

This is still **not runtime certification**. The next mechanics step is to resolve and collect the dependency graph behind the 90 side-effect pointers, 9 directly referenced battle subscripts, specialized battle commands, and engine-side hooks, while keeping the 77 upstream-unimplemented moves isolated.
