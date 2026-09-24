# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **10** | **14** | **2** | **26** |
| Fire | **16** | **8** | **2** | **26** |
| Water | **9** | **4** | **2** | **15** |
| Electric | **10** | **3** | **4** | **17** |
| Grass | **11** | **3** | **3** | **17** |
| Ice | **8** | **3** | **1** | **12** |
| Fighting | **11** | Pending | Pending | **11** |
| Poison | **10** | **3** | **4** | **17** |
| Ground | **15** | **4** | **2** | **21** |
| Flying | **8** | **6** | Pending | **14** |
| Psychic | **7** | **8** | **4** | **19** |
| Bug | **6** | **1** | Pending | **7** |
| Rock | **9** | **5** | Pending | **14** |
| Ghost | **7** | **7** | **2** | **16** |
| Dragon | **11** | **2** | **1** | **14** |
| Dark | **11** | **5** | **2** | **18** |
| Steel | **15** | **3** | **2** | **20** |
| Fairy | **13** | **1** | **1** | **15** |
| **Canonical total** | **187** | **80** | **32** | **299** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Sound | **6** | **1** | **1** | **8** |
| Qmarks | **1** | **1** | **1** | **3** |
| Shadow | Pending | Pending | **1** | **1** |
| Nuclear | **4** | **6** | **2** | **12** |

**Grand total: 323 unique non-vanilla move designs**
- 198 Physical
- 88 Special
- 37 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`
Result: **187** imported.

### Pokémon Vanguard via PokeRover — All-Type Source Sweep 02
Pinned commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`
Result: **63** imported, including 8 Sound-type designs.

### Pokémon Rejuvenation via Rejuvenation Wiki Converter — All-Type Source Sweep 03
Pinned commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`
Result: **43** imported, including QMARKS/Shadow source-specific records.

### Pokémon Reborn Episode 19.16 snapshot — All-Type Source Sweep 04
Pinned commit: `655411b65ee3fc166c916b6f15c55a398d9daf01`
Result: **0** original named move designs after auditing 771 move records and filtering official move IDs/names. This source is recorded so it will not be pointlessly re-audited.

### Pokémon Uranium 1.3.1 via uranium-mining — All-Type Source Sweep 05
Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
Result: **30** imported:
- 11 Physical
- 15 Special
- 4 Status
- 12 use Uranium's custom Nuclear type

Master catalog progression: **187 → 250 → 293 → 293 → 323**.

This matrix is updated after every source-wide audit. We do **not** search one type/category cell at a time; remaining gaps guide source selection without narrowing the sweep.
