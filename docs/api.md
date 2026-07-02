# API Design

## Philosophy

The frontend should never manipulate application state directly.

All state changes occur through HTTP endpoints.

The backend owns canonical session state. GM endpoints may operate on full state. Player endpoints must consume only the public projection defined in `docs/state-model.md`.

The MVP uses Flask as a minimal wrapper for routes, templates, static files, JSON endpoints, uploads, and tests.

## Route Principles

- Keep routes small.
- Prefer simple JSON payloads.
- Validate every GM update server-side.
- Trigger autosave after every successful GM state-changing action once local persistence is implemented.
- Never return full session state from player routes.
- Never expose local paths, original image URLs, hidden notes, hidden trackers, hidden combatants, hidden AC, or hidden HP to players.

Current implementation status:

- Phase 1 and Phase 2 page routes, public projection, scene update, asset upload, asset URL download, duplicate preview, and app-managed asset serving are implemented.
- Tracker, initiative, GM session listing/creation, full GM session API, and persistence APIs remain planned work.
- JSON responses currently return `"autosaved": false` for implemented GM mutations because local persistence is not implemented yet.

## Page Routes

### `GET /`

Redirects to the GM session picker or local GM home page.

### `GET /gm`

Returns the GM session picker and local management page.

### `GET /s/<session_id>`

Redirects to `/s/<session_id>/player`.

The bare session route uses the safer player view by default.

### `GET /s/<session_id>/gm`

Returns the GM control interface for a foldered session.

This page may load full GM state through GM API endpoints.

### `GET /s/<session_id>/player`

Returns the passive player display for a foldered session.

This page must not include full state in rendered HTML or client-side JavaScript. It should poll the public state endpoint.

## Public API

### `GET /api/s/<session_id>/public`

Returns the player-safe public projection.

This endpoint is used by the player display polling loop.

Example response:

```json
{
  "session": {
    "id": "session-001",
    "name": "Goblin Caves"
  },
  "scene": {
    "id": "scene-001",
    "title": "Cavern Entrance",
    "description": "A damp stone opening descends into darkness.",
    "image": {
      "id": "asset-001",
      "url": "/assets/session-001/asset-001.png"
    }
  },
  "trackers": [
    {
      "id": "tracker-001",
      "label": "Security Alert",
      "display_mode": "label_color",
      "display": {
        "label": "Yellow",
        "color": "#d8b400"
      }
    }
  ],
  "initiative": null
}
```

Projection rules:

- `scene` contains only public scene fields and app-managed asset references.
- Scene image includes both asset ID and resolved app URL.
- `trackers` includes only visible trackers.
- Tracker display follows each tracker's configured display mode.
- `initiative` is `null` when the overall initiative display is hidden.
- Initiative entries include only non-hidden rows.
- Combatant AC and HP are included only when visibility rules allow them.

## GM Session API

Status: planned. The current app supports direct session URLs such as `/s/default/gm`, but session listing, creation, and full GM-state JSON endpoints are not implemented yet.

### `GET /api/gm/sessions`

Lists available foldered sessions.

Example response:

```json
{
  "sessions": [
    {
      "id": "session-001",
      "name": "Goblin Caves",
      "updated_at": "2026-06-29T20:15:00Z"
    }
  ]
}
```

### `POST /api/gm/sessions`

Creates a new foldered session.

Example request:

```json
{
  "name": "Goblin Caves"
}
```

Example response:

```json
{
  "session": {
    "id": "session-001",
    "name": "Goblin Caves"
  }
}
```

### `GET /api/gm/session/<session_id>`

Returns full GM state for a session.

This endpoint is GM-only. It may include GM notes, hidden trackers, hidden combatants, asset source metadata, save metadata, and other private state.

It must never be called by the player display.

## Scene API

### `POST /api/gm/session/<session_id>/scene`

Updates the active scene fields.

Example request:

```json
{
  "title": "Cavern Entrance",
  "description": "A damp stone opening descends into darkness.",
  "image_asset_id": "asset-001"
}
```

Example response:

```json
{
  "scene": {
    "id": "scene-001",
    "title": "Cavern Entrance",
    "description": "A damp stone opening descends into darkness.",
    "image_asset_id": "asset-001"
  },
  "autosaved": false
}
```

Validation:

- `image_asset_id`, when present, must point to an app-managed asset in the same session.
- Local file paths and external URLs are not accepted as scene image references.
- The GM must import/upload/download assets through the asset API first.

