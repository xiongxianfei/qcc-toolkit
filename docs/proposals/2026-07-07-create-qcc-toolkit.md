# Proposal: Create QCC Toolkit

## Status

superseded

This revised proposal records an earlier project direction for creating QCC Toolkit.
It is superseded by `docs/proposals/2026-07-09-markdown-first-method-guides.md`, but it remains a historical record for the implemented first-slice work.
It is not a specification, an implementation plan, or verification evidence.

This revision incorporates the product direction that QCC Toolkit should be a template-backed, Python-powered evidence system for QCC methods.
PowerPoint QCC method templates are first-class user-facing assets because users already learn methods from them, copy examples from them, and build QCC materials from them.
Python supports those templates by making data-dependent charts, tables, captions, warnings, and metadata reliable, reproducible, and traceable.

## Problem

Quality Control Circle project work is often split across disconnected spreadsheets, scripts, charting tools, method notes, and presentation files.
That fragmentation makes QCC evidence harder to repeat, review, teach, audit, and explain.

The project needs a coherent product direction before implementation begins.
The direction should define how QCC stages, PowerPoint method templates, Markdown method guides, data validation, statistical calculations, chart generation, interpretations, scripts, evidence packages, and report-ready outputs fit together.
It should do this without turning the project into a generic charting library, a statistical IDE, a dashboard platform, a document editor, or an enterprise quality-management system.

A second practical problem is adoption.
Many QCC users already start from PowerPoint method templates before they understand the full Python package design.
They need those templates to remain useful for teaching and presentation, while Python protects the quality of data-dependent evidence and Markdown preserves method knowledge in a reviewable form.

## Goals

| ID | Goal |
|---|---|
| G1 | Create a template-backed, Python-powered toolkit for Quality Control Circle project work. |
| G2 | Treat QCC stage workflow as the organizing frame for methods, templates, guides, analyses, charts, scripts, evidence packages, and outputs. |
| G3 | Implement a core QCC method engine with stage-aware method selection, input contracts, validation, calculations, chart specifications, summaries, and report-ready artifacts. |
| G4 | Prioritize the core QCC toolkit first: 5W2H, SIPOC, Flowchart, Check Sheet, Sampling, Stratification, Pareto Chart, Fishbone Diagram, 5 Whys, Histogram, Scatter Diagram, Control Chart, and Poka-Yoke records. |
| G5 | Make generated charts method-aware, stage-aware, reproducible, and review-ready rather than decorative visuals. |
| G6 | Preserve calculation assumptions, input data context, filters, parameters, version metadata, warnings, and interpretation with each generated chart. |
| G7 | Provide Markdown documentation for each QCC method explaining what it is, when to use it, when not to use it, required inputs, procedure, chart support, interpretation guidance, and common mistakes. |
| G8 | Provide beginner-friendly Python scripts and examples that let users run common QCC methods from CSV or Excel-like data without designing a full application first. |
| G9 | Treat PowerPoint QCC method templates as first-class user-facing assets for method teaching, demo examples, and copyable QCC slide structures. |
| G10 | Support notebooks as an ergonomic learning and review surface while keeping the core library scriptable and suitable for later CLI, batch, API, or UI surfaces. |
| G11 | Keep the project small enough to build and verify by avoiding enterprise workflow, dashboard, and document-editor scope. |

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Build a no-code desktop application as the initial product. |
| NG2 | Build a general-purpose business intelligence dashboard platform. |
| NG3 | Replace specialized statistical software for advanced industrial statistics. |
| NG4 | Build a broad enterprise quality management system, CAPA system, audit system, or workflow approval platform. |
| NG5 | Build a generic plotting library unrelated to QCC stages and method logic. |
| NG6 | Treat PPT templates, notebooks, or example scripts as the source of truth for formulas, validation logic, or final data-dependent chart calculations. |
| NG7 | Implement every advanced quality method in the first product slice. DOE, QFD, Kano, matrix data analysis, advanced regression, and complex network planning can be deferred. |
| NG8 | Define final implementation tasks, milestones, or ticket-level plans in this proposal. Those belong in downstream specs and plans. |
| NG9 | Adopt governance, release policy, or source-of-truth rules beyond what is necessary to describe this project direction. |

## Vision fit

fits the current vision

The proposal fits the existing vision because it keeps QCC stage workflow visible, treats charts as evidence objects, emphasizes explainable and testable quality methods, prioritizes chart and report outputs for review and project documentation, and preserves the split where PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates evidence.

The revised direction reflects the current vision more directly.
PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates evidence.
PPT method templates are first-class user-facing assets, but generated charts, calculations, captions, warnings, and metadata remain traceable to the method engine and evidence package.

The proposal also follows the positioning direction that QCC Toolkit should favor QCC project coherence and explainable evidence over broad dashboard, document-editing, or general statistical-platform scope.

## Context

QCC Toolkit is now positioned as a template-backed, Python-powered evidence system for Quality Control Circle method work.
Its primary users are QCC facilitators, quality engineers, improvement teams, educators, and analysts who need repeatable support for QCC workflows, methods, analysis, charts, and report artifacts.

The current vision and positioning identify the same core pain: QCC project evidence is scattered across multiple tools, making it difficult to repeat, review, teach, and explain.
The project should therefore treat a generated chart as part of a QCC evidence story rather than as a standalone graphic.

This revision makes the template-backed workflow central.
The first usable release should not require users to abandon familiar QCC slide templates or understand the entire future architecture.
It should connect practical templates, method guides, generated evidence, and ready-to-run assets:

