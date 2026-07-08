# Architecture Context

Purpose: give AI agents a concise, stable map of the current application architecture before they make changes.

## Current Shape

- Aurex Corp VTT is a local-first, minimal Flask virtual tabletop for Dungeons & Dragons.
- The backend owns canonical session state.
- The app has two user-facing surfaces:
  - GM interface: read/write controls.
  - Player interface: passive/read-only public display.
- Player-facing routes and payloads must consume public projected state only.
- Current runtime state is in-memory, with project-local session folders bootstrapped under `data/sessions/`.
- App-managed scene assets are stored under `data/sessions/<session_id>/assets/`.
- Local save/load persistence is planned but not implemented.

## Main Modules

- `app/server.py`: Flask app factory, routes, JSON endpoints, form handlers, asset serving.
- `app/state.py`: in-memory session state and session folder bootstrap helpers.
- `app/projection.py`: public-state projection boundary for player-facing data.
- `app/scenes.py`: scene update and scene image asset validation.
- `app/assets.py`: image upload/download, duplicate detection, asset registration.
- `app/trackers.py`: generic tracker validation, creation, update, and adjustment.
- `app/templates/`: Jinja templates for GM, player, base, and error pages.
- `app/static/`: simple CSS and GM-only JavaScript.

## Route Conventions

- GM page/form routes use `/s/<session_id>/gm/...`.
- GM JSON APIs use `/api/gm/session/<session_id>/...`.
- Player page routes use `/s/<session_id>/player`.
- Player JSON routes use `/api/s/<session_id>/public`.
- The bare session route redirects to the safer player route.

## Current Roadmap Position

- Phase 1 application skeleton: complete.
- Phase 2 scene display: complete, with prepared scene library still backlog.
- Phase 3 generic trackers: in progress.
- Current active ticket: `P03-005 Add Player Auto Refresh`.
- Phase 4 initiative and local save/load: backlog.

## Hard Safety Boundary

Never expose full session state through player routes, player API payloads, static files, or player JavaScript.

Player-facing state must not include GM notes, hidden trackers, hidden scenes, unrevealed combatants, local paths, original asset source URLs, save metadata, GM keys, or tokens.

TODO: Decide the long-term storage location for user data outside the app directory.
TODO: Decide whether session listing/creation remains in Phase 4 or gets its own later phase.
