# Vanguard All-Type Source Sweep 02

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source snapshot:
- Project represented: Pokémon Vanguard
- Public data carrier: `SEXYREXY-DEV/PokeRover`
- Pinned commit: `4919c813a9d1f3f1e1bed54189bf541d46fc7e8a`
- Source data: `PBS/moves.txt`
- PokeRover README identifies its bundled PBS files as Vanguard patch **3.0.16**
- Repository-level license file: not detected
- Reuse policy for this library: metadata/provenance only unless permission is established

## Filtering method

The Vanguard PBS snapshot was compared against:
- the current Pokémon Essentials move PBS baseline
- this repository's pinned hg-engine official Gen 5–9 move manifest

This prevented newer official moves from being mislabeled as fangame originals.

## Result

The sweep found:
- **64** non-official PBS move sections
- **63** unique custom move designs after source-local deduplication
- one duplicate display-name/design pair for **Code:Power** was collapsed to one catalog entry
- **55** custom designs use the normal 18 Pokémon types
- **8** designs use Vanguard's extra **Sound** type

Category totals added:
- **39 Physical**
- **17 Special**
- **7 Status**
- **63 total**

Master catalog:
- Before Sweep 02: **187**
- After Sweep 02: **250 unique non-vanilla moves**

## Important discoveries

This sweep immediately filled several weaknesses from Sweep 01, including:
- Special Grass coverage
- additional Special Electric, Water, Rock, Steel, Psychic, Fire, Flying, Ghost and Poison designs
- more non-damaging utility designs

Special Fighting and Special Bug remain empty in the canonical 18-type matrix after the first two source sweeps.

## Animation status

The public PokeRover PBS snapshot provides move mechanics/data but not the underlying Vanguard battle-animation implementation. These entries are therefore cataloged as:
- mechanics source-certified
- animation source still requiring a separate audit/recreation step for Nintendo DS

## Custom Sound type

Vanguard's Sound-type moves are preserved without forcing them into an official type. Mercury Redux can later decide whether to:
- implement a Sound type,
- remap selected moves,
- or borrow only the move concepts/mechanics.

## Next restart point

**All-Type Source Sweep 03** — audit another public source as a whole and deduplicate every original move against the 250-design master catalog.
