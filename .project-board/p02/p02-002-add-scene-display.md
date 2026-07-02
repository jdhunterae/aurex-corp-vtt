# P02-002 Add Scene Display

## Status

Done

## Phase

Phase 2 - Scene Display

## Goal

Show the current public scene on the player display.

## Acceptance Criteria

- [x] Player display renders public scene title.
- [x] Player display renders public scene description.
- [x] Player display renders the approved public scene image reference.
- [x] Missing scene data has a readable fallback state.

## Notes

Depends on P02-001 and P01-004.

Completed in `app/templates/player.html` with projection-backed route data and coverage in `tests/test_scene_display.py`.
