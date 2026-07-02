# UI Concepts

The application has two interfaces.

Current implementation status:

- The player interface currently renders the public scene image, title, and description.
- The GM interface currently manages scene title, scene description, image asset selection by ID, image upload, image URL download, and duplicate asset handling.
- Public trackers, initiative controls, notes, quick actions, and persistence controls are planned for later phases.

## Player

Goals

- Clean
- Readable from across a room
- Minimal distractions

Primary regions

- Scene: implemented for Phase 2.
- Public trackers: planned for Phase 3.
- Initiative: planned for Phase 4.

---

## GM

Primary regions

Scene controls: implemented for Phase 2.

Tracker controls: planned for Phase 3.

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
