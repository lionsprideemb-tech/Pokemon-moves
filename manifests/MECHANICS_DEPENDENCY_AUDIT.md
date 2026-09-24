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
- Audited in F2 so far: **20/173**
- Current batch: sorted required-effect positions **11–20**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **4 unique**
- Cumulative unique side-effect pointers observed: **10**
- Generic-damage-only scripts in this batch: **1** (effect 42, BIND_HIT)

## Batch 02 dependency notes

- Effects 29 and 44 directly depend on the engine's multi-hit machinery.
- Effect 40 computes half-current-HP damage directly and sets type effectiveness to be ignored.
- Effect 42 is byte-identical to the generic HIT script; trapping/bind behavior must be supplied elsewhere.
- Effect 45 relies on `ABILITY_RECKLESS` and `BATTLE_STATUS_CRASH_DAMAGE`, which require engine processing beyond the script.
- Effects 31, 51, 61, and 68 delegate their stat/status behavior to side-effect pointer handlers.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
