# Blocker recovery 01 — Airborne Slam

Date: 2026-09-24

Move: **MOVE_AIRBORNE_SLAM / Airborne Slam**  
Provisional Mercury ID: **1013**

## Recovery result

**Still source-limited. Do not invent the missing stats.**

The pinned Elite Redux record confirms:
- Normal type
- Physical category
- selected target
- hammer-based
- 20% confusion in the prose
- Gigaton Hammer animation reuse
- ignores Protect in the source record

But it omits:
- base power
- accuracy
- PP
- a machine-readable effect-chance field

## Historical Elite Redux check

Multiple public `er-config` revisions from March 2025 through July 2026 were sampled. The move consistently appears without power, accuracy, or PP. This is therefore not just a one-commit transcription gap in our catalog.

## Downstream implementation found

Reborn Reatomized exposes an Airborne Slam with:
- Fighting / Physical
- 85 BP
- 100% accuracy
- 10 PP
- 20% confusion
- contact + hammer flags

That is strong fallback design evidence, but it **cannot be treated as authoritative Elite Redux recovery** because Elite Redux's own public record says **Normal**, not Fighting.

## Decision rule

Airborne Slam remains blocked until one of these happens:
1. an authoritative Elite Redux runtime/source record with the missing values is found; or
2. Mercury deliberately adopts a version (for example, the downstream 85/100/10 implementation) as a project design choice.

No values were silently inserted.
