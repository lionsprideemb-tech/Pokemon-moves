# Community Discovery Scope Correction — All Types

Status: **LOCKED**

Date: 2026-09-24

The community-move project scope is now explicitly:

- all 18 Pokémon types
- Physical moves
- Special moves
- Status moves retained as part of the broader non-vanilla library

The earlier Physical Electric batch is only the first seed batch. It is **not** the project boundary and should not cause the discovery process to stay on Electric until that type is exhausted.

New discovery workflow: perform **source-wide sweeps** and collect every distinct custom move from each audited public project across all types/categories, then deduplicate into `manifests/community_moves.csv`.

Existing seed:
- Electric / Physical: 5 source-certified moves from Pokémon Elite Redux

Next restart point:
**All-Type Source Sweep 01** — audit a source for its complete custom-move set, not just its Electric moves.
