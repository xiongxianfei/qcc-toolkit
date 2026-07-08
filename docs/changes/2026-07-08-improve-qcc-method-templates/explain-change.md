# Change Explanation: Improve QCC Method Templates Vision Alignment

## Status

completed

## Summary

This change aligns project vision artifacts with the accepted proposal to improve QCC method templates.
The proposal changes the product-surface priority for method-template work from Python-centered wording to PowerPoint-first, Python-assisted method kits.

The update preserves the constitutional source-of-truth split:

| Surface | Role |
|---|---|
| PowerPoint method kits | Primary teaching, working, and presentation workflow. |
| Markdown method guides | Canonical method knowledge and review guidance. |
| Python assist | Selective validation, calculation, reproducibility, and evidence packaging when PowerPoint is insufficient. |

## Decision Trail

| Decision source | Decision used by this update |
|---|---|
| Accepted proposal | Adopt PowerPoint-first, Python-assisted QCC method kits for method-template work. |
| Proposal review | Approve the amended proposal with no material findings. |
| Vision skill | Update root `VISION.md`, synchronize README front matter, and refresh strategic positioning rationale for a substantive repositioning. |

## Changed Artifacts

| Artifact | Change | Reason |
|---|---|---|
| `VISION.md` | Reframed the pitch, differentiator, audience fit, commitments, refusals, and falsifiability around PowerPoint-first, Python-assisted QCC method kits. | Aligns canonical project identity with the accepted proposal. |
| `README.md` | Replaced only the existing vision marker block. | Keeps README front matter derived from `VISION.md`. |
| `docs/vision/strategic-positioning.md` | Refreshed the positioning pass. | Records the project category, promise, mechanism, tradeoff, refusals, and falsifiability behind the repositioning. |
| `docs/changes/2026-07-08-improve-qcc-method-templates/change.yaml` | Added change-local metadata and causal links. | Records why this substantive vision update exists. |

## M1 Implementation Rationale

M1 implements the catalog contract and validation layer from `specs/qcc-method-kits.md` and `specs/qcc-method-kits.test.md`.
The catalog now makes official method-kit metadata reviewable before deeper template content work begins.

| Artifact | Change | Reason |
|---|---|---|
| `qcc_toolkit/templates/__init__.py` | Added catalog fields and validation for catalog status, method name, implementation mode, Python assist status/reasons, required content metadata, evidence levels, chart editability, and Python-assisted artifact paths. | Satisfies M1 requirements for machine-checkable official kit metadata, ownership, assist status, and failure behavior. |
| `templates/ppt/catalog.yml` | Migrated first-slice method template entries to explicit official method-kit metadata. | Makes Pareto, 5W2H, Fishbone, 5 Whys, and Check Sheet discoverable with their implementation modes and assist status. |
| `tests/test_template_catalog.py` | Added acceptance coverage for official entries, modes, assist status, evidence levels, and Pareto chart editability. | Proves T1 and T10 for valid catalog metadata. |
| `tests/test_template_catalog_failures.py` | Added invalid fixtures for missing minimum metadata, missing chart editability, and incomplete Python-assisted artifacts; updated old fixtures to target one failure branch at a time. | Proves T2 and EB1-EB4 without failures being hidden by unrelated missing fields. |

## Scope Control

The vision alignment portion updates positioning artifacts only.
M1 implementation is limited to catalog metadata and validation behavior.
It does not update PPTX template content, implement full automated PPTX generation, add advanced QCC methods, or change existing Pareto evidence package behavior.

## Validation

Validation for this documentation update is direct artifact inspection:

- `VISION.md` remains under the vision skill word limit.
- README synchronization stays inside the existing `<!-- vision:start -->` and `<!-- vision:end -->` marker block.
- The strategic positioning rationale links to the accepted proposal direction.

M1 validation:

- `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` passed: 11 passed.
- `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
- `.venv/bin/python -m ruff check qcc_toolkit tests` passed.
- `.venv/bin/python -m mypy qcc_toolkit` passed.

## Readiness

The vision alignment is complete.
M1 implementation is ready for code-review and is not final closeout evidence.
