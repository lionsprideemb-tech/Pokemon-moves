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
- Audited in F2 so far: **50/173**
- Current batch: sorted required-effect positions **41–50**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **6 unique**
- Cumulative unique side-effect pointers observed: **27**
- Generic-damage-only scripts in this batch: **2** (effects 198 and 228)

## Batch 05 dependency notes

- Effect 186 sets the break-screens flag and delegates screen removal to `MOVE_SUBSCRIPT_PTR_BREAK_SCREENS`.
- Effect 190 uses the specialized `CalcHPFalloffPower` command for HP-dependent power.
- Effect 198 (RECOIL_THIRD) is byte-identical to generic HIT; its recoil is engine-side.
- Effect 202 delegates badly poisoned status to `MOVE_SUBSCRIPT_PTR_BADLY_POISON`.
- Effects 204 and 218 reuse previously seen stat-drop side-effect handlers.
- Effect 223 uses `TryFeint` plus `MOVE_SUBSCRIPT_PTR_FEINT`, exposing both command-level and side-effect dependencies for protection removal.
- Effect 227 uses the specialized `TryMetalBurst` command and ignores type effectiveness when its counter calculation succeeds.
- Effect 228 (SWITCH_HIT) is generic damage only; its post-hit switch behavior is engine-side.
- Effect 229 introduces a combined Defense + Sp. Defense self-drop handler.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
