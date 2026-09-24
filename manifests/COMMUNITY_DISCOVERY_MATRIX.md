# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **15** | **16** | **6** | **37** |
| Fire | **19** | **12** | **5** | **36** |
| Water | **12** | **8** | **2** | **22** |
| Electric | **11** | **7** | **5** | **23** |
| Grass | **18** | **5** | **5** | **28** |
| Ice | **14** | **3** | **4** | **21** |
| Fighting | **14** | **1** | **4** | **19** |
| Poison | **13** | **6** | **4** | **23** |
| Ground | **17** | **7** | **2** | **26** |
| Flying | **11** | **8** | Pending | **19** |
| Psychic | **8** | **16** | **4** | **28** |
| Bug | **6** | **3** | Pending | **9** |
| Rock | **12** | **8** | **1** | **21** |
| Ghost | **12** | **12** | **2** | **26** |
| Dragon | **14** | **5** | **3** | **22** |
| Dark | **16** | **8** | **4** | **28** |
| Steel | **18** | **5** | **3** | **26** |
| Fairy | **19** | **3** | **3** | **25** |
| **Canonical total** | **249** | **133** | **57** | **439** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| ??? | **1** | **1** | Pending | **2** |
| Crystal | **1** | Pending | Pending | **1** |
| Nuclear | **4** | **6** | **2** | **12** |
| Qmarks | **2** | **3** | **2** | **7** |
| Shadow | Pending | Pending | **1** | **1** |
| Sound | **6** | **1** | **1** | **8** |

**Grand total: 470 unique non-vanilla move designs**
- 263 Physical
- 144 Special
- 63 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`
Result: **187** imported.

### Pokémon Vanguard via PokeRover — All-Type Source Sweep 02
Pinned commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`
Result: **63** imported.

### Pokémon Rejuvenation via Rejuvenation Wiki Converter — All-Type Source Sweep 03
Pinned commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`
Result: **43** imported.

### Pokémon Reborn Episode 19.16 snapshot — All-Type Source Sweep 04
Pinned commit: `655411b65ee3fc166c916b6f15c55a398d9daf01`
Result: **0** imported.

### Pokémon Uranium 1.3.1 via uranium-mining — All-Type Source Sweep 05
Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
Result: **30** imported.

### Pokémon Insurgence via Insurgence-Showdown — All-Type Source Sweep 06
Pinned commit: `72d72a7af4642d3c8391ab1118f0afbb2647020b`
Result: **22** imported.

### Pokémon Clover via Clovermon Showdown — All-Type Source Sweep 07
Pinned commit: `008196c839c1efe859e2d59c092c88370b7752d6`
Result: **58** imported.

### Pokémon Opalo via xorgies/PokemonOpalo — All-Type Source Sweep 08
Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
Result: **30** imported.

### Pokémon Sage-associated Showdown fork — All-Type Source Sweep 09
Pinned commit: `f6757adccfc138272f10e738afdc36472387e646`
Result: **1** imported: Magikarp's Revenge.

### Pokémon Untamed — All-Type Source Sweep 10
Pinned commit: `8d757cdeb132c947602dce6a9f327fc5883e84c2`
Result: **36** imported from `PBS/moves.txt`:
- 12 Physical
- 19 Special
- 5 Status
- 32 canonical-type designs
- 4 Qmarks-type designs

Filtering excluded:
- official Struggle
- internal support/dummy records `SUPERNOVA_ALT` and `PREMONITIONMOVE`
- four designs already in the master catalog: Venom Strike, Erosion Wave, Ow The Edge, Think Fast

**Important coverage milestone:** Fighting now has both Physical **and Special** custom-move coverage via **Force Wave**.

Master catalog progression: **187 → 250 → 293 → 293 → 323 → 345 → 403 → 433 → 434 → 470**.

This matrix is updated after every source-wide audit. We do **not** search one type/category cell at a time; remaining gaps guide source selection without narrowing the sweep.
