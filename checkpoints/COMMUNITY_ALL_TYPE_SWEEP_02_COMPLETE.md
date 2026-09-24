# Community Discovery — All-Type Source Sweep 02 Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Completed:
- Audited the Pokémon Vanguard PBS snapshot bundled with PokeRover at commit `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`.
- Filtered official moves against Pokémon Essentials plus the repository's hg-engine modern-move baseline.
- Identified 64 custom PBS sections.
- Collapsed one duplicate Code:Power design.
- Imported **63 new unique designs** into `manifests/community_moves.csv`.
- Master catalog now contains **250 unique non-vanilla moves**.
- Overall category totals are **169 Physical / 54 Special / 27 Status**.
- Canonical 18-type designs total **242**.
- Preserved **8 Vanguard Sound-type moves** separately without silently remapping their type.
- No duplicate move IDs or move names remain in the master manifest.
- Animation availability remains pending for Vanguard because the PokeRover PBS snapshot exposes mechanics but not animation assets/scripts.

Next:
**All-Type Source Sweep 03** — locate and audit the next public hack/fangame/decomp source, import all distinct original moves in one pass, and deduplicate against the 250-move master catalog.
