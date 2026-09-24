# Current 519-Move Mechanics Audit — Status Checkpoint

Status: **MECHANICS AUDIT NEAR-COMPLETE — FOUR SOURCE BLOCKERS REMAIN**

Date: 2026-09-24

## Current coverage

- Master catalog: **519 unique moves**
- Audit-detail records: **519/519**
- Fully source-resolved mechanics records: **515**
- Source-limited records: **3**
- Source-conflict records: **1**
- Total unresolved/blocker records: **4**

The approval board treats a move as mechanically approval-ready only when its audit status is `complete` and `approval_ready !== false`.

## Remaining source blockers

### MOVE_AIRBORNE_SLAM — Airborne Slam
Pinned Elite Redux MoveList.textproto omits power, accuracy, PP, and effect chance for this move and assigns EFFECT_PLACEHOLDER. The intended battle values cannot be certified from the audited source.

### HUNTERSWILDS — Hunter's Wilds
Targets one adjacent Pokémon with 100% accuracy and 2 PP. The public Vanguard data states that the move produces different effects depending on which of the user's attacking stats is higher, but the public PokeRover snapshot does not include the custom runtime function that defines those branches. The exact Attack-higher and Sp. Atk-higher effects therefore remain unverified and are not guessed.

### TERRESTRIALCLAW — Terrestrial Claw
Deals 70 base-power physical Dragon-type damage with 100% accuracy and makes contact. The source says it raises different stats depending on the active terrain, but the public PokeRover snapshot does not contain the custom TypeAndPowerDependOnTerrain implementation or the terrain-to-stat mapping. Those exact boosts are therefore not guessed.

### SHUFFLE — Shuffle
Source limitation: exact heal chance/amount is not documented in the audited public move data.

## Recently cleared

- **ZARZAS / Brambles** — 0CF binding behavior source-resolved to 4–5 turns and 1/16 max-HP residual damage.
- **PROTOPLUMA / Proto Feather** — encoded behavior resolved as 0% functional flinch; conflicting prose retained as a warning rather than a blocker.