| Asset | Purpose | Relationship to core toolkit |
|---|---|---|
| Markdown method guides | Explain how and when to use each QCC method. | Human-facing documentation tied to method registry IDs and QCC stages. |
| Python scripts | Let users run common methods quickly from local data. | Thin wrappers around the public Python API, not duplicated formulas. |
| Notebooks | Support teaching, exploration, review, and example-based learning. | Examples that call the same public API as scripts. |
| Synthetic datasets | Provide safe, reusable examples for manufacturing and service QCC cases. | Test fixtures and teaching inputs. |
| PowerPoint method templates | Teach methods, provide demo examples, and give users copyable QCC slide structures. | First-class presentation pattern and teaching-layout assets tied to method IDs. |
| Markdown or HTML reports | Provide lightweight report-ready outputs before complex office export. | Structured output generated from method results and chart specifications. |

## Resolved questions

The previous proposal listed open questions.
This revision resolves them as proposal-level defaults.
Downstream specifications can refine details, but they should not reopen these decisions without a new proposal or decision record.

| ID | Question | Decision |
|---|---|---|
| RQ1 | Which Python versions should be supported initially? | Support Python 3.11 through 3.14 initially. Exclude Python 3.10 from the first support matrix because it is close to upstream end-of-life in 2026. Revisit the minimum version before 1.0 if dependency compatibility or user environments require a narrower or broader range. |
| RQ2 | Should pandas be the only first-class DataFrame dependency at launch? | Use pandas as the first-class tabular dependency and document pandas-compatible inputs. Keep internal boundaries clean enough to add Polars or Arrow-backed adapters later, but do not make multiple DataFrame engines part of the first slice. |
| RQ3 | Which control-chart rules should be supported first? | Start with basic control-limit generation, center line, UCL, LCL, and explicit rule configuration. Support simple individual/run-style charts first, then add common attribute and subgroup charts as method contracts mature. Defer complex rule-pack automation until formulas, examples, and warnings are well documented. |
| RQ4 | Which report formats should be supported first? | Support Markdown and HTML report output first. Add static image export for charts where practical. Include PPT slide templates in the first adoption slice, but defer fully automated PPTX generation until the report object model stabilizes. |
| RQ5 | Should Plotly be the only renderer? | Use Plotly as the first renderer for interactive charts. Keep chart specifications renderer-aware but not renderer-locked so static image, HTML, and future rendering paths can reuse the same calculation results. |
| RQ6 | How should authoritative quality-method formulas and definitions be documented? | Create one Markdown method guide per method, with formula notes, assumptions, input contracts, examples, interpretation guidance, cautions, and references. Method docs should be treated as part of the method contract, not optional marketing documentation. |
| RQ7 | Should examples use synthetic manufacturing, service, or mixed datasets? | Use mixed synthetic datasets. Include at least one manufacturing-style defect dataset and one service/process-error dataset so the toolkit does not appear manufacturing-only. |
| RQ8 | How much generated interpretation should be automated? | Start with deterministic, transparent summaries and warnings. Avoid opaque AI-generated conclusions in the core. Generated interpretation should explain what was calculated, what appears important, and what the user should verify next. |
| RQ9 | Should a project-folder file format be defined in the first slice? | Define a lightweight project-folder convention in the first slice because scripts, examples, report generation, and reproducibility benefit from predictable paths. Keep it simple enough to change before 1.0. |
| RQ10 | Should PPT templates be part of the first slice? | Yes, as first-class user-facing assets. Start with static method templates and slide-outline documentation. Automated PPTX export can follow when chart-export, placeholder, and report-bundle contracts are stable. |
| RQ11 | Should simple Python scripts be implemented before a polished application? | Yes. Starter scripts should be the first practical execution surface after the minimal core API because they help users apply QCC methods immediately and keep the product local-first. |
| RQ12 | Should Markdown method documentation be created before or after code? | Create method documentation alongside the first method contracts. For each core method, the documentation should define intended use before implementation is considered complete. |

## Options considered

| Option | Name | Summary | Benefits | Costs / risks | Decision |
|---|---|---|---|---|---|
| O1 | Template-only first | Start with spreadsheets and presentation templates before a reusable method engine. | Familiar to QCC teams; easy to demonstrate; low technical barrier. | Does not solve reproducibility; formulas and charts remain fragile; difficult to test; weak Python identity. | Rejected option. |
| O2 | Generic charting/statistics library with QCC examples | Build chart functions and statistical helpers, then add QCC examples. | Faster to build charts; flexible for analysts. | Weak differentiation; QCC stage workflow becomes superficial; likely to violate the vision by becoming unrelated plotting helpers. | Rejected option. |
| O3 | Full web application or dashboard first | Build a complete web product around QCC project stages. | Clear product experience; easier for non-programmers. | Higher delivery risk; premature UI decisions; backend method contracts may become inconsistent; risks dashboard scope creep. | Deferred follow-up. |
| O4 | Python-first library API with notebook ergonomics and report-ready artifacts | Build the reusable method engine first, with notebooks as the first ergonomic surface. | Strong fit with vision; testable; reusable; supports notebooks, scripts, batch, and later UI surfaces. | Requires disciplined API design and documentation; non-programmers may need simpler starter assets. | Recommended foundation. |
| O5 | Template-backed adoption slice around the Python core | Combine first-class PPT method templates, Markdown guides, minimal Python evidence generation, starter scripts, synthetic data, notebooks, and an evidence package. | Matches how users already learn and present QCC methods while preserving reproducibility and testability. | Requires careful source-of-truth discipline so templates, docs, scripts, and evidence do not drift. | Recommended first usable slice. |
| O6 | Enterprise quality-management platform | Add approvals, CAPA, audit workflows, and document control. | Broad market category; can integrate formal quality workflows. | Far outside current focus; high operational, security, and compliance burden; dilutes QCC-specific value. | Out of scope. |

## Recommended direction

Create QCC Toolkit as a template-backed, Python-powered project for QCC method education, chart generation, and evidence preparation.
The core should model QCC projects, stages, method instances, templates, method guides, data contracts, calculation results, chart specifications, interpretations, evidence packages, and report artifacts.

PowerPoint QCC method templates are first-class user-facing assets.
They explain each method, provide demo examples, and give users copyable slide structures for their own QCC materials.

