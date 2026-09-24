# Phase F1 Effect Collection — Batch 12

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **10**
- Sorted required-effect positions: **111–120**
- Effect IDs: **345, 346, 347, 348, 349, 350, 351, 352, 353, 354**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All ten effect scripts were copied exactly from the pinned source.

Cumulative Phase F1 effect scripts collected: **120/173**.

Notable dependency-heavy effects in this batch include Poltergeist held-item validation, Clangorous Soul HP/stat handling, 75% draining, burn-and-drain behavior, Fickle Beam random power, and Tri Attack-style random status application.

Effects 351–354 are byte-identical generic damage scripts in the pinned source. Their trapping and entry-hazard behavior is therefore supplied by engine-side hooks rather than these effect scripts themselves; that dependency is preserved for the later Phase F audit.

Next restart point: **Phase F1 Batch 13 — sorted required-effect positions 121–130.**
