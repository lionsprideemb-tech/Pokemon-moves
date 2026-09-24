# BULK06 automated validation — complete with one quarantined source conflict

Date: 2026-09-24

Range: **1173–1222**  
Candidates: **50**

Automated validation result: **PASS**

- 50/50 provisional IDs present, unique, ordered, and contiguous
- 50/50 symbolic move IDs unique
- 50/50 source-record types recognized
- 50/50 valid Physical / Special / Status categories
- numeric power/accuracy/PP fields parse correctly
- **49/50 source-mechanics resolved**
- **1/50 quarantined source conflict**
- approval-board blocker cross-check matches the bulk plan

## Quarantined blocker

### 1219 — Shuffle
The pinned Pokémon Uranium record remains internally contradictory: 60 BP Normal/Special, 90% accuracy, 15 PP, Present-like text saying the gift may restore HP, but function code `0D6`—the same function used for Roost in that dataset—and an effect-chance field of 100.

A fresh repository-wide search did not uncover an authoritative Uranium runtime implementation or documentation that resolves the contradiction. No heal chance, heal amount, or alternate behavior is invented.

Shuffle remains `source-conflict` / `BLOCKED_MECHANICS`. The other 49 candidates continue.

## Source-special 0-PP records

The validator caught five Rejuvenation Intercept/Z-Move records that source-faithfully store **0 PP**:
- **1211 — Unleashed Power**
- **1212 — Blinding Speed**
- **1213 — Elysian Shield**
- **1214 — Chthonic Malady**
- **1215 — Domain Shift**

These are not missing-data errors—their detailed mechanics are source-resolved—but they are special-format moves rather than ordinary selectable moves. The validator now permits 0 PP only when the source record is explicitly tagged as an Intercept/Z-Move. Mercury must later decide whether to give them ordinary PP and distribution or preserve special-only behavior.

## Source-native custom types

Eight candidates use source-native non-canonical types:
- **1211 — Unleashed Power** — Qmarks
- **1212 — Blinding Speed** — Qmarks
- **1214 — Chthonic Malady** — Shadow
- **1215 — Domain Shift** — Qmarks
- **1217 — Atomic Punch** — Nuclear
- **1220 — Nuclear Waste** — Nuclear
- **1221 — Gamma Ray** — Nuclear
- **1222 — Radioacid** — Nuclear

They remain source-faithful during collection and require explicit Mercury remap/approval later.

## Visual workload

- **49** defer visual work until move approval
- **0** post-Gen-4 unique donor certifications after Platinum-native porting
- **0** Platinum/base-era donor spot-check cases
- **1** mechanics blocker

No per-move MP4 sweep is required.

BULK06 is complete under the bulk-validation workflow.
