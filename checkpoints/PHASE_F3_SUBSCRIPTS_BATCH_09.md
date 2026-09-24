# Phase F3 Subscript Resolution — Batch 09

Status: **PASS**

Verified on 2026-09-24.

Resolved final sorted side-effect pointers **81–90 of 90**:

- MOVE_SUBSCRIPT_PTR_STUFF_CHEEKS → BATTLE_SUBSCRIPT_STUFF_CHEEKS
- MOVE_SUBSCRIPT_PTR_TAKE_HEART → BATTLE_SUBSCRIPT_TAKE_HEART
- MOVE_SUBSCRIPT_PTR_THRASH → BATTLE_SUBSCRIPT_THRASH
- MOVE_SUBSCRIPT_PTR_TIDY_UP → BATTLE_SUBSCRIPT_TIDY_UP
- MOVE_SUBSCRIPT_PTR_TOXIC_THREAD → BATTLE_SUBSCRIPT_TOXIC_THREAD
- MOVE_SUBSCRIPT_PTR_USER_DEF_AND_SPDEF_DOWN_1_STAGE → BATTLE_SUBSCRIPT_USER_DEF_AND_SPDEF_DOWN_1_STAGE
- MOVE_SUBSCRIPT_PTR_USER_DEF_DOWN_HIT → BATTLE_SUBSCRIPT_USER_DEF_DOWN_HIT
- MOVE_SUBSCRIPT_PTR_USER_SWAP_ATK_AND_DEF → BATTLE_SUBSCRIPT_USER_SWAP_ATK_AND_DEF
- MOVE_SUBSCRIPT_PTR_V_CREATE → BATTLE_SUBSCRIPT_USER_DEF_SP_DEF_SPEED_DOWN_HIT
- MOVE_SUBSCRIPT_PTR_WORK_UP → BATTLE_SUBSCRIPT_ATK_SP_ATK_UP

Collected **10 new concrete subscript files**, bringing the pointer-resolution collection to **72 unique files**.

Notable dependency expansion:
- Stuff Cheeks exposes the specialized Berry-processing command.
- Take Heart combines two stat boosts with major-status clearing.
- Thrash stores rampage duration and move lock.
- Tidy Up directly clears Substitutes plus all major entry hazards on both sides before boosting Attack and Speed.
- Toxic Thread composes the shared stat engine with the full Poison status handler.
- Power Trick-style Attack/Defense swapping is performed directly in-script.

Cumulative Phase F3 side-effect-pointer resolution: **90/90**.

Next restart point: **Phase F3 Direct Subscripts — resolve and collect the 9 direct BATTLE_SUBSCRIPT dependencies from Phase F2.**
