# Mercury Redux custom move ID policy

The current post-Gen-4 official move constants occupy IDs **471–922**. ID **922** is `MOVE_MALIGNANT_CHAIN`.

Custom/community candidates therefore stage from **923** upward. The current 519-candidate library occupies provisional IDs **923–1441**.

Rules:
1. Do not reserve a giant unused numeric block.
2. Candidate IDs are provisional until approval is complete.
3. Final integration compacts only approved moves from the next free official ID.
4. Build work in 50-move batches; the last batch may be smaller.
5. Automated validation runs on every move.
6. Visual certification is deduplicated by donor animation and is mandatory for custom/recreated ports or failures, not for every move individually.
