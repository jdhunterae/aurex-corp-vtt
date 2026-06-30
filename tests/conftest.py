from pathlib import Path

import pytest

import app.state as state
from app.server import create_app


@pytest.fixture()
def app(tmp_path: Path):
    state.DATA_DIR = tmp_path / "data"
    state.SESSIONS_DIR = state.DATA_DIR / "sessions"
    state._sessions.clear()
    state._active_session_id = state.DEFAULT_SESSION_ID

    flask_app = create_app()
    flask_app.config.update(TESTING=True)
    return flask_app


@pytest.fixture()
def client(app):
    return app.test_client()
