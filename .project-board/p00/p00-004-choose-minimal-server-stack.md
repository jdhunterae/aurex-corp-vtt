# P00-004 Choose Minimal Server Stack

## Status

Done

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Choose the minimal Python server approach for the local server MVP.

## Acceptance Criteria

- [x] The selected server library or standard-library approach is documented.
- [x] Any dependency addition is justified before implementation.
- [x] Startup command and development workflow are documented.
- [x] The choice supports templates, static assets, JSON routes, and unit tests.
- [x] The choice does not require handing canonical game state management to a framework ORM or database layer.

## Notes

Decision: use Flask as a minimal wrapper for routes, templates, static files, JSON endpoints, upload handling, and tests. Flask should not own canonical game state.

Current commands are documented in `README.md`:

```text
.venv/bin/python -m pytest
.venv/bin/flask --app app.server run --debug
```
