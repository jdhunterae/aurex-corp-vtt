# P00-003 Define Public Projection Contract

## Status

Ready

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Define the explicit public-state payload consumed by the player interface.

## Acceptance Criteria

- [ ] `docs/api.md` documents the public payload shape for the MVP.
- [ ] The public projection excludes all GM-only fields from P00-002.
- [ ] Test expectations for projection behavior are listed.
- [ ] The projection contract can be implemented as a small pure Python function.

## Notes

Depends on P00-002. This is the main safety boundary for player routes.
