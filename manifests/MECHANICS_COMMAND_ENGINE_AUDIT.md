# Phase F3 Command / Engine Audit

Phase F3 has completed script dependency resolution and is now mapping mechanics-relevant battle-script commands to the engine implementations that Mercury Redux must preserve or reproduce.

## Completed script resolution

- `MOVE_SUBSCRIPT_PTR_*`: **90/90**
- Direct `BATTLE_SUBSCRIPT_*` dependencies from Phase F2: **9/9**
- Unique concrete battle-subscript files collected: **80**

## Command / engine audit progress

Batch 01 resolves **10 high-impact mechanics commands** exposed by the required effect/subscript graph.

The audit distinguishes three implementation classes:

1. **hg-engine new command table** — commands at/after the extended command range with implementations in `src/battle/battle_script_commands.c`.
2. **vanilla opcode replaced by hg-engine hook** — original HGSS command IDs whose behavior is replaced by an hg-engine hook.
3. **vanilla BattleScriptCmdTable** — commands still supplied by the base HGSS engine where no hg-engine replacement implementation was found.

## Batch 01 findings

- `ChangeStatStage` is the central stat engine and is explicitly replaced by hg-engine's `btl_scr_cmd_33_statbuffchange` hook. It handles modern interactions including Simple, Contrary, and Defiant/Competitive trigger setup.
- `CheckCanActivateDefiantOrCompetitive` is a separate extended command that consumes that trigger state and dispatches the proper ability branch.
- `ChangeExecutionOrderPriority` implements After You/Quash turn-order forcing and fails against a battler that has already acted.
- `AddEntryHazardToQueue` feeds the engine's entry-hazard queue.
- `StrengthSapCalc` computes recovery from the target's stage-adjusted Attack.
- `HandleSoak` and `HandleMagicPowder` refuse type replacement on a Terastallized target and otherwise convert the target to a pure type while storing move-condition state.
- `SetMoveConditionFlag` owns the engine state for Powder, Laser Focus, Glaive Rush, and Throat Chop.
- `TryLightScreen` and `TryPartyStatusRefresh` remain dependencies on the original HGSS `BattleScriptCmdTable`; no replacement hook/source implementation was found in the pinned hg-engine source.

## Collected engine source

The pinned command definitions and engine implementation sources used by this audit are mirrored under:

- `support/hg-engine/battle_commands.inc`
- `mechanics/hg-engine/engine/battle_script_commands.c`
- `mechanics/hg-engine/engine/btl_scr_cmd_33_statbuffchange.c`
- `mechanics/hg-engine/engine/hooks`

The command mapping manifest is `manifests/mechanics_command_engine_audit.csv`.

This is source resolution, not runtime certification. The remaining mechanics-specific commands and broader before-move/post-move engine hooks still require mapping.
