# Community Move Discovery

## Scope reset

The official Gen 5–9 move/ability baseline already exists in hg-engine and is preserved in this repository. Community discovery now focuses on **non-vanilla moves created by other projects** that can fill real movepool gaps in Mercury Redux.

The first target is **physical Electric**, because many physical Electric Pokémon have relatively few broadly usable physical STAB options.

## Discovery Batch 01 — physical Electric

Source-certified from **Pokémon Elite Redux** current public config:

| Move | Power | Accuracy | PP | Role |
|---|---:|---:|---:|---|
| Smite | 120 | 80 | 15 | High-power contact Electric move; Smack Down effect + 20% paralysis |
| Shocking Jab | 80 | 100 | 10 | Reliable physical Electric attack; 20% paralysis; horn synergy |
| Shocking Edge | 80 | 100 | 10 | Reliable physical Electric blade move; 10% paralysis; Keen Edge synergy |
| Lightning Strike | 70 | 100 | 20 | Utility offense; 20% chance to raise user's Speed |
| Volt Bolt | 70 | 100 | 20 | Doubles damage against a paralyzed target; arrow-tagged |

### Animation evidence

- **Smite:** `src/battle_anim_new.c::sAnimCmdSmiteBeam` exists in the Elite Redux source tree.
- **Shocking Jab:** `src/battle_anim_effects_1.c::gShockingJabProjectileSpriteTemplate` exists.
- **Volt Bolt:** the move data explicitly requests the existing `MOVE_VOLT_TACKLE` animation.
- **Shocking Edge / Lightning Strike:** no dedicated move-name animation linkage was source-certified in this first sweep.

Because these sources are GBA-oriented, their mechanics are useful references but their visual assets are **not DS-native**. Mercury should either reproduce the effect with DS animation commands/assets or adapt a DS-native equivalent.

## Licensing / provenance rule

The Elite Redux repositories checked in this batch do not expose a repository-level license through GitHub and contain no root LICENSE/COPYING file. For that reason this repository stores **metadata, factual mechanics, source paths, symbols, and pinned commits** rather than copying their source files wholesale.

## DS-native first sweep

A first pass over `B-Kiraly/Benndots-HGengine-ROMhack` confirmed useful DS animation infrastructure and modified move animations, but did not source-certify an original physical-Electric move in that initial search. It remains a candidate animation/reference source for later batches.

## Next discovery step

Continue the physical-Electric hunt across additional public hacks/fangames and collect distinct concepts rather than duplicates. Then move through the other under-served type/category combinations.
