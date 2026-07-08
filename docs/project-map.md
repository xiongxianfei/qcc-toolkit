# Project Map

## Map metadata

- Map status: partial
- Scope: repository
- Baseline: `2e91f93+dirty`
- Last reviewed: 2026-07-08
- Coverage: root documentation, governance artifacts, workflow guide, vision rationale, active proposal, first-slice spec, architecture package, ADRs, plan index, first-slice plan, change pack, M1 package scaffold, security/contribution files, and repository file layout
- Exclusions: `.git/` internals and `.agents/` skill implementation details, except skill skeletons read to create this map
- Parent map: not applicable
- Known gaps: no QCC method behavior, runtime entry points, data schemas, method docs, templates, examples, CI workflows, release automation, or evidence-generation implementation exists yet
- Inspected uncommitted paths: `README.md`, `AGENTS.md`, `CONSTITUTION.md`, `VISION.md`, `docs/vision/strategic-positioning.md`, `docs/proposals/2026-07-07-create-qcc-toolkit.md`, `specs/qcc-toolkit-first-slice.md`, `docs/architecture/system/architecture.md`, `docs/adr/ADR-20260708-python-local-first-stack.md`, `docs/adr/ADR-20260708-evidence-package-boundary.md`, `docs/plan.md`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/project-map.md`

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

Observed: M1 added `pyproject.toml`, the `qcc_toolkit` package scaffold, and `tests/test_import.py`. No QCC method behavior, runtime command, evidence generation, or CI workflow files are present yet.

## Repository layout

- `README.md`: public project entry point with generated vision front-matter and remaining template repository content.
- `VISION.md`: canonical project identity and scope for QCC Toolkit.
- `docs/vision/strategic-positioning.md`: supporting rationale for the current vision.
- `docs/proposals/2026-07-07-create-qcc-toolkit.md`: accepted proposal for creating QCC Toolkit.
- `specs/qcc-toolkit-first-slice.md`: approved feature spec for the Pareto-centered first usable slice.
- `docs/architecture/system/architecture.md`: draft canonical architecture package for the first slice.
- `docs/architecture/system/diagrams/context.mmd`: C4 system context diagram source.
- `docs/architecture/system/diagrams/container.mmd`: C4 container diagram source.
- `docs/adr/ADR-20260708-python-local-first-stack.md`: accepted ADR for local-first Python package and dependency stack.
- `docs/adr/ADR-20260708-evidence-package-boundary.md`: accepted ADR for generated evidence package authority.
- `docs/changes/2026-07-07-create-qcc-toolkit/`: lifecycle change pack with proposal review, spec review, review log, and change metadata.
- `docs/plan.md`: active plan index.
- `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`: active implementation plan for the first slice.
- `pyproject.toml`: Python package metadata and pytest/Ruff/mypy configuration for the M1 scaffold.
- `qcc_toolkit/__init__.py`: minimal public package import surface with `__version__`.
- `qcc_toolkit/py.typed`: typed package marker.
- `tests/test_import.py`: M1 import smoke test.
- `CONSTITUTION.md`: highest operational governance source for agentic development rules.
- `AGENTS.md`: concise agent operating rules that point to the constitution.
- `docs/workflows.md`: project-local workflow and artifact-location guide.
- `CONTRIBUTING.md`: lightweight contribution guidance for focused PRs, tests/docs for behavior changes, and reporting relevant checks.
- `SECURITY.md`: vulnerability reporting policy; currently contains placeholder contact text.
- `CODE_OF_CONDUCT.md`: community behavior expectations; currently contains placeholder contact text.
- `LICENSE`: Apache License 2.0 text.

Observed: there is no `src/` layout, `.github/workflows/`, runtime CLI, method implementation modules, templates, examples, or evidence-generation code in the inspected file inventory.

## Runtime flow

Not observed in the mapped scope beyond package import. The repository has a minimal importable `qcc_toolkit` package, but no application entry point, command-line entry point, service configuration, runtime script, or QCC method behavior in the inspected files.

## Data flow

Not observed in the mapped scope. The repository has no implementation data models, schemas, migrations, fixtures, sample datasets, storage configuration, or report-generation code in the inspected files.

Inferred: future data-flow work will likely involve QCC method templates, Markdown method guides, stage identifiers, data contracts, chart specifications, evidence packages, and report artifacts because those concepts are named in `VISION.md`, `CONSTITUTION.md`, and the active proposal. This is product intent, not observed implementation.

## External boundaries

Observed: `SECURITY.md` describes an external vulnerability reporting path, but the contact value is still the placeholder `<SECURITY_EMAIL>`.

Observed: `CODE_OF_CONDUCT.md` describes an external conduct reporting path, but the contact value is still the placeholder `<MAINTAINER_EMAIL>`.

Not observed in implementation: no runtime external integrations, network services, telemetry, package registries, databases, or third-party APIs are configured in the inspected repository.

## Test map

Observed: M1 added `tests/test_import.py` and pytest configuration in `pyproject.toml`.
The configured local validation commands are `python -m pytest`, `python -m ruff check .`, and `python -m mypy qcc_toolkit` after installing the package with development dependencies.
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

M1 implementation later ran package, test, lint, and type checks in an ignored `.venv`; see the active plan validation notes for exact commands and results.

## CI and release map

Not observed in the mapped scope. The inspected file inventory did not include `.github/workflows/`, release configuration, package publication configuration, or deployment configuration. Package version metadata currently exists in `pyproject.toml` and `qcc_toolkit.__version__`.

Observed: `CONTRIBUTING.md` asks contributors to run relevant checks and mention the commands in pull requests, but no concrete project check commands are configured yet.

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
- Package, test, lint, and type configuration now exists, but only for the M1 import scaffold.
- No CI or release configuration exists.
- No QCC method modules exist yet, so future method work must establish module boundaries under the approved architecture.

## Open questions

- Should the repository keep the root package layout or move to `src/` before public release?
- Which CI workflow should run package management, tests, linting, typing, and release checks?
- What concrete maintainer and security contact addresses should replace the placeholders?
- Should the template README sections be replaced before public use?
- Which first QCC behavior should enter the proposal/spec workflow?

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `VISION.md` | source | Defines QCC Toolkit product identity, audience, commitments, refusals, and falsifiability. |
| `README.md` | source | Contains generated vision front-matter plus remaining template repository content. |
| `docs/vision/strategic-positioning.md` | source | Records positioning as a template-backed, Python-powered evidence system for QCC methods. |
| `docs/proposals/2026-07-07-create-qcc-toolkit.md` | source | Records accepted proposal for template-backed QCC Toolkit direction. |
| `specs/qcc-toolkit-first-slice.md` | source | Records approved first-slice behavior contract. |
| `docs/architecture/system/architecture.md` | source | Records draft first-slice architecture package. |
| `docs/adr/ADR-20260708-python-local-first-stack.md` | source | Records accepted local-first Python package stack decision. |
| `docs/adr/ADR-20260708-evidence-package-boundary.md` | source | Records accepted evidence package boundary decision. |
| `CONSTITUTION.md` | source | Defines governance, source-of-truth order, spec/test/architecture/security/verification/review/documentation rules. |
| `AGENTS.md` | source | Provides concise agent-facing operating rules linked to `CONSTITUTION.md`. |
| `docs/workflows.md` | source | Defines project-local lifecycle graph, artifact registry, review placement, and map path. |
| `CONTRIBUTING.md` | source | Defines lightweight PR and issue expectations. |
| `SECURITY.md` | source | Defines vulnerability reporting shape with placeholder contact. |
| `CODE_OF_CONDUCT.md` | source | Defines conduct expectations and placeholder reporting contact. |
| `LICENSE` | source | Apache License 2.0. |
| `rg --files` | executed command | Exit 0; showed documentation-only repository file inventory. |
| `git rev-parse --short HEAD && git status --short` | executed command | Exit 0; baseline `2e91f93` with uncommitted documentation changes. |
| `find . -maxdepth 3 -type f -not -path './.git/*' -not -path './.agents/*' | sort` | executed command | Exit 0; confirmed visible project files at depth 3. |
