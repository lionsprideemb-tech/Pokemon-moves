# BULK09 automated validation — complete

Date: 2026-09-24

Range: **1323–1372**  
Candidates: **50**

Automated validation result: **PASS**

- 50/50 provisional IDs present, unique, ordered, and contiguous
- 50/50 symbolic move IDs unique
- 50/50 source-record types recognized
- 50/50 valid Physical / Special / Status categories
- numeric power/accuracy/PP fields parse correctly where used
- **50/50 mechanics-ready**
- **0 mechanics blockers in BULK09**

## Zarzas / Brambles source gap resolved

**1337 — Zarzas (English review name: Brambles)** had been quarantined because the exact residual-damage fraction was not certified from the Opalo data mirror alone.

The follow-up source pass resolved the mismatch:
- Opalo assigns Zarzas effect family **0CF**.
- In the same pinned Opalo table, **Bind, Wrap, Fire Spin, and Sand Tomb** also use 0CF and explicitly describe a **4–5 turn** binding duration.
- Matching legacy Pokémon Essentials `PokeBattle_Move_0CF` implementations define the trapped target's residual damage as **1/16 max HP at the end of each turn**.

That is enough to source-resolve the mechanics without inventing behavior. Zarzas is now `complete` and no longer blocked.

## Source-native custom types

No source-native custom types in this batch.

## Visual workload

- **43** defer visual work until move approval
- **7** post-Gen-4 unique donor certifications after Platinum-native porting
- **0** Platinum/base-era donor spot-check cases
- **0** mechanics blockers

No per-move MP4 sweep is required.

BULK09 is complete under the bulk-validation workflow.
