# Publication Boundary Report

## Purpose

This report defines the publication boundary for `zpe-taste` before repo-orchestrator review. The repository is scoped as a public-facing evidenced negative reference for the current taste lane object.

## Extracted Public Material

- The narrow negative claim that the current taste lane object is not geometry-bearing under the tested evaluation.
- The associated non-claim that this result does not prove biological taste coding impossible.
- The frozen numeric results needed to support that narrow claim: distance preservation, neighborhood preservation, local injectivity, graph preservation, replay parity, and dispatch stability.
- Plain-language summaries of the evaluation panel, control routes, and scope boundaries.

## Material Held Back

- Private process documents, runbooks, and historical execution notes.
- Internal naming, doctrine, and evaluation vocabulary that are not required for a grant reviewer to understand the science.
- Private code paths, local machine paths, and archive references.
- Any material that would re-open the science instead of freezing the existing negative cleanly.

## Public Claim Boundary

- Public statement: the current taste lane object is not geometry-bearing under the tested evaluation in this repository.
- Public non-claim: this repository does not prove that biological taste coding is impossible.
- Public posture: evidenced negative reference, not a meta-methodology case study and not a relitigation surface.

## Cleanliness Checks

- Public markdown, JSON, TOML, Python, and workflow files are scanned for local user paths and path-based publication leaks.
- The README follows the required ten-section contract and promotes only values that trace to committed proof artifacts.
- The validation artifact at `validation/results/reference_validation.json` records the passing surface and installation checks for this repo state.

## Remaining Risk

The remaining cleanliness risk is publication metadata drift: the repository should receive one final repo-orchestrator check for remote URL correctness and any founder-specific publication text before push. No open scientific scope leak was detected in the local review state.
