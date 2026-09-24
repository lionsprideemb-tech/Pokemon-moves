# Phase F2 Dependency Audit — Batch 12

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **111–120 of 173**:

- 345 — POLTERGEIST
- 346 — RAISE_ALL_STATS_LOSE_THIRD_MAX_HP
- 347 — RECOVER_THREE_QUARTERS_DAMAGE_DEALT
- 348 — RECOVER_HALF_DAMAGE_DEALT_BURN_HIT
- 349 — FICKLE_BEAM
- 350 — SLEEP_POISON_PARALYZE_HIT
- 351 — PREVENT_ESCAPE_HIT
- 352 — PREVENT_ESCAPE_BOTH_HIT
- 353 — STEALTH_ROCK_HIT
- 354 — SET_SPIKES_HIT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Six side-effect pointers appear; three are new to the cumulative audit: CLANGOROUS_SOUL, DRAIN_THREE_QUARTERS, and BURN_AND_DRAIN_HEALTH.
- Poltergeist performs its held-item requirement directly.
- Fickle Beam and the Sleep/Poison/Paralysis effect both implement their random branching directly in-script.
- Effects 351–354 are generic damage only. Their trapping/hazard behavior must be located in engine-side processing.

Cumulative Phase F2 audit coverage: **120/173**.

Next restart point: **Phase F2 Batch 13 — sorted required-effect positions 121–130.**
