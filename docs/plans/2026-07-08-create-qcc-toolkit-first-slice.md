# Create QCC Toolkit First Slice Plan

## Status

- Plan lifecycle state: active
- Terminal disposition: not-applicable
- Plan review: approved
- Test spec: specs/qcc-toolkit-first-slice.test.md

## Purpose / big picture

This plan sequences the approved QCC Toolkit first slice into reviewable implementation milestones.
The work creates a local-first Python package that can generate a Pareto evidence package from synthetic data, while also adding first-slice Markdown method guides, static PowerPoint template placeholders, a template catalog, starter scripts, example project outputs, and validation checks.

Readiness is not Done.
This plan does not authorize implementation until plan-review and test-spec gates are complete.

## Source artifacts

- Proposal: [docs/proposals/2026-07-07-create-qcc-toolkit.md](../proposals/2026-07-07-create-qcc-toolkit.md)
- Spec: [specs/qcc-toolkit-first-slice.md](../../specs/qcc-toolkit-first-slice.md)
- Architecture: [docs/architecture/system/architecture.md](../architecture/system/architecture.md)
- ADR: [docs/adr/ADR-20260708-python-local-first-stack.md](../adr/ADR-20260708-python-local-first-stack.md)
- ADR: [docs/adr/ADR-20260708-evidence-package-boundary.md](../adr/ADR-20260708-evidence-package-boundary.md)
- Proposal review: [docs/changes/2026-07-07-create-qcc-toolkit/reviews/proposal-review-r1.md](../changes/2026-07-07-create-qcc-toolkit/reviews/proposal-review-r1.md)
- Spec review: [docs/changes/2026-07-07-create-qcc-toolkit/reviews/spec-review-r1.md](../changes/2026-07-07-create-qcc-toolkit/reviews/spec-review-r1.md)
- Architecture review: [docs/changes/2026-07-07-create-qcc-toolkit/reviews/architecture-review-r1.md](../changes/2026-07-07-create-qcc-toolkit/reviews/architecture-review-r1.md)
- Plan review: [docs/changes/2026-07-07-create-qcc-toolkit/reviews/plan-review-r1.md](../changes/2026-07-07-create-qcc-toolkit/reviews/plan-review-r1.md)
- Test spec: [specs/qcc-toolkit-first-slice.test.md](../../specs/qcc-toolkit-first-slice.test.md)

## Context and orientation

The repository is still at project genesis.
M1 has added the initial Python package scaffold, package configuration, and import smoke test.
There is still no QCC method behavior, method docs, templates, examples, CI workflow, runtime command, or evidence-generation code yet.

The first implementation must preserve the source-of-truth split:

- PowerPoint templates teach and present.
- Markdown method guides govern method knowledge.
- Python validates data, calculates Pareto outputs, builds chart specifications, writes captions and warnings, and generates evidence packages.
- Evidence packages are authoritative for data-dependent QCC conclusions.

The implementation must stay local-first.
It must not add web UI, telemetry, hosted services, CAPA/EQMS workflow, automated PPTX generation, Control Chart, or advanced methods in this slice.

## Non-goals

- Build a web UI, dashboard, desktop application, CAPA/EQMS workflow, approval workflow, or document editor.
- Implement Control Chart or advanced methods such as DOE, QFD, Kano, advanced regression, or complex network planning.
- Fully automate PowerPoint deck generation.
- Use AI-generated conclusions in the core method engine.
- Add external network calls, telemetry, secrets, or cloud dependencies.
- Treat starter scripts, notebooks, or PPT templates as formula owners.

## Requirements covered

| Requirement range | Milestones |
|---|---|
| R1-R2 | M5, M6 |
| R3-R4 | M2, M4, M5 |
| R5-R8 | M2, M4 |
| R9-R10 | M2, M4 |
| R11-R20 | M4 |
| R21-R24 | M5 |
| R25-R38 | M2, M3, M5 |
| R39-R44 | M3, M5, M6 |
| R45-R47 | All milestones as scope guardrails |
| R48-R50 | M1, M4, M5, M6 |

