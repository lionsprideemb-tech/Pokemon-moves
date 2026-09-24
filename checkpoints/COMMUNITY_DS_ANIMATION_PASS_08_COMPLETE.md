# DS Animation Source Pass 08 — Pokémon Opalo Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Pokémon Opalo move data via `xorgies/PokemonOpalo`
- Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
- 30 Opalo custom move designs already present in `manifests/community_moves.csv`
- Source move table: `JsonTransformer/txt/opalo/moves.txt`

Verified result:
- **30/30** Opalo custom moves audited for animation-source availability.
- The pinned source exposes move-definition/mechanics data but no source-certified move-animation assets or per-move visual mappings for these custom moves.
- Repository-wide searches for `animation`, `move animation`, `battle animation`, `anim`, `moveanimations`, `Animations.rxdata`, and `PkmnAnimations` returned no matching animation evidence.
- The pinned `moves.txt` records move data/mechanics; no DS visual asset path is supplied.
- **0 direct DS animation mappings** can be source-certified from this repository.
- **30 moves remain animation-unassigned** from the Opalo source.
- No animation was guessed or falsely attributed.

Implementation guidance:
- These 30 moves can later be matched to existing Platinum/hg-engine animations where the visual fit is strong.
- Only moves without a convincing existing DS visual analog should need new animation work.

Output:
- `manifests/OPALO_DS_ANIMATION_PASS_08.csv`

Next:
**DS Animation Source Pass 09 — Pokémon Sage-associated Showdown source.**
