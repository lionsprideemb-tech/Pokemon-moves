# Pokémon Clover All-Type Source Sweep 07

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project represented: Pokémon Clover battle data
- Public implementation: `Squeetz/clovermon-showdown`
- Pinned commit: `008196c839c1efe859e2d59c092c88370b7752d6`
- Move table: `data/moves.ts`
- Repository license: MIT for simulator code

## Filtering method

This repository is a Pokémon Showdown fork, so Sweep 07 used the same stronger fork-diff method established in Sweep 06:

1. Parse all top-level move definitions from the pinned Clovermon `data/moves.ts`.
2. Parse upstream Pokémon Showdown's `data/moves.ts`.
3. Remove every move whose normalized ID or display name exists upstream.
4. Deduplicate the remaining fork-specific records against `manifests/community_moves.csv`.

Result before master deduplication: **60 fork-specific moves**.

Already present:
- Inverse Room
- Scorched Earth

New imports: **58**.

## Result

Imported:
- **33 Physical**
- **16 Special**
- **9 Status**

Type coverage:
- **56 canonical-type moves**
- **2 source-native `???`-type moves**

Representative additions include:
- Sleazy Spores
- Slime Gulp
- Fruit Punch
- Dragon Fist
- Speed Weed
- 1000 Folds
- Warhead
- Hulk Up
- Quick Sand
- Think Fast
- Boltbeam
- Pixie Pummel
- Great Rage
- Plunder
- Ban Hammer
- Chaos Dunk
- Erosion Wave
- Falcon Punch
- Fire Bomb
- Futaba Break
- Overenergize
- Punch Out
- Regenerate
- Riot Shield
- Spook Out
- Strato Blade
- Swindle
- Toxiravage

The source also contains several intentionally comedic/irreverent move names. They are preserved as source metadata rather than pre-approved for Mercury Redux; later design curation can keep, rename, rebalance, or discard them.

## Animation status

Clovermon Showdown provides simulator mechanics, not Nintendo DS battle-animation assets. Imported records therefore remain:
- mechanics source-certified
- DS mechanics reimplementation required
- DS animation sourcing/recreation required

## Licensing note

The simulator code is MIT-licensed, but that does not automatically establish reuse permission for original Pokémon Clover move designs or game assets. This repository preserves provenance and does not treat Clover art/animation assets as freely reusable.

## Master catalog

Before Sweep 07: **345**

After Sweep 07: **403 unique designs**

Current totals:
- **236 Physical**
- **110 Special**
- **57 Status**
- **376 canonical-type designs**

Duplicate verification:
- normalized duplicate IDs: **0**
- normalized duplicate names: **0**

## Next restart point

**All-Type Source Sweep 08** — audit another public project source-wide and deduplicate against the **403-design** master catalog.