## Current Handoff Summary

- Current milestone: M5
- Current milestone state: planned
- Last reviewed milestone: M4
- Review status: plan-review approved; test-spec-review approved; M4 code-review clean-with-notes after CR-M4-001 rereview
- Remaining in-scope implementation milestones: M5, M6, M7
- Next stage: implement
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1-M4 are closed; M5-M7, explain-change, verify, and PR handoff have not occurred.

## Milestones

### M1. Package and quality gate scaffold

- Milestone state: closed
- Goal: Establish the minimal Python package, dependency, test, lint, type, and local validation surfaces required for later milestones.
- Requirements: R22, R48, R49, R50, NG1-NG8
- Files/components likely touched:
  - `pyproject.toml`
  - `qcc_toolkit/`
  - `tests/`
  - `.gitignore`
  - `README.md`
  - optional `.github/workflows/`
- Dependencies:
  - Approved architecture and ADRs.
  - No package tooling exists yet.
- Tests to add/update:
  - Import smoke test for `qcc_toolkit`.
  - Tooling smoke tests for package import and configured checks.
- Implementation steps:
  - Add `pyproject.toml` with Python 3.11 through 3.14 metadata and first-slice dependencies.
  - Add initial package directory and public import surface.
  - Configure pytest, Ruff, and typing checks.
  - Add a minimal test suite and package import test.
  - Document local validation commands.
- Validation commands:
  - `python -m pytest`
  - `python -m ruff check .`
  - `python -m mypy qcc_toolkit`
  - `python -m pip install -e .`
- Expected observable result: A local checkout can install the package and run baseline checks without implementation behavior beyond imports.
- Commit message: `M1: scaffold package and quality gates`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Python 3.14 dependency compatibility may lag.
  - Typing setup may be too strict for early implementation.
- Rollback/recovery:
  - Reduce strictness only through a recorded decision.
  - Keep dependency groups small and pin only where compatibility requires it.

### M2. Core contracts and Pareto calculation engine

- Milestone state: closed
- Goal: Implement structured method IDs, stage IDs, Pareto input validation, calculation result, warnings, and deterministic caption inputs without rendering or evidence writing.
- Requirements: R3, R5, R7-R10, R21, R25-R31, R36-R38, R42
- Files/components likely touched:
  - `qcc_toolkit/stages.py`
  - `qcc_toolkit/methods/`
  - `qcc_toolkit/contracts/`
  - `qcc_toolkit/analysis/`
  - `qcc_toolkit/interpretation/`
  - `tests/`
- Dependencies:
  - M1 package and test scaffold.
- Tests to add/update:
  - Pareto calculation fixture tests.
  - Empty dataset, missing column, negative count, nonnumeric count, blank category, zero-total, tie-break, and one-category tests.
  - Deterministic caption and warning classification tests.
- Implementation steps:
  - Define canonical first-slice stage IDs and method IDs.
  - Define Pareto input parameter and validation result models.
  - Implement category-count and supported event-record validation path.
  - Implement deterministic Pareto calculation and tie-break behavior.
  - Implement warning types for validation, data caution, export skip, and interpretation caution.
  - Implement deterministic caption/summary data generation.
- Validation commands:
  - `python -m pytest tests`
  - `python -m ruff check qcc_toolkit tests`
  - `python -m mypy qcc_toolkit`
