# zpe-taste

[![License: SAL v7.0](https://img.shields.io/badge/license-SAL%20v7.0-orange)](https://github.com/Zer0pa/ZPE-Taste/blob/main/LICENSE)
[![CI](https://github.com/Zer0pa/ZPE-Taste/actions/workflows/ci.yml/badge.svg)](https://github.com/Zer0pa/ZPE-Taste/actions/workflows/ci.yml)

## What This Is

Public evidence record for the taste lane. Negative-reference boundary and audit limits define the claim surface.

The finding for this lane is a bounded negative: the current taste lane object is **not geometry-bearing** under the evaluation committed here. Identity controls score 1.0 across all four geometry metrics, confirming the evaluation machinery discriminates correctly before the lane object is tested. The lane object scores well below every pass threshold — that result is what this repository preserves and publishes.

This repository does not claim that biological taste coding is impossible. It claims one narrow thing: the committed object did not pass.

## Codec Mechanics

<p>
  <img src=".github/assets/readme/lane-mechanics/TASTE.gif" alt="ZPE-Taste Codec Mechanics animation" width="100%">
</p>

| Field | Value |
| ------- | ------- |
| Architecture | TASTE_REFERENCE_STREAM |
| Encoding | TASTE_NEGATIVE_REFERENCE_V1 |
| Mechanics Asset | `.github/assets/readme/lane-mechanics/TASTE.gif` |

## Key Metrics

| Metric | Value | Baseline |
| -------- | ------- | ---------- |
| metric_fit | 0.207 | 0.6 gate (gap −0.393) |
| topology_fit | 0.156 | 0.5 gate (gap −0.344) |
| local_injectivity | 0.250 | 0.5 gate (gap −0.250) |
| graph_fit | 0.181 | 0.5 gate (gap −0.319) |

> Source: `proofs/artifacts/taste_negative_reference.json`

## Repo Identity

| Field | Value |
| ------- | ------- |
| Identifier | ZPE-Taste |
| Repository | https://github.com/Zer0pa/ZPE-Taste |
| Section | encoding |
| Visibility | PUBLIC |
| Architecture | TASTE_REFERENCE_STREAM |
| Encoding | TASTE_NEGATIVE_REFERENCE_V1 |
| Commit SHA | 900726f407cf |
| License | SAL-7.0 |
| Authority Source | proofs/artifacts/taste_negative_reference.json |

## Readiness

| Field | Value |
| ------- | ------- |
| Verdict | PARTIAL |
| Checks | 4/4 |
| Anchors | 4 display anchors |
| Commit | 900726f407cf |
| Authority | proofs/artifacts/taste_negative_reference.json |

### Honest Blocker

This repository does not claim that biological taste coding is impossible.; This repository does not settle disputed models of cortical taste organization.; This repository does not claim that a different native taste object could never support a geometry-bearing representation.

## What We Prove

- The committed reference packet preserves the narrow negative verdict for the current taste lane object.
- The evaluation machinery discriminates (identity control 1.0), so the lane object scores are meaningful, not noise.

## What We Don't Claim

- This repository does not claim that biological taste coding is impossible.
- No comparative benchmarks are published for this lane. This is a no-comp lane by design.

## Verification Status

| Code | Check | Verdict |
| ------ | ------- | --------- |
| V_01 | Reference packet and manifest preserve the narrow negative verdict and biological non-claim. | PASS |
| V_02 | Identity control scores 1.0 across all four geometry metrics — evaluation machinery discriminates. | PASS |
| V_03 | Scope and boundary documents are present in the tracked tree. | PASS |
| V_04 | Fresh-clone install and read-only falsification commands run locally. | PASS |

## Proof Anchors

| Path | State |
| ------ | ------- |
| `proofs/artifacts/taste_negative_reference.json` | VERIFIED |
| `proofs/manifests/CURRENT_REFERENCE_PACKET.md` | VERIFIED |
| `PUBLIC_AUDIT_LIMITS.md` | VERIFIED |
| `docs/LEGAL_BOUNDARIES.md` | VERIFIED |

## Repo Shape

| Field | Value |
| ------- | ------- |
| Proof Anchors | 4 display anchors |
| Modality Lanes | 1 |
| Architecture | TASTE_REFERENCE_STREAM |
| Encoding | TASTE_NEGATIVE_REFERENCE_V1 |
| Verification | 4/4 checks |
| Authority Source | proofs/artifacts/taste_negative_reference.json |

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
