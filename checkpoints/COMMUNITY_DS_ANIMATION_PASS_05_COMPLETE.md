# DS Animation Source Pass 05 — Pokémon Uranium Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Primary source:
- Pokémon Uranium 1.3.1 data via `eriedaberrie/uranium-mining`
- Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
- 30 Uranium custom move designs already present in `manifests/community_moves.csv`

Secondary implementation check:
- `acedogblast/Project-Uranium-Godot`
- Pinned commit: `46776724aa60af7a08685912f335f0c50d1f33f5`
- 93 move implementation files present in its battle move database
- Only **2** of the 30 cataloged Uranium custom moves match implemented move files there:
  - **Sky Fall**
  - **Flame Impact**
- Those files confirm mechanics, but contain no move-animation field/reference.
- The Godot repository contains generic battle/UI animations, but no source-certified per-move animation mapping for these Uranium customs.

Verified result:
- **30/30** Uranium custom moves audited.
- **0 direct DS animation mappings** can be source-certified from the available public Uranium sources.
- **30 moves remain animation-unassigned**.
- No visual animation was guessed from move name/type.

Output:
- `manifests/URANIUM_DS_ANIMATION_PASS_05.csv`

Next:
**DS Animation Source Pass 06 — Pokémon Insurgence**.
