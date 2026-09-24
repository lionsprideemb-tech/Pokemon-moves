# Source / Asset Policy

This repository is intended to preserve reusable **source code and metadata** for Nintendo DS Pokémon ROM-hacking work.

Included:
- Community-authored animation scripts.
- Animation command macros/support source.
- Move constant mappings and manifests.
- Attribution and source revision metadata.

Not included:
- Nintendo DS ROMs or patched ROM images.
- Commercial game binaries.
- User-supplied clean ROMs.
- Extracted proprietary graphics/audio archives copied from a ROM.

Some animation scripts reference particle, sound, background, or sprite resources expected to exist in the target DS engine or source ROM. Those references are intentionally preserved so Mercury Redux can resolve them during integration/testing.

Primary upstream: https://github.com/BluRosie/hg-engine
Pinned revision: 398a3020943f1ae98987e5b12b73d9086bbba3ce
