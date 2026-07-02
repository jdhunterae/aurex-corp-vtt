# P03-002 Add Tracker State and Projection

## Status

Done

## Phase

Phase 3 - Generic Trackers

## Goal

Complete tracker state and public projection behavior.

## Acceptance Criteria

- [x] Tracker state matches the documented model.
- [x] Public projection includes only visible trackers.
- [x] Public projection supports numeric-only tracker display.
- [x] Public projection supports named-state tracker display.
- [x] Public projection supports display modes: number, label, label_color, number_label.
- [x] Public projection handles interval-mapped tracker states.
- [x] Public projection can hide raw numeric progress for interval-mapped trackers.
- [x] Public projection supports default tracker color scales.
- [x] Public projection uses custom named-value colors only when present and otherwise derives colors from the selected default color scale.
- [x] Public projection handles missing or malformed optional tracker fields safely.
- [x] Hidden trackers are excluded from player-facing payloads.
- [x] Projection behavior is covered by focused unit tests for all display modes and hidden/private-field exclusion.

## Notes

Depends on P03-001 and P01-004.

`app/state.py` already initializes `trackers` as an empty list, and `app/projection.py` already contains basic tracker projection helpers. Current helper coverage is partial: hidden trackers and one `label_color` interval case are tested, but default color scale derivation, all display modes, malformed optional fields, and validation boundaries still need Phase 3 work.

This ticket should preserve the player safety boundary from Phase 1: hidden trackers, GM notes, local paths, and any private tracker fields must not appear in `/api/s/<session_id>/public`.

Completed in `app/projection.py` with coverage in `tests/test_tracker_projection.py`.
