# Reproducibility

## Canonical Inputs

The read-only verification surface in this repository is driven by the committed reference files below.

- `proofs/artifacts/taste_negative_reference.json`
- `proofs/manifests/CURRENT_REFERENCE_PACKET.md`
- `docs/SCOPE.md`
- `PUBLIC_AUDIT_LIMITS.md`

## Golden-Bundle Hash

This repository does not yet publish a committed golden-bundle hash.

## Verification Command

Run the canonical verification path from a fresh clone:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install .
python -m zpe_taste.verify
python -m unittest discover -s tests -v
```

## Supported Runtimes

- Python package runtime: CPython `>=3.11` (`pyproject.toml`)
- Distribution shape: pure-Python package with no compiled extension build step
- Verification surface: `python -m zpe_taste.verify` plus the stdlib `unittest` suite in `tests/`
