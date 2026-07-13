# Project Map

## Map metadata

- Map status: partial
- Scope: repository
- Baseline: `8b6c976+dirty`
- Last reviewed: 2026-07-09
- Coverage: root documentation, governance artifacts, workflow guide, vision rationale, proposal history, approved first-slice specs, architecture package, ADRs, plan index, implementation plans, change packs, Python package, method kits, method guides, template catalog, real PPTX method templates, template source notes, synthetic example project, starter script, tests, security/contribution files, and repository file layout
- Exclusions: `.git/` internals and `.agents/` skill implementation details, except skill skeletons read to create this map
- Parent map: not applicable
- Known gaps: no hosted CI workflows, release automation, automated PPTX generation, web UI, dashboard, CAPA/EQMS workflow, Control Chart support, or advanced QCC methods exist yet
- Inspected uncommitted paths: `AGENTS.md`, `CONSTITUTION.md`, `README.md`, `VISION.md`, `docs/vision/strategic-positioning.md`, `docs/proposals/2026-07-07-create-qcc-toolkit.md`, `docs/proposals/2026-07-08-improve-qcc-method-templates.md`, `docs/proposals/2026-07-09-markdown-first-method-guides.md`, `docs/changes/2026-07-09-markdown-first-method-guides/`, `specs/qcc-toolkit-first-slice.md`, `specs/qcc-method-kits.md`

## Purpose and scope

This map orients future work in the repository as it exists now. It records observed current state for standing governance, workflow placement, and repository contents. It does not approve future architecture, define a backlog, or claim implementation readiness.

## System overview

Observed: the repository currently defines a project identity for QCC Toolkit as a Markdown-first guide system for Quality Control Circle methods and projects in `VISION.md`, `CONSTITUTION.md`, `AGENTS.md`, and the README vision block in `README.md`.

Observed: repository governance exists in `CONSTITUTION.md`, with a concise agent-facing entry point in `AGENTS.md`.

Observed: workflow artifact placement and lifecycle routing are defined in `docs/workflows.md`. That guide places the root project map at `docs/project-map.md` and records the standard lifecycle from proposal through PR handoff.

Observed: strategic positioning rationale for the vision exists at `docs/vision/strategic-positioning.md`.

Observed: proposal history at `docs/proposals/2026-07-07-create-qcc-toolkit.md`, `docs/proposals/2026-07-08-improve-qcc-method-templates.md`, and `docs/proposals/2026-07-09-markdown-first-method-guides.md` records the direction history from template-backed evidence tooling to PowerPoint-first method kits and then to the accepted Markdown-first method-guidance direction.

Observed: an approved first-slice feature spec at `specs/qcc-toolkit-first-slice.md` defines the earlier Pareto-centered first usable slice.
Observed: an approved Markdown-first method-guidance spec at `specs/markdown-first-method-guidance.md` defines the current method-kit guidance contract.

Observed: an approved canonical architecture package at `docs/architecture/system/architecture.md` defines the first-slice package boundaries, evidence flow, deployment view, crosscutting rules, and links to ADRs.

Observed: accepted ADRs at `docs/adr/ADR-20260708-python-local-first-stack.md` and `docs/adr/ADR-20260708-evidence-package-boundary.md` record durable first-slice decisions.

Observed: the change packs under `docs/changes/` record proposal review, spec review, architecture review, upstream status settlement, implementation review evidence, positioning rationale, and lifecycle metadata for completed changes.

Observed: the plan index at `docs/plan.md` records no active plans and lists the merged first-slice, method-template, and Markdown-first method-guidance plans as recently done.

Observed: M1-M7 for the earlier first slice are closed by code review.
The repository now includes a local-first Python package, Pareto method engine, chart specification and rendering adapter, evidence package writer, report writer, template catalog validator, Markdown method guides, a QCC project-story guide, a Markdown-first Pareto method kit, real PPTX method templates with reviewable Markdown source notes, a Pareto starter script, synthetic example project, and automated tests.
Existing Python and PowerPoint assets are optional execution aids under the current Markdown-first direction.

## Repository layout