- Expected observable result: Pareto calculation and validation are correct and testable without rendering, scripts, templates, or file output.
- Commit message: `M2: implement Pareto contracts and calculation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Validation rules could drift from method docs if docs are added later without checks.
  - Event-record and category-count support could overexpand scope.
- Rollback/recovery:
  - If dual input support becomes too broad, keep category-count support first and document event-record support as deferred only through spec revision.
- Milestone handoff:
  - Tests were added first for T2-T6 registry, validation, calculation, and deterministic interpretation coverage.
  - Implementation added stable QCC stage IDs, first-slice method metadata, Pareto parameters and validation errors, warning categories, category-count and event-record Pareto calculation, deterministic tie ordering, and deterministic Pareto caption/summary generation.
  - Rendering, evidence writing, scripts, templates, reports, and chart specifications remain out of M2 scope and are left to later milestones.

### M3. Chart specification, rendering adapter, and evidence writer

- Milestone state: closed
- Goal: Convert Pareto calculation results into chart specs, HTML output, optional PNG output, and method-scoped evidence packages.
- Requirements: R29-R38, R39-R44, R49, R50
- Files/components likely touched:
  - `qcc_toolkit/charts/`
  - `qcc_toolkit/evidence/`
  - `qcc_toolkit/reports/`
  - `tests/`
- Dependencies:
  - M2 contracts and Pareto result models.
- Tests to add/update:
  - Chart spec snapshot tests.
  - Evidence package file manifest tests.
  - PNG unavailable warning test.
  - Metadata and warnings JSON tests.
  - Reproducibility tests for calculated table and chart spec.
- Implementation steps:
  - Define renderer-independent Pareto chart spec.
  - Implement Plotly HTML rendering.
  - Implement optional PNG export with structured skip warning.
  - Write evidence package files: `chart.html`, optional `chart.png`, `chart-spec.json`, `calculated-table.csv`, `caption.md`, `warnings.json`, `metadata.json`, and `README.md`.
  - Add Markdown report output referencing the evidence package.
- Validation commands:
  - `python -m pytest tests`
  - `python -m ruff check qcc_toolkit tests`
  - `python -m mypy qcc_toolkit`
- Expected observable result: A test can generate a complete Pareto evidence package from in-memory or fixture data and assert required artifacts.
- Commit message: `M3: generate Pareto chart specs and evidence packages`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Plotly/Kaleido export behavior may be environment-sensitive.
  - Metadata may reveal more input detail than intended.
- Rollback/recovery:
  - Keep HTML output required and PNG optional.
  - Narrow metadata to source references and reproducibility fields, not raw row dumps.
- Milestone handoff:
  - Tests were added first for T7-T10 and M3-owned pieces of T19: chart spec snapshots, HTML rendering, optional PNG skip behavior, evidence package files, warning serialization, explicit overwrite behavior, and reproducible chart spec/calculated table output.
  - Implementation added renderer-independent Pareto chart specs, Plotly HTML rendering, optional PNG exporter hooks with `export_skipped` warnings, method-scoped evidence package writing, metadata/warnings JSON artifacts, calculated-table CSV, caption, README, and Markdown report output.
  - Starter scripts, example project data, method guides, templates, catalog validation, and full end-to-end regeneration remain out of M3 scope and are left to later milestones.

### M4. Method guides, PPT placeholders, and template catalog

- Milestone state: closed
- Goal: Add first-slice method guides, static template placeholder assets, and validated template catalog traceability.
- Requirements: R4-R20, R43, R48, AC3, AC4, AC8, AC11, AC12
- Files/components likely touched:
  - `docs/methods/`
  - `templates/ppt/catalog.yml`
  - `templates/ppt/methods/`
  - `qcc_toolkit/templates/`
  - `tests/`
- Dependencies:
  - M1 package scaffold.
  - M2 method IDs and stage IDs.
- Tests to add/update:
  - Catalog schema and path validation tests.
  - Method guide front matter and required section checks.
  - Demo-label and placeholder contract checks where feasible for static assets.
- Implementation steps:
  - Add Markdown guides for Pareto Chart, Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys.
  - Add first-slice static template assets or placeholder templates with stable IDs and demo labels.
  - Add `templates/ppt/catalog.yml` with required fields and first-slice entries.
  - Implement catalog validation through the public or tooling API.
  - Add docs/catalog consistency checks.
- Validation commands:
  - `python -m pytest tests`
  - `python -m ruff check qcc_toolkit tests`
  - `python -m mypy qcc_toolkit`
  - `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
