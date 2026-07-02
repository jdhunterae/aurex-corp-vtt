"""Scene update helpers."""

from __future__ import annotations

from typing import Any

ACTIVE_SCENE_ID = "scene-active"


class SceneValidationError(ValueError):
    pass


def update_scene(
    session: dict[str, Any],
    *,
    title: str,
    description: str,
    image_asset_id: str | None,
) -> dict[str, Any]:
    image_asset_id = normalize_asset_id(image_asset_id)
    validate_scene_image_asset(session, image_asset_id)

    scene = get_or_create_active_scene(session)
    scene["title"] = title.strip()
    scene["description"] = description.strip()
    scene["image_asset_id"] = image_asset_id
    scene["is_public"] = True
    return scene


def get_or_create_active_scene(session: dict[str, Any]) -> dict[str, Any]:
    active_scene_id = session.get("active_scene_id") or ACTIVE_SCENE_ID
    session["active_scene_id"] = active_scene_id

    scene = next((item for item in session.get("scenes", []) if item.get("id") == active_scene_id), None)
    if scene is None:
        scene = {
            "id": active_scene_id,
            "title": "",
            "description": "",
            "image_asset_id": None,
            "gm_notes": "",
            "is_public": True,
        }
        session.setdefault("scenes", []).append(scene)
    return scene


def normalize_asset_id(image_asset_id: str | None) -> str | None:
    if image_asset_id is None:
        return None
    stripped = image_asset_id.strip()
    return stripped or None


def validate_scene_image_asset(session: dict[str, Any], image_asset_id: str | None) -> None:
    if image_asset_id is None:
        return
    if image_asset_id.startswith(("http://", "https://")) or "/" in image_asset_id or "\\" in image_asset_id:
        raise SceneValidationError("Scene image must reference an app-managed asset ID.")
    if not any(asset.get("id") == image_asset_id for asset in session.get("assets", [])):
        raise SceneValidationError("Scene image asset does not exist in this session.")
