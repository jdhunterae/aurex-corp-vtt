# P03-003 Add Tracker GM Controls

## Status

Done

## Phase

Phase 3 - Generic Trackers

## Goal

Allow the GM to create and update reusable trackers through server-side routes and JSON APIs.

## Acceptance Criteria

- [x] GM can create a tracker.
- [x] GM can update tracker value and label.
- [x] GM can choose bounded or unbounded tracker mode.
- [x] GM can define optional named values for a tracker.
- [x] GM can define interval mapping for named tracker states.
- [x] GM can choose a default color scale for label_color display.
- [x] GM controls always include default -1 and +1 buttons.
- [x] GM controls support interval-derived or GM-configured larger step buttons.
- [x] GM can choose whether players see raw numbers, mapped text/color, or another documented display mode.
- [x] GM can change tracker visibility.
- [x] Invalid tracker updates are rejected server-side.
- [x] Successful JSON mutations return `autosaved: false` until local persistence is implemented.
- [x] Form routes follow the current Phase 2 pattern of re-rendering the GM session page with a clear error on validation failure.
- [x] Tracker update behavior is covered by tests.

## Notes

Depends on P03-002.

Use the current scene and asset patterns in `app/server.py` and `app/templates/gm_session.html` as the baseline. Phase 3 should not introduce a frontend framework, database, authentication layer, WebSockets, or persistence.

Autosave is still planned for P04-004. Do not make tracker controls claim autosave succeeded until persistence exists.

Completed in `app/trackers.py`, `app/server.py`, and `app/templates/gm_session.html` with coverage in `tests/test_tracker_controls.py`.

Follow-up: the current controls satisfy the functional route/API requirements, but the GM page layout remains too live-entry oriented. `P03-006 Redesign GM Control Layout` tracks the prep-first control surface work.