- Expected observable result: A reviewer can trace every first-slice template to method ID, guide, script or no-script status, example project, placeholders, and expected assets.
- Commit message: `M4: add method guides and template catalog`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Real `.pptx` binary assets are hard to diff.
  - Placeholder checks may be weak before automation exists.
- Rollback/recovery:
  - Keep catalog and Markdown template outlines authoritative if binary PPT assets need staged follow-up.
  - Record any deferred binary PPT generation as a plan discovery and spec/architecture follow-up if it affects acceptance.
- Milestone handoff:
  - Tests were added first for T11-T14: method guide front matter, required guide sections, Pareto formula/input documentation, template catalog coverage, missing-path failures, duplicate template IDs, duplicate method ownership, and reviewable placeholder/demo-label metadata.
  - Implementation added five method guides, reviewable PPT placeholder sources, `templates/ppt/catalog.yml`, `qcc_toolkit.templates` catalog validation, and the catalog validation CLI.
  - The Pareto starter script and example project paths are declared as M4 placeholders only; functional script behavior, synthetic data, and regenerated example evidence remain in M5 scope.
  - CR-M4-001 remediation added guide front-matter method ID validation and a mismatched-guide negative test.
  - M4 rereview closed CR-M4-001 after direct proof that mismatched guide/catalog method IDs now fail with entry and path details.

### M5. Starter scripts and synthetic example project

- Milestone state: planned
- Goal: Provide local starter scripts and the synthetic `reduce-packing-label-errors` project that regenerate Pareto evidence from local data.
- Requirements: R1-R2, R21-R24, R39-R43, R48-R50, AC1, AC2, AC5, AC6, AC7, AC9
- Files/components likely touched:
  - `examples/scripts/generate_pareto.py`
  - `examples/projects/reduce-packing-label-errors/`
  - `examples/projects/reduce-packing-label-errors/data/`
  - `examples/projects/reduce-packing-label-errors/evidence/`
  - `tests/`
- Dependencies:
  - M2 Pareto contracts.
  - M3 evidence package writer.
  - M4 catalog and guide paths.
- Tests to add/update:
  - Script smoke tests using synthetic CSV data.
  - Exit-code tests for valid and invalid input.
  - Example project regeneration test.
  - No-real-data fixture review where practical.
- Implementation steps:
  - Add synthetic defect dataset.
  - Add `generate_pareto.py` as a thin wrapper around public APIs.
  - Add example project README and expected invocation.
  - Regenerate or provide generated evidence package artifacts from synthetic data.
  - Add smoke tests for script behavior and output artifacts.
- Validation commands:
  - `python examples/scripts/generate_pareto.py --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv --category-column defect_type --count-column count --project examples/projects/reduce-packing-label-errors --output examples/projects/reduce-packing-label-errors/evidence/pareto`
  - `python -m pytest tests`
  - `python -m ruff check qcc_toolkit tests examples`
  - `python -m mypy qcc_toolkit`
- Expected observable result: A user can regenerate the Pareto evidence package from the synthetic project with a local script.
- Commit message: `M5: add Pareto starter script and synthetic project`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Generated artifacts may create noisy diffs.
  - Script paths may drift from catalog entries.
- Rollback/recovery:
  - Keep generated artifacts minimal and deterministic.
  - Add catalog/path checks to catch drift.

### M6. Report-ready outputs and full first-slice integration

- Milestone state: planned
- Goal: Connect generated evidence, method guides, template catalog, and report output into one coherent first-slice workflow.
- Requirements: R39-R44, R48-R50, AC1-AC12
- Files/components likely touched:
  - `qcc_toolkit/reports/`
  - `examples/projects/reduce-packing-label-errors/report/`
  - `README.md`
  - `docs/methods/`
  - `tests/`
- Dependencies:
  - M3 evidence package writer.
  - M4 method docs and catalog.
  - M5 starter script and synthetic project.
- Tests to add/update:
  - Markdown report artifact test.
  - Optional HTML report test when local renderer is available.
  - Warning visibility test.
  - End-to-end first-slice acceptance test.
