# State Model

## Purpose

This document defines the canonical backend state shape for the local server MVP.

The backend owns the full state. GM routes may read and update this full state through server-side APIs. Player routes must never receive the full state directly. Player routes receive only the explicit public projection described in this document.

The MVP should remain file-backed and small enough to run without a database.

## Safety Boundary

Full session state may contain private GM data, source URLs, local asset paths, hidden combatants, undiscovered stats, and save metadata.

Player-facing state must never include:

- GM notes
- Private counters or hidden trackers
- Unrevealed combatants
- Secret data
- GM keys or tokens
- Local filesystem paths
- Original image source URLs
- Private save metadata
- Hidden AC or HP values

When in doubt, add a field to full state and explicitly omit it from the public projection.

## Storage Layout

Immediate MVP storage can live under a project-local `data/` directory.

Long term, user data should move outside the app directory.

Suggested MVP layout:

```text
data/
  sessions/
    <session_id>/
      session.json
      assets/
        <asset_id>.<ext>
      autosaves/
        autosave-1.json
        autosave-2.json
        autosave-3.json
      saves/
        <timestamp>-<gm-name>.json
```

The exact file names can change during implementation, but the state model assumes:

- Each session has its own folder.
- Session assets are copied or downloaded into that folder.
- Autosaves and manual saves are scoped to the session.
- Player payloads receive app-managed asset references, not local paths.

## Top-Level Save File

Each persisted save file should be JSON and include schema metadata.

```json
{
  "schema_version": 1,
  "saved_at": "2026-06-29T20:15:00Z",
  "save_kind": "active",
  "session": {}
}
```

`save_kind` values:

- `active`: current session state.
- `autosave`: rolling recovery save.
- `manual`: GM-created in-session save.
- `export`: GM-created external copy.

Loading any save or autosave must require GM confirmation before active state is replaced.

If a save is corrupt, the GM should be notified and offered timestamped autosave/manual save options to attempt loading.

## Session

The session is the root canonical game state.

```json
{
  "id": "session-001",
  "name": "Goblin Caves",
  "created_at": "2026-06-29T19:00:00Z",
  "updated_at": "2026-06-29T20:15:00Z",
  "active_scene_id": "scene-001",
  "scenes": [],
  "assets": [],
  "trackers": [],
  "initiative": {},
  "settings": {},
  "gm": {}
}
```

Public fields:

- `id`
- `name`
- public scene projection
- public tracker projection
- public initiative projection

Private fields:

- `gm`
- asset source metadata
- local storage paths
- full tracker definitions for hidden trackers
- hidden initiative entries
- undiscovered combatant stats

## GM Metadata

GM metadata stores private local-only state.

```json
{
  "notes": "",
  "last_manual_save_id": "save-001",
  "active_save_id": "active",
  "private_flags": {}
}
```

These fields are never sent to the player display.

## Assets

Assets represent app-managed files that can be shown publicly.

```json
{
  "id": "asset-001",
  "kind": "image",
  "display_name": "Cavern Entrance",
  "filename": "asset-001.png",
  "mime_type": "image/png",
  "public_url": "/assets/session-001/asset-001.png",
  "created_at": "2026-06-29T19:30:00Z",
  "source": {
    "type": "url",
    "original_url": "https://example.test/cavern.png",
    "imported_at": "2026-06-29T19:30:00Z"
  }
}
```

Supported MVP image formats:

- jpg/jpeg
- tiff
- png
- gif
- webp
- svg

SVG is allowed at GM discretion for the MVP because this is a local GM-controlled tool.

Public asset projection:

```json
{
  "id": "asset-001",
  "url": "/assets/session-001/asset-001.png"
}
```

Player payloads may include app asset IDs and resolved app URLs. They must not include:

- `filename`
- local storage path
- `source.original_url`
- import metadata

Open asset questions:

- Final asset directory.

MVP asset decisions:

- No explicit image file size limit is required for the local-only MVP.
- Asset filenames should be generated internally as stable IDs, such as `asset-<uuid>.<ext>`.
- GM-facing display names should be stored separately from filenames.
- Duplicate image handling should notify the GM when an imported/downloaded image appears to match an existing asset.
- On duplicate detection, the GM should choose whether both locations share the existing asset or keep a separate copy.
- URL downloads may follow normal redirects up to a small redirect limit.
- The final URL response must still validate as an allowed image type.

