# Project Map

## Map metadata

- Map status: partial
- Scope: repository
- Baseline: `6c752fe`
- Last reviewed: 2026-07-08
- Coverage: root documentation, governance artifacts, workflow guide, vision rationale, accepted proposal, approved first-slice spec, architecture package, ADRs, plan index, first-slice plan, change pack, Python package, method guides, template catalog, real PPTX method templates, template source notes, synthetic example project, starter script, tests, security/contribution files, and repository file layout
- Exclusions: `.git/` internals and `.agents/` skill implementation details, except skill skeletons read to create this map
- Parent map: not applicable
- Known gaps: no hosted CI workflows, release automation, automated PPTX generation, web UI, dashboard, CAPA/EQMS workflow, Control Chart support, or advanced QCC methods exist yet
- Inspected uncommitted paths: none at map refresh start

## Purpose and scope

This map orients future work in the repository as it exists now. It records observed current state for standing governance, workflow placement, and repository contents. It does not approve future architecture, define a backlog, or claim implementation readiness.

## System overview

Observed: the repository currently defines a project identity for QCC Toolkit as a template-backed, Python-powered evidence system for Quality Control Circle methods and projects in `VISION.md`, `CONSTITUTION.md`, `AGENTS.md`, and the README vision block in `README.md`.

Observed: repository governance exists in `CONSTITUTION.md`, with a concise agent-facing entry point in `AGENTS.md`.

Observed: workflow artifact placement and lifecycle routing are defined in `docs/workflows.md`. That guide places the root project map at `docs/project-map.md` and records the standard lifecycle from proposal through PR handoff.

Observed: strategic positioning rationale for the vision exists at `docs/vision/strategic-positioning.md`.

Observed: an accepted proposal at `docs/proposals/2026-07-07-create-qcc-toolkit.md` records the recommended template-backed direction.

Observed: an approved first-slice feature spec at `specs/qcc-toolkit-first-slice.md` defines the Pareto-centered first usable slice.

Observed: an approved canonical architecture package at `docs/architecture/system/architecture.md` defines the first-slice package boundaries, evidence flow, deployment view, crosscutting rules, and links to ADRs.

Observed: accepted ADRs at `docs/adr/ADR-20260708-python-local-first-stack.md` and `docs/adr/ADR-20260708-evidence-package-boundary.md` record durable first-slice decisions.

Observed: the change pack at `docs/changes/2026-07-07-create-qcc-toolkit/` records proposal review, spec review, architecture review, upstream status settlement, and current lifecycle metadata.

Observed: the plan index at `docs/plan.md` records the active first-slice plan, and the plan body at `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md` sequences implementation milestones.

Observed: M1-M7 are closed by code review.
The repository now includes a local-first Python package, Pareto method engine, chart specification and rendering adapter, evidence package writer, report writer, template catalog validator, Markdown method guides, real PPTX method templates with reviewable Markdown source notes, a Pareto starter script, synthetic example project, and automated tests.

## Repository layout

- `README.md`: public project entry point with generated vision front-matter and remaining template repository content.
- `VISION.md`: canonical project identity and scope for QCC Toolkit.
- `docs/vision/strategic-positioning.md`: supporting rationale for the current vision.
- `docs/proposals/2026-07-07-create-qcc-toolkit.md`: accepted proposal for creating QCC Toolkit.
- `specs/qcc-toolkit-first-slice.md`: approved feature spec for the Pareto-centered first usable slice.
- `docs/architecture/system/architecture.md`: approved canonical architecture package for the first slice.
- `docs/architecture/system/diagrams/context.mmd`: C4 system context diagram source.
- `docs/architecture/system/diagrams/container.mmd`: C4 container diagram source.
- `docs/adr/ADR-20260708-python-local-first-stack.md`: accepted ADR for local-first Python package and dependency stack.
- `docs/adr/ADR-20260708-evidence-package-boundary.md`: accepted ADR for generated evidence package authority.
- `docs/changes/2026-07-07-create-qcc-toolkit/`: lifecycle change pack with review records, review log, review-resolution evidence, change metadata, and explain-change artifact.
- `docs/plan.md`: active plan index.
- `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`: active implementation plan for the first slice.
- `docs/methods/`: Markdown method guides for Pareto Chart, Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys.
- `templates/ppt/catalog.yml`: template catalog linking first-slice PPTX method templates to guides, source notes, scripts, example project, placeholders, and expected assets.
- `templates/ppt/methods/*.pptx`: real editable PowerPoint method templates for first-slice methods.
- `templates/ppt/sources/*.md`: reviewable source notes for the PPTX method templates.
- `tools/build_ppt_templates.py`: deterministic builder for regenerating the first-slice PPTX method templates from the catalog contract.
- `examples/scripts/generate_pareto.py`: local Pareto starter script that calls the public package API.
- `examples/projects/reduce-packing-label-errors/`: synthetic example project with sample defect data and ignored generated evidence/report folders.
- `pyproject.toml`: Python package metadata and pytest/Ruff/mypy configuration.
- `qcc_toolkit/__init__.py`: public package import surface and first-slice API exports.
- `qcc_toolkit/analysis.py`: Pareto validation and calculation behavior.
- `qcc_toolkit/charts.py`: Pareto chart specification and Plotly HTML rendering adapter.
- `qcc_toolkit/contracts.py`: public data contracts and validation error types.
- `qcc_toolkit/evidence.py`: method-scoped evidence package writer.
- `qcc_toolkit/interpretation.py`: deterministic Pareto captions and warnings.
- `qcc_toolkit/methods.py`: first-slice method registry.
- `qcc_toolkit/reports.py`: Markdown and HTML report-ready output writer.
- `qcc_toolkit/stages.py`: canonical QCC stage registry.
- `qcc_toolkit/templates/`: template catalog loading, validation, and CLI entry point.
- `qcc_toolkit/py.typed`: typed package marker.
- `tests/`: automated unit, integration, smoke, scope, lifecycle, template, guide, reproducibility, and acceptance tests for the first slice.
- `CONSTITUTION.md`: highest operational governance source for agentic development rules.
- `AGENTS.md`: concise agent operating rules that point to the constitution.
- `docs/workflows.md`: project-local workflow and artifact-location guide.
- `CONTRIBUTING.md`: lightweight contribution guidance for focused PRs, tests/docs for behavior changes, and reporting relevant checks.
- `SECURITY.md`: vulnerability reporting policy; currently contains placeholder contact text.
- `CODE_OF_CONDUCT.md`: community behavior expectations; currently contains placeholder contact text.
- `LICENSE`: Apache License 2.0 text.

