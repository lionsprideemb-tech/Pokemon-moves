# DS Animation Source Pass 07 — Pokémon Clover Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Pokémon Clover mechanics via `Squeetz/clovermon-showdown`
- Pinned commit: `008196c839c1efe859e2d59c092c88370b7752d6`
- 58 Clover custom move designs already present in `manifests/community_moves.csv`

Verified result:
- **58/58** Clover custom moves audited for animation-source availability.
- The pinned Clovermon Showdown commit is the repository's latest audited commit and is a Pokémon Showdown battle-simulator fork focused on mechanics/data.
- Repository-wide searches for `animation`, `move animation`, `battle animation`, and `anim` returned no move-animation assets or per-custom-move visual mappings.
- **0 direct DS animation mappings** can be source-certified from this repository.
- **58 moves remain animation-unassigned** from the Clover source.
- No animation was guessed or falsely attributed.

Implementation guidance:
- These 58 moves can later be matched to existing Platinum/hg-engine animations where the visual fit is strong.
- Only moves without a convincing existing DS visual analog should need new animation work.

Output:
- `manifests/CLOVER_DS_ANIMATION_PASS_07.csv`

Next:
**DS Animation Source Pass 08 — Pokémon Opalo.**
