# UI Concepts

The application has two interfaces.

Current implementation status:

- The player interface currently renders the public scene image, title, and description.
- The GM interface currently manages scene title, scene description, image asset selection by ID, image upload, image URL download, duplicate asset handling, and tracker controls.
- Public tracker rendering, automatic player refresh, initiative controls, notes, quick actions, and persistence controls are planned for later phases.
- The current GM controls are still too live-entry oriented. The target workflow is prep-first: build scenes, assets, and trackers before play, then use compact controls to change what players see during the session.

## Player

Goals

- Clean
- Readable from across a room
- Minimal distractions
- Updates automatically after GM public-state changes

Primary regions

- Scene: implemented for Phase 2.
- Public trackers: planned for Phase 3.
- Initiative: planned for Phase 4.

---

## GM

Primary regions

Scene controls: implemented for Phase 2.

Scene controls should evolve from a single live-entry form into a prepared scene library:

- Create and edit prepared scenes before play.
- Attach app-managed image assets to scenes.
- Select the active public scene during play.
- Avoid retyping scene title, description, or image IDs as the normal live workflow.

Tracker controls: implemented for Phase 3.

Phase 3 tracker controls should support:

- Creating generic numeric trackers rather than specialized tracker types.
- Editing label, value, visibility, bounds, interval, display mode, color scale, and named values.
- Quick adjustment buttons that always include `-1` and `+1`.
- Larger adjustment buttons derived from the tracker interval or explicit `step_controls`.
- Clear validation errors on the GM session page.

Initiative controls: planned for Phase 4.

Notes: planned.

Quick actions: planned.

---

The GM interface prioritizes speed over appearance.

Every common action should be accomplishable with one or two clicks.

Setup workflows and live control workflows should be distinct. The GM should not have to use large setup forms for common in-session actions.

Live controls should update the player display without asking the player to refresh. A GM action is incomplete from a UX perspective until the public display reflects it automatically.
