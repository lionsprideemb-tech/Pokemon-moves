# Full Move Audit Schema and Animation Preview Plan

This document defines the audit standard for the current 519-move community library.

## Mechanics record
Every move should end with these fields resolved or explicitly marked unavailable in the pinned source:

- `move_id`
- `move_name`
- `source_project`
- `source_repo`
- `source_commit`
- `source_data_path`
- `type`
- `category`
- `power`
- `accuracy`
- `pp`
- `priority`
- `target`
- `contact`
- `flags`
- `primary_effect`
- `secondary_effect`
- `effect_chance`
- `status_effects`
- `stat_changes`
- `recoil`
- `drain_or_healing`
- `hit_count_or_duration`
- `switching_behavior`
- `field_weather_terrain_behavior`
- `item_ability_species_interactions`
- `custom_conditions`
- `implementation_notes`

## Animation record
Every move should also receive:

- `source_animation_status`
- `source_animation_reference`
- `source_animation_engine`
- `source_animation_side_variants`
- `source_animation_assets`
- `ds_native`
- `ds_candidate_or_port_plan`
- `preview_status`
- `preview_path_or_url`
- `visual_approval_status`

## Preview gallery design
The gallery should be searchable/filterable by:
- move name
- source project
- type
- Physical / Special / Status
- source animation availability
- DS port state

Each move card should show:
- all mechanics
- source citation/ref
- exact animation mapping where one exists
- source animation preview when renderable
- referenced/reused move preview when the source explicitly reuses an animation
- proposed DS animation preview
- final approved DS animation preview

For animation sources that are not directly playable in a browser:
- GBA animation scripts should be captured from a source-compatible test build/emulator or recreated in a controlled preview harness.
- Pokémon Essentials/RGSS animation mappings should be rendered from their native animation data or recreated as a DS test sequence.
- hg-engine/Platinum animations should be captured from the DS test harness/emulator.
- Data-only sources should display **No source animation** until a DS analog/custom animation is selected.

No visual mapping should be guessed merely to fill a preview slot.
