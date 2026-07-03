# Testing Strategy

## Purpose

The MVP should be covered by focused tests around state projection, validation, routes, and persistence.

The most important regression class is accidental leakage of GM-only state to player-facing routes.

## Test Tooling

Use `pytest` for MVP tests.

Use Flask's test client for route tests.

Current command:

```text
.venv/bin/python -m pytest
```

The project currently uses `pytest` and Flask's test client. Dependencies are listed in `requirements.txt`.

Current coverage includes:

- Route smoke tests for GM, player, health, redirects, and 404 handling.
- Public projection tests for session, scene, tracker, and initiative visibility behavior.
- Scene update validation tests.
- Scene display rendering tests.
- Asset upload, URL download, duplicate detection, and asset-serving tests.

## Test Layout

Current layout:

```text
tests/
  test_projection.py
  test_routes.py
  test_scene_controls.py
  test_scene_display.py
  test_asset_ingestion.py
  test_tracker_controls.py
  test_tracker_display.py
  test_tracker_projection.py
```

Future player auto-refresh, initiative, and persistence work should add focused test modules, such as `test_player_refresh.py`, `test_initiative.py`, and `test_persistence.py`, as those features are implemented. Tests should stay grouped by behavior rather than by UI page.

## Projection Tests

Projection tests should use pure Python state fixtures where possible.

Cover:

- Player projection excludes GM notes.
- Player projection excludes local paths.
- Player projection excludes original image URLs.
- Player projection includes asset ID and resolved app URL.
- Hidden trackers are omitted.
- Interval-mapped trackers hide raw numeric progress unless configured to show it.
- Hidden initiative returns no initiative panel.
- Hidden initiative entries are omitted.
- Visible initiative entries show `???` for hidden data.
- Known initiative entries expose only discovered AC and HP.
- Non-creature initiative rows expose only title/name and initiative slot number plus rendering fields.

## Validation Tests

Validation tests should cover:

- Session IDs and object IDs are unique within a session.
- Scene image references point to app-managed assets in the same session.
- Asset formats are accepted only when supported.
- URL downloads validate the final response as an image.
- Bounded tracker values stay within bounds.
- Tracker interval and named values are coherent.
- Initiative visibility values are valid.
- HP values are non-negative and do not exceed max HP.
- Save files include supported schema metadata.

## Route Tests

Use Flask's test client.

Cover:

- GM pages return successfully.
- Player page returns successfully without embedding full state.
- Bare session page redirects to the safer player view.
- Public polling endpoint returns only projected state.
- GM state-changing endpoints validate input.
- GM state-changing endpoints trigger autosave.
- Asset upload/download routes create app-managed asset records.
- Scene update routes reject local paths and external URLs as direct scene image references.

Autosave assertions are pending until local persistence is implemented.

## Persistence Tests

Cover:

- Active session state can be saved and loaded.
- Autosave writes the latest state to slot 1.
- Autosave warm-up fills empty slots.
- Autosave rotation preserves older restore points according to age windows.
- Manual saves are named, timestamped, and separate from autosaves.
- Manual save copy versus replace behavior works.
- Loading any save requires explicit GM confirmation.
- Corrupt saves return clear errors and viable timestamped alternatives when possible.

## Safety Regression Tests

Every phase that adds player-visible data should add or update tests proving that private fields are not present in player payloads.

Fields that must never appear in player responses include:

- GM notes
- Local filesystem paths
- Original image URLs
- GM keys or tokens
- Hidden trackers
- Hidden combatants
- Hidden AC
- Hidden HP
- Private save metadata