Python is the evidence-generation layer for data-dependent methods.
It validates project data, calculates tables, generates charts, creates deterministic captions and warnings, and writes metadata that makes outputs reproducible.

Markdown method guides are the version-controlled method-knowledge layer.
They define when to use each method, when not to use it, required inputs, outputs, procedure, interpretation guidance, common mistakes, and links to matching templates and scripts.

The first usable slice should include three things together:

| Slice component | Recommendation | Reason |
|---|---|---|
| PowerPoint method templates | Provide first-class QCC teaching and presentation structures. | Matches the easiest existing user workflow and gives users copyable method examples. |
| Minimal core API | Implement method contracts and chart-generation logic for data-dependent QCC methods. | Prevents scripts, examples, and templates from becoming disconnected manual assets. |
| Markdown method library | Document each method with usage guidance, inputs, procedure, interpretation, cautions, and examples. | Helps users know when and how to use QCC methods. |
| Starter assets | Provide Python scripts, notebooks, synthetic datasets, and an evidence package. | Gives users immediate practical entry points without waiting for a web UI. |

The project should treat charts as evidence objects.
A Pareto chart, control chart, histogram, or scatter diagram should carry enough metadata to explain what data was used, which filters were applied, what method rules were used, which QCC stage it supports, and what interpretation was generated.

The first release should not attempt to replace PowerPoint or fully automate slide decks.
It should help users keep their familiar template workflow while improving the reliability and traceability of the charts and evidence inserted into those templates.

The source-of-truth split is:

| Surface | Source-of-truth role |
|---|---|
| PowerPoint method templates | Presentation pattern, teaching layout, reusable demo examples, and copyable slide structures. |
| Markdown method guides | Method explanation, usage guidance, review checklist, and method-selection advice. |
| Python method contracts | Data validation, formulas, calculations, chart specifications, generated captions, warnings, and metadata. |
| Evidence package | Final generated charts, tables, captions, metadata, and reproducibility information. |

The recommended initial implementation technology is:

| Layer | Recommendation | Rationale |
|---|---|---|
| Core language | Python | Best fit for quality-method calculations, tabular data, notebooks, packaging, and report-generation workflows. |
| Python support | Python 3.11 to 3.14 initially | Covers currently supported modern Python versions while avoiding near-EOL Python 3.10. |
| Package shape | `qcc_toolkit` Python package managed with `pyproject.toml` | Keeps the core reusable across notebooks, scripts, batch, APIs, and later UI surfaces. |
| Data contracts | Pydantic models plus DataFrame schema validation | Gives structured validation for method parameters, chart specifications, and export metadata. |
| Tabular analysis | pandas-compatible internal interfaces first | Matches common Python analysis workflows and Plotly interoperability; Polars support can be considered later. |
| Charts | Plotly-first chart specifications and renderers | Good default for interactive QCC charts; chart specs can later support static exporters. |
| Static chart export | Plotly static image export through the maintained Kaleido path where practical | Enables Markdown, HTML, and slide/report artifacts to use the same chart results. |
| PPT template support | First-class static PPT method templates; later generation with `python-pptx` if needed | Lets users learn and present QCC methods early while avoiding premature deck-automation complexity. |
| Documentation | Markdown method pages under a stable `docs/methods/` structure | Keeps method guidance versioned, reviewable, searchable, and close to the code. |
| Scripts | Thin Python scripts under `examples/scripts/` or an equivalent examples area | Helps users run methods without building an application and keeps calculations inside the public API. |
| Testing | pytest-based test suite | Supports unit, integration, regression, documentation-example, and chart-spec tests. |
| Quality gates | Ruff, type checking, pre-commit hooks, CI package-build checks | Keeps the project maintainable as statistical and chart logic grows. |
| Future API/UI | FastAPI and a separate frontend only after method contracts stabilize | Avoids letting UI concerns define core method behavior prematurely. |

## Evidence notes for technology defaults

The technology defaults in this proposal are based on portable project practices and current ecosystem status checked on 2026-07-08.
These notes are included so downstream specifications can see why the defaults were selected.

| Evidence note | Proposal implication | Source |
|---|---|---|
| The Python Developer's Guide lists Python 3.14 and 3.13 in bugfix status, Python 3.12 and 3.11 in security status, and Python 3.10 with end-of-life in 2026-10. | Initial support should target Python 3.11 through 3.14 and avoid starting a new project with Python 3.10 as a required supported version. | https://devguide.python.org/versions/ |
| The Python Packaging User Guide describes `pyproject.toml` as a configuration file used by packaging tools and says the `[build-system]` table should always be present. | The package should use `pyproject.toml` as the packaging and tool-configuration center. | https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ |
| Plotly's Python documentation describes static image export to PNG, JPEG, SVG, PDF, and other formats through Kaleido. | Plotly can serve as the first interactive chart renderer and produce static assets for reports or slides where practical. | https://plotly.com/python/static-image-export/ |
| The `python-pptx` documentation describes creating, reading, and updating `.pptx` files without requiring the PowerPoint application to be installed or licensed. | Static PPT templates can be included early, and automated PPTX generation can be added later when report-bundle contracts stabilize. | https://python-pptx.readthedocs.io/en/latest/ |

## Method documentation model

Each QCC method should have a Markdown guide with a consistent structure.
This documentation should be treated as a user-facing method contract.

Recommended path pattern:

```text
docs/methods/<method-id>.md
```

Recommended method-guide sections:

| Section | Purpose |
|---|---|
| Method summary | Explain the method in one short paragraph. |
| QCC stage fit | Show which QCC stage or stages the method supports. |
| When to use | Explain the conditions where the method is appropriate. |
| When not to use | Warn against common misuse. |
| Inputs required | List data columns, qualitative inputs, or project context required. |
| Outputs produced | List tables, charts, diagrams, summaries, and report artifacts. |
| Procedure | Give the practical steps a QCC team should follow. |
| Chart support | Explain whether the method produces a chart and what chart type. |
| Interpretation guidance | Explain how to read the result and what conclusions are safe. |
| Common mistakes | Capture practical mistakes and misleading uses. |
| Example | Link to a script, notebook, dataset, or image. |
| Related methods | Suggest upstream and downstream QCC methods. |
| Formula or logic notes | Document formulas, assumptions, or decision rules where applicable. |
| Review checklist | Provide a small checklist for facilitators or reviewers. |

