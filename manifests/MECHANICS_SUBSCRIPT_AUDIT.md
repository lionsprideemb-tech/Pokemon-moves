# Mechanics Subscript Resolution

Phase F3 resolves the `MOVE_SUBSCRIPT_PTR_*` dependencies discovered in Phase F2 to the concrete hg-engine battle subscripts that implement them.

## Progress

- Unique side-effect pointers requiring resolution: **90**
- Resolved side-effect pointers: **90/90**
- Concrete subscript files collected from pointer resolution: **72 unique**
- Source: `BluRosie/hg-engine @ 398a3020943f1ae98987e5b12b73d9086bbba3ce`

## Batch 09 notes

- `STUFF_CHEEKS` boosts Defense by two stages, invokes the specialized `StuffCheeks` command to process the Berry, then removes the held item.
- `TAKE_HEART` raises Sp. Atk and Sp. Def by one stage each and also clears the user's major status condition.
- `THRASH` writes the rampage duration into status state and locks the attacker to the current move.
- `TIDY_UP` is a large field-cleanup script: it removes Substitutes from all battler slots, clears Spikes, Toxic Spikes, Stealth Rock, and Sticky Web on both sides, then raises the user's Attack and Speed.
- `TOXIC_THREAD` combines Speed -2 through the common stat updater with the full Poison subscript.
- `USER_DEF_AND_SPDEF_DOWN_1_STAGE`, `USER_DEF_DOWN_HIT`, `V_CREATE`, and `WORK_UP` are wrappers around the shared stat-stage system.
- `USER_SWAP_ATK_AND_DEF` toggles the Power Trick move-effect flag and directly swaps the user's Attack and Defense values.

## Side-effect pointer resolution status

**Complete: 90/90.**

This does not finish all of Phase F3. The next step is to resolve and collect the **9 direct `BATTLE_SUBSCRIPT_*` dependencies** discovered in Phase F2, then continue into specialized battle-command and engine-hook mapping.

The mapping manifest is `manifests/mechanics_subscript_resolution.csv`.
