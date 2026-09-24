# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **10/90**
- Concrete subscript files collected so far: **8**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 01 notes

The first 10 pointers resolve to eight concrete files because three stat-stage pointers share `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.

Important nested dependencies already visible:
- `UPDATE_STAT_STAGE` can call Defiant and Competitive handling.
- Forest's Curse / Trick-or-Treat handlers call the attack-message/animation subscript and specialized type-change commands.
- After You uses `ChangeExecutionOrderPriority`.
- Multi-stat handlers recursively call `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.
- Aurora Veil uses `TryAuroraVeil` and the prepared-message animation subscript.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
