# Changelog

## Phase 2

### Scene Display

- Added public scene display for the player view.
- Added GM scene controls for title, description, and selected image asset.
- Added app-managed scene image asset upload.
- Added image URL download into session-scoped app-managed assets.
- Added duplicate image detection with GM choice to reuse or keep a copy.
- Added validation so scene images must reference app-managed session assets.
- Added route and projection tests covering scene display, asset ingestion, and player-safe payloads.

## Phase 1

### Application Skeleton

- Added Flask server entrypoint.
- Added GM home, GM session, and player display routes.
- Added shared in-memory session state.
- Added explicit public-state projection for player-facing routes.
- Added basic static assets and templates.
- Added route and projection tests.

## Phase 0

### Repository Initialization

- Created project repository
- Added documentation
- Defined project scope
- Planned application architecture
