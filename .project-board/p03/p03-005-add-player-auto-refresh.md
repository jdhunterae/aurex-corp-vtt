# P03-005 Add Player Auto Refresh

## Status

Ready

## Phase

Phase 3 - Generic Trackers

## Goal

Keep the passive player display updated after GM changes without requiring players to manually refresh.

## Acceptance Criteria

- [ ] Player display automatically updates after GM changes to public scene state.
- [ ] Player display automatically updates after GM changes to visible public trackers.
- [ ] Player display automatically updates after any current or future GM action that changes public projected state.
- [ ] The update mechanism consumes only `/api/s/<session_id>/public` or another explicit public projection endpoint.
- [ ] The update mechanism does not expose full GM state, hidden trackers, hidden scenes, local paths, source URLs, or private notes.
- [ ] The first implementation avoids WebSockets unless explicitly promoted; polling or server-sent events should be evaluated first.
- [ ] The implementation is resilient when the public endpoint temporarily fails and resumes updating without requiring a page reload.
- [ ] Update behavior is covered by tests where practical.

## Notes

Manual refresh after every GM update defeats the purpose of the player display. This is a core local-table usability requirement, not a later online-hosting feature.

The current player page has `data-public-state-url` but no client-side update loop yet.

This ticket should be worked before GM layout polish. The app is not usable at the table if players must refresh after each GM action.
