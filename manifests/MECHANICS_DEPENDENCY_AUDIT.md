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
- Audited in F2 so far: **30/173**
- Current batch: sorted required-effect positions **21–30**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **7 unique**
- Cumulative unique side-effect pointers observed: **17**
- Generic-damage-only scripts in this batch: **2** (effects 101 and 103)

## Batch 03 dependency notes

- Effects 69–73 delegate one-stage defensive/offensive stat drops to dedicated side-effect handlers.
- Effect 76 delegates confusion to `MOVE_SUBSCRIPT_PTR_CONFUSE`.
- Effect 80 delegates recharge-turn handling to `MOVE_SUBSCRIPT_PTR_RECHARGE_TURN`.
- Effect 85 is a true non-damaging no-op script that sets `MOVE_STATUS_SPLASH`.
- Effect 101 (LEAVE_WITH_1_HP) is byte-identical to the generic HIT script; the non-KO behavior must be enforced elsewhere.
- Effect 103 (PRIORITY_1) is also byte-identical to generic HIT; priority must be supplied by move data and/or engine turn-order handling.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
