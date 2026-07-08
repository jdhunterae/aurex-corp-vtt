# Terminology Context

Purpose: define project terms so AI agents use consistent names in code, docs, tickets, and UI copy.

## Surfaces

- GM interface: the read/write control surface for managing session state.
- Player display: preferred term for the passive/read-only display of public projected state.
- Player interface: avoid when possible because it implies player interaction.

## State Terms

- Full session state: canonical backend-owned state. May contain private GM data.
- Public projection: explicit filtered state returned to player-facing routes and APIs.
- Session: top-level game state object identified by `session_id`.
- Foldered session: a session with a project-local folder under `data/sessions/<session_id>/`.
- Active scene: the current public scene selected for display.
- App-managed asset: an uploaded or downloaded asset copied into the app's session asset folder and referenced by asset ID/public URL.

## Feature Terms

- Scene: public title, description, and optional app-managed image asset selected by the GM.
- Prepared scene library: planned workflow for creating multiple scenes before play and switching between them.
- Tracker: generic numeric counter/scale used for resources, timers, alert levels, gold, rounds, and similar state.
- Named values: labels mapped from tracker numeric ranges.
- Display mode: tracker player-facing display behavior: `number`, `label`, `label_color`, or `number_label`.
- Initiative: planned combat turn-order feature with player visibility controls.
- Autosave: planned rolling persistence after successful GM state-changing actions.
- Manual save: planned GM-named in-session save.
- Export: planned separate workflow for creating a named save copy outside normal in-session saves.

## Visibility Terms

- Visible tracker: included in public projection.
- Hidden tracker: omitted from public projection.
- Hidden initiative: overall initiative projection returns `null`.
- Hidden combatant: omitted from public projection.
- Visible combatant: shown to players with hidden data replaced by `???`.
- Known combatant: shown with discovered information according to visibility rules.

## Status Terms

- Backlog: planned but not ready to work immediately.
- Ready: ready to implement when current active work is complete.
- In Progress: currently being worked.
- Blocked: waiting on a stated dependency or decision.
- Done: completed and retained for history.

TODO: Decide final terminology for health "vibe" bands before Phase 4 UI work.
