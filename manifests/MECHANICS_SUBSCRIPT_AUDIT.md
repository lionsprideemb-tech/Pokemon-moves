# Mechanics Subscript Resolution

Phase F3 resolves script-level dependencies discovered by the Phase F2 effect audit.

## Side-effect pointer resolution

- Unique `MOVE_SUBSCRIPT_PTR_*` dependencies: **90**
- Resolved: **90/90**
- Unique concrete files represented by that mapping: **72**

## Direct battle-subscript resolution

- Unique direct `BATTLE_SUBSCRIPT_*` dependencies from Phase F2: **9**
- Resolved: **9/9**
- New concrete files collected in this pass: **8**
- One dependency, `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`, was already present from side-effect pointer resolution.
- Total unique collected subscript files after this pass: **80**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Direct dependency findings

- `ATTACK_MESSAGE_AND_ANIMATION` is the common attack-message plus move-animation helper.
- `CHARGE_MOVE_CLEANUP` clears locked-move state and marks charge-move completion.
- `CREATE_TERRAIN_OVERLAY` contains terrain presentation plus Quark Drive/paradox activation/reset handling; its source includes an upstream TODO around terrain-move behavior.
- `HANDLE_SNOW_TEMPORARY` installs five-turn snow, handles duration-extending held items, and resets/activates Protosynthesis-related state.
- `ITEM_SKIP_CHARGE_TURN` contains Power Herb-style animation/item consumption and semi-invulnerable visual handling.
- `MAGIC_ROOM_END` clears the Magic Room field condition and prints the end message.
- `POWER_HERB_METEOR_BEAM` and `SP_ATK_UP_RAIN_SKIP` both call the shared stat-stage updater; the Power Herb variant also consumes the item.
- `UPDATE_STAT_STAGE` itself calls Defiant and Competitive handlers and depends on `ChangeStatStage` plus `CheckCanActivateDefiantOrCompetitive`.

The direct mapping manifest is `manifests/mechanics_direct_subscripts.csv`.

Phase F3 is still active. The next step is to inventory and resolve the specialized battle commands and nested battle-subscript dependencies exposed by the collected effect/subscript graph, then map the corresponding C implementations and engine hooks.
