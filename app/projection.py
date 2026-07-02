"""Public state projection for player-facing routes."""

from __future__ import annotations

from typing import Any

COLOR_SCALE_ENDPOINTS = {
    "green_to_red": ("#2f9e44", "#c92a2a"),
    "red_to_green": ("#c92a2a", "#2f9e44"),
    "black_to_white": ("#1f2933", "#f8fafc"),
    "white_to_black": ("#f8fafc", "#1f2933"),
}

TRACKER_DISPLAY_MODES = {"number", "label", "label_color", "number_label"}


def project_public_state(session: dict[str, Any]) -> dict[str, Any]:
    return {
        "session": {
            "id": session["id"],
            "name": session["name"],
        },
        "scene": project_scene(session),
        "trackers": project_trackers(session.get("trackers", [])),
        "initiative": project_initiative(session.get("initiative", {})),
    }


def project_scene(session: dict[str, Any]) -> dict[str, Any] | None:
    scene_id = session.get("active_scene_id")
    if not scene_id:
        return None

    scene = next((item for item in session.get("scenes", []) if item.get("id") == scene_id), None)
    if not scene or not scene.get("is_public", True):
        return None

    projected: dict[str, Any] = {
        "id": scene["id"],
        "title": scene.get("title", ""),
        "description": scene.get("description", ""),
    }

    asset_id = scene.get("image_asset_id")
    asset = find_asset(session, asset_id)
    if asset:
        projected["image"] = {
            "id": asset["id"],
            "url": asset["public_url"],
        }

    return projected


def find_asset(session: dict[str, Any], asset_id: str | None) -> dict[str, Any] | None:
    if not asset_id:
        return None
    return next((item for item in session.get("assets", []) if item.get("id") == asset_id), None)


def project_trackers(trackers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [project_tracker(tracker) for tracker in trackers if isinstance(tracker, dict) and tracker.get("visible", False)]


def project_tracker(tracker: dict[str, Any]) -> dict[str, Any]:
    display_mode = normalize_tracker_display_mode(tracker.get("display_mode"))
    projected = {
        "id": tracker.get("id", ""),
        "label": tracker.get("label", ""),
        "display_mode": display_mode,
        "display": {},
    }

    value = safe_int(tracker.get("value"), 0)
    if display_mode == "number":
        projected["display"] = {"value": value}
        return projected

    label, color = tracker_label_and_color(tracker, value)
    if display_mode == "label":
        projected["display"] = {"label": label}
    elif display_mode == "label_color":
        projected["display"] = {"label": label, "color": color}
    else:
        projected["display"] = {"value": value, "label": label}

    return projected


def normalize_tracker_display_mode(display_mode: Any) -> str:
    if display_mode in TRACKER_DISPLAY_MODES:
        return display_mode
    return "number"


def tracker_label_and_color(tracker: dict[str, Any], value: int) -> tuple[str, str | None]:
    named_values = normalized_named_values(tracker.get("named_values", []))
    if not named_values:
        return str(value), None

    interval = max(safe_int(tracker.get("interval"), 1), 1)
    min_value = safe_int(tracker.get("min_value"), 1)
    index = max((value - min_value) // interval, 0)
    index = min(index, len(named_values) - 1)
    item = named_values[index]
    return item["label"], item.get("color") or derived_tracker_color(tracker.get("color_scale"), index, len(named_values))


def normalized_named_values(named_values: Any) -> list[dict[str, str | None]]:
    if not isinstance(named_values, list):
        return []

    normalized = []
    for item in named_values:
        if not isinstance(item, dict):
            continue
        label = str(item.get("label", "")).strip()
        if not label:
            continue
        color = item.get("color")
        normalized.append({"label": label, "color": color if isinstance(color, str) and color.strip() else None})
    return normalized


def derived_tracker_color(color_scale: Any, index: int, count: int) -> str:
    start, end = COLOR_SCALE_ENDPOINTS.get(color_scale, COLOR_SCALE_ENDPOINTS["green_to_red"])
    if count <= 1:
        return start
    ratio = index / (count - 1)
    return interpolate_hex_color(start, end, ratio)


def interpolate_hex_color(start: str, end: str, ratio: float) -> str:
    start_rgb = hex_to_rgb(start)
    end_rgb = hex_to_rgb(end)
    mixed = tuple(round(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * ratio) for i in range(3))
    return "#{:02x}{:02x}{:02x}".format(*mixed)


def hex_to_rgb(color: str) -> tuple[int, int, int]:
    stripped = color.lstrip("#")
    return int(stripped[0:2], 16), int(stripped[2:4], 16), int(stripped[4:6], 16)


def safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def project_initiative(initiative: dict[str, Any]) -> dict[str, Any] | None:
    if not initiative.get("visible", False):
        return None

    entries = [
        project_initiative_entry(entry, initiative)
        for entry in sorted(
            initiative.get("entries", []),
            key=lambda item: (-int(item.get("initiative", 0)), int(item.get("sort_order", 0))),
        )
        if entry.get("player_visibility") != "hidden"
    ]
    return {"entries": entries}


def project_initiative_entry(entry: dict[str, Any], initiative: dict[str, Any]) -> dict[str, Any]:
    is_current = entry.get("id") == initiative.get("current_entry_id")
    if entry.get("player_visibility") == "visible":
        return {
            "id": entry["id"],
            "kind": entry.get("kind", "creature"),
            "name": "???",
            "initiative": entry.get("initiative"),
            "is_current": is_current,
        }

    projected = {
        "id": entry["id"],
        "kind": entry.get("kind", "creature"),
        "name": entry.get("name", ""),
        "initiative": entry.get("initiative"),
        "is_current": is_current,
    }

    if entry.get("kind") != "creature":
        return projected

    if entry.get("ac_revealed"):
        projected["ac"] = entry.get("ac")

    hp = project_hp(entry, initiative.get("hp_number_display", "current_max"))
    if hp:
        projected["hp"] = hp

    return projected


def project_hp(entry: dict[str, Any], hp_number_display: str) -> dict[str, Any] | None:
    visibility = entry.get("hp_visibility", "none")
    if visibility == "none":
        return None

    current = int(entry.get("hp_current", 0))
    maximum = int(entry.get("hp_max", 0))
    if visibility == "numbers":
        hp = {"mode": "numbers", "current": current}
        if hp_number_display == "current_max":
            hp["max"] = maximum
        return hp

    if visibility == "vibe":
        return {"mode": "vibe", "status": hp_vibe(current, maximum)}

    return None


def hp_vibe(current: int, maximum: int) -> str:
    if maximum <= 0:
        return "bloodied"
    ratio = current / maximum
    if ratio >= 0.7:
        return "healthy"
    if ratio >= 0.5:
        return "injured"
    return "bloodied"
