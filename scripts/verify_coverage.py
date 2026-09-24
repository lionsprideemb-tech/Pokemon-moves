#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
expected = set(range(471, 923))

animations = set()
for path in (root / "animations" / "hg-engine").glob("gen*/*.s"):
    try:
        animations.add(int(path.stem))
    except ValueError:
        pass

mechanics = set()
rx = re.compile(r"move_script_(\d{4})_.*\.s$")
for path in (root / "mechanics" / "hg-engine" / "move_scripts").glob("move_script_*.s"):
    m = rx.match(path.name)
    if m:
        mechanics.add(int(m.group(1)))

missing_anim = sorted(expected - animations)
missing_mech = sorted(expected - mechanics)
extra_anim = sorted(animations - expected)
extra_mech = sorted(mechanics - expected)

print(f"Animations: {len(animations & expected)}/452")
print(f"Mechanics:  {len(mechanics & expected)}/452")

if missing_anim:
    print("Missing animations:", ", ".join(map(str, missing_anim)))
if missing_mech:
    print("Missing mechanics:", ", ".join(map(str, missing_mech)))
if extra_anim:
    print("Extra animation IDs:", ", ".join(map(str, extra_anim)))
if extra_mech:
    print("Extra mechanics IDs:", ", ".join(map(str, extra_mech)))

if missing_anim or missing_mech:
    sys.exit(1)

print("PASS: complete 452/452 modern DS move animation + mechanics coverage.")
