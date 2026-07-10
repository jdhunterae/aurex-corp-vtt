from app.state import get_session


def test_player_page_loads_public_refresh_script(client):
    response = client.get("/s/refresh-demo/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'data-public-state-url="/api/s/refresh-demo/public"' in body
    assert 'data-refresh-interval-ms="5000"' in body
    assert 'src="/static/player-display.js"' in body
    assert "/api/gm/" not in body


def test_player_page_includes_non_interrupting_refresh_warning(client):
    response = client.get("/s/refresh-warning/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "data-refresh-warning" in body
    assert "data-refresh-countdown" in body
    assert "Display may be out of date." in body
    assert "Retrying in" in body


def test_player_refresh_script_fetches_only_public_state(client):
    response = client.get("/static/player-display.js")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "dataset.publicStateUrl" in body
    assert "window.fetch(publicStateUrl" in body
    assert "/api/gm/" not in body
    assert "gm_notes" not in body


def test_gm_page_does_not_load_player_refresh_script(client):
    response = client.get("/s/refresh-gm/gm")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "player-display.js" not in body
    assert "gm-session.js" in body


def test_player_refresh_markup_excludes_private_state(client):
    session = get_session("refresh-private")
    session["trackers"] = [
        {
            "id": "visible",
            "label": "Visible Tracker",
            "visible": True,
            "value": 5,
            "display_mode": "number",
            "gm_notes": "visible tracker note",
            "source_url": "https://example.test/private",
        }
    ]
    session.update(
        {
            "active_scene_id": "scene-1",
            "assets": [
                {
                    "id": "asset-1",
                    "public_url": "/assets/refresh-private/asset-1.png",
                    "filename": "private-file-name.png",
                    "source": {"original_url": "https://example.test/private.png"},
                }
            ],
            "scenes": [
                {
                    "id": "scene-1",
                    "title": "Public Scene",
                    "description": "Public description.",
                    "image_asset_id": "asset-1",
                    "gm_notes": "private scene note",
                }
            ],
        }
    )

    response = client.get("/s/refresh-private/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Public Scene" in body
    assert "Visible Tracker" in body
    for forbidden in (
        "private scene note",
        "visible tracker note",
        "private-file-name.png",
        "https://example.test/private.png",
        "source_url",
        "example.test/private",
    ):
        assert forbidden not in body
