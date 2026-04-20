# zpe-taste

## What This Is

This repository is the evidenced negative record for the current taste lane object. It is useful now as an auditable reference package that shows what the tested object preserves, where it fails, and which claims remain out of scope.

The claim is narrow by design: the current taste lane object is not geometry-bearing under the evaluation captured in this repository. That result does not generalize to all possible biological taste representations.

| Field | Value |
|-------|-------|
| Architecture | TASTE_REFERENCE_STREAM |
| Encoding | TASTE_NEGATIVE_REFERENCE_V1 |

## Key Metrics

| Metric | Value | Baseline |
|---|---:|---|
| METRIC_FIT | 0.2066 | 0.60 gate |
| TOPOLOGY_FIT | 0.1563 | 0.50 gate |
| LOCAL_INJECTIVITY | 0.2500 | 0.50 gate |
| GRAPH_FIT | 0.1807 | 0.50 gate |

> Source: `proofs/artifacts/taste_negative_reference.json`

## What We Prove

- The current taste lane object fails the tested structural thresholds on distance preservation, neighborhood preservation, local injectivity, and graph preservation when evaluated without carrying full packet identity through as the answer.
- Exact packet replay does not create a stronger public claim than direct decode of the same packet fields.
- The strongest positive control comes only from preserving full packet identity, which is outside the claim surface of this repository.

## What We Don't Claim

- This repository does not claim that biological taste coding is impossible.
- This repository does not settle disputed models of cortical taste organization.
- This repository does not claim that a different native taste object could never support a geometry-bearing representation.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | STAGED |
| Commit SHA | c880f9e93585 |
| Confidence | 100% |
| Source | validation/results/reference_validation.json |

## Tests and Verification

| Code | Check | Verdict |
|---|---|---|
| V_01 | Reference packet preserves the frozen negative verdict and non-claims. | PASS |
| V_02 | Public surface scan blocks local path leakage and keeps links repo-local. | PASS |
| V_03 | README matches the required heading contract and metric table shape. | PASS |
| V_04 | `pip install .`, package import, manifest load, and test discovery succeed locally. | PASS |

## Proof Anchors

| Path | State |
|---|---|
| `proofs/artifacts/taste_negative_reference.json` | VERIFIED |
| `proofs/manifests/CURRENT_REFERENCE_PACKET.md` | VERIFIED |
| `validation/results/reference_validation.json` | VERIFIED |
| `PUBLICATION_BOUNDARY_REPORT.md` | VERIFIED |

## Repo Shape

| Field | Value |
|-------|-------|
| Proof Anchors | 4 |
| Modality Lanes | 1 |
| Authority Source | `proofs/artifacts/taste_negative_reference.json` |
| State Label | `EVIDENCED_NEGATIVE` |

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
python -m zpe_taste.verify
python -m unittest discover -s tests -v
```
