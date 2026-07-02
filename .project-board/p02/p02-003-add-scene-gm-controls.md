# P02-003 Add Scene GM Controls

## Status

Done

## Phase

Phase 2 - Scene Display

## Goal

Allow the GM to update the public scene through server-side routes or APIs.

## Acceptance Criteria

- [x] GM can update scene title.
- [x] GM can update scene description.
- [ ] GM can import or upload a local image into app-managed assets. Deferred to P02-004.
- [ ] GM can provide a URL for the server to download an image into app-managed assets. Deferred to P02-004.
- [x] GM can select an app-managed scene image reference for public display.
- [x] Scene updates are validated server-side.
- [x] Scene update behavior is covered by tests.

## Notes

Depends on P02-001, P01-003, and P01-005.

Completed scene title, description, and existing asset reference controls in `app/scenes.py`, `app/server.py`, and `app/templates/gm_session.html`.

Asset upload and URL download are intentionally deferred to P02-004, the dedicated asset ingestion ticket.
