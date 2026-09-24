# Pokémon Sage-Associated Showdown Fork — All-Type Source Sweep 09

Status: **PASS — ONE FORK-SPECIFIC DESIGN IMPORTED**

Date: 2026-09-24

Source:
- Repository: `SageFox/Pokemon-Showdown-Sage`
- Pinned commit: `f6757adccfc138272f10e738afdc36472387e646`
- Move table: `data/moves.js`
- License: MIT for the Showdown fork code

## Filtering

The legacy move table was compared against modern upstream Pokémon Showdown by normalized move ID and display name.

Only two source records failed the official-upstream comparison:
1. `Vice Grip`
2. `Magikarp's Revenge`

`Vice Grip` is the legacy spelling of official **Vise Grip**, so it was excluded.

That leaves **1 genuine fork-specific design**.

## Imported move

**Magikarp's Revenge**
- Water / Physical
- 120 BP
- always hits
- 10 PP
- only succeeds when used by Magikarp
- drains 50% of damage
- sets Rain Dance
- grants the user Aqua Ring and Magic Coat
- confuses the target
- lowers the target's Defense and Special Attack by 1 stage
- forces the user to recharge next turn

## Provenance caution

The repository name associates the fork with Pokémon Sage, but its README is generic legacy Pokémon Showdown documentation and does not independently document the authorship/origin of this move. The catalog therefore labels it **Sage-associated fork evidence**, not an independently verified official Pokémon Sage move record.

## Master catalog

Before Sweep 09: **433**

After Sweep 09: **434 unique designs**

Current totals:
- **251 Physical**
- **125 Special**
- **58 Status**
- **407 canonical-type designs**
- normalized duplicate IDs: **0**
- normalized duplicate names: **0**

## Next restart point

**All-Type Source Sweep 10** — continue source-wide discovery against the **434-design** master catalog.
