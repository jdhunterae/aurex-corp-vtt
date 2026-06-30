# P01-005 Add Basic Route Tests

## Status

Backlog

## Phase

Phase 1 - Application Skeleton

## Goal

Add tests for server startup behavior, page routes, and the public projection boundary.

## Acceptance Criteria

- [ ] Test command runs locally.
- [ ] `pytest` is added or documented as the test runner.
- [ ] GM route test verifies page availability.
- [ ] Player route test verifies page availability.
- [ ] Player polling API test verifies page-safe public payload availability.
- [ ] Public projection test verifies private fields are excluded.
- [ ] Test fixture or helper creates a Flask app without starting a real server.
- [ ] Test fixture or helper isolates session data under a temporary directory.
- [ ] Tests verify player HTML does not embed known GM-only sample strings.

## Notes

Depends on P00-005, P01-002, and P01-004.

Use `docs/testing.md` as the source of truth for test scope. Keep Phase 1 tests focused on the skeleton and public-state safety boundary.
