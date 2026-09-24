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
- Audited in F2 so far: **170/173**
- Current batch: sorted required-effect positions **161–170**
- Direct battle-subscript dependencies found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **4 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **90**
- Generic-damage-only scripts in this batch: **3** (effects 396, 403, 405)

## Batch 17 dependency notes

- Effect 396 (BELCH) is generic damage only; pinned upstream enforces its Berry-eaten prerequisite during move-selection/use validation.
- Effect 397 (STUFF_CHEEKS) delegates its effect to a dedicated handler, while upstream also validates that the user currently holds a Berry.
- Effects 398–399 introduce dedicated handlers for Powder and Laser Focus.
- Effect 400 (GLAIVE_RUSH) uses `SetMoveConditionFlag`; pinned upstream maps this to the user's `wideOpen` state and later clears it in move-end logic.
- Effect 401 (THROAT_CHOP) also uses `SetMoveConditionFlag`; upstream stores the target's Throat Chop timer in battle state.
- Effect 402 (FINAL_GAMBIT) directly sets damage equal to the user's current HP and ignores type effectiveness; user fainting is handled separately in post-move processing.
- Effect 403 (RECOIL_HALF_MAX_HP) is generic damage only; pinned upstream handles Reckless interaction in base-damage calculation and the half-max-HP recoil subscript post-move.
- Effect 404 delegates Bestow/item transfer to `MOVE_SUBSCRIPT_PTR_GIVE_HELD_ITEM`, with pre-move item/species validity checks elsewhere.
- Effect 405 (IGNORE_PROTECT) is generic damage only; protect bypass is handled by pre-move engine logic.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
