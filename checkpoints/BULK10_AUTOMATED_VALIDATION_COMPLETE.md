# BULK10 automated validation — complete

Date: 2026-09-24

Range: **1373–1422**  
Candidates: **50**

Automated validation result: **PASS**

- 50/50 provisional IDs present, unique, ordered, and contiguous
- 50/50 symbolic move IDs unique
- 50/50 source-record types recognized
- 50/50 valid Physical / Special / Status categories
- numeric power/accuracy/PP fields parse correctly where used
- **50/50 mechanics-ready**
- **0 mechanics blockers in BULK10**

## Protopluma / Proto Feather source behavior resolved

**1398 — Protopluma** had been blocked because its Spanish description says it may flinch while its machine-readable row stores a 0% effect chance.

For source-faithful collection, the machine-readable record is decisive:
- Rock / Physical
- 60 BP
- 100% accuracy
- 15 PP
- effect family 00F (flinch family)
- effect chance **0%**

Therefore the encoded source behavior is fully determined: **it does not functionally flinch**. The prose mismatch remains visible as a warning, but it no longer blocks the mechanics audit. Mercury can deliberately give it a nonzero flinch chance later during approval if desired, but collection does not invent one.

## Source-native custom types

- **1377 — Titan's Wrath** — Qmarks
- **1383 — Queso Blast** — Qmarks
- **1386 — Hard Drive Crash** — Qmarks
- **1388 — Virus Inject** — Qmarks
- **1417 — Patronaje** — Shadow

These remain source-faithful and require an explicit Mercury type/remap decision before final integration.

## Visual workload

- **47** defer visual work until move approval
- **3** post-Gen-4 unique donor certifications after Platinum-native porting
- **0** Platinum/base-era donor spot-check cases
- **0** mechanics blockers

No per-move MP4 sweep is required.

BULK10 is complete under the bulk-validation workflow.