## Asset API

### `POST /api/gm/session/<session_id>/assets/upload`

Imports a local image file into app-managed session assets.

Request type: multipart form upload.

Accepted file formats:

- jpg/jpeg
- tiff
- png
- gif
- webp
- svg

Example response:

```json
{
  "asset": {
    "id": "asset-001",
    "kind": "image",
    "display_name": "Cavern Entrance",
    "mime_type": "image/png",
    "public_url": "/assets/session-001/asset-001.png"
  },
  "autosaved": false
}
```

### `POST /api/gm/session/<session_id>/assets/download`

Downloads an image URL immediately into app-managed session assets.

This avoids delaying the player display when the GM later selects the image.

Example request:

```json
{
  "url": "https://example.test/cavern.png",
  "display_name": "Cavern Entrance"
}
```

Example response:

```json
{
  "asset": {
    "id": "asset-001",
    "kind": "image",
    "display_name": "Cavern Entrance",
    "mime_type": "image/png",
    "public_url": "/assets/session-001/asset-001.png"
  },
  "autosaved": false
}
```

Private asset metadata may retain the original URL for GM reference and debugging. Player payloads must never include original source URLs.

MVP asset API decisions:

- No explicit image file size limit is required for the local-only MVP.
- Assets are stored in the app-managed `data/sessions/<session_id>/assets/` folder for the current MVP implementation.
- Asset filenames should be generated internally as stable IDs, such as `asset-<uuid>.<ext>`.
- GM-facing display names should be stored separately from filenames.
- Duplicate asset detection should warn the GM when an imported/downloaded image appears to match an existing asset.
- The GM should choose whether to reuse/share the existing asset or keep a separate copy.
- URL downloads may follow normal redirects up to a small redirect limit.
- The final URL response must still validate as an allowed image type.

### `GET /assets/<session_id>/<asset_filename>`

Serves app-managed asset files.

This route must only serve files from the app-managed session asset folder. It must not accept arbitrary local file paths.

## Tracker API

Status: planned for Phase 3. Tracker projection helpers exist, but tracker GM routes, tracker state validation, and tracker UI are not implemented yet.

### `POST /api/gm/session/<session_id>/trackers`

Creates a tracker.

Example request:

```json
{
  "label": "Security Alert",
  "mode": "bounded",
  "min_value": 1,
  "max_value": 15,
  "value": 1,
  "interval": 3,
  "display_mode": "label_color",
  "color_scale": "green_to_red",
  "named_values": [
    { "label": "Green" },
    { "label": "Yellow" },
    { "label": "Orange" },
    { "label": "Red" },
    { "label": "Black" }
  ],
  "visible": true
}
```

Example response:

```json
{
  "tracker": {
    "id": "tracker-001",
    "label": "Security Alert"
  },
  "autosaved": false
}
```

### `PATCH /api/gm/session/<session_id>/trackers/<tracker_id>`

Updates tracker settings or value.

Example request:

```json
{
  "value": 5,
  "visible": true,
  "display_mode": "label"
}
```

### `POST /api/gm/session/<session_id>/trackers/<tracker_id>/adjust`

Adjusts tracker value using a delta.

Example request:

```json
{
  "delta": 1
}
```

Validation:

- Bounded tracker values must stay within `min_value` and `max_value`.
- Unbounded trackers may omit `max_value`.
- Interval must be a positive integer.
- Display mode must be one of `number`, `label`, `label_color`, `number_label`.
- Color scale must be one of `green_to_red`, `red_to_green`, `black_to_white`, `white_to_black`.

## Initiative API

Status: planned for Phase 4. Initiative projection helpers exist, but initiative GM routes, initiative state validation, and initiative UI are not implemented yet.

### `PATCH /api/gm/session/<session_id>/initiative`

Updates overall initiative settings.

Example request:

```json
{
  "visible": true,
  "current_entry_id": "init-001",
  "hp_number_display": "current_max"
}
```

If `visible` is `false`, public projection returns `initiative: null`.

### `POST /api/gm/session/<session_id>/initiative/entries`

Creates a creature or non-creature initiative entry.

Creature example:

```json
{
  "kind": "creature",
  "name": "Goblin Boss",
  "initiative": 18,
  "player_visibility": "hidden",
  "ac": 15,
  "hp_current": 56,
  "hp_max": 56,
  "hp_visibility": "none"
}
```

