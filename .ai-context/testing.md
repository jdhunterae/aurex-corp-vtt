# Testing Context

Purpose: give AI agents a concise testing checklist before changing behavior.

## Test Command

Run the full suite with:

```bash
.venv/bin/python -m pytest
```

Pytest is configured in `pyproject.toml` with `testpaths = ["tests"]`.

## Current Test Stack

- Test runner: pytest.
- Route tests: Flask test client.
- Test fixture isolation: `tests/conftest.py` redirects `app.state.DATA_DIR` and `SESSIONS_DIR` to a temporary directory and clears in-memory sessions.

## Current Test Areas

- `test_routes.py`: GM/player route smoke tests, redirects, health, 404, public payload safety.
- `test_projection.py`: public projection safety and initiative visibility basics.
- `test_scene_controls.py`: scene update validation.
- `test_scene_display.py`: player scene rendering.
- `test_asset_ingestion.py`: upload, URL download, duplicate detection, asset serving.
- `test_tracker_projection.py`: tracker projection behavior and hidden tracker handling.
- `test_tracker_controls.py`: tracker JSON/form controls and validation.
- `test_tracker_display.py`: player tracker rendering safety.

## Testing Expectations

- Add or update tests for every behavior change.
- Every feature that changes player-visible state should test that private fields do not leak.
- Prefer focused tests by behavior rather than broad page snapshots.
- Use pure Python state fixtures for projection logic where possible.
- Use Flask test client for route/API behavior.
- Autosave assertions are pending until persistence exists.

## Safety Regression Checklist

Player-facing responses and rendered player HTML must not expose:

- GM notes.
- Local filesystem paths.
- Original image URLs.
- GM keys or tokens.
- Hidden trackers.
- Hidden combatants.
- Hidden AC or HP.
- Private save metadata.

TODO: Add `test_player_refresh.py` when implementing `P03-005`.
TODO: Add initiative and persistence test modules when Phase 4 work begins.
