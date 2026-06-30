"""In-memory session state for the Phase 1 skeleton."""

from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

DEFAULT_SESSION_ID = "default"
DATA_DIR = Path("data")
SESSIONS_DIR = DATA_DIR / "sessions"

_sessions: dict[str, dict[str, Any]] = {}
_active_session_id = DEFAULT_SESSION_ID


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def session_path(session_id: str) -> Path:
    return SESSIONS_DIR / session_id


def bootstrap_session_layout(session_id: str = DEFAULT_SESSION_ID) -> Path:
    """Create the local folder layout needed for a session skeleton."""
    root = session_path(session_id)
    for child in (root, root / "assets", root / "autosaves", root / "saves"):
        child.mkdir(parents=True, exist_ok=True)
    return root


def create_session_state(session_id: str = DEFAULT_SESSION_ID, name: str | None = None) -> dict[str, Any]:
    now = utc_now_iso()
    return {
        "id": session_id,
        "name": name or session_id,
        "created_at": now,
        "updated_at": now,
        "active_scene_id": None,
        "scenes": [],
        "assets": [],
        "trackers": [],
        "initiative": {
            "visible": False,
            "current_entry_id": None,
            "hp_number_display": "current_max",
            "sort_mode": "initiative_then_manual",
            "entries": [],
        },
        "settings": {},
        "gm": {
            "notes": "",
            "last_manual_save_id": None,
            "active_save_id": "active",
            "private_flags": {},
        },
    }


def load_or_create_session(session_id: str = DEFAULT_SESSION_ID, name: str | None = None) -> dict[str, Any]:
    bootstrap_session_layout(session_id)
    if session_id not in _sessions:
        _sessions[session_id] = create_session_state(session_id, name)
    return _sessions[session_id]


def get_session(session_id: str = DEFAULT_SESSION_ID) -> dict[str, Any]:
    return load_or_create_session(session_id)


def update_session(session_id: str, updates: dict[str, Any]) -> dict[str, Any]:
    session = load_or_create_session(session_id)
    session.update(updates)
    session["updated_at"] = utc_now_iso()
    return session


def set_active_session(session_id: str) -> dict[str, Any]:
    global _active_session_id
    _active_session_id = session_id
    return load_or_create_session(session_id)


def get_active_session() -> dict[str, Any]:
    return load_or_create_session(_active_session_id)


def snapshot_session(session_id: str = DEFAULT_SESSION_ID) -> dict[str, Any]:
    return deepcopy(load_or_create_session(session_id))
