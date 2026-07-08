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

## M2 Implementation Rationale

M2 upgrades the Pareto Chart from a useful first-slice template into a complete PowerPoint-native chart method kit.
The change keeps Markdown as the canonical method guide, uses PowerPoint as the teaching and working surface, and keeps Python assist selective for raw, repeated, validation-heavy, or high-rigor evidence.

| Artifact | Change | Reason |
|---|---|---|
| `docs/methods/pareto_chart.md` | Added purpose, PowerPoint workflow, edit instructions, blank slide guidance, interpretation patterns, Python assist decision, and evidence-level/source-note guidance. | Makes the Markdown guide satisfy the Pareto method-kit content contract and reviewer guidance. |
| `templates/ppt/sources/pareto-chart.md` | Added method-kit section source notes covering purpose, stage fit, use/not-use, inputs, edit guidance, demo, blank slide, mistakes, checklist, assist decision, and evidence/source notes. | Keeps the PPTX content reviewable without relying on opaque binary inspection alone. |
| `tools/build_ppt_templates.py` | Added Pareto-specific method-kit slides and updated the project slide to be a blank copyable project slide. | Builds a richer Pareto PowerPoint template while preserving deterministic local generation. |
| `templates/ppt/methods/pareto-chart-template.pptx` | Regenerated as a 10-slide Pareto method kit. | Provides the PowerPoint teaching, editing, demo, checklist, evidence, and blank project-slide surfaces required by M2. |
| `tests/test_method_guides.py` | Added Pareto guide assertions for the PowerPoint-first method-kit standard. | Proves guide-side M2 requirements before implementation. |
| `tests/test_template_assets.py` | Added Pareto source-note and PPTX package assertions for required user-facing surfaces. | Proves source/template M2 requirements before implementation. |
| `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md` | Added MP1 review evidence and renderer limitation. | Records the manual proof required for Pareto template usability before M2 review. |

## M3 Implementation Rationale

M3 upgrades the template-native worksheet and diagram methods into complete method kits without over-automating qualitative methods.
The change keeps these methods PowerPoint-first and does not introduce Python as a required workflow for 5W2H, 5 Whys, Check Sheet, or Fishbone Diagram.

| Artifact | Change | Reason |
|---|---|---|
| `docs/methods/5w2h.md`, `docs/methods/5_whys.md`, `docs/methods/check_sheet.md`, `docs/methods/fishbone_diagram.md` | Added purpose, PowerPoint workflow, blank working slide or worksheet, interpretation patterns, Python assist decision, and evidence-level/source-note guidance. | Makes Markdown govern the minimum method-kit guidance for each template-native method. |
| `templates/ppt/sources/5w2h.md`, `templates/ppt/sources/5-whys.md`, `templates/ppt/sources/check-sheet.md`, `templates/ppt/sources/fishbone-diagram.md` | Added source-note method-kit sections for purpose, stage fit, use/not-use, inputs, demo, blank working surface, interpretation, mistakes, checklist, assist decision, and evidence/source note. | Keeps generated PPTX content reviewable without relying only on opaque binary assets. |
| `tools/build_ppt_templates.py` | Added template-native guidance data and generated guidance slides for non-chart official kits. | Produces complete 10-slide worksheet/diagram decks while preserving deterministic local generation. |
| `templates/ppt/methods/5w2h-template.pptx`, `templates/ppt/methods/5-whys-template.pptx`, `templates/ppt/methods/check-sheet-template.pptx`, `templates/ppt/methods/fishbone-diagram-template.pptx` | Regenerated as complete template-native method kits. | Provides the PowerPoint teaching, working, demo, checklist, evidence, and blank working surfaces required by M3. |
| `tests/test_method_guides.py` | Added template-native guide assertions for required method-kit headings and evidence guidance. | Proves T3, T6, and T8 for non-chart guides. |
| `tests/test_template_assets.py` | Added source-note and PPTX package assertions for template-native method-kit surfaces and an unsupported-authority scope guard. | Proves T5, T6, T7, and T8 for non-chart templates. |
| `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md` | Added MP2 review evidence and renderer limitation. | Records required manual proof for 5W2H, 5 Whys, Check Sheet, and Fishbone template usability before M3 review. |

## Scope Control

The vision alignment portion updates positioning artifacts only.
M1 implementation is limited to catalog metadata and validation behavior.
M2 implementation is limited to the Pareto Chart method kit.
M3 implementation is limited to the four first-slice template-native worksheet and diagram kits.
It does not implement full automated PPTX generation, add advanced QCC methods, require Python for qualitative methods, or change existing Pareto evidence package behavior.

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

M2 validation:

- `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` passed: 14 passed.
- `.venv/bin/python tools/build_ppt_templates.py` passed.
- `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
- `.venv/bin/python -m ruff check .` passed.
- `.venv/bin/python -m mypy qcc_toolkit` passed.
- MP1 manual review recorded deterministic PPTX package/text/layout inspection; no PowerPoint or LibreOffice renderer is available in this environment.

M3 validation:

- Expected failing proof: `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` failed before implementation with missing template-native guide sections, missing source-note method-kit sections, and only 4 slides in each non-chart PPTX deck.
- `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` passed: 17 passed.
- `.venv/bin/python tools/build_ppt_templates.py` passed.
- `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
- `.venv/bin/python -m ruff check .` passed.
- `.venv/bin/python -m mypy qcc_toolkit` passed.
- `git diff --check` passed.
- MP2 manual review recorded deterministic PPTX package/text inspection; no PowerPoint or LibreOffice renderer is available in this environment.

## Readiness

The vision alignment is complete.
M1 is closed.
M2 is closed.
M3 implementation is ready for code-review and is not final closeout evidence.
