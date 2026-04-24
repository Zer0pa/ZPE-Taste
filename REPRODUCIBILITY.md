# Reproducibility

## Canonical Inputs

- `proofs/artifacts/taste_negative_reference.json` is the machine-readable reference packet that promotes the README metrics.
- `proofs/manifests/CURRENT_REFERENCE_PACKET.md` is the plain-language manifest for the current taste lane object and its bounded negative.

## Golden-Bundle Hash

This value will be populated by the `receipt-bundle.yml` workflow in Wave 3.

## Verification Command

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install .
python -m zpe_taste.verify
python -m unittest discover -s tests -v
```

## Supported Runtimes

- CPython 3.11+ in a fresh local virtual environment.
