# Elite Redux All-Type Source Sweep 01

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project: Pokémon Elite Redux
- Repository: `Elite-Redux/er-config`
- Pinned commit: `e32616fea6ccf5245096d8d7eeb54f0f5ac0b2a7`
- Data source: `MoveList.textproto`
- Repository-level license file: not detected at the pinned revision
- Copy policy: metadata/provenance only unless reuse permission is confirmed

## Result

The first true all-type sweep identified and imported **187 non-vanilla moves** after filtering the Elite Redux move enum against the repository's official modern-move baseline.

Category totals:
- **130 Physical**
- **37 Special**
- **20 Status**
- **187 total**

All **18 Pokémon types** are represented.

The canonical entries are now stored in:
- `manifests/community_moves.csv`
- `manifests/COMMUNITY_DISCOVERY_MATRIX.md`

## Type totals

| Type | Physical | Special | Status | Total |
|---|---:|---:|---:|---:|
| Normal | 8 | 4 | 2 | 14 |
| Fire | 9 | 4 | 0 | 13 |
| Water | 6 | 1 | 1 | 8 |
| Electric | 8 | 2 | 2 | 12 |
| Grass | 9 | 0 | 2 | 11 |
| Ice | 6 | 1 | 1 | 8 |
| Fighting | 6 | 0 | 0 | 6 |
| Poison | 5 | 2 | 3 | 10 |
| Ground | 11 | 2 | 0 | 13 |
| Flying | 6 | 3 | 0 | 9 |
| Psychic | 6 | 3 | 3 | 12 |
| Bug | 5 | 0 | 0 | 5 |
| Rock | 8 | 3 | 0 | 11 |
| Ghost | 4 | 5 | 2 | 11 |
| Dragon | 7 | 1 | 1 | 9 |
| Dark | 9 | 4 | 2 | 15 |
| Steel | 8 | 1 | 1 | 10 |
| Fairy | 9 | 1 | 0 | 10 |

## Animation handling

Where the Elite Redux move record explicitly names `uses_animation`, the master manifest records that reference immediately. Moves without a directly linked animation are marked for the separate animation-source audit rather than being falsely labeled DS-ready.

Existing source-certified animation evidence for Smite and Shocking Jab remains preserved.

Because Elite Redux is GBA/pokeemerald-derived, its custom animation code is a **reference for DS recreation/conversion**, not a claim of native Nintendo DS compatibility.

## Next restart point

**All-Type Source Sweep 02** — audit another public project source-wide and import every distinct non-vanilla move across all types/categories, deduplicating against these 187.
