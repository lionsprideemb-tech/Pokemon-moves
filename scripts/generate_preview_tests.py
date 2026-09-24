#!/usr/bin/env python3
"""Generate a small deterministic hg-engine battle-test set for animation preview capture."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from pathlib import Path


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value)


def move_constant(row: dict, modern_by_id: dict[str, str]) -> str:
    if row["source_kind"] == "platinum-base-move":
        constant = row["animation_reference"].strip()
    else:
        constant = modern_by_id.get(row["ds_move_id"].strip(), "")
    if not constant.startswith("MOVE_"):
        raise ValueError(f"Could not resolve move constant for {row['preview_id']}: {row}")
    return constant


TEST_TEMPLATE = r"""// Test: Preview {preview_id} {move_constant}
#ifndef GET_TEST_CASE_ONLY

#include "../../../../include/battle.h"
#include "../../../../include/constants/ability.h"
#include "../../../../include/constants/item.h"
#include "../../../../include/constants/moves.h"
#include "../../../../include/constants/species.h"
#include "../../../../include/test_battle.h"

const struct TestBattleScenario BattleTests[] = {{

#endif

    {{
        .battleType = BATTLE_TYPE_TRAINER,
        .weather = FIELD_CONDITION_NONE,
        .fieldCondition = 0,
        .terrain = TERRAIN_NONE,
        .playerParty = {{
            {{
                .species = SPECIES_MUDKIP,
                .level = 50,
                .form = 0,
                .ability = ABILITY_TORRENT,
                .item = ITEM_NONE,
                .moves = {{ {move_constant}, MOVE_NONE, MOVE_NONE, MOVE_NONE }},
                .hp = FULL_HP,
                .status = 0,
                .condition2 = 0,
                .moveEffectFlags = 0,
            }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }}
        }},
        .enemyParty = {{
            {{
                .species = SPECIES_TREECKO,
                .level = 50,
                .form = 0,
                .ability = ABILITY_OVERGROW,
                .item = ITEM_NONE,
                .moves = {{ MOVE_SLEEP_TALK, MOVE_NONE, MOVE_NONE, MOVE_NONE }},
                .hp = FULL_HP,
                .status = 0,
                .condition2 = 0,
                .moveEffectFlags = 0,
            }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }},
            {{ .species = SPECIES_NONE }}
        }},
        .playerScript = {{
            {{
                {{ ACTION_MOVE_SLOT_1, BATTLER_ENEMY_FIRST }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
            }},
            {{
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
            }}
        }},
        .enemyScript = {{
            {{
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
            }},
            {{
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }}, {{ ACTION_NONE, 0 }},
            }}
        }},
        .expectations = {{ {{ 0 }} }},
    }},
#ifndef GET_TEST_CASE_ONLY
}};
// Auto-generated preview test. The battle ends after the scripted turn.
#endif
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-manifest", required=True)
    parser.add_argument("--moves-manifest", required=True)
    parser.add_argument("--hg-engine", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--count", type=int, default=5)
    args = parser.parse_args()

    render_rows = read_csv(Path(args.render_manifest))
    modern_rows = read_csv(Path(args.moves_manifest))
    modern_by_id = {r["ds_id"].strip(): r["constant"].strip() for r in modern_rows}

    start = max(0, args.start)
    selected = render_rows[start : start + max(1, args.count)]
    if not selected:
        raise SystemExit(f"No preview rows selected at start={start}, count={args.count}")

    hg = Path(args.hg_engine)
    out_dir = hg / "data" / "battle_tests" / "preview_auto"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    selection_path = hg / "preview_selection.csv"
    with selection_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "preview_id",
                "move_constant",
                "source_kind",
                "ds_move_id",
                "animation_reference",
                "ds_animation_path",
            ],
        )
        writer.writeheader()
        for idx, row in enumerate(selected):
            constant = move_constant(row, modern_by_id)
            preview_id = row["preview_id"].strip()
            filename = f"{idx:04d}_{safe_name(preview_id)}.c"
            (out_dir / filename).write_text(
                TEST_TEMPLATE.format(preview_id=preview_id, move_constant=constant),
                encoding="utf-8",
            )
            writer.writerow(
                {
                    "preview_id": preview_id,
                    "move_constant": constant,
                    "source_kind": row["source_kind"],
                    "ds_move_id": row["ds_move_id"],
                    "animation_reference": row["animation_reference"],
                    "ds_animation_path": row["ds_animation_path"],
                }
            )

    # hg-engine's build_tests.py treats this file as keyword filters.
    # Deliberately omit a trailing newline because the pinned helper does not strip lines.
    (hg / "test_filter.txt").write_text("Preview ", encoding="utf-8")
    print(f"Generated {len(selected)} preview tests in {out_dir}")
    for row in selected:
        print(row["preview_id"])


if __name__ == "__main__":
    main()
