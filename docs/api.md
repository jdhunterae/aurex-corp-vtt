# API Design

## Philosophy

The frontend should never manipulate application state directly.

All state changes occur through HTTP endpoints.

---

## Planned Routes

Player View

GET /player/<session_id>

GM View

GET /gm/<gm_key>

---

## Planned API

GET /api/session/public

Returns

- scene
- public trackers
- visible initiative

GET /api/session/full

Returns

Complete game state.

POST /api/session/update

Updates one portion of game state.

---

## Design Goals

Small payloads

Simple JSON

Easy to debug
