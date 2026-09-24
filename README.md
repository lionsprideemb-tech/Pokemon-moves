# Pokémon DS Modern Move & Animation Library

Standalone Nintendo DS move-source library prepared for **Mercury Redux**.

## Verified coverage
This repository mirrors every post-Gen-IV move currently implemented in the pinned hg-engine source snapshot:

| Generation | Move IDs | Count |
|---|---:|---:|
| Gen 5 | 471–562 | 92 |
| Gen 6 | 563–624 | 62 |
| Gen 7 | 625–745 | 121 |
| Gen 8 + Legends: Arceus | 746–853 | 108 |
| Gen 9 + DLC | 854–922 | 69 |
| **Total** | **471–922** | **452** |

**Verified:** 452/452 DS animation scripts and 452/452 matching battle move scripts, with zero missing IDs.

## Primary source
[BluRosie/hg-engine](https://github.com/BluRosie/hg-engine), pinned to commit `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

The hg-engine README permits reuse of its code/assets for free hobby projects provided no money/paywall is involved and credits are retained. Upstream attribution is preserved in `CREDITS_HG_ENGINE.md`.

## Repository layout
- `animations/hg-engine/gen5/` through `gen9/` — canonical DS animation scripts.
- `mechanics/hg-engine/move_scripts/` — matching battle scripts for moves 471–922.
- `support/hg-engine/` — animation macros, move constants/effects headers, move-data support, shared sub-animation source, and hg-engine-provided move SPA support assets.
- `references/hg-engine/` — pinned reference files/documentation useful during the Mercury port.
- `constants/moves_post_gen4.h` — compact modern-move constant list.
- `manifests/moves.csv` — one row per modern move with its animation and mechanics path.
- `manifests/COVERAGE.md` — generation-level coverage summary.
- `scripts/verify_coverage.py` — verifies both 452-file sets.
- `scripts/sync_from_hg_engine.sh` — reproducibly rebuilds the library from the pinned upstream revision.

## Mercury Redux use
Treat this repository as a **source library**, not a ROM build. When Mercury Redux reaches modern move integration, use `manifests/moves.csv` to pull the selected animation + battle script together, then resolve the listed hg-engine support dependencies and test in the Platinum/DS runtime.

No Nintendo DS ROM image or patched commercial ROM is stored here.
