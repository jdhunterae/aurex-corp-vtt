# P03-006 Redesign GM Control Layout

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Rework the GM session page from stacked live-entry forms into a practical control surface for prepared session elements.

## Acceptance Criteria

- [ ] GM page layout supports fast scanning during play.
- [ ] GM controls distinguish setup/editing workflows from live control workflows.
- [ ] Scene controls, asset controls, and tracker controls are visually grouped without becoming one long stack of forms.
- [ ] Common live actions are available with one or two clicks.
- [ ] Less common setup/edit actions can be tucked into edit forms or secondary sections.
- [ ] Tracker adjustment controls are compact and usable during play.
- [ ] The layout remains simple HTML/CSS with no frontend framework.
- [ ] The GM page remains usable on common laptop screen sizes.

## Notes

Depends on P03-005.

Current Phase 3 tracker controls technically support creating and updating trackers, but the UI is still a live-entry form stack. That is not the intended session-control experience.

The GM should be able to prepare scenes, assets, and trackers before a session, then use the GM page to control which prepared elements are public during play.

Do not treat visual polish as a substitute for control behavior. Live GM controls must update the player display automatically through the public-state update flow.
