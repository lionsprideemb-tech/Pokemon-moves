# Mercury Custom Move Bulk Pipeline — Started

Date: 2026-09-24

## Verified ID boundary

The modern official move table currently ends at **922 — MOVE_MALIGNANT_CHAIN**. The first custom/community candidate slot is therefore **923**.

The 519 current candidates stage provisionally at **923–1441** in 11 bulk batches: ten batches of 50 and a final batch of 19.

Candidate IDs are provisional. Final Mercury Redux integration compacts only approved moves, so rejected candidates do not leave permanent holes.

## Fast validation policy

Every candidate receives automated validation. Visual work is intentionally deduplicated:
- no per-move MP4 before move approval;
- Platinum/base-era donor animations are spot-checked;
- imported DS donor animations are certified once per unique donor after Platinum-native porting;
- custom/missing/unresolved animation work waits until the move itself is approved;
- failures are escalated to targeted visual testing.

Five previously identified mechanics-source blockers remain marked `BLOCKED_MECHANICS` and cannot become final imports until resolved or deliberately redesigned.

Generated manifests:
- `manifests/MERCURY_CUSTOM_MOVE_BATCH_PLAN.csv`
- `manifests/MERCURY_CUSTOM_MOVE_BATCH_SUMMARY.csv`

Tools:
- `scripts/build_mercury_move_plan.py`
- `scripts/validate_mercury_bulk.py`
