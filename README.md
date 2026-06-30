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

Phase 0 — Project Planning Complete

The repository contains finalized MVP planning docs for the local server version. Application development begins in Phase 1 with the Flask application skeleton.

Key planning docs:

- `/docs/roadmap.md`
- `/docs/architecture.md`
- `/docs/state-model.md`
- `/docs/api.md`
- `/docs/testing.md`
- `/.project-board/`

## Planned Features

- Scene display
- Battle maps
- Initiative tracker
- Generic counters
- Public/GM visibility controls
- GM notes
- Session sharing
- Local save/load

## Roadmap

See `/docs/roadmap.md`

## Local Development

Create a local virtual environment:

```text
python -m venv .venv
```

Install dependencies:

```text
.venv/bin/python -m pip install -r requirements.txt
```

Run the local server:

```text
.venv/bin/flask --app app.server run --debug
```

Health check:

```text
GET /healthz
```

Use the local virtual environment for future Python commands, package installs, and tests. Do not install project dependencies into the global Python environment.
