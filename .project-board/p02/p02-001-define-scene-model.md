# P02-001 Define Scene Model

## Status

Done

## Phase

Phase 2 - Scene Display

## Goal

Define the MVP scene fields and visibility rules before implementing scene display.

## Acceptance Criteria

- [x] Scene title, description, and image fields are documented.
- [x] Public versus GM-only scene fields are identified.
- [x] Local image import/upload rules are documented.
- [x] URL image download rules are documented.
- [x] Supported image formats are documented: jpg/jpeg, tiff, png, gif, webp, svg.
- [x] Local file paths and arbitrary external URLs are never exposed to the player display.
- [x] Public scene images are represented by app-managed asset references.
- [x] Public scene image payloads include asset ID and resolved app URL.
- [x] Scene update validation requirements are listed.

## Notes

Depends on P00-002 and P00-003.

Completed by `docs/state-model.md` and `docs/api.md`.
