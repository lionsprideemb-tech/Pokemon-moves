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
- Cumulative resolved command mappings: **30**

The audit distinguishes three implementation classes:

1. **hg-engine new command table** — extended commands implemented in `src/battle/battle_script_commands.c`.
2. **vanilla opcode replaced by hg-engine hook** — original HGSS command IDs whose runtime behavior is redirected to hg-engine implementations.
3. **vanilla BattleScriptCmdTable** — commands still supplied by the base HGSS engine where no hg-engine replacement implementation was found.

## Batch 03 findings

- `UpdateTerrainOverlay` and `GotoIfTerrainOverlayIsType` define the modern terrain overlay state used by Grassy, Misty, Electric, and Psychic Terrain. The update command delegates to the shared terrain helper in `src/battle/ability.c`.
- `ActivateParadoxAbility` and `ResetParadoxAbility` are explicit extended commands. They process Protosynthesis/Quark Drive state in battler speed order and coordinate field-condition versus Booster Energy activation/end scripts.
- `SetFieldCondition2` and `IsFieldCondition2On` provide the secondary field-condition state used by Magic Room. The setter owns the five-turn Magic Room counter; `ServerFieldConditionCheck.c` is the engine-side lifetime/expiry dependency.
- `TryIncinerate` implements modern item destruction for Berries/Gems, including Sticky Hold behavior and no-Recycle deletion.
- `AddType` plus `GoToIfThirdType` formalize hg-engine's explicit third-type system, which is important for Forest's Curse, Trick-or-Treat, Leech Seed immunity, and several modern status checks.
- `RemoveItem` remains a dependency on the original HGSS command table. It is used by several otherwise-modern mechanics, so Mercury integration cannot treat the extended C source alone as sufficient.

## Additional engine sources collected

- `mechanics/hg-engine/engine/ability.c` — terrain/paradox helpers.
- `mechanics/hg-engine/engine/other_battle_calculators.c` — shared type helpers including AddType.
- `mechanics/hg-engine/engine/ServerFieldConditionCheck.c` — field-condition lifetime handling including Magic Room expiry.

The cumulative command mapping is `manifests/mechanics_command_engine_audit.csv`.

This is source resolution, not runtime certification. More mechanics-specific commands and before-move/post-move engine hooks still require mapping.
