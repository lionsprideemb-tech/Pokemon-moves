# Pokémon Uranium All-Type Source Sweep 05

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Game represented: Pokémon Uranium **1.3.1**
- Public extraction/reformatting repository: `eriedaberrie/uranium-mining`
- Pinned commit: `33e18f15c892e431f2d188363daba64bd51406b4`
- Move data: `pbs/moves.txt`

The repository README states that its data was extracted from Pokémon Uranium 1.3.1. It also distinguishes the `pbs` directory as select game data while saying everything else in the repository is GPLv3. For that reason, this library stores PBS **metadata/provenance only** rather than treating the extracted game data as GPL-licensed reusable assets.

## Filtering method

The Uranium move table was compared against:
- current Pokémon Essentials official move IDs and names
- this repository's pinned hg-engine official Gen 5–9 move manifest
- the existing community master catalog

The spelling/identifier `VICEGRIP` was treated as the official Vise Grip rather than a custom design.

## Result

**30 new unique custom move designs** were imported:
- **11 Physical**
- **15 Special**
- **4 Status**

Of those 30:
- **18** use one of the canonical 18 Pokémon types
- **12** use Pokémon Uranium's custom **Nuclear** type

Master catalog:
- Before Sweep 05: **293**
- After Sweep 05: **323**

## Uranium custom move haul

Examples include Coral Break, Atomic Punch, Metal Whip, Shuffle, Nuclear Waste, Gamma Ray, Radioacid, Sky Fall, Flame Impact, Subduction, Instant Crush, Get Lucky, Laser Pulse, Gemstone Glimmer, Half-life, Ocean's Wrath, Fission Burst, Caustic Breath, Nuclear Slash, Thunderstorm, Sudden Strike, Expunge, Fallout, Proton Beam, Infernal Blade, Quantum Leap, Metal Cruncher, Drain Life, Sticky Terrain, and Nuclear Wind.

## Custom Nuclear type

Nuclear-type move records are preserved exactly as a source-specific custom type. They are **not** automatically converted to Poison, Electric, or any other canonical type.

That lets Mercury Redux later decide whether to implement Nuclear as an actual type, selectively retype individual moves, or reuse only their mechanics/concepts.

## Animation status

The uranium-mining README says it contains no actual game assets and the PBS snapshot contains move data rather than battle-animation resources. Therefore the mechanics/data are source-certified, while animations remain a separate later sourcing/recreation task for DS.

## Next restart point

**All-Type Source Sweep 06** — locate the next public project with original move definitions and deduplicate it against the **323-design** master catalog.
