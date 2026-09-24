#!/usr/bin/env python3
"""Build docs/approval/previews.json from rendered MP4 files and move mapping."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--preview-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    moves = {}
    missing = set()

    with args.mapping.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            preview_id = row["preview_id"].strip()
            move_id = row["move_id"].strip()
            clip = args.preview_dir / f"{preview_id}.mp4"
            if not clip.exists():
                missing.add(preview_id)
                continue

            source = row["animation_reference"].strip() or row["ds_animation_path"].strip()
            caption_bits = [f"DS animation preview • move {row['ds_move_id'].strip()}"]
            if source:
                caption_bits.append(source)

            moves[move_id] = {
                "type": "video",
                "url": f"./previews/mp4/{preview_id}.mp4",
                "caption": " • ".join(caption_bits),
            }

    payload = {
        "schema_version": 1,
        "description": "Rendered Nintendo DS move-animation previews keyed by community move_id.",
        "rendered_move_count": len(moves),
        "missing_unique_preview_count": len(missing),
        "moves": moves,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(moves)} move previews to {args.output}; {len(missing)} unique clips still missing")


if __name__ == "__main__":
    main()
