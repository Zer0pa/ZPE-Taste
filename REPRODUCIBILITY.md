# Reproducibility

## Canonical Inputs

- `proofs/artifacts/taste_negative_reference.json` is the machine-readable reference packet that promotes the README metrics.
- `proofs/manifests/CURRENT_REFERENCE_PACKET.md` is the plain-language manifest for the current taste lane object and its bounded negative.

## Golden-Bundle Hash

Not yet populated. A bundle hash will be recorded here once the receipt-bundle workflow is activated for this lane.

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
