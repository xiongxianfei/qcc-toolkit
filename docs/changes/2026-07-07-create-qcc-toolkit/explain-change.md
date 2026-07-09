# Change Explanation: Create QCC Toolkit

## Status

completed

## Summary

This change creates the first usable QCC Toolkit slice.
It turns the accepted template-backed, Python-powered product direction into a local Python package, first-slice method registry, Pareto calculation engine, chart specification and rendering path, evidence package writer, method guides, template catalog, starter script, synthetic example project, report-ready outputs, and lifecycle proof.

The implementation preserves the core source-of-truth split:

| Surface | Role |
|---|---|
| PowerPoint template assets | Teach and present QCC methods. |
| Markdown method guides | Govern method knowledge and review checklists. |
| Python package and scripts | Validate data, calculate results, generate chart evidence, captions, warnings, and metadata. |
| Evidence package | Preserve the authoritative data-dependent calculation record. |

The current workflow state is ready for `verify`.
Final verification, hosted CI status, PR readiness, and merge readiness are not claimed by this explanation.

## Problem

The accepted proposal records two related problems.
First, QCC work is commonly split across spreadsheets, scripts, chart tools, method notes, and presentation files.
That fragmentation makes QCC evidence difficult to repeat, review, teach, audit, and explain.

Second, QCC users often start from PowerPoint method templates.
The first slice therefore needed to keep templates useful while using Python to protect data-dependent evidence quality and Markdown to keep method knowledge reviewable.

## Decision Trail

| Decision source | Decision used by implementation |
|---|---|
| Vision | Preserve the rule that PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates traceable QCC evidence. |
| Proposal | Build a template-backed, Python-powered first slice with first-class PPT method templates, Markdown guides, a minimal Python evidence engine, starter scripts, synthetic data, and report-ready outputs. |
| Spec | Implement Pareto Chart as the first complete vertical data-chart method, plus template-guided Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys support. |
| Spec requirements | Cover R1-R50 and acceptance criteria AC1-AC12 for synthetic project, method IDs, templates, guides, Pareto validation, evidence packages, reports, scope exclusions, and verification commands. |
| ADR-20260708-python-local-first-stack | Use a local-first Python package with `pyproject.toml`, Python 3.11-3.14, Plotly-first HTML charts, optional PNG export, and local starter scripts. |
| ADR-20260708-evidence-package-boundary | Make the evidence package the authoritative record for data-dependent conclusions; keep manually edited slides as presentation artifacts. |
| Plan | Implement the first slice through M1-M7: package scaffold, core contracts, evidence package, docs/templates/catalog, starter script/example, reports, and lifecycle closeout proof. |

## Diff Rationale By Area