Observed: there is no `src/` layout or `.github/workflows/`.
No hosted CI, release workflow, web UI, dashboard, CAPA/EQMS workflow, automated PPTX generation, Control Chart implementation, or advanced QCC method implementation is present.

## Runtime flow

Observed runtime flow is local script and library execution.
The Pareto starter script loads a local CSV, accepts explicit category/count/project/output inputs, calls the public `qcc_toolkit` API, validates inputs, calculates Pareto rows, builds chart specification and HTML, writes a method-scoped evidence package, and updates Markdown/HTML report-ready outputs.
The template catalog validator can be run through `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`.
No service process, web entry point, telemetry path, or hosted dependency is configured.

## Data flow

Observed data flow starts from synthetic CSV data under `examples/projects/reduce-packing-label-errors/data/`.
Pareto calculation outputs flow into chart specs, captions, warnings, metadata, calculated tables, chart HTML, README/manifest-style evidence notes, and report-ready Markdown/HTML outputs under ignored generated folders.
Template and method-guide data flow is governed by `templates/ppt/catalog.yml`, `docs/methods/*.md`, and catalog validation.
No database, migrations, persistent service storage, or external data transmission path is configured.

## External boundaries

Observed: `SECURITY.md` describes an external vulnerability reporting path, but the contact value is still the placeholder `<SECURITY_EMAIL>`.

Observed: `CODE_OF_CONDUCT.md` describes an external conduct reporting path, but the contact value is still the placeholder `<MAINTAINER_EMAIL>`.

Not observed in implementation: no runtime external integrations, network services, telemetry, package registries, databases, or third-party APIs are configured.
Plotly is used locally for HTML chart rendering; generated chart HTML is configured for local/offline use rather than CDN use.

## Test map

Observed: the test suite covers package import, method and stage registries, Pareto calculation and validation, warnings, interpretation, chart specs and HTML rendering, evidence packages, reproducibility, method guides, template catalog validation and failure modes, real PPTX template assets, starter script behavior, synthetic data boundaries, reports, scope guards, artifact consistency, and acceptance lifecycle checks.
The configured local validation commands include `python -m pytest`, `python -m ruff check .`, `python -m mypy qcc_toolkit`, `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`, and the documented Pareto starter script command.
No CI workflow, `tox.ini`, or `noxfile.py` is present.

Executed read-only inspection commands during this mapping session:

- `sed -n '1,360p' .agents/skills/project-map/SKILL.md`: exit code 0
- `find .agents/skills/project-map -maxdepth 3 -type f -print | sort`: exit code 0
- `git rev-parse --short HEAD && git status --short`: exit code 0
- `rg --files`: exit code 0
- `sed -n '1,260p' .agents/skills/project-map/assets/project-map-skeleton.md`: exit code 0
- `sed -n '1,220p' docs/workflows.md`: exit code 0
- `sed -n '1,220p' SECURITY.md`: exit code 0
- `sed -n '1,220p' CODE_OF_CONDUCT.md`: exit code 0
- `sed -n '1,220p' LICENSE`: exit code 0
- `sed -n '1,220p' CONTRIBUTING.md`: exit code 0
- `find . -maxdepth 3 -type d -not -path './.git*' -not -path './.agents*' | sort`: exit code 0
- `find . -maxdepth 3 -type f -not -path './.git/*' -not -path './.agents/*' | sort`: exit code 0

