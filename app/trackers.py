"""Tracker state helpers."""

from __future__ import annotations

from math import ceil
from typing import Any
import uuid

from app.state import utc_now_iso

COLOR_SCALES = {"green_to_red", "red_to_green", "black_to_white", "white_to_black"}
DISPLAY_MODES = {"number", "label", "label_color", "number_label"}
TRACKER_MODES = {"bounded", "unbounded"}
LABEL_DISPLAY_MODES = {"label", "label_color", "number_label"}


class TrackerValidationError(ValueError):
    pass


def create_tracker(session: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    tracker = normalize_tracker_payload(payload)
    tracker["id"] = f"tracker-{uuid.uuid4().hex}"
    tracker["gm_notes"] = str(payload.get("gm_notes", "")).strip()
    session.setdefault("trackers", []).append(tracker)
    session["updated_at"] = utc_now_iso()
    return tracker


def update_tracker(session: dict[str, Any], tracker_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    tracker = find_tracker(session, tracker_id)
    merged = {**tracker, **payload}
    normalized = normalize_tracker_payload(merged)
    normalized["id"] = tracker["id"]
    normalized["gm_notes"] = str(merged.get("gm_notes", "")).strip()
    tracker.clear()
    tracker.update(normalized)
    session["updated_at"] = utc_now_iso()
    return tracker


def adjust_tracker(session: dict[str, Any], tracker_id: str, delta: Any) -> dict[str, Any]:
    tracker = find_tracker(session, tracker_id)
    delta_value = parse_int(delta, "Tracker adjustment must be an integer.")
    payload = {**tracker, "value": int(tracker.get("value", 0)) + delta_value}
    return update_tracker(session, tracker_id, payload)


def find_tracker(session: dict[str, Any], tracker_id: str) -> dict[str, Any]:
    tracker = next((item for item in session.get("trackers", []) if item.get("id") == tracker_id), None)
    if tracker is None:
        raise TrackerValidationError("Tracker does not exist in this session.")
    return tracker


def normalize_tracker_payload(payload: dict[str, Any]) -> dict[str, Any]:
    label = str(payload.get("label", "")).strip()
    if not label:
        raise TrackerValidationError("Tracker label is required.")

    mode = str(payload.get("mode", "bounded")).strip() or "bounded"
    if mode not in TRACKER_MODES:
        raise TrackerValidationError("Tracker mode must be bounded or unbounded.")

    display_mode = str(payload.get("display_mode", "number")).strip() or "number"
    if display_mode not in DISPLAY_MODES:
        raise TrackerValidationError("Tracker display mode is invalid.")

    color_scale = str(payload.get("color_scale", "green_to_red")).strip() or "green_to_red"
    if color_scale not in COLOR_SCALES:
        raise TrackerValidationError("Tracker color scale is invalid.")

    value = parse_int(payload.get("value", 0), "Tracker value must be an integer.")
    min_value = parse_int(payload.get("min_value", 0), "Tracker minimum must be an integer.")
    interval = parse_int(payload.get("interval", 1), "Tracker interval must be an integer.")
    if interval < 1:
        raise TrackerValidationError("Tracker interval must be at least 1.")

    max_value = None
    if mode == "bounded":
        max_value = parse_int(payload.get("max_value"), "Tracker maximum must be an integer.")
        if min_value > max_value:
            raise TrackerValidationError("Tracker minimum cannot be greater than maximum.")
        if value < min_value or value > max_value:
            raise TrackerValidationError("Tracker value must stay within its bounds.")
    elif payload.get("max_value") not in (None, ""):
        max_value = parse_int(payload.get("max_value"), "Tracker maximum must be an integer.")

    named_values = normalize_named_values(payload.get("named_values", []))
    if display_mode in LABEL_DISPLAY_MODES and not named_values:
        raise TrackerValidationError("Mapped tracker displays require at least one named value.")

    step_controls = normalize_step_controls(payload.get("step_controls"), interval)

    tracker = {
        "label": label,
        "value": value,
        "visible": parse_bool(payload.get("visible", False)),
        "mode": mode,
        "min_value": min_value,
        "interval": interval,
        "display_mode": display_mode,
        "color_scale": color_scale,
        "named_values": named_values,
        "step_controls": step_controls,
    }
    if max_value is not None:
        tracker["max_value"] = max_value
    return tracker


def normalize_named_values(value: Any) -> list[dict[str, str | None]]:
    if isinstance(value, str):
        raw_items = [{"label": part.strip()} for part in value.splitlines()]
    elif isinstance(value, list):
        raw_items = value
    else:
        raw_items = []

    named_values = []
    for item in raw_items:
        if isinstance(item, str):
            item = {"label": item}
        if not isinstance(item, dict):
            continue
        label = str(item.get("label", "")).strip()
        if not label:
            continue
        color = item.get("color")
        named_values.append({"label": label, "color": color if isinstance(color, str) and color.strip() else None})
    return named_values


def normalize_step_controls(value: Any, interval: int) -> list[int]:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped:
            raw_values = [part.strip() for part in stripped.replace(",", "\n").splitlines()]
        else:
            raw_values = derived_step_controls(interval)
    elif isinstance(value, list):
        raw_values = value
    else:
        raw_values = derived_step_controls(interval)

    controls = []
    for item in raw_values:
        try:
            parsed = int(item)
        except (TypeError, ValueError):
            continue
        if parsed != 0 and parsed not in controls:
            controls.append(parsed)

    for required in (-1, 1):
        if required not in controls:
            controls.append(required)
    return sorted(controls)


def derived_step_controls(interval: int) -> list[int]:
    derived = ceil(interval / 2)
    return [-derived, -1, 1, derived] if derived > 1 else [-1, 1]


def parse_int(value: Any, message: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        raise TrackerValidationError(message) from None


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in {"1", "true", "yes", "on"}
    return bool(value)
