# P03-004 Add Tracker Player Display

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Render public trackers on the passive player display using only the public state projection.

## Acceptance Criteria

- [ ] Player display renders visible public trackers from `public_state.trackers`.
- [ ] Player display does not render hidden trackers.
- [ ] Player display supports tracker display modes: number, label, label_color, number_label.
- [ ] Player display presents interval-mapped trackers without revealing hidden raw progress unless the selected display mode includes the number.
- [ ] Player display uses projected color values for `label_color` trackers without reading full tracker state.
- [ ] Player display remains readable from across a room.
- [ ] Empty tracker state does not create distracting placeholder UI.
- [ ] Player route and rendered HTML do not expose GM notes, hidden trackers, local paths, source URLs, or private tracker fields.
- [ ] Player tracker rendering is covered by route or template tests.

## Notes

Depends on P03-002.

The current Phase 2 player template renders scene content only. This ticket adds the player-facing tracker widget area after tracker state and projection behavior are finalized.

The player display must consume `public_state.trackers`; it must not receive or inspect the full session tracker state.
