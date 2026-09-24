# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **50/90**
- Concrete subscript files collected so far: **43 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 05 notes

- `HEAL_BLOCK_START` checks Substitute/current Heal Block state, sets the Heal Block move-effect flag, and installs a five-turn timer.
- `HEAL_PULSE` calculates 50% target healing, or 75% when the attacker has Mega Launcher, then delegates to `BATTLE_SUBSCRIPT_RECOVER_HP`.
- `HYPERSPACE_FURY` explicitly removes the target's protecting turn flag and then applies the user's Defense drop through the shared stat-stage updater.
- `ION_DELUGE` sets `FIELD_CONDITION_ION_DELUGE` directly.
- `LASER_FOCUS` uses `SetMoveConditionFlag`, exposing another battle-state condition that must be traced through the command/engine layer.
- `LEECH_SEED_START` handles Substitute, Grass typing including the third-type slot, repeat application, semi-invulnerable/missed states, and attacker ownership of the seed effect.
- `LIFE_DEW` restores one quarter of max HP through `BATTLE_SUBSCRIPT_UPDATE_HP`.
- `LIGHT_SCREEN` relies on the specialized `TryLightScreen` command plus the prepared-message animation subscript.
- `MAKE_IT_RAIN` adds level-scaled coin value on the player's side, then applies the user's Sp. Atk drop via the common stat updater.
- `PARALYZE` is a full modern status pipeline covering Limber, Comatose, Purifying Salt, Leaf Guard/weather suppression, Flower Veil, Misty Terrain/grounding, Shield Dust, Substitute, Electric immunity including third typing, Safeguard/Infiltrator, Synchronize, and status-curing berries.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
