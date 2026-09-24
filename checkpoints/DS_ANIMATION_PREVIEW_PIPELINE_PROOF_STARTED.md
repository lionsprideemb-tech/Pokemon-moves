# DS Animation Preview Pipeline — Proof Batch Started

Date: 2026-09-24

## Current audited state

- Community move catalog: **519 moves**
- Moves with an assigned DS animation baseline: **519 / 519**
- Moves still lacking an animation assignment: **0**
- Unique animation previews needed after deduplication: **303**
- Final preview mapping is stored in:
  - `docs/approval/manifests/preview_render_manifest.csv`
  - `docs/approval/manifests/preview_move_mapping.csv`

## Preview implementation

The approval page already supports inline MP4/WebM/image previews through
`docs/approval/previews.json`.

The new capture pipeline adds:

- `scripts/generate_preview_tests.py`
  - Generates deterministic hg-engine battle tests for selected preview IDs.
- `scripts/capture_preview_tests.py`
  - Runs the generated tests in py-desmume and captures the top DS screen to MP4.
- `scripts/build_preview_index.py`
  - Rebuilds `docs/approval/previews.json` from actually rendered MP4 files.
- `.github/workflows/render-move-previews.yml`
  - Reproducibly builds the DS test ROM from source, captures a small preview batch,
    updates the approval index, and commits successful preview clips.

## First proof batch

Default proof size: **5 unique animations**, starting at preview row 0.

Expected first preview IDs:

1. `anim_0003` — Double Slap visual
2. `anim_0004` — Comet Punch visual
3. `anim_0005` — Mega Punch visual
4. `anim_0015` — Cut visual
5. `anim_0025` — Mega Kick visual

These five previews collectively cover the community moves currently mapped to
those base-era DS animations.

## Next checkpoint

Do not scale to all 303 unique animations until the proof batch has been checked for:

- successful DS build
- successful auto-battle launch
- complete animation capture
- correct 256x192 top-screen crop
- acceptable clip length / playback quality
- inline playback on the approval page

After proof certification, continue in small render batches and regenerate
`previews.json` after each successful batch.
