# P03-007 Add GM Action Feedback

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Give the GM clear temporary feedback when the scene update action succeeds.

## Acceptance Criteria

- [ ] Clicking `Update Scene` gives the GM a temporary confirmation that the update was submitted and applied.
- [ ] The confirmation is visible on the GM page without requiring the GM to infer success from unchanged form fields.
- [ ] The feedback pattern can be reused later for other GM actions if needed.
- [ ] The feedback remains simple HTML/CSS/JavaScript with no frontend framework.
- [ ] Validation errors remain distinct from success confirmations.
- [ ] Player-facing routes and payloads remain unchanged.
- [ ] The behavior is covered by focused route/template or frontend tests where practical.

## Notes

Observed during Phase 3 usage: after the GM clicks `Update Scene`, the GM screen often looks unchanged because the scene panel is already at the top of the page. A temporary confirmation would make it clear that the action went through.

Related but separate issue: full-page GM form submissions scroll back to the top of the page, which is especially painful for tracker updates. That scroll retention problem is tracked by `P03-008 Retain Scroll Position After Updates`.
