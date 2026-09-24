# Phase F3 Command / Engine Audit

Phase F3 has completed script dependency resolution and is now mapping mechanics-relevant battle-script commands to the engine implementations that Mercury Redux must preserve or reproduce.

## Completed script resolution

- `MOVE_SUBSCRIPT_PTR_*`: **90/90**
- Direct `BATTLE_SUBSCRIPT_*` dependencies from Phase F2: **9/9**
- Unique concrete battle-subscript files collected: **80**

## Command / engine audit progress

- Batch 01: **10 commands**
- Batch 02: **10 commands**
- Batch 03: **10 commands**
- Batch 04: **10 commands**
- Cumulative resolved command mappings: **40**

## Batch 04 findings

- `HandleForestsCurse` and `HandleTrickOrTreat` are genuine engine-level third-type mutations, not cosmetic script effects. They add Grass/Ghost, store persistent move-condition flags, and are guarded against Terastallized targets. Their fail conditions are also enforced in `BattleController_BeforeMove.c`.
- `HandleBurnUp` and `HandleDoubleShock` remove Fire/Electric typing respectively and store engine state flags. Their type-presence eligibility checks live in `BattleController_BeforeMove.c`, so copying only the post-hit command would be incomplete.
- `ClearSmog` resets the defender's stat stages, but its activation is wired through `ServerDoPostMoveEffects.c`; this is a concrete example of why post-move hooks must be collected alongside scripts and commands.
- `ClearAuroraVeil` directly clears the side flag and counter, complementing the broader `TryBreakScreens` command from Batch 02.
- `AbilityPopup` is a full asynchronous UI command with allocation, animation state, script pausing, and cleanup—not just a message call.
- `SetCurrentMoveSwitchingStatus` feeds a shared switching state used by Baton Pass, Parting Shot, pivot/forced-switch flows and consumed later by post-move/MoveEnd logic.
- `RemoveEntryHazardFromQueue` is the cleanup half of the hazard queue model already identified through `AddEntryHazardToQueue`.

## Additional engine sources collected

- `mechanics/hg-engine/engine/BattleController_BeforeMove.c`
- `mechanics/hg-engine/engine/ServerDoPostMoveEffects.c`

These files capture move eligibility/failure gates and post-hit dispatch that cannot be recovered from battle scripts alone.

The cumulative command mapping is `manifests/mechanics_command_engine_audit.csv`.

This remains source resolution, not runtime certification. The next audit pass should continue through modern item, grounding/terrain, hazard, and protection-contact commands, then expand the before/post-move hook manifest.
