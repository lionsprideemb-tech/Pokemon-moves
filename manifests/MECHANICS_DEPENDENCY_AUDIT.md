# Mechanics Dependency Audit

Phase F2 extracts the dependencies hidden behind the 173 battle-effect scripts collected in Phase F1.

This audit tracks:
- direct `BATTLE_SUBSCRIPT_*` calls;
- `MOVE_SUBSCRIPT_PTR_*` side-effect handlers;
- battle-script commands used by each effect;
- explicit references to engine-side C hooks;
- effect scripts that are generic damage stubs even though the named effect requires additional engine behavior.

## Progress

- Required effect scripts: **173**
- Audited in F2 so far: **110/173**
- Current batch: sorted required-effect positions **101–110**
- Direct battle-subscript dependencies found in this batch: **3 unique**
- Side-effect pointer dependencies found in this batch: **8 unique**
- Cumulative unique battle subscripts observed: **7**
- Cumulative unique side-effect pointers observed: **64**
- Generic-damage-only scripts in this batch: **0**

## Batch 11 dependency notes

- Effect 322 combines poison application with Venoshock-style poisoned-target power doubling.
- Effect 323 introduces `MOVE_SUBSCRIPT_PTR_GIVE_TARGET_SIMPLE` for Simple Beam-style ability replacement.
- Effect 324 exposes Meteor Beam's charge dependency stack: Sp. Atk boost, Power Herb skip subscript, and charge cleanup.
- Effect 325 adds rain-aware charge skipping, `CheckIgnoreWeather`, and a dedicated `BATTLE_SUBSCRIPT_SP_ATK_UP_RAIN_SKIP` path.
- Effect 326 depends on `TryStickyWeb` and `AddEntryHazardToQueue`, making entry-hazard queue support an explicit Mercury requirement.
- Effect 328 introduces a +3 Defense handler.
- Effect 341 sets `BATTLE_STATUS_HIT_FLY` and confusion for Hurricane; its weather-sensitive accuracy behavior is not encoded here and must be checked in engine-side accuracy logic.
- Effects 342–344 add handlers for self-Defense reduction, Hyperspace Fury behavior, and simultaneous Attack/Defense/Speed boosts.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
