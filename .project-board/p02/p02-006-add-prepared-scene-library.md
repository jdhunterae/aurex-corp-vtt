# P02-006 Add Prepared Scene Library

## Status

Backlog

## Phase

Phase 2 - Scene Display

## Goal

Allow the GM to prepare multiple scenes before play, then switch the active public scene during the session.

## Acceptance Criteria

- [ ] GM can create more than one scene in a session.
- [ ] GM can edit a prepared scene's title, description, and image asset.
- [ ] GM can select which prepared scene is currently active on the player display.
- [ ] The GM page shows a list of prepared scenes.
- [ ] Scene switching is a control action, not a requirement to retype scene content live.
- [ ] Player routes receive only the active public scene projection.
- [ ] Hidden/private scene fields and GM notes are not exposed to players.
- [ ] Scene create/edit/select behavior is covered by tests.

## Notes

The original Phase 2 scene controls behave like a live-entry form for a single active scene. That is not the intended table workflow.

The intended GM workflow is prep-first:

- Load or import assets before the game.
- Create a list of prepared scenes.
- Attach assets and descriptions to those scenes.
- During play, switch the active scene from the GM control panel.
- Edit or add a scene only when needed.

This ticket should replace the single implicit `scene-active` workflow with an explicit prepared scene list while preserving the public projection safety boundary.
