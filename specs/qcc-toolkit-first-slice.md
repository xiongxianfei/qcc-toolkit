# QCC Toolkit First Slice Spec

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-07-create-qcc-toolkit.md`
- Proposal status: superseded by `docs/proposals/2026-07-09-markdown-first-method-guides.md` after this spec was implemented
- Proposal review: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/proposal-review-r1.md`

This spec defines the first usable slice for QCC Toolkit.
It turned the then-accepted proposal direction into observable behavior for a template-backed, Python-powered QCC evidence workflow.

## Goal and context

The first slice MUST let a user apply a small QCC method set through PowerPoint templates, Markdown method guides, Python-generated evidence, and a reproducible example project.

The first complete vertical method is Pareto Chart.
The first slice also includes lighter template-guided support for Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys.

The system MUST preserve the product rule that PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates traceable evidence.

## Glossary

| Term | Meaning |
|---|---|
| Method ID | Stable machine-readable identifier for a QCC method, such as `pareto_chart`. |
| Template ID | Stable machine-readable identifier for a PowerPoint method template. |
| Method guide | Markdown document that explains a QCC method, its use, inputs, outputs, interpretation, cautions, and review checklist. |
| Data-chart method | QCC method whose final project evidence depends on data validation, calculation, chart generation, warnings, and metadata. |
| Template-guided method | QCC method whose first-slice support is primarily a PPT template, Markdown guide, and optional structured notes. |
| Evidence package | Method-scoped folder of generated chart assets, calculated tables, captions, warnings, metadata, and a README or manifest. |
| Demo chart | Example chart embedded in a template or guide to teach a method; it is not project evidence. |
| First vertical method | The first method implemented end-to-end across guide, template, data, script, generated evidence, and report-ready output. |

## Examples first

Example E1: Generate Pareto evidence from synthetic project data
Given a synthetic project named `reduce-packing-label-errors`
And a local defect dataset with a category column and a count column
When the user runs the Pareto starter script with the dataset, required columns, project path, and output path
Then the system generates a method-scoped Pareto evidence package containing an interactive chart, static chart image when export support is available, calculated table, caption, warnings, metadata, and README or manifest.

Example E2: Reject invalid Pareto input before producing evidence
Given a Pareto input dataset missing the configured category column
When the user runs the Pareto starter script
Then the system exits with a non-zero status
And the system explains the missing required input
And the system MUST NOT write a final chart, final caption, or success metadata for that run.

Example E3: Trace a method template to its guide and generator
Given `templates/ppt/catalog.yml`
When a reviewer checks the Pareto template entry
Then the entry identifies the template ID, method ID, QCC stages, PPT file, Markdown guide, example project, supported generated assets, and the Pareto generator script.

Example E4: Use template-guided methods without inventing formulas
Given the first-slice 5W2H, Check Sheet, Fishbone, and 5 Whys assets
When a user opens their method templates or Markdown guides
Then the assets teach method usage and presentation structure
And they MUST NOT claim to perform final data-dependent calculations unless backed by a Python-generated evidence artifact.

Example E5: Reproduce a Pareto chart
Given the same source dataset, method ID, parameters, filters, chart specification, and toolkit version
When the user regenerates the Pareto evidence package
Then the calculated table and chart specification are equivalent to the previous run under the same package version.

## Requirements

