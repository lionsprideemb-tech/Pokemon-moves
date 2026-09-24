# Phase F2 Complete — Effect-Script Dependency Audit

Status: **SOURCE DEPENDENCY AUDIT COMPLETE**

Verified on 2026-09-24.

Phase F2 audited every unique battle effect script required by modern move IDs 471–922.

- Required effect scripts: **173**
- Audited effect scripts: **173/173**
- Unique `MOVE_SUBSCRIPT_PTR_*` dependencies observed: **90**
- Unique direct `BATTLE_SUBSCRIPT_*` dependencies observed: **9**
- Modern moves represented by the mechanics map: **452**
- Upstream-unimplemented moves already isolated by the Phase F audit: **77**
- Pinned source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

The audit also identified a substantial class of effects whose defining behavior is not contained in the effect script itself. Confirmed examples include recoil, forced switching, terrain removal, Fell Stinger, Clear Smog, Burn Up, Double Shock, Smack Down, Steel Beam, Belch, protect bypass, priority/power modifiers, and several trapping/hazard effects.

This checkpoint certifies **dependency discovery from the effect layer**, not Mercury runtime readiness.

## Next phase

**Phase F3 — dependency resolution and collection**

Resolve the 90 side-effect pointer handlers and 9 direct battle subscripts to their concrete source files, collect missing required subscripts, inventory specialized battle commands, and map the corresponding C-side hooks. Keep the 77 upstream-unimplemented moves separately marked until their missing mechanics are implemented and tested.
