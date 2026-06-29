# P00-006 Define Local Persistence Strategy

## Status

Ready

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the local save/load persistence approach required for the MVP.

## Acceptance Criteria

- [ ] Persistence format is documented.
- [ ] Save location rules are documented.
- [ ] Load validation and error handling expectations are documented.
- [ ] Private GM-only state remains local and is never exposed through player routes.
- [ ] Persistence can save and restore all MVP state through Phase 4.

## Notes

Depends on P00-002. Local save/load is required before the MVP is complete because session data must survive errors.
