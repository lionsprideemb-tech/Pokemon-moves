# Current 519-Move Mechanics Audit — Status Checkpoint

Status: **MECHANICS AUDIT IN PROGRESS — APPROVAL BOARD NOT YET RELEASED FOR FINAL REVIEW**

Date: 2026-09-24

## Current coverage

- Master catalog: **519 unique moves**
- Audit-detail records: **519/519**
- Records with a player-facing move description: **519/519**
- Records with a player-facing "What it does" explanation: **519/519**
- Records with priority, target, and contact information populated: **519/519**
- Obvious placeholder explanations such as only "damage" / "effect code" / raw function names in the approval-facing effect field: **0**
- Fully source-resolved mechanics records: **514**
- Source-limited records: **3**
- Source-conflict records: **2**

The approval board now refuses to treat a move as mechanically approval-ready unless its audit status is `complete` and `approval_ready !== false`.

## Remaining five source blockers

### HUNTERSWILDS — Hunter's Wilds
Pinned Vanguard PBS says the move changes behavior depending on the user's higher attacking stat, using custom function `EffectDependsOnHigherDamage`. The public PokeRover snapshot does not include Vanguard's implementation, so the Attack-dominant and Sp. Atk-dominant branches are not guessed.

### TERRESTRIALCLAW — Terrestrial Claw
Pinned Vanguard PBS confirms 70 BP Dragon / Physical / 100% / 10 PP / contact and says different stats are raised depending on terrain. The custom runtime terrain-to-stat mapping is absent from the public source snapshot, so no mapping is invented.

### SHUFFLE — Shuffle
The pinned Uranium row is internally inconsistent: it is a 60 BP Normal Special damaging move with Present-like flavor text ("may restore HP"), while its function code is `0D6`, which the same Uranium move table assigns to Roost. Its chance field is 100, it has no learner in the pinned public Pokémon table, and public Uranium move documentation does not resolve the intended behavior. Approval is locked rather than inventing a heal chance/amount.

### ZARZAS — Zarzas / Brambles
Pinned Opalo data certifies a 90 BP Grass physical attack using the binding family and supports a 4–5 turn trapping duration. The public data mirror does not contain Opalo's runtime implementation needed to certify the exact residual HP fraction per turn. The approval-facing text therefore states the trapping/residual behavior but does not invent the missing fraction.

### PROTOPLUMA — Protopluma / Proto Feather
Pinned Armonia data says the move may flinch and assigns the standard flinch effect family, but the same row stores a 0% chance. Because the prose and machine-readable chance conflict, no flinch percentage is invented.

## QA rule

No move proceeds to user approval with unexplained internal effect codes. Every status/stat change, chance, multihit rule, priority change, recoil/drain/healing rule, protection interaction, switching rule, field/weather/terrain behavior, and other special condition must be described in plain English when source evidence supports it.

Where the public source is missing or contradictory, the approval board shows the limitation and locks the move rather than silently guessing.

## Next work

Continue source recovery for the five blocked moves. Once those are resolved (or an explicit Mercury Redux behavior is deliberately chosen for an unrecoverable source gap), rerun the 519-row QA and then unlock the approval pass.
