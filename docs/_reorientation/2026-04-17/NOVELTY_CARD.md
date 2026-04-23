# ZPE-Taste Novelty Card

**Product:** ZPE-Taste
**Domain:** Taste-lane evaluation of the admissible taste lane object against a geometry-bearing codec claim.
**What we sell:** An auditable, publicly registered negative result — the current taste lane object is not geometry-bearing under the tested evaluation. Useful as a falsification reference, a boundary document, and a transparent disclosure that closes the taste lane for the current object.

## Novel contributions

There are no novel codec contributions in this repository. ZPE-Taste is an Evidenced Negative reference. Its purpose is to register a negative result, not to contribute a new encoding technique.

The contribution of this repository is its **falsification surface** — a packaged, reproducible, publicly committed negative result for the bounded taste lane object:

1. **Evidenced-negative reference package.** A committed evaluation panel (1600 balanced events, 25 ordered quality pairs, 4 intensity levels, 4 temporal patterns, 4 flavor patterns) and a frozen artifact (`proofs/artifacts/taste_negative_reference.json`) that records the best achievable scores without full identity carry-through. All four structural geometry metrics (metric fit, topology fit, local injectivity, graph fit) fail against the declared thresholds. Code: [`src/zpe_taste/verify.py:103-152`](src/zpe_taste/verify.py). Nearest prior art: N/A — this is a negative reference record, not a codec design.

2. **Confound-removal discipline.** The evaluation explicitly separates full packet identity replay (which achieves 1.0 on all metrics) from the reduced geometric representation claim. Exact replay parity does not strengthen the public claim; the negative result holds only when identity carry-through is removed from the claim surface. Code: [`src/zpe_taste/verify.py:109-121`](src/zpe_taste/verify.py); artifact: [`proofs/artifacts/taste_negative_reference.json`](proofs/artifacts/taste_negative_reference.json) (`replay_controls` block). What is genuinely useful here: the transparent separation of confound sources is the methodological contribution, not a codec technique.

## Standard techniques used (explicit, not novel)

- Python `json` serialization for the reference packet artifact.
- Standard structural geometry metrics (metric fit, topology fit, local injectivity, graph fit) applied as evaluation thresholds — these are assessment methods, not novel codec techniques.
- No compression, no directional encoding, no quantization, no serialization codec of any kind. This repository contains no codec.

## Compass-8 / 8-primitive architecture

NO — Not applicable. ZPE-Taste does not implement a codec of any kind and does not use the Compass-8 directional encoding pattern. License §7.15 confirms: "Compass-8 Pattern: Not applicable — no positive codec claim is made for this lane under this License." There is no directional encoder in the source; the repository contains only an evaluation harness and a frozen negative result artifact.

## Open novelty questions for the license agent

None. The Evidenced Negative status is settled. The LICENSE §7.15 novelty schedule is correct as written. No positive codec claim exists or should be added. If any future evaluation of a different native taste object produces a geometry-bearing result, that would constitute a new product, not a revision of this reference.
