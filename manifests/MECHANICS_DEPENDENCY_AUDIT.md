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
- Audited in F2 so far: **90/173**
- Current batch: sorted required-effect positions **81–90**
- Direct battle-subscript calls found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **8 unique**
- Cumulative unique side-effect pointers observed: **50**
- Generic-damage-only scripts in this batch: **0**

## Batch 09 dependency notes

- Effect 301 delegates sleep application to `MOVE_SUBSCRIPT_PTR_SLEEP`.
- Effects 302–306 introduce dedicated handlers for Spicy Extract, Fillet Away, Shed Tail, After You, and Quash.
- Effect 307 (Techno Blast) performs Drive detection directly with `CheckItemHoldEffect` and rewrites `BSCRIPT_VAR_MOVE_TYPE`.
- Effect 308 (Multi-Attack) does the same across the full Memory item set, including Fairy.
- Effect 310 delegates Leech Seed startup through `MOVE_SUBSCRIPT_PTR_LEECH_SEED_START` and checks target HP.
- Effect 311 delegates on-hit Light Screen setup to `MOVE_SUBSCRIPT_PTR_LIGHT_SCREEN`.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