| ID | Requirement |
|---|---|
| R1 | The system MUST provide a first-slice synthetic QCC project with the project ID `reduce-packing-label-errors` or an explicitly equivalent stable project ID. |
| R2 | The first-slice project MUST include synthetic data only and MUST NOT include real customer, production, employee, supplier, patient, or private operational data. |
| R3 | The system MUST support Pareto Chart as the first complete vertical data-chart method. |
| R4 | The first slice MUST include template-guided support for Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys. |
| R5 | Every first-slice method MUST have a stable `method_id`. |
| R6 | Every first-slice PowerPoint method template MUST have a stable `template_id`. |
| R7 | Every first-slice method guide MUST identify its `method_id`, method name, supported QCC stage or stages, method type, generated-chart support, first-slice status, and last-reviewed date. |
| R8 | Every first-slice method guide MUST include sections for summary, QCC stage fit, when to use, when not to use, inputs required, outputs produced, procedure, interpretation guidance, common mistakes, example, related methods, formula or logic notes when applicable, and review checklist. |
| R9 | The Pareto method guide MUST describe required input shapes for both event-record data and category-count data when both are supported; if only one input shape is supported in the first slice, the guide MUST state that limit. |
| R10 | The Pareto method guide MUST document the implemented Pareto calculation convention, including category frequency, percentage, cumulative count or cumulative percentage, and sort order. |
| R11 | The system MUST provide first-slice PowerPoint templates for Pareto Chart, Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys. |
| R12 | PowerPoint templates MUST clearly label demo examples and demo charts as not project evidence. |
| R13 | PowerPoint templates MUST reserve stable, documented placeholders for generated evidence where generated evidence is expected. |
| R14 | The template catalog MUST exist at `templates/ppt/catalog.yml`. |
| R15 | The template catalog MUST contain one entry per first-slice PowerPoint template. |
| R16 | Each template catalog entry MUST include `template_id`, `method_id`, `template_type`, `qcc_stages`, `file`, `markdown_guide`, `supports_generated_chart`, `expected_placeholders`, and `expected_assets`. |
| R17 | The Pareto catalog entry MUST also identify the Pareto generator script and example project. |
| R18 | Template catalog validation MUST fail when a referenced template file, Markdown guide, generator script, or example project path is missing. |
| R19 | Template catalog validation MUST fail when duplicate `template_id` values exist. |
| R20 | Template catalog validation MUST fail when duplicate first-slice method entries create ambiguous template ownership unless the duplicate is explicitly classified as an alternate template. |
| R21 | The Pareto starter script MUST accept local input data, category column, optional count column, project path, and output path as explicit user-provided inputs. |
| R22 | The Pareto starter script MUST be executable locally without a web server, cloud service, telemetry service, or external network call. |
| R23 | The Pareto starter script MUST call the public package API for validation, calculation, chart specification, caption generation, warnings, metadata, and evidence writing. |
| R24 | Starter scripts MUST NOT duplicate Pareto formulas or chart calculation logic outside the public package API. |
| R25 | The Pareto evidence generator MUST validate required columns before producing final chart artifacts. |
| R26 | The Pareto evidence generator MUST reject empty input datasets. |
| R27 | The Pareto evidence generator MUST reject negative counts when category-count input is used. |
| R28 | The Pareto evidence generator MUST provide a clear error or warning for missing, blank, or null category values according to the method contract. |
| R29 | The Pareto calculation result MUST include category, count, percentage, cumulative count or cumulative percentage, and rank fields. |
| R30 | The Pareto chart specification MUST include bars for category counts and a cumulative percentage line when cumulative percentage is supported by the selected calculation convention. |
| R31 | The Pareto chart specification MUST preserve method ID, QCC stage, input data context, selected columns, filters when provided, parameters, generated timestamp or equivalent run metadata, and toolkit version. |
| R32 | The Pareto evidence package MUST include a calculated table, chart specification, caption, warnings artifact, metadata artifact, and README or manifest. |
| R33 | The Pareto evidence package SHOULD include an interactive HTML chart as the primary chart artifact. |
| R34 | The Pareto evidence package SHOULD include a PNG chart when the configured chart renderer and local static export dependency are available. |
| R35 | If static PNG export is unavailable, the system MUST still produce the remaining evidence artifacts and MUST record a warning explaining that PNG export was skipped. |
| R36 | Generated Pareto captions MUST be deterministic from the calculation result, method metadata, and configured data context. |
| R37 | Generated Pareto interpretation MUST remain deterministic and transparent; it MUST NOT use opaque AI-generated conclusions in the core first slice. |
| R38 | Generated warnings MUST distinguish validation errors, non-blocking data cautions, skipped optional exports, and interpretation cautions. |
| R39 | The example project MUST include a report-ready Markdown output that references the generated Pareto evidence package. |
| R40 | The example project SHOULD include an HTML report output when the local report renderer is available. |
| R41 | Report-ready outputs MUST preserve links or references to generated chart artifacts, calculated tables, captions, warnings, and metadata. |
| R42 | Final data-dependent chart artifacts MUST be reproducible from source data, method ID, parameters, filters, chart specification, output path, and toolkit version. |
| R43 | The system MUST provide documentation or a manifest that tells users which generated assets should be inserted into the PowerPoint template. |
| R44 | The system MUST keep manually edited slides out of the authoritative calculation record for data-dependent conclusions. |
| R45 | The first slice MUST NOT include a web UI, real-time dashboard, CAPA/EQMS workflow, approval workflow, or document editor. |
| R46 | The first slice MUST NOT require automated PPTX generation. Static PPT templates and slide-ready generated assets are sufficient. |
| R47 | Control Chart support MUST remain outside the required first vertical proof slice unless a later accepted spec explicitly adds it. |
| R48 | The system MUST provide automated checks or documented commands that verify method IDs, template IDs, catalog paths, guide paths, script paths, and example project paths for the first slice. |
| R49 | The system MUST provide automated checks or documented commands that regenerate the Pareto evidence package from synthetic data. |
| R50 | The system MUST provide automated checks or documented commands that verify the same input data and parameters produce the same Pareto calculation result and chart specification under the same toolkit version. |

