# Phase F1 Effect Collection — Batch 17

Status: **PASS**

Verified on 2026-09-24.

- Full Phase F1 unique effect requirement: **173**
- Collected this batch: **10**
- Sorted required-effect positions: **161–170**
- Effect IDs: **396, 397, 398, 399, 400, 401, 402, 403, 404, 405**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

All ten effect scripts were copied from the pinned source.

Cumulative Phase F1 effect scripts collected: **170/173**.

Notable dependency-heavy effects in this batch include Belch, Stuff Cheeks, Powder, Laser Focus, Glaive Rush, Throat Chop, Final Gambit, half-max-HP recoil, Bestow, and protection-bypassing damage.

Important engine-hook findings:
- Glaive Rush and Throat Chop set move-condition flags that require later engine handling.
- Belch, half-max-HP recoil, and ignore-protect use generic damage scripts, so their special restrictions/effects are implemented outside these files.
- Final Gambit directly derives damage from the attacker's current HP.
- Bestow delegates item transfer to a dedicated side-effect subscript.

Next restart point: **Phase F1 Batch 18 — final sorted required-effect positions 171–173.**
