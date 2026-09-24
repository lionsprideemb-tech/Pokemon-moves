# Community Discovery — All-Type Source Sweep 09 Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Completed:
- Audited `SageFox/Pokemon-Showdown-Sage` at pinned commit `f6757adccfc138272f10e738afdc36472387e646`.
- Compared its legacy `data/moves.js` against modern upstream Showdown and the official move baseline.
- Excluded the `VICEGRIP` spelling alias for official Vise Grip.
- Rejected nested object keys that are not move records.
- Imported **1** genuine fork-specific design: **Magikarp's Revenge**.
- Master catalog increased from **433 → 434**.
- Current totals: **251 Physical / 125 Special / 58 Status**.
- Duplicate normalized move IDs: **0**.
- Duplicate normalized move names: **0**.

Next:
**All-Type Source Sweep 10** — audit another public project and deduplicate against the 434-design master catalog.
