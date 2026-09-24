# DS Animation Source Pass 10 — Pokémon Untamed Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Pokémon Untamed via `untamed-team/project-untamed`
- Pinned commit: `8d757cdeb132c947602dce6a9f327fc5883e84c2`
- 36 Untamed custom move designs already present in `manifests/community_moves.csv`
- Move definitions: `PBS/moves.txt`
- Move-to-animation map: `Data/move2anim.dat`
- Animation database: `Data/PkmnAnimations.rxdata`

Verified result:
- **36/36** Untamed custom moves audited for animation-source availability.
- Unlike several earlier simulator/data-only sources, Untamed includes a real Pokémon Essentials/RGSS battle-animation system and a compiled move-to-animation mapping table.
- The pinned `Data/move2anim.dat` was decoded and checked directly.
- **10/36** custom moves have source-certified direct animation mappings.
- **26/36** have no direct player/opponent entry in the pinned move-to-animation table.
- **0/36 are DS-native**; the 10 mapped animations are cross-engine source references that must be recreated/converted for Platinum/hg-engine.
- No unmapped move was assigned an animation by guesswork.

Source-certified mappings:
- `HARDDRIVECRASH` → player 1144; source also layers common animation `HardDriveCrash`
- `MYSTICBLADE` → player 1145 / opponent 1146
- `FORGEBREATH` → player 1147
- `SLIMESHOT` → player 1149 / opponent 1150
- `CRIMSONSURGE` → player 1151 / opponent 1152
- `CHILLINGWAIL` → player 1153
- `HAUNT` → player 1154 / opponent 1155
- `JOLTKICK` → player 1156
- `SWEETTOOTH` → player 1158
- `PSYSONIC` → player 1159 / opponent 1160

Mapping semantics:
- `Data/Scripts/011_Battle/003_Scene/004_Scene_PlayAnimations.rb` confirms `move2anim[0]` is the player-side animation map and `move2anim[1]` is the opposing-side map.
- `Data/PkmnAnimations.rxdata` is present in the pinned source, but it is an RGSS/Pokémon Essentials animation database rather than a Nintendo DS animation-script format.
- The source repository has no general reuse license at the audited revision, so the Mercury library records exact source references rather than copying the animation assets.

Output:
- `manifests/UNTAMED_DS_ANIMATION_PASS_10.csv`

Next:
**DS Animation Source Pass 11 — Pokémon Armonia.**
