# Remaining 4 mechanics blockers — source recovery pass

Date: 2026-09-24

The post-bulk source-recovery pass is complete for the four remaining blockers. No additional authoritative runtime implementation was found that safely fills the missing behavior. The remaining issues are now classified as **design-decision blockers**, not search tasks.

## 1013 — Airborne Slam

Authoritative Elite Redux evidence supports:
- Normal / Physical
- selected target
- hammer move
- ignores Protect
- description: 20% chance to confuse
- Gigaton Hammer animation reuse

The pinned er-config record omits base power, accuracy, PP, and an implemented effect body. Historical MoveList revisions checked back through the move's early public history also omit those numeric values.

A separate generated Elite Redux audit/port dataset preserves the same move as 0 power / 0 accuracy / 0 PP while recognizing the confusion behavior, confirming that the missing numbers are source omissions rather than a parsing failure.

A downstream Reborn Reatomized implementation uses **85 BP / 100% accuracy / 10 PP / 20% confusion**, but changes the move to Fighting. This is useful fallback design evidence, not authoritative Elite Redux recovery.

### Mercury recommendation
Keep Elite Redux's source identity and use:
- **Normal / Physical**
- **85 BP / 100% / 10 PP**
- **20% confusion**
- Hammer flag
- ignores Protect
- Gigaton Hammer DS animation

This deliberately borrows only the missing numeric shell from the downstream implementation while preserving Elite Redux's original type/effect identity.

---

## 1160 — Hunter's Wilds

The public Vanguard/PokeRover data provides:
- Grass / Status
- 100% accuracy
- 2 PP
- one adjacent target
- custom function `EffectDependsOnHigherDamage`
- description: effect changes depending on the user's higher attacking stat

Repository-tree inspection confirms the public PokeRover snapshot contains PBS data but not Vanguard's custom battle-script implementation. Exact branches are unrecoverable from the public source.

### Mercury recommendation
Preserve the higher-offense branching concept:
- If **Attack >= Sp. Atk**: lower the target's **Defense by 2 stages**
- If **Sp. Atk > Attack**: lower the target's **Sp. Def by 2 stages**
- Grass / Status / 100% / 2 PP
- one adjacent target

This makes the move automatically expose the defensive side best matched to the user's stronger attacking stat without inventing unrelated mechanics.

---

## 1162 — Terrestrial Claw

The public Vanguard/PokeRover data provides:
- Dragon / Physical
- 70 BP / 100% / 10 PP
- contact
- description: different stats are raised depending on terrain
- function name `TypeAndPowerDependOnTerrain`

The standard Essentials function with that name is Terrain Pulse-like and does not explain Vanguard's stat-boost prose. Repository-tree inspection confirms Vanguard's custom override is absent from the public snapshot.

### Mercury recommendation
Keep the move's sourced damage values and make the post-hit +1 boost terrain-dependent:
- **Electric Terrain:** Speed +1
- **Grassy Terrain:** Defense +1
- **Psychic Terrain:** Attack +1
- **Misty Terrain:** Sp. Def +1
- **No terrain:** no stat boost

The attack itself remains Dragon-type rather than inheriting Terrain Pulse's type-changing behavior.

---

## 1219 — Shuffle

The pinned Uranium 1.3.1 row provides:
- Normal / Special
- 60 BP / 90% / 15 PP
- target: one other Pokémon
- description: "A gift in the form of a bomb. May restore HP."
- effect chance field: 100
- function code 0D6

In the same Uranium table, 0D6 is Roost while Present uses 094. Repository-tree inspection confirms the public uranium-mining source contains the PBS extraction but no runtime scripts to resolve the contradiction.

### Mercury recommendation
Turn the source's Present-like concept into an explicit, deterministic rule:
- **80%:** deal the listed 60 BP Normal special damage
- **20%:** deal no damage and restore **25% of the target's max HP**
- 90% accuracy / 15 PP

This preserves the "bomb gift that may heal" identity without pretending the broken Uranium function code is trustworthy.

---

## Result

No further public-source search is expected to resolve these four faithfully. The next step is to either:
1. approve the Mercury recommendations above and promote all four to mechanics-complete, or
2. deliberately choose different Mercury behavior for any of them.

Until that decision is made, the source audit remains **515/519 complete with 4 design-decision blockers**.
