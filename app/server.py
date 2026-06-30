"""Minimal Flask server entrypoint for Aurex Corp VTT."""

from flask import Flask, jsonify, redirect, render_template, url_for


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        return redirect(url_for("gm_home"))

    @app.get("/gm")
    def gm_home():
        return render_template("gm_home.html")

    @app.get("/s/<session_id>")
    def session_home(session_id: str):
        return redirect(url_for("player_view", session_id=session_id))

    @app.get("/s/<session_id>/gm")
    def gm_session(session_id: str):
        return render_template("gm_session.html", session_id=session_id)

    @app.get("/s/<session_id>/player")
    def player_view(session_id: str):
        public_state_url = f"/api/s/{session_id}/public"
        return render_template(
            "player.html",
            public_state_url=public_state_url,
            session_id=session_id,
        )

    @app.get("/healthz")
    def healthz():
        return jsonify({"status": "ok"})

    return app


app = create_app()
