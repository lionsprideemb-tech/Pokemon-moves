# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **60/90**
- Concrete subscript files collected so far: **53 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 06 notes

- `POISON` is a full modern status pipeline covering Immunity, Comatose, Purifying Salt, Leaf Guard/weather suppression, Flower Veil, grounding, Misty Terrain, Shield Dust, Substitute, Corrosion, Poison/Steel typing including the third-type slot, Safeguard/Infiltrator, Synchronize, Toxic Spikes context, and berry curing.
- `POLLEN_PUFF_HEAL` heals an allied target for half max HP via `BATTLE_SUBSCRIPT_RECOVER_HP` while ignoring normal type-effectiveness flow.
- `POWDER` uses `SetMoveConditionFlag`, exposing another condition-state path for the later command/engine audit.
- `POWER_SPLIT` directly averages both battlers' Attack and Sp. Atk values.
- `PRESENT_HEAL` checks Heal Block before dispatching HP recovery.
- `PRINT_MESSAGE_AND_PLAY_ANIMATION` is the generic buffered-message/animation helper used by several otherwise unrelated mechanics, including Sticky Web setup.
- `PROTECT` depends on the specialized `TryProtection` command and then displays the prepared protection message.
- `QUASH` uses `ChangeExecutionOrderPriority`, mirroring the execution-order dependency already seen with After You.
- `QUIVER_DANCE` fans out through Sp. Atk, Sp. Def, and Speed stat-stage updates.
- `RAISE_ATTACK_AND_ACCURACY` fans out through Attack and Accuracy stat-stage updates.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
