# Pokémon Reborn All-Type Source Sweep 04

Status: **PASS — AUDITED, ZERO NEW DESIGNS**

Date: 2026-09-24

Source snapshot:
- Project: Pokémon Reborn
- Public snapshot carrier: `Lycoris9/PokemonStarRail`
- Pinned commit: `655411b65ee3fc166c916b6f15c55a398d9daf01`
- Move data: `Pokemon_Reborn/PBS/moves.txt`
- Version file: `19.16`
- Bundled README identifies **Pokémon Reborn Episode 19: Final**, dated 2022-05-27
- README states Reborn is updated to **Generation 7** using Ultra Sun / Ultra Moon learnsets and data

## Result

The sweep parsed **771 move records**.

After comparison against:
- official move IDs and names
- the repository's hg-engine modern official baseline
- the existing community move master catalog

only one apparent non-match remained:
- `VICEGRIP` / **Vice Grip**

That record is the legacy spelling/identifier for the official Pokémon move **Vise Grip**, so it was correctly excluded.

### Imported
**0 new non-vanilla move designs**

Master catalog remains:
- **293 unique community move designs**
- **187 Physical**
- **73 Special**
- **33 Status**

## Why this sweep is still useful

A zero-add audit matters because it:
- confirms Reborn 19.16 is not a productive source of original named move designs
- prevents repeated searching of the same source
- validates the official-move filter against an older Essentials/Gen 7-format PBS
- keeps provenance for later animation/mechanics reference work if needed

## Next restart point

**All-Type Source Sweep 05** — move to a source with a stronger likelihood of original moves, while deduplicating against the 293-design master catalog.