- `README.md`: public project entry point with generated vision front-matter, method-kit pointer, local development commands, and optional-aid positioning.
- `VISION.md`: canonical project identity and scope for QCC Toolkit.
- `docs/vision/strategic-positioning.md`: supporting rationale for the current vision.
- `docs/proposals/2026-07-07-create-qcc-toolkit.md`: superseded proposal for creating QCC Toolkit.
- `docs/proposals/2026-07-08-improve-qcc-method-templates.md`: superseded proposal for PowerPoint-first method-template improvement.
- `docs/proposals/2026-07-09-markdown-first-method-guides.md`: accepted proposal for the current Markdown-first method-guide direction.
- `specs/qcc-toolkit-first-slice.md`: approved feature spec for the Pareto-centered first usable slice.
- `docs/architecture/system/architecture.md`: approved canonical architecture package for the first slice.
- `docs/architecture/system/diagrams/context.mmd`: C4 system context diagram source.
- `docs/architecture/system/diagrams/container.mmd`: C4 container diagram source.
- `docs/adr/ADR-20260708-python-local-first-stack.md`: accepted ADR for local-first Python package and dependency stack.
- `docs/adr/ADR-20260708-evidence-package-boundary.md`: accepted ADR for generated evidence package authority.
- `docs/changes/2026-07-07-create-qcc-toolkit/`: lifecycle change pack with review records, review log, review-resolution evidence, change metadata, and explain-change artifact.
- `docs/changes/2026-07-09-markdown-first-method-guides/`: lifecycle change pack with metadata and explain-change artifact for the substantive governance and vision repositioning.
- `docs/plan.md`: plan index with recently completed merged plans.
- `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`: completed implementation plan for the first slice.
- `docs/plans/2026-07-08-improve-qcc-method-templates.md`: completed implementation plan for method-template improvements.
- `docs/plans/2026-07-09-markdown-first-method-guidance.md`: completed implementation plan for Markdown-first method guidance.
- `method-kits/`: Markdown-first method-guide root; one method guide should be one Markdown file until it needs multiple guide files.
- `docs/templates/`: reusable Markdown templates for method guides and image prompts.
- `docs/qcc-project-story.md`: Markdown guide that connects method choices across the QCC project story from problem selection through standardization.
- `method-kits/pareto-chart.md`: first complete Markdown-first method guide.
- `method-kits/metadata/pareto-chart.yml`: machine-readable metadata sidecar for the Pareto method guide.
- `media/prompts/`: per-image prompt records for generated teaching visuals.
- `media/`: media root for reviewed teaching visuals.
- `method-kits/`: canonical Markdown-first method kits for QCC methods.
- `docs/methods-key-content.md`: extracted legacy guide content retained as source material, not an active guide surface.
- `templates/ppt/catalog.yml`: optional execution-aid catalog linking first-slice PPTX method templates to guides, source notes, placeholders, and expected assets.
- `templates/ppt/methods/*.pptx`: real editable PowerPoint method templates for first-slice methods; optional execution aids under the current product identity.
- `templates/ppt/sources/*.md`: reviewable source notes for the PPTX method templates.
- `tools/build_ppt_templates.py`: deterministic builder for regenerating the first-slice PPTX method templates from the catalog contract.
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

Observed Python package data flow starts from caller-provided records or CSV-like inputs in tests.
Pareto calculation outputs flow into chart specs, captions, warnings, metadata, calculated tables, chart HTML, README/manifest-style evidence notes, and report-ready Markdown/HTML outputs when optional automation is used.
Template and method-guide data flow is governed by `templates/ppt/catalog.yml`, `method-kits/*.md`, and catalog validation.
No database, migrations, persistent service storage, or external data transmission path is configured.

## External boundaries

Observed: `SECURITY.md` describes an external vulnerability reporting path, but the contact value is still the placeholder `<SECURITY_EMAIL>`.

Observed: `CODE_OF_CONDUCT.md` describes an external conduct reporting path, but the contact value is still the placeholder `<MAINTAINER_EMAIL>`.

Not observed in implementation: no runtime external integrations, network services, telemetry, package registries, databases, or third-party APIs are configured.
Plotly is used locally for HTML chart rendering; generated chart HTML is configured for local/offline use rather than CDN use.

## Test map

Observed: the test suite covers package import, method and stage registries, Pareto calculation and validation, warnings, interpretation, chart specs and HTML rendering, evidence packages, method guides, template catalog validation and failure modes, real PPTX template assets, reports, scope guards, artifact consistency, and acceptance lifecycle checks.
The configured local validation commands include `python -m pytest`, `python -m ruff check .`, `python -m mypy qcc_toolkit`, and `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`.
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

