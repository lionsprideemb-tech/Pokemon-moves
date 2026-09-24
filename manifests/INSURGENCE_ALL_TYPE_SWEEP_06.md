# Pokémon Insurgence All-Type Source Sweep 06

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project represented: Pokémon Insurgence battle data
- Public implementation: `Poilerwags/Insurgence-Showdown`
- Pinned commit: `72d72a7af4642d3c8391ab1118f0afbb2647020b`
- Move table: `data/moves.ts`
- Repository license: MIT for simulator code

## Filtering method

Because this repository is a Pokémon Showdown fork, comparing it only against a Pokémon Essentials baseline produces many false positives such as official Z-Moves, G-Max moves, Hidden Power variants, and other upstream simulator records.

Sweep 06 therefore used a stronger filter:

1. Parse every top-level move definition from the pinned Insurgence-Showdown `data/moves.ts`.
2. Parse upstream Pokémon Showdown's `data/moves.ts`.
3. Remove every move whose normalized ID or display name exists upstream.
4. Deduplicate the remaining fork-specific records against `manifests/community_moves.csv`.

That reduced the apparent candidate set to **22 genuine fork-specific move designs**.

## Result

Imported **22** new unique moves:
- **5 Physical**
- **6 Special**
- **11 Status**

Canonical-type additions: **21**

Custom-type additions:
- **Crystal: 1 Physical**

New moves:
- Achilles Heel
- Ancient Roar
- Corrode
- Crystal Rush
- Dark Matter
- Draco Jet
- Dragonify
- Drakon Voice
- Jet Stream
- Livewire
- Lunar Cannon
- Medusa Ray
- Morph
- Nanorepair
- New Moon
- Permafrost
- Retrograde
- Spirit Away
- Stealth Coal
- Wildfire
- Wormhole
- Zombie Strike

## Mechanics highlights

Several entries add mechanics that are especially useful as later Mercury Redux design references:
- **Achilles Heel** — super-effective against any non-immune target.
- **Corrode** — Poison attack that bypasses Poison immunity behavior and treats Steel as vulnerable.
- **Jet Stream** — temporary ally-side priority boost.
- **Livewire** — stackable Electric switch-in hazard with paralysis behavior.
- **Nanorepair** — 50% recovery plus a Defense boost.
- **Permafrost** — stackable Ice switch-in hazard with freeze behavior.
- **Stealth Coal** — Fire-type Stealth Rock-style hazard.
- **New Moon / Lunar Cannon** — custom weather and a move that skips its charge turn during that weather.
- **Retrograde** — reverses Mega Evolution.
- **Crystal Rush** — preserves Insurgence's source-specific Crystal typing.

## Animation status

Insurgence-Showdown is a battle simulator implementation. It provides mechanics code rather than Nintendo DS battle-animation resources.

Every imported move is therefore marked:
- mechanics source-certified
- DS mechanics reimplementation required
- DS animation sourcing/recreation still required

## Licensing note

The simulator repository is MIT-licensed, but that does not automatically establish reuse permission for the underlying Pokémon Insurgence move designs or any original game assets. The library keeps provenance explicit and does not treat game art/animation assets as freely reusable.

## Master catalog

Before Sweep 06: **323**

After Sweep 06: **345 unique designs**

Totals:
- **203 Physical**
- **94 Special**
- **48 Status**
- **320 canonical-type designs**

## Next restart point

**All-Type Source Sweep 07** — audit the next public project source-wide and deduplicate against the **345-design** master catalog.
