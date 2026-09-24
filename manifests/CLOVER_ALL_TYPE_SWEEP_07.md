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

As with the Insurgence sweep, this source is a Pokémon Showdown fork. The audit therefore directly compared the fork's `data/moves.ts` against upstream Pokémon Showdown rather than treating every non-Essentials record as custom.

Result of the source diff:
- **60** fork-specific move designs
- **2** already existed in the Mercury community catalog: **Inverse Room** and **Scorched Earth**
- **58** new unique move designs imported

## Imported category totals

- **33 Physical**
- **16 Special**
- **9 Status**

The sweep adds designs across essentially the entire canonical type spread and also preserves two source-native **???**-type moves without remapping them.

Examples include:
- Sleazy Spores
- Slime Gulp
- Fruit Punch
- Dragon Fist
- Speed Weed
- 1000 Folds
- Warhead
- Weird Flex
- Quick Sand
- Think Fast
- Boltbeam
- Pixie Pummel
- Great Rage
- Plunder
- Chaos Dunk
- Erosion Wave
- Fire Bomb
- Overenergize
- Puke Blood
- Riot Shield
- Strato Blade
- Toxiravage

The source also contains intentionally comedic/edgy move names; the catalog preserves source names exactly for provenance rather than sanitizing or silently renaming them.

## Animation status

Clovermon Showdown is a battle-simulator source. Its move definitions certify mechanics/data, but it does not provide Nintendo DS battle animations.

Imported records are marked for:
- DS mechanics reimplementation
- separate DS animation sourcing or recreation

## Licensing note

The simulator code is MIT-licensed. That does not automatically establish reuse permission for original Pokémon Clover move designs, artwork, or game assets, so the library keeps those provenance boundaries explicit.

## Master catalog

Before Sweep 07: **345**

After Sweep 07: **403 unique designs**

Current totals:
- **236 Physical**
- **110 Special**
- **57 Status**
- **376 canonical-type designs**

Custom types currently preserved source-faithfully:
- ???: 2
- Crystal: 1
- Nuclear: 12
- Qmarks: 3
- Shadow: 1
- Sound: 8

## Next restart point

**All-Type Source Sweep 08** — audit another public project source-wide and deduplicate against the **403-design** master catalog.
