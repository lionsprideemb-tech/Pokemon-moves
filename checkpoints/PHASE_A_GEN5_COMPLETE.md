# Phase A Complete — Gen 5 DS Moves

Status: **PASS**

Verified on 2026-09-24.

## Coverage
- Move IDs: **471–562**
- Expected animations: **92**
- Present animations: **92**
- Missing animations: **0**
- Source hash mismatches: **0**
- Expected move-mechanics scripts: **92**
- Present move-mechanics scripts: **92**
- Missing mechanics scripts: **0**

## Source
Primary source: `BluRosie/hg-engine`

Pinned source commit:
`398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Repository locations
- Animations: `animations/hg-engine/gen5/`
- Mechanics: `mechanics/hg-engine/move_scripts/`
- Move manifest: `manifests/moves.csv`
- Constants: `constants/moves_post_gen4.h`
- Animation support: `support/hg-engine/`

## Certification
All Gen 5 animation files from IDs 471 through 562 are present and their Git blob hashes match the corresponding files in the pinned hg-engine source snapshot.

Phase A is safe to use as the restart point for the next phase.
