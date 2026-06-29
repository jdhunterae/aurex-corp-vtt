# P00-002 Define State Model

## Status

Ready

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the canonical backend state shape for the local server MVP.

## Acceptance Criteria

- [ ] `docs/state-model.md` describes session, scene, tracker, initiative, and GM-only fields needed for the MVP.
- [ ] Public versus private fields are explicitly identified.
- [ ] The model avoids exposing hidden GM notes, private counters, unrevealed monsters, secrets, keys, tokens, and local file paths.
- [ ] The model is small enough to implement without a database.

## Notes

Depends on P00-001. This blocks route, projection, and unit-test tickets.
