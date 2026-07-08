# Coding Style Context

Purpose: capture current implementation style and coding constraints for AI agents changing application code.

## Python Style

- Use boring, readable Python.
- Prefer standard library features where practical.
- Keep route handlers small and delegate validation/state logic to helper modules.
- Use explicit validation functions and custom `ValueError` subclasses for domain validation.
- Use dict-based state for the current MVP; do not introduce a database unless explicitly approved.
- Keep module organization simple until the project clearly needs more structure.
- Use type hints where the existing code uses them, especially `dict[str, Any]`.

## Flask Style

- Use `create_app()` as the app factory.
- Use Flask test client for route tests.
- Form routes redirect back to GM pages on success and re-render with HTTP 400 plus visible error on validation failure.
- JSON mutation endpoints return simple JSON payloads and currently include `"autosaved": false`.
- JSON error responses use:

```json
{
  "error": {
    "code": "invalid_tracker_update",
    "message": "Human-readable message."
  }
}
```

## State And Projection

- Backend owns canonical full session state.
- Player-facing code must use `project_public_state()` or another explicit public projection function.
- Do not pass full session state to player templates, player JavaScript, or player JSON.
- When adding player-visible fields, update projection tests.

## Dependencies And Tooling

- Runtime dependencies are in `requirements.txt`.
- Current dependencies: Flask and pytest.
- `pyproject.toml` contains project metadata and pytest test discovery.
- Do not add package managers, build tools, async workers, WebSockets, authentication, or databases without explicit approval.

## File Boundaries

- Stable docs live in `docs/`.
- AI scratch/audit material lives in `.brainstorming/`.
- Local project tickets live in `.project-board/pNN/`.
- Stable AI-agent guidance lives in `.ai-context/`.
- Runtime data lives in `data/` and must not be committed.

TODO: Decide whether to add formatting/linting tools later. None are configured now.
TODO: Decide whether to migrate dependencies into `pyproject.toml` later. The current workflow keeps them in `requirements.txt`.
