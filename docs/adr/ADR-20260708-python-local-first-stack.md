# ADR-20260708-python-local-first-stack: Local-First Python Package Stack

## Status

accepted

Allowed statuses: `draft`, `proposed`, `accepted`, `active`, `deprecated`, `superseded`, `archived`, `abandoned`.

## Context

The accepted proposal and approved first-slice spec require QCC Toolkit to be template-backed and Python-powered.
The first slice must run locally, generate Pareto evidence from local data, provide Markdown guides and static PPT templates, and avoid web UI, dashboard, CAPA/EQMS, telemetry, and automated PPTX generation.

The architecture must settle enough package and dependency direction for implementation planning without overcommitting to future UI or advanced statistical scope.

## Decision

Use a local-first Python package architecture for the first slice.

The package is named `qcc_toolkit` and is configured through `pyproject.toml`.
The first supported Python range is 3.11 through 3.14.

Use pandas-compatible tabular inputs as the first data interface.
Use Pydantic-style structured models for method parameters, validation results, chart specs, warnings, evidence metadata, and catalog records.
Use Plotly as the first interactive chart renderer.
Use local static image export through the maintained Plotly/Kaleido path when available, but treat PNG export as optional.

Starter scripts are local Python CLI wrappers around public package APIs.
Static PPT templates ship as user-facing assets.
Automated PPTX generation is deferred until evidence package and placeholder contracts stabilize.

## Alternatives considered

| Alternative | Reason not chosen |
|---|---|
| Template-only first | Does not protect formula correctness, reproducibility, or evidence traceability. |
| Full web app first | Adds UI and operational complexity before method contracts and evidence formats stabilize. |
| Multiple DataFrame engines at launch | Adds adapter complexity before first-slice behavior is proven. |
| Automated PPTX generation in first slice | Couples implementation to template placeholder mechanics before report and evidence contracts are stable. |
| Static image-only charts | Weakens review and exploratory use; HTML remains the primary chart artifact. |

## Consequences

The first implementation can stay small, local, testable, and notebook/script friendly.
The package can later support CLI, batch, APIs, or UI surfaces without moving formula logic into those surfaces.

The first slice depends on the Python packaging and data-analysis ecosystem, so dependency compatibility must be checked in CI once tooling exists.
PNG export behavior must be documented as optional and warning-producing when unavailable.
Automated PPTX generation remains out of scope for first-slice implementation.

## Follow-up

- Define `pyproject.toml`, dependency groups, test/lint/type tooling, and package metadata during packaging setup.
- Confirm dependency support for Python 3.11 through 3.14 in CI.
- Add architecture or ADR updates if automated PPTX generation becomes part of a later accepted slice.
