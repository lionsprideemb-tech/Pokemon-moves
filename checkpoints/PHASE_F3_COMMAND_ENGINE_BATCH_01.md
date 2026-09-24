# Phase F3 Command / Engine Audit — Batch 01

Status: **PASS**

Verified on 2026-09-24 against pinned hg-engine source `398a3020943f1ae98987e5b12b73d9086bbba3ce`.

Resolved 10 mechanics-relevant commands:

- AddEntryHazardToQueue — opcode 0x101 — hg-engine C implementation
- ChangeExecutionOrderPriority — opcode 0xF6 — hg-engine C implementation
- ChangeStatStage — opcode 0x33 — original opcode replaced by hg-engine hook
- CheckCanActivateDefiantOrCompetitive — opcode 0xFF — hg-engine C implementation
- HandleMagicPowder — opcode 0x10F — hg-engine C implementation
- HandleSoak — opcode 0x10E — hg-engine C implementation
- SetMoveConditionFlag — opcode 0x115 — hg-engine C implementation
- StrengthSapCalc — opcode 0x108 — hg-engine C implementation
- TryLightScreen — opcode 0x51 — base HGSS command; no hg-engine replacement found
- TryPartyStatusRefresh — opcode 0x62 — base HGSS command; no hg-engine replacement found

Key result: the audit now explicitly separates mechanics that are portable from hg-engine C source from mechanics that still depend on original HGSS command behavior.

Next restart point: **Phase F3 Command / Engine Audit — Batch 02**, continuing the mechanics-specific commands exposed by the collected subscript graph.
