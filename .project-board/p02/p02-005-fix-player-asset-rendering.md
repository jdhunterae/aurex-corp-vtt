# P02-005 Fix Player Asset Rendering

## Status

Done

## Phase

Phase 2 - Scene Display

## Goal

Fix the player display broken-image behavior for app-managed scene assets.

## Acceptance Criteria

- [x] App-managed image assets served through `/assets/<session_id>/<asset_filename>` load successfully in the player view.
- [x] Asset serving works with the default project-local `data/sessions/` runtime path.
- [x] Asset serving does not expose arbitrary local file paths.
- [x] Asset serving still strips path components from requested filenames.
- [x] Route or integration tests cover the default relative runtime data path, not only test-time absolute paths.

## Notes

Observed during Phase 3 GM tracker UI smoke testing: the player page requested an app-managed asset URL and received a 404 even though the file existed under `data/sessions/default/assets/`.

Likely cause: relative asset directories passed to Flask asset serving can resolve differently than the repository-level runtime data path. Serve app-managed assets from a resolved session asset directory.

Completed in `app/server.py` with regression coverage in `tests/test_asset_ingestion.py`.
