# P02-004 Add Scene Asset Ingestion

## Status

In Progress

## Phase

Phase 2 - Scene Display

## Goal

Allow the GM to add scene images through local import/upload or URL download while keeping player-facing image references public-safe.

## Acceptance Criteria

- [x] GM can add a local image through the documented import/upload workflow.
- [x] GM can provide a URL that the server downloads into app-managed assets.
- [x] URL image import downloads when submitted so scene display does not wait on remote download.
- [x] Imported and downloaded files are validated as supported image types.
- [x] Supported image types include jpg/jpeg, tiff, png, gif, webp, and svg.
- [x] SVG is allowed at GM discretion for MVP.
- [x] Local-only MVP has no explicit image file size limit.
- [x] Asset filenames use generated stable IDs, with GM display names stored separately.
- [ ] Duplicate image detection warns the GM when an asset appears to match an existing asset.
- [x] GM can choose whether duplicate-looking images reuse the existing asset or remain separate copies.
- [x] URL downloads may follow limited redirects and must validate final image type.
- [x] Player-facing payloads receive only app-managed public asset references.
- [x] Player-facing payloads include asset ID and resolved app URL.
- [x] Local filesystem source paths are not stored in public state.
- [x] URL source values are not exposed to the player display.
- [x] Original URL source metadata is stored privately in GM/session data.
- [x] Downloaded URL assets are reused locally instead of redownloaded when shown again.
- [x] Failed imports or downloads return clear errors.
- [x] Asset ingestion behavior is covered by tests.

## Notes

Depends on P02-001. This ticket should define and implement the safe boundary between GM-supplied image sources and player-visible scene assets.

Upload, URL download, local asset registration, app-managed serving, and duplicate behavior selection are implemented. Remaining work: active duplicate warning UX before saving a duplicate.
