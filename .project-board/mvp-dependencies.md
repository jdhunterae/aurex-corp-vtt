# MVP Dependency Map

## Current Source of Truth

- Roadmap phases are defined in `docs/roadmap.md`.
- Architecture constraints are defined in `docs/architecture.md`.
- Public API intent is defined in `docs/api.md`.
- Player and GM interface goals are defined in `docs/ui-concepts.md`.

## Open Decisions

- State model: `docs/state-model.md` is currently empty.
- Server stack: the docs call for a Python web server but do not choose a framework or standard-library approach. Flask or Django may be considered if useful, but the app should keep its own backend data model instead of relying on Django ORM/database machinery.
- Persistence: local save/load is required for the MVP but is not assigned to a roadmap phase.
- Image handling: GM image import/upload and URL download are required, but public-safe asset storage and validation rules still need to be defined.

## MVP Boundary

The local server MVP is complete after Phase 4 when the local-network version includes:

- Application skeleton
- Scene display
- Generic trackers
- Initiative tracker
- Local save/load persistence
- Scene image import/upload or URL download into app-managed assets

Hosting beyond the local network and player session connections are post-MVP concerns.

## Dependency Order

1. P00-001 Finalize Local Server MVP Scope
2. P00-002 Define State Model
3. P00-003 Define Public Projection Contract
4. P00-004 Choose Minimal Server Stack
5. P00-005 Define Test Strategy
6. P00-006 Define Local Persistence Strategy
7. Phase 1 skeleton tickets
8. Phase 2 scene tickets
9. Phase 3 tracker tickets
10. Phase 4 initiative tickets
11. Local save/load implementation before MVP completion

## Safety Boundary

Player-facing routes and payloads must consume public projection output only. Tickets that add or change player-visible data should depend on the relevant model ticket and public projection ticket.
