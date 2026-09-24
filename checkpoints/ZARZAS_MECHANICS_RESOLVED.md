# Zarzas / Brambles mechanics resolution

Date: 2026-09-24

Move: **ZARZAS / Zarzas**  
English review name: **Brambles**  
Provisional Mercury ID: **1337**

Resolved mechanics:
- Grass / Physical
- 90 BP
- 95% accuracy
- 15 PP
- contact
- successful hit applies the standard 0CF binding/trapping family
- binding lasts 4–5 turns
- trapped target cannot switch normally
- trapped target loses 1/16 of maximum HP at the end of each trapped turn

Evidence chain:
1. The pinned Opalo row assigns Zarzas function family `0CF`.
2. Bind, Wrap, Fire Spin, and Sand Tomb in that same pinned Opalo table use `0CF` and explicitly say 4–5 turns.
3. Matching legacy Pokémon Essentials `PokeBattle_Move_0CF` code defines 1/16 max-HP residual damage.

Result: the previous source-limited blocker is cleared. No mechanic was guessed.
