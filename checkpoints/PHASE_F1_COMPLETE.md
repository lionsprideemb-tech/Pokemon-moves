# Phase F1 Complete — Required Battle Effect Scripts

Status: **SOURCE COLLECTION COMPLETE**

Verified on 2026-09-24.

Phase F1 collected the complete set of battle effect scripts referenced by the modern move library.

- Modern move IDs audited: **452** (471–922)
- Unique effect IDs required: **173**
- Required effect scripts collected: **173/173**
- Collection batches: **18**
- Pinned source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`
- Upstream-unimplemented moves previously identified: **77**

This checkpoint certifies **source collection only**. It does not certify that all 452 moves are Mercury runtime-ready.

The collected scripts expose dependencies on battle subscripts, `MOVE_SUBSCRIPT_PTR_*` handlers, battle commands, field/status state, item/ability logic, and engine-side C hooks. Several effect scripts are intentionally generic because their special mechanics are implemented elsewhere in hg-engine.

## Next phase

**Phase F2 — dependency extraction and engine-hook audit**

Audit all 173 collected effect scripts for:
1. `Call BATTLE_SUBSCRIPT_*` dependencies.
2. `MOVE_SUBSCRIPT_PTR_*` side-effect dependencies.
3. Specialized battle commands such as multi-hit, hazards, targeting, terrain/weather, and move-condition flags.
4. Explicit engine-side references such as `BeforeMove.c` / `before_move.c`.
5. Generic effect scripts whose real move behavior must be located elsewhere.
6. Separation of the 77 upstream-unimplemented moves from mechanics that can be source-certified.

Do not mark Phase F complete until those dependencies are collected/mapped and the unimplemented set is handled.
