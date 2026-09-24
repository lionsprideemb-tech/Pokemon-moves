# Phase F2 Dependency Audit — Batch 03

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **21–30 of 173**:

- 69 — LOWER_DEFENSE_HIT
- 70 — LOWER_SPEED_HIT
- 71 — LOWER_SP_ATK_HIT
- 72 — LOWER_SP_DEF_HIT
- 73 — LOWER_ACCURACY_HIT
- 76 — CONFUSE_HIT
- 80 — RECHARGE_AFTER
- 85 — DO_NOTHING
- 101 — LEAVE_WITH_1_HP
- 103 — PRIORITY_1

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Seven new side-effect pointer dependencies appear: DEFENSE_DOWN_1_STAGE, SPEED_DOWN_1_STAGE, SP_ATTACK_DOWN_1_STAGE, SP_DEFENSE_DOWN_1_STAGE, ACCURACY_DOWN_1_STAGE, CONFUSE, and RECHARGE_TURN.
- Effect 85 sets `MOVE_STATUS_SPLASH` directly.
- Effect 101 is a generic damage script; its leave-at-1-HP behavior is engine-side.
- Effect 103 is a generic damage script; its priority behavior is outside the effect file.

Cumulative Phase F2 audit coverage: **30/173**.

Next restart point: **Phase F2 Batch 04 — sorted required-effect positions 31–40.**
