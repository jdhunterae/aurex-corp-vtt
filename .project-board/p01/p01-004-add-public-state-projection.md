# P01-004 Add Public State Projection

## Status

Backlog

## Phase

Phase 1 - Application Skeleton

## Goal

Implement the public projection layer used by player routes and APIs.

## Acceptance Criteria

- [ ] Projection returns only fields documented in the public contract.
- [ ] Projection is covered by unit tests.
- [ ] Player routes and player API payloads use projection output.
- [ ] `/api/session/<session_id>/public` route returns projection output.
- [ ] Projection includes session ID/name and empty or default scene/tracker/initiative fields.
- [ ] Projection handles globally hidden initiative as `null`.
- [ ] Projection includes app-managed asset ID and URL when a scene image exists.
- [ ] GM-only fields are never exposed through player-facing responses.
- [ ] Projection function is pure or close to pure so it can be tested without Flask where practical.

## Notes

Depends on P00-003 and P01-003.

This ticket is the primary safety boundary for player-facing state. Add tests before or with the route hookup.
