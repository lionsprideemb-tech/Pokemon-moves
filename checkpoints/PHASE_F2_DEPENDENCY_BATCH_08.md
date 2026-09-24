# Phase F2 Dependency Audit — Batch 08

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **71–80 of 173**:

- 291 — USER_DEF_SP_DEF_SPEED_DOWN_HIT
- 292 — HEAVY_SLAM
- 293 — CONFUSE_HIT_CRASH_ON_MISS
- 294 — APPLY_TERRAINS
- 295 — ATK_SP_ATK_UP
- 296 — HIT_TWICE_AND_FLINCH
- 297 — UP_TO_10_HITS
- 298 — HIT_THREE_TIMES_INCREMENT_BASE_POWER_20
- 299 — HIT_THREE_TIMES
- 300 — PSYBLADE

Findings:
- One direct battle-subscript dependency occurs: `BATTLE_SUBSCRIPT_CREATE_TERRAIN_OVERLAY`.
- Three side-effect pointers appear; V_CREATE and WORK_UP are new to the cumulative audit.
- Heavy Slam depends on `CalcHeavySlamPower`.
- The terrain effect depends on both `UpdateTerrainOverlay` and the terrain-overlay subscript.
- Three different multi-hit patterns are exposed, including `MULTIHIT_TRIPLE_KICK` progression.
- Psyblade is generic damage only; its Electric Terrain boost must be supplied elsewhere.

Cumulative Phase F2 audit coverage: **80/173**.

Next restart point: **Phase F2 Batch 09 — sorted required-effect positions 81–90.**
