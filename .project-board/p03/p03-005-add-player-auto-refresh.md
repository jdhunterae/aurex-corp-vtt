# P03-005 Add Player Auto Refresh

## Status

Done

## Phase

Phase 3 - Generic Trackers

## Goal

Keep the passive player display updated after GM changes without requiring players to manually refresh.

## Acceptance Criteria

- [x] Player display automatically updates after GM changes to public scene state.
- [x] Player display automatically updates after GM changes to visible public trackers.
- [x] Player display automatically updates after any current or future GM action that changes public projected state.
- [x] The update mechanism consumes only `/api/s/<session_id>/public` or another explicit public projection endpoint.
- [x] The update mechanism does not expose full GM state, hidden trackers, hidden scenes, local paths, source URLs, or private notes.
- [x] The first implementation avoids WebSockets unless explicitly promoted; polling or server-sent events should be evaluated first.
- [x] The implementation is resilient when the public endpoint temporarily fails and resumes updating without requiring a page reload.
- [x] Update behavior is covered by tests where practical.

## Notes

Manual refresh after every GM update defeats the purpose of the player display. This is a core local-table usability requirement, not a later online-hosting feature.

Completed with a player-only polling script that reads the public projection endpoint every 5 seconds, re-renders scene and tracker DOM from public projected state, and shows a non-interrupting retry countdown when polling fails.

Implemented in `app/static/player-display.js`, `app/templates/player.html`, and `app/static/styles.css`, with focused coverage in `tests/test_player_refresh.py`.
