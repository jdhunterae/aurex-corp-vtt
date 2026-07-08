# UI Concepts

The application has two interfaces.

Current implementation status:

- The player interface currently renders the public scene image, title, description, and public trackers.
- The GM interface currently manages scene title, scene description, image asset selection by ID, image upload, image URL download, duplicate asset handling, and tracker controls.
- Automatic player refresh, initiative controls, notes, quick actions, and persistence controls are planned for later phases.
- The current GM controls are still too live-entry oriented. The target workflow is prep-first: build scenes, assets, and trackers before play, then use compact controls to change what players see during the session.

## Player

Goals

- Clean
- Readable from across a room
- Minimal distractions
- Updates automatically after GM public-state changes

Primary regions

- Scene: implemented for Phase 2.
- Public trackers: implemented for Phase 3.
- Initiative: planned for Phase 4.

Frontend safety conventions:

- Player JavaScript may fetch only public projection endpoints such as `/api/s/<session_id>/public`.
- Player JavaScript must update the display from public projection payloads only.
- Player pages must not load GM-only JavaScript, call GM APIs, or embed full session state in HTML.
- Player-facing JavaScript must never receive hidden scenes, hidden trackers, GM notes, local paths, original asset source URLs, save metadata, GM keys, or other private state.

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

Current tracker controls support:

- Creating generic numeric trackers rather than specialized tracker types.
- Editing label, value, visibility, bounds, interval, display mode, color scale, and named values.
- Quick adjustment buttons that always include `-1` and `+1`.
- Larger adjustment buttons derived from the tracker interval or explicit `step_controls`.
- Clear validation errors on the GM session page.

Remaining Phase 3 workflow gaps:

- Player auto-refresh after GM public-state changes.
- A more compact GM layout that separates setup/editing from live controls.
- A prepared scene library so scene switching does not require live retyping.

Initiative controls: planned for Phase 4.

Notes: planned.

Quick actions: planned.

Frontend safety conventions:

- GM JavaScript may call GM routes and GM JSON APIs when needed for controls and previews.
- GM-only JavaScript must be loaded only by GM pages.
- Shared JavaScript should be treated as player-safe by default; if it needs GM data or GM endpoints, keep it in a GM-only file.

---

The GM interface prioritizes speed over appearance.

Every common action should be accomplishable with one or two clicks.

Setup workflows and live control workflows should be distinct. The GM should not have to use large setup forms for common in-session actions.

Live controls should update the player display without asking the player to refresh. A GM action is incomplete from a UX perspective until the public display reflects it automatically.
