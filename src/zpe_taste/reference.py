from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def get_repo_root() -> Path:
    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    for candidate in candidates:
        if (candidate / "pyproject.toml").exists() and (candidate / "proofs").is_dir():
            return candidate
    raise FileNotFoundError("Could not locate the zpe-taste repository root.")


def load_reference_packet() -> dict[str, Any]:
    packet_path = get_repo_root() / "proofs" / "artifacts" / "taste_negative_reference.json"
    return json.loads(packet_path.read_text(encoding="utf-8"))


def load_manifest_text() -> str:
    manifest_path = get_repo_root() / "proofs" / "manifests" / "CURRENT_REFERENCE_PACKET.md"
    return manifest_path.read_text(encoding="utf-8")
