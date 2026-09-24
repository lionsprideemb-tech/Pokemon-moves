# Current Community Move Library — Full Audit Start

Status: **AUDIT LOCKED / NO NEW SOURCE EXPANSION UNTIL CURRENT LIBRARY IS REVIEWED**

Date: 2026-09-24

## Scope correction
The current `manifests/community_moves.csv` contains **519 unique move IDs**, not 516.

The difference is **3 Smogon CAP moves** that are now present in the master catalog in addition to the previously summarized 516-move community collection.

Current source groups:
- Pokémon Elite Redux — 187
- Pokémon Vanguard — 63
- Pokémon Rejuvenation — 43
- Pokémon Uranium — 30
- Pokémon Insurgence — 22
- Pokémon Clover — 58
- Pokémon Opalo — 30
- Pokémon Sage-associated Showdown source — 1
- Pokémon Untamed — 36
- Pokémon Armonia — 46
- Smogon CAP — 3

Total: **519 unique moves**

## New priority
Before adding another community source, audit the current 519 moves for complete mechanics and animation usability.

Each move audit should verify, where the source makes the information available:
- move ID and display name
- source project/repository/commit/path
- type
- category
- base power
- accuracy
- PP
- priority
- target
- contact/non-contact
- major flags and move families/tags
- primary effect
- secondary effect and effect chance
- status/stat changes
- recoil/drain/healing
- multihit or multi-turn rules
- switching, field, weather, terrain, item, ability, or species-specific behavior
- any custom/conditional mechanics
- animation source status
- exact animation mapping/reference when available
- DS-native vs cross-engine status
- recommended Platinum/hg-engine port strategy
- source/license handling notes

## Visual animation audit
Build a move-animation preview gallery alongside the mechanics audit.

Preview states:
1. **Source preview available** — actual source animation can be rendered/captured.
2. **Source mapping only** — exact animation/script/reference exists but still needs a rendered preview.
3. **Reused animation** — source explicitly reuses another move's animation; show that move as the reference preview.
4. **No source animation** — no custom source visual exists; show this clearly rather than inventing one.
5. **DS candidate preview** — after an hg-engine/Platinum analog is selected, render that DS animation for approval.
6. **Custom DS preview** — for moves requiring a new animation, add a test-render preview before implementation is locked.

## Completion rule
A move is not considered fully audited until its mechanics are source-verified and its animation state is classified. If it will be used in Mercury Redux, a visual preview should be available before its final DS animation choice is locked.
