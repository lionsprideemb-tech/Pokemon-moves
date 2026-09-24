# Community Move Collection Scope

## Goal

Build a reusable GitHub library of **non-vanilla Pokémon moves and move-animation references** for later Mercury Redux integration on Nintendo DS.

The collection is not limited to Electric moves or to any single gameplay gap.

## Required coverage

Audit all 18 Pokémon types and collect community-created moves in both damaging categories:

- Physical
- Special

Status moves are also included whenever a source contains original designs, because the project goal is a broad non-vanilla move library rather than only attacking moves.

## Collection method

Use **source-wide sweeps**.

When a public ROM hack, fangame, decomp project, battle simulator, or related source is audited:

1. Identify every clearly non-vanilla move in the source.
2. Record all types/categories in the same pass.
3. Deduplicate against the existing master manifest.
4. Preserve exact repository, commit, and source path.
5. Record mechanics separately from animation evidence.
6. Mark whether the animation is DS-native, reusable, adaptable, or requires recreation/conversion.
7. Respect source licensing. If reuse permission is unclear, store metadata/provenance only rather than copying code/assets.

This replaces the earlier narrow workflow of finishing one Electric subcategory before looking elsewhere.

## Master data location

`manifests/community_moves.csv` is the canonical discovered-move manifest.

Required fields already include:
- source project/repository/commit
- move identifier/name
- type
- category
- power/accuracy/PP
- primary and secondary effects
- role tags
- source path
- animation status/reference
- license status
- DS portability
- notes

## Animation objective

For each move, prefer the strongest available evidence in this order:

1. Native Nintendo DS / hg-engine animation implementation.
2. DS animation assembled from existing Gen IV assets.
3. Openly reusable cross-engine animation source that can be converted.
4. Source-certified animation reference from a non-DS engine.
5. Mechanics-only concept requiring a new DS animation later.

## Completion definition

The discovery phase is complete only after multiple major public sources have been audited and the resulting catalog spans **all 18 types**, with Physical and Special moves represented wherever community projects provide them.

A type/category cell may remain empty only when the audited sources genuinely contain no suitable original move; it should not be skipped merely because another category was being prioritized.
