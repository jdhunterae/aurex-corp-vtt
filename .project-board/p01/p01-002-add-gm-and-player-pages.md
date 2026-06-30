# P01-002 Add GM and Player Pages

## Status

Done

## Phase

Phase 1 - Application Skeleton

## Goal

Serve basic GM and Player pages from the local server.

## Acceptance Criteria

- [x] GM route returns a readable control page shell.
- [x] Player route returns a readable display page shell.
- [x] `/gm` route exists.
- [x] `/s/<session_id>` route exists and redirects to the safer player view.
- [x] `/s/<session_id>/gm` route exists, even if it initially renders placeholder controls.
- [x] `/s/<session_id>/player` route exists.
- [x] Player page is passive and has no state-changing controls.
- [x] Player page does not embed full GM state in HTML or client-side JavaScript.
- [x] Player page is structured to poll `/api/s/<session_id>/public`.
- [x] Templates and static assets follow the chosen minimal stack.
- [x] Static CSS/JS folders exist only if needed by this ticket.

## Notes

Depends on P01-001.

This ticket should establish page shells only. Do not implement scene, tracker, initiative, upload, save/load, or styling beyond what is needed for a readable skeleton.

Completed with Jinja templates in `app/templates/`, shared CSS in `app/static/styles.css`, and page routes in `app/server.py`.
