# Interactive Move Approval Board

Open `docs/approval/index.html` through GitHub Pages to review the current move catalog.

The board:
- loads the live `manifests/community_moves.csv` master catalog;
- overlays `MERCURY_CUSTOM_MOVE_BATCH_PLAN.csv` so every move shows its compact Mercury provisional ID, approval batch, mechanics state, and visual-review policy;
- defaults to compact Mercury ID order (923–1441) and can filter by approval batch;
- overlays every completed DS animation audit manifest;
- shows move source, type/category, power, accuracy, PP, effects, tags, source notes, license/portability notes, and the currently assigned or referenced animation;
- supports move approval, change/reject decisions, separate animation approval, and free-form notes;
- stores decisions in browser local storage;
- exports/imports review JSON and exports a CSV;
- supports rendered GIF/video previews through `previews.json`;
- supports richer mechanics fields as source audits are completed through `audit_details.json`.

## Review states

Move decision:
- Approve move
- Needs changes
- Reject move

Animation decision:
- Approve animation
- Change animation

A move counts as fully reviewed after both decisions have been made.

## Preview registry

Add entries to `previews.json` keyed by move ID:

```json
{
  "MOVE_EXAMPLE": {
    "type": "video",
    "url": "./previews/MOVE_EXAMPLE.mp4",
    "caption": "Platinum/hg-engine test capture"
  }
}
```

The page will automatically render the preview.

## Extended mechanics

As the 519-move source audit progresses, add verified fields under the move ID in `audit_details.json`. The approval board displays every supplied field in the Effects & Behavior section.


## Current approval phase

As of 2026-09-24, the mechanics audit is complete for **519/519** candidate moves. The approval board is now the canonical human-review surface before final approved-move ID compaction and native Platinum import.

Source-native custom types and the five source-special Rejuvenation Intercept/Z-Move 0-PP records remain explicitly visible for deliberate approval decisions rather than being silently normalized.
