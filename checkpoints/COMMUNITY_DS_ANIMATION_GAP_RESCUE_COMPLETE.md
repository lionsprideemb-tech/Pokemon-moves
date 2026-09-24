# Community DS Animation Gap Rescue — Complete

Date: 2026-09-24

## Result

All **519 / 519** community moves in `manifests/community_moves.csv` now resolve to a direct hg-engine / Nintendo DS animation baseline in the approval board.

Final verified bucket count:

- DS reuse assigned: **519**
- No source animation: **0**
- Animation selection pending: **0**
- Source animation needs DS port: **0**
- Referenced-only / chained animation: **0**

## Passes

### Pass 12 — Rescue assignments
`manifests/COMMUNITY_DS_ANIMATION_RESCUE_PASS_12.csv`

Assigned direct DS-native analog animations to the 354 moves that previously had no source animation or still needed an animation selection.

### Pass 13 — Cross-engine fallbacks
`manifests/COMMUNITY_DS_ANIMATION_PORT_FALLBACK_PASS_13.csv`

Added runnable DS fallbacks for the 12 moves whose only animation evidence was GBA / Pokémon Essentials / other cross-engine source material. Original source evidence remains preserved in the earlier source manifests for later high-fidelity recreation.

### Pass 14 — Direct resolution
`manifests/COMMUNITY_DS_ANIMATION_DIRECT_RESOLUTION_PASS_14.csv`

Resolved the final 9 referenced-only cases, including chained references and `MOVE_NONE` entries, into direct DS animation paths.

## Approval board

`docs/approval/app.js` now loads Passes 12–14 after the source audit manifests, so the visual approval sheet shows the direct DS baseline assignment while retaining source provenance from earlier passes.

## Important review rule

These assignments are **review baselines**, not claims that the original fangames used these exact DS animations. During the move-by-move visual audit, any baseline can be approved, rejected, recolored, combined, or replaced with a custom animation.

## Verification

A repository-level audit confirmed:

- 519 total community moves
- 519 direct DS reuse assignments
- 0 unresolved animation gaps
