# zpe-taste

[![License: SAL v7.0](https://img.shields.io/badge/license-SAL%20v7.0-orange)](https://github.com/Zer0pa/ZPE-Taste/blob/main/LICENSE)

## What This Is

This repository is the evidenced negative record for the current taste lane object.

The public claim is narrow by design: the current taste lane object is not geometry-bearing under the tested evaluation represented in this repository.

## Key Metrics

Use `proofs/artifacts/taste_negative_reference.json` for the committed evaluation values and thresholds.

## What We Prove

- The committed reference packet preserves the narrow negative verdict for the current taste lane object.

## What We Don't Claim

- This repository does not claim that biological taste coding is impossible.

## Commercial Readiness

This section carries no claim beyond the committed proof anchors and CI checks listed below.

## Tests and Verification

- `python -m zpe_taste.verify`
- `python -m unittest discover -s tests -v`

## Proof Anchors

| Path | State |
|---|---|
| `proofs/artifacts/taste_negative_reference.json` | VERIFIED |
| `proofs/manifests/CURRENT_REFERENCE_PACKET.md` | VERIFIED |
| `PUBLIC_AUDIT_LIMITS.md` | VERIFIED |
| `docs/LEGAL_BOUNDARIES.md` | VERIFIED |

## Repo Shape

| Path | Role |
|-------|------|
| `proofs/artifacts/taste_negative_reference.json` | Machine-readable authority packet |
| `proofs/manifests/CURRENT_REFERENCE_PACKET.md` | Plain-language manifest |
| `src/zpe_taste/` | Read-only loader and verifier |
| `tests/` | CI regression checks |

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install .
python -m zpe_taste.verify
python -m unittest discover -s tests -v
```

### Scope Document

See [`docs/SCOPE.md`](docs/SCOPE.md) for the explicit public claim boundary, and [`PUBLIC_AUDIT_LIMITS.md`](PUBLIC_AUDIT_LIMITS.md) for the outsider audit boundary.
