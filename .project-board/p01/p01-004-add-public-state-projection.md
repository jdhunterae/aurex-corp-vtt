# P01-004 Add Public State Projection

## Status

Done

## Phase

Phase 1 - Application Skeleton

## Goal

Implement the public projection layer used by player routes and APIs.

## Acceptance Criteria

- [x] Projection returns only fields documented in the public contract.
- [x] Projection is covered by unit tests.
- [x] Player routes and player API payloads use projection output.
- [x] `/api/s/<session_id>/public` route returns projection output.
- [x] Projection includes session ID/name and empty or default scene/tracker/initiative fields.
- [x] Projection handles globally hidden initiative as `null`.
- [x] Projection includes app-managed asset ID and URL when a scene image exists.
- [x] GM-only fields are never exposed through player-facing responses.
- [x] Projection function is pure or close to pure so it can be tested without Flask where practical.

## Notes

Depends on P00-003 and P01-003.

This ticket is the primary safety boundary for player-facing state. Add tests before or with the route hookup.

Completed in `app/projection.py`, `app/server.py`, and `tests/test_projection.py`.
