# Mercury 519-move duplicate audit

Date: 2026-09-24

Status: **FIRST FULL CATALOG DUPLICATE PASS COMPLETE**

I compared all 519 candidate moves against each other using:
- exact type/category/power/accuracy/PP/effect matching;
- audited priority, target, contact, flags, status/stat effects, recoil/drain, switching, multihit, and field behavior;
- plain-English mechanics similarity for same-type/same-category moves;
- a manual review of the highest-overlap groups.

## Confirmed exact duplicate

### 1114 — Swift Strike
### 1116 — Shadow Step

These two are not merely similar. Their pinned Vanguard/PokeRover source records are identical:
- Fighting / Physical
- 40 BP
- 100 accuracy
- 30 PP
- +1 priority
- one adjacent target
- contact
- Protect-blocked
- Mirror Move-compatible
- FunctionCode None
- exact same description

**Final Mercury should not keep both unchanged.**

## Strong role-overlap groups

The following are not byte-for-byte duplicates, but they occupy nearly the same battle role and deserve a keep/merge/redesign decision before final import:

1. **Wormhole / Think Fast** — both 40 BP Psychic special +1 priority attacks with no secondary effect; only PP differs.
2. **Instant Crush / Wormhole / Think Fast** — three Psychic special +1 priority moves with no secondary effect.
3. **Stampede / Migration** — Flying physical contact pivot attacks; numerical differences only.
4. **Blazing Stampede / Solar Flare** — Fire physical attacks with the same 50% Attack +1 secondary.
5. **Ethereal Tempest / Sky Fall** — Flying special attacks in the same power band with paralysis secondaries.
6. **Fang Leech / Mana Fangs** — Dragon physical draining attacks at different power/drain tiers.
7. **Zombie Strike / Elbow Drop** — Ghost physical contact attacks with no secondary effect.
8. **Beatdown / Relentless Clobber** — same Dark physical 25 BP 2–5-hit move; Relentless Clobber's only major distinction is the Hammer tag.

## Similar moves that are *not* duplicates

I also checked the obvious same-type/same-effect clusters. These have meaningful interaction differences and should not be automatically removed:

- **Aqua Fang / Aqua Bash** — bite/Strong Jaw versus horn synergy.
- **Lovely Bite / Cutsie Slap** — bite/Strong Jaw versus Iron Fist.
- **Flame Tongue / Smolder Bash** — blade/Keen Edge versus horn.
- **Cupid Shot / Squeaky Hammer** — non-contact arrow versus contact hammer.
- **Totemic Fury / Illusory Sand** — single-target versus spread tri-status attack.
- **Fire Bomb / Fiery Horn** — major power tier plus non-contact versus contact/horn role.

## Important conclusion

There is **one confirmed exact duplicate pair** in the current 519-source catalog, plus several role-overlap groups that could feel duplicated in play even though their source records differ.

No source rows were deleted in this audit. The source catalog should remain intact for provenance. Final Mercury selection should instead reject, merge, or redesign redundant candidates before final compact IDs are generated.

Detailed classifications are in:
`manifests/MERCURY_DUPLICATE_REVIEW.csv`
