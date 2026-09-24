# Secondary Nintendo DS Move/Animation Source Audit

Checkpoint: 2026-09-24

## Goal
Find Nintendo DS Pokémon projects that contain non-vanilla move implementations or battle animations not already present in the pinned hg-engine snapshot used by this repository.

## Primary result
The pinned hg-engine snapshot remains the only public GitHub source found in this pass with the full DS animation scripting system plus contiguous modern move coverage through move ID 922.

## hg-engine-derived hacks checked
The following public repositories were checked for move constants and animation IDs beyond the upstream set:

- B-Kiraly/Benndots-HGengine-ROMhack
- MicheleBiena/ShadowsOfTime
- zenmodeman/Contemporary-HeartGold
- CrescentsChaos/rom-hack-hge
- clumsycatgirl/pokemon-heart-gold-rom-hack

For each of these repositories:
- the highest animation ID found was 922;
- no move animation IDs above 922 were found;
- the move constants matched hg-engine's 0-922 ID/name map in the checked snapshot.

These projects are therefore not mirrored here as separate move packs, because doing so would only duplicate the primary hg-engine source.

## Other DS resources found
- DameNavarro/HGEngineGUI — useful editing/tooling reference for hg-engine moves.
- hzla/HG-Engine-Dumps — useful engine dump/reference material.
- BluRosie/hg-mega-evolution — older DS engine/reference work.

No independent public custom-move animation pack was identified from the broader searches for:
- loadparticlefromspa
- animscriptcmd.s
- move_sub_anim
- armips/move/move_anim

## Repository policy
If a future DS project is found with genuinely unique custom moves or animations:
1. verify provenance and reuse terms;
2. place reusable content under `community/<source>/`;
3. keep ROM-extracted commercial assets out of this repository unless redistribution is clearly permitted;
4. record source commit and credits;
5. keep Mercury-original moves under a separate `mercury-original/` namespace.

## Current conclusion
For practical Mercury Redux development, the hg-engine collection in this repository is currently the strongest complete DS-native base:
- 452 post-Gen-IV animations (471-922)
- 452 matching move battle scripts
- animation macros, move sub-animations and SPA support
- move/effect constants and move-data headers
- animation and move-data documentation
