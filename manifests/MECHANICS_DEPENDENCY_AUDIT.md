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
- Audited in F2 so far: **160/173**
- Current batch: sorted required-effect positions **151–160**
- Direct battle-subscript dependencies found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **3 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **86**
- Generic-damage-only scripts in this batch: **6** (effects 387, 388, 390, 393, 394, 395)

## Batch 16 dependency notes

- Effect 386 (DECORATE) delegates its boosts to `MOVE_SUBSCRIPT_PTR_DECORATE`; pinned upstream confirms its failure conditions in `src/individual/BattleController_BeforeMove.c`.
- Effect 387 (END_TERRAIN) is generic damage only. Pinned upstream handles Steel Roller eligibility before the move and terrain removal after the move; Ice Spinner's terrain removal is also post-move.
- Effect 388 (FELL_STINGER) is generic damage only; its KO-triggered Attack boost is implemented in `src/individual/ServerDoPostMoveEffects.c`.
- Effect 389 (PARTING_SHOT) delegates the target's Attack/Sp. Atk drops, while upstream BeforeMove and post-move hooks cover failure validation and switching.
- Effect 390 (CLEAR_SMOG) is generic damage only; the stat reset is invoked from post-move processing through `BATTLE_SUBSCRIPT_HANDLE_CLEAR_SMOG`.
- Effects 391–392 delegate Ion Deluge state setup to `MOVE_SUBSCRIPT_PTR_ION_DELUGE`; the status-only variant also prevents duplicate field activation.
- Effects 393–394 (Burn Up / Double Shock) explicitly rely on engine-side pre-move type validation and post-move type removal.
- Effect 395 (FORCE_SWITCH_HIT) is generic damage only; the forced-switch trigger is handled in post-move processing.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
