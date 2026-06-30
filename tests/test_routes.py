def test_health_route(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_root_redirects_to_gm(client):
    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["location"] == "/gm"


def test_gm_routes_return_page_shells(client):
    home = client.get("/gm")
    session = client.get("/s/demo-session/gm")

    assert home.status_code == 200
    assert "GM Interface" in home.get_data(as_text=True)
    assert session.status_code == 200
    assert "GM Session" in session.get_data(as_text=True)


def test_player_routes_return_passive_page_shell(client):
    response = client.get("/s/demo-session/player")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert 'data-session-id="demo-session"' in body
    assert 'data-public-state-url="/api/s/demo-session/public"' in body
    assert "Controls" not in body
    assert "gm_notes" not in body


def test_bare_session_route_redirects_to_player(client):
    response = client.get("/s/demo-session")
    response_with_slash = client.get("/s/demo-session/")

    assert response.status_code == 302
    assert response.headers["location"] == "/s/demo-session/player"
    assert response_with_slash.status_code == 302
    assert response_with_slash.headers["location"] == "/s/demo-session/player"


def test_not_found_uses_project_error_page(client):
    response = client.get("/missing-page")
    body = response.get_data(as_text=True)

    assert response.status_code == 404
    assert "Page not found" in body
    assert "Return to GM home" in body