- Implementation steps:
  - Generate Markdown report output that references Pareto evidence artifacts.
  - Add optional HTML report output when renderer support is available.
  - Ensure warnings are visible in reports.
  - Add README usage path from template to script to evidence package to report.
  - Run end-to-end acceptance checks against AC1-AC12.
- Validation commands:
  - `python -m pytest tests`
  - `python -m ruff check .`
  - `python -m mypy qcc_toolkit`
  - `python examples/scripts/generate_pareto.py --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv --category-column defect_type --count-column count --project examples/projects/reduce-packing-label-errors --output examples/projects/reduce-packing-label-errors/evidence/pareto`
- Expected observable result: The first-slice workflow can be demonstrated from synthetic data through evidence package and report-ready output.
- Commit message: `M6: integrate first-slice report workflow`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Report generation could overgrow into document-editor scope.
  - HTML report rendering may add avoidable dependency complexity.
- Rollback/recovery:
  - Keep Markdown report required and HTML optional.
  - Avoid report editing features.

### M7. Lifecycle closeout preparation

- Milestone state: planned
- Goal: Prepare completed implementation evidence for code review, explain-change, verify, and PR handoff after all implementation milestones close.
- Requirements: all first-slice acceptance criteria
- Files/components likely touched:
  - `docs/changes/2026-07-07-create-qcc-toolkit/`
  - `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
  - `docs/plan.md`
- Dependencies:
  - M1-M6 closed.
  - Code reviews and review-resolution completed for all implementation milestones.
- Tests to add/update:
  - No new product tests expected; this milestone gathers evidence and closes lifecycle records.
- Implementation steps:
  - Update plan progress and validation notes.
  - Ensure code-review records exist for implementation milestones.
  - Prepare explain-change after implementation review is clean.
  - Run final verify after explain-change.
  - Prepare PR notes only after verify passes.
- Validation commands:
  - `python -m pytest`
  - `python -m ruff check .`
  - `python -m mypy qcc_toolkit`
  - `git status --short`
- Expected observable result: The branch has complete lifecycle evidence for final verification and PR handoff.
- Commit message: `M7: prepare first-slice lifecycle closeout`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Closing lifecycle records too early could hide open review or validation work.
- Rollback/recovery:
  - Keep plan active until code-review, explain-change, verify, and PR handoff requirements are actually satisfied.

## Validation plan

| Validation | Purpose | First used |
|---|---|---|
| `python -m pip install -e .` | Confirm local editable install works. | M1 |
| `python -m pytest` | Run complete automated test suite. | M1 onward |
| `python -m pytest tests` | Run repository tests during milestone work. | M1 onward |
| `python -m ruff check .` | Lint package, tests, examples, and docs-support scripts. | M1 onward |
| `python -m mypy qcc_toolkit` | Type-check public package implementation. | M1 onward |
| `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | Validate template catalog traceability. | M4 onward |
| `python examples/scripts/generate_pareto.py --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv --category-column defect_type --count-column count --project examples/projects/reduce-packing-label-errors --output examples/projects/reduce-packing-label-errors/evidence/pareto` | Regenerate first-slice Pareto evidence package. | M5 onward |
| Project artifact lifecycle state-sync check | Confirm proposal, spec, architecture, plan, review log, and change metadata do not contradict current lifecycle state. | Before plan-review and later handoffs |

Exact commands may be adjusted during implementation only if tooling names differ after M1.
Any adjustment must be recorded in `Validation notes` with the reason.

## Risks and recovery

| Risk | Recovery |
|---|---|
| Dependency compatibility with Python 3.14 fails. | Record the compatibility issue, keep code compatible where possible, and route any support-matrix change through spec or ADR update. |
| Static PNG export is flaky or unavailable. | Keep HTML and structured evidence required; record PNG skip warning as designed. |
| Template assets become hard to review as binary files. | Keep Markdown guides and YAML catalog as reviewable sources; use placeholder or outline assets until binary handling is stable. |
| Scope creeps into report editing or deck automation. | Keep reports Markdown-first and slide-ready; defer automated PPTX through a later accepted proposal/spec. |
| Public API shape becomes too narrow for future methods. | Keep facade small but method-oriented; record API naming decisions in milestone decision log. |
| Generated evidence includes sensitive source data. | Use synthetic examples, minimize metadata, and add tests or review checks against raw row dumps. |

