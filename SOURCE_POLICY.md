# Source / Asset Policy

This repository preserves reusable source and support material for Nintendo DS Pokémon ROM-hacking work.

## Included
- Community-authored hg-engine move animation scripts.
- Matching move battle scripts.
- Animation command macros and move-data/effect support source.
- hg-engine-provided shared sub-animation and move-SPA support material required by its animation implementation.
- Move constant mappings, manifests, documentation, attribution, and pinned source metadata.

## Not included
- Nintendo DS ROMs or patched ROM images.
- User-supplied clean ROMs.
- Commercial game executables/binaries.
- A redistributed base Platinum/HGSS game.

Some animation scripts reference sound, background, sprite, particle, or engine resources that are expected to exist in the target DS project. Mercury Redux integration should resolve and test those dependencies against the legally obtained project/source setup.

Primary upstream: https://github.com/BluRosie/hg-engine
Pinned revision: 398a3020943f1ae98987e5b12b73d9086bbba3ce
