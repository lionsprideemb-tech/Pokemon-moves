# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **20/90**
- Concrete subscript files collected so far: **18 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 02 notes

- `AUTOTOMIZE` calls the shared stat-stage updater and uses `ReduceWeight 1000`, exposing weight mutation as a specialized command dependency.
- `BADLY_POISON` is a large status handler covering Toxic Spikes context, ability checks, weather suppression, Flower Veil, grounding, Misty Terrain, Shield Dust, Safeguard/Infiltrator, Corrosion, Synchronize, held-item cases, third typing, and status-curing berries.
- `BOOST_ALL_STATS` fans out through five calls to `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.
- `BREAK_SCREENS` uses the specialized `TryBreakScreens` command and the common attack-message/animation subscript.
- `BURN` is another deep status handler with ability, weather, terrain, Safeguard/Infiltrator, Shield Dust, third-type, Synchronize, and berry-cure dependencies.
- `BURN_AND_DRAIN_HEALTH` composes `BATTLE_SUBSCRIPT_BURN` with `BATTLE_SUBSCRIPT_DRAIN_HALF_DAMAGE_DEALT`.
- Psychic/Water type conversion use specialized `HandleMagicPowder` and `HandleSoak` commands.
- Clangorous Soul checks stat caps and HP cost, then calls UPDATE_HP and BOOST_ALL_STATS.
- Coaching is a compact two-stat wrapper around UPDATE_STAT_STAGE; its separate pre-move failure rules remain mapped in BattleController_BeforeMove.c from Phase F2.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
