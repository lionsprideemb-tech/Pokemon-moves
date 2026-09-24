# Protopluma / Proto Feather mechanics resolution

Date: 2026-09-24

Move: **PROTOPLUMA / Protopluma**  
English review name: **Proto Feather**  
Provisional Mercury ID: **1398**

Pinned Armonia data:
- Rock / Physical
- 60 BP
- 100% accuracy
- 15 PP
- effect family `00F`
- effect chance `0`
- description says it may make the target flinch

Resolution:
The prose and numeric data disagree about design intent, but the encoded runtime behavior is not ambiguous: a 0% chance means the chance-based flinch does not trigger. The collection therefore records **0% flinch / no functional secondary effect** as the source behavior and preserves the prose mismatch as a non-blocking warning.

No nonzero flinch percentage was invented.
