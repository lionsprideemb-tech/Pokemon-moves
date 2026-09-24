# Community Discovery Matrix

Status legend:
- **Seeded (N)** — source-certified non-vanilla moves are already in `community_moves.csv`
- **Pending** — that category still has no discovery from the sources audited so far

## Canonical 18-type coverage

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | **10** | **12** | **2** | **24** |
| Fire | **14** | **8** | **2** | **24** |
| Water | **9** | **2** | **2** | **13** |
| Electric | **10** | **3** | **3** | **16** |
| Grass | **11** | **3** | **3** | **17** |
| Ice | **8** | **3** | **1** | **12** |
| Fighting | **11** | Pending | Pending | **11** |
| Poison | **10** | **3** | **3** | **16** |
| Ground | **14** | **4** | **2** | **20** |
| Flying | **8** | **5** | Pending | **13** |
| Psychic | **7** | **6** | **4** | **17** |
| Bug | **6** | **1** | Pending | **7** |
| Rock | **9** | **4** | Pending | **13** |
| Ghost | **7** | **7** | **2** | **16** |
| Dragon | **11** | **1** | **1** | **13** |
| Dark | **9** | **5** | **2** | **16** |
| Steel | **13** | **3** | **2** | **18** |
| Fairy | **13** | **1** | **1** | **15** |
| **Canonical total** | **180** | **71** | **30** | **281** |

## Source-specific custom types retained

| Custom Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Sound | **6** | **1** | **1** | **8** |
| Qmarks | **1** | **1** | **1** | **3** |
| Shadow | Pending | Pending | **1** | **1** |

**Grand total: 293 unique non-vanilla move designs**
- 187 Physical
- 73 Special
- 33 Status

## Source coverage so far

### Pokémon Elite Redux — All-Type Source Sweep 01
Pinned config commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`

Result: **187** distinct non-vanilla moves across all 18 canonical types.

### Pokémon Vanguard via PokeRover PBS snapshot — All-Type Source Sweep 02
Pinned snapshot commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`

Result: **63** additional unique designs. Vanguard's 8 custom Sound-type moves are preserved source-faithfully.

### Pokémon Rejuvenation via Rejuvenation Wiki Converter — All-Type Source Sweep 03
Pinned converter/database commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`

The converter README describes `DatabaseMoves.txt` as a list of all official and custom moves in Rejuvenation. Official main-series entries, generic official Z-Moves, Orre Shadow moves, aliases/dummies, and master-catalog duplicates were filtered out.

Result: **43** additional unique custom designs:
- 18 Physical
- 19 Special
- 6 Status
- includes Rejuvenation-specific QMARKS and Shadow-typed custom entries, preserved without remapping

Master catalog progression: **187 → 250 → 293**.

This matrix is updated from the canonical master manifest after each source-wide sweep. We do **not** search one type/category cell at a time; remaining gaps are targets for later source projects.