Implementation milestones ran package, test, lint, type, catalog, starter-script, and git whitespace checks in an ignored `.venv`; see the completed plan validation notes and verify reports for exact commands and results.

## CI and release map

Not observed in the mapped scope. The inspected file inventory did not include `.github/workflows/`, release configuration, package publication configuration, or deployment configuration. Package version metadata currently exists in `pyproject.toml` and `qcc_toolkit.__version__`.

Observed: `CONTRIBUTING.md` asks contributors to run relevant checks and mention the commands in pull requests.
Concrete local validation commands are configured in `pyproject.toml`, the test specs, completed plans, and package entry points, but no hosted CI workflow is present.

## Architecture rules observed

Observed explicit governance rules in `CONSTITUTION.md`:

- Markdown governs QCC method knowledge and chart-quality expectations; generated images teach concepts but do not serve as quantitative evidence; specific charting, analysis, presentation, or programming tools are optional execution choices rather than the project identity.
- Manual chart-creation guidance is a core competency, and data-dependent final charts remain supported by source data, scope, assumptions, interpretation, and review evidence regardless of tool.
- Behavior changes affecting public API, QCC stages, method-guide structure, chart-creation guidance, evidence checklist policy, image-assisted demonstration policy, method contracts, statistical calculations, chart outputs, report artifacts, configuration, compatibility, security, privacy, or user-facing workflow require a spec before implementation.
- Implementation work that changes behavior starts from a test, fixture, or executable proof when practical.
- The intended architectural boundaries are QCC project and stage model, Markdown method-guide standards, manual chart-creation guidance and chart-quality standards, image prompt and reviewed teaching-visual assets, method contracts and data validation when automation is used, statistical calculation logic when automation is used, chart specification and rendering backends when automation is used, and interpretation/evidence/report artifacts.
- Calculation logic must not depend on a rendering backend, rendering must preserve review metadata, and report generation must not hide data, parameters, assumptions, warnings, or method context.

Observed workflow rules in `docs/workflows.md`:

- New workflow-managed artifacts use the project-local paths recorded in the artifact registry.
- Formal review records live under `docs/changes/<change-id>/reviews/`.
- Project-map content is owned by the `project-map` skill and this root map path is `docs/project-map.md`.

## Risk areas

- Placeholder contacts remain in `SECURITY.md` and `CODE_OF_CONDUCT.md`, so reporting paths are not operationally usable yet.
- First-slice public APIs and evidence metadata are pre-1.0 and may need compatibility refinement through future specs.
- Existing specs, architecture records, package metadata, and implementation artifacts still reflect earlier first-slice and PowerPoint-first directions where they describe already-built behavior; downstream specifications need to align future work with the current Markdown-first vision.
- No CI or release configuration exists.
- PPTX template visual quality remains a human-review concern even though automated tests validate file existence, placeholders, demo labels, and deterministic package metadata.
- Control Chart and advanced QCC methods are intentionally outside the first vertical proof slice.

## Open questions

- Should the repository keep the root package layout or move to `src/` before public release?
- Which CI workflow should run package management, tests, linting, typing, catalog validation, and starter-script smoke checks?
- What concrete maintainer and security contact addresses should replace the placeholders?
- Should the template README sections be replaced before public use?
- Which next QCC method should enter the proposal/spec workflow after Pareto?
- Which existing specs or architecture records should be superseded, amended, or left as historical implementation records after the Markdown-first repositioning?

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `VISION.md` | source | Defines QCC Toolkit product identity, audience, commitments, refusals, and falsifiability. |
| `README.md` | source | Contains generated vision front-matter, method-kit pointer, optional-aid positioning, and local development commands. |
| `docs/vision/strategic-positioning.md` | source | Records positioning as a Markdown-first QCC method-guide and chart-quality guidance system. |
| `docs/proposals/2026-07-09-markdown-first-method-guides.md` | source | Records accepted proposal for the current Markdown-first method-guide direction. |
| `docs/proposals/2026-07-07-create-qcc-toolkit.md` | source | Records earlier superseded proposal for template-backed QCC Toolkit direction. |
| `docs/proposals/2026-07-08-improve-qcc-method-templates.md` | source | Records earlier superseded proposal for PowerPoint-first method-template improvement. |
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
| `sed -n '1,260p' .agents/skills/project-map/SKILL.md` | executed command | Exit 0; read project-map refresh rules for this targeted identity refresh. |
