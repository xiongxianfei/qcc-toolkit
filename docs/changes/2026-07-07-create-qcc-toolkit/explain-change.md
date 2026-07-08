# Change Explanation: Create QCC Toolkit

## Status

draft

## M1 package scaffold

M1 creates the minimal Python package and quality-gate surface required before later QCC method behavior can be implemented.

The scaffold adds `pyproject.toml`, the `qcc_toolkit` import package, a typed package marker, and an import smoke test.
It does not implement Pareto behavior, method registries, evidence packages, charts, templates, scripts, or reports.

The package metadata follows the approved local-first Python stack decision:

- package name: `qcc-toolkit`;
- import name: `qcc_toolkit`;
- supported Python range: 3.11 through 3.14;
- first-slice runtime dependencies: pandas, Plotly, and Pydantic;
- development checks: pytest, Ruff, and mypy.

The import smoke test exists so M1 has executable proof before later milestones add method behavior.

## M2 core contracts and Pareto calculation

M2 adds the first behavior-bearing package surface for stable QCC stage IDs, first-slice method IDs, Pareto validation, Pareto calculation, warning categories, and deterministic interpretation text.

The implementation keeps the scope below rendering and evidence writing. It does not create chart specs, files, scripts, templates, reports, or project folders; those are assigned to later milestones.

The Pareto engine supports category-count input through an explicit count column and event-record input when no count column is supplied. It rejects empty data, missing columns, blank or null categories, nonnumeric counts, negative counts, and zero-total counts before a result can be produced.

The calculation result exposes ranked category rows with count, percentage, cumulative count, cumulative percentage, and rank. Ties are sorted by category after descending count so repeated runs are deterministic.

Deterministic interpretation output produces caption and summary text from the calculation result and emits structured cautions for one-category and many-category cases.

## M3 chart specifications and evidence packages

M3 connects the M2 Pareto calculation result to renderer-independent chart specifications and method-scoped evidence package output.

The chart spec records method ID, QCC stage, selected input columns, source-data context, filters, deterministic run metadata, a count bar series, and a cumulative-percentage line series.
The spec intentionally omits timestamps so the same input data and parameters can reproduce the same chart specification under the same toolkit version.

The evidence writer produces `chart.html`, `chart-spec.json`, `calculated-table.csv`, `caption.md`, `warnings.json`, `metadata.json`, `README.md`, and `report.md`.
PNG export is optional and handled through an injectable exporter so local static-export availability does not block the evidence package.
When PNG export is requested but unavailable, the package records an `export_skipped` warning and still writes the required non-PNG artifacts.

The package metadata identifies the evidence package as the authoritative calculation record and marks slide edits as presentation-only.
It stores source references, filters, selected columns, method/stage IDs, package version, chart-spec version, and calculation version without dumping raw source rows.