Formula and method references should prefer recognized quality references, standards, or authoritative training materials.
When formulas vary by convention, the method guide should state which convention the toolkit implements and why.

Recommended front matter should include at least `method_id`, `method_name`, `qcc_stages`, `method_type`, `supports_generated_chart`, `first_slice_status`, and `last_reviewed`.

Recommended first method-documentation set:

| Stage | Method docs |
|---|---|
| Select Theme / Define Problem | 5W2H, VOC and CTQ, SIPOC |
| Understand Current Condition | Flowchart, Check Sheet, Sampling, Stratification, Pareto Chart, Histogram |
| Analyze Causes | Fishbone Diagram, 5 Whys, Scatter Diagram |
| Develop Countermeasures | Poka-Yoke, matrix selection notes, basic FMEA notes if included later |
| Verify Effects / Control | Control Chart, before/after Pareto, monitoring Check Sheet |
| Reflect and Share | QCC story report, lessons learned, standardization record |

## Starter script model

Starter scripts should be thin, readable, and practical.
They should help users apply one method at a time while calling the public API.
They should not duplicate formulas or create a second implementation path.

Recommended script categories:

| Script category | Example purpose |
|---|---|
| Data inspection | Load a CSV or Excel-like file, validate required columns, and summarize missing values. |
| Pareto generation | Generate a Pareto table, chart, caption, and Markdown snippet from defect data. |
| Histogram generation | Generate a histogram, summary statistics, and interpretation notes for numeric CTQ data. |
| Scatter generation | Generate a scatter diagram, correlation summary, and caution notes. |
| Control chart generation | Generate a basic control chart with center line, limits, warnings, and metadata. |
| QCC report bundle | Combine selected evidence outputs into a Markdown or HTML report. |
| Slide asset export | Export selected charts and captions for insertion into the PPT template. |

Recommended script principles:

| Principle | Description |
|---|---|
| Local-first | Scripts should run on local files without requiring a server or cloud service. |
| Explicit inputs | Required columns and parameters should be visible in script help text or config. |
| Public API only | Scripts should call stable package functions instead of internal modules. |
| Reproducible outputs | Scripts should write output files with metadata and stable chart specifications. |
| Small scope | One script should solve one clear QCC task. |
| Testable examples | Scripts should be tested with synthetic datasets in CI where practical. |

## PPT template model

PPT slide templates should help QCC teams present methods and evidence in a standard story.
They should not define formulas, validation rules, or chart logic.

Recommended static template set:

| Template | Purpose |
|---|---|
| QCC project story deck | End-to-end project presentation structure. |
| Theme selection slide | Show problem background, business impact, and project scope. |
| 5W2H problem-definition slide | Present the problem statement clearly. |
| SIPOC / flow slide | Show process scope and major steps. |
| Current-condition slide | Present baseline data, check sheet summary, or stratified view. |
| Pareto slide | Show vital few categories and interpretation. |
| Root-cause slide | Show fishbone or 5 Whys output. |
| Countermeasure slide | Show selected actions, owners, and expected effect. |
| Verification slide | Show before/after chart, control chart, or result summary. |
| Standardization slide | Show updated SOP, training, control plan, and next monitoring method. |

Recommended PPT principles:

| Principle | Description |
|---|---|
| Evidence-driven | Slides should contain chart images, captions, metadata, and method interpretation generated from evidence objects. |
| Editable | Users should be able to edit static templates manually when automation is not available. |
| Traceable | Slide captions should preserve data source, date range, filters, and method name where practical. |
| Not authoritative | The authoritative record should remain the project evidence package, not manually edited slides. |
| Automatable later | Templates should be structured so later `python-pptx` generation can fill placeholders consistently. |

## Template-backed workflow

The default first-release workflow should be:

1. User opens a QCC method PowerPoint template.
2. User learns the method and reviews the demo example.
3. User prepares project data using the documented input format.
4. User runs a Python script or notebook for the method.
5. Toolkit validates the data and generates chart image, calculated table, caption, warnings, and metadata.
6. User inserts the generated chart and caption into the PowerPoint template or project deck.
7. User keeps the evidence package with the final QCC materials.

This workflow keeps PowerPoint as the easiest user-facing path while making final data-dependent evidence reproducible through Python outputs and metadata.

## Method classification model

Not every QCC method needs the same implementation depth.
The first slice should classify methods by how much Python evidence generation they need.

| Method type | Examples | First implementation |
|---|---|---|
| Template-guided methods | 5W2H, Fishbone, 5 Whys, Poka-Yoke, SIPOC | PowerPoint template, Markdown guide, and optional structured notes. |
| Data-chart methods | Pareto, Histogram, Scatter Diagram, Stratification, Control Chart, Before/After Chart | PowerPoint template, Markdown guide, Python chart generator, and evidence package. |
| Advanced analytical methods | Process Capability, Regression, DOE, FMEA, QFD, Kano | Defer or implement carefully after core method contracts stabilize. |

This classification prevents overengineering.
Fishbone does not need heavy Python automation in the first version, while Pareto and Control Chart need Python-backed calculation, validation, and interpretation because formula consistency matters.

## Template governance model

Templates are first-class assets, so they need lightweight governance.

| Practice | Reason |
|---|---|
| Assign every template a stable `template_id`. | Allows scripts, docs, examples, and future automation to reference it. |
| Assign every QCC method a stable `method_id`. | Keeps Markdown, Python, and PPT aligned. |
| Maintain `templates/ppt/catalog.yml`. | Makes template inventory reviewable and script-friendly. |
| Add version metadata to each template. | Helps users know which template version they used. |
| Label demo charts clearly. | Prevents sample charts from being mistaken for project evidence. |
| Provide a blank user slide in every template. | Makes copying safe and consistent. |
| Reserve placeholders for generated charts and captions. | Enables later automation without redesigning templates. |
| Review PPT templates against Markdown guides. | Prevents method explanation drift. |