## Inputs and outputs

| Surface | Required inputs | Required outputs |
|---|---|---|
| Pareto starter script | Input data path, category column, optional count column, project path, output path, optional filters or data context when supported. | Method-scoped evidence package with calculated table, chart specification, chart artifact, caption, warnings, metadata, and README or manifest. |
| Pareto method guide | Method ID, QCC stages, method type, input contract, output contract, procedure, formula notes, cautions, example links. | Markdown guide that reviewers can inspect and docs checks can validate. |
| PowerPoint template catalog | Template entries with stable IDs and paths. | Catalog that maps method templates to guides, scripts, examples, placeholders, and expected assets. |
| Static PPT templates | Teaching content, demo examples, placeholders, method IDs, template IDs. | User-facing templates for method learning and project presentation. |
| Example project | Synthetic data, script invocation, method guide links, template links. | Reproducible project evidence and report-ready outputs. |

The first-slice default generated evidence package SHOULD use method-scoped folders so repeated method outputs do not overwrite unrelated evidence.

## State and invariants

I1. Method IDs are stable compatibility surfaces once documented.

I2. Template IDs are stable compatibility surfaces once documented.

I3. PowerPoint templates are authoritative for teaching layout and presentation pattern, not formulas or final data-dependent calculations.

I4. Markdown method guides are authoritative for method guidance and review checklist text.

I5. Python method contracts and generated evidence artifacts are authoritative for validation, formulas, chart specifications, captions, warnings, and metadata.

I6. Starter scripts are execution surfaces around the public API and MUST NOT become a second implementation of formulas.

I7. Evidence packages remain valid even when users manually edit copied slide content later, because the package stores the calculation record separately.

I8. Demo charts and final generated charts MUST be distinguishable by labels, metadata, or artifact location.

## Error and boundary behavior

EB1. Missing required input files MUST produce a clear failure and MUST NOT produce success metadata.

EB2. Missing required columns MUST produce a clear validation failure that names the missing column or columns.

EB3. Empty datasets MUST fail before final chart generation.

EB4. Negative counts in category-count Pareto input MUST fail validation.

EB5. Non-numeric count values in category-count Pareto input MUST fail validation unless the parser can safely coerce them according to documented rules.

EB6. Blank category values MUST be handled by a documented rule: reject, warn and group, or warn and drop.