Non-creature example:

```json
{
  "kind": "event",
  "name": "Lair Action",
  "initiative": 20,
  "player_visibility": "known",
  "description": "The cavern trembles."
}
```

### `PATCH /api/gm/session/<session_id>/initiative/entries/<entry_id>`

Updates an initiative entry.

Example request:

```json
{
  "player_visibility": "known",
  "ac_revealed": true,
  "hp_visibility": "vibe",
  "hp_current": 20
}
```

### `POST /api/gm/session/<session_id>/initiative/reorder`

Reorders initiative entries.

Initiative defaults to initiative descending, then manual order for ties and special rows.

Example request:

```json
{
  "entry_ids": ["init-002", "init-001", "init-003"]
}
```

Validation:

- `player_visibility` must be `hidden`, `visible`, or `known`.
- Hidden entries are omitted from public projection.
- Visible entries use `???` for hidden data except initiative slot/speed.
- Known entries may show discovered information.
- AC reveal is per combatant.
- HP visibility must be `none`, `vibe`, or `numbers`.
- Non-creature rows may omit AC and HP fields.

Public non-creature initiative rows should include title/name and initiative slot number only, plus technical fields needed for rendering such as ID, kind, and current-turn status.

## Save And Load API

Status: planned for the MVP after scene, tracker, and initiative state exist. Local save/load persistence and autosave are not implemented yet.

### `POST /api/gm/session/<session_id>/save`

Creates a manual in-session save.

Manual saves are GM-named, timestamped, and separate from autosaves.

Example request:

```json
{
  "name": "Before boss fight",
  "mode": "copy"
}
```

`mode` values:

- `copy`: preserve previous manual saves.
- `replace_previous`: replace or supersede the previous manual save.

### `GET /api/gm/session/<session_id>/saves`

Lists available autosaves and manual saves for a session.

Example response:

```json
{
  "saves": [
    {
      "id": "autosave-1",
      "save_kind": "autosave",
      "label": "Most recent autosave",
      "created_at": "2026-06-29T20:15:00Z"
    },
    {
      "id": "save-001",
      "save_kind": "manual",
      "label": "Before boss fight",
      "created_at": "2026-06-29T20:05:00Z"
    }
  ]
}
```

### `POST /api/gm/session/<session_id>/load`

Loads a selected save after GM confirmation.

Example request:

```json
{
  "save_id": "save-001",
  "confirmed": true
}
```

The server should reject load requests unless confirmation is explicit.

If the selected save is corrupt, the server should return a clear error and include viable timestamped alternatives when possible.

### `POST /api/gm/session/<session_id>/export`

Creates an export copy.

Export is separate from in-session manual save.

For MVP, export should return a browser file download. If server-side export directories are added later, they should use an app-configured export directory rather than assuming Flask can write directly to an arbitrary user-selected folder.

Example request:

```json
{
  "name": "Goblin Caves backup"
}
```

## Autosave Behavior

Status: planned. Implemented GM mutation endpoints currently return `"autosaved": false`.

Every successful GM state-changing endpoint should trigger autosave.

Autosave slots:

- `autosave-1`: most recent change.
- `autosave-2`: roughly 5-10 minutes old during regular activity.
- `autosave-3`: roughly 10-30 minutes old during regular activity.

During startup/warm-up, empty autosave slots should be populated from prior slot contents even if they are recent. The slots then drift toward target age windows during normal play.

## Error Responses

Use simple JSON error responses.

Example:

```json
{
  "error": {
    "code": "invalid_tracker_value",
    "message": "Tracker value must be between 1 and 15."
  }
}
```

## Test Expectations

Tests should cover:

- Player public endpoint excludes GM-only fields.
- Player public endpoint includes asset ID and resolved app URL.
- Hidden trackers are omitted from public projection.
- Interval-mapped trackers do not expose hidden numeric progress unless configured to do so.
- Hidden initiative returns `initiative: null`.
- Hidden initiative entries are omitted.
- Visible initiative entries use `???` for hidden data.
- Known initiative entries show only discovered AC/HP.
- Scene image references must be app-managed assets.
- GM state-changing endpoints trigger autosave once persistence is implemented.
- Save load requires explicit confirmation.
- Corrupt save handling returns clear errors and viable alternatives when possible.
