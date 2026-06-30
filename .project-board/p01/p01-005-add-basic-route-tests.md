# P01-005 Add Basic Route Tests

## Status

Done

## Phase

Phase 1 - Application Skeleton

## Goal

Add tests for server startup behavior, page routes, and the public projection boundary.

## Acceptance Criteria

- [x] Test command runs locally.
- [x] `pytest` is added or documented as the test runner.
- [x] GM route test verifies page availability.
- [x] Player route test verifies page availability.
- [x] Player polling API test verifies page-safe public payload availability.
- [x] Public projection test verifies private fields are excluded.
- [x] Test fixture or helper creates a Flask app without starting a real server.
- [x] Test fixture or helper isolates session data under a temporary directory.
- [x] Tests verify player HTML does not embed known GM-only sample strings.

## Notes

Depends on P00-005, P01-002, and P01-004.

Use `docs/testing.md` as the source of truth for test scope. Keep Phase 1 tests focused on the skeleton and public-state safety boundary.

Completed with `tests/conftest.py`, `tests/test_routes.py`, and `tests/test_projection.py`.
