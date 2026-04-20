# Architecture

## Repository Layout

| Path | Role |
|---|---|
| `src/zpe_taste/` | Lightweight Python package for loading the reference packet and running read-only falsification checks. |
| `proofs/artifacts/` | Machine-readable evidence promoted by the README. |
| `proofs/manifests/` | Plain-language manifest for the current reference packet. |
| `PUBLIC_AUDIT_LIMITS.md` | Repository-level scope document for outsider audit boundaries. |
| `tests/` | Regression checks for claim preservation and surface cleanliness. |

## Runtime Flow

1. `zpe_taste.reference` loads the committed reference packet and manifest.
2. `zpe_taste.verify` checks the public surface, README contract, and artifact consistency without writing tracked outputs.
3. The same guardrails are exercised in `tests/`.

## Design Boundaries

- The package is a reference loader and verifier, not a new scientific evaluation surface.
- Public files depend only on committed relative paths inside this repository.
- The package keeps the claim narrow by checking that non-claims remain present alongside the negative verdict.
