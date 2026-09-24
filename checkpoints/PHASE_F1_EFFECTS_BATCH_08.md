# Phase F1 Effect Collection — Batch 08

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **10**
- Sorted required-effect positions: **71–80**
- Effect IDs: **291, 292, 293, 294, 295, 296, 297, 298, 299, 300**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All ten effect scripts were copied exactly from the pinned source.

Cumulative Phase F1 effect scripts collected: **80/173**.

Notable engine dependencies exposed in this batch include V-create stat drops, Heavy Slam weight scaling, Reckless/crash handling, terrain overlays, Work Up, and several multi-hit modes.

Effect script 0300 (Psyblade) is byte-identical to the generic crit/damage effect in the pinned source; its Electric Terrain power behavior is therefore handled elsewhere in the engine and remains part of the later dependency audit.

Next restart point: **Phase F1 Batch 09 — sorted required-effect positions 81–90.**
