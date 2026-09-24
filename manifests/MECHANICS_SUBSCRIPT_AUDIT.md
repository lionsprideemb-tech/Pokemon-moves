# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved in F3 so far: **40/90**
- Concrete subscript files collected so far: **33 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 04 notes

- `ENTRAINMENT` resolves to a direct ability-copy subscript; the script copies the attacker's ability onto the defender, so legality/failure gating remains outside this small handler.
- `EVASION_UP_1_STAGE` reuses the already-collected shared `BATTLE_SUBSCRIPT_UPDATE_STAT_STAGE`.
- `FEINT` clears the defender's protecting turn flag and emits the appropriate protection-break message.
- `FILLET_AWAY` enforces the HP threshold and stat-cap checks, removes half max HP, then raises Attack, Sp. Atk, and Speed by two stages through the shared stat updater.
- `FLINCH` checks move order, Substitute, Inner Focus, and Shield Dust before setting flinch.
- `FREEZE` is another deep status pipeline: Magma Armor, Comatose, Purifying Salt, sun, Flower Veil, grounding, Misty Terrain, Shield Dust, Substitute, Ice typing, Safeguard/Infiltrator, and move-choice unlocking are all involved.
- `GIVE_HELD_ITEM` implements Bestow's actual held-item transfer and checks Quick Claw/Custap flags plus Klutz.
- `GIVE_TARGET_SIMPLE` carries an explicit protected-ability list and Ability Shield check before replacing the target's ability with Simple.
- `GUARD_SPLIT` directly averages both battlers' Defense and Sp. Def values.
- `HEAL_BELL` delegates party status refresh to `TryPartyStatusRefresh` and includes Heal Bell/Aromatherapy/Sparkly Swirl messaging and ability-block reporting.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.

Phase F3 is not complete until all 90 side-effect pointers, the nine direct battle-subscript dependencies from Phase F2, and their important nested/engine dependencies are resolved.
