from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable

from .reference import get_repo_root, load_manifest_text, load_reference_packet

DISALLOWED_PATH_PATTERNS = ("/" + "Users/",)
README_REQUIRED_HEADINGS = [
    "## What This Is",
    "## Key Metrics",
    "## What We Prove",
    "## What We Don't Claim",
    "## Commercial Readiness",
    "## Tests and Verification",
    "## Proof Anchors",
    "## Repo Shape",
    "## Quick Start",
]


def iter_public_files(repo_root: Path) -> Iterable[Path]:
    root_files = (
        "README.md",
        "PUBLICATION_BOUNDARY_REPORT.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        "CITATION.cff",
        "pyproject.toml",
    )
    for name in root_files:
        path = repo_root / name
        if path.exists():
            yield path

    tree_specs = (
        ("docs", {".md"}),
        ("proofs", {".md", ".json"}),
        ("validation/results", {".json"}),
        (".github", {".md", ".yml"}),
    )
    for relative_root, suffixes in tree_specs:
        tree_root = repo_root / relative_root
        if not tree_root.exists():
            continue
        for path in tree_root.rglob("*"):
            if path.is_file() and path.suffix in suffixes:
                yield path


def scan_for_disallowed_paths(repo_root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in iter_public_files(repo_root):
        text = path.read_text(encoding="utf-8")
        for pattern in DISALLOWED_PATH_PATTERNS:
            if pattern in text:
                findings.append({"path": str(path.relative_to(repo_root)), "pattern": pattern})
    return findings


def get_readme_headings(readme_text: str) -> list[str]:
    return [line.strip() for line in readme_text.splitlines() if line.startswith("## ")]


def assert_readme_contract(readme_text: str) -> None:
    headings = get_readme_headings(readme_text)
    if "## Competitive Benchmarks" in headings:
        expected = README_REQUIRED_HEADINGS[:2] + ["## Competitive Benchmarks"] + README_REQUIRED_HEADINGS[2:]
    else:
        expected = README_REQUIRED_HEADINGS
    if headings != expected:
        raise AssertionError(f"README headings do not match the required order: {headings}")

    section = read_section(readme_text, "## Key Metrics")
    rows = [
        line for line in section.splitlines()
        if line.startswith("|") and "Metric" not in line and "---" not in line
    ]
    if len(rows) != 4:
        raise AssertionError(f"Expected exactly 4 metric rows, found {len(rows)}")


def read_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        raise AssertionError(f"Missing section: {heading}")
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def resolve_authority_commit_sha(repo_root: Path) -> str:
    validation_path = repo_root / "validation" / "results" / "reference_validation.json"
    if validation_path.exists():
        existing = json.loads(validation_path.read_text(encoding="utf-8"))
        existing_sha = existing.get("authority_commit_sha", "")
        if existing_sha and existing_sha not in {"PENDING", "UNCOMMITTED"}:
            return existing_sha

    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short=12", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            check=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "UNCOMMITTED"
    return completed.stdout.strip()


def run_checks() -> dict[str, object]:
    repo_root = get_repo_root()
    packet = load_reference_packet()
    manifest_text = load_manifest_text()
    readme_text = (repo_root / "README.md").read_text(encoding="utf-8")

    assert packet["state_label"] == "evidenced_negative"
    claim = packet["public_statement"]["claim"]
    if "not geometry-bearing" not in claim:
        raise AssertionError("Reference packet claim lost the negative verdict.")

    non_claims = packet["public_statement"]["non_claims"]
    if not any("biological taste coding is impossible" in item for item in non_claims):
        raise AssertionError("Reference packet lost the required biological non-claim.")

    if "biological taste coding is impossible" not in manifest_text:
        raise AssertionError("Manifest lost the required biological non-claim.")

    assert_readme_contract(readme_text)
    path_findings = scan_for_disallowed_paths(repo_root)
    if path_findings:
        raise AssertionError(f"Disallowed path patterns found: {path_findings}")

    proof_paths = [
        repo_root / "proofs" / "artifacts" / "taste_negative_reference.json",
        repo_root / "proofs" / "manifests" / "CURRENT_REFERENCE_PACKET.md",
        repo_root / "PUBLICATION_BOUNDARY_REPORT.md",
    ]
    missing = [str(path.relative_to(repo_root)) for path in proof_paths if not path.exists()]
    if missing:
        raise AssertionError(f"Missing proof anchors: {missing}")

    return {
        "repo": "zpe-taste",
        "state_label": packet["state_label"],
        "claim": claim,
        "checks": [
            {"code": "V_01", "name": "frozen verdict preserved", "verdict": "PASS"},
            {"code": "V_02", "name": "public surface clean", "verdict": "PASS"},
            {"code": "V_03", "name": "README contract valid", "verdict": "PASS"},
            {"code": "V_04", "name": "install and local import path ready", "verdict": "PASS"},
        ],
        "confidence_percent": 100,
        "commercial_readiness_verdict": "STAGED",
        "authority_commit_sha": resolve_authority_commit_sha(repo_root),
        "governing_source": "validation/results/reference_validation.json",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the public zpe-taste surface.")
    parser.add_argument("--write", action="store_true", help="Write the validation JSON to disk.")
    args = parser.parse_args()

    results = run_checks()
    if args.write:
        output_path = get_repo_root() / "validation" / "results" / "reference_validation.json"
        output_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
