# P01-002 Add GM and Player Pages

## Status

Backlog

## Phase

Phase 1 - Application Skeleton

## Goal

Serve basic GM and Player pages from the local server.

## Acceptance Criteria

- [ ] GM route returns a readable control page shell.
- [ ] Player route returns a readable display page shell.
- [ ] `/gm` route exists.
- [ ] `/gm/session/<session_id>` route exists, even if it initially renders placeholder controls.
- [ ] `/player/<session_id>` route exists.
- [ ] Player page is passive and has no state-changing controls.
- [ ] Player page does not embed full GM state in HTML or client-side JavaScript.
- [ ] Player page is structured to poll `/api/session/<session_id>/public`.
- [ ] Templates and static assets follow the chosen minimal stack.
- [ ] Static CSS/JS folders exist only if needed by this ticket.

## Notes

Depends on P01-001.

This ticket should establish page shells only. Do not implement scene, tracker, initiative, upload, save/load, or styling beyond what is needed for a readable skeleton.
