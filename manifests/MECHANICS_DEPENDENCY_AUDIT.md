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
- Audited in F2 so far: **60/173**
- Current batch: sorted required-effect positions **51–60**
- Direct battle-subscript calls found in this batch: **1 unique**
- Side-effect pointer dependencies found in this batch: **7 unique**
- Cumulative unique side-effect pointers observed: **33**
- Generic-damage-only scripts in this batch: **1** (effect 269)

## Batch 06 dependency notes

- Effect 238 delegates Attack/Defense swapping to `MOVE_SUBSCRIPT_PTR_USER_SWAP_ATK_AND_DEF`.
- Effect 248 uses the specialized `TrySuckerPunch` command to validate whether the target is attacking.
- Effect 269 (RECOIL_HALF) is byte-identical to generic HIT; half-damage recoil is handled elsewhere.
- Effect 271 introduces the two-stage Sp. Defense drop handler.
- Effect 272 (SHADOW_FORCE) manipulates Phantom Force and semi-invulnerable state, toggles battler visibility, reuses the FEINT side-effect pointer to bypass protection, and directly calls `BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP`.
- Effects 276–279 introduce handlers for Sp. Attack boosting, Attack+Accuracy boosting, Guard Split, and Power Split.
- Effect 280 implements its poison check and 2x power multiplier directly in the effect script.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
