# P01-001 Add Server Entrypoint

## Status

Ready

## Phase

Phase 1 - Application Skeleton

## Goal

Create a Python application entrypoint that starts the local server successfully.

## Acceptance Criteria

- [ ] Flask is added as the minimal runtime dependency.
- [ ] Server starts with a documented local command.
- [ ] App uses a small app factory or equivalent testable creation function.
- [ ] Root route redirects to `/gm` or returns the local GM home page.
- [ ] Health route confirms the app is running.
- [ ] Server code remains small and readable.
- [ ] No database, async worker, authentication system, or build tool is introduced.
- [ ] Development data paths are not created at import time unless explicitly initialized by app startup.

## Notes

Depends on P00-004.

Suggested implementation files:

- `app/server.py`
- `app/__init__.py`

Suggested command:

```text
flask --app app.server run --debug
```

If a different command is chosen during implementation, update `README.md` or a developer setup doc in the same change.
