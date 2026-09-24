# Modern Move Mechanics Audit

Pinned source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Phase F status

Phase F is **in progress**.

- Modern move IDs mapped: **452/452** (471–922)
- Existing per-move battle scripts: **452/452**
- Unique battle effect IDs required: **173**
- Missing move-data effect mappings: **0**
- Moves explicitly marked upstream with `FLAG_UNUSABLE_UNIMPLEMENTED`: **77**

Unimplemented-flag count by generation:
- Gen 5: **14**
- Gen 6: **8**
- Gen 7: **11**
- Gen 8: **30**
- Gen 9: **14**

## Important finding

The earlier 452/452 battle-script count proves every modern move has a dispatch script, but it does **not** prove every mechanic is complete. The pinned hg-engine move-data table explicitly marks 77 modern moves as unimplemented.

Those moves are retained in the library and marked in `manifests/mechanics_effects.csv`; they must not be treated as Mercury-ready until their behavior is implemented and tested.

## F1 collection plan

The **173 unique effect scripts** required by the 452 moves will be copied into `mechanics/hg-engine/effects/` in small verified batches to avoid losing progress.

After those are collected, Phase F continues with shared battle subscripts, command includes, and engine-side hooks.
