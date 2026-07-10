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

Phase 3 — Generic Trackers In Progress

The repository contains a working Flask application with GM and player pages, an explicit public-state projection layer, scene display controls, app-managed scene image asset ingestion, generic tracker controls/rendering, and player auto-refresh. GM control layout polish is the next Phase 3 usability milestone.

For detailed status, see `/docs/roadmap.md` and `/docs/changelog.md`.

Key planning docs:

- `/docs/roadmap.md`
- `/docs/changelog.md`
- `/docs/architecture.md`
- `/docs/state-model.md`
- `/docs/api.md`
- `/docs/developer-setup.md`
- `/docs/testing.md`
- `/.project-board/`

## Roadmap

See `/docs/roadmap.md`

## Quick Start

For more detail, see `/docs/developer-setup.md`.

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
