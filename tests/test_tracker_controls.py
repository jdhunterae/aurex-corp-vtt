from app.state import get_session


def tracker_payload(**overrides):
    payload = {
        "label": "Security Alert",
        "value": 1,
        "visible": True,
        "mode": "bounded",
        "min_value": 1,
        "max_value": 15,
        "interval": 3,
        "display_mode": "label_color",
        "color_scale": "green_to_red",
        "named_values": [{"label": "Green"}, {"label": "Yellow"}, {"label": "Red"}],
    }
    payload.update(overrides)
    return payload


def test_api_creates_tracker(client):
    response = client.post("/api/gm/session/tracker-create/trackers", json=tracker_payload())

    assert response.status_code == 200
    assert response.json["autosaved"] is False
    tracker = response.json["tracker"]
    assert tracker["id"].startswith("tracker-")
    assert tracker["label"] == "Security Alert"
    assert tracker["step_controls"] == [-2, -1, 1, 2]

    public_response = client.get("/api/s/tracker-create/public")
    assert public_response.json["trackers"][0]["display"] == {
        "label": "Green",
        "color": "#2f9e44",
    }


def test_api_updates_tracker(client):
    create = client.post("/api/gm/session/tracker-update/trackers", json=tracker_payload())
    tracker_id = create.json["tracker"]["id"]

    response = client.patch(
        f"/api/gm/session/tracker-update/trackers/{tracker_id}",
        json=tracker_payload(label="Torch Timer", value=6, display_mode="number_label"),
    )

    assert response.status_code == 200
    assert response.json["autosaved"] is False
    assert response.json["tracker"]["label"] == "Torch Timer"
    assert response.json["tracker"]["value"] == 6

    public_response = client.get("/api/s/tracker-update/public")
    assert public_response.json["trackers"][0]["display"] == {"value": 6, "label": "Yellow"}


def test_api_adjusts_tracker(client):
    create = client.post("/api/gm/session/tracker-adjust/trackers", json=tracker_payload(value=5))
    tracker_id = create.json["tracker"]["id"]

    response = client.post(f"/api/gm/session/tracker-adjust/trackers/{tracker_id}/adjust", json={"delta": 2})

    assert response.status_code == 200
    assert response.json["tracker"]["value"] == 7


def test_api_rejects_invalid_tracker(client):
    response = client.post(
        "/api/gm/session/tracker-invalid/trackers",
        json=tracker_payload(label="", value=99),
    )

    assert response.status_code == 400
    assert response.json["error"]["code"] == "invalid_tracker_update"


def test_api_rejects_adjustment_outside_bounds(client):
    create = client.post("/api/gm/session/tracker-bounds/trackers", json=tracker_payload(value=15))
    tracker_id = create.json["tracker"]["id"]

    response = client.post(f"/api/gm/session/tracker-bounds/trackers/{tracker_id}/adjust", json={"delta": 1})

    assert response.status_code == 400
    assert response.json["error"]["code"] == "invalid_tracker_update"


def test_gm_tracker_form_creates_tracker(client):
    response = client.post(
        "/s/form-tracker/gm/trackers",
        data={
            "label": "Security Alert",
            "value": "1",
            "visible": "on",
            "mode": "bounded",
            "min_value": "1",
            "max_value": "15",
            "interval": "3",
            "display_mode": "label_color",
            "color_scale": "green_to_red",
            "named_values": "Green\nYellow\nRed",
            "step_controls": "",
        },
        follow_redirects=True,
    )
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Security Alert" in body
    assert "Update Tracker" in body
    assert "+2" in body


def test_gm_tracker_form_renders_validation_error(client):
    response = client.post(
        "/s/form-tracker-error/gm/trackers",
        data={
            "label": "",
            "value": "1",
            "mode": "bounded",
            "min_value": "1",
            "max_value": "15",
            "interval": "3",
            "display_mode": "number",
            "color_scale": "green_to_red",
        },
    )
    body = response.get_data(as_text=True)

    assert response.status_code == 400
    assert "Tracker label is required." in body


def test_gm_tracker_adjust_form_updates_value(client):
    session = get_session("form-tracker-adjust")
    session["trackers"].append(
        {
            "id": "tracker-1",
            "label": "Round",
            "value": 1,
            "visible": True,
            "mode": "unbounded",
            "min_value": 1,
            "interval": 1,
            "display_mode": "number",
            "color_scale": "green_to_red",
            "named_values": [],
            "step_controls": [-1, 1],
            "gm_notes": "",
        }
    )

    response = client.post(
        "/s/form-tracker-adjust/gm/trackers/tracker-1/adjust",
        data={"delta": "1"},
        follow_redirects=True,
    )
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'name="value" type="number" value="2"' in body
