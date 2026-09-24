# DS Animation Source Pass 01 — Elite Redux Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source set:
- Pokémon Elite Redux community moves already cataloged in `manifests/community_moves.csv`
- 187 Elite Redux custom moves audited
- Output: `manifests/ELITE_REDUX_DS_ANIMATION_PASS_01.csv`

Verified result:
- **187/187** Elite Redux custom moves classified for DS animation handling
- **93** can directly reuse a vanilla Platinum/base-era DS animation
- **51** can directly reuse a modern hg-engine DS animation already stored in this repository
- **144 total** therefore already have a direct Nintendo DS animation reuse route
- **2** have source-certified custom GBA animation evidence and need DS recreation/conversion
- **2** reuse another custom Elite Redux move's animation and need the custom chain followed during conversion
- **7** explicitly use no source animation and require a new/adapted DS animation
- **32** have no source-certified animation linkage yet and require selection or a dedicated animation audit
- **0 unresolved references** after normalized official/custom reference matching

Next:
**DS Animation Source Pass 02** — process the next community source as one complete source, map any reusable official DS animations, and isolate only the moves that genuinely need new DS animation work.
