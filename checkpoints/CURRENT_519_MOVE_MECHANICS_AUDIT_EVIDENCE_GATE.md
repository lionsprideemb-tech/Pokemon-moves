# Current 519-Move Mechanics Audit — Evidence Gate

Status: **MECHANICS AUDIT COMPLETE EXCEPT SOURCE-EVIDENCE BLOCKERS**

Date: 2026-09-24

- Current catalog: **519 unique moves**
- Fully source-resolved: **514**
- Source-limited: **3**
- Source-conflict: **2**
- Approval remains disabled for every non-complete record.
- Internal function/effect codes are not used as player-facing explanations.

## Remaining evidence blockers

### HUNTERSWILDS
- Status: **source-limited**
- Current verified explanation: Targets one adjacent Pokémon with 100% accuracy and 2 PP. The public Vanguard data states that the move produces different effects depending on which of the user's attacking stats is higher, but the public PokeRover snapshot does not include the custom runtime function that defines those branches. The exact Attack-higher and Sp. Atk-higher effects therefore remain unverified and are not guessed.

### TERRESTRIALCLAW
- Status: **source-limited**
- Current verified explanation: Deals 70 base-power physical Dragon-type damage with 100% accuracy and makes contact. The source says it raises different stats depending on the active terrain, but the public PokeRover snapshot does not contain the custom TypeAndPowerDependOnTerrain implementation or the terrain-to-stat mapping. Those exact boosts are therefore not guessed.

### SHUFFLE
- Status: **source-conflict**
- Current verified explanation: The pinned Uranium 1.3.1 row lists Shuffle as a 60-power Normal-type special move with 90% accuracy and 15 PP, and says the bomb-like gift may restore HP. However, that same row assigns function code 0D6—the Roost healing function used by Roost in the very same Uranium move table—and gives a 100% effect-chance field. No Pokémon in the pinned public pokemon.txt learn Shuffle, and the public Uranium move list does not document it. Because the damage-versus-healing behavior cannot be reconciled from the available source, no heal chance or heal amount is invented.
- Evidence gap/conflict: Source limitation: exact heal chance/amount is not documented in the audited public move data.

### ZARZAS
- Status: **source-limited**
- Current verified explanation: Deals 90 base-power Grass-type physical damage with 95% accuracy and 15 PP, then partially traps the target for 4–5 turns. While trapped, the target cannot switch normally and takes residual damage at the end of each turn. The pinned Opalo data certifies the 0CF binding-effect family and the 4–5 turn duration through matching moves in the same dataset, but the mirror does not include Opalo's runtime script needed to certify the exact fraction of max HP lost each turn.
- Evidence gap/conflict: Exact per-turn residual-damage fraction is not source-certified by the public Opalo mirror.

### PROTOPLUMA
- Status: **source-conflict**
- Current verified explanation: Deals 60 base-power physical Rock-type damage with 100% accuracy and 15 PP. The source description says the move can make the target flinch, but the pinned Armonia row stores an effect chance of 0%. Because the same 00F effect family is used by flinching moves such as Bite, Air Slash, Headbutt, Zen Headbutt, Waterfall, and Rock Slide, the intended secondary effect is clearly flinching; however, the audited data does not provide a nonzero percentage for Protopluma.
- Evidence gap/conflict: Source conflict: the description mentions a possible flinch, while the machine-readable effect chance is 0. The approval board treats the actual data row as the current behavior and flags the text discrepancy.

## Required evidence to unlock the remaining entries

- **HUNTERSWILDS** — Project Vanguard runtime implementation for `EffectDependsOnHigherDamage`, specifically the Attack-higher and Sp. Atk-higher branches.
- **TERRESTRIALCLAW** — Project Vanguard runtime override for `TypeAndPowerDependOnTerrain`, specifically Vanguard's terrain-to-stat/type/power behavior.
- **SHUFFLE** — Pokémon Uranium runtime implementation or authoritative documentation reconciling its damaging PBS stats/description with function code `0D6`.
- **PROTOPLUMA** — original Armonia runtime or authoritative documentation resolving the description's flinch claim versus the pinned row's 0% effect chance.
- Any other entry that becomes conflicting during later provenance review must be returned to a non-complete status rather than guessed.

## Review rule

The interactive approval board must not allow the user to approve a move whose mechanics audit is `source-limited` or `source-conflict`. Review begins only after the move's behavior is understandable in plain English and either source-resolved or explicitly removed from the candidate library.
