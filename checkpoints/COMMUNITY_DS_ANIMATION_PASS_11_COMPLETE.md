# DS Animation Source Pass 11 — Pokémon Armonia Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Pokémon Armonia move dataset via `xorgies/PokemonOpalo`
- Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
- 46 Armonia custom move designs already present in `manifests/community_moves.csv`
- Source move table: `JsonTransformer/txt/armonia/moves.txt`
- Pinned source-file blob: `33aab4a6ab50a3928fbcd851e3d75954b7c64f98`

Verified result:
- **46/46** Armonia custom moves audited for animation-source availability.
- The Armonia mirror provides move-definition/mechanics data, but no source-certified battle-animation assets or per-move visual mappings.
- Repository-wide searches for `animation`, `move animation`, `battle animation`, `anim`, `PkmnAnimations`, and `Animations.rxdata` returned no matching animation evidence.
- **0 direct DS animation mappings** can be source-certified from this repository.
- **46 moves remain animation-unassigned** from the Armonia source.
- No animation was guessed or falsely attributed.

Implementation guidance:
- These 46 moves can later be matched to existing Platinum/hg-engine animations where the visual fit is strong.
- Only moves without a convincing DS visual analog should need new animation work.
- Source-specific typing such as `Shadow` remains preserved and should not be silently remapped during animation selection.

Output:
- `manifests/ARMONIA_DS_ANIMATION_PASS_11.csv`

Next:
**DS Animation Source Pass 12 — audit the next community-move source beyond the eleven completed source sets.**
