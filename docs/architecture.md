# Architecture

## Purpose

The application consists of a single Flask backend responsible for maintaining game state.

The GM interacts with the backend through a control interface.

Players receive a filtered, read-only view of the same state.

Current implementation status:

- Phase 1 application skeleton is complete.
- Phase 2 scene display is complete.
- Phase 3 generic trackers are in progress: tracker state, projection, GM controls, player rendering, and player auto-refresh are implemented; GM control layout polish remains.
- Phase 4 initiative and local save/load persistence remain backlog.

---

## System Overview

GM Browser

↓

Flask Server

↓

Backend Session State

↓

Public Projection

↓

Player Browser

The player browser must update automatically when the GM changes public state. Manual refresh is not an acceptable steady-state workflow for the MVP.

---

## Core Principles

The backend owns all state.

The player display never modifies state.

The GM interface edits state through server-side routes and JSON endpoints.

The player display only receives public projected information.

GM-only notes, original asset source URLs, local paths, hidden trackers, hidden combatants, hidden AC, hidden HP, and private save metadata must not reach player routes or player JSON.

## Player Update Flow

Every successful GM action that changes public state should become visible on the player display without manual player refresh.

The update mechanism must preserve the public projection boundary. The player display may poll or subscribe to public projected state, but it must not receive full GM/session state.

Initial MVP implementation should prefer the simplest reliable local-first mechanism, such as polling `/api/s/<session_id>/public`. WebSockets or server-sent events should be introduced only if the simpler approach is not adequate.

## Current Runtime Shape

The MVP currently uses in-memory session state with project-local session folders under `data/sessions/`.

Implemented session-scoped assets are stored under:

```text
data/sessions/<session_id>/assets/
```

Local save/load persistence is planned but not implemented yet. JSON GM mutation responses currently report `autosaved: false` until persistence exists.

---

## Future Considerations

Session IDs are already part of the route and folder structure. A session listing/creation UI and persistence-backed session loading are still future work.

Each session should have:

- Session ID
- GM Key or other access control, if remote sharing is added later
- Independent state
