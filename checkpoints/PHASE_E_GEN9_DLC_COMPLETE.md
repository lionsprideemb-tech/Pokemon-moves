# Phase E Complete — Gen 9 + DLC DS Moves

Status: **PASS**

Verified on 2026-09-24.

## Coverage
- Move IDs: **854–922**
- Expected animations: **69**
- Present animations: **69**
- Missing animations: **0**
- Source hash mismatches: **0**
- Expected move-mechanics scripts: **69**
- Present move-mechanics scripts: **69**
- Missing/ambiguous mechanics scripts: **0**
- Mechanics source/name/hash mismatches: **0**

## Range contents
This phase covers Generation 9 through the DLC-era additions and ends at:

- **922 — Malignant Chain**

Notable included groups include:
- Scarlet/Violet base-game moves
- Paradox/signature moves
- Teal Mask additions
- Indigo Disk additions
- Pecharunt-era move support

## Animation integrity
All 69 Gen 9 + DLC animation files have unique Git blob SHAs within this phase. No two stored files are byte-identical duplicates.

As with earlier phases, this verifies source integrity—not that every visual is final Mercury quality. Semantic reuse, generic particles, and any animations that deserve custom upgrades remain part of **Phase H — Certification**.

## Dependency snapshot verification
The shared hg-engine support copied into this repository matches the pinned upstream source exactly:
- `support/hg-engine/animscriptcmd.s`
- `support/hg-engine/moves.h`
- `support/hg-engine/move_effects.h`
- `support/hg-engine/move_data.h`
- `support/hg-engine/move_sub_anim/`
- `support/hg-engine/move_spa/`

Additional raw resources intentionally not copied remain indexed in:
`manifests/upstream_raw_animation_dependencies.txt`

## Source
Primary source: `BluRosie/hg-engine`

Pinned source commit:
`398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Repository locations
- Animations: `animations/hg-engine/gen9/`
- Mechanics: `mechanics/hg-engine/move_scripts/`
- Move manifest: `manifests/moves.csv`
- Shared animation support: `support/hg-engine/`
- Raw dependency index: `manifests/upstream_raw_animation_dependencies.txt`

## Certification
All move animation files from IDs 854 through 922 are present and match the corresponding files in the pinned hg-engine source snapshot exactly. Every ID also resolves to exactly one matching upstream battle/mechanics script with the same file name and Git blob hash.

Phases A–E now provide complete certified source coverage for **all 452 post-Gen-IV move IDs, 471–922**.

Phase E is safe to use as the restart point for **Phase F — Mechanics audit/integration mapping**.
