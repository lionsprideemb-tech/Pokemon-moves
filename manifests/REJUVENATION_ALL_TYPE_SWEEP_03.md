# Rejuvenation All-Type Source Sweep 03

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project represented: Pokémon Rejuvenation
- Public data source: `ThumsRipa/Rejuvenation-Wiki-Converter`
- Pinned commit: `05677bfc23298db5bbe484f731ec60c7fd801c5a`
- Move database: `Outputs/DatabaseMoves.txt`
- Converter README states the database contains all official and custom Rejuvenation moves
- Repository-level license file: not detected
- Library policy: metadata/provenance only unless reuse permission is established

## Filtering safeguards

The source contains official and custom moves together. Before import, the sweep filtered:
- official move IDs and display names using Pokémon Essentials and the pinned hg-engine official move baseline
- official generic Z-Moves whose Rejuvenation identifiers differ from hg-engine's physical/special constants
- official Orre Shadow moves
- dummy/alias records such as Future Sight/Doom Desire/Hex helper entries
- Hidden Power alias entries
- the legacy spelling alias `VICEGRIP` / Vise Grip
- any move already present in the community master catalog

## Result

**43 new unique custom move designs** were imported:
- **18 Physical**
- **19 Special**
- **6 Status**

The master catalog increased from **250 → 293**.

Notable additions include:
- Venam's Kiss
- Gale Strike
- Multipulse
- Spectral Scream
- Aquabatics
- Barbed Web
- Cold Truth
- Fever Pitch
- Thunder Raid
- Uproot
- Bunraku Beatdown
- Matrix Shot
- Desert's Mark
- Decimation
- Pyrokinesis
- Irritation
- Magma Drift
- Mud Barrage
- Slash and Burn
- Quicksilver Spear
- Solar Flare
- Hexing Slash
- Wake-Up Shock
- Ethereal Tempest
- Mirror Beam

Rejuvenation-specific custom type records were also retained source-faithfully:
- QMARKS: Unleashed Power, Blinding Speed, Domain Shift
- Shadow: Chthonic Malady

## Animation status

The wiki-converter move database certifies move definitions/mechanics metadata, not animation scripts or assets. Animation remains a separate later audit for these entries.

## Next restart point

**All-Type Source Sweep 04** — audit the next public project source-wide and deduplicate against the **293-move** master catalog.
