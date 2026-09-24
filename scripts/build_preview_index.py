#!/usr/bin/env python3
"""Build docs/approval/previews.json from committed preview assets.

The move->preview mapping is generated from the approval-board animation assignments.
Only previews that actually exist are published, so the web UI never points at 404 media.
MP4 is preferred; GIF is used as a fallback.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVAL = ROOT / "docs" / "approval"
MAPPING = APPROVAL / "manifests" / "preview_move_mapping.csv"
OUTPUT = APPROVAL / "previews.json"


def relative_url(path_text: str) -> str:
    p = Path(path_text)
    try:
        rel = p.relative_to(APPROVAL)
    except ValueError:
        rel = p
    return "./" + rel.as_posix()


def main() -> int:
    with MAPPING.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    moves = {}
    ready_assets = set()

    for row in rows:
        mp4 = ROOT / row["preview_mp4"]
        gif = ROOT / row["preview_gif"]

        if mp4.exists():
            media_type = "video"
            url = relative_url(row["preview_mp4"])
            ready_assets.add(row["preview_id"])
        elif gif.exists():
            media_type = "image"
            url = relative_url(row["preview_gif"])
            ready_assets.add(row["preview_id"])
        else:
            continue

        source_label = (
            row["animation_reference"]
            if row["source_kind"] == "platinum-base-move"
            else row["ds_animation_path"]
        )
        moves[row["move_id"]] = {
            "type": media_type,
            "url": url,
            "caption": (
                f"Assigned DS animation preview • {row['preview_id']} • "
                f"DS move {row['ds_move_id']} • {source_label}"
            ),
        }

    payload = {
        "schema_version": 2,
        "description": (
            "Rendered move-animation previews keyed by move_id. "
            "Generated from preview_move_mapping.csv; only committed media is indexed."
        ),
        "rendered_unique_preview_count": len(ready_assets),
        "rendered_move_count": len(moves),
        "moves": moves,
    }

    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUTPUT.relative_to(ROOT)}: "
        f"{len(ready_assets)} unique preview assets / {len(moves)} moves"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
