from app.projection import project_public_state
from app.state import get_session


def test_default_public_state_projection(client):
    response = client.get("/api/s/demo-session/public")

    assert response.status_code == 200
    assert response.json == {
        "session": {"id": "demo-session", "name": "demo-session"},
        "scene": None,
        "trackers": [],
        "initiative": None,
    }


def test_projection_excludes_private_fields(client):
    session = get_session("private-demo")
    session.update(
        {
            "name": "Private Demo",
            "active_scene_id": "scene-1",
            "assets": [
                {
                    "id": "asset-1",
                    "public_url": "/assets/private-demo/asset-1.png",
                    "filename": "secret-local-file.png",
                    "source": {"original_url": "https://example.test/private.png"},
                }
            ],
            "scenes": [
                {
                    "id": "scene-1",
                    "title": "Public Scene",
                    "description": "Visible text",
                    "image_asset_id": "asset-1",
                    "gm_notes": "ambush notes",
                }
            ],
            "trackers": [
                {
                    "id": "hidden-tracker",
                    "label": "Hidden Tracker",
                    "visible": False,
                    "value": 99,
                }
            ],
            "initiative": {
                "visible": True,
                "current_entry_id": "visible-entry",
                "hp_number_display": "current_max",
                "entries": [
                    {
                        "id": "hidden-entry",
                        "kind": "creature",
                        "name": "Hidden Goblin",
                        "initiative": 20,
                        "player_visibility": "hidden",
                        "ac": 13,
                        "hp_current": 7,
                        "hp_max": 7,
                        "gm_notes": "hidden note",
                    },
                    {
                        "id": "visible-entry",
                        "kind": "creature",
                        "name": "Unknown Goblin",
                        "initiative": 15,
                        "player_visibility": "visible",
                        "ac": 13,
                        "hp_current": 7,
                        "hp_max": 7,
                    },
                ],
            },
            "gm": {"notes": "private gm note"},
        }
    )

    projected = project_public_state(session)
    text = str(projected)

    assert projected["session"] == {"id": "private-demo", "name": "Private Demo"}
    assert projected["scene"]["image"] == {
        "id": "asset-1",
        "url": "/assets/private-demo/asset-1.png",
    }
    assert projected["trackers"] == []
    assert projected["initiative"]["entries"] == [
        {
            "id": "visible-entry",
            "kind": "creature",
            "name": "???",
            "initiative": 15,
            "is_current": True,
        }
    ]

    for forbidden in (
        "gm_notes",
        "ambush notes",
        "secret-local-file",
        "original_url",
        "private.png",
        "Hidden Tracker",
        "Hidden Goblin",
        "hidden note",
        "private gm note",
    ):
        assert forbidden not in text


def test_projection_supports_scene_asset_tracker_and_known_initiative(client):
    session = get_session("full-demo")
    session.update(
        {
            "active_scene_id": "scene-1",
            "assets": [{"id": "asset-1", "public_url": "/assets/full-demo/asset-1.png"}],
            "scenes": [
                {
                    "id": "scene-1",
                    "title": "Hall",
                    "description": "A long hall.",
                    "image_asset_id": "asset-1",
                }
            ],
            "trackers": [
                {
                    "id": "alert",
                    "label": "Alert",
                    "visible": True,
                    "value": 5,
                    "min_value": 1,
                    "interval": 3,
                    "display_mode": "label_color",
                    "named_values": [
                        {"label": "Green", "color": "#00ff00"},
                        {"label": "Yellow", "color": "#ffff00"},
                    ],
                }
            ],
            "initiative": {
                "visible": True,
                "current_entry_id": "known",
                "hp_number_display": "current_max",
                "entries": [
                    {
                        "id": "known",
                        "kind": "creature",
                        "name": "Knight",
                        "initiative": 12,
                        "sort_order": 0,
                        "player_visibility": "known",
                        "ac": 16,
                        "ac_revealed": True,
                        "hp_current": 20,
                        "hp_max": 56,
                        "hp_visibility": "numbers",
                    }
                ],
            },
        }
    )

    projected = project_public_state(session)

    assert projected["scene"] == {
        "id": "scene-1",
        "title": "Hall",
        "description": "A long hall.",
        "image": {"id": "asset-1", "url": "/assets/full-demo/asset-1.png"},
    }
    assert projected["trackers"][0]["display"] == {
        "label": "Yellow",
        "color": "#ffff00",
    }
    assert projected["initiative"]["entries"][0]["ac"] == 16
    assert projected["initiative"]["entries"][0]["hp"] == {
        "mode": "numbers",
        "current": 20,
        "max": 56,
    }
