# Community Discovery Matrix

Status legend:
- **N** — source-certified non-vanilla moves already in `community_moves.csv`
- **Pending** — no move in that category has been found in the sources audited so far

## Canonical Pokémon types

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **10** | **7** | **2** | **19** |
| Fire | **13** | **6** | **2** | **21** |
| Water | **8** | **2** | **1** | **11** |
| Electric | **8** | **3** | **3** | **14** |
| Grass | **10** | **2** | **3** | **15** |
| Ice | **8** | **1** | **1** | **10** |
| Fighting | **9** | Pending | Pending | **9** |
| Poison | **7** | **3** | **3** | **13** |
| Ground | **14** | **3** | Pending | **17** |
| Flying | **7** | **4** | Pending | **11** |
| Psychic | **7** | **4** | **4** | **15** |
| Bug | **5** | Pending | Pending | **5** |
| Rock | **8** | **4** | Pending | **12** |
| Ghost | **6** | **6** | **2** | **14** |
| Dragon | **11** | **1** | **1** | **13** |
| Dark | **9** | **4** | **2** | **15** |
| Steel | **11** | **2** | **2** | **15** |
| Fairy | **12** | **1** | Pending | **13** |
| **Canonical total** | **163** | **53** | **26** | **242** |

## Source-native custom types

Some fangames introduce their own type systems. These are retained source-faithfully instead of being forced into one of the canonical 18 types.

| Source type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Sound | **6** | **1** | **1** | **8** |

**Grand catalog total: 250 unique community move designs — 169 Physical, 54 Special, 27 Status.**

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned config commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`

Result: **187** source-certified non-vanilla moves across all 18 canonical types.

### Pokémon Vanguard — All-Type Source Sweep 02
Data source: Vanguard PBS snapshot bundled with PokeRover.
Pinned PokeRover commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`

Result: **63 unique custom move designs** after filtering official Pokémon moves and deduplicating a repeated Code:Power definition. Of these, 55 use canonical types and 8 use Vanguard's custom Sound type.

This matrix is updated after each **source-wide** sweep. Empty cells are useful gap signals, but they do not change the workflow into one-cell-at-a-time searching.
