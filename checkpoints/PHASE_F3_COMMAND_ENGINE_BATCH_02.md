# Phase F3 Command / Engine Audit — Batch 02

Status: **PASS**

Verified on 2026-09-24 against pinned hg-engine source `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

Resolved 10 additional mechanics-relevant commands:

- TryReflect — opcode 0x52 — base HGSS command; no hg-engine replacement found
- TryProtection — opcode 0x64 — hg-engine replacement hook
- TryBreakScreens — opcode 0x85 — hg-engine replacement hook
- TryAuroraVeil — opcode 0x106 — hg-engine extended C command
- StuffCheeks — opcode 0x114 — hg-engine extended C command
- ResetAllStatChanges — opcode 0x3F — hg-engine replacement hook
- TryStickyWeb — opcode 0xFC — hg-engine extended C command
- TryCureStatusBerry — opcode 0x11B — hg-engine extended C command
- TrySynchronizeStatus — opcode 0x11A — hg-engine extended C command
- CheckTargetIsPartner — opcode 0x109 — hg-engine extended C command

Cumulative command/engine mappings: **20**.

Important portability split:
- Base-engine dependencies still exist, including Reflect.
- Several original commands are explicitly replaced by hg-engine hooks and therefore require the replacement C behavior, not merely the original opcode.
- Modern mechanics such as Aurora Veil, Sticky Web, Stuff Cheeks, Synchronize/Berry handling, and Pollen Puff ally detection live in the extended command table.

Next restart point: **Phase F3 Command / Engine Audit — Batch 03**, continuing with terrain, type, item, hazard, status, and move-state commands exposed by the collected graph.
