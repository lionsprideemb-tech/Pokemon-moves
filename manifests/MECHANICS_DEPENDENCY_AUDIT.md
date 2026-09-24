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
- Audited in F2 so far: **40/173**
- Current batch: sorted required-effect positions **31–40**
- Direct battle-subscript calls found in this batch: **1 unique**
- Side-effect pointer dependencies found in this batch: **8 unique**
- Cumulative unique side-effect pointers observed: **23**
- Generic-damage-only scripts in this batch: **1** (effect 121)

## Batch 04 dependency notes

- Effect 111 delegates Protect to `MOVE_SUBSCRIPT_PTR_PROTECT`.
- Effect 121 (POWER_BASED_ON_FRIENDSHIP) is a generic crit/damage script, so friendship-based power scaling is handled elsewhere.
- Effect 125 is byte-identical to ordinary BURN_HIT; its thawing component must therefore be engine-side.
- Effect 132 uses the specialized `WeatherHPRecovery` command, `ABILITY_MEGA_SOL`, and the PRESENT_HEAL handler.
- Effects 138–140 delegate self-stat boosts to dedicated side-effect handlers.
- Effect 150 checks `MOVE_EFFECT_FLAG_MINIMIZE` and doubles the power multiplier before damage, while also installing FLINCH.
- Effect 151 is the first F2 script audited so far with a direct `Call BATTLE_SUBSCRIPT_*`: `BATTLE_SUBSCRIPT_CHARGE_MOVE_CLEANUP`.
- Effect 172 uses the specialized `FollowMe` command and delegates its user-facing message/animation.

The dependency manifest is `manifests/mechanics_dependencies.csv`.

Phase F2 is not a runtime certification. The goal is to identify every dependency that Mercury Redux must carry over or reimplement.
