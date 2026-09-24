#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
anim = root / "animations" / "hg-engine"
expected = set(range(471, 923))
present = set()

for path in anim.glob("*.s"):
    try:
        present.add(int(path.stem))
    except ValueError:
        pass

missing = sorted(expected - present)
extra = sorted(present - expected)

print(f"Expected: {len(expected)}")
print(f"Present:  {len(present & expected)}")
if missing:
    print("Missing:", ", ".join(map(str, missing)))
if extra:
    print("Extra numeric IDs:", ", ".join(map(str, extra)))

if missing:
    sys.exit(1)

print("PASS: 452/452 modern DS move animation scripts are present.")