| Area | Files | Change | Why | Source / proof |
|---|---|---|---|---|
| Product direction and governance | `VISION.md`, `README.md`, `AGENTS.md`, `CONSTITUTION.md`, `docs/vision/strategic-positioning.md` | Updated project identity around a template-backed, Python-powered QCC evidence system. | Keeps the repository aligned around the accepted source-of-truth split. | Proposal, vision updates, constitution rules. |
| Proposal, spec, architecture, plan | `docs/proposals/...`, `specs/qcc-toolkit-first-slice.md`, `docs/architecture/system/architecture.md`, ADRs, `docs/plans/...` | Added accepted product direction, approved behavioral spec, architecture package, ADRs, and milestone plan. | Required before implementing a cross-component first slice. | Proposal review, spec review, architecture review, plan review. |
| Package scaffold | `pyproject.toml`, `qcc_toolkit/__init__.py`, `_version.py`, `py.typed`, `.gitignore` | Added installable Python package and quality-gate tooling. | Needed a stable package surface and local validation base before method behavior. | M1, R22, R48-R50. |
| Stage and method registry | `qcc_toolkit/stages.py`, `qcc_toolkit/methods.py` | Added canonical QCC stage IDs and first-slice method definitions. | Method IDs and stage IDs must be stable across Python, guides, templates, and reports. | R3-R8, R11-R17, AC3-AC4, AC11. |
| Pareto validation and calculation | `qcc_toolkit/contracts.py`, `analysis.py`, `interpretation.py` | Added Pareto parameters, validation errors, warning categories, calculation rows/results, and deterministic captions. | Pareto is the first complete data-chart method and must reject invalid inputs before evidence generation. | R21-R29, R36-R38, E1-E2. |
| Chart specification and rendering | `qcc_toolkit/charts.py` | Added renderer-independent Pareto chart specs and Plotly HTML rendering. | Chart logic must preserve method metadata and remain separable from calculation logic. | R30-R35, ADR local-first stack. |
| Evidence package | `qcc_toolkit/evidence.py` | Writes chart, chart spec, calculated table, caption, warnings, metadata, README, and method report fragment. | Evidence package is the authoritative local record for data-dependent conclusions. | R32-R35, R42-R44, ADR evidence boundary. |
| Reports | `qcc_toolkit/reports.py` | Added project-level Markdown and simple local HTML reports from evidence packages. | Users need report-ready outputs that reference generated evidence without becoming a document editor. | R39-R41, R43-R44. |
| Template catalog validation | `qcc_toolkit/templates/` | Added catalog loading, validation, CLI, duplicate checks, path checks, and guide-method ownership checks. | Template, guide, script, and example paths must remain synchronized and reviewable. | R14-R20, R48, CR-M4-001. |
| Method guides | `docs/methods/*.md` | Added guides for Pareto, Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys. | Markdown guides are the method-knowledge surface and document usage, cautions, formulas, and review checklists. | R7-R10, AC3, AC11. |
| Template assets | `templates/ppt/catalog.yml`, `templates/ppt/methods/*.pptx`, `templates/ppt/sources/*.md`, `tools/build_ppt_templates.py` | Added real editable PPTX method templates, reviewable Markdown source notes, stable IDs, placeholders, and demo labels. | PPT method templates are first-class teaching and presentation assets; Markdown source notes and catalog metadata keep them reviewable and testable. | R11-R17, AC4, AC11-AC12. |
| Starter script and example project | `examples/scripts/generate_pareto.py`, `examples/projects/reduce-packing-label-errors/` | Added local CSV script, synthetic dataset, README, and ignored generated output folders. | Gives users an immediate local workflow from synthetic data to evidence and report outputs. | R1-R2, R21-R24, R49, AC1-AC2, AC5, AC7, AC9. |
| Tests | `tests/` | Added unit, integration, contract, smoke, reproducibility, catalog, report, scope, and acceptance tests. | Requirements involving formulas, validation, evidence files, lifecycle, and scope exclusions need executable proof. | Test spec T1-T24. |
| Lifecycle records | `docs/changes/2026-07-07-create-qcc-toolkit/`, `docs/plan.md` | Recorded reviews, findings, review-resolution, validation notes, and milestone state. | The workflow requires durable review evidence and traceability from proposal through implementation review. | M1-M7 reviews and review-resolution. |

## Tests Added Or Changed

| Test area | Files | What it proves | Test-spec link |
|---|---|---|---|
| Package import and registry | `tests/test_import.py`, `tests/test_registry.py`, `tests/test_method_registry.py` | Package imports, stage IDs, and first-slice methods are stable and unique. | T1, T2, T3 |
| Pareto calculation and validation | `tests/test_pareto_calculation.py`, `tests/test_pareto_validation.py`, `tests/test_warnings.py`, `tests/test_interpretation.py` | Known fixtures, validation failures, warning categories, deterministic interpretation, and edge cases behave as specified. | T4-T10 |
| Chart spec and rendering | `tests/test_chart_spec.py`, `tests/test_chart_rendering.py` | Chart specs are renderer-independent and deterministic, HTML is generated locally, and optional PNG export records warnings when unavailable. | T11-T13 |
| Evidence package and reproducibility | `tests/test_evidence_package.py`, `tests/test_reproducibility.py` | Evidence packages contain required artifacts and repeated inputs produce equivalent calculated tables and chart specs. | T14, T19 |
| Method guides and templates | `tests/test_method_guides.py`, `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py`, `tests/test_template_assets.py` | Guides have required metadata and sections, catalog paths/IDs are valid, invalid catalogs fail, and real PPTX templates contain placeholders, demo labels, and stable package metadata. | T12, T13, T14 |
| Starter script and example | `tests/test_generate_pareto_script.py`, `tests/test_example_project_e2e.py`, `tests/test_example_project_structure.py`, `tests/test_synthetic_data_only.py` | The script delegates to public APIs, handles failures safely, regenerates evidence, and examples stay synthetic. | T15-T18, T24 |
| Reports and integration | `tests/test_reports.py`, `tests/test_first_slice_integration.py` | Project reports reference evidence artifacts, expose warnings, and the starter script writes report-ready outputs. | T20 |
| Scope and lifecycle | `tests/test_scope_guards.py`, `tests/test_artifact_consistency.py`, `tests/test_acceptance.py` | Out-of-scope surfaces stay absent, lifecycle paths are consistent, and first-slice acceptance surfaces remain valid across workflow states. | T21-T23 |

