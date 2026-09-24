# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **15** | **16** | **7** | **38** |
| Fire | **22** | **15** | **6** | **43** |
| Water | **15** | **12** | **2** | **29** |
| Electric | **13** | **9** | **5** | **27** |
| Grass | **21** | **6** | **5** | **32** |
| Ice | **14** | **3** | **5** | **22** |
| Fighting | **15** | **1** | **4** | **20** |
| Poison | **14** | **8** | **4** | **26** |
| Ground | **18** | **9** | **2** | **29** |
| Flying | **13** | **9** | Pending | **22** |
| Psychic | **8** | **17** | **4** | **29** |
| Bug | **7** | **3** | Pending | **10** |
| Rock | **14** | **9** | **1** | **24** |
| Ghost | **14** | **12** | **2** | **28** |
| Dragon | **14** | **5** | **3** | **22** |
| Dark | **16** | **8** | **4** | **28** |
| Steel | **18** | **5** | **3** | **26** |
| Fairy | **20** | **6** | **3** | **29** |
| **Canonical total** | **271** | **153** | **60** | **484** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| ??? | **1** | **1** | Pending | **2** |
| Crystal | **1** | Pending | Pending | **1** |
| Nuclear | **4** | **6** | **2** | **12** |
| Qmarks | **2** | **3** | **2** | **7** |
| Shadow | Pending | Pending | **2** | **2** |
| Sound | **6** | **1** | **1** | **8** |

**Grand total: 516 unique non-vanilla move designs**
- 285 Physical
- 164 Special
- 67 Status

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
Result: **36** imported from `PBS/moves.txt`.
This sweep supplied the first custom **Fighting/Special** entry via **Force Wave**, completing Physical + Special coverage for all 18 canonical types.

### Pokémon Armonia dataset via xorgies/PokemonOpalo — All-Type Source Sweep 11
Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
Source data: `JsonTransformer/txt/armonia/moves.txt`

Result: **46** new designs imported after excluding official/alias rows and collapsing the five same-name **Golpe Bífido** helper records into one catalog design.
- 22 Physical
- 20 Special
- 4 Status
- Includes a source-native Shadow-type status move, **Patronaje**
- No DS-native battle-animation assets were present in the data mirror

A sibling `hispalis/moves.txt` file was also checked: 281 move records, with no non-official IDs surviving the current official/alias filter.

Master catalog progression: **187 → 250 → 293 → 293 → 323 → 345 → 403 → 433 → 434 → 470 → 516**.

This matrix is updated after every source-wide audit. We do **not** search one type/category cell at a time; remaining gaps guide source selection without narrowing the sweep.
