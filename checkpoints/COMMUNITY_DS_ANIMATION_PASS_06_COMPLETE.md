# DS Animation Source Pass 06 — Pokémon Insurgence Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Pokémon Insurgence mechanics via `Poilerwags/Insurgence-Showdown`
- Pinned commit: `72d72a7af4642d3c8391ab1118f0afbb2647020b`
- 22 Insurgence custom move designs already present in `manifests/community_moves.csv`

Verified result:
- **22/22** Insurgence custom moves audited for animation-source availability.
- The audited repository is a Pokémon Showdown battle-simulator fork focused on mechanics/data.
- Repository-wide searches for `animation`, `move animation`, `battle animation`, and `anim` returned no move-animation assets or per-custom-move visual mappings.
- **0 direct DS animation mappings** can be source-certified from this repository.
- **22 moves remain animation-unassigned** from the Insurgence source.
- No animation was guessed or falsely attributed.

Implementation guidance:
- These 22 moves can later be matched to existing Platinum/hg-engine animations where the visual fit is strong.
- Only moves without a convincing existing DS visual analog should need new animation work.

Output:
- `manifests/INSURGENCE_DS_ANIMATION_PASS_06.csv`

Next:
**DS Animation Source Pass 07 — Pokémon Clover**.
