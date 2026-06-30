# MVP Clarifications TODO

This is a rolling, non-binding working document for open questions that need clarification before implementation tickets become ready.

## Current Context

- Planning branch: `p00-project-board-planning`
- Current planning commit: `4a304d9 p00: add MVP planning tickets`
- MVP boundary: local-network MVP is complete after Phase 4, including scene display, generic trackers, initiative tracker, local image ingestion, and local save/load.
- Post-MVP: hosting beyond the local network and broader player session connection features.

## Critical Decisions

### Server Stack

Status: Resolved

Question: Should the MVP use Flask, Django, or standard-library HTTP tooling?

Decision: Use Flask as a minimal wrapper for routes, templates, static files, JSON endpoints, upload handling, and tests.

Constraint: Flask should not own the game data model. The app should keep explicit backend state and persistence modules.

### State And Session Scope

Status: Resolved

Question: Does the MVP manage exactly one active local session at a time, or multiple local campaigns/saves selectable inside the app?

Decision: Support foldered sessions for MVP so different prep contexts can have different maps, trackers, initiative state, and saves.

Implementation implication: The app needs an app-managed sessions directory, session selection, and per-session assets/save data.

### Persistence Behavior

Status: Resolved

Question: How should local save/load work for error recovery?

Decision: Autosave after every GM action and also support manual export/saves for intentional restore points.

Decision: For immediate MVP, session data can live in a local `data/` directory inside the project. Long-term goal is to move user data outside the app directory.

Decision: Keep a rolling set of 3 autosaves per session.

Decision: Save files should use JSON with schema/version metadata.

Decision: Manual saves are GM-named and timestamped. Manual saves are stored in the session data folder and do not affect autosaves.

Decision: Manual save should ask whether to replace the last manual save or save as a copy. Replacing deletes or supersedes the previous timestamped manual save. Saving as a copy preserves previous manual saves.

Decision: Export is separate from manual save and should allow the GM to name/save a file outside the session folder, such as Downloads, where browser/server constraints allow it.

Decision: If a save is corrupt, notify the GM and offer load options instead of silently replacing state. Options should include viable autosaves and manual saves, with timestamps compared so the GM can choose the best restore point.

Autosave behavior:

- Autosave 1 is the most recent change.
- Autosave 2 should represent a recent prior point, roughly 5-10 minutes old.
- Autosave 3 should represent an older prior point, roughly 10-30 minutes old.
- Before overwriting the active autosave, the app should consider whether older slots should be rotated forward based on age and whether the save content differs.
- During startup/warm-up, empty autosave slots should be populated from prior slot contents even if they are recent, then naturally drift toward target age windows as play continues.

Decision: MVP export should use browser download. App-configured server-side export directories can be added later.

### Public Projection Contract

Status: Resolved

Question: What exact public JSON should the player display receive?

Decisions:

- Player-facing asset payloads should include both app-managed asset ID and resolved app URL.
- Public payload fields are defined in `docs/api.md` and `docs/state-model.md`.

Hard rule: player payloads must never include hidden GM notes, private counters, unrevealed monsters, secret data, keys, tokens, local source paths, or original image source URLs.

### Asset Storage

Status: Resolved

Question: How should imported/uploaded/downloaded scene images be stored and exposed?

Decisions:

- MVP assets live under each foldered session, at `data/sessions/<session_id>/assets/`.
- Allowed image formats for GM-selected assets: jpg/jpeg, tiff, png, gif, webp, and svg.
- The intent is to allow common web-displayable image files at GM discretion.
- Original URL source metadata should be stored privately in GM/session data.
- Downloaded URL assets should be local resources so the app does not redownload the same image every time it is shown.
- No explicit image file size limit is required for the local-only MVP.
- Asset filenames should be generated internally as stable IDs, such as `asset-<uuid>.<ext>`.
- GM-facing display names should be stored separately from filenames.
- Duplicate image handling should warn the GM when an image appears to match an existing asset.
- On duplicate detection, the GM should choose whether both locations share the existing asset or keep a separate copy.
- URL downloads may follow normal redirects up to a small redirect limit.
- The final URL response must still validate as an allowed image type.

