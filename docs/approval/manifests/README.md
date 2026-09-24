# Animation preview render queue

The approval board has **519 community moves**, but many moves intentionally reuse the same DS animation.

The preview system therefore renders each unique assigned DS animation once and maps every compatible community move to that shared capture.

Files:

- `preview_render_manifest.csv` — deduplicated render/capture queue.
- `preview_move_mapping.csv` — all 519 moves mapped to their shared preview asset.
- `../../previews/mp4/` — preferred rendered clips.
- `../../previews/gif/` — optional fallback clips.
- `../../../scripts/build_preview_index.py` — rebuilds `previews.json` using only preview files that actually exist.

Two capture sources are used:

1. **hg-engine-script** — post-Gen-IV DS animation scripts preserved in this repository.
2. **platinum-base-move** — direct reuse of an original Platinum/base-era move animation.

Do not replace a source-certified/custom animation reference merely because the approval baseline currently uses a DS analog. The preview exists to let the reviewer judge the assigned DS visual and request a better/custom version when needed.
