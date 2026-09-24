# Phase F3 Command / Engine Audit — Batch 05

Status: **PASS**

Verified on 2026-09-24 against pinned hg-engine source `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

Resolved 10 additional mechanics-relevant commands:

- GotoIfGrounded — opcode 0xE8 — hg-engine extended C command
- CheckProtectContactMoves — opcode 0x103 — hg-engine extended C command
- JumpToCurrentEntryHazard — opcode 0x100 — hg-engine extended C command
- CheckItemHoldEffect — opcode 0xA6 — base HGSS command; no hg-engine replacement found
- GetItemHoldEffect — opcode 0xA7 — base HGSS command; no hg-engine replacement found
- GetItemEffectParam — opcode 0xA8 — base HGSS command; no hg-engine replacement found
- CheckSubstitute — opcode 0xD2 — hg-engine replacement hook
- TryToxicSpikes — opcode 0x9F — base HGSS command; no hg-engine replacement found
- CheckToxicSpikes — opcode 0xA0 — hg-engine replacement hook
- TrySpikes — opcode 0x68 — base HGSS command; no hg-engine replacement found

Cumulative command/engine mappings: **50**.

Important integration findings:
- Grounding is shared engine state used by terrain, hazards, status immunities, and move calculations.
- Modern protection reactions are centralized in one hg-engine contact dispatcher.
- Entry hazards have an explicit ordered queue with its own tracker.
- Infiltrator-aware Substitute handling comes from an hg-engine replacement hook.
- Several modern item and hazard flows still rely on untouched HGSS battle commands.
- The pinned Toxic Spikes absorption implementation contains a side-condition mask worth targeted runtime verification before certification.

Next restart point: **Phase F3 Command / Engine Audit — Batch 06**, continuing with terrain/move-property helpers, protection/priority checks, and remaining move-state commands before building the dedicated engine-hook manifest.