EB7. Optional static chart export failure MUST NOT fail the entire evidence generation when the interactive chart, table, caption, warnings, and metadata can still be produced.

EB8. A partially failed run MUST leave no ambiguous success state; warnings and metadata MUST show which outputs were produced and which were skipped.

EB9. Catalog validation errors MUST identify the catalog entry and field that failed.

EB10. Duplicate template IDs MUST fail catalog validation.

## Compatibility and migration

The first slice is pre-1.0.
Public APIs, method IDs, template IDs, project-folder fields, template catalog fields, chart specification fields, and evidence metadata fields SHOULD be treated as compatibility surfaces even before 1.0.

Breaking changes before 1.0 MUST be documented in the relevant spec, method guide, or changelog once those artifacts exist.

Generated evidence metadata MUST include enough toolkit version information to distinguish old outputs from new outputs when formulas, chart rules, or metadata fields change.

No migration from existing package data is required because no implementation exists yet.

## Observability

O1. Starter scripts MUST return exit code `0` on successful evidence generation and non-zero on validation or fatal runtime failures.

O2. Starter scripts MUST print or write the output evidence path on success.

O3. Starter scripts MUST print or write validation errors in a user-visible form on failure.

O4. Evidence metadata MUST record method ID, chart ID or evidence ID, input data reference, selected columns, parameters, filters when supported, generated artifacts, warnings, toolkit version, and generation timestamp or equivalent run metadata.

O5. Warnings MUST be written to a structured artifact so scripts, reports, and future UIs can consume them.

O6. Report-ready outputs MUST make warning state visible when warnings exist.

## Security and privacy

S1. First-slice examples MUST use synthetic data only.

S2. Generated metadata MUST avoid embedding raw private row-level data beyond what is necessary to reproduce or explain the example output.

S3. The first slice MUST run locally by default and MUST NOT transmit project data over a network.

S4. Scripts MUST NOT require secrets, credentials, API keys, or telemetry tokens.

S5. Spreadsheet or CSV parsing behavior MUST avoid executing formulas or external references from imported files.

S6. Output path handling MUST avoid writing outside the user-selected project or output path through path traversal.

## Accessibility and UX

UX1. Markdown method guides MUST be readable as plain Markdown without requiring a custom documentation site.

UX2. Generated chart captions MUST be usable as text outside the chart image.

UX3. Static PPT templates SHOULD use text placeholders and labels that remain meaningful when charts are not visible.

UX4. Generated charts SHOULD include descriptive titles, axis labels, legend labels when applicable, and captions sufficient for review.

UX5. Demo charts in templates MUST be visibly labeled as demo examples so users do not mistake them for project evidence.

## Performance expectations

P1. The Pareto starter script SHOULD regenerate the synthetic first-slice evidence package in no more than 10 seconds on a typical developer laptop, excluding optional dependency installation time and unusually slow static image export.

P2. The Pareto calculation SHOULD support at least 10,000 input rows in the first slice without requiring manual pre-aggregation by the user.

P3. Performance failures MUST NOT silently produce incomplete evidence; the run must either complete or report a clear failure.

## Edge cases

EC1. Input data has ties in category counts; the calculation MUST use a documented deterministic tie-break rule.

EC2. Input data has only one category; the chart and caption MUST avoid implying a meaningful vital-few comparison.

EC3. Input data has many categories; the method guide or warning behavior MUST document whether categories are shown individually, grouped, truncated, or left to user configuration.

EC4. Input data has zero total count; the system MUST fail validation or produce a documented no-data warning without dividing by zero.

EC5. Input data contains extra columns; the system MUST ignore or preserve them according to the documented input contract without changing the Pareto calculation unexpectedly.

EC6. Output folder already exists; the system MUST either overwrite only method-owned generated files, write a new run folder, or fail with a clear message.

EC7. Static image export dependency is missing; the system MUST produce non-PNG evidence artifacts and record a warning.

EC8. Template catalog references a guide that exists but has a mismatched `method_id`; validation MUST fail.

