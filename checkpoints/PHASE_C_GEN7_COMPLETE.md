# Phase C Complete — Gen 7 DS Moves

Status: **PASS**

Verified on 2026-09-24.

## Coverage
- Move IDs: **625–745**
- Expected animations: **121**
- Present animations: **121**
- Missing animations: **0**
- Source hash mismatches: **0**
- Expected move-mechanics scripts: **121**
- Present move-mechanics scripts: **121**
- Missing/ambiguous mechanics scripts: **0**
- Mechanics source/name/hash mismatches: **0**

## Dependency snapshot verification
The shared hg-engine support copied into this repository matches the pinned upstream source exactly:
- `support/hg-engine/animscriptcmd.s`
- `support/hg-engine/moves.h`
- `support/hg-engine/move_effects.h`
- `support/hg-engine/move_data.h`
- `support/hg-engine/move_sub_anim/`
- `support/hg-engine/move_spa/`

All six checked files/trees have matching Git blob/tree SHAs against the pinned source.

Additional raw animation resources that are intentionally not copied are indexed in:
`manifests/upstream_raw_animation_dependencies.txt`

## Z-Move-era note
The Gen 7 range includes the generic and signature Z-Move-era scripts plus later Gen 7 / Let's Go moves. These are valid DS/hg-engine scripts and are preserved exactly from upstream.

Some upstream Gen 7 animation scripts intentionally reuse generic particles/animation patterns (for example, several Z-Move scripts reuse SPA 486). That is **not** a source-integrity failure. Animation uniqueness, placeholder/reuse classification, and any Mercury-specific visual replacement work remain scheduled for **Phase H — Certification**.

## Source
Primary source: `BluRosie/hg-engine`

Pinned source commit:
`398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Repository locations
- Animations: `animations/hg-engine/gen7/`
- Mechanics: `mechanics/hg-engine/move_scripts/`
- Move manifest: `manifests/moves.csv`
- Shared animation support: `support/hg-engine/`
- Raw dependency index: `manifests/upstream_raw_animation_dependencies.txt`

## Certification
All Gen 7 animation files from IDs 625 through 745 are present and their Git blob hashes match the corresponding files in the pinned hg-engine source snapshot. Every ID also resolves to exactly one matching upstream battle/mechanics script with the same file name and Git blob hash.

Phase C is safe to use as the restart point for **Phase D — Gen 8 + Legends: Arceus (746–853)**.
