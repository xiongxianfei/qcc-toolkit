# QCC Toolkit First-Slice Architecture

## Status

- approved

## Related artifacts

- Proposal: [Create QCC Toolkit](../../proposals/2026-07-07-create-qcc-toolkit.md)
- Spec: [QCC Toolkit First Slice Spec](../../../specs/qcc-toolkit-first-slice.md)
- Spec review: [Spec Review R1](../../changes/2026-07-07-create-qcc-toolkit/reviews/spec-review-r1.md)
- Plan: [Create QCC Toolkit First Slice Plan](../../plans/2026-07-08-create-qcc-toolkit-first-slice.md)
- ADRs:
  - [ADR-20260708-python-local-first-stack](../../adr/ADR-20260708-python-local-first-stack.md)
  - [ADR-20260708-evidence-package-boundary](../../adr/ADR-20260708-evidence-package-boundary.md)

## Introduction and Goals

This package defines the technical architecture for the first usable QCC Toolkit slice.
The first slice must implement a template-backed, Python-powered workflow centered on Pareto Chart evidence generation and lighter template-guided support for Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys.

The architecture must make these boundaries reviewable before implementation:

- PowerPoint templates teach and present.
- Markdown method guides govern method knowledge.
- Python validates data, calculates results, creates chart specifications, generates captions and warnings, and writes evidence packages.
- Evidence packages preserve final data-dependent QCC evidence outside manually edited slides.

The first architecture goal is not to optimize for a future UI.
It is to keep scripts, examples, templates, and reports aligned around a reusable method engine so that the first Pareto vertical slice can be tested and reviewed end to end.

## Architecture Constraints

| Constraint | Architectural response |
|---|---|
| The spec is limited to the first slice. | Design only Pareto as the complete data-chart method and only first-slice template-guided support for Check Sheet, 5W2H, Fishbone, and 5 Whys. |
| The product is local-first. | Scripts and package APIs read local files and write local artifacts without network calls, telemetry, secrets, or services. |
| PowerPoint is first-class but not authoritative for formulas. | PPT templates remain static user-facing assets; evidence metadata and Python results remain the calculation record. |
| Starter scripts must call public APIs only. | Scripts depend on a public facade in `qcc_toolkit` and do not import calculation internals. |
| Calculation logic must not depend on rendering. | Analysis produces structured results and chart specs before Plotly or static export rendering runs. |
| Static PNG export is optional. | HTML chart output and evidence metadata are required; PNG export is best-effort with structured warning when unavailable. |
| Examples must be synthetic. | Example project data and generated evidence use synthetic manufacturing or service-style data only. |
| Public IDs become compatibility surfaces. | Method IDs, template IDs, catalog fields, evidence metadata fields, chart spec fields, and project-folder fields are versioned or treated as pre-1.0 compatibility surfaces. |
| Dependency choices must be documented. | First-slice dependency and adapter choices are recorded in ADR-20260708-python-local-first-stack. |

## Context and Scope

QCC Toolkit runs in a user's local Python environment and interacts with local project files.
Users learn from PPT templates and method guides, run Python scripts against local data, and insert generated chart images, captions, and metadata references into their QCC decks.

The first slice excludes web UI, dashboards, CAPA/EQMS workflows, automated PPTX generation, and Control Chart implementation.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

The system boundary includes:

- the `qcc_toolkit` Python package;
- starter Python scripts;
- Markdown method guides;
- PowerPoint templates;
- `templates/ppt/catalog.yml`;
- the synthetic example project;
- generated local evidence packages and report-ready outputs.

External surfaces are local input files, local browser rendering of generated HTML, and PowerPoint as a user-managed presentation application.

## Solution Strategy

The selected approach is a layered evidence-generation architecture.

```text
Template catalog + method guide + starter script
  -> public method API
    -> input contract validation
      -> calculation result
        -> chart specification
          -> renderer/export adapter
            -> evidence package
              -> Markdown/HTML report and slide-ready assets
```

The tradeoff is deliberate duplication avoidance.
Templates, docs, notebooks, scripts, and reports may describe or present a method, but they must not own Pareto formulas or final chart logic.
The public Python API owns validation, calculation, chart specification, warnings, captions, and evidence writing.

