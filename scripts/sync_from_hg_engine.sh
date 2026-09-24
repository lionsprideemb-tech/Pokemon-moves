#!/usr/bin/env bash
set -euo pipefail

PINNED_HG_ENGINE_COMMIT="398a3020943f1ae98987e5b12b73d9086bbba3ce"
WORKDIR="${TMPDIR:-/tmp}/mercury-hg-engine-moves"

rm -rf "$WORKDIR"
git clone --filter=blob:none https://github.com/BluRosie/hg-engine.git "$WORKDIR"
git -C "$WORKDIR" checkout "$PINNED_HG_ENGINE_COMMIT"

mkdir -p animations/hg-engine/{gen5,gen6,gen7,gen8,gen9}
mkdir -p mechanics/hg-engine/move_scripts
mkdir -p support/hg-engine references/hg-engine

for id in $(seq 471 922); do
  if [ "$id" -le 562 ]; then gen=gen5
  elif [ "$id" -le 624 ]; then gen=gen6
  elif [ "$id" -le 745 ]; then gen=gen7
  elif [ "$id" -le 853 ]; then gen=gen8
  else gen=gen9
  fi
  cp "$WORKDIR/armips/move/move_anim/${id}.s" "animations/hg-engine/${gen}/${id}.s"

  n=$(printf "%04d" "$id")
  matches=("$WORKDIR"/data/battle_scripts/moves/move_script_${n}_*.s)
  test -f "${matches[0]}"
  cp "${matches[0]}" mechanics/hg-engine/move_scripts/
done

cp "$WORKDIR/armips/include/animscriptcmd.s" support/hg-engine/animscriptcmd.s
cp "$WORKDIR/include/constants/moves.h" support/hg-engine/moves.h
cp "$WORKDIR/include/constants/move_effects.h" support/hg-engine/move_effects.h
cp "$WORKDIR/include/move_data.h" support/hg-engine/move_data.h
rm -rf support/hg-engine/move_sub_anim support/hg-engine/move_spa
[ -d "$WORKDIR/armips/move/move_sub_anim" ] && cp -R "$WORKDIR/armips/move/move_sub_anim" support/hg-engine/
[ -d "$WORKDIR/rawdata/move_spa" ] && cp -R "$WORKDIR/rawdata/move_spa" support/hg-engine/

cp "$WORKDIR/CREDITS.md" CREDITS_HG_ENGINE.md
cp "$WORKDIR/armips/asm/moves.s" references/hg-engine/armips_moves.s
cp "$WORKDIR/include/constants/moves.h" references/hg-engine/moves.h
cp "$WORKDIR/include/constants/move_effects.h" references/hg-engine/move_effects.h
cp "$WORKDIR/documentation/wiki/Move-Data-Structure-Documentation.md" references/hg-engine/

python3 scripts/verify_coverage.py
echo "Modern DS move library synchronized to $PINNED_HG_ENGINE_COMMIT"
