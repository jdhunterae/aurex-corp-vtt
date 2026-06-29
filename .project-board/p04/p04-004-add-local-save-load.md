# P04-004 Add Local Save Load

## Status

Backlog

## Phase

Phase 4 - Initiative Tracker

## Goal

Add local save/load support for the complete MVP state after scene, tracker, and initiative models exist.

## Acceptance Criteria

- [ ] GM can save the current local session state.
- [ ] GM can load a previously saved local session state.
- [ ] Loaded state is validated before replacing active state.
- [ ] Save/load includes scene, trackers, initiative, and GM-only fields defined for the MVP.
- [ ] Corrupt or incompatible save data fails with a clear error instead of crashing the server.
- [ ] Save/load behavior is covered by unit tests.

## Notes

Depends on P00-006, P02-003, P03-003, and P04-003. This ticket is placed in Phase 4 for now because the roadmap has no persistence phase yet; it should move if the roadmap adds a dedicated persistence phase.