Demo charts in method templates should be labeled as demo examples, not project evidence.
Final data-dependent charts should be traceable to source data, method ID, parameters, filters, calculation version, chart specification, output file, and toolkit version.

## Template catalog artifact

The first slice should include a template catalog:

```text
templates/ppt/catalog.yml
```

Example shape:

```yaml
schema_version: 1
templates:
  - template_id: pareto_chart_method_template
    method_id: pareto_chart
    template_type: method_template
    qcc_stages:
      - understand_current_condition
      - analyze_causes
    file: templates/ppt/methods/pareto-chart-template.pptx
    markdown_guide: docs/methods/pareto-chart.md
    python_generator: examples/scripts/generate_pareto.py
    example_project: examples/projects/reduce-packing-label-errors
    supports_generated_chart: true
    expected_placeholders:
      - chart_image
      - calculated_table
      - caption
      - data_context
      - warnings
    expected_assets:
      - chart_image
      - calculated_table
      - caption
      - metadata
```

The catalog gives downstream specs a concrete traceability surface for method-template coverage, documentation checks, example checks, and future PPT automation.

## Revised first-slice scope

The first implementation slice should prove one complete vertical example plus a small method library.

| Deliverable | Recommendation |
|---|---|
| One complete demo project | Use "Reduce Packing Label Errors" or an equivalent synthetic QCC story. |
| Three to five method templates | Pareto, Check Sheet, 5W2H, Fishbone, and 5 Whys. |
| Two Python chart generators | Pareto and Before/After Pareto first; Control Chart can follow. |
| Markdown guides | One guide per included method. |
| Template catalog | Map PPT templates to method IDs, docs, examples, and supported generated assets. |
| Evidence package format | Chart image, calculated table, caption, warnings, metadata, and README. |
| Script smoke tests | Ensure sample scripts regenerate expected outputs. |
| Documentation checks | Ensure docs link to templates, scripts, examples, and method IDs. |

Pareto Chart should be the first complete vertical method because it exercises data validation, calculation, charting, interpretation, report output, scripts, PPT template placeholders, and evidence packaging in one method.
Check Sheet, 5W2H, Fishbone, and 5 Whys should support the same adoption slice as lighter template-guided methods.

Control Chart remains part of the core method roadmap, but it is not required in the first vertical proof slice unless the method-contract specification chooses to include it.

Suggested first-slice acceptance criteria for downstream specs:

| ID | Criterion |
|---|---|
| AC1 | One synthetic QCC project regenerates a Pareto chart evidence package from local data. |
| AC2 | The generated evidence package includes chart, calculated table, caption, warnings, and metadata. |
| AC3 | The Pareto method guide explains when to use it, when not to use it, required inputs, procedure, interpretation, and common mistakes. |
| AC4 | The Pareto PPT template exists and is listed in `templates/ppt/catalog.yml`. |
| AC5 | The starter script calls the public API only. |
| AC6 | The same input data and parameters produce the same calculation result and chart specification. |
| AC7 | Script smoke tests regenerate expected artifacts from synthetic data. |
| AC8 | Documentation checks confirm method IDs, guide paths, script paths, and template catalog paths are consistent. |
| AC9 | No real customer data is included in examples. |
| AC10 | The first slice does not add web UI, dashboard, CAPA/EQMS, or advanced method scope. |

## Expected behavior changes

| ID | Expected behavior change |
|---|---|
| B1 | Users can create or load a QCC project context and associate work with a QCC stage. |
| B2 | Users can read a method guide to understand when and how to use a QCC method before running it. |
| B3 | Users can select a quality method based on the current stage and available data. |
| B4 | Users receive validation feedback before invalid charts or misleading statistical outputs are generated. |
| B5 | Users can run starter Python scripts against local CSV or Excel-like data to produce QCC tables, charts, captions, and warnings. |
| B6 | Users can generate QCC charts that include calculated tables, metadata, warnings, and interpretation text. |
| B7 | Users can connect charts and analyses to root-cause notes, countermeasure records, and standardization records. |
| B8 | Users can produce Markdown or HTML report-ready outputs without manually reconstructing the evidence chain from spreadsheets, scripts, and slides. |
| B9 | Users can use first-class PPT method templates to learn methods, copy slide structures, and present QCC work while preserving links to generated evidence where practical. |
| B10 | Users can reproduce a previous chart from the source data, method parameters, chart specification, and toolkit version. |
| B11 | Users can teach or review QCC projects through method templates, method docs, notebooks, scripts, datasets, and examples that expose the full reasoning path. |
| B12 | Users and reviewers can trace each supported template to a method ID, Markdown guide, script, example dataset, and supported generated assets through a template catalog. |

## Architecture impact

The project should use a layered architecture that keeps QCC method logic independent from presentation surfaces.
Markdown docs, scripts, notebooks, reports, and PPT templates should consume the same method contracts and chart specifications instead of reimplementing logic.

Recommended conceptual flow:

```text
QCC Project
  -> Stage
    -> Method Template
      -> Method Guide
        -> Method Instance
          -> Data Contract
            -> Validated Dataset
              -> Calculation Result
                -> Chart Specification
                  -> Rendered Chart or Diagram
                    -> Interpretation
                      -> Evidence Package
                        -> Markdown / HTML / Slide-Ready Asset
```

Recommended package and repository boundaries:

