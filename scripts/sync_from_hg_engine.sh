#!/usr/bin/env bash
set -euo pipefail

PINNED_HG_ENGINE_COMMIT="398a3020943f1ae98987e5b12b73d9086bbba3ce"
WORKDIR="${TMPDIR:-/tmp}/mercury-hg-engine-moves"

rm -rf "$WORKDIR"
git clone --filter=blob:none https://github.com/BluRosie/hg-engine.git "$WORKDIR"
git -C "$WORKDIR" checkout "$PINNED_HG_ENGINE_COMMIT"

mkdir -p animations/hg-engine support
for id in $(seq 471 922); do
  cp "$WORKDIR/armips/move/move_anim/${id}.s" "animations/hg-engine/${id}.s"
done
cp "$WORKDIR/armips/include/animscriptcmd.s" support/animscriptcmd.s
cp "$WORKDIR/CREDITS.md" CREDITS_HG_ENGINE.md

python3 scripts/verify_coverage.py
echo "Modern DS move library synchronized to $PINNED_HG_ENGINE_COMMIT"
