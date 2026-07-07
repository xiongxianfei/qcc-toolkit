# Project Map

## Map metadata

- Map status: partial
- Scope: repository
- Baseline: `71e4153+dirty`
- Last reviewed: 2026-07-07
- Coverage: root documentation, governance artifacts, workflow guide, vision rationale, security/contribution files, and repository file layout
- Exclusions: `.git/` internals and `.agents/` skill implementation details, except skill skeletons read to create this map
- Parent map: not applicable
- Known gaps: no Python package layout, runtime entry points, implementation modules, data schemas, tests, CI workflows, release automation, specs, architecture docs, plans, or change packs exist yet
- Inspected uncommitted paths: `README.md`, `AGENTS.md`, `CONSTITUTION.md`, `VISION.md`, `docs/workflows.md`, `docs/vision/strategic-positioning.md`

## Purpose and scope

This map orients future work in the repository as it exists now. It records observed current state for standing governance, workflow placement, and repository contents. It does not approve future architecture, define a backlog, or claim implementation readiness.

## System overview

Observed: the repository currently defines a project identity for QCC Toolkit as a Python-first, stage-aware evidence toolkit for Quality Control Circle projects in `VISION.md` and the README vision block in `README.md`.

Observed: repository governance exists in `CONSTITUTION.md`, with a concise agent-facing entry point in `AGENTS.md`.

Observed: workflow artifact placement and lifecycle routing are defined in `docs/workflows.md`. That guide places the root project map at `docs/project-map.md` and records the standard lifecycle from proposal through PR handoff.

Observed: strategic positioning rationale for the vision exists at `docs/vision/strategic-positioning.md`.

Observed: no executable source, package manifest, runtime configuration, tests, or CI workflow files were present in the inspected repository file list.

## Repository layout

- `README.md`: public project entry point with generated vision front-matter and remaining template repository content.
- `VISION.md`: canonical project identity and scope for QCC Toolkit.
- `docs/vision/strategic-positioning.md`: supporting rationale for the current vision.
- `CONSTITUTION.md`: highest operational governance source for agentic development rules.
- `AGENTS.md`: concise agent operating rules that point to the constitution.
- `docs/workflows.md`: project-local workflow and artifact-location guide.
- `CONTRIBUTING.md`: lightweight contribution guidance for focused PRs, tests/docs for behavior changes, and reporting relevant checks.
- `SECURITY.md`: vulnerability reporting policy; currently contains placeholder contact text.
- `CODE_OF_CONDUCT.md`: community behavior expectations; currently contains placeholder contact text.
- `LICENSE`: Apache License 2.0 text.

Observed: there is no `src/`, package directory, `tests/`, `specs/`, `.github/workflows/`, or package configuration file in the inspected file inventory.

## Runtime flow

Not observed in the mapped scope. The repository has no executable source, package manifest, application entry point, command-line entry point, service configuration, or runtime script in the inspected files.

## Data flow

Not observed in the mapped scope. The repository has no implementation data models, schemas, migrations, fixtures, sample datasets, storage configuration, or report-generation code in the inspected files.

Inferred: future data-flow work will likely involve QCC project evidence, stage identifiers, methods, chart specifications, and report artifacts because those concepts are named in `VISION.md` and governance rules in `CONSTITUTION.md`. This is product intent, not observed implementation.

## External boundaries

Observed: `SECURITY.md` describes an external vulnerability reporting path, but the contact value is still the placeholder `<SECURITY_EMAIL>`.

Observed: `CODE_OF_CONDUCT.md` describes an external conduct reporting path, but the contact value is still the placeholder `<MAINTAINER_EMAIL>`.

Not observed in implementation: no runtime external integrations, network services, telemetry, package registries, databases, or third-party APIs are configured in the inspected repository.

## Test map

No test locations or configured test commands were observed. There is no `tests/` directory, package manifest, CI workflow, `pytest.ini`, `tox.ini`, `noxfile.py`, or equivalent test configuration in the inspected file inventory.

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

No build, test, lint, network, or mutating commands were run.

## CI and release map

Not observed in the mapped scope. The inspected file inventory did not include `.github/workflows/`, release configuration, package publication configuration, deployment configuration, or versioning metadata.

Observed: `CONTRIBUTING.md` asks contributors to run relevant checks and mention the commands in pull requests, but no concrete project check commands are configured yet.

## Architecture rules observed

Observed explicit governance rules in `CONSTITUTION.md`:

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
- No package, test, lint, type, CI, or release configuration exists, so future implementation cannot make package-level verification claims until tooling is added.
- No specs or architecture docs exist yet, so the first behavior or architecture change must establish those artifacts before implementation.
- No source layout exists, so future change placement cannot rely on current module boundaries.

## Open questions

- What initial Python package name and source layout should the project use?
- Which tooling will define package management, tests, linting, typing, formatting, and release/versioning?
- What concrete maintainer and security contact addresses should replace the placeholders?
- Should the template README sections be replaced before public use?
- Which first QCC behavior should enter the proposal/spec workflow?

## Evidence trail

| Evidence | Type | Result |
| --- | --- | --- |
| `VISION.md` | source | Defines QCC Toolkit product identity, audience, commitments, refusals, and falsifiability. |
| `README.md` | source | Contains generated vision front-matter plus remaining template repository content. |
| `docs/vision/strategic-positioning.md` | source | Records positioning as a stage-aware QCC evidence toolkit for Python. |
| `CONSTITUTION.md` | source | Defines governance, source-of-truth order, spec/test/architecture/security/verification/review/documentation rules. |
| `AGENTS.md` | source | Provides concise agent-facing operating rules linked to `CONSTITUTION.md`. |
| `docs/workflows.md` | source | Defines project-local lifecycle graph, artifact registry, review placement, and map path. |
| `CONTRIBUTING.md` | source | Defines lightweight PR and issue expectations. |
| `SECURITY.md` | source | Defines vulnerability reporting shape with placeholder contact. |
| `CODE_OF_CONDUCT.md` | source | Defines conduct expectations and placeholder reporting contact. |
| `LICENSE` | source | Apache License 2.0. |
| `rg --files` | executed command | Exit 0; showed documentation-only repository file inventory. |
| `git rev-parse --short HEAD && git status --short` | executed command | Exit 0; baseline `71e4153` with uncommitted documentation changes. |
| `find . -maxdepth 3 -type f -not -path './.git/*' -not -path './.agents/*' | sort` | executed command | Exit 0; confirmed visible project files at depth 3. |
