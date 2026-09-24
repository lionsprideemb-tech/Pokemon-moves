# Phase F1 Effect Collection — Batch 18

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **3**
- Sorted required-effect positions: **171–173**
- Effect IDs: **406, 407, 408**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All three effect scripts were copied from the pinned source.

Cumulative Phase F1 effect scripts collected: **173/173**.

Important engine-hook findings:
- Smack Down uses a generic damage script, so its grounding/flying-state behavior is handled outside this effect file.
- Magic Room directly manipulates a field-condition flag and calls dedicated battle subscripts for activation/end handling.
- Steel Beam uses a generic damage script, so its recoil behavior is handled elsewhere in the engine.

Phase F1 source collection is complete.

Next restart point: **Phase F2 — audit the 173 collected effect scripts for battle subscripts, side-effect pointers, battle commands, and engine-side hooks.**