| Area | Responsibility |
|---|---|
| `qcc_toolkit.project` | Project, stage, theme, target, and evidence-package models. |
| `qcc_toolkit.stages` | Canonical QCC Story stage model, aliases, and terminology mapping. |
| `qcc_toolkit.methods` | Method registry and method instances such as Pareto, 5 Whys, Fishbone, Histogram, Control Chart, and Poka-Yoke. |
| `qcc_toolkit.contracts` | Input contracts, parameter models, chart-spec models, and validation rules. |
| `qcc_toolkit.analysis` | Statistical calculations and method-specific result generation. |
| `qcc_toolkit.charts` | Chart specifications, renderers, chart metadata, and export adapters. |
| `qcc_toolkit.interpretation` | Structured summaries, warnings, recommended next methods, and report captions. |
| `qcc_toolkit.evidence` | Evidence package metadata, generated asset records, reproducibility data, and final evidence manifests. |
| `qcc_toolkit.reports` | Report-ready bundles, Markdown/HTML outputs, and later PDF/PPTX support. |
| `qcc_toolkit.io` | CSV, Excel, JSON, and project-folder input/output. |
| `qcc_toolkit.templates` | Template metadata and future hooks for report and slide templates. |
| `docs/methods` | User-facing QCC method guides. |
| `examples/scripts` | Starter Python scripts that call the public API. |
| `examples/notebooks` | Teaching and review notebooks that call the public API. |
| `examples/data` | Synthetic manufacturing and service datasets. |
| `templates/ppt/catalog.yml` | Template inventory mapping template IDs to method IDs, docs, scripts, examples, and generated assets. |
| `templates/ppt/methods` | Static PPT method templates. |
| `templates/ppt/story-decks` | Static QCC story deck templates. |

The architecture should make it possible for notebooks, scripts, CLI commands, APIs, and future UIs to call the same validated method engine.
Frontend, notebook, script, template, or slide code should not be responsible for statistical formulas or method-specific validation.

## Testing and verification strategy

Testing should focus first on calculation correctness, validation behavior, reproducibility, evidence traceability, documentation accuracy, and example usability.

| Test area | Strategy |
|---|---|
| Formula unit tests | Use known fixtures for Pareto counts, cumulative percentages, histograms, scatter/correlation, control-limit calculations, and process-capability calculations when introduced. |
| Validation tests | Confirm invalid data shapes, missing columns, invalid parameter ranges, impossible chart requests, and misleading-method conditions produce clear warnings or errors. |
| Chart-spec tests | Snapshot chart specifications rather than relying only on rendered pixel output. |
| Reproducibility tests | Confirm the same input dataset, parameters, and toolkit version produce the same calculation result and chart specification. |
| Documentation tests | Check that method docs link to valid examples, refer to known method IDs, and do not drift away from supported inputs and outputs. |
| Script smoke tests | Run starter scripts against synthetic datasets and verify expected output files are produced. |
| Notebook smoke tests | Execute notebooks or convert key examples to CI-testable scripts where practical. |
| Report artifact tests | Confirm report-ready outputs contain expected charts, tables, metadata, captions, and warnings. |
| PPT template checks | Confirm templates exist, use expected placeholders, and match the QCC story structure. Automated PPTX generation can receive deeper tests later. |
| Template catalog checks | Confirm every listed template has a stable template ID, method ID, guide link, file path, and expected generated assets. |
| Type and style checks | Run static checks, formatting checks, and import/package-build checks in CI. |
| Security-oriented tests | Validate file parsing assumptions, path handling, unsafe formula content in imported spreadsheets, and privacy expectations for sample data. |

Verification evidence should include passing CI, formula fixture results, chart-spec snapshots, script outputs, example outputs, documentation-link checks, and sample report artifacts.
Manual review should remain important for visual clarity and QCC story quality, but formula correctness should not rely on manual inspection alone.

## Rollout and rollback

Rollout should begin with a small Python package surface and a practical adoption pack.
APIs can remain explicitly unstable until method contracts, chart specs, documentation structure, and example scripts are validated with real examples.

Recommended rollout posture:

| Area | Approach |
|---|---|
| Package release | Begin with pre-1.0 releases until public method contracts, chart specs, and stage model are stable. |
| API compatibility | Treat method input/output contracts as the most important compatibility surface. |
| Method documentation | Release docs with the first supported methods so users know when and how to use them. |
| Starter scripts | Release scripts early as thin public-API examples, not as separate product logic. |
| Examples | Release synthetic datasets and examples before broad feature expansion so users can validate the QCC story flow. |
| PPT templates | Release first-class static templates early; add automated PPTX generation only when placeholders and report-bundle contracts stabilize. |
| Feature expansion | Add advanced methods only after the core QCC toolkit is tested and documented. |
| Export formats | Start with Markdown/HTML and static image export where practical; add PPTX/PDF after report contracts stabilize. |
| Future UI | Build UI/API surfaces only after core contracts are stable enough to prevent duplicate method logic. |

Rollback should be handled through package version pinning, retained chart-spec versions, reproducible project artifacts, and stable example datasets.
If a method formula, chart rule, or method-documentation contract changes, the project should preserve enough version metadata to distinguish old outputs from new outputs.
Deprecation should be favored over abrupt removal once public examples, scripts, or templates depend on an API.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Scope creep into generic dashboards or enterprise quality systems | Dilutes the project and increases delivery risk. | Keep the QCC Story model and method registry as the organizing frame; reject features that do not improve QCC evidence. |
| Starter scripts become a second implementation | Creates inconsistent formulas and maintenance burden. | Scripts should call public APIs only and should be covered by smoke tests. |
| PPT templates become manual source of truth | Weakens reproducibility and traceability. | Treat slides as teaching and presentation surfaces; preserve evidence bundles, chart specs, captions, and metadata separately. |
| Template catalog drifts from files | Breaks traceability between templates, docs, scripts, and examples. | Check catalog paths and method IDs in CI once tooling exists. |
| Method docs drift from code | Users learn unsupported behavior. | Link docs to method IDs, include docs checks, and update method docs with method contract changes. |
| Incorrect statistical formulas | Damages trust and may mislead QCC teams. | Use fixture-based tests, external formula references, peer review, and visible formula documentation. |
| Misleading charts from invalid data | Users may draw false conclusions. | Add method contracts, validation checks, sample-size warnings, stability warnings, and chart metadata. |
| Overly complex initial scope | Delays usable release. | Prioritize core QCC methods, docs, scripts, and essential charts; defer advanced tools such as DOE, QFD, Kano, and complex network diagrams. |
| Ambiguous QCC terminology across organizations | Confuses users and examples. | Use stable internal stage identifiers with customizable display labels and aliases. |
| Report outputs become brittle | Users may return to manual slide assembly. | Treat report artifacts as structured outputs generated from evidence objects, not one-off templates. |
| Dependency churn | Breaks charting, validation, export, or packaging unexpectedly. | Keep a small dependency set, use CI, version constraints, and compatibility notes. |
| Notebook examples diverge from package behavior | Teaching material becomes unreliable. | Run example smoke tests and make examples call public APIs only. |
| Data privacy concerns | Users may hesitate to use real quality data. | Keep the core local-first; avoid network transmission by default; use synthetic sample datasets. |
| Performance issues on large datasets | Users may see slow chart generation. | Optimize after core correctness; keep data processing interfaces separable enough to add Polars or lazy execution later. |

