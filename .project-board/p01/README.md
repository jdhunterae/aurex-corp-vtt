# Phase 1 - Application Skeleton

Phase 1 creates the smallest runnable Flask application that serves GM and player page shells and exposes a safe public projection endpoint.

Do not implement Phase 2-4 features in Phase 1 except as empty/default state needed to support the skeleton.

## Dependency Order

1. `P01-001 Add Server Entrypoint`
2. `P01-002 Add GM and Player Pages`
3. `P01-003 Add Shared State Module`
4. `P01-004 Add Public State Projection`
5. `P01-005 Add Basic Route Tests`

## Implementation Notes

- Use Flask as the minimal server wrapper.
- Keep canonical state in app-owned Python modules.
- Bootstrap project-local session data under `data/sessions/` for MVP development.
- Player routes must consume public projection output only.
- Do not introduce a database, authentication system, async worker, frontend framework, or build tool.

## Phase 1 Completion Criteria

- Local server starts with the documented command.
- GM page shell is available.
- Player page shell is available.
- Public polling endpoint at `/api/s/<session_id>/public` returns player-safe state.
- Basic route and projection tests pass with `.venv/bin/python -m pytest`.
- No GM-only fields are exposed through player routes, public JSON, static files, or client JavaScript.
