from app.state import get_session


def test_player_page_renders_public_scene(client):
    session = get_session("scene-demo")
    session.update(
        {
            "active_scene_id": "scene-1",
            "assets": [
                {
                    "id": "asset-1",
                    "public_url": "/assets/scene-demo/asset-1.png",
                    "filename": "private-file-name.png",
                    "source": {"original_url": "https://example.test/private.png"},
                }
            ],
            "scenes": [
                {
                    "id": "scene-1",
                    "title": "Cavern Entrance",
                    "description": "A damp stone opening descends into darkness.",
                    "image_asset_id": "asset-1",
                    "gm_notes": "Ambush if they make noise.",
                }
            ],
        }
    )

    response = client.get("/s/scene-demo/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Cavern Entrance" in body
    assert "A damp stone opening descends into darkness." in body
    assert 'src="/assets/scene-demo/asset-1.png"' in body
    assert "Ambush if they make noise." not in body
    assert "private-file-name.png" not in body
    assert "https://example.test/private.png" not in body
