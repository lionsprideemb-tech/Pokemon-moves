# Pokémon Sage All-Type Source Sweep 09

Status: **PASS — SOURCE-WIDE AUDIT COMPLETE**

Date: 2026-09-24

Source:
- Sage-associated public fork: `SageFox/Pokemon-Showdown-Sage`
- Pinned commit: `f6757adccfc138272f10e738afdc36472387e646`
- Move data: `data/moves.js`
- Repository README is generic legacy Pokémon Showdown documentation rather than independent Pokémon Sage documentation
- Repository code license: MIT
- Move-design provenance: treated conservatively as fork-specific Sage-associated evidence

## Filtering method

The legacy Showdown move table was compared against:
- modern upstream Pokémon Showdown
- current Pokémon Essentials official move IDs/names
- the existing community move master catalog

A naive object-key parser also encounters nested keys such as `secondary`, `boosts`, `self`, `effect`, and `moveData`; these were explicitly rejected as non-move records.

`VICEGRIP` was excluded because it is the legacy spelling/identifier for official **Vise Grip**.

## Result

Exactly **1** new non-vanilla move design survived filtering:

### Magikarp's Revenge
- Type: Water
- Category: Physical
- Power: 120
- Accuracy: always hits in source
- PP: 10
- Restricted to Magikarp
- Drains 50% of damage dealt
- Sets Rain Dance
- Grants Aqua Ring
- Grants Magic Coat
- Forces recharge next turn
- 100% confuses the target
- Lowers target Defense by 1
- Lowers target Sp. Atk by 1

This is an unusually dense mechanics package and will need a dedicated DS battle-script implementation rather than a simple effect-code mapping.

## Master catalog

Before Sweep 09: **433**
After Sweep 09: **434**

Current totals:
- **251 Physical**
- **125 Special**
- **58 Status**

Duplicate normalized IDs: **0**
Duplicate normalized names: **0**

## Animation status

The source is battle-simulator code only and provides no Nintendo DS animation assets. Animation will require separate sourcing or recreation.

## Next restart point

**All-Type Source Sweep 10** — audit the next public project source-wide and deduplicate against the **434-move** master catalog.
