# ADR-20260708-evidence-package-boundary: Evidence Package Boundary

## Status

accepted

Allowed statuses: `draft`, `proposed`, `accepted`, `active`, `deprecated`, `superseded`, `archived`, `abandoned`.

## Context

QCC users learn and present through PowerPoint templates, but data-dependent QCC conclusions need reproducibility and traceability.
The first-slice spec requires generated Pareto evidence to include chart artifacts, calculated table, caption, warnings, metadata, and README or manifest.
It also requires manually edited slides to stay outside the authoritative calculation record.

Without a clear evidence boundary, formulas could drift into scripts, templates, notebooks, or slides.

## Decision

Make the evidence package the authoritative local record for data-dependent QCC conclusions.

For Pareto in the first slice, a method-scoped evidence package contains:

- `chart.html`;
- optional `chart.png`;
- `chart-spec.json`;
- `calculated-table.csv`;
- `caption.md`;
- `warnings.json`;
- `metadata.json`;
- `README.md` or an equivalent manifest.

PowerPoint templates consume slide-ready assets from the evidence package.
Markdown and HTML reports reference evidence package artifacts.
Starter scripts create or regenerate evidence packages through the public package API.

Manually edited PPT slides are presentation artifacts.
They do not replace the evidence package for formulas, source data context, warnings, metadata, or reproducibility.

## Alternatives considered

| Alternative | Reason not chosen |
|---|---|
| Treat final PPT slides as the only record | Makes data-dependent conclusions hard to audit, reproduce, or test. |
| Store only chart images | Loses calculated tables, warnings, metadata, chart specifications, and source context. |
| Store only notebooks | Useful for teaching, but weaker for scriptable batch generation and slide-ready outputs. |
| Store only reports | Reports are useful outputs, but the package needs method-scoped artifacts that can feed reports and slides. |

## Consequences

Evidence generation becomes testable through structured files and reproducibility checks.
Reviewers can inspect metadata, warnings, and calculated outputs without reverse-engineering PowerPoint slides.

The project must maintain stable evidence metadata and chart spec fields as compatibility surfaces.
Output path handling becomes a security boundary because generated evidence is written locally.
Generated metadata must avoid unnecessary raw private row-level data.

## Follow-up

- Define the exact evidence metadata schema in method contracts or architecture follow-up work.
- Add tests that verify generated evidence packages contain required files and structured warning states.
- Revisit the package format before 1.0 if method coverage expands beyond first-slice Pareto.
