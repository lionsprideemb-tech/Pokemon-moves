# Phase F1 Effect Collection — Batch 16

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **10**
- Sorted required-effect positions: **151–160**
- Effect IDs: **386, 387, 388, 389, 390, 391, 392, 393, 394, 395**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All ten effect scripts were copied exactly from the pinned source.

Cumulative Phase F1 effect scripts collected: **160/173**.

Notable dependency-heavy effects in this batch include Decorate, terrain removal, Fell Stinger, Parting Shot, Clear Smog, Ion Deluge, Burn Up, Double Shock, and damaging force-switch behavior.

Important engine-hook findings:
- Decorate explicitly relies on fail conditions in `before_move.c`.
- Burn Up and Double Shock explicitly rely on `src/individual/BeforeMove.c` for failure conditions/type-removal behavior.
- End Terrain, Fell Stinger, and Force Switch Hit use generic damage scripts, confirming that their special mechanics live in engine-side hooks rather than these effect files alone.

Next restart point: **Phase F1 Batch 17 — sorted required-effect positions 161–170.**
