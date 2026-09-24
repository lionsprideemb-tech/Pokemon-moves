# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **70/90**
- Concrete subscript files collected so far: **60 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 07 notes

- `RECHARGE_TURN` sets the recharge status, locks the attacker to the current move, and stores the recharge turn state.
- `REFLECT` delegates side-condition setup to the specialized `TryReflect` command and then uses the prepared-message animation path.
- `RESET_ALL_STAT_STAGES` directly invokes `ResetAllStatChanges`.
- `SHED_TAIL` is a substantial compound script: it rejects an existing Substitute, requires a valid switch option and more than half HP, pays half max HP, creates a quarter-max-HP Substitute, clears the user's stat stages, removes Leech Seed, and marks Baton Pass-style switching state.
- `SHELL_SMASH` applies Attack/Sp. Atk/Speed +2 and Defense/Sp. Def -1 through the common stat-stage engine.
- `SHIFT_GEAR` applies Attack +1 and Speed +2 through the common stat updater.
- `SLEEP` is a full modern status pipeline covering Insomnia/Vital Spirit, Comatose, Purifying Salt, Leaf Guard/weather suppression, Flower Veil, Electric/Misty Terrain, Shield Dust, Substitute, Uproar/Soundproof, Safeguard/Infiltrator, sleep-turn generation, move-choice unlocking, and semi-invulnerable state cleanup.
- The three Speed-stage pointers in this batch all resolve to the already-collected `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
