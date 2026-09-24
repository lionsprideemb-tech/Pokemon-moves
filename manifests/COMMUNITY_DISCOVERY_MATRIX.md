# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **13** | **14** | **5** | **32** |
| Fire | **17** | **10** | **5** | **32** |
| Water | **11** | **5** | **2** | **18** |
| Electric | **10** | **5** | **5** | **20** |
| Grass | **15** | **4** | **5** | **24** |
| Ice | **10** | **3** | **2** | **15** |
| Fighting | **14** | Pending | **3** | **17** |
| Poison | **13** | **5** | **4** | **22** |
| Ground | **17** | **4** | **2** | **23** |
| Flying | **10** | **6** | Pending | **16** |
| Psychic | **8** | **11** | **4** | **23** |
| Bug | **6** | **2** | Pending | **8** |
| Rock | **10** | **7** | **1** | **18** |
| Ghost | **10** | **8** | **2** | **20** |
| Dragon | **14** | **3** | **3** | **20** |
| Dark | **13** | **8** | **3** | **24** |
| Steel | **16** | **4** | **3** | **23** |
| Fairy | **16** | **2** | **3** | **21** |
| **Canonical total** | **223** | **101** | **52** | **376** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| ??? | **1** | **1** | Pending | **2** |
| Crystal | **1** | Pending | Pending | **1** |
| Nuclear | **4** | **6** | **2** | **12** |
| Qmarks | **1** | **1** | **1** | **3** |
| Shadow | Pending | Pending | **1** | **1** |
| Sound | **6** | **1** | **1** | **8** |

**Grand total: 403 unique non-vanilla move designs**
- 236 Physical
- 110 Special
- 57 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`
Result: **187** imported.

### Pokémon Vanguard via PokeRover — All-Type Source Sweep 02
Pinned commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`
Result: **63** imported, including 8 Sound-type designs.

### Pokémon Rejuvenation via Rejuvenation Wiki Converter — All-Type Source Sweep 03
Pinned commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`
Result: **43** imported.

### Pokémon Reborn Episode 19.16 snapshot — All-Type Source Sweep 04
Pinned commit: `655411b65ee3fc166c916b6f15c55a398d9daf01`
Result: **0** imported after official filtering.

### Pokémon Uranium 1.3.1 via uranium-mining — All-Type Source Sweep 05
Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
Result: **30** imported, including 12 Nuclear-type designs.

### Pokémon Insurgence via Insurgence-Showdown — All-Type Source Sweep 06
Pinned commit: `72d72a7af4642d3c8391ab1118f0afbb2647020b`
Result: **22** imported, including 1 Crystal-type design.

### Pokémon Clover via Clovermon Showdown — All-Type Source Sweep 07
Pinned commit: `008196c839c1efe859e2d59c092c88370b7752d6`
Result after direct diff against upstream Pokémon Showdown:
- 60 fork-specific move designs identified
- 2 already present in the master catalog: Inverse Room and Scorched Earth
- **58 new designs imported**
- 33 Physical
- 16 Special
- 9 Status
- 2 use Clover's source-native `???` type

Master catalog progression: **187 → 250 → 293 → 293 → 323 → 345 → 403**.

This matrix is updated after every source-wide audit. We do **not** search one type/category cell at a time; remaining gaps guide source selection without narrowing the sweep.
