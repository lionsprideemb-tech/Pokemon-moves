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
- Audited in F2 so far: **120/173**
- Current batch: sorted required-effect positions **111–120**
- Direct battle-subscript dependencies found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **6 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **67**
- Generic-damage-only scripts in this batch: **4** (effects 351–354)

## Batch 12 dependency notes

- Effect 345 (Poltergeist) checks the target's held item directly and fails when no item is held.
- Effect 346 delegates Clangorous Soul's HP cost and all-stat boost to `MOVE_SUBSCRIPT_PTR_CLANGOROUS_SOUL`.
- Effect 347 introduces the three-quarters drain handler.
- Effect 348 delegates combined burn + drain behavior to `MOVE_SUBSCRIPT_PTR_BURN_AND_DRAIN_HEALTH`.
- Effect 349 implements its randomized stronger-power branch directly in the effect script.
- Effect 350 randomly selects among existing Sleep, Poison, and Paralysis handlers.
- Effects 351–354 are all byte-identical generic damage scripts. Prevent-escape, mutual trapping, Stealth Rock placement, and Spikes placement therefore depend on engine-side hooks not visible in these effect files.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
