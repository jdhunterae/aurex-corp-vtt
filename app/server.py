"""Minimal Flask server entrypoint for Aurex Corp VTT."""

from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, url_for

from app.assets import AssetIngestionError, download_image_asset, upload_image_asset
from app.projection import project_public_state
from app.scenes import SceneValidationError, update_scene
from app.state import get_session, load_or_create_session, session_path


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        return redirect(url_for("gm_home"))

    @app.get("/gm")
    def gm_home():
        load_or_create_session()
        return render_template("gm_home.html")

    @app.get("/s/<session_id>")
    @app.get("/s/<session_id>/")
    def session_home(session_id: str):
        return redirect(url_for("player_view", session_id=session_id))

    @app.get("/s/<session_id>/gm")
    def gm_session(session_id: str):
        session = get_session(session_id)
        public_state = project_public_state(session)
        return render_template("gm_session.html", public_state=public_state, session=session)

    @app.post("/s/<session_id>/gm/scene")
    def gm_scene_update(session_id: str):
        session = get_session(session_id)
        try:
            update_scene(
                session,
                title=request.form.get("title", ""),
                description=request.form.get("description", ""),
                image_asset_id=request.form.get("image_asset_id"),
            )
        except SceneValidationError as error:
            public_state = project_public_state(session)
            return (
                render_template(
                    "gm_session.html",
                    error_message=str(error),
                    public_state=public_state,
                    session=session,
                ),
                400,
            )
        return redirect(url_for("gm_session", session_id=session_id))

    @app.post("/s/<session_id>/gm/assets/upload")
    def gm_asset_upload(session_id: str):
        session = get_session(session_id)
        try:
            upload_image_asset(
                session,
                request.files.get("image"),
                display_name=request.form.get("display_name"),
                duplicate_choice=request.form.get("duplicate_choice", "copy"),
            )
        except AssetIngestionError as error:
            public_state = project_public_state(session)
            return (
                render_template(
                    "gm_session.html",
                    error_message=str(error),
                    public_state=public_state,
                    session=session,
                ),
                400,
            )
        return redirect(url_for("gm_session", session_id=session_id))

    @app.post("/s/<session_id>/gm/assets/download")
    def gm_asset_download(session_id: str):
        session = get_session(session_id)
        try:
            download_image_asset(
                session,
                url=request.form.get("url", ""),
                display_name=request.form.get("display_name"),
                duplicate_choice=request.form.get("duplicate_choice", "reuse"),
            )
        except AssetIngestionError as error:
            public_state = project_public_state(session)
            return (
                render_template(
                    "gm_session.html",
                    error_message=str(error),
                    public_state=public_state,
                    session=session,
                ),
                400,
            )
        return redirect(url_for("gm_session", session_id=session_id))

    @app.get("/s/<session_id>/player")
    def player_view(session_id: str):
        session = get_session(session_id)
        public_state = project_public_state(session)
        public_state_url = f"/api/s/{session_id}/public"
        return render_template(
            "player.html",
            public_state=public_state,
            public_state_url=public_state_url,
            session_id=session["id"],
        )

    @app.get("/healthz")
    def healthz():
        return jsonify({"status": "ok"})

    @app.get("/api/s/<session_id>/public")
    def public_state(session_id: str):
        return jsonify(project_public_state(get_session(session_id)))

    @app.post("/api/gm/session/<session_id>/scene")
    def api_scene_update(session_id: str):
        session = get_session(session_id)
        payload = request.get_json(silent=True) or {}
        try:
            scene = update_scene(
                session,
                title=payload.get("title", ""),
                description=payload.get("description", ""),
                image_asset_id=payload.get("image_asset_id"),
            )
        except SceneValidationError as error:
            return jsonify({"error": {"code": "invalid_scene_update", "message": str(error)}}), 400
        return jsonify({"scene": scene, "autosaved": False})

    @app.post("/api/gm/session/<session_id>/assets/upload")
    def api_asset_upload(session_id: str):
        session = get_session(session_id)
        try:
            asset = upload_image_asset(
                session,
                request.files.get("image"),
                display_name=request.form.get("display_name"),
                duplicate_choice=request.form.get("duplicate_choice", "copy"),
            )
        except AssetIngestionError as error:
            return jsonify({"error": {"code": "invalid_asset_upload", "message": str(error)}}), 400
        return jsonify({"asset": public_asset_response(asset), "autosaved": False})

    @app.post("/api/gm/session/<session_id>/assets/download")
    def api_asset_download(session_id: str):
        session = get_session(session_id)
        payload = request.get_json(silent=True) or {}
        try:
            asset = download_image_asset(
                session,
                url=payload.get("url", ""),
                display_name=payload.get("display_name"),
                duplicate_choice=payload.get("duplicate_choice", "reuse"),
            )
        except AssetIngestionError as error:
            return jsonify({"error": {"code": "invalid_asset_download", "message": str(error)}}), 400
        return jsonify({"asset": public_asset_response(asset), "autosaved": False})

    @app.get("/assets/<session_id>/<asset_filename>")
    def serve_asset(session_id: str, asset_filename: str):
        asset_dir = session_path(session_id) / "assets"
        return send_from_directory(asset_dir, Path(asset_filename).name)

    @app.errorhandler(404)
    def not_found(error):
        return render_template("error.html", status_code=404, title="Page not found"), 404

    return app


app = create_app()


def public_asset_response(asset):
    return {
        "id": asset["id"],
        "kind": asset["kind"],
        "display_name": asset["display_name"],
        "mime_type": asset["mime_type"],
        "public_url": asset["public_url"],
    }
