# P00-006 Define Local Persistence Strategy

## Status

Done

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the local save/load persistence approach required for the MVP.

## Acceptance Criteria

- [x] Persistence format is documented.
- [x] JSON save files include schema/version metadata.
- [x] MVP save location uses project-local `data/` and notes the long-term goal of moving user data outside the app directory.
- [x] Foldered session layout is documented.
- [x] Load validation and error handling expectations are documented.
- [x] Autosave after every GM action is documented.
- [x] Three-slot rolling autosave behavior is documented.
- [x] Autosave warm-up behavior for empty slots is documented.
- [x] Manual save/export behavior is documented.
- [x] Manual saves are GM-named and timestamped.
- [x] Manual save replace-versus-copy behavior is documented.
- [x] Export behavior is documented separately from in-session manual saves.
- [x] Export behavior accounts for browser download versus app-configured server-side export directory constraints.
- [x] Restore or rewind behavior is documented.
- [x] Loading any manual save or autosave requires GM confirmation before replacing active state.
- [x] Corrupt save recovery behavior notifies the GM and offers timestamped restore options.
- [x] Private GM-only state remains local and is never exposed through player routes.
- [x] Persistence can save and restore all MVP state through Phase 4.

## Notes

Depends on P00-002. Local save/load is required before the MVP is complete because session data must survive errors. MVP should support foldered sessions so prep contexts can have different maps, trackers, initiative state, assets, and saves. Autosave should keep 3 rolling restore points: most recent, roughly 5-10 minutes old, and roughly 10-30 minutes old. Empty autosave slots should be populated during startup/warm-up, then naturally drift toward target age windows. Manual save creates GM-named, timestamped save files in the session folder and should ask whether to replace the previous manual save or preserve it as a copy. Export is a separate workflow for saving a named file outside the session folder where platform constraints allow it. MVP export may be a browser download; if the server writes exports directly, it should use an app-configured export directory rather than assuming arbitrary folder selection. If a save is corrupt, the GM should be notified and offered timestamped autosave/manual save options to attempt loading.

Completed by `docs/state-model.md` and `docs/api.md`.
