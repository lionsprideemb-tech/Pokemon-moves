# Phase F3 Command / Engine Audit

Phase F3 has completed script dependency resolution and is now mapping mechanics-relevant battle-script commands to the engine implementations that Mercury Redux must preserve or reproduce.

## Completed script resolution

- `MOVE_SUBSCRIPT_PTR_*`: **90/90**
- Direct `BATTLE_SUBSCRIPT_*` dependencies from Phase F2: **9/9**
- Unique concrete battle-subscript files collected: **80**

## Command / engine audit progress

- Batch 01: **10 commands**
- Batch 02: **10 commands**
- Cumulative resolved command mappings: **20**

The audit distinguishes three implementation classes:

1. **hg-engine new command table** — extended commands implemented in `src/battle/battle_script_commands.c`.
2. **vanilla opcode replaced by hg-engine hook** — original HGSS command IDs whose runtime behavior is redirected to hg-engine implementations.
3. **vanilla BattleScriptCmdTable** — commands still supplied by the base HGSS engine where no hg-engine replacement implementation was found.

## Batch 02 findings

- `TryProtection` is not just vanilla Protect logic: hg-engine replaces the command and handles single-user Protect, side-wide protection, Endure, ally-granted protection state, and modern protect-success-counter rules.
- `TryBreakScreens` is replaced and explicitly clears Reflect, Light Screen, and Aurora Veil together, including all three duration counters.
- `ResetAllStatChanges` is also replaced and resets every active battler.
- `TryAuroraVeil` is an extended command; it installs five-turn Aurora Veil, applies the screen-extending held-item duration bonus, and intentionally leaves fail gating to `BattleController_BeforeMove.c`.
- `StuffCheeks` is an extended Berry dispatcher that chooses the correct held-item recovery/effect subscript; the pinned source contains an explicit TODO for Ripen.
- `TryStickyWeb` handles duplicate-web failure and installs the side condition before the separate hazard-queue command is used.
- `TrySynchronizeStatus` and `TryCureStatusBerry` form important parts of the modern status pipeline. The Berry command also records Berry consumption for Belch eligibility.
- `CheckTargetIsPartner` is the Pollen Puff ally-heal branch point.
- `TryReflect` remains a dependency on the original HGSS `BattleScriptCmdTable`; no hg-engine replacement hook/source implementation was found at the pinned commit.

The cumulative command mapping is `manifests/mechanics_command_engine_audit.csv`.

This is source resolution, not runtime certification. More mechanics-specific commands and broader before-move/post-move engine hooks still require mapping.
