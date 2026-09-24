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
- Audited in F2 so far: **150/173**
- Current batch: sorted required-effect positions **141–150**
- Direct battle-subscript dependencies found in this batch: **0**
- Side-effect pointer dependencies found in this batch: **9 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **84**
- Generic-damage-only scripts in this batch: **1** (effect 382)

## Batch 15 dependency notes

- Effects 375–379 introduce dedicated handlers for third-type Ghost, Psychic-type replacement, Aurora Veil, Strength Sap, and Heal Pulse-style target healing.
- Effect 380 uses `CheckTargetIsPartner` to choose between normal damage and ally healing, then delegates the healing branch to `MOVE_SUBSCRIPT_PTR_POLLEN_PUFF_HEAL`.
- Effect 381 (COACHING) explicitly says its fail conditions live outside the script. The pinned upstream source confirms `MOVE_EFFECT_COACHING` checks in `src/individual/BattleController_BeforeMove.c`, including stat-cap and valid-ally conditions.
- Effect 382 (DOUBLE_POWER_IF_FASTER) is byte-identical to generic HIT, so speed comparison / power doubling is engine-side.
- Effects 383–384 delegate Life Dew and Entrainment to dedicated handlers.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
