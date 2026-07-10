# P03-008 Retain Scroll Position After Updates

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Keep the GM and player displays from unexpectedly losing their scroll position after updates or refreshes.

## Acceptance Criteria

- [ ] After a GM scene, asset, or tracker form submission, the GM page returns to the relevant area instead of always landing at the top of the page.
- [ ] Repeated tracker updates do not require the GM to scroll back down to the tracker controls after every action.
- [ ] The scene update panel remains usable with or without a separate success notification.
- [ ] Player auto-refresh preserves the current player display scroll position where practical.
- [ ] The solution remains simple HTML/CSS/JavaScript with no frontend framework.
- [ ] Validation errors still bring the GM to the relevant error context.
- [ ] Behavior is covered by focused route/template or frontend tests where practical.

## Notes

Observed during Phase 3 usage: GM form submissions currently perform a full page update and return the browser to the top of the GM page. This is hard to notice for the scene update area because that panel is already at the top, but it is disruptive for tracker controls lower on the page.

This is related to, but separate from, `P03-007 Add GM Action Feedback`. `P03-007` captures the need for explicit scene update confirmation. This ticket captures the broader scroll-position and workflow continuity problem.
