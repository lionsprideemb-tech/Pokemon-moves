# Pokémon DS Modern Move & Animation Library

Standalone source library for **Mercury Redux** and other Nintendo DS Pokémon projects.

## Scope
- DS-native battle animation scripts for every post-Gen IV move currently implemented by hg-engine.
- Move IDs **471–922**: **452 modern moves**, covering Gen 5 through Gen 9.
- Matching move constants and an import manifest.
- The animation-script macro support required to read/port the scripts.
- No ROM, commercial game binary, or extracted ROM image is stored here.

## Coverage
| Generation | DS move IDs | Count |
|---|---:|---:|
| Gen 5 | 471–562 | 92 |
| Gen 6 | 563–624 | 62 |
| Gen 7 | 625–745 | 121 |
| Gen 8 | 746–853 | 108 |
| Gen 9 | 854–922 | 69 |
| **Total** | **471–922** | **452** |

Every ID in that range has a corresponding animation script in the pinned source snapshot.

## Primary source
[BluRosie/hg-engine](https://github.com/BluRosie/hg-engine), pinned to commit `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

hg-engine's README permits reuse of its code/assets for free hobby projects provided no money/paywall is involved and credits are retained. The upstream credits are mirrored in `CREDITS_HG_ENGINE.md`.

## Layout
- `animations/hg-engine/` — DS move animation scripts 471–922
- `support/animscriptcmd.s` — hg-engine animation script command macros
- `constants/moves_post_gen4.h` — post-Gen IV move constants from the pinned snapshot
- `manifests/moves.csv` — ID, constant, generation, source path, pinned commit
- `SOURCE_POLICY.md` — what is and is not stored here

## Mercury Redux use
Treat this repository as a source library, not as the game build. When Mercury Redux is ready for modern battle effects, import only the chosen scripts and required support into the DS engine, then test them in-engine.

## Status
Initial collection target: official post-Gen IV move animations implemented for Nintendo DS by hg-engine.
