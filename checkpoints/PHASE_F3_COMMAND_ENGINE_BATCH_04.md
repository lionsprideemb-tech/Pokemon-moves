# Phase F3 Command / Engine Audit — Batch 04

Status: **PASS**

Verified on 2026-09-24 against pinned hg-engine source `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

Resolved 10 additional mechanics-relevant commands:

- ClearAuroraVeil — opcode 0x107 — hg-engine extended C command
- ClearSmog — opcode 0x10A — hg-engine extended C command
- GoToIfTerastallized — opcode 0x10C — hg-engine extended C command
- HandleForestsCurse — opcode 0x110 — hg-engine extended C command
- HandleTrickOrTreat — opcode 0x111 — hg-engine extended C command
- HandleBurnUp — opcode 0x112 — hg-engine extended C command
- HandleDoubleShock — opcode 0x113 — hg-engine extended C command
- AbilityPopup — opcode 0x116 — hg-engine extended C command
- SetCurrentMoveSwitchingStatus — opcode 0x119 — hg-engine extended C command
- RemoveEntryHazardFromQueue — opcode 0x102 — hg-engine extended C command

Cumulative command/engine mappings: **40**.

Important integration findings:
- Forest's Curse, Trick-or-Treat, Burn Up, and Double Shock depend on both their command implementations and BeforeMove eligibility logic.
- Clear Smog depends on post-move dispatch in ServerDoPostMoveEffects.c.
- AbilityPopup has its own asynchronous UI lifecycle.
- Switching moves depend on shared currentMoveSwitchStatus state beyond their individual scripts.
- Hazard cleanup has a real queue model, not only side-condition bit clearing.

Added engine sources:
- BattleController_BeforeMove.c
- ServerDoPostMoveEffects.c

Next restart point: **Phase F3 Command / Engine Audit — Batch 05**, continuing with grounding/terrain checks, protection-contact behavior, hazard processing, held-item helpers, and remaining modern move-state commands.
