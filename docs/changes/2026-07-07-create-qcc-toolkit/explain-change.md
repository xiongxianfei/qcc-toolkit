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

## M5 starter script and synthetic example project

M5 turns the M4 placeholder script and project path into a working local example.

The Pareto starter script at `examples/scripts/generate_pareto.py` now accepts explicit local inputs for CSV path, category column, optional count column, project folder, and output folder.
It performs only input parsing and CSV conversion itself, then delegates Pareto validation, calculation, chart specification, captions, warnings, metadata, and evidence writing to the public `qcc_toolkit` API.
This preserves the rule that starter scripts are execution surfaces, not formula owners.

The script returns `0` and prints the output evidence path on success.
For missing files, missing columns, validation errors, or invalid output paths, it prints a user-visible error to stderr, returns non-zero, and does not write success metadata.
The output folder must be inside the selected project folder so a path mistake cannot silently write generated evidence outside the project boundary.

The example project at `examples/projects/reduce-packing-label-errors` now includes a synthetic defect dataset and README command that regenerates Pareto evidence from local data.
The data is explicitly synthetic and contains no real customer, employee, supplier, production, or private operational data.

M5 does not commit regenerated Pareto evidence artifacts.
The self-contained Plotly `chart.html` generated by the documented command is large, so the example `evidence/` folder records the output convention and ignores regenerated artifacts.
The documented script command and automated tests prove the evidence package can be regenerated when needed.

## M6 report-ready workflow integration

M6 connects the generated evidence package to project-level report-ready outputs.

The new `build_qcc_project_report()` API reads a generated evidence package and writes `report.md` plus a simple local `report.html`.
The reports link to the generated chart, calculated table, caption, warnings, metadata, chart spec, and evidence README.
They also make warning state visible and repeat that the evidence package remains the authoritative calculation record while slides are presentation artifacts.

The Pareto starter script now calls the report builder after evidence generation.
A single local command therefore regenerates both method evidence under `evidence/pareto` and project report output under `report/`.

M6 intentionally keeps report generation small.
It does not add a Markdown renderer dependency, web UI, dashboard, document editor, automated PPTX generation, Control Chart support, or AI-generated conclusions.
The HTML report is a simple local artifact produced from the Markdown content so the first slice remains local-first and dependency-light.

The example project keeps generated report files ignored, matching the generated evidence policy from M5.
The documented command and tests prove those report artifacts can be regenerated.

## M7 lifecycle closeout preparation

M7 prepares the completed first-slice implementation for code review of the lifecycle closeout milestone.

It adds `tests/test_acceptance.py` as the explicit T23 acceptance proof surface.
That test checks that lifecycle metadata is in the M7 review-requested state, M1-M6 code-review records are present, the catalog covers the implemented first-slice methods, the Pareto generator and synthetic example project exist, and template-guided methods remain cataloged with template assets and demo labels.

M7 changes only lifecycle and proof artifacts.
It does not change product behavior, public APIs, method calculations, chart generation, report output semantics, templates, or example data.

The plan remains active because M7 still needs code-review.
Final explain-change, verify, and PR handoff remain downstream stages and are not claimed by this milestone.
