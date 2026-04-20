# Architecture

## Repository Layout

| Path | Role |
|---|---|
| `src/zpe_taste/` | Lightweight Python package for loading the reference packet and running local validation. |
| `proofs/artifacts/` | Machine-readable evidence promoted by the README. |
| `proofs/manifests/` | Plain-language manifest for the current reference packet. |
| `validation/results/` | Generated local validation outputs for installation and surface checks. |
| `tests/` | Regression checks for claim preservation and surface cleanliness. |

## Runtime Flow

1. `zpe_taste.reference` loads the committed reference packet and manifest.
2. `zpe_taste.verify` checks the public surface, README contract, and artifact consistency.
3. The same validation logic is exercised in `tests/`.

## Design Boundaries

- The package is a reference loader and verifier, not a new scientific evaluation surface.
- Public files depend only on committed relative paths inside this repository.
- The package keeps the claim narrow by checking that non-claims remain present alongside the negative verdict.
