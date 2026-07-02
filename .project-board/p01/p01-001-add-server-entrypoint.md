# P01-001 Add Server Entrypoint

## Status

Done

## Phase

Phase 1 - Application Skeleton

## Goal

Create a Python application entrypoint that starts the local server successfully.

## Acceptance Criteria

- [x] Flask is added as the minimal runtime dependency.
- [x] Server starts with a documented local command.
- [x] App uses a small app factory or equivalent testable creation function.
- [x] Root route redirects to `/gm` or returns the local GM home page.
- [x] Health route confirms the app is running.
- [x] Server code remains small and readable.
- [x] No database, async worker, authentication system, or build tool is introduced.
- [x] Development data paths are not created at import time unless explicitly initialized by app startup.

## Notes

Depends on P00-004.

Suggested implementation files:

- `app/server.py`
- `app/__init__.py`

Current command:

```text
.venv/bin/flask --app app.server run --debug
```

If a different command is chosen during implementation, update `README.md` or a developer setup doc in the same change.

Completed in `app/server.py`, `app/__init__.py`, `requirements.txt`, and `README.md`.
