# Interactive Move Approval Board

Open `docs/approval/index.html` through GitHub Pages to review the current move catalog.

The board:
- loads the live `manifests/community_moves.csv` master catalog;
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
