# P00-002 Define State Model

## Status

Done

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the canonical backend state shape for the local server MVP.

## Acceptance Criteria

- [x] `docs/state-model.md` describes session, scene, tracker, initiative, and GM-only fields needed for the MVP.
- [x] Public versus private fields are explicitly identified.
- [x] The model avoids exposing hidden GM notes, private counters, unrevealed monsters, secrets, keys, tokens, and local file paths.
- [x] The model is small enough to implement without a database.

## Notes

Depends on P00-001. This blocks route, projection, and unit-test tickets.

Completed by `docs/state-model.md`. Remaining open model-adjacent questions are listed in that document and should be resolved during API and implementation planning.
