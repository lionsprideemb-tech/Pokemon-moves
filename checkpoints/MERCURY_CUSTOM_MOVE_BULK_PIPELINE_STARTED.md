# Mercury Custom Move Bulk Pipeline — Started

Date: 2026-09-24

## Verified ID boundary

The modern official move table in this repository currently ends at **922 — MOVE_MALIGNANT_CHAIN**.
Therefore the first custom/community move slot is **923**, not 920.

For all 519 current candidates, the provisional compact range is:

- **923–1441**
- no 2048+ reserved gap
- no pre-allocation beyond the candidates that actually exist

These IDs are **provisional during review**. Before final Mercury Redux integration, rejected moves are removed and the approved set is compacted again from the next free official ID so final IDs remain contiguous.

## Bulk execution policy

The 519 candidates are split into **11 batches**:
- BULK01–BULK10: 50 moves each
- BULK11: 19 moves

Every candidate receives automated validation for ID uniqueness, mechanics fields, type/category, power, accuracy, PP, audit status, animation reference, and batch membership.

Visual testing is no longer one MP4 per move:
- direct Platinum/base-era donor animations are deduplicated and spot-checked;
- imported DS donor animations are visually certified once per unique donor/port;
- custom/recreated animations require a visual test after the Platinum-native port;
- any failed automated/runtime check is escalated to visual inspection.

## Existing blockers

The prior mechanics audit still has five source-blocked/conflicted moves. They remain in the staging plan but are marked **BLOCKED_MECHANICS** and cannot become final imports until resolved or deliberately redesigned for Mercury Redux.

## Generated manifests

- `manifests/MERCURY_CUSTOM_MOVE_BATCH_PLAN.csv`
- `manifests/MERCURY_CUSTOM_MOVE_BATCH_SUMMARY.csv`

Generator/checker:
- `scripts/build_mercury_move_plan.py`

This replaces the old 3-at-a-time / 2048+ workflow.
