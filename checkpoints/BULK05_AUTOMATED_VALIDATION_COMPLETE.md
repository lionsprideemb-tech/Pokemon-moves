# BULK05 automated validation — complete with two quarantined blockers

Date: 2026-09-24

Range: **1123–1172**  
Candidates: **50**

Automated validation result: **PASS**

- 50/50 provisional IDs present, unique, ordered, and contiguous
- 50/50 symbolic move IDs unique
- 50/50 source-record types recognized
- 50/50 valid Physical / Special / Status categories
- numeric power/accuracy/PP fields parse correctly when present
- **48/50 mechanics-ready**
- **2/50 quarantined mechanics blockers**
- approval-board blocker cross-check matches the bulk plan

## Quarantined blockers

### 1160 — Hunter's Wilds
The pinned Vanguard/PokeRover record uses `EffectDependsOnHigherDamage`, but the public snapshot does not include that custom implementation. A repository-wide source search found no public implementation of that function beyond the PBS reference itself. The Attack-dominant and Sp. Atk-dominant branches remain unknown and are not guessed.

### 1162 — Terrestrial Claw
The pinned record uses `TypeAndPowerDependOnTerrain`, but Vanguard's prose says it raises different stats depending on terrain. Public implementations of that function are the standard Terrain Pulse behavior (terrain-dependent type/power), which does not explain Vanguard's custom stat-raise description. Without Vanguard's custom override, the terrain-to-stat mapping remains unverified and is not guessed.

These two moves remain in the candidate catalog as `BLOCKED_MECHANICS`. They do **not** stop the other 48 candidates from advancing.

## Source-native custom types

Six candidates in this batch use Vanguard's source-native **Sound** type:
- **1138 — Strident Spark**
- **1146 — Rhythmic Combo**
- **1147 — Instant Whistle**
- **1148 — Discordant Shriek**
- **1149 — Heart Beat**
- **1150 — Audio Break**

They remain source-faithful during collection and will be explicitly remapped/approved (or rejected) for Mercury rather than silently converted.

## Visual workload

- **48** defer visual work until move approval
- **0** post-Gen-4 unique donor certifications after Platinum-native porting
- **0** Platinum/base-era donor spot-check cases
- **2** mechanics blockers

No per-move MP4 sweep is required.

BULK05 is complete under the bulk-validation workflow.
