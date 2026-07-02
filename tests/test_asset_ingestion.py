from io import BytesIO
from pathlib import Path

import app.assets as assets
from app.state import get_session, session_path


PNG_BYTES = b"\x89PNG\r\n\x1a\nfake-image"


def test_api_upload_registers_app_managed_asset(client):
    response = client.post(
        "/api/gm/session/upload-demo/assets/upload",
        data={
            "display_name": "Elevator",
            "image": (BytesIO(PNG_BYTES), "elevator.png"),
        },
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    asset = response.json["asset"]
    assert asset["display_name"] == "Elevator"
    assert asset["public_url"].startswith("/assets/upload-demo/asset-")
    assert asset["public_url"].endswith(".png")

    session = get_session("upload-demo")
    private_asset = session["assets"][0]
    assert private_asset["filename"].startswith("asset-")
    assert private_asset["source"]["original_filename"] == "elevator.png"
    assert (session_path("upload-demo") / "assets" / private_asset["filename"]).is_file()


def test_uploaded_asset_can_be_selected_for_scene_and_served(client):
    upload = client.post(
        "/api/gm/session/serve-demo/assets/upload",
        data={"image": (BytesIO(PNG_BYTES), "elevator.png")},
        content_type="multipart/form-data",
    )
    asset_id = upload.json["asset"]["id"]

    scene = client.post(
        "/api/gm/session/serve-demo/scene",
        json={"title": "Elevator", "description": "Going down.", "image_asset_id": asset_id},
    )
    public_state = client.get("/api/s/serve-demo/public").json
    image_response = client.get(public_state["scene"]["image"]["url"])

    assert scene.status_code == 200
    assert public_state["scene"]["image"]["id"] == asset_id
    assert image_response.status_code == 200
    assert image_response.data == PNG_BYTES


def test_upload_rejects_unsupported_file_type(client):
    response = client.post(
        "/api/gm/session/upload-bad/assets/upload",
        data={"image": (BytesIO(b"not an image"), "notes.txt")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    assert response.json["error"]["code"] == "invalid_asset_upload"


def test_url_download_registers_asset_without_exposing_source_url(client, monkeypatch):
    class FakeHeaders:
        def get_content_type(self):
            return "image/png"

    class FakeResponse:
        headers = FakeHeaders()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def geturl(self):
            return "https://cdn.example.test/elevator.png"

        def read(self):
            return PNG_BYTES

    monkeypatch.setattr(assets, "urlopen", lambda request, timeout: FakeResponse())

    response = client.post(
        "/api/gm/session/download-demo/assets/download",
        json={"url": "https://example.test/elevator.png", "display_name": "Elevator"},
    )

    assert response.status_code == 200
    asset = response.json["asset"]
    assert asset["display_name"] == "Elevator"
    assert "https://example.test/elevator.png" not in str(asset)

    session = get_session("download-demo")
    private_asset = session["assets"][0]
    assert private_asset["source"]["original_url"] == "https://example.test/elevator.png"


def test_duplicate_download_reuses_existing_asset(client, monkeypatch):
    class FakeHeaders:
        def get_content_type(self):
            return "image/png"

    class FakeResponse:
        headers = FakeHeaders()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def geturl(self):
            return "https://cdn.example.test/elevator.png"

        def read(self):
            return PNG_BYTES

    monkeypatch.setattr(assets, "urlopen", lambda request, timeout: FakeResponse())

    first = client.post(
        "/api/gm/session/dupe-demo/assets/download",
        json={"url": "https://example.test/elevator.png", "display_name": "Elevator"},
    )
    second = client.post(
        "/api/gm/session/dupe-demo/assets/download",
        json={"url": "https://example.test/elevator.png", "display_name": "Elevator Again"},
    )

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json["asset"]["id"] == second.json["asset"]["id"]
    assert len(get_session("dupe-demo")["assets"]) == 1


def test_upload_preview_warns_about_duplicate_asset(client):
    upload = client.post(
        "/api/gm/session/upload-preview/assets/upload",
        data={
            "display_name": "Elevator",
            "image": (BytesIO(PNG_BYTES), "elevator.png"),
        },
        content_type="multipart/form-data",
    )

    preview = client.post(
        "/api/gm/session/upload-preview/assets/upload/preview",
        data={"image": (BytesIO(PNG_BYTES), "elevator-copy.png")},
        content_type="multipart/form-data",
    )

    assert upload.status_code == 200
    assert preview.status_code == 200
    assert preview.json["duplicate"]["id"] == upload.json["asset"]["id"]
    assert preview.json["duplicate"]["display_name"] == "Elevator"


def test_download_preview_warns_about_duplicate_asset(client, monkeypatch):
    class FakeHeaders:
        def get_content_type(self):
            return "image/png"

    class FakeResponse:
        headers = FakeHeaders()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def geturl(self):
            return "https://cdn.example.test/elevator.png"

        def read(self):
            return PNG_BYTES

    monkeypatch.setattr(assets, "urlopen", lambda request, timeout: FakeResponse())

    download = client.post(
        "/api/gm/session/download-preview/assets/download",
        json={"url": "https://example.test/elevator.png", "display_name": "Elevator"},
    )
    preview = client.post(
        "/api/gm/session/download-preview/assets/download/preview",
        json={"url": "https://example.test/elevator.png"},
    )

    assert download.status_code == 200
    assert preview.status_code == 200
    assert preview.json["duplicate"]["id"] == download.json["asset"]["id"]


def test_gm_upload_form_shows_registered_asset(client):
    response = client.post(
        "/s/form-upload/gm/assets/upload",
        data={
            "display_name": "Elevator",
            "image": (BytesIO(PNG_BYTES), "elevator.png"),
        },
        content_type="multipart/form-data",
        follow_redirects=True,
    )
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Elevator" in body
    assert "asset-" in body


def test_gm_session_page_includes_duplicate_warning_script(client):
    response = client.get("/s/script-demo/gm")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "gm-session.js" in body
    assert "data-preview-url" in body
