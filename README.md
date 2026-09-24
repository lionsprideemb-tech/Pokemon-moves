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


## Current mission: community-created move discovery

The official Gen 5–9 baseline is already preserved above. New work in this repository now focuses on **non-vanilla/community-created moves and animations** that can expand Mercury Redux's movepool instead of re-auditing official moves that hg-engine already provides.

### Full collection scope

**Physical Electric was only the first discovery batch, not the project scope.**

The master target is to collect and source-certify community-created moves across **all 18 Pokémon types**:

- Normal
- Fire
- Water
- Electric
- Grass
- Ice
- Fighting
- Poison
- Ground
- Flying
- Psychic
- Bug
- Rock
- Ghost
- Dragon
- Dark
- Steel
- Fairy

For every type, collect **Physical and Special moves**. Community-created **Status moves are also retained** so the library does not accidentally discard useful non-damaging designs.

Discovery is source-wide rather than type-locked: when a public hack/fangame/decomp source is audited, extract all distinct custom moves from that source across every type/category in one pass, then deduplicate them into `manifests/community_moves.csv`.

For every discovered move, record:
- source project/repository and pinned commit
- move name, type, category, power, accuracy, PP, mechanics/effects
- gameplay-role tags
- exact source data path
- animation evidence/reference
- license/reuse status
- DS portability / conversion requirements
- notes needed for later Mercury Redux implementation

Priorities:
- Prefer DS-native/HG-Engine-compatible resources when they exist.
- Cross-engine moves are still indexed when the concept/mechanics are valuable, but their animations are marked as requiring DS conversion.
- Do not copy source code/assets from repositories without a clear reuse license; index exact source paths/commits instead.
- Avoid duplicate concepts and duplicate move definitions while preserving materially different implementations.

See:
- `docs/COMMUNITY_COLLECTION_SCOPE.md`
- `manifests/COMMUNITY_DISCOVERY_MATRIX.md`
- `manifests/community_moves.csv`

Current source-wide result: **434 unique non-vanilla move designs** after nine completed source-wide audits:

- Pokémon Elite Redux: +187
- Pokémon Vanguard via PokeRover: +63
- Pokémon Rejuvenation via Rejuvenation Wiki Converter: +43
- Pokémon Reborn Episode 19.16: +0 (audited and recorded)
- Pokémon Uranium 1.3.1 via uranium-mining: +30
- Pokémon Insurgence via Insurgence-Showdown: +22
- Pokémon Clover via Clovermon Showdown: +58
- Pokémon Opalo via xorgies/PokemonOpalo: +30
- Pokémon Sage via Pokemon-Showdown-Sage: +1

Current master totals: **251 Physical, 125 Special, 58 Status**. Source-specific custom types including Sound, Qmarks, Shadow, Nuclear, Crystal, and ??? are preserved without silently remapping them.

Next restart point: **All-Type Source Sweep 10** — audit the next public project as a whole and deduplicate its custom moves against the 434-move master catalog.
