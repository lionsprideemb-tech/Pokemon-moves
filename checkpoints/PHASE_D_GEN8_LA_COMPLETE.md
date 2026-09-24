# Phase D Complete — Gen 8 + Legends: Arceus DS Moves

Status: **PASS**

Verified on 2026-09-24.

## Coverage
- Move IDs: **746–853**
- Expected animations: **108**
- Present animations: **108**
- Missing animations: **0**
- Source hash mismatches: **0**
- Expected move-mechanics scripts: **108**
- Present move-mechanics scripts: **108**
- Missing/ambiguous mechanics scripts: **0**
- Mechanics source/name/hash mismatches: **0**

## Range contents
This phase includes:
- Sword/Shield-era moves
- Max Move-era entries represented by hg-engine
- Isle of Armor / Crown Tundra moves
- Legends: Arceus move additions through **Take Heart (853)**

## Animation integrity
All 108 Gen 8 / Legends: Arceus animation files have unique Git blob SHAs within this phase. No two stored files are byte-identical duplicates.

That does **not** by itself prove every visual is bespoke or final-quality; semantic reuse, generic particles, or Mercury-specific visual upgrades remain part of **Phase H — Certification**.

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
- Animations: `animations/hg-engine/gen8/`
- Mechanics: `mechanics/hg-engine/move_scripts/`
- Move manifest: `manifests/moves.csv`
- Shared animation support: `support/hg-engine/`
- Raw dependency index: `manifests/upstream_raw_animation_dependencies.txt`

## Certification
All move animation files from IDs 746 through 853 are present and match the corresponding files in the pinned hg-engine source snapshot exactly. Every ID also resolves to exactly one matching upstream battle/mechanics script with the same file name and Git blob hash.

Phase D is safe to use as the restart point for **Phase E — Gen 9 + DLC (854–922)**.
