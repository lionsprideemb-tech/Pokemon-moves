# BULK04 automated validation — complete

Date: 2026-09-24

Range: **1073–1122**  
Candidates: **50**

Automated validation result: **PASS**

Checks completed:
- 50/50 provisional IDs present, unique, ordered, and contiguous
- 50/50 symbolic move IDs unique in the batch
- 50/50 valid source-record types
- 50/50 valid Physical / Special / Status categories
- 50/50 valid PP values
- power/accuracy fields parse correctly when present
- 50/50 mechanics audit status = `complete`
- approval-board audit cross-check found **0 locked/source-limited records**
- **0 mechanics blockers in BULK04**

## Source-native custom types caught

Two Vanguard candidates in this batch use its non-canonical **Sound** type:
- **1117 — Drum Beat**
- **1118 — Beat Drop**

They are preserved source-faithfully in the candidate library and flagged for a later Mercury type decision rather than being silently remapped or rejected during collection.

The bulk validator has been updated to distinguish the 18 official types from known source-native custom types (`Sound`, `Qmarks`, `Shadow`, `Nuclear`, `Crystal`, `???`). Custom-type candidates pass source validation but remain review items for final Mercury integration.

## Source-aware blank fields

- **Oni Fist (1074)** has blank accuracy because the pinned source explicitly says it always hits.
- **Godspeed (1102)** omits its accuracy field in the pinned source; no percentage is invented.
- status/effect-only moves may legitimately omit power or accuracy where the source does not use those fields.

## Visual workload

- **23** defer visual work until move approval
- **6** use a post-Gen-4 DS donor requiring one unique-donor certification after Platinum-native porting
- **21** use Platinum/base-era donor animations and require no per-move video
- **0** mechanics blockers

No per-move MP4 sweep was performed or required.

BULK04 is ready to move forward.
