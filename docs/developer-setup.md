# Developer Setup

## Requirements

- Python 3.11 or newer.
- A local virtual environment for project commands.
- No database, frontend package manager, or build step is required for the current MVP.

Project metadata in `pyproject.toml` declares:

```text
requires-python = ">=3.11"
```

## Local Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Use the virtual environment for Python, Flask, pytest, and package installs. Do not install project dependencies into the global Python environment.

## Run Tests

Run the full test suite:

```bash
.venv/bin/python -m pytest
```

Pytest is configured in `pyproject.toml` to discover tests under `tests/`.

For testing strategy and expected coverage by feature area, see `docs/testing.md`.

## Run The Server

Start the local Flask development server:

```bash
.venv/bin/flask --app app.server run --debug
```

The development server defaults to:

```text
http://127.0.0.1:5000
```

Useful local URLs:

- `http://127.0.0.1:5000/gm` - GM home page.
- `http://127.0.0.1:5000/s/default/gm` - GM controls for the default session.
- `http://127.0.0.1:5000/s/default/player` - player display for the default session.
- `http://127.0.0.1:5000/api/s/default/public` - player-safe public JSON.
- `http://127.0.0.1:5000/healthz` - health check.

## Runtime Data

During MVP development, runtime session data lives under:

```text
data/sessions/
```

The app may create session folders, asset folders, save folders, uploaded images, downloaded images, and other local runtime data there.

Do not commit runtime data. The repository `.gitignore` excludes `data/`.

To reset local runtime state during development, stop the server and remove the project-local `data/` directory. This deletes local sessions, uploaded assets, downloaded assets, autosaves, and saves.

Do not remove another user's local data unless they explicitly ask for it.

## Development Constraints

- Keep the app local-first.
- Keep player routes and player JavaScript limited to public projected state.
- Do not add databases, authentication systems, async workers, frontend frameworks, build tools, or package managers unless explicitly approved.
- Add dependencies to `requirements.txt` only when they clearly reduce complexity.
- Prefer focused tests around projection safety, route behavior, validation, and user-visible workflows.
