from app.state import get_session


def test_player_page_renders_public_trackers(client):
    session = get_session("tracker-display")
    session["trackers"] = [
        {
            "id": "round",
            "label": "Round",
            "visible": True,
            "value": 3,
            "display_mode": "number",
        },
        {
            "id": "alert",
            "label": "Alert",
            "visible": True,
            "value": 4,
            "min_value": 1,
            "interval": 3,
            "display_mode": "label_color",
            "color_scale": "green_to_red",
            "named_values": [{"label": "Green"}, {"label": "Yellow"}],
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
        {
            "id": "weather",
            "label": "Weather",
            "visible": True,
            "value": 0,
            "display_mode": "label",
            "named_values": [{"label": "Calm"}],
        },
    ]

    response = client.get("/s/tracker-display/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'aria-label="Public trackers"' in body
    assert 'data-tracker-id="round"' in body
    assert "Round" in body
    assert ">3<" in body
    assert 'data-tracker-id="alert"' in body
    assert "Alert" in body
    assert "Yellow" in body
    assert "background-color: #c92a2a" in body
    assert 'data-tracker-id="torch"' in body
    assert "Torch" in body
    assert "High" in body
    assert 'data-tracker-id="weather"' in body
    assert "Weather" in body
    assert "Calm" in body


def test_player_page_does_not_render_empty_tracker_placeholder(client):
    response = client.get("/s/no-trackers/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Public trackers" not in body
    assert "player-tracker" not in body


def test_player_page_excludes_hidden_and_private_tracker_fields(client):
    session = get_session("tracker-private-display")
    session["trackers"] = [
        {
            "id": "hidden",
            "label": "Hidden Tracker",
            "visible": False,
            "value": 99,
            "gm_notes": "hidden tracker note",
            "local_path": "/tmp/hidden",
        },
        {
            "id": "visible",
            "label": "Visible Tracker",
            "visible": True,
            "value": 5,
            "display_mode": "number",
            "gm_notes": "visible tracker note",
            "source_url": "https://example.test/private",
        },
    ]

    response = client.get("/s/tracker-private-display/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Visible Tracker" in body
    for forbidden in (
        "Hidden Tracker",
        "hidden tracker note",
        "visible tracker note",
        "local_path",
        "/tmp/hidden",
        "source_url",
        "example.test/private",
    ):
        assert forbidden not in body
