#!/usr/bin/env python3
"""Generate one deterministic hg-engine battle test per unique preview animation.

The generated tests are visual-capture fixtures, not mechanics tests. Each fixture
uses the official DS move whose animation is assigned in preview_render_manifest.csv.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def parse_move_constants(moves_c: Path) -> list[str]:
    text = moves_c.read_text(encoding="utf-8")
    constants = re.findall(r"^\s*\[(MOVE_[A-Z0-9_]+)\]\s*=\s*\{", text, re.MULTILINE)
    if not constants:
        raise RuntimeError(f"No move constants found in {moves_c}")
    return constants


def test_source(index: int, preview_id: str, move_constant: str) -> str:
    return f"""// Test: PREVIEW_CAPTURE {preview_id} {move_constant}
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
                .moves = {{ MOVE_SPLASH, MOVE_NONE, MOVE_NONE, MOVE_NONE }},
                .hp = FULL_HP,
                .status = STATUS_SLEEP,
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
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
            }},
            {{
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
            }}
        }},
        .enemyScript = {{
            {{
                {{ ACTION_MOVE_SLOT_1, BATTLER_PLAYER_FIRST }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
            }},
            {{
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
                {{ ACTION_NONE, 0 }},
            }}
        }},
        .expectations = {{}},
    }},

#ifndef GET_TEST_CASE_ONLY
}};
// PREVIEW_CAPTURE fixture {index}
#endif
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--hg-engine-root", required=True, type=Path)
    args = parser.parse_args()

    moves_c = args.hg_engine_root / "data" / "Moves.c"
    constants = parse_move_constants(moves_c)

    out_dir = args.hg_engine_root / "data" / "battle_tests" / "preview_capture"
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.c"):
        old.unlink()

    rows = list(csv.DictReader(args.manifest.open(newline="", encoding="utf-8")))
    if not rows:
        raise RuntimeError("Preview render manifest is empty")

    written = 0
    for index, row in enumerate(rows):
        preview_id = row["preview_id"].strip()
        move_id_text = row["ds_move_id"].strip()
        if not preview_id or not move_id_text:
            raise RuntimeError(f"Missing preview_id/ds_move_id in row {index + 2}")

        move_id = int(move_id_text)
        if move_id < 0 or move_id >= len(constants):
            raise RuntimeError(
                f"{preview_id}: DS move id {move_id} is outside data/Moves.c "
                f"(0..{len(constants) - 1})"
            )

        move_constant = constants[move_id]
        filename = out_dir / f"{index:04d}_{preview_id}.c"
        filename.write_text(test_source(index, preview_id, move_constant), encoding="utf-8")
        written += 1

    print(f"Generated {written} PREVIEW_CAPTURE battle tests in {out_dir}")


if __name__ == "__main__":
    main()