The first slice uses a narrow public facade rather than exposing internal modules as the normal user surface.
Starter scripts call that facade, and examples teach that facade.

The architecture keeps rendering replaceable by making chart specifications structured outputs from method logic.
Plotly is the first renderer, and static image export is optional so missing local export dependencies do not prevent HTML evidence generation.

## Building Block View

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

### Repository-level building blocks

| Area | Responsibility | First-slice contract |
|---|---|---|
| `qcc_toolkit` | Python package and public API. | Owns method registry, validation, Pareto calculation, chart spec, warnings, captions, metadata, evidence writing, and catalog checks. |
| `docs/methods` | Markdown method guides. | One guide per first-slice method with stable front matter and required sections. |
| `templates/ppt` | PPT method templates and catalog. | Static templates, demo labels, placeholders, and catalog traceability. |
| `examples/projects/reduce-packing-label-errors` | Synthetic end-to-end QCC story. | Source data, script invocation, generated evidence package, and report-ready output. |
| `examples/scripts` | Starter scripts. | Thin local CLI wrappers around the public API. |
| `tests` | Automated proof once implementation exists. | Formula, validation, catalog, script smoke, reproducibility, and report/evidence checks. |

### Python package building blocks

| Package area | Responsibility | Dependency direction |
|---|---|---|
| `qcc_toolkit.project` | Project context, evidence IDs, project metadata, and project-folder references. | Does not depend on renderers. |
| `qcc_toolkit.stages` | Canonical QCC Story stage IDs and display labels. | Shared by methods, guides, templates, and evidence metadata. |
| `qcc_toolkit.methods` | Public method registry and first-slice Pareto facade. | Calls contracts and analysis; exposes stable method IDs. |
| `qcc_toolkit.contracts` | Input, parameter, warning, chart spec, evidence metadata, and catalog models. | Shared structured models; no rendering dependency. |
| `qcc_toolkit.analysis` | Pareto calculation and deterministic summary inputs. | Receives validated data; returns calculation result. |
| `qcc_toolkit.charts` | Chart spec construction and renderer adapters. | Consumes calculation result and metadata; rendering depends on spec, not the reverse. |
| `qcc_toolkit.interpretation` | Deterministic captions, warnings, and transparent interpretation text. | Consumes calculation result and method metadata. |
| `qcc_toolkit.evidence` | Evidence package writer, manifests, metadata, generated asset records, and reproducibility data. | Writes local outputs; records renderer/export outcomes. |
| `qcc_toolkit.reports` | Markdown and optional HTML report-ready output. | Consumes evidence package records. |
| `qcc_toolkit.io` | CSV and Excel-like input loading with safe parsing boundaries. | Normalizes local input into tabular data for contracts. |
| `qcc_toolkit.templates` | Template catalog loading and validation. | Checks catalog paths, IDs, placeholders, expected assets, and method/guide linkage. |

### Public first-slice API shape

The first implementation should expose a small public API that starter scripts can call without reaching into internals.
Exact names can be refined during implementation, but the public surface must provide these operations:

| Public operation | Required behavior |
|---|---|
| Build Pareto evidence | Accept local tabular input or loaded data, category column, optional count column, project context, output path, and optional data context; return an evidence package result. |
| Validate Pareto input | Validate required columns, empty data, negative counts, nonnumeric counts, blank category behavior, and zero-total behavior. |
| Calculate Pareto result | Return category count, percentage, cumulative value, and rank fields with deterministic sort and tie behavior. |
| Build Pareto chart spec | Return a renderer-independent chart specification with method metadata and data context. |
| Render/export chart artifacts | Produce HTML and optional PNG; record skipped optional export as a warning. |
| Validate template catalog | Load `templates/ppt/catalog.yml` and verify IDs, paths, guide links, generator links, example project links, placeholders, and expected assets. |
| Write evidence package | Write calculated table, chart spec, chart artifacts, caption, warnings, metadata, and README or manifest. |

Internal modules may be reorganized later, but starter scripts and examples must use public operations only.

### Evidence package shape

The first-slice Pareto evidence package is method-scoped and local.

