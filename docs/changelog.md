# Changelog

## Phase 3

### Generic Trackers

- Added generic tracker state helpers for bounded and unbounded numeric trackers.
- Added tracker validation for labels, values, bounds, intervals, display modes, color scales, named values, and step controls.
- Added public tracker projection for number, label, label_color, and number_label display modes.
- Added GM tracker create, update, and adjustment controls.
- Added player tracker rendering backed only by public projected state.
- Added player auto-refresh using public projection polling.
- Added non-interrupting stale-display warning with retry countdown when public polling fails.
- Added GM and player scroll-position retention around form updates and player auto-refresh.
- Added route, projection, control, and display tests for tracker behavior.

Remaining Phase 3 work:

- Redesign the GM control layout for faster live-session use.
- Add GM action feedback for scene updates.

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
