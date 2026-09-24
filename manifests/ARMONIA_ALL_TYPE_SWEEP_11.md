# Pokémon Armonia Dataset — All-Type Source Sweep 11

Status: **PASS — SOURCE-WIDE CATALOG IMPORTED**

Date: 2026-09-24

Source:
- Dataset directory: `JsonTransformer/txt/armonia/`
- Public repository: `xorgies/PokemonOpalo`
- Pinned commit: `2133a2c0db1a0d8a78a6cc7090fddc62a0d0afeb`
- Move data: `JsonTransformer/txt/armonia/moves.txt`
- Repository README documents the project as a text-to-JSON/database/web converter; it does not separately document the Armonia dataset's authorship
- Repository-level license: not detected
- Library policy: metadata/provenance only; DS mechanics and animations must be recreated or separately sourced

## Filtering safeguards

The Spanish source table was filtered to remove clear official/alias entries:
- Struggle / Combate
- Flip Turn / Viraje
- Smart Strike / Cuerno Certero
- Leafage / Follaje
- Rock Smash helper alias / ROCKSMASHH

The source also contains five helper records with the same display name **Golpe Bífido**:
- BIFIDOFANTASMA
- BIFIDOTIERRA
- BIFIDOBICHO
- BIFIDOVOLADOR
- BIFIDOROCA

Those five records share the same display name, power, accuracy, PP and category but use different type/effect helper fields. They were cataloged once as a **variant family** instead of five duplicate move-name rows. Exact multi-type mapping is marked for a later gameplay-script audit.

## Result

**46 new unique designs** were imported:
- **22 Physical**
- **20 Special**
- **4 Status**

Notable examples include:
- Plegaria Cálamo
- Púa Burbuja
- Floraleteo
- Cuerno Ígneo
- Fermentación
- Protopluma
- Poder Ninfa / Ignis / Volta / Cimex / Aqua
- Arena Ilusoria
- Lluvia de Puños
- Mordisco Feroz
- Poder Evolutivo
- Ebullición
- Tres Deseos
- Rito Chamánico
- Patronaje
- Aerogenerador
- Hiedra Ágil
- Táser
- Aguas Nocivas
- Fuego Cruzado
- Electroarena
- Golpe Bífido
- Roca Voltaica
- Galope Espectral
- Ira Llameante
- Enfriar
- Zambullida
- Dardos Reales
- Mordisco Cardúmen

## Sibling Hispalis check

The same repository includes `JsonTransformer/txt/hispalis/moves.txt`.

That file contains **281 move records**. After current official-ID and legacy-alias filtering, **0** non-official move IDs remained. It is therefore recorded as checked but does not add entries to the master catalog.

## Master catalog

Before Sweep 11: **470**
After Sweep 11: **516**

Current totals:
- **285 Physical**
- **164 Special**
- **67 Status**
- **484 canonical-type designs**

Duplicate normalized IDs: **0**
Duplicate normalized names: **0**

## Animation status

The audited repository is a data/web project and does not provide Nintendo DS battle-animation assets for these moves. Animation remains a later DS sourcing/recreation task.

## Next restart point

**All-Type Source Sweep 12** — audit the next public project source-wide and deduplicate against the **516-move** master catalog.
