from app.state import get_session


def test_api_updates_scene_title_and_description(client):
    response = client.post(
        "/api/gm/session/scene-controls/scene",
        json={
            "title": "Cavern Entrance",
            "description": "A damp opening.",
            "image_asset_id": None,
        },
    )

    assert response.status_code == 200
    assert response.json["scene"]["title"] == "Cavern Entrance"
    assert response.json["scene"]["description"] == "A damp opening."

    public_response = client.get("/api/s/scene-controls/public")
    assert public_response.json["scene"]["title"] == "Cavern Entrance"
    assert public_response.json["scene"]["description"] == "A damp opening."


def test_api_selects_existing_scene_asset(client):
    session = get_session("scene-asset")
    session["assets"].append({"id": "asset-1", "public_url": "/assets/scene-asset/asset-1.png"})

    response = client.post(
        "/api/gm/session/scene-asset/scene",
        json={
            "title": "Hall",
            "description": "Long shadows.",
            "image_asset_id": "asset-1",
        },
    )

    assert response.status_code == 200
    public_response = client.get("/api/s/scene-asset/public")
    assert public_response.json["scene"]["image"] == {
        "id": "asset-1",
        "url": "/assets/scene-asset/asset-1.png",
    }


def test_api_rejects_external_scene_image_reference(client):
    response = client.post(
        "/api/gm/session/bad-scene/scene",
        json={
            "title": "Bad",
            "description": "Bad",
            "image_asset_id": "https://example.test/image.png",
        },
    )

    assert response.status_code == 400
    assert response.json["error"]["code"] == "invalid_scene_update"


def test_api_rejects_missing_scene_asset(client):
    response = client.post(
        "/api/gm/session/missing-asset/scene",
        json={
            "title": "Bad",
            "description": "Bad",
            "image_asset_id": "asset-missing",
        },
    )

    assert response.status_code == 400
    assert response.json["error"]["code"] == "invalid_scene_update"


def test_gm_scene_form_updates_scene(client):
    response = client.post(
        "/s/form-scene/gm/scene",
        data={
            "title": "Bridge",
            "description": "The bridge sways.",
            "image_asset_id": "",
        },
        follow_redirects=True,
    )
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Bridge" in body
    assert "The bridge sways." in body
