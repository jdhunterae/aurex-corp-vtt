# P00-003 Define Public Projection Contract

## Status

Done

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the explicit public-state payload consumed by the player interface.

## Acceptance Criteria

- [x] `docs/api.md` documents the public payload shape for the MVP.
- [x] The public projection excludes all GM-only fields from P00-002.
- [x] Player-facing asset payloads include both app-managed asset IDs and resolved app URLs.
- [x] Test expectations for projection behavior are listed.
- [x] The projection contract can be implemented as a small pure Python function.

## Notes

Depends on P00-002. This is the main safety boundary for player routes.

Completed by `docs/api.md` and `docs/state-model.md`. Remaining route-level open questions are listed in `docs/api.md`.
