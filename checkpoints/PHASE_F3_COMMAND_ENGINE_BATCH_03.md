# Phase F3 Command / Engine Audit — Batch 03

Status: **PASS**

Verified on 2026-09-24 against pinned hg-engine source `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

Resolved 10 additional mechanics-relevant commands:

- UpdateTerrainOverlay — opcode 0xEC — hg-engine extended C command
- GotoIfTerrainOverlayIsType — opcode 0xED — hg-engine extended C command
- ActivateParadoxAbility — opcode 0x117 — hg-engine extended C command
- ResetParadoxAbility — opcode 0x118 — hg-engine extended C command
- SetFieldCondition2 — opcode 0x129 — hg-engine extended C command
- IsFieldCondition2On — opcode 0x128 — hg-engine extended C command
- RemoveItem — opcode 0xCA — base HGSS command; no hg-engine replacement found
- TryIncinerate — opcode 0x104 — hg-engine extended C command
- AddType — opcode 0x105 — hg-engine extended C command
- GoToIfThirdType — opcode 0x10B — hg-engine extended C command

Cumulative command/engine mappings: **30**.

Important portability findings:
- Terrain and Paradox mechanics require both the extended battle commands and helpers from `ability.c`.
- Magic Room requires both the field-condition commands and the field-condition server tick/expiry logic.
- The third-type model is a real engine dependency, not merely script metadata.
- Item-consuming modern scripts still depend on the original HGSS `RemoveItem` command.

Next restart point: **Phase F3 Command / Engine Audit — Batch 04**, continuing with modern type mutation, status cleanup, item/ability presentation, switching-state, and field cleanup commands.
