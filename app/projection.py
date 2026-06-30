"""Public state projection for player-facing routes."""

from __future__ import annotations

from typing import Any


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
    return [project_tracker(tracker) for tracker in trackers if tracker.get("visible", False)]


def project_tracker(tracker: dict[str, Any]) -> dict[str, Any]:
    display_mode = tracker.get("display_mode", "number")
    projected = {
        "id": tracker["id"],
        "label": tracker.get("label", ""),
        "display_mode": display_mode,
        "display": {},
    }

    value = tracker.get("value", 0)
    if display_mode == "number":
        projected["display"] = {"value": value}
        return projected

    label, color = tracker_label_and_color(tracker)
    if display_mode == "label":
        projected["display"] = {"label": label}
    elif display_mode == "label_color":
        projected["display"] = {"label": label, "color": color}
    elif display_mode == "number_label":
        projected["display"] = {"value": value, "label": label}
    else:
        projected["display"] = {"value": value}

    return projected


def tracker_label_and_color(tracker: dict[str, Any]) -> tuple[str, str | None]:
    named_values = tracker.get("named_values", [])
    if not named_values:
        return str(tracker.get("value", 0)), None

    interval = max(int(tracker.get("interval", 1)), 1)
    min_value = int(tracker.get("min_value", 1))
    value = int(tracker.get("value", min_value))
    index = max((value - min_value) // interval, 0)
    index = min(index, len(named_values) - 1)
    item = named_values[index]
    return item.get("label", ""), item.get("color")


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
