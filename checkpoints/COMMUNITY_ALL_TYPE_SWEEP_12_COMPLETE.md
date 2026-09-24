# Community Discovery — All-Type Source Sweep 12 Complete

Status: **CHECKPOINT LOCKED**

Date: 2026-09-24

Source:
- Smogon CAP move definitions in `smogon/pokemon-showdown`
- Pinned commit: `a5df8274e85b0889bf2a9b3422a08b39732374fc`
- Source file: `data/moves.ts`

Completed:
- Audited all move records explicitly marked `isNonstandard: "CAP"`.
- Imported **3 new unique community-created move designs**:
  - **Paleo Wave** — Rock / Special / 85 BP / 100% / 15 PP; 20% chance to lower Attack.
  - **Shadow Strike** — Ghost / Physical / 80 BP / 95% / 10 PP; contact; 50% chance to lower Defense.
  - **Polar Flare** — Fire / Special / 75 BP / 100% / 10 PP; spread move; 10% freeze; defrosts; custom Ramnarok form-toggle behavior.
- No duplicate normalized move IDs or names were introduced.
- Master catalog increased from **516 → 519**.
- Current totals: **286 Physical / 166 Special / 67 Status**.

Discovery phase note:
This completes the planned **12-source-sweep cap**. Further source discovery should only resume for an unusually strong/high-value source; otherwise the next phase should focus on animation sourcing, DS compatibility, cleanup, and selecting the best designs for Mercury Redux.
