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
- Audited in F2 so far: **100/173**
- Current batch: sorted required-effect positions **91–100**
- Direct battle-subscript dependencies found in this batch: **4 unique**
- Side-effect pointer dependencies found in this batch: **11 unique**
- Cumulative unique battle subscripts observed: **5**
- Cumulative unique side-effect pointers observed: **59**
- Generic-damage-only scripts in this batch: **0**

## Batch 10 dependency notes

- Effects 312–317 delegate Reflect, stat reset, party status cure, full draining, Evasion boost, and +2 Defense to side-effect handlers.
- Effect 318 exposes one of the deepest dependency stacks yet: Power Herb-style charge skipping, staged stat updates through `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`, three +2 stat handlers, and charge cleanup.
- Effect 319 delegates Snow weather handling to `BATTLE_SUBSCRIPT_HANDLE_SNOW_TEMPORARY`.
- Effect 320 delegates healing prevention to `MOVE_SUBSCRIPT_PTR_HEAL_BLOCK_START`.
- Effect 321 combines Burn with Hex-style power doubling and explicitly treats `ABILITY_COMATOSE` as satisfying the status condition.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
