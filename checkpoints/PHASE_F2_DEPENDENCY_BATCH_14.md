# Phase F2 Dependency Audit — Batch 14

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **131–140 of 173**:

- 365 — QUARTER_HP
- 366 — HIT_THREE_TIMES_ALWAYS_CRITICAL
- 367 — TAKE_HEART
- 368 — HIGH_CRITICAL_RAISE_SPEED_HIT
- 369 — MORTAL_SPIN
- 370 — TIDY_UP
- 371 — PROTECT_USER_SIDE
- 372 — INCINERATE
- 373 — FIRST_TURN_ONLY
- 374 — ADD_THIRD_TYPE_GRASS

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Six side-effect pointers appear; three are new to the cumulative audit: TAKE_HEART, TIDY_UP, and ADD_TYPE_GRASS.
- The three-hit always-critical effect sets multi-hit behavior but does not explicitly force critical hits in-script.
- Mortal Spin's hazard/bind cleanup is absent from this effect script and must be engine-side.
- Protect User Side deliberately reuses the Protect handler and relies on move-effect differentiation.
- Incinerate and First-Turn-Only are generic damage scripts; their special behavior is outside these files.

Cumulative Phase F2 audit coverage: **140/173**.

Next restart point: **Phase F2 Batch 15 — sorted required-effect positions 141–150.**
