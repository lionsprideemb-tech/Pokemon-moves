# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **14** | **16** | **5** | **35** |
| Fire | **18** | **11** | **5** | **34** |
| Water | **12** | **5** | **2** | **19** |
| Electric | **10** | **7** | **5** | **22** |
| Grass | **17** | **4** | **5** | **26** |
| Ice | **12** | **3** | **2** | **17** |
| Fighting | **14** | Pending | **3** | **17** |
| Poison | **13** | **6** | **4** | **23** |
| Ground | **17** | **6** | **2** | **25** |
| Flying | **11** | **7** | Pending | **18** |
| Psychic | **8** | **13** | **4** | **25** |
| Bug | **6** | **2** | Pending | **8** |
| Rock | **11** | **7** | **1** | **19** |
| Ghost | **11** | **11** | **2** | **24** |
| Dragon | **14** | **3** | **3** | **20** |
| Dark | **16** | **8** | **4** | **28** |
| Steel | **17** | **4** | **3** | **24** |
| Fairy | **17** | **3** | **3** | **23** |
| **Canonical total** | **238** | **116** | **53** | **407** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| ??? | **1** | **1** | Pending | **2** |
| Crystal | **1** | Pending | Pending | **1** |
| Nuclear | **4** | **6** | **2** | **12** |
| Qmarks | **1** | **1** | **1** | **3** |
| Shadow | Pending | Pending | **1** | **1** |
| Sound | **6** | **1** | **1** | **8** |

**Grand total: 434 unique non-vanilla move designs**
- 251 Physical
- 125 Special
- 58 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`
Result: **187** imported.

### Pokémon Vanguard via PokeRover — All-Type Source Sweep 02
Pinned commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`
Result: **63** imported, including 8 Sound-type designs.

### Pokémon Rejuvenation via Rejuvenation Wiki Converter — All-Type Source Sweep 03
Pinned commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`
Result: **43** imported, including Qmarks/Shadow source-specific records.

### Pokémon Reborn Episode 19.16 snapshot — All-Type Source Sweep 04
Pinned commit: `655411b65ee3fc166c916b6f15c55a398d9daf01`
Result: **0** original named move designs after auditing 771 move records and filtering official move IDs/names.

### Pokémon Uranium 1.3.1 via uranium-mining — All-Type Source Sweep 05
Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
Result: **30** imported, including 12 Nuclear-type designs.

### Pokémon Insurgence via Insurgence-Showdown — All-Type Source Sweep 06
Pinned commit: `72d72a7af4642d3c8391ab1118f0afbb2647020b`
Result: **22** imported after direct diff against upstream Pokémon Showdown.

### Pokémon Clover via Clovermon Showdown — All-Type Source Sweep 07
Pinned commit: `008196c839c1efe859e2d59c092c88370b7752d6`
Result: **58** imported after direct diff against upstream Pokémon Showdown.
Two fork-specific records, **Inverse Room** and **Scorched Earth**, were already present in the master catalog and were not duplicated.
This sweep added:
- 33 Physical
- 16 Special
- 9 Status
- 56 canonical-type designs
- 2 source-native `???`-type designs

### Pokémon Opalo via xorgies/PokemonOpalo — All-Type Source Sweep 08
Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`

The repository is a data-conversion/web project for Pokémon Opalo and includes the Spanish move table at `JsonTransformer/txt/opalo/moves.txt`.

Result: **30** new non-vanilla designs imported after excluding official/translated aliases such as High Jump Kick, Smelling Salts, Struggle, Dual Wingbeat, Liquidation, Flip Turn, First Impression, Smart Strike, Scorching Sands, High Horsepower, Pollen Puff, Psychic Fangs, Darkest Lariat, Accelerock, Lunge, and Fire Lash.

Sweep 08 added:
- 14 Physical
- 15 Special
- 1 Status
- all 30 use canonical Pokémon types

Master catalog progression: **187 → 250 → 293 → 293 → 323 → 345 → 403 → 434**.

This matrix is updated after every source-wide audit. We do **not** search one type/category cell at a time; remaining gaps guide source selection without narrowing the sweep.