## Dependencies

- Plan-review approved this plan before test-spec authoring.
- Test-spec must pass test-spec-review before implementation.
- M1 must precede all implementation milestones because no package or test tooling exists yet.
- M2 must precede M3 and M5 because validation and calculation contracts are required.
- M3 must precede M5 and M6 because evidence writing and chart specs are required.
- M4 can proceed after M1 and M2, but full catalog script links are complete only after M5.
- M7 can start only after implementation milestones and code reviews are complete.

## Progress

- 2026-07-08: Plan created from accepted proposal, approved spec, approved architecture, and accepted ADRs.
- 2026-07-08: Plan review approved the plan with no material findings.
- 2026-07-08: Test spec authored for test-spec-review.
- 2026-07-08: Test spec review requested revisions before implementation handoff.
- 2026-07-08: Test spec revised to remove manual proof as a required gate and add explicit IO safety proof.
- 2026-07-08: Test spec review approved the revised proof map and allowed implementation handoff.
- 2026-07-08: M1 implemented package metadata, `qcc_toolkit` import surface, typed package marker, import smoke test, Python ignore patterns, and README local development commands.
- 2026-07-08: M1 code review closed the package and quality-gate scaffold with no material findings.
- 2026-07-08: M2 added tests first for method/stage registry contracts, Pareto validation failures, known Pareto calculations, event-record counting, deterministic tie ordering, reproducibility, and deterministic interpretation warnings.
- 2026-07-08: M2 implemented core contracts and Pareto calculation without rendering, evidence writing, starter scripts, templates, or report output.
- 2026-07-08: M2 code review closed the core contracts and Pareto calculation engine with no material findings.
- 2026-07-08: M3 added tests first for chart spec construction, HTML rendering, optional PNG skip warnings, evidence package files and metadata, warning serialization, overwrite behavior, and reproducible chart spec/calculated table output.
- 2026-07-08: M3 implemented Pareto chart specs, evidence package writing, Plotly HTML rendering, optional PNG exporter hooks, metadata/warnings artifacts, and Markdown report output without starter scripts, templates, or example project assets.
- 2026-07-08: M3 code review requested changes for CR-M3-001 because generated `chart.html` depends on a Plotly CDN resource instead of being local-first/self-contained.
- 2026-07-08: M3 review-resolution changed Plotly HTML rendering to self-contained mode and added a regression check that rejects external Plotly CDN script output.
- 2026-07-08: M3 rereview classified CR-M3-001 as failed-remediation because generated HTML still contains `https://cdn.plot.ly/un/` and the test does not reject that Plotly CDN URL string.
- 2026-07-08: Strict CR-M3-001 remediation added `assert "https://cdn.plot.ly" not in chart_html` and removed Plotly CDN URL strings from generated self-contained HTML.
- 2026-07-08: M3 strict rereview closed CR-M3-001 after focused chart-rendering tests and direct generated-output inspection showed no `https://cdn.plot.ly` string remains.
- 2026-07-08: M4 started with tests for method guides, template catalog coverage, invalid catalog failures, and reviewable template placeholder assets.
- 2026-07-08: M4 implemented five method guides, reviewable PPT placeholder sources, template catalog entries, catalog validator API, catalog validator CLI, and planned placeholder paths for the M5 Pareto script and example project.
- 2026-07-08: M4 code review requested changes for CR-M4-001 because catalog validation accepts mismatched catalog and Markdown guide method IDs.
- 2026-07-08: CR-M4-001 remediation added guide front-matter method ID validation and a mismatched-guide negative test.
- 2026-07-08: M4 rereview closed CR-M4-001 after focused catalog tests and a direct mutation probe confirmed mismatched guide/catalog method IDs fail with entry and path details.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-08 | Sequence package/tooling first, then contracts, evidence, docs/templates, scripts/examples, integration, and lifecycle closeout. | The repository has no package or tests yet, and later milestones need a stable validation surface. | Start with scripts before package; implement docs/templates after final integration only. |
| 2026-07-08 | Keep PNG export optional in implementation milestones. | The spec and architecture make HTML primary and PNG dependent on local static export support. | Treat PNG export as required for success. |
| 2026-07-08 | Treat binary PPT assets as review-risk items. | Static templates are required, but reviewable YAML and Markdown must remain the traceability surface. | Make binary PPT contents the only source of template truth. |
| 2026-07-08 | Use an ignored `.venv` for local M1 validation in this workspace. | System Python lacks `pip`, so the planned `python -m` validation commands need a project-local Python environment. | Install packages into system Python; skip package validation. |
| 2026-07-08 | Implement M2 contracts with dataclasses and standard library validation. | The M2 scope only needs stable IDs, validation, calculation, and deterministic interpretation; Pydantic schemas can be introduced when file/project/evidence boundaries require them. | Add Pydantic models before evidence or IO contracts exist. |
| 2026-07-08 | Support both category-count and event-record Pareto inputs in M2. | The approved spec allows both when documented, and the calculation path stays small enough to validate with tests. | Support only category-count input in M2. |
| 2026-07-08 | Keep M3 chart specs deterministic and omit timestamps. | R50 requires same inputs and parameters to reproduce the same calculated table and chart spec under the same toolkit version. | Add generated timestamps to chart specs in M3. |
| 2026-07-08 | Treat PNG export as an injectable optional exporter in M3. | The milestone must record PNG skip warnings without depending on local Kaleido behavior. | Require Kaleido-backed PNG export for M3 success. |
| 2026-07-08 | Use reviewable Markdown placeholder sources for M4 PPT template assets. | The test spec allows accepted placeholder assets and reviewable metadata, and binary PPT files are hard to inspect before PPT automation exists. | Commit binary-only PPTX files as the first review surface. |
| 2026-07-08 | Add placeholder paths for the M5 Pareto script and example project during M4. | The M4 catalog must identify and validate Pareto generator and example project paths, while M5 remains responsible for functional script behavior and synthetic evidence. | Leave catalog paths missing until M5; implement the full starter script in M4. |