## Open questions

No proposal-level open questions remain after this revision.
The previous open questions are answered in the `Resolved questions` section.

The following downstream design details remain for specification work and do not block proposal review:

| ID | Downstream detail | Proposed owner artifact |
|---|---|---|
| DQ1 | Exact Markdown method-guide template wording and front matter fields. | Method documentation specification. |
| DQ2 | Exact starter script names, command-line arguments, and output-folder convention. | Starter scripts specification or product specification. |
| DQ3 | Exact PPT slide dimensions, placeholder names, style, and deck structure. | PPT template specification. |
| DQ4 | Exact first control-chart set and rule-pack wording. | Method contracts specification. |
| DQ5 | Exact supported static image formats and export dependencies. | Chart generation specification. |
| DQ6 | Exact project-folder schema and metadata file names. | Architecture design or project format specification. |
| DQ7 | Exact `templates/ppt/catalog.yml` schema. | PPT template specification or template catalog specification. |

Recommended defaults for downstream specs:

| ID | Recommended default |
|---|---|
| DQ1 | Use one guide per method under `docs/methods/<method-id>.md`, with front matter for method ID, name, stages, method type, generated-chart support, first-slice status, and review date. |
| DQ2 | Start with method-specific scripts such as `generate_pareto.py`, `generate_before_after_pareto.py`, `generate_histogram.py`, `generate_scatter.py`, `generate_control_chart.py`, and `build_qcc_report.py`; scripts should write to method-scoped evidence folders. |
| DQ3 | Use 16:9 widescreen PPT templates with stable semantic placeholders such as `project_title`, `qcc_stage`, `method_name`, `chart_image`, `calculated_table`, `caption`, `data_context`, `warnings`, and `next_method_suggestion`. |
| DQ4 | Start control-chart support with individuals-style chart behavior, center line, UCL, LCL, explicit calculation parameters, and visible warnings; defer complex rule-pack automation. |
| DQ5 | Treat `.html` as the first interactive chart output and `.png` as the first static output; keep `.svg` optional and defer `.pdf` or `.pptx` embedding until renderer and report contracts stabilize. |
| DQ6 | Use a lightweight project folder with `qcc-project.yml`, `data/`, `methods/`, `evidence/`, `reports/`, and `slides/`; keep the format explicitly pre-1.0. |
| DQ7 | Use a small `templates/ppt/catalog.yml` schema with `schema_version`, unique `template_id`, `method_id`, template type, stages, file path, guide path, optional generator path, example project, placeholders, and expected assets. |

## Decision log

