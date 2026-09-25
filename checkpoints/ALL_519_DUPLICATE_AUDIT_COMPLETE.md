# 519-move duplicate / redundancy audit

Date: 2026-09-24

## Result

Every one of the **519 candidate moves** was compared against the rest of the catalog using:
- type and damage category
- base power / accuracy / PP
- priority and target
- contact and move/ability interaction flags
- secondary-effect family and chance
- status/stat changes
- multi-hit/duration rules
- recoil, drain/healing, switching, weather/terrain/field behavior
- audited plain-English behavior

### Exact duplicates found: **1 pair**

**1114 Swift Strike** and **1116 Shadow Step** are functionally identical:
- Fighting / Physical
- 40 BP
- 100% accuracy
- 30 PP
- +1 priority
- contact
- same target
- same flags
- no secondary effect

This pair should **not both survive final approval unchanged**.

## High-overlap families

The audit also found several families that are not literal duplicates but occupy almost the same mechanical niche. These are flagged in `manifests/MOVE_DUPLICATE_REVIEW.csv` and on the approval board so they can be reviewed deliberately instead of accidentally keeping redundant moves.

Highest-priority overlap checks:
- Shocking Jab / Shocking Edge
- Aqua Fang / Aqua Bash
- Lovely Bite / Cutsie Slap / Cupid Shot / Squeaky Hammer
- Frost Brand / Frost Bolt / Chiller
- Fertile Fangs / Bramble Blast
- Flame Tongue / Blazing Arrow / Smolder Bash / Spread Bomb
- Beatdown / Relentless Clobber
- Blazing Stampede / Solar Flare

## Same-effect but meaningfully distinct

Other same-effect families were checked and are **not duplicates** because power/accuracy, targeting, priority, ability tags, contact state, crit behavior, or other mechanics create materially different roles. They remain documented in the manifest as `SAME_EFFECT_DISTINCT` or `SAME_ROLE_DISTINCT`.

## Rule going forward

A move is considered a duplicate only when its actual battle behavior is the same—not merely because it shares a type or status effect. Ability interaction tags such as Strong Jaw, Iron Fist, Keen Edge, Hammer, Arrow, Mega Launcher, contact state, targeting, priority, and meaningful power/accuracy/PP tradeoffs count as legitimate mechanical distinctions.

No move was deleted automatically. The exact duplicate and high-overlap families are now visible during approval so the final 519 list can be trimmed or redesigned deliberately.