## Surprises and discoveries

- System Python has no `pip`, `pytest`, `ruff`, or `mypy`; M1 validation used an ignored `.venv` seeded through the available `uv` executable.
- M4 catalog validation needs stable Pareto script and example-project paths before M5 can implement them, so M4 adds explicit placeholders without implementing starter-script behavior.

## Validation notes

- 2026-07-08: Plan authoring validation used Markdown structure checks and `git diff --check`; package validation commands cannot run until M1 creates package tooling.
- 2026-07-08: Initial tests-first check `python -m pytest tests/test_import.py` failed before scaffolding because system Python had no `pytest`.
- 2026-07-08: `uv venv .venv --python python3.12` and `uv pip install --python .venv/bin/python pip` created a local ignored validation environment because system Python had no `pip`.
- 2026-07-08: `.venv/bin/python -m pip install -e ".[dev]"` installed the package and development tools.
- 2026-07-08: `.venv/bin/python -m pip install -e .` passed.
- 2026-07-08: `.venv/bin/python -m pytest` passed with 1 test.
- 2026-07-08: `.venv/bin/python -m pytest tests` passed with 1 test.
- 2026-07-08: `.venv/bin/python -m ruff check .` passed.
- 2026-07-08: `.venv/bin/python -m mypy qcc_toolkit` passed.
- 2026-07-08: `git diff --check` passed.
- 2026-07-08: Tests-first M2 check `PATH=.venv/bin:$PATH python -m pytest tests` failed as expected with missing `qcc_toolkit.analysis`, `qcc_toolkit.methods`, and related M2 modules.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m pytest tests` passed with 25 tests.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests` passed.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- 2026-07-08: Tests-first M3 check `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_spec.py tests/test_chart_rendering.py tests/test_evidence_package.py tests/test_warnings.py` failed as expected with missing `qcc_toolkit.charts` and `qcc_toolkit.evidence` modules.
- 2026-07-08: Focused M3 check `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_spec.py tests/test_chart_rendering.py tests/test_evidence_package.py tests/test_warnings.py` passed with 9 tests.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m pytest tests` passed with 34 tests.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests` passed.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- 2026-07-08: CR-M3-001 tests-first check `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py` failed as expected because generated HTML contained `src="https://cdn.plot.ly...`.
- 2026-07-08: After CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py` passed with 3 tests.
- 2026-07-08: After CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests` passed with 34 tests.
- 2026-07-08: After CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests` passed.
- 2026-07-08: After CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- 2026-07-08: Strict CR-M3-001 tests-first check `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py` failed as expected because generated HTML contained `https://cdn.plot.ly/un/`.
- 2026-07-08: After strict CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py` passed with 3 tests.
- 2026-07-08: After strict CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests` passed with 34 tests.
- 2026-07-08: After strict CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests` passed.
- 2026-07-08: After strict CR-M3-001 fix, `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- 2026-07-08: M3 strict rereview reran `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py`, which passed with 3 tests.
- 2026-07-08: M3 strict rereview directly generated `chart.html` and confirmed `Plotly.newPlot=True`, `cdn_url=False`, `cdn_src=False`, and `script_charset=False`.
- 2026-07-08: Tests-first M4 check `PATH=.venv/bin:$PATH python -m pytest tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_template_assets.py` failed as expected with missing `qcc_toolkit.templates`.
- 2026-07-08: Focused M4 check `PATH=.venv/bin:$PATH python -m pytest tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_template_assets.py` passed with 11 tests.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed and validated 5 template catalog entries.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m pytest tests` passed with 45 tests.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests` passed.
- 2026-07-08: `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- 2026-07-08: M4 rereview reran `PATH=.venv/bin:$PATH python -m pytest tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id tests/test_template_catalog_failures.py tests/test_template_catalog.py tests/test_method_guides.py tests/test_template_assets.py`, which passed with 13 selected test cases because the targeted test was also included in the file selection.
- 2026-07-08: M4 rereview ran `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`, which passed and validated 5 template catalog entries.
- 2026-07-08: M4 rereview direct mutation probe raised `CatalogValidationError` with `pareto_chart_template markdown_guide docs/methods/check_sheet.md declares method_id 'check_sheet', expected 'pareto_chart'.`
- 2026-07-08: M4 rereview ran `PATH=.venv/bin:$PATH python -m pytest tests`, which passed with 46 tests.
- 2026-07-08: M4 rereview ran `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests examples`, which passed.
- 2026-07-08: M4 rereview ran `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit`, which passed.
- 2026-07-08: M4 rereview ran `git diff --check`, which passed.
- 2026-07-08: CR-M4-001 tests-first check `PATH=.venv/bin:$PATH python -m pytest tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id` failed as expected because mismatched catalog and guide method IDs were accepted.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id` passed.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests/test_template_catalog_failures.py tests/test_template_catalog.py tests/test_method_guides.py tests/test_template_assets.py` passed with 12 tests.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed and validated 5 template catalog entries.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m pytest tests` passed with 46 tests.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests examples` passed.
- 2026-07-08: After CR-M4-001 fix, `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.

## Outcome and retrospective

- M1 closed by code-review.
- M2 closed by code-review.
- M3 is closed by code-review.
- M4 is closed by code-review after CR-M4-001 rereview.
- M5 is the next planned implementation milestone.

## Readiness

- See `Current Handoff Summary`.
- Ready for M5 implementation.
- Not ready for final verification, branch readiness, or PR handoff.
