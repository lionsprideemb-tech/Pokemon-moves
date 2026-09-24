# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

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

## Source-specific custom types retained

Vanguard defines a non-canonical **Sound** type. These designs are preserved source-faithfully instead of being silently remapped:

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Sound | **6** | **1** | **1** | **8** |

**Grand total: 250 unique non-vanilla move designs**
- 169 Physical
- 54 Special
- 27 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned config commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`

Result: **187** distinct non-vanilla moves across all 18 canonical types.

### Pokémon Vanguard via PokeRover PBS snapshot — All-Type Source Sweep 02
Pinned snapshot commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`

PokeRover states that its bundled PBS files are from Pokémon Vanguard patch 3.0.16.

Result after official-move filtering and source-local deduplication:
- 64 custom PBS sections identified
- 63 unique custom move designs retained
- 55 designs use canonical Pokémon types
- 8 designs use Vanguard's custom Sound type
- Master catalog increased from **187 → 250** unique designs

This matrix is updated from the canonical master manifest after each source-wide sweep. We do **not** search one type/category cell at a time; remaining gaps are targets for later source projects.
