# DS Modern Move Coverage

Primary source snapshot: BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce

| Generation | Move IDs | Animation scripts | Mechanics scripts | Certification |
|---|---:|---:|---:|---|
| Gen 5 | 471–562 | 92/92 | 92/92 | ✅ Phase A certified |
| Gen 6 | 563–624 | 62/62 | 62/62 | ✅ Phase B certified |
| Gen 7 | 625–745 | 121 | pending audit | Pending |
| Gen 8 + Legends: Arceus | 746–853 | 108 | pending audit | Pending |
| Gen 9 + DLC | 854–922 | 69 | pending audit | Pending |
| **Total** | **471–922** | **452** |  |  |

## Certification method

For completed phases:
- Every expected move ID is present.
- The stored DS animation script blob matches the pinned hg-engine source blob exactly.
- A matching move battle/mechanics script is present under `mechanics/hg-engine/move_scripts/`.

The pinned hg-engine snapshot contains a dedicated DS animation script for every ID from 471 through 922.

## Completed phases

### Phase A — Generation 5
- IDs: 471–562
- Animation coverage: 92/92
- Source hash mismatches: 0
- Mechanics coverage: 92/92
- Missing IDs: none

### Phase B — Generation 6
- IDs: 563–624
- Animation coverage: 62/62
- Source hash mismatches: 0
- Mechanics coverage: 62/62
- Missing IDs: none
