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

### M3 review-resolution: CR-M3-001

Code review found that generated `chart.html` used Plotly CDN mode.
The renderer now uses Plotly's self-contained HTML mode so the evidence package does not depend on an external Plotly script.

The chart-rendering test now rejects external Plotly CDN script output and any `https://cdn.plot.ly` URL in generated HTML.
The renderer removes Plotly CDN URL strings from the self-contained HTML bundle after Plotly generates the local artifact.

## M4 method guides and template catalog

M4 adds the first-slice method guidance and template traceability surface.

The method guides under `docs/methods/` cover Pareto Chart, Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys.
Their front matter uses the same stable method IDs, stage IDs, method types, generated-chart flags, and first-slice status as the Python method registry.
Each guide includes the required sections for summary, stage fit, use guidance, inputs, outputs, procedure, interpretation, common mistakes, examples, related methods, formula or logic notes, and review checklist.

The Pareto guide documents both supported input shapes: event-record data and category-count data.
It also records the implemented calculation convention: category frequency, percentage, cumulative count, cumulative percentage, and deterministic sort order.

M4 adds `templates/ppt/catalog.yml` as the reviewable catalog for first-slice template assets.
The catalog maps each template to a stable `template_id`, `method_id`, stage list, guide path, placeholder list, and expected assets.
The Pareto entry also identifies the planned M5 starter script and example project paths.

The template assets under `templates/ppt/methods/` are Markdown placeholder sources for future PPT files.
They are intentionally reviewable text assets with stable IDs, explicit `DEMO EXAMPLE - not project evidence` labels, and documented placeholders.
This keeps binary PPT content from becoming the only review surface.

The placeholder `examples/scripts/generate_pareto.py` and example-project README exist only so M4 catalog validation can reference stable future paths.
The functional starter script, synthetic data, and regenerated example evidence remain assigned to M5.

The `qcc_toolkit.templates` module validates catalog shape, duplicate template IDs, duplicate method ownership, and referenced paths.
It also provides the milestone CLI:

```sh
python -m qcc_toolkit.templates validate templates/ppt/catalog.yml
```

### M4 review-resolution: CR-M4-001

Code review found that catalog validation accepted a template entry whose `method_id` did not match the referenced Markdown guide front matter.

The catalog validator now parses the referenced Markdown guide front matter during validation and compares guide `method_id` with the catalog entry `method_id`.
If they differ, it raises `CatalogValidationError` with the template ID and guide path.

The catalog failure tests now include a mismatched-guide regression fixture that points a Pareto catalog entry at the Check Sheet guide and expects validation to fail.