| Date | Decision | Reason | Alternatives rejected or deferred |
|---|---|---|---|
| 2026-07-07 | Use `qcc-toolkit` / `qcc_toolkit` as the working project identity. | Clear, searchable, and broad enough for QCC methods, workflows, charts, and reports. | Overly narrow names such as chart-only or method-only names. |
| 2026-07-07 | Recommend a Python-first library API as the primary product foundation. | Best fit for repeatability, testability, notebooks, scripts, and future UI reuse. | Spreadsheet-first, UI-first, and generic charting-library-first approaches. |
| 2026-07-07 | Treat method documentation as a first-slice deliverable. | Users need to know when and how to use each QCC method, not only how to call code. | Code-only implementation; scattered tutorial notes. |
| 2026-07-07 | Treat starter Python scripts as the first practical execution surface. | Scripts help users run QCC methods quickly while preserving local-first and reproducible behavior. | Web-app-first execution; notebook-only execution. |
| 2026-07-07 | Treat static PPT method templates as first-class user-facing assets. | QCC users learn from templates, copy examples from them, and present project stories through them. | Template-only product; fully automated PPTX generation before placeholders and report contracts stabilize. |
| 2026-07-07 | Use `templates/ppt/catalog.yml` as the template traceability artifact. | The catalog keeps template IDs, method IDs, guides, scripts, examples, and generated assets reviewable. | Untracked template folders; chat-only template inventory. |
| 2026-07-07 | Treat notebooks as an ergonomic teaching and review surface. | Supports exploration, teaching, and review without compromising the core library. | Notebook-only architecture; batch-only architecture. |
| 2026-07-07 | Use a canonical QCC Story stage model internally. | Provides a stable workflow model while allowing local terminology. | Pure PDCA-only, DMAIC-only, or organization-specific stage models. |
| 2026-07-07 | Treat generated charts as evidence objects. | Supports review, teaching, reproducibility, and report generation. | Decorative chart rendering with hidden assumptions. |
| 2026-07-07 | Support Python 3.11 through 3.14 initially. | Balances modern dependency support with practical user environment coverage. | Python 3.10 support; single-version support. |
| 2026-07-07 | Defer web UI and enterprise features. | Prevents premature complexity and protects the QCC-specific scope. | Full dashboard application, CAPA/EQMS platform, document-control system. |
| 2026-07-07 | Keep the repository's existing Apache-2.0 license unless a separate governance decision changes it. | `LICENSE` already records Apache-2.0 for this repository. | MIT or other licenses are not selected in this proposal. |
| 2026-07-08 | Make Pareto the first complete vertical method. | Pareto exercises data validation, calculation, charting, interpretation, report output, scripts, PPT template placeholders, and evidence packaging in one method. | Start with all methods equally; start with Fishbone only. |

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Build the overall QCC Toolkit project. | in scope | Goals, Recommended direction, Architecture impact |
| Implement the best core QCC toolkit for different QCC stages. | in scope | Goals, Context, Scope budget |
| Emphasize chart generation. | in scope | Goals, Recommended direction, Expected behavior changes, Architecture impact |
| Choose implementation technology such as programming language. | in scope | Recommended direction, Resolved questions |
| Follow best practices. | in scope | Testing and verification strategy, Risks and mitigations, Rollout and rollback |
| Preserve the vision and answer open questions before implementation. | in scope | Vision fit, Resolved questions, Decision log |
| Implement simple Python scripts first so users can easily use QCC methods. | in scope | Goals, Recommended direction, Starter script model, Scope budget |
| Provide PPT slide templates to help users apply and present QCC methods. | in scope | Goals, Recommended direction, PPT template model, Scope budget |
| Make PowerPoint templates first-class rather than optional adoption assets. | in scope | Goals, Recommended direction, Template governance model, Scope budget |
| Provide Markdown documentation for each QCC method explaining how and when to use it. | in scope | Goals, Method documentation model, Scope budget |
| Avoid changing implementation files before direction is clear. | in scope | Non-goals, Readiness |
| Keep advanced methods such as DOE, QFD, Kano, and matrix data analysis available later. | deferred follow-up | Non-goals, Scope budget, Open questions |
| Support later user interfaces. | deferred follow-up | Options considered, Architecture impact, Scope budget |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Project identity and repository naming | core to this proposal | The proposal needs a stable working identity for downstream specs. |
| Vision and positioning alignment | same-slice dependency | Direction should fit the existing vision and positioning. |
| Canonical QCC Story stage model | core to this proposal | Stage awareness is central to the product. |
| Python package and public library API | core to this proposal | This is the recommended primary product foundation. |
| Method registry and method contracts | core to this proposal | Methods need stable inputs, outputs, validation, and stage mapping. |
| Markdown method documentation | first-slice candidate | Users need to know how and when to use QCC methods before adoption succeeds. |
| PowerPoint method templates | first-slice candidate | Templates are the primary teaching and presentation surface for many QCC users. |
| Template catalog | first-slice candidate | Template IDs, method IDs, docs, scripts, and generated assets need a reviewable traceability map. |
| Starter Python scripts | first-slice candidate | Scripts provide immediate usability without waiting for a web UI. |
| Synthetic datasets | first-slice candidate | Examples and tests need safe data. |
| Notebook examples | first-slice candidate | Notebooks support teaching, review, and adoption. |
| Core QCC methods | first-slice candidate | These create the primary user value and validate the architecture. |
| Chart generation engine | first-slice candidate | Chart generation is a central product differentiator and should be built early. |
| Markdown/HTML report-ready artifacts | first-slice candidate | Needed to reduce manual reconstruction, and feasible before complex office export. |
| Automated PPTX generation | separate implementation slice | Useful after chart-export and report-bundle contracts stabilize. |
| Batch/CLI generation | separate implementation slice | Important for reproducibility, but can follow the core library API and starter scripts. |
| Web API and UI | deferable follow-up | Useful later, but should not define method logic prematurely. |
| Advanced statistical and quality methods | deferable follow-up | Valuable after core correctness and architecture are proven. |
| Enterprise workflows, approvals, CAPA, EQMS | out of scope | Conflicts with focus and greatly increases product complexity. |
| Governance, contributor policy, and release policy | separate proposal | These require source-of-truth and governance decisions not adopted here. |

## Next artifacts

| Artifact | Purpose |
|---|---|
| PPT template specification | Define static QCC method templates, story deck structure, slide placeholders, template IDs, template catalog fields, required metadata, and future automation hooks. |
| Method documentation specification | Define Markdown method-guide structure, front matter, required sections, review checklist, and method-doc quality bar. |
| Example project pack | Define the first synthetic QCC story, datasets, templates, scripts, generated charts, evidence package, and report examples. |
| Chart generation specification | Define chart specs, renderers, metadata, warnings, export behavior, and reproducibility rules. |
| Starter scripts specification | Define script purposes, command-line inputs, expected outputs, project-folder assumptions, and smoke-test expectations. |
| Architecture design | Define package boundaries, data flow, method contracts, chart specs, evidence package, report object model, docs linkage, scripts, and templates. |
| Product specification | Define user-facing behavior, supported stages, method catalog, acceptance criteria, and first-slice adoption assets. |
| Method contracts specification | Define input/output contracts, validation rules, formulas, warnings, and summary outputs for each core method. |
| Testing strategy | Define fixture coverage, CI checks, numerical tolerances, chart-spec snapshots, documentation checks, script smoke tests, and notebook test rules. |
| Packaging and contributor setup | Define `pyproject.toml`, dependency policy, code style, CI checks, and release conventions. |

## Follow-on artifacts

None yet.

## Readiness

Formal proposal review approved the direction with no material findings.
The recorded review is `docs/changes/2026-07-07-create-qcc-toolkit/reviews/proposal-review-r1.md`.

This proposal is accepted as the durable proposal decision.
It is ready for downstream specification, architecture design, and test planning.
It is not implementation-ready by itself.
The next useful step is to author product specification and architecture design artifacts that convert this direction into concrete requirements, method contracts, chart behaviors, documentation templates, starter scripts, PPT templates, project-folder structure, and verification criteria.