EC9. A method guide exists without a matching first-slice template; validation MUST identify whether that is intentional or a coverage gap.

EC10. A user edits a PPT slide after inserting generated assets; the evidence package MUST remain the authoritative calculation record.

## Non-goals

NG1. The first slice does not build a web UI, dashboard, desktop application, CAPA system, EQMS, approval workflow, or document editor.

NG2. The first slice does not fully automate PowerPoint deck generation.

NG3. The first slice does not implement every core QCC method.

NG4. The first slice does not require Control Chart implementation.

NG5. The first slice does not support advanced methods such as DOE, QFD, Kano, advanced regression, or complex network planning.

NG6. The first slice does not use AI-generated conclusions in the core method engine.

NG7. The first slice does not make Plotly, pandas, Pydantic, or any other dependency choice final without architecture and packaging documentation.

NG8. The first slice does not define enterprise governance, release policy, or contributor policy beyond what the existing repository governance already records.

## Acceptance criteria

| ID | Criterion |
|---|---|
| AC1 | One synthetic QCC project regenerates a Pareto chart evidence package from local data. |
| AC2 | The generated Pareto evidence package includes a chart artifact, calculated table, caption, warnings, metadata, and README or manifest. |
| AC3 | The Pareto method guide explains when to use it, when not to use it, required inputs, procedure, interpretation, formula or logic notes, and common mistakes. |
| AC4 | The Pareto PPT template exists and is listed in `templates/ppt/catalog.yml`. |
| AC5 | The Pareto starter script calls the public API for validation, calculation, chart specification, captions, warnings, metadata, and evidence writing. |
| AC6 | The same Pareto input data and parameters produce the same calculation result and chart specification under the same toolkit version. |
| AC7 | Script smoke tests or documented local commands regenerate expected Pareto artifacts from synthetic data. |
| AC8 | Documentation and catalog checks confirm method IDs, template IDs, guide paths, script paths, example paths, and template catalog paths are consistent. |
| AC9 | No real customer data is included in examples, templates, generated evidence, reports, or tests. |
| AC10 | The first slice does not add web UI, dashboard, CAPA/EQMS, automated PPTX generation, or advanced method scope. |
| AC11 | Template-guided methods Check Sheet, 5W2H, Fishbone Diagram, and 5 Whys have method guides, PPT templates, catalog entries, and clear first-slice status. |
| AC12 | Demo charts and demo examples in PPT templates are labeled as demo and not project evidence. |

## Open questions

None blocking this spec.

The first architecture pass now records public API shape, package layout, first-slice dependency decisions, chart renderer boundaries, evidence package format, and template catalog boundaries.
Method contracts and template/script specifications still need to refine exact validation rules, CLI names, placeholder mechanics, and test fixtures.

## Next artifacts

| Artifact | Purpose |
|---|---|
| Spec review | Review this behavioral contract before architecture or planning relies on it. |
| Architecture design | Define package boundaries, public API shape, method contracts, chart specification structure, evidence package structure, project-folder format, and dependency choices. |
| Method contracts specification | Define exact Pareto validation rules, calculation convention, output fields, warnings, and deterministic caption rules. |
| PPT template specification | Define template catalog schema, placeholder names, static template rules, and demo-labeling requirements. |
| Starter scripts specification | Define CLI names, arguments, output folders, exit codes, and smoke-test expectations. |
| Test specification | Map these requirements and acceptance criteria to automated checks and fixtures. |

## Follow-on artifacts

| Artifact | Purpose |
|---|---|
| `docs/architecture/system/architecture.md` | Draft canonical architecture package for this spec. |
| `docs/adr/ADR-20260708-python-local-first-stack.md` | Accepted first-slice local Python package and dependency decision. |
| `docs/adr/ADR-20260708-evidence-package-boundary.md` | Accepted evidence package boundary decision. |

## Readiness

Spec-review approved this spec with no material findings.
Architecture has been authored and is ready for architecture-review.
