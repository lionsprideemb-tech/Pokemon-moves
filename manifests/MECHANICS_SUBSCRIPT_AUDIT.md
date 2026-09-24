# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **80/90**
- Concrete subscript files collected so far: **62 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 08 notes

- Seven ordinary stat-change pointers in this batch, plus `SPEED_UP_2_STAGES`, all resolve to the already-collected shared `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.
- `SPICY_EXTRACT` is a two-stat wrapper: Attack +2 and Defense -2, both dispatched through the common stat updater after one shared attack-message/animation path.
- `STRENGTH_SAP` is a compound healing/stat script. It calls the specialized `StrengthSapCalc` command to determine healing from the target's Attack, lowers the target's Attack by one stage, applies held-item leech-boost scaling, reverses healing under Liquid Ooze, respects Magic Guard on that damage path, and uses the shared HP recovery/update subscripts.
- This batch strongly reinforces that a large fraction of modern move behavior depends on one central stat-stage engine, while the genuinely unique mechanics tend to live in specialized wrapper scripts and battle commands.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
