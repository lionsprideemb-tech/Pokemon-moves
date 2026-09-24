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
- Audited in F2 so far: **80/173**
- Current batch: sorted required-effect positions **71–80**
- Direct battle-subscript calls found in this batch: **1 unique**
- Side-effect pointer dependencies found in this batch: **3 unique**
- Cumulative unique side-effect pointers observed: **42**
- Generic-damage-only scripts in this batch: **1** (effect 300)

## Batch 08 dependency notes

- Effect 291 delegates V-create-style defensive/Speed drops to `MOVE_SUBSCRIPT_PTR_V_CREATE`.
- Effect 292 uses the specialized `CalcHeavySlamPower` battle command.
- Effect 293 combines Reckless-aware scaling, crash-damage processing, and confusion.
- Effect 294 directly calls `BATTLE_SUBSCRIPT_CREATE_TERRAIN_OVERLAY` after `UpdateTerrainOverlay`.
- Effect 295 introduces the `MOVE_SUBSCRIPT_PTR_WORK_UP` handler.
- Effect 296 combines fixed two-hit logic with the FLINCH side effect.
- Effects 297 and 298 rely on `MULTIHIT_TRIPLE_KICK` engine behavior; 297 requests up to 10 hits and 298 requests three escalating hits.
- Effect 299 uses ordinary fixed three-hit multi-hit handling.
- Effect 300 (PSYBLADE) is generic crit/damage only; its Electric Terrain power modifier is engine-side.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