Current leaning: copy/download assets into an app-managed local asset folder and expose only server-generated public asset references.

## Feature Behavior Questions

### Scene Updates

Status: Resolved

Question: Should player screens update automatically, or is manual refresh acceptable for the first MVP?

Decision: Player display should auto-update using polling for MVP. Players should not need to manually refresh during play.

### Generic Trackers

Status: Partially resolved

Questions:

- Do trackers need min/max values?
- Do trackers need step size?
- Do trackers need reset value?
- Do trackers need ordering?
- Do trackers need visibility toggles?
- Should tracker values support only numbers, or also text labels/states?

Decisions:

- Trackers are usually numeric values on a scale.
- Trackers can be bounded or unbounded.
- Bounded examples: alert levels 1-5, magic item uses 0-3.
- Unbounded example: items found, 0 to infinity.
- Numeric values may map to named display states.
- A tracker can keep plain numeric display or define a list of named values.
- Trackers may use intervals so multiple numeric values map to one named display state.
- Example: security alert level has named states Green, Yellow, Orange, Red, Black. With interval 3, values 1-3 map to Green, 4-6 map to Yellow, and so on.
- GM chooses player display mode per tracker.
- Player display can hide raw numeric values and show only mapped text/color values.
- For interval-mapped trackers, the player display should not reveal hidden progress within the interval unless the GM chooses to expose it.

Decisions:

- Tracker GM controls should always include default `-1` and `+1` buttons.
- Interval-mapped trackers should also support larger step buttons based on `ceil(interval / 2)` where practical. Example: interval 3 gives `-2`, `-1`, tracker, `+1`, `+2`.
- If easier or clearer, the GM may explicitly configure extra step controls.
- MVP tracker display mode names:
  - `number`
  - `label`
  - `label_color`
  - `number_label`
- Tracker color scales should support defaults and later custom colors.
- Default color scale options should include green-to-red, red-to-green, black-to-white, and white-to-black.
- Custom color picker per state is a stretch goal.

### Initiative

Status: Partially resolved

Questions:

- Are hidden monsters absent from player initiative, or shown as hidden placeholders?
- Does the GM manually control turn order ties?
- What combatant fields are visible to players?
- Should non-combat public rows such as lair actions be supported in MVP?

Decisions:

- Initiative has an overall hidden toggle because the table is not always in combat.
- When initiative is active, each character/combatant needs its own show/hide control.
- Per-combatant player visibility has three states:
  - `hidden`: no row is shown.
  - `visible`: row is shown with `???` replacing hidden data except initiative slot/speed.
  - `known`: name and discovered information are shown.
- Enemy AC should be hidden by default and revealable once discovered.
- Enemy HP/health visibility should be configurable.
- HP visibility modes:
  - `none`: show no injury indication.
  - `vibe`: show rough health status.
  - `numbers`: show discovered health numbers according to global GM configuration.
- HP number display style should be a global GM configuration, defaulting to current/max such as `20/56`.
- Vibe health bands:
  - healthy: 70% or higher.
  - injured: 50% to 70%.
  - seriously injured/bloodied: below 50%.
- When the overall initiative display is hidden, the player UI should show no initiative panel, blank space, or placeholder.

Decisions:

- AC reveal is per combatant. MVP does not need global enemy-type AC reveal behavior.
- Initiative should support non-creature rows such as lair actions, environmental effects, pets, companions, vehicles, and similar turn-order entries.
- Public non-creature rows should show only title/name and initiative slot number, plus technical rendering fields such as ID, kind, and current-turn status.
- Duplicate initiative values sort by initiative descending, then manual `sort_order`.

### Save Load

Status: Partially resolved

Questions:

- Should autosave happen after every GM action?
- Should manual save create named save files?
- Should load replace current state immediately or require confirmation?
- Should the app keep backup save files?

