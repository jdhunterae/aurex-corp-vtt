# P03-003 Add Tracker GM Controls

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Allow the GM to create and update reusable trackers through server-side routes and JSON APIs.

## Acceptance Criteria

- [ ] GM can create a tracker.
- [ ] GM can update tracker value and label.
- [ ] GM can choose bounded or unbounded tracker mode.
- [ ] GM can define optional named values for a tracker.
- [ ] GM can define interval mapping for named tracker states.
- [ ] GM can choose a default color scale for label_color display.
- [ ] GM controls always include default -1 and +1 buttons.
- [ ] GM controls support interval-derived or GM-configured larger step buttons.
- [ ] GM can choose whether players see raw numbers, mapped text/color, or another documented display mode.
- [ ] GM can change tracker visibility.
- [ ] Invalid tracker updates are rejected server-side.
- [ ] Successful JSON mutations return `autosaved: false` until local persistence is implemented.
- [ ] Form routes follow the current Phase 2 pattern of re-rendering the GM session page with a clear error on validation failure.
- [ ] Tracker update behavior is covered by tests.

## Notes

Depends on P03-002.

Use the current scene and asset patterns in `app/server.py` and `app/templates/gm_session.html` as the baseline. Phase 3 should not introduce a frontend framework, database, authentication layer, WebSockets, or persistence.

Autosave is still planned for P04-004. Do not make tracker controls claim autosave succeeded until persistence exists.
