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
- Audited in F2 so far: **10/173**
- Current batch: sorted required-effect positions **1–10**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **7 unique**
- Generic-damage-only scripts in this batch: **3** (effect 0 is the normal base HIT; effects 7 and 17 require special behavior elsewhere)

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
