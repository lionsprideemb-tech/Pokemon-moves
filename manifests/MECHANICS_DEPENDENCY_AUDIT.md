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
- Audited in F2 so far: **140/173**
- Current batch: sorted required-effect positions **131–140**
- Direct battle-subscript dependencies found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **6 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **75**
- Generic-damage-only scripts in this batch: **2** (effects 372 and 373)

## Batch 14 dependency notes

- Effect 365 computes its HP-based damage directly from the defender's current HP and ignores type effectiveness.
- Effect 366 sets up a fixed three-hit sequence, but its always-critical property is not forced in the effect script and needs engine-side critical verification.
- Effect 367 introduces `MOVE_SUBSCRIPT_PTR_TAKE_HEART`.
- Effect 368 raises critical stage directly and reuses the one-stage Speed-up handler.
- Effect 369 (MORTAL_SPIN) only expresses damage + poison here; hazard/bind cleanup is an engine-side dependency.
- Effect 370 introduces the dedicated `MOVE_SUBSCRIPT_PTR_TIDY_UP` handler.
- Effect 371 reuses the Protect handler, with the upstream script explicitly noting that the move effect differentiates protection variants.
- Effects 372 (INCINERATE) and 373 (FIRST_TURN_ONLY) are generic damage scripts; their special item-destruction and eligibility rules are engine-side.
- Effect 374 introduces `MOVE_SUBSCRIPT_PTR_ADD_TYPE_GRASS` for third-type addition.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