## Scenes

Scenes describe the public scene display chosen by the GM.

```json
{
  "id": "scene-001",
  "title": "Cavern Entrance",
  "description": "A damp stone opening descends into darkness.",
  "image_asset_id": "asset-001",
  "gm_notes": "Ambush if they make noise.",
  "is_public": true
}
```

Public scene projection:

```json
{
  "id": "scene-001",
  "title": "Cavern Entrance",
  "description": "A damp stone opening descends into darkness.",
  "image": {
    "id": "asset-001",
    "url": "/assets/session-001/asset-001.png"
  }
}
```

Private scene fields:

- `gm_notes`
- local asset paths
- original image source URLs

## Trackers

Trackers are reusable counters/scales for timers, alert levels, resources, gold, and similar table state.

```json
{
  "id": "tracker-001",
  "label": "Security Alert",
  "value": 5,
  "visible": true,
  "mode": "bounded",
  "min_value": 1,
  "max_value": 15,
  "interval": 3,
  "display_mode": "label_color",
  "color_scale": "green_to_red",
  "named_values": [
    { "label": "Green", "color": null },
    { "label": "Yellow", "color": null },
    { "label": "Orange", "color": null },
    { "label": "Red", "color": null },
    { "label": "Black", "color": null }
  ],
  "step_controls": [-2, -1, 1, 2],
  "gm_notes": ""
}
```

`mode` values:

- `bounded`
- `unbounded`

`display_mode` values:

- `number`
- `label`
- `label_color`
- `number_label`

Default `color_scale` values:

- `green_to_red`
- `red_to_green`
- `black_to_white`
- `white_to_black`

Custom per-state colors are a stretch goal unless promoted into the MVP.

For MVP, custom per-state color picker remains a stretch goal. MVP uses the default color scales.

Interval mapping:

- If `interval` is `1`, each numeric value maps directly to a named value.
- If `interval` is greater than `1`, multiple numeric values map to one named value.
- Example: interval `3` maps values `1-3` to the first label, `4-6` to the second label, and so on.

GM controls:

- Always include `-1` and `+1`.
- May include interval-derived step buttons based on `ceil(interval / 2)`.
- May support explicit GM-configured step controls.

Public tracker projection for `label_color`:

```json
{
  "id": "tracker-001",
  "label": "Security Alert",
  "display_mode": "label_color",
  "display": {
    "label": "Yellow",
    "color": "#d8b400"
  }
}
```

Public tracker projection for `number`:

```json
{
  "id": "tracker-002",
  "label": "Party Gold",
  "display_mode": "number",
  "display": {
    "value": 125
  }
}
```

Hidden trackers are omitted from the public projection.

For interval-mapped trackers, the public projection must not reveal raw progress inside the interval unless the GM chooses a display mode that exposes the number.

## Initiative

Initiative state supports combatants and non-creature turn-order entries.

```json
{
  "visible": false,
  "current_entry_id": null,
  "hp_number_display": "current_max",
  "sort_mode": "initiative_then_manual",
  "entries": []
}
```

If `visible` is `false`, the player projection omits the initiative panel entirely.

`hp_number_display` values:

- `current_max`

Future values may include current-only display if needed.

Ordering:

- Sort by initiative descending.
- Use manual `sort_order` to resolve ties and place special rows.

### Creature Entry

```json
{
  "id": "init-001",
  "kind": "creature",
  "name": "Goblin Boss",
  "initiative": 18,
  "sort_order": 10,
  "player_visibility": "known",
  "ac": 15,
  "ac_revealed": true,
  "hp_current": 20,
  "hp_max": 56,
  "hp_visibility": "vibe",
  "gm_notes": "Flees below 10 HP."
}
```

`player_visibility` values:

- `hidden`: no row is shown.
- `visible`: row is shown with `???` replacing hidden data except initiative slot/speed.
- `known`: name and discovered information are shown.

`hp_visibility` values:

- `none`: no injury indication.
- `vibe`: rough health status.
- `numbers`: discovered health numbers according to `hp_number_display`.

Vibe health bands:

