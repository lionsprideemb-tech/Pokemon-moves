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
- Audited in F2 so far: **70/173**
- Current batch: sorted required-effect positions **61–70**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **7 unique**
- Cumulative unique side-effect pointers observed: **40**
- Generic-damage-only scripts in this batch: **1** (effect 282)

## Batch 07 dependency notes

- Effect 281 delegates Autotomize's Speed boost and weight reduction to `MOVE_SUBSCRIPT_PTR_AUTOTOMIZE`.
- Effect 282 (ALWAYS_CRITICAL) is structurally just `CalcCrit` + `CalcDamage`; forced-critical behavior must be supplied outside this effect script.
- Effects 283, 286, 288, and 290 expose dedicated handlers for Quiver Dance, Coil, Shift Gear, and Shell Smash.
- Effect 284 delegates target type replacement to `MOVE_SUBSCRIPT_PTR_CHANGE_TARGET_TO_WATER_TYPE`.
- Effect 285 introduces the one-stage Speed-up handler.
- Effect 287 implements status-dependent 2x power directly and explicitly treats `ABILITY_COMATOSE` as satisfying the status condition.
- Effect 289 implements no-held-item 2x power directly through `BMON_DATA_HELD_ITEM == ITEM_NONE`.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
