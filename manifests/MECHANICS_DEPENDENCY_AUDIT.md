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
- Audited in F2 so far: **130/173**
- Current batch: sorted required-effect positions **121–130**
- Direct battle-subscript dependencies found in this batch: **2 unique**
- Side-effect pointer dependencies found in this batch: **9 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **72**
- Generic-damage-only scripts in this batch: **0**

## Batch 13 dependency notes

- Effect 355 introduces the two-stage Speed-down handler.
- Effects 356–358 delegate Bleakwind/Wildbolt/Sandsear Storm secondary effects to existing handlers. Their storm/weather-sensitive accuracy behavior is not expressed in these effect scripts and remains an engine-side verification item.
- Effect 359 delegates Toxic Thread to a dedicated combined poison + Speed-drop handler.
- Effect 360 has explicit Parental Bond branching: the normal path uses `MOVE_SUBSCRIPT_PTR_MAKE_IT_RAIN`, while the second Parental Bond hit falls back to the ordinary one-stage Sp. Atk drop handler.
- Effect 361 performs its poisoned-target prerequisite check directly, then delegates Attack/Sp. Atk/Speed drops.
- Effect 362 delegates simultaneous Attack + Sp. Atk reduction.
- Effects 363–364 use the established two-turn charge framework, including `BATTLE_SUBSCRIPT_ITEM_SKIP_CHARGE_TURN` and `BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP`, then apply Paralysis or Burn after damage.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
