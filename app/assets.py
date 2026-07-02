"""Asset ingestion helpers for scene images."""

from __future__ import annotations

import hashlib
import mimetypes
import shutil
import uuid
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app.state import session_path, utc_now_iso

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "tiff", "png", "gif", "webp", "svg"}
ALLOWED_MIME_PREFIXES = ("image/",)
DOWNLOAD_TIMEOUT_SECONDS = 15


class AssetIngestionError(ValueError):
    pass


def upload_image_asset(
    session: dict[str, Any],
    file_storage: FileStorage,
    *,
    display_name: str | None = None,
    duplicate_choice: str = "copy",
) -> dict[str, Any]:
    if not file_storage or not file_storage.filename:
        raise AssetIngestionError("Choose an image file to upload.")

    original_filename = secure_filename(file_storage.filename)
    extension = extension_from_name(original_filename)
    validate_extension(extension)

    data = file_storage.read()
    if not data:
        raise AssetIngestionError("Uploaded image is empty.")

    mime_type = file_storage.mimetype or guess_mime_type(original_filename)
    validate_mime_type(mime_type)

    return register_asset(
        session,
        data=data,
        extension=extension,
        mime_type=mime_type,
        display_name=display_name or Path(original_filename).stem,
        source={"type": "upload", "original_filename": original_filename},
        duplicate_choice=duplicate_choice,
    )


def preview_uploaded_image_duplicate(session: dict[str, Any], file_storage: FileStorage) -> dict[str, Any] | None:
    if not file_storage or not file_storage.filename:
        raise AssetIngestionError("Choose an image file to upload.")

    original_filename = secure_filename(file_storage.filename)
    validate_extension(extension_from_name(original_filename))
    data = file_storage.read()
    if not data:
        raise AssetIngestionError("Uploaded image is empty.")
    validate_mime_type(file_storage.mimetype or guess_mime_type(original_filename))
    return find_duplicate_asset(session, hashlib.sha256(data).hexdigest())


def download_image_asset(
    session: dict[str, Any],
    *,
    url: str,
    display_name: str | None = None,
    duplicate_choice: str = "reuse",
) -> dict[str, Any]:
    downloaded = fetch_image_url(url)

    return register_asset(
        session,
        data=downloaded["data"],
        extension=downloaded["extension"],
        mime_type=downloaded["content_type"],
        display_name=display_name or Path(downloaded["final_url"]).stem or "downloaded-image",
        source={"type": "url", "original_url": url, "final_url": downloaded["final_url"], "imported_at": utc_now_iso()},
        duplicate_choice=duplicate_choice,
    )


def preview_downloaded_image_duplicate(session: dict[str, Any], *, url: str) -> dict[str, Any] | None:
    downloaded = fetch_image_url(url)
    return find_duplicate_asset(session, hashlib.sha256(downloaded["data"]).hexdigest())


def fetch_image_url(url: str) -> dict[str, Any]:
    url = url.strip()
    if not url:
        raise AssetIngestionError("Enter an image URL.")
    if not url.startswith(("http://", "https://")):
        raise AssetIngestionError("Image URL must start with http:// or https://.")

    request = Request(url, headers={"User-Agent": "AurexCorpVTT/0"})
    try:
        with urlopen(request, timeout=DOWNLOAD_TIMEOUT_SECONDS) as response:
            final_url = response.geturl()
            content_type = response.headers.get_content_type()
            data = response.read()
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        raise AssetIngestionError("Image download failed.") from error

    validate_mime_type(content_type)
    extension = extension_from_mime_type(content_type) or extension_from_name(final_url)
    validate_extension(extension)
    if not data:
        raise AssetIngestionError("Downloaded image is empty.")

    return {"content_type": content_type, "data": data, "extension": extension, "final_url": final_url}


def register_asset(
    session: dict[str, Any],
    *,
    data: bytes,
    extension: str,
    mime_type: str,
    display_name: str,
    source: dict[str, Any],
    duplicate_choice: str,
) -> dict[str, Any]:
    digest = hashlib.sha256(data).hexdigest()
    existing = find_duplicate_asset(session, digest)
    if existing and duplicate_choice == "reuse":
        return existing

    asset_id = f"asset-{uuid.uuid4().hex}"
    filename = f"{asset_id}.{extension}"
    asset_dir = session_path(session["id"]) / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    (asset_dir / filename).write_bytes(data)

    asset = {
        "id": asset_id,
        "kind": "image",
        "display_name": display_name.strip() or asset_id,
        "filename": filename,
        "mime_type": mime_type,
        "public_url": f"/assets/{session['id']}/{filename}",
        "created_at": utc_now_iso(),
        "content_hash": digest,
        "source": source,
    }
    session.setdefault("assets", []).append(asset)
    session["updated_at"] = utc_now_iso()
    return asset


def find_duplicate_asset(session: dict[str, Any], digest: str) -> dict[str, Any] | None:
    return next((asset for asset in session.get("assets", []) if asset.get("content_hash") == digest), None)


def copy_asset_file(session: dict[str, Any], asset: dict[str, Any], destination: Path) -> None:
    source = session_path(session["id"]) / "assets" / asset["filename"]
    shutil.copyfile(source, destination)


def extension_from_name(name: str) -> str:
    suffix = Path(name).suffix.lower().lstrip(".")
    return "jpg" if suffix == "jpeg" else suffix


def extension_from_mime_type(mime_type: str) -> str | None:
    guessed = mimetypes.guess_extension(mime_type)
    if not guessed:
        return None
    return extension_from_name(f"file{guessed}")


def guess_mime_type(filename: str) -> str:
    return mimetypes.guess_type(filename)[0] or "application/octet-stream"


def validate_extension(extension: str) -> None:
    if extension not in ALLOWED_EXTENSIONS:
        raise AssetIngestionError("Unsupported image type.")


def validate_mime_type(mime_type: str) -> None:
    if not mime_type.startswith(ALLOWED_MIME_PREFIXES):
        raise AssetIngestionError("Downloaded or uploaded file is not an image.")