```text
evidence/
  pareto/
    chart.html
    chart.png              # optional when static export is available
    chart-spec.json
    calculated-table.csv
    caption.md
    warnings.json
    metadata.json
    README.md
```

The exact folder root can be set by the starter script output path.
The file names above are the default architecture contract unless a later spec or ADR supersedes them.

### Template catalog shape

`templates/ppt/catalog.yml` is the traceability map between templates, method IDs, guides, scripts, examples, placeholders, and expected assets.

The first implementation should preserve the spec-required fields and may add schema metadata such as `schema_version`.
Catalog validation belongs in Python so CI, scripts, and maintainers can detect drift.

## Runtime View

### Pareto evidence generation

1. User opens the Pareto method guide or PPT template to understand the method and input requirements.
2. User runs the Pareto starter script with local input data, category column, optional count column, project path, and output path.
3. The script calls the public Pareto evidence API.
4. IO loads local tabular input using safe parsing rules.
5. Contracts validate required columns, empty data, count values, category values, and method parameters.
6. Analysis calculates Pareto counts, percentages, cumulative values, ranks, and deterministic order.
7. Chart code builds a renderer-independent chart specification.
8. Interpretation builds deterministic caption text and warnings.
9. Renderer/export adapter writes `chart.html` and attempts `chart.png` when local static export support is available.
10. Evidence writer writes table, chart spec, caption, warnings, metadata, README or manifest, and generated artifact records.
11. Script exits `0` and prints or writes the evidence package path.

### Validation failure

1. User runs the starter script with invalid input.
2. IO or contracts detect the error before final chart artifacts are produced.
3. Script exits non-zero and reports the validation problem.
4. The output path must not contain success metadata for that run.

### Optional export failure

1. Pareto validation and calculation succeed.
2. HTML chart rendering succeeds.
3. PNG export fails or static export dependency is unavailable.
4. Evidence writer records a structured warning and still writes the non-PNG evidence artifacts.
5. Script exits `0` unless another fatal error occurred.

### Template catalog validation

1. Validation loads `templates/ppt/catalog.yml`.
2. Validation checks unique template IDs, method IDs, paths, expected placeholders, expected assets, and first-slice coverage.
3. Validation fails with a catalog entry and field name when any referenced path or ID contract is invalid.

## Deployment View

The first slice is distributed as a local Python package plus repository assets.

| Deployable or artifact | Deployment concern |
|---|---|
| Python package | Packaged through `pyproject.toml`; supports Python 3.11 through 3.14 for the first slice. |
| Starter scripts | Checked into examples and executable from a local checkout or installed package environment. |
| Method guides | Versioned Markdown under `docs/methods`. |
| PPT templates | Versioned static `.pptx` assets under `templates/ppt`. |
| Template catalog | Versioned YAML file under `templates/ppt/catalog.yml`. |
| Example project | Versioned synthetic example data and generated or regenerable outputs under examples. |
| Evidence packages | User-generated local outputs; not transmitted or centrally stored by the toolkit. |

No server, hosted service, database, queue, telemetry endpoint, cloud storage, or web UI is part of the first slice.

Automated PPTX generation is deferred.
The first slice exports slide-ready evidence assets that users insert into PowerPoint manually.

## Crosscutting Concepts

### Source of truth

PowerPoint templates own teaching layout and presentation pattern.
Markdown guides own method knowledge and review guidance.
Python owns validation, formulas, chart specs, deterministic captions, warnings, metadata, and generated evidence.
Evidence packages own the final calculation record for data-dependent conclusions.

### Validation

Validation is layered:

- IO validates file existence and safe parsing assumptions.
- Contracts validate input shape, required columns, counts, category values, parameters, and output path constraints.
- Method validation produces method-specific errors and warnings.
- Catalog validation checks template, guide, script, example, placeholder, and asset traceability.

Validation errors block final evidence generation.
Warnings are structured and can appear in evidence packages and reports.

### Reproducibility

Evidence metadata must record method ID, evidence or chart ID, input data reference, selected columns, parameters, filters when supported, generated artifacts, warnings, toolkit version, and generation timestamp or equivalent run metadata.

Calculation results and chart specs must be deterministic for the same input data, parameters, filters, and toolkit version.

### Rendering boundary