Decisions:

- Autosave happens after every GM action.
- Manual save/export is required for intentional rewind points.
- MVP keeps 3 rolling autosaves per session.
- Immediate MVP can store data under project-local `data/`.
- Manual saves are GM-named, timestamped, and separate from autosaves.
- Export is a separate workflow from in-session manual save.
- Saves use JSON with schema/version metadata.
- Corrupt saves notify the GM and offer timestamped autosave/manual save options to attempt loading.

Decisions:

- Loading any manual save or autosave should always require GM confirmation before replacing active state.
- MVP export should use browser download. App-configured server-side export directories can be added later.

### URL Image Download

Status: Partially resolved

Questions:

- Should URL download happen immediately when submitted?
- Should the app support preview before committing the image?
- Should redirects be allowed?
- Should only image MIME types be accepted?
- Should remote source URL be stored privately, discarded, or optional?

Decisions:

- URL image import should download immediately when the GM submits/pastes the URL so showing the scene later does not block on resource download.
- SVG is allowed at GM discretion for MVP because the local tool is currently GM-only.
- URL downloads may follow normal redirects up to a small redirect limit.
- The final URL response must still validate as an allowed image type.

## Tickets Needing Expansion

- `P00-002 Define State Model`
- `P00-003 Define Public Projection Contract`
- `P00-006 Define Local Persistence Strategy`
- `P02-004 Add Scene Asset Ingestion`
- `P03-001 Define Generic Tracker Model`
- `P04-001 Define Initiative Model`

## Resolved Decisions

- MVP ends after Phase 4.
- Local save/load is required for MVP completion.
- Scene images can come from local import/upload or URL download.
- The app should own its backend game data model rather than relying on Django ORM/database update behavior.
- Flask is approved as the minimal server wrapper.
- MVP should support foldered sessions.
- Autosave after every GM action and manual saves/exports are both required.
- Player display should auto-update through polling.
- Immediate MVP data may live in a project-local `data/` directory.
- Autosave should keep 3 rolling restore points per session.
- Trackers support numeric scales with optional named value mapping and intervals.
- Initiative supports global visibility, per-combatant visibility, AC reveal, and HP visibility modes.
- Manual saves are GM-named, timestamped, and separate from autosaves.
- Export is a separate workflow from in-session manual save.
- Saves use JSON with schema/version metadata.
- Initiative combatant visibility states are hidden, visible, and known.
- Corrupt saves notify the GM and offer timestamped restore options.
- Trackers can be bounded or unbounded and can hide raw numeric progress from players.
- Initiative HP number display defaults to current/max, such as `20/56`.
- Hidden initiative display leaves no player-facing panel or placeholder.
- Allowed image asset formats: jpg/jpeg, tiff, png, gif, webp, svg.
- Tracker controls include default +/-1 and may include interval-derived or GM-configured larger step buttons.
- Tracker display modes: number, label, label_color, number_label.
- AC reveal is per combatant.
- URL image import downloads immediately.
- SVG is allowed at GM discretion for MVP.
- Player asset payloads include both app-managed asset ID and resolved app URL.
- Original image URL metadata is stored privately in GM/session data.
- Downloaded URL assets are stored locally and reused.
- Tracker default color scales include green-to-red, red-to-green, black-to-white, and white-to-black.
- Initiative supports non-creature rows such as lair actions, environmental effects, pets, companions, and vehicles.
- Loading a save always requires GM confirmation before replacing active state.
- No explicit image file size limit is required for the local-only MVP.
- Duplicate image handling warns the GM and offers reuse/share versus separate copy.
- Public non-creature initiative rows show only title/name and initiative slot number.
- Asset filenames use generated stable IDs, with GM display names stored separately.
- URL downloads may follow limited redirects and must validate final image type.
- MVP export uses browser download.
- Custom tracker color picker is a stretch goal.
- Duplicate initiative values sort by initiative descending, then manual sort order.
