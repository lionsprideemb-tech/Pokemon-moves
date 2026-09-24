# Pokémon Opalo All-Type Source Sweep 08

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Project represented: Pokémon Opalo
- Public data/web repository: `xorgies/PokemonOpalo`
- Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
- Move data: `JsonTransformer/txt/opalo/moves.txt`
- Repository README describes the project as reading Pokémon Opalo text files, converting them to JSON, and displaying them on a web Pokédex
- Repository-level license: not detected
- Library policy: metadata/provenance only; mechanics and animations must be recreated/ported separately for DS

## Filtering safeguards

The source table mixes original Opalo moves with official Pokémon moves, and some newer official moves use Spanish/internal identifiers that do not match the English identifiers in modern upstream data.

The sweep explicitly excluded official or translated equivalents including:
- High Jump Kick
- Smelling Salts
- Struggle
- Dual Wingbeat / Ala Bis
- Liquidation / Hidroariete
- Flip Turn / Viraje
- First Impression / Escaramuza
- Smart Strike / Cuerno Certero
- Scorching Sands / Arenas Ardientes
- High Horsepower / Fuerza Equina
- Pollen Puff / Bola de Polen
- Psychic Fangs / Psicocolmillo
- Darkest Lariat / Lariat Oscuro
- Accelerock / Roca Veloz
- Lunge / Plancha
- Fire Lash / Látigo Ígneo

This prevented official Gen 7–8 moves from being mislabeled as fan-made designs.

## Result

**30 new unique Pokémon Opalo move designs** were imported:
- **14 Physical**
- **15 Special**
- **1 Status**

All 30 use canonical Pokémon types.

Examples include:
- Tiroteo
- Electrobaba
- Fuego Lunar
- Rompehielos
- Trinchar
- Desbandada
- Fiebre del Oro
- Maldignición
- Limpia Sueños
- Ala Funesta
- Furia Totémica
- Zarzas
- Sombratela
- Abrazo Feroz
- Geoimpacto
- Pipa de la Paz
- Borrasca
- Ojos Terribles
- Drenánima
- Danza Vudú
- Choque Vapor
- Patada Gélida
- Colmillos Salvajes
- Brazo Musgo
- Láser Esencia
- Caricatura
- Flecha Astral
- Lingotazo
- Absorbesencia
- Fuerzaesencia

## Master catalog

Before Sweep 08: **403**
After Sweep 08: **434**

Current totals:
- **251 Physical**
- **125 Special**
- **58 Status**
- **407 canonical-type designs**

## Language handling

The source is Spanish. The manifest preserves the source move names rather than inventing replacement English names. Short English glosses are stored in notes only where helpful.

## Animation status

The audited Opalo repository provides move data for its web/data tooling, not Nintendo DS battle-animation resources. Every imported Opalo move is therefore marked as requiring DS animation recreation/adaptation.

## Next restart point

**All-Type Source Sweep 09** — audit another public project source-wide and deduplicate against the **434-move** master catalog.
