# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **30/90**
- Concrete subscript files collected so far: **24 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 03 notes

- `COIL` resolves to `BATTLE_SUBSCRIPT_ATK_DEF_ACC_UP`, which fans out through Attack, Defense, and Accuracy stat-stage updates.
- `CONFUSE` is a full status pipeline: Own Tempo, Shield Dust, Substitute, Safeguard/Infiltrator, held-item context, confusion duration, move-range failure behavior, and berry curing are all handled in the subscript.
- `DECORATE` is a two-stat wrapper around the shared stat-stage updater.
- All four Defense stage pointers in this batch resolve to the already-collected `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.
- Full, half, and three-quarter drain resolve to three concrete scripts with the same core dependency stack: Leech-boost held-item handling, Liquid Ooze reversal, Magic Guard interaction, and `BATTLE_SUBSCRIPT_UPDATE_HP`.
- The three drain scripts differ chiefly in the fraction applied to hit damage before the shared drain logic.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
