# P03-004 Add Tracker Player Display

## Status

Done

## Phase

Phase 3 - Generic Trackers

## Goal

Render public trackers on the passive player display using only the public state projection.

## Acceptance Criteria

- [x] Player display renders visible public trackers from `public_state.trackers`.
- [x] Player display does not render hidden trackers.
- [x] Player display supports tracker display modes: number, label, label_color, number_label.
- [x] Player display presents interval-mapped trackers without revealing hidden raw progress unless the selected display mode includes the number.
- [x] Player display uses projected color values for `label_color` trackers without reading full tracker state.
- [x] Player display remains readable from across a room.
- [x] Empty tracker state does not create distracting placeholder UI.
- [x] Player route and rendered HTML do not expose GM notes, hidden trackers, local paths, source URLs, or private tracker fields.
- [x] Player tracker rendering is covered by route or template tests.

## Notes

Depends on P03-002.

The current Phase 2 player template renders scene content only. As observed during Phase 3 smoke testing, visible trackers created by the GM do not appear on the player view yet. This ticket adds the player-facing tracker widget area after tracker state and projection behavior are finalized.

The player display must consume `public_state.trackers`; it must not receive or inspect the full session tracker state.

Completed in `app/templates/player.html` and `app/static/styles.css` with coverage in `tests/test_tracker_display.py`.
