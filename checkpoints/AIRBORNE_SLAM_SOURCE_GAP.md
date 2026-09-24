# Airborne Slam source gap

Candidate: **MOVE_AIRBORNE_SLAM**  
Provisional Mercury ID: **1013**  
Found during: **BULK02**

Pinned Elite Redux MoveList.textproto confirms:
- Normal / Physical
- target: selected
- ignores Protect
- Hammer flag
- donor animation: Gigaton Hammer
- prose: 20% chance to confuse

But the same source record omits:
- base power
- accuracy
- PP
- machine-readable effect chance

It also uses `EFFECT_PLACEHOLDER`.

Decision: **do not invent missing values**. Keep the move in the candidate catalog but quarantine it as `source-limited` until a reliable implementation/source is found or Mercury Redux deliberately redesigns it during approval.
