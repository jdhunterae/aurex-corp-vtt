# Aurex Corp VTT

A lightweight Virtual Tabletop focused on one job:

Giving a Dungeon Master complete control over what players see during a tabletop RPG session.

Unlike traditional VTTs, Aurex Corp VTT is intentionally minimal. It is designed for local, in-person games where the GM controls a secondary display (TV, projector, or monitor), while also supporting future online sessions through shareable player links.

## Project Goals

- Local-first
- Simple to run
- Modular feature design
- Self-hostable
- Easy to understand and modify
- No unnecessary complexity

## Current Status

Phase 2 — Scene Display Complete

The repository contains a working Flask application with GM and player pages, an explicit public-state projection layer, scene display controls, and app-managed scene image asset ingestion.

Development is currently ready to begin Phase 3: Generic Trackers.

Implemented today:

- Local Flask server and app factory.
- GM home page and per-session GM control page.
- Passive player display backed by public projected state.
- Public JSON endpoint that excludes GM-only state.
- Scene title, description, and image display.
- GM scene controls.
- Image upload into app-managed session assets.
- Image URL download into app-managed session assets.
- Duplicate image detection with GM choice to reuse or keep a separate copy.
- Tests for routes, projection safety, scene controls, scene display, and asset ingestion.

Not implemented yet:

- Generic tracker GM controls and player rendering.
- Initiative GM controls and player rendering.
- Local save/load persistence and autosave.
- Session listing/creation UI beyond direct session URLs.

Key planning docs:

- `/docs/roadmap.md`
- `/docs/architecture.md`
- `/docs/state-model.md`
- `/docs/api.md`
- `/docs/testing.md`
- `/.project-board/`

## Planned Features

- Scene display: complete for the current MVP phase
- Generic counters and trackers: next phase
- Initiative tracker
- Public/GM visibility controls
- GM notes
- Local save/load
- Future session sharing beyond the local MVP

## Roadmap

See `/docs/roadmap.md`

## Quick Start

Create a local virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Run tests:

```bash
.venv/bin/python -m pytest
```

Run the local server:

```bash
.venv/bin/flask --app app.server run --debug
```

The development server defaults to:

```text
http://127.0.0.1:5000
```

Useful local URLs:

- `http://127.0.0.1:5000/gm` — GM home page.
- `http://127.0.0.1:5000/s/default/gm` — GM controls for the default session.
- `http://127.0.0.1:5000/s/default/player` — player display for the default session.
- `http://127.0.0.1:5000/api/s/default/public` — player-safe public JSON.
- `http://127.0.0.1:5000/healthz` — health check.

Health check:

```bash
curl http://127.0.0.1:5000/healthz
```

Use the local virtual environment for future Python commands, package installs, and tests. Do not install project dependencies into the global Python environment.

Runtime data is stored under project-local `data/sessions/` during MVP development. Do not commit local session data, uploaded assets, saves, logs, virtual environments, or caches.
