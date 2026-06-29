# P02-004 Add Scene Asset Ingestion

## Status

Backlog

## Phase

Phase 2 - Scene Display

## Goal

Allow the GM to add scene images through local import/upload or URL download while keeping player-facing image references public-safe.

## Acceptance Criteria

- [ ] GM can add a local image through the documented import/upload workflow.
- [ ] GM can provide a URL that the server downloads into app-managed assets.
- [ ] Imported and downloaded files are validated as supported image types.
- [ ] Player-facing payloads receive only app-managed public asset references.
- [ ] Local filesystem source paths are not stored in public state.
- [ ] URL source values are not exposed to the player display.
- [ ] Failed imports or downloads return clear errors.
- [ ] Asset ingestion behavior is covered by tests.

## Notes

Depends on P02-001. This ticket should define and implement the safe boundary between GM-supplied image sources and player-visible scene assets.