The tests are split by behavior level because the first slice spans calculations, local file output, documentation/catalog drift, user-facing scripts, and lifecycle evidence.
Formula and validation behavior use unit tests.
Generated files, scripts, reports, and acceptance use integration or smoke tests.
Lifecycle and scope use contract-style tests.

## Validation Evidence Available Before Final Verify

Local validation has been run during implementation and review.
The latest M7 rereview recorded these passing commands:

```sh
PATH=.venv/bin:$PATH python -m pytest tests/test_acceptance.py tests/test_artifact_consistency.py
PATH=.venv/bin:$PATH python -m pytest
PATH=.venv/bin:$PATH python -m ruff check .
PATH=.venv/bin:$PATH python -m mypy qcc_toolkit
PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml
PATH=.venv/bin:$PATH python examples/scripts/generate_pareto.py \
  --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv \
  --category-column defect_type \
  --count-column count \
  --project examples/projects/reduce-packing-label-errors \
  --output examples/projects/reduce-packing-label-errors/evidence/pareto
git diff --check
```

The full pytest suite passed with 58 tests during M7 rereview.
The catalog validator reported 5 template catalog entries.
The documented Pareto regeneration command wrote the evidence package and project report.

Hosted CI status is not claimed here.
Final `verify` has not run yet.

## Review Resolution Summary

Review-resolution is closed in `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`.

| Finding group | Count | Final disposition |
|---|---:|---|
| Test-spec review findings | 2 | Closed by test-spec revision and approved in test-spec review R2. |
| Code-review findings | 3 | Closed by code-review rereviews. |
| Open findings | 0 | None. |

Key code-review resolutions:

- CR-M3-001: generated Plotly HTML no longer depends on Plotly CDN output.
- CR-M4-001: template catalog validation now rejects mismatched catalog and Markdown guide `method_id` values.
- CR-M7-001: the acceptance proof no longer hard-codes transient M7 review-requested lifecycle strings and passes after M7 moves to a closed/explain-change state.

## Alternatives Rejected

| Alternative | Why it was rejected |
|---|---|
| Template-only implementation | Would leave formulas, chart logic, and evidence reproducibility fragile and hard to test. |
| Generic charting/statistics package | Would weaken QCC stage context and make charts decorative rather than project evidence. |
| Web UI or dashboard first | Would add delivery and scope risk before method contracts and evidence package boundaries stabilize. |
| Automated PPTX generation in the first slice | Would couple implementation to template automation before evidence and report contracts are proven. |
| Control Chart in the first vertical proof slice | Explicitly deferred by R47 to keep Pareto as the complete first vertical method. |
| Committing generated self-contained chart/report outputs | The Plotly HTML artifact is large; tests and documented commands prove regeneration instead. |

## Scope Control

The first slice preserves the non-goals from the proposal and spec:

- no web UI, dashboard, desktop app, or real-time operational surface;
- no CAPA/EQMS workflow, approval workflow, or document editor;
- no automated PPTX generation requirement;
- no Control Chart or advanced methods in the required first vertical proof slice;
- no AI-generated conclusions in the core method engine;
- no network calls, telemetry, secrets, or hosted services for the local example workflow;
- no real customer, production, employee, supplier, patient, or private operational data in examples.

## Risks And Follow-Ups

| Risk or follow-up | Current handling |
|---|---|
| Generated Plotly HTML is large. | Generated evidence outputs are ignored and regenerated by documented commands and tests. |
| PNG export depends on local static-export support. | PNG is optional; missing export records a structured warning while required artifacts still write. |
| PPTX assets are binary and harder to review than Markdown. | The catalog points at real PPTX files, while adjacent Markdown source notes, data-entry slide tests, Pareto embedded-chart tests, and deterministic `tools/build_ppt_templates.py` keep the template structure reviewable and reproducible. |
| Public API and evidence metadata may need refinement before 1.0. | The spec marks this slice pre-1.0, and compatibility surfaces are documented for future migration decisions. |
| Lifecycle closeout is complete. | Final verify passed locally, PR #1 merged the branch into `main`, and release readiness is not claimed. |

## Readiness

All implementation milestones M1-M7 are closed by code review.
All recorded review-resolution findings are closed.
This explanation is complete and the later verify, PR handoff, and merge stages are complete.

This artifact does not claim hosted CI success or release readiness.
