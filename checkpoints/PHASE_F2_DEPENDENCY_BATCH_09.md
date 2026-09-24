# Phase F2 Dependency Audit — Batch 09

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **81–90 of 173**:

- 301 — SLEEP_HIT
- 302 — SPICY_EXTRACT
- 303 — ATK_SP_ATK_SPEED_UP_2_LOSE_HALF_MAX_HP
- 304 — SHED_TAIL
- 305 — AFTER_YOU
- 306 — QUASH
- 307 — TECHNO_BLAST
- 308 — MULTI_ATTACK
- 310 — LEECH_SEED_HIT
- 311 — SET_LIGHT_SCREEN_HIT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Eight side-effect pointer dependencies appear, all new to the cumulative audit.
- Fillet Away and Shed Tail are largely delegated to dedicated side-effect handlers, making those handlers critical Mercury dependencies.
- After You and Quash both depend on dedicated turn-order manipulation handlers.
- Techno Blast and Multi-Attack implement item-driven type changes directly using `CheckItemHoldEffect` plus `BSCRIPT_VAR_MOVE_TYPE`.
- Leech Seed and Light Screen on-hit effects delegate setup to dedicated handlers.

Cumulative Phase F2 audit coverage: **90/173**.

Next restart point: **Phase F2 Batch 10 — sorted required-effect positions 91–100.**