Chart specs are structured data produced before rendering.
Plotly is the first renderer.
HTML is the required interactive output.
PNG is optional and depends on local static export support.
Renderer failures for optional outputs become warnings rather than formula or validation failures.

### Security and privacy

The first slice is local-first.
It performs no network transmission, needs no credentials, and includes only synthetic example data.
Metadata avoids embedding raw private row-level data beyond what is necessary for the example and reproducibility contract.
Output writing must stay inside the selected output path.

### Observability

Scripts communicate status through exit codes, user-visible messages, output paths, structured warnings, and metadata.
Generated reports surface warning state when warnings exist.

## Architecture Decisions

- [ADR-20260708-python-local-first-stack](../../adr/ADR-20260708-python-local-first-stack.md) - choose the local-first Python package, first-slice dependency stack, and deferred PPTX automation.
- [ADR-20260708-evidence-package-boundary](../../adr/ADR-20260708-evidence-package-boundary.md) - make the evidence package the authoritative record for data-dependent QCC conclusions.

## Quality Requirements

| Quality | Scenario | Measure |
|---|---|---|
| Reproducibility | A user regenerates Pareto evidence with the same input data, parameters, filters, chart spec inputs, and toolkit version. | Calculated table and chart specification are equivalent to the previous run. |
| Reviewability | A reviewer opens the template catalog and Pareto evidence package. | The reviewer can trace template ID, method ID, guide, generator script, source data reference, generated artifacts, warnings, and metadata. |
| Validation safety | A user provides missing columns, empty data, negative counts, or duplicate template IDs. | The system fails before final evidence generation and identifies the failing input or catalog field. |
| Local privacy | A user runs the first-slice scripts on local data. | No network call, telemetry call, secret, or external service is required. |
| Optional export resilience | PNG export is unavailable. | HTML, table, caption, warnings, metadata, and README or manifest are still produced with a structured warning. |
| Performance | A user regenerates the synthetic Pareto example on a typical developer laptop. | The run completes within the spec target of 10 seconds excluding installation and unusually slow static export. |

## Risks and Technical Debt

| Risk or debt | Impact | Mitigation |
|---|---|---|
| Public API names may be overfit to the first script. | Later methods could inherit awkward patterns. | Keep first-slice API small and method-oriented; review during method contracts and architecture review. |
| Optional PNG export depends on local renderer support. | Users may expect a PNG every time. | Make HTML primary and record skipped PNG as a warning. |
| PPT template visual quality is partly manual. | Automated checks can prove file validity, placeholders, demo labels, and traceability, but not presentation polish. | Keep reviewable Markdown source notes, deterministic PPTX generation, catalog validation, and human PR review for visual quality. |
| Evidence metadata can expose sensitive source paths. | Users may share reports or metadata externally. | Store input references intentionally and avoid raw private row-level data in metadata. |
| Project folder schema is pre-1.0. | Early examples may need migration. | Include toolkit version and keep breaking changes documented before 1.0. |

## Glossary

| Term | Meaning |
|---|---|
| Chart specification | Renderer-independent structured description of the chart, method metadata, visual marks, and data context. |
| Evidence package | Local method-scoped output folder containing generated chart artifacts, table, caption, warnings, metadata, and README or manifest. |
| Public facade | Supported import and call surface used by scripts and examples. |
| Renderer adapter | Code that turns chart specifications into HTML, PNG, or future render targets. |
| Template catalog | YAML inventory that links PowerPoint templates to method IDs, guides, scripts, examples, placeholders, and expected assets. |

## Next artifacts

- Plan review for [Create QCC Toolkit First Slice Plan](../../plans/2026-07-08-create-qcc-toolkit-first-slice.md).
- Method contracts specification for Pareto validation, calculation convention, warnings, captions, and output fields.
- PPT template specification for catalog schema, placeholder rules, demo labels, and static template checks.
- Starter scripts specification for CLI arguments, output paths, exit codes, and smoke tests.
- Test specification after architecture review.

## Follow-on artifacts

- [Create QCC Toolkit First Slice Plan](../../plans/2026-07-08-create-qcc-toolkit-first-slice.md)

## Readiness

Architecture-review approved this package with no material findings.
Execution plan has been authored and is ready for plan-review.
