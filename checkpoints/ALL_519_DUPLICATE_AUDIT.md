# 519-move duplicate / redundancy audit

Date: 2026-09-24

Scope: all **519** current candidate moves.

Goal: prevent Mercury Redux from importing two custom moves that are mechanically the same move under different names.

## Result

The catalog does **not** contain widespread duplicates, but it is **not yet duplicate-clean**.

### Confirmed exact duplicate

#### Swift Strike vs Shadow Step

Both are:
- Fighting / Physical
- 40 BP
- 100% accuracy
- 30 PP
- +1 priority
- contact
- one adjacent target
- Protect-blocked / Mirror Move-compatible
- no secondary effect

Their audited descriptions and battle behavior are identical.

**Disposition required before final ID compaction:** keep one, reject one, or deliberately redesign one.

### Confirmed functional duplicate

#### Wormhole vs Think Fast

Both are:
- Psychic / Special
- 40 BP
- 100% accuracy
- +1 priority
- one adjacent target
- non-contact
- Protect-blocked / Mirror Move-compatible
- no secondary effect

Only PP differs:
- Wormhole: 30 PP
- Think Fast: 20 PP

That PP difference does not give them a distinct battle function, so they are functionally redundant for Mercury.

**Disposition required before final ID compaction:** keep one, reject one, or deliberately redesign one.

## High-overlap pairs that are NOT exact duplicates

These were manually checked because automated similarity scoring flagged them.

- **Lovely Bite / Cutsie Slap** — same Fairy 85/100 and 10% infatuation, but Lovely Bite is Strong Jaw-tagged while Cutsie Slap is Iron Fist-tagged.
- **Flame Tongue / Smolder Bash** — same Fire 80/100 and 10% burn, but Flame Tongue is Keen Edge-tagged while Smolder Bash is Horn-tagged.
- **Aqua Fang / Aqua Bash** — both Water physical flinch attacks, but their BP and ability-family tags differ (Strong Jaw vs Horn).
- **Cupid Shot / Squeaky Hammer** — both Fairy physical infatuation attacks, but one is an Arrow/non-contact archetype and the other is a Hammer/contact archetype.
- **Beatdown / Relentless Clobber** — same Dark multi-hit shell, but Relentless Clobber is Hammer-tagged.
- **Soul Sucker / Haunt** — both Ghost physical 50%-drain attacks, but BP and source flags differ (85 vs 75; Soul/Mirror Move distinctions).
- **Blazing Stampede / Solar Flare** — both Fire physical attacks with a 50% Attack +1 chance, but BP/accuracy/contact/PP differ.
- **Zombie Strike / Elbow Drop** — both plain Ghost physical contact attacks, but one is 90 BP / 90% / 15 PP while the other is 100 BP / 100% / 5 PP.

These are role overlaps, not literal clones. They should stay visible during the approval pass, but they do not need automatic removal.

## Audit inconsistency discovered during duplicate review

**Jagged Punch / Diamond Blade** initially appeared duplicate-like in the detailed prose, but the master source catalog says:
- Jagged Punch: `EFFECT_STEALTH_ROCK_HIT`
- Diamond Blade: `EFFECT_BLEED_HIT`

The detailed audit prose currently describes Diamond Blade as a Stealth Rock move, which conflicts with the master source record. Therefore this pair is **not classified as a duplicate** until that audit-detail mismatch is corrected/verified.

## Name-level audit

- Duplicate normalized move names: **0**
- Duplicate symbolic IDs: **0**

## Gate for final import

Do **not** compact final Mercury IDs or begin the final 519-move import with both confirmed duplicate pairs unresolved.

Recommended next action:
1. choose a disposition for Swift Strike / Shadow Step;
2. choose a disposition for Wormhole / Think Fast;
3. verify/correct Diamond Blade's detailed effect record;
4. rerun the duplicate audit;
5. then compact the final approved move IDs.
