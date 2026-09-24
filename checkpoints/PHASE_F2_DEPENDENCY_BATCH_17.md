# Phase F2 Dependency Audit — Batch 17

Status: **PASS**

Verified on 2026-09-24.

Audited sorted required-effect positions **161–170 of 173**:

- 396 — BELCH
- 397 — STUFF_CHEEKS
- 398 — POWDER
- 399 — LASER_FOCUS
- 400 — GLAIVE_RUSH
- 401 — THROAT_CHOP
- 402 — FINAL_GAMBIT
- 403 — RECOIL_HALF_MAX_HP
- 404 — GIVE_HELD_ITEM
- 405 — IGNORE_PROTECT

Findings:
- No direct `Call BATTLE_SUBSCRIPT_*` dependencies occur in this batch.
- Four side-effect pointers appear, all new to the cumulative audit.
- Belch and Stuff Cheeks have confirmed pre-move/selection eligibility logic outside their effect scripts.
- Glaive Rush and Throat Chop use `SetMoveConditionFlag` backed by battle-state handling in `battle_script_commands.c`.
- Final Gambit's fixed damage is in-script, but the user's faint is a post-move engine hook.
- Half-max-HP recoil has confirmed base-damage/Reckless and post-move recoil hooks.
- Bestow has explicit pre-move item/species validation.
- Ignore Protect is generic damage only and relies on pre-move protection-bypass logic.

Cumulative Phase F2 audit coverage: **170/173**.

Next restart point: **Phase F2 Batch 18 — final sorted required-effect positions 171–173.**
