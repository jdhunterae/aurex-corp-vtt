# UI Conventions Context

Purpose: summarize practical UI rules for future AI sessions working on templates, CSS, or JavaScript.

## Overall UI Direction

- Keep the UI simple, local-first, and easy to run without a frontend build step.
- Use Jinja templates, static CSS, and small JavaScript files.
- Do not introduce frontend frameworks unless explicitly approved.
- GM UI should prioritize practical control speed over decoration.
- Player UI should be readable from across a room.

## Player UI

- Player pages are passive/read-only.
- Player pages render public scene title, description, optional app-managed image, and public trackers.
- Player JavaScript may fetch only public projection endpoints such as `/api/s/<session_id>/public`.
- Player JavaScript must update the display from public projection payloads only.
- Player pages must not load GM-only JavaScript, call GM APIs, or embed full session state in HTML.
- Empty public tracker state should not create distracting placeholder UI.
- If player auto-refresh polling fails, keep the current display visible and non-interrupted.
- Show a temporary popup/popdown indicator that the display may be out of date.
- The failure indicator should include a countdown until the next attempted update.

## GM UI

- Current GM page uses stacked panels and forms for scene, assets, and trackers.
- Current tracker controls are functional but still too live-entry oriented.
- Target workflow is prep-first: prepare scenes/assets/trackers before play, then use compact controls during the session.
- Common live actions should become one or two clicks where practical.
- Less common setup/edit actions can live in larger forms or secondary sections.

## JavaScript

- `app/static/gm-session.js` is GM-only and currently handles duplicate asset preview warnings.
- Shared JavaScript should be treated as player-safe by default.
- If JavaScript needs GM data or GM endpoints, keep it in a GM-only file and load it only from GM templates.

## Styling

- Current CSS uses simple panels, forms, grids, and player tracker cards.
- Keep CSS readable and framework-free.
- Current project uses 8px or smaller border radii.
- Avoid decorative complexity that makes the app feel larger than the MVP.

TODO: Decide the final GM control layout for `P03-006`.
TODO: Decide whether prepared scene library UI should be a separate panel, tabbed section, or compact selector.
TODO: Decide polling interval for `P03-005` player auto-refresh.
