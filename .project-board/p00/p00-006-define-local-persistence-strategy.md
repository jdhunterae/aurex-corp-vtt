# P00-006 Define Local Persistence Strategy

## Status

Ready

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the local save/load persistence approach required for the MVP.

## Acceptance Criteria

- [ ] Persistence format is documented.
- [ ] JSON save files include schema/version metadata.
- [ ] MVP save location uses project-local `data/` and notes the long-term goal of moving user data outside the app directory.
- [ ] Foldered session layout is documented.
- [ ] Load validation and error handling expectations are documented.
- [ ] Autosave after every GM action is documented.
- [ ] Three-slot rolling autosave behavior is documented.
- [ ] Autosave warm-up behavior for empty slots is documented.
- [ ] Manual save/export behavior is documented.
- [ ] Manual saves are GM-named and timestamped.
- [ ] Manual save replace-versus-copy behavior is documented.
- [ ] Export behavior is documented separately from in-session manual saves.
- [ ] Restore or rewind behavior is documented.
- [ ] Loading any manual save or autosave requires GM confirmation before replacing active state.
- [ ] Corrupt save recovery behavior notifies the GM and offers timestamped restore options.
- [ ] Private GM-only state remains local and is never exposed through player routes.
- [ ] Persistence can save and restore all MVP state through Phase 4.

## Notes

Depends on P00-002. Local save/load is required before the MVP is complete because session data must survive errors. MVP should support foldered sessions so prep contexts can have different maps, trackers, initiative state, assets, and saves. Autosave should keep 3 rolling restore points: most recent, roughly 5-10 minutes old, and roughly 10-30 minutes old. Empty autosave slots should be populated during startup/warm-up, then naturally drift toward target age windows. Manual save creates GM-named, timestamped save files in the session folder and should ask whether to replace the previous manual save or preserve it as a copy. Export is a separate workflow for saving a named file outside the session folder where platform constraints allow it. If a save is corrupt, the GM should be notified and offered timestamped autosave/manual save options to attempt loading.
