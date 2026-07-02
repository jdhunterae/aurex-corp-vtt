from app.projection import project_public_state
from app.state import get_session


def test_tracker_projection_supports_all_display_modes(client):
    session = get_session("tracker-display-modes")
    session["trackers"] = [
        {
            "id": "round",
            "label": "Round",
            "visible": True,
            "value": "3",
            "display_mode": "number",
        },
        {
            "id": "alert-label",
            "label": "Alert Label",
            "visible": True,
            "value": 5,
            "min_value": 1,
            "interval": 3,
            "display_mode": "label",
            "named_values": [{"label": "Green"}, {"label": "Yellow"}],
        },
        {
            "id": "alert-color",
            "label": "Alert Color",
            "visible": True,
            "value": 9,
            "min_value": 1,
            "interval": 3,
            "display_mode": "label_color",
            "color_scale": "green_to_red",
            "named_values": [{"label": "Green"}, {"label": "Yellow"}, {"label": "Red"}],
        },
        {
            "id": "torch",
            "label": "Torch",
            "visible": True,
            "value": 2,
            "min_value": 0,
            "interval": 2,
            "display_mode": "number_label",
            "named_values": [{"label": "Low"}, {"label": "High"}],
        },
    ]

    projected = project_public_state(session)

    assert projected["trackers"] == [
        {
            "id": "round",
            "label": "Round",
            "display_mode": "number",
            "display": {"value": 3},
        },
        {
            "id": "alert-label",
            "label": "Alert Label",
            "display_mode": "label",
            "display": {"label": "Yellow"},
        },
        {
            "id": "alert-color",
            "label": "Alert Color",
            "display_mode": "label_color",
            "display": {"label": "Red", "color": "#c92a2a"},
        },
        {
            "id": "torch",
            "label": "Torch",
            "display_mode": "number_label",
            "display": {"value": 2, "label": "High"},
        },
    ]


def test_tracker_projection_prefers_explicit_named_value_color(client):
    session = get_session("tracker-explicit-color")
    session["trackers"] = [
        {
            "id": "alert",
            "label": "Alert",
            "visible": True,
            "value": 4,
            "min_value": 1,
            "interval": 3,
            "display_mode": "label_color",
            "color_scale": "green_to_red",
            "named_values": [
                {"label": "Green", "color": "#00ff00"},
                {"label": "Yellow", "color": "#ffff00"},
            ],
        }
    ]

    projected = project_public_state(session)

    assert projected["trackers"][0]["display"] == {"label": "Yellow", "color": "#ffff00"}


def test_tracker_projection_excludes_hidden_and_private_fields(client):
    session = get_session("tracker-private-fields")
    session["trackers"] = [
        {
            "id": "hidden",
            "label": "Hidden Tracker",
            "visible": False,
            "value": 99,
            "gm_notes": "secret tracker note",
            "source_url": "https://example.test/secret",
        },
        {
            "id": "visible",
            "label": "Visible Tracker",
            "visible": True,
            "value": 1,
            "display_mode": "number",
            "gm_notes": "visible tracker secret",
            "source_url": "https://example.test/visible-secret",
            "local_path": "/tmp/secret",
        },
    ]

    projected = project_public_state(session)
    text = str(projected)

    assert projected["trackers"] == [
        {
            "id": "visible",
            "label": "Visible Tracker",
            "display_mode": "number",
            "display": {"value": 1},
        }
    ]
    for forbidden in (
        "Hidden Tracker",
        "secret tracker note",
        "visible tracker secret",
        "source_url",
        "example.test",
        "local_path",
        "/tmp/secret",
    ):
        assert forbidden not in text


def test_tracker_projection_handles_malformed_optional_fields(client):
    session = get_session("tracker-malformed")
    session["trackers"] = [
        {
            "id": "bad-number",
            "label": "Bad Number",
            "visible": True,
            "value": "not-a-number",
            "display_mode": "unknown",
        },
        {
            "id": "bad-label",
            "label": "Bad Label",
            "visible": True,
            "value": "not-a-number",
            "min_value": "bad-min",
            "interval": "bad-interval",
            "display_mode": "label_color",
            "color_scale": "unknown",
            "named_values": ["bad item", {"label": ""}, {"label": "Fallback"}],
        },
    ]

    projected = project_public_state(session)

    assert projected["trackers"] == [
        {
            "id": "bad-number",
            "label": "Bad Number",
            "display_mode": "number",
            "display": {"value": 0},
        },
        {
            "id": "bad-label",
            "label": "Bad Label",
            "display_mode": "label_color",
            "display": {"label": "Fallback", "color": "#2f9e44"},
        },
    ]
