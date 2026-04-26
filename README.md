# zpe-taste

[![License: SAL v7.0](https://img.shields.io/badge/license-SAL%20v7.0-orange)](https://github.com/Zer0pa/ZPE-Taste/blob/main/LICENSE)
[![CI](https://github.com/Zer0pa/ZPE-Taste/actions/workflows/ci.yml/badge.svg)](https://github.com/Zer0pa/ZPE-Taste/actions/workflows/ci.yml)

## What This Is

ZPE-Taste is the public evidence record for the taste lane of the [Zer0pa](https://github.com/Zer0pa) codec portfolio — one of 17 independent encoding lanes, each with its own domain and its own claim boundary.

The finding for this lane is a bounded negative: the current taste lane object is **not geometry-bearing** under the evaluation committed here. Identity controls score 1.0 across all four geometry metrics, confirming the evaluation machinery discriminates correctly before the lane object is tested. The lane object scores well below every pass threshold — that result is what this repository preserves and publishes.

This repository does not claim that biological taste coding is impossible. It claims one narrow thing: the committed object did not pass.

## Key Metrics

Evaluation panel: **1,600 balanced events** — 25 ordered quality pairs, 4 intensity levels, 4 temporal patterns, 4 flavor patterns.

Identity control scores: **1.0 across all four metrics** (evaluation machinery confirmed discriminating).

Lane object scores against pass thresholds:

| Metric | Best score | Pass threshold | Gap |
|---|---|---|---|
| metric\_fit (distance preservation) | 0.207 | 0.6 | −0.393 |
| topology\_fit (neighborhood preservation) | 0.156 | 0.5 | −0.344 |
| local\_injectivity | 0.250 | 0.5 | −0.250 |
| graph\_fit | 0.181 | 0.5 | −0.319 |

Reconstruction gain over direct decode: 0.0 (exact replay parity — no geometric claim strength added by the decode path).

Source: `proofs/artifacts/taste_negative_reference.json` · exercised by CI test `test_reference_packet_preserves_negative_scope` in `tests/test_reference_packet.py`.

## What We Prove

- The committed reference packet preserves the narrow negative verdict for the current taste lane object.
- The evaluation machinery discriminates (identity control 1.0), so the lane object scores are meaningful, not noise.

## What We Don't Claim

- This repository does not claim that biological taste coding is impossible.
- No comparative benchmarks are published for this lane. This is a no-comp lane by design.

## Commercial Readiness

This section carries no claim beyond the committed proof anchors and CI checks listed below.

## Tests and Verification

```bash
python -m zpe_taste.verify
python -m unittest discover -s tests -v
```

## Proof Anchors

| Path | State |
|---|---|
| `proofs/artifacts/taste_negative_reference.json` | VERIFIED |
| `proofs/manifests/CURRENT_REFERENCE_PACKET.md` | VERIFIED |
| `PUBLIC_AUDIT_LIMITS.md` | VERIFIED |
| `docs/LEGAL_BOUNDARIES.md` | VERIFIED |

## Repo Shape

| Path | Role |
|---|---|
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

## Upcoming Workstreams

This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **Taste lane object — conceptual rethink** — Zero-Base Scientific Thinking — GPD Research and Planning Pending. Current lane object is not geometry-bearing (metric_fit 0.207 vs threshold 0.6, topology_fit 0.156 vs 0.5) — published as falsification. Active rethinking: what is the actual encodable taste object? Receptor-space (parallel to ZPE-Smell), psychophysical-space, or something else? No new engineering until the conceptual model resolves.
