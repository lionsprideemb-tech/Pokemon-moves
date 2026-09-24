# Phase F1 Effect Collection — Batch 15

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **10**
- Sorted required-effect positions: **141–150**
- Effect IDs: **375, 376, 377, 378, 379, 380, 381, 382, 383, 384**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All ten effect scripts were copied exactly from the pinned source.

Cumulative Phase F1 effect scripts collected: **150/173**.

Notable dependency-heavy effects in this batch include Trick-or-Treat-style third typing, Magic Powder, Aurora Veil, Strength Sap, Heal Pulse, Pollen Puff ally healing, Coaching, Life Dew, and Entrainment.

Two important engine-hook notes were exposed:
- Coaching explicitly says its fail conditions live in `before_move.c`.
- Effect 382 (double power if faster) is a generic damage script, so its speed comparison/power scaling is handled outside this effect script.

Next restart point: **Phase F1 Batch 16 — sorted required-effect positions 151–160.**
