# Pokémon Untamed All-Type Source Sweep 10

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project: Pokémon Untamed
- Repository: `untamed-team/project-untamed`
- Pinned commit: `8d757cdeb132c947602dce6a9f327fc5883e84c2`
- Move data: `PBS/moves.txt`
- No repository license detected at the pinned snapshot.

## Filtering

The PBS was compared against the current official Pokémon Essentials move IDs/names and against the existing Mercury community master catalog.

Excluded:
- **Struggle** — official move
- `SUPERNOVA_ALT` — internal PP-0 support/alternate record
- `PREMONITIONMOVE` — explicit PP-0 "Premonition Dummy" support record
- **Venom Strike**, **Erosion Wave**, **Ow The Edge**, **Think Fast** — already present in the master catalog

## Result

Imported **36 new unique designs**:
- **12 Physical**
- **19 Special**
- **5 Status**

Type split:
- **32 canonical-type moves**
- **4 Qmarks-type moves**

Notable additions include:
- Slime Shot
- Zealous Dance
- Psysonic
- Psycrush
- Kinetic Rend
- Jolt Kick
- Frost Kick
- Scouring Winds
- Haunt
- Biting Cold
- Chilling Wail
- Mystic Blade
- **Force Wave**
- Geode Burst
- Forge Breath
- Scatterdust
- Sweet Tooth
- Impact Event
- Pepper Spray
- Titan's Wrath
- Siren Song
- Rebalancing
- Frigid Maw
- Mana Drain
- Steam Burst
- Crimson Surge
- Thousand Folds
- Hard Drive Crash
- Splinter Shot
- Virus Inject
- Trim Tackle
- Stalagbite
- Glacial Gulf
- Golden Splash

## Coverage milestone

**Force Wave** is Fighting / Special, 90 BP, 95% accuracy, 10 PP, and targets all nearby foes.

That closes the long-standing **Fighting Special** gap in the canonical discovery matrix. Every canonical type now has at least one Physical and at least one Special non-vanilla design in the master catalog.

## Animation status

The repository contains an `Animations/` directory, but the first audit did not establish dedicated custom animation mappings for these 36 moves. No animation assets are copied because repository-level reuse permission is not established.

For Mercury Redux, treat these as mechanics/design references until a later animation-specific audit certifies a reusable source or a DS recreation is built.

## Master catalog

Before Sweep 10: **434**

After Sweep 10: **470 unique designs**

Current totals:
- **263 Physical**
- **144 Special**
- **63 Status**
- **439 canonical-type designs**
- normalized duplicate IDs: **0**
- normalized duplicate names: **0**

## Next restart point

**All-Type Source Sweep 11** — continue source-wide discovery against the **470-design** master catalog.