- `healthy`: 70% or higher.
- `injured`: 50% to 70%.
- `bloodied`: below 50%.

AC reveal is per combatant. The MVP does not need global enemy-type AC reveal behavior.

### Non-Creature Entry

Non-creature entries cover lair actions, environmental effects, pets, companions, vehicles, and similar turn-order rows.

```json
{
  "id": "init-002",
  "kind": "event",
  "name": "Lair Action",
  "initiative": 20,
  "sort_order": 20,
  "player_visibility": "known",
  "description": "The cavern trembles.",
  "gm_notes": "Drop loose stones near the altar."
}
```

Open initiative question:

- Resolved: public non-creature rows show only title/name and initiative slot number.

### Public Initiative Projection

If initiative is hidden:

```json
null
```

Known creature with revealed AC and vibe HP:

```json
{
  "id": "init-001",
  "kind": "creature",
  "name": "Goblin Boss",
  "initiative": 18,
  "is_current": true,
  "ac": 15,
  "hp": {
    "mode": "vibe",
    "status": "bloodied"
  }
}
```

Visible but not known creature:

```json
{
  "id": "init-003",
  "kind": "creature",
  "name": "???",
  "initiative": 14,
  "is_current": false
}
```

Known creature with number HP:

```json
{
  "id": "init-004",
  "kind": "creature",
  "name": "Knight",
  "initiative": 12,
  "is_current": false,
  "hp": {
    "mode": "numbers",
    "current": 20,
    "max": 56
  }
}
```

Non-creature entry:

```json
{
  "id": "init-002",
  "kind": "event",
  "name": "Lair Action",
  "initiative": 20,
  "is_current": false
}
```

Public non-creature entries should not include private descriptions or GM notes. MVP public detail is limited to title/name, initiative slot number, ID, kind, and current-turn status.

Hidden initiative entries are omitted.

GM-only initiative fields are omitted:

- `gm_notes`
- hidden names
- hidden AC
- hidden HP
- private descriptions

## Public State Projection

The player polling endpoint should return only projected state.

```json
{
  "session": {
    "id": "session-001",
    "name": "Goblin Caves"
  },
  "scene": {},
  "trackers": [],
  "initiative": null
}
```

Projection rules:

- Scene includes only public title, description, and app-managed image reference.
- Trackers include only visible trackers.
- Tracker display follows each tracker's `display_mode`.
- Initiative is `null` when globally hidden.
- Initiative entries include only non-hidden rows.
- Combatant names, AC, and HP are included only when visibility rules allow them.
- Asset objects include `id` and resolved app `url`.

## Save And Autosave Metadata

Autosave behavior is part of persistence, but save metadata affects the state model.

```json
{
  "id": "autosave-1",
  "save_kind": "autosave",
  "created_at": "2026-06-29T20:15:00Z",
  "label": "Most recent autosave",
  "path": "autosaves/autosave-1.json"
}
```

Autosave slots:

- `autosave-1`: most recent change.
- `autosave-2`: roughly 5-10 minutes old during regular activity.
- `autosave-3`: roughly 10-30 minutes old during regular activity.

During startup/warm-up, empty autosave slots should be populated from prior slot contents even if they are recent. The slots then drift toward target age windows during normal play.

Manual saves:

- GM-named.
- Timestamped.
- Stored in the session folder.
- Separate from autosaves.
- Save flow asks whether to replace the previous manual save or save as a copy.

Exports:

- Separate workflow from in-session manual save.
- Intended for creating a named file outside the session folder where platform constraints allow it.
- Browser-based export may return a file download to the browser instead of writing directly to an arbitrary folder chosen by Flask.
- Server-side export to a specific folder should use an app-configured export directory if direct folder selection is not available.

## Validation Notes

Implementation should validate:

- Required IDs and labels.
- Unique IDs within a session.
- Asset references point to app-managed assets in the same session.
- Asset duplicate checks should warn the GM and allow shared asset reuse or a separate copy.
- Bounded tracker values stay inside bounds unless explicitly allowed later.
- Tracker interval and named values are coherent.
- Initiative visibility values are known enum values.
- HP values are non-negative and `hp_current` does not exceed `hp_max` unless explicitly allowed later.
- Save files include supported `schema_version`.
