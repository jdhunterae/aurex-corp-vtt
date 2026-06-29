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
- [ ] GM actions trigger autosave.
- [ ] GM can create manual save/export restore points.
- [ ] Manual saves are GM-named and timestamped.
- [ ] Manual save asks whether to replace the previous manual save or save as a copy.
- [ ] Export is available as a separate workflow from manual in-session save.
- [ ] Foldered sessions keep assets and saves scoped to the selected session.
- [ ] Each foldered session keeps 3 rolling autosave restore points.
- [ ] Loaded state is validated before replacing active state.
- [ ] Loading any save requires GM confirmation before active state is replaced.
- [ ] Corrupt save handling notifies the GM and offers timestamped autosave/manual save options.
- [ ] Save/load includes scene, trackers, initiative, and GM-only fields defined for the MVP.
- [ ] Corrupt or incompatible save data fails with a clear error instead of crashing the server.
- [ ] Save/load behavior is covered by unit tests.

## Notes

Depends on P00-006, P02-003, P03-003, and P04-003. This ticket is placed in Phase 4 for now because the roadmap has no persistence phase yet; it should move if the roadmap adds a dedicated persistence phase.