Implementation milestones ran package, test, lint, type, catalog, starter-script, and git whitespace checks in an ignored `.venv`; see the active plan validation notes and verify report for exact commands and results.

## CI and release map

Not observed in the mapped scope. The inspected file inventory did not include `.github/workflows/`, release configuration, package publication configuration, or deployment configuration. Package version metadata currently exists in `pyproject.toml` and `qcc_toolkit.__version__`.

Observed: `CONTRIBUTING.md` asks contributors to run relevant checks and mention the commands in pull requests.
Concrete local validation commands are configured in `pyproject.toml`, the test spec, the active plan, and package entry points, but no hosted CI workflow is present.

## Architecture rules observed

Observed explicit governance rules in `CONSTITUTION.md`:

- PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates traceable QCC evidence.
- QCC charts and reports are traceable project evidence, not decorative visuals or isolated plotting utilities.
- Behavior changes affecting public API, QCC stages, method contracts, statistical calculations, chart outputs, report artifacts, configuration, compatibility, security, privacy, or user-facing workflow require a spec before implementation.
- Implementation work that changes behavior starts from a test, fixture, or executable proof when practical.
- The intended architectural boundaries are QCC project and stage model, method contracts and data validation, statistical calculation logic, chart specification, rendering backends, and interpretation/report artifacts.
- Calculation logic must not depend on a rendering backend, rendering must preserve review metadata, and report generation must not hide data, parameters, assumptions, warnings, or method context.

Observed workflow rules in `docs/workflows.md`:

- New workflow-managed artifacts use the project-local paths recorded in the artifact registry.
- Formal review records live under `docs/changes/<change-id>/reviews/`.
- Project-map content is owned by the `project-map` skill and this root map path is `docs/project-map.md`.

## Risk areas

- Placeholder contacts remain in `SECURITY.md` and `CODE_OF_CONDUCT.md`, so reporting paths are not operationally usable yet.
- `README.md` still contains template repository content after the vision block, which may mislead readers about project maturity and included files.
- First-slice public APIs and evidence metadata are pre-1.0 and may need compatibility refinement through future specs.
- No CI or release configuration exists.
- PPTX template visual quality remains a human-review concern even though automated tests validate file existence, placeholders, demo labels, and deterministic package metadata.
- Control Chart and advanced QCC methods are intentionally outside the first vertical proof slice.

## Open questions

- Should the repository keep the root package layout or move to `src/` before public release?
- Which CI workflow should run package management, tests, linting, typing, catalog validation, and starter-script smoke checks?
- What concrete maintainer and security contact addresses should replace the placeholders?
- Should the template README sections be replaced before public use?
- Which next QCC method should enter the proposal/spec workflow after Pareto?

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `VISION.md` | source | Defines QCC Toolkit product identity, audience, commitments, refusals, and falsifiability. |
| `README.md` | source | Contains generated vision front-matter plus remaining template repository content. |
| `docs/vision/strategic-positioning.md` | source | Records positioning as a template-backed, Python-powered evidence system for QCC methods. |
| `docs/proposals/2026-07-07-create-qcc-toolkit.md` | source | Records accepted proposal for template-backed QCC Toolkit direction. |
| `specs/qcc-toolkit-first-slice.md` | source | Records approved first-slice behavior contract. |
| `docs/architecture/system/architecture.md` | source | Records approved first-slice architecture package. |
| `docs/adr/ADR-20260708-python-local-first-stack.md` | source | Records accepted local-first Python package stack decision. |
| `docs/adr/ADR-20260708-evidence-package-boundary.md` | source | Records accepted evidence package boundary decision. |
| `CONSTITUTION.md` | source | Defines governance, source-of-truth order, spec/test/architecture/security/verification/review/documentation rules. |
| `AGENTS.md` | source | Provides concise agent-facing operating rules linked to `CONSTITUTION.md`. |
| `docs/workflows.md` | source | Defines project-local lifecycle graph, artifact registry, review placement, and map path. |
| `CONTRIBUTING.md` | source | Defines lightweight PR and issue expectations. |
| `SECURITY.md` | source | Defines vulnerability reporting shape with placeholder contact. |
| `CODE_OF_CONDUCT.md` | source | Defines conduct expectations and placeholder reporting contact. |
| `LICENSE` | source | Apache License 2.0. |
| `rg --files` | executed command | Exit 0; showed first-slice repository file inventory. |
| `git status --short --branch` | executed command | Exit 0; branch `proposal/create-qcc-toolkit` was clean before verify drift edits. |
| `find qcc_toolkit -maxdepth 3 -type f -print | sort` | executed command | Exit 0; confirmed package files and ignored cache files. |
| `find examples docs/methods templates/ppt tests -maxdepth 3 -type f -print | sort` | executed command | Exit 0; confirmed guides, templates, examples, tests, and ignored cache files. |
