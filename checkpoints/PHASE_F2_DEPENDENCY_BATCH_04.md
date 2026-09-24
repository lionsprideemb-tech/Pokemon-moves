# Phase F2 Dependency Audit — Batch 04

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **31–40 of 173**:

- 111 — PROTECT
- 121 — POWER_BASED_ON_FRIENDSHIP
- 125 — THAW_AND_BURN_HIT
- 132 — HEAL_HALF_DIFFERENT_IN_WEATHER
- 138 — RAISE_DEF_HIT
- 139 — RAISE_ATTACK_HIT
- 140 — RAISE_ALL_STATS_HIT
- 150 — FLINCH_MINIMIZE_DOUBLE_HIT
- 151 — CHARGE_TURN_SUN_SKIPS
- 172 — MAKE_GLOBAL_TARGET

Findings:
- This is the first audited batch with a direct battle-subscript call: `BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP`.
- Eight side-effect pointers appear in the batch; six are new to the cumulative audit.
- Effect 121 is generic damage only; friendship-based power scaling is engine-side.
- Effect 125 is byte-identical to BURN_HIT, so thawing is not implemented in this effect script.
- Effect 132 depends on weather-aware HP recovery plus special `ABILITY_MEGA_SOL` handling.
- Effect 150 handles Minimize-based power doubling inside the effect script.
- Effect 172 depends on the specialized `FollowMe` battle command.

Cumulative Phase F2 audit coverage: **40/173**.

Next restart point: **Phase F2 Batch 05 — sorted required-effect positions 41–50.**
