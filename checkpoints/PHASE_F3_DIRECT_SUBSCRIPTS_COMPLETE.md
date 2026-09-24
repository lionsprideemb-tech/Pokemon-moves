# Phase F3 Direct Battle Subscripts

Status: **PASS**

Verified on 2026-09-24.

Resolved all **9/9 direct BATTLE_SUBSCRIPT dependencies** discovered in Phase F2:

- BATTLE_SUBSCRIPT_ATTACK_MESSAGE_AND_ANIMATION → subscript 76
- BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP → subscript 259
- BATTLE_SUBSCRIPT_CREATE_TERRAIN_OVERLAY → subscript 354
- BATTLE_SUBSCRIPT_HANDLE_SNOW_TEMPORARY → subscript 364
- BATTLE_SUBSCRIPT_ITEM_SKIP_CHARGE_TURN → subscript 217
- BATTLE_SUBSCRIPT_MAGIC_ROOM_END → subscript 520
- BATTLE_SUBSCRIPT_POWER_HERB_METEOR_BEAM → subscript 380
- BATTLE_SUBSCRIPT_SP_ATK_UP_RAIN_SKIP → subscript 381
- BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE → subscript 12

Collected **8 new concrete files**. UPDATE_STAT_STAGE was already collected during side-effect pointer resolution, bringing the cumulative unique subscript collection to **80 files**.

Important nested dependencies identified here:
- UPDATE_STAT_STAGE → HANDLE_DEFIANT; HANDLE_COMPETITIVE
- POWER_HERB_METEOR_BEAM → UPDATE_STAT_STAGE
- SP_ATK_UP_RAIN_SKIP → UPDATE_STAT_STAGE

Important specialized-command dependencies exposed here include:
- ChangeStatStage
- CheckCanActivateDefiantOrCompetitive
- GotoIfTerrainOverlayIsType
- ResetParadoxAbility / ActivateParadoxAbility
- ToggleVanish
- RemoveItem
- SetFieldCondition2

Next restart point: **Phase F3 Command/Engine Audit — inventory specialized battle commands used by the required effect/subscript graph and resolve them to their C implementations and engine-side hooks.**
