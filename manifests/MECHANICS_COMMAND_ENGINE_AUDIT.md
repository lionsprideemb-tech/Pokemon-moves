# Phase F3 Command / Engine Audit

Phase F3 has completed script dependency resolution and is mapping mechanics-relevant battle-script commands to the engine implementations that Mercury Redux must preserve or reproduce.

## Completed script resolution

- `MOVE_SUBSCRIPT_PTR_*`: **90/90**
- Direct `BATTLE_SUBSCRIPT_*` dependencies from Phase F2: **9/9**
- Unique concrete battle-subscript files collected: **80**

## Command / engine audit progress

- Batch 01: **10 commands**
- Batch 02: **10 commands**
- Batch 03: **10 commands**
- Batch 04: **10 commands**
- Batch 05: **10 commands**
- Cumulative resolved command mappings: **50**

## Batch 05 findings

- `GotoIfGrounded` confirms grounding is a shared engine concept rather than a script-only check. `IsClientGrounded` accounts for Levitate/EElevate, Air Balloon, Magnet Rise, Flying typing, Iron Ball, Ingrain, Gravity, explicit grounded state, and semi-invulnerable Fly/Dig/Dive/Phantom Force states.
- `CheckProtectContactMoves` is the central modern contact-on-protection dispatcher for King's Shield, Spiky Shield, Baneful Bunker, Obstruct, Silk Trap, and Burning Bulwark.
- `JumpToCurrentEntryHazard` proves hg-engine has an ordered hazard queue rather than relying only on side-condition bits. The queue supports Spikes, Toxic Spikes, Stealth Rock, Sticky Web, and a Sharp Steel slot.
- `CheckSubstitute` is an hg-engine replacement for the original opcode and includes Infiltrator bypass logic, except for Transform and Sky Drop.
- `CheckToxicSpikes` is also replaced and handles modern Poison-type absorption. The pinned implementation clears the layer count and also masks `side_condition` with `SIDE_EFFECT_TYPE_TOXIC_SPIKES`; this exact source behavior should be preserved in the archive but explicitly runtime-tested before Mercury certification.
- `CheckItemHoldEffect`, `GetItemHoldEffect`, and `GetItemEffectParam` remain base-HGSS dependencies. They underpin a surprisingly large amount of modern mechanics, including Power Herb, weather duration items, drain boosts, Room Service, and resist-Berry behavior.
- `TrySpikes` and `TryToxicSpikes` also remain original HGSS commands, with hg-engine layering its own BeforeMove caps and hazard-queue handling around them.

## Existing engine sources covering this batch

- `mechanics/hg-engine/engine/battle_script_commands.c`
- `mechanics/hg-engine/engine/other_battle_calculators.c`
- `mechanics/hg-engine/engine/BattleController_BeforeMove.c`
- `mechanics/hg-engine/engine/hooks`

The cumulative command mapping is `manifests/mechanics_command_engine_audit.csv`.

This remains source resolution, not runtime certification. The next pass should continue with remaining terrain/move-property helpers, protection/priority gates, and move-state commands, then convert the discovered cross-file dependencies into a dedicated engine-hook manifest.
