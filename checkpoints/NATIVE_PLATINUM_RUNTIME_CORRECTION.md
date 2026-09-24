# Native Platinum Runtime Correction

Date: 2026-09-24

## Decision

Mercury Redux uses **native Pokémon Platinum / pokeplatinum** as its final runtime.

HG-Engine remains a donor/reference source for:
- modern move implementations
- move animation concepts/scripts
- modern battle mechanics
- test patterns
- data structures and QoL ideas

## Animation meaning

The current 519/519 assignment coverage means every community move has a selected
**DS donor animation baseline**. It does **not** mean those animations are already
ported to or certified in pokeplatinum.

The 303 deduplicated preview targets remain useful for visual review. HG-rendered
clips are concept/reference previews only. Final acceptance requires a Platinum-native
port and runtime test.

## Next animation phase

1. Audit pokeplatinum's native move-animation script/data format.
2. Build a conversion map from each selected HG donor animation to Platinum-native assets/commands.
3. Port a small proof batch into pokeplatinum.
4. Render and approve those clips from the actual Platinum runtime.
5. Scale only after the proof batch is certified.
