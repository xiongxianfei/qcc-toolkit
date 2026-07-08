# Proposal: Improve QCC Method Templates

## Status

accepted

This proposal records a recommended direction for improving QCC Toolkit method templates.
It is an accepted decision, but it is not a specification, an implementation plan, or verification evidence.

This proposal responds to user feedback that the generated QCC method template is too simple and not useful enough.
It also records the product judgment that PowerPoint should be the primary user workflow for most QCC method templates, while Python should be used when PowerPoint is weak, unsafe, hard to validate, or unable to produce the required analysis reliably.

## Problem

The current generated QCC method template is too shallow to be useful as a practical QCC working asset.
It contains method identifiers, basic placeholders, a small editable chart or data table, a demo label, and project-evidence placeholders, but it does not yet teach the method deeply enough or help users apply it with confidence.

A useful QCC method template should help users understand the method, decide when to use it, avoid misuse, edit the chart or worksheet correctly, interpret the output, write a slide conclusion, and know when Python support is worth using.

The project also needs to avoid over-weighting Python as the first user-facing surface for every method.
Many QCC users are already comfortable with PowerPoint templates and can create many common QCC charts directly in PowerPoint by changing the data.
For those users, requiring Python for simple PowerPoint-native charts adds friction without enough benefit.

The project needs a revised improvement direction that treats method templates as first-class user-facing assets while preserving Python as a rigorous assist layer for cases that need calculation, validation, reproducibility, or scale.

## Goals

| ID | Goal |
|---|---|
| G1 | Improve QCC method templates so they are practical teaching, working, and presentation assets, not simple placeholder decks. |
| G2 | Make PowerPoint the default user-facing surface for QCC methods that can be taught, edited, and presented reliably in PowerPoint. |
| G3 | Use Python only for methods or situations where PowerPoint is insufficient: complex calculations, validation, large datasets, repeatable generation, reproducibility, or evidence packaging. |
| G4 | Keep Markdown method guides as the canonical written method reference so template content can be reviewed, versioned, and kept consistent. |
| G5 | Define a repeatable method-kit structure for every QCC method: PowerPoint template, Markdown guide, sample data where applicable, optional Python assist, and review checklist. |
| G6 | Improve each PowerPoint template with practical content: method purpose, QCC stage fit, when to use, when not to use, required data, editing steps, demo example, blank copyable slide, interpretation patterns, common mistakes, and facilitator checklist. |
| G7 | Classify QCC methods by implementation mode so the project does not over-automate qualitative or simple methods. |
| G8 | Preserve evidence traceability for final data-dependent conclusions without forcing Python into every draft, training, or simple project use case. |
| G9 | Defer full automated PPTX generation until template structure, placeholders, evidence packages, and method contracts stabilize. |
| G10 | Keep the project focused on QCC method application and avoid generic dashboard, enterprise quality-system, and broad document-editor scope. |

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not require Python for every QCC method or every chart. |
| NG2 | Do not treat a simple placeholder deck as an acceptable QCC method template. |
| NG3 | Do not build full automated PowerPoint generation as the first improvement. |
| NG4 | Do not replace users' existing PowerPoint-based QCC workflow where it is already effective. |
| NG5 | Do not make manually edited PowerPoint charts the only authoritative record for high-risk, reviewed, or data-dependent QCC conclusions. |
| NG6 | Do not turn QCC Toolkit into a generic PowerPoint template marketplace unrelated to QCC stage workflow and method logic. |
| NG7 | Do not build a no-code desktop application, web dashboard, CAPA/EQMS platform, or broad document-management system as part of this proposal. |
| NG8 | Do not implement advanced statistical methods such as DOE, regression, or process capability before the core method-kit structure is proven. |
| NG9 | Do not define ticket-level implementation milestones in this proposal. Those belong in downstream specifications or plans. |

## Vision fit

proposes a vision revision

This proposal preserves the current vision's evidence-quality principles, QCC-stage focus, explainability, reproducibility goals, and source-of-truth split.
PowerPoint still teaches and presents, Markdown still governs method knowledge, and Python still generates traceable QCC evidence.

However, it revises the primary user-facing workflow for method-template work from Python-first or Python-centered to PowerPoint-first, Python-assisted.
For QCC method-template work, PowerPoint method kits become the primary teaching, working, and presentation workflow.
Python is used selectively when PowerPoint cannot create, validate, scale, or reproduce the analysis reliably.

Therefore, `VISION.md` and the create-toolkit proposal should be amended if they imply that Python is the first user surface for every QCC method.

## Context

QCC Toolkit is positioned around QCC stage workflow, quality-method selection, chart generation, interpretation, and report-ready outputs.
The existing create-toolkit proposal made PowerPoint method templates first-class user-facing assets around a Python evidence core.
This improvement proposal revises that first-slice direction by making PowerPoint method templates the primary user-facing workflow for method-template work.

The latest user feedback changes the immediate priority.
The generated Pareto method template is too simple and not useful enough.
Users already have or expect PowerPoint templates that explain QCC quality methods, provide demo examples, and allow users to copy charts into their own QCC materials by modifying data.
For many common QCC methods, that PowerPoint-native workflow is more convenient than a Python-first workflow.

The current Pareto template demonstrates the gap.
It identifies the method and QCC stage, includes placeholder names, provides a small editable data table, labels a demo example as not project evidence, and includes a project evidence checklist.
That is useful as a structural proof of concept, but it is not yet a complete method kit.
It lacks enough user-facing instruction, edit guidance, interpretation help, common-mistake warnings, and facilitator review logic.

This proposal therefore changes the improvement emphasis from:

```text
Python evidence core with PPT templates as supporting adoption assets.
```

to:

```text
PowerPoint-first QCC method kits with Python assist when needed.
```

## Options Considered

| Option | Name | Summary | Benefits | Costs / risks | Decision |
|---|---|---|---|---|---|
| O1 | Keep Python-first improvement emphasis | Improve the Python core first and treat PowerPoint templates as adoption assets. | Strong reproducibility and testing story; clean architecture for advanced analysis. | Too much friction for simple QCC templates; may produce technically correct but practically underused assets. | Rejected for this improvement. |
| O2 | Template-only product | Build only PowerPoint templates and let users manually edit everything. | Lowest user friction; matches current PowerPoint behavior. | Weak validation, weak reproducibility, hard to test formulas, and risky for reviewed data-dependent conclusions. | Rejected as a complete product direction. |
| O3 | PowerPoint-first, Python-assisted method kits | Make high-quality PowerPoint method kits the main user workflow; add Markdown method guides and optional Python assist where PowerPoint is insufficient. | Best fit with user workflow; keeps templates useful; preserves evidence rigor when needed. | Requires clear rules for when Python is recommended and how templates stay aligned with docs. | Recommended direction. |
| O4 | Full automated PPTX generation first | Build code that fills slide placeholders and generates decks automatically. | Attractive for batch reporting and standardized organizations. | Brittle too early; template structures are not mature; may distract from content quality. | Deferred follow-up. |
| O5 | Web application first | Build a UI around method selection, chart generation, and slide export. | Easier for non-technical users eventually. | Higher delivery risk; premature product decisions; does not solve template quality first. | Deferred follow-up. |

## Recommended Direction

Create a new improvement direction called:

```text
PowerPoint-first, Python-assisted QCC method kits.
```

Each QCC method should be delivered as a method kit, not only as a simple PowerPoint file.
A method kit should contain the teaching content, working template, reusable slide, example data, interpretation guidance, and optional Python assist needed for that method.

Recommended method-kit shape:

```text
method-kits/<method-id>/
  README.md
  <method-id>.md
  <method-id>-template.pptx
  sample-data.xlsx or sample-data.csv, if applicable
  examples/
  python-assist/, only if useful
  review-checklist.md
```

The primary workflow should be:

```text
User opens the PowerPoint method template.
User learns the method and reviews the demo example.
User edits the worksheet, diagram, or chart directly in PowerPoint when the method is simple.
User copies the blank project slide into their own QCC material.
User uses Python assist only if the analysis is too complex, too large, too repetitive, or needs stronger traceability.
```

The project should use this operating model:

| Surface | Role | Default authority |
|---|---|---|
| PowerPoint template | Main teaching, working, and presentation surface. | Authoritative for slide layout, visual example, and copyable working pattern. |
| Markdown guide | Method explanation and review standard. | Authoritative for method purpose, usage guidance, cautions, and review checklist. |
| Python assist | Optional evidence engine. | Authoritative for complex formulas, validation, generated evidence, and reproducible data-dependent outputs. |
| Evidence package | Optional final evidence record. | Authoritative for reviewed, high-rigor, or reproducible project evidence. |

### Method Template Quality Standard

A useful PowerPoint method template should follow a consistent structure.
The exact number of slides may differ by method, but each kit should cover the same user questions.

Every method kit should contain this minimum content set:

| Required item | Purpose |
|---|---|
| Markdown method guide | Provides the canonical written method reference. |
| PowerPoint method template | Provides the primary teaching, working, and presentation asset. |
| Completed demo example | Shows a realistic completed use case with finding and next action. |
| Blank copyable project slide or worksheet | Gives users a clean working surface for their own QCC deck. |
| Interpretation patterns | Helps users write safe, method-specific conclusions. |
| Common mistakes | Warns against frequent errors and review risks. |
| Facilitator checklist | Provides pass/fail review criteria. |
| Python assist decision guidance | States when PowerPoint is enough and when Python is recommended. |
| Evidence/source note guidance | Explains how to record source, date range, filters, assumptions, and calculation notes. |
| Catalog entry | Registers method ID, stage fit, implementation mode, template path, guide path, and optional Python assist. |

Chart methods should also contain:

| Required item | Purpose |
|---|---|
| Editable PowerPoint chart or documented reason why not | Keeps simple chart methods usable in PowerPoint. |
| Sample data table | Shows the expected data shape and formulas when applicable. |
| Chart-editing instructions | Helps users update categories, values, labels, formulas, and review checks safely. |

Python-assisted methods should also contain:

| Required item | Purpose |
|---|---|
| Sample input data | Gives users a known input shape for the assist path. |
| Runnable assist script or notebook | Provides the optional calculation, validation, or generation path. |
| Generated output example | Shows the expected chart, table, caption, or evidence output. |
| Metadata/reproducibility note | Records how source data, parameters, method version, and output can be traced. |

Recommended slide/content model:

| Section | Purpose |
|---|---|
| Method overview | Explain what the method is and what question it answers. |
| QCC stage fit | Show where the method fits in the QCC story. |
| When to use | Explain suitable problem types and data conditions. |
| When not to use | Prevent common misuse and false conclusions. |
| Required inputs | Show the data, categories, worksheet fields, or project context required. |
| Step-by-step use | Explain exactly how to use the template. |
| PowerPoint edit instructions | Explain how to edit chart data, diagram nodes, tables, labels, and formulas safely. |
| Completed demo example | Show a realistic example with a clear finding and next action. |
| Blank copyable slide | Give users a clean project slide they can copy into their own QCC deck. |
| Interpretation patterns | Provide sentence templates for common conclusions. |
| Common mistakes | Warn against errors that reviewers often find. |
| Facilitator checklist | Provide a pass/fail checklist for method review. |
| Python assist decision | Explain when PowerPoint is enough and when Python assist is recommended. |
| Evidence note | Explain how to record source data, date range, filters, and calculation notes for final evidence. |

For the Pareto Chart method, the improved template should include at least:

| Slide/content item | Recommended content |
|---|---|
| Purpose | Pareto Chart identifies the vital few categories contributing most to a problem. |
| Stage fit | Understand Current Condition and Analyze Causes. |
| Required data | Category and count, with non-overlapping categories and a consistent period. |
| Edit instructions | Right-click chart, edit data, replace categories/counts, sort descending, verify cumulative line if used. |
| Demo example | Realistic defect dataset with top category, top-three share, and next method. |
| Blank slide | Title, chart, data period, source, key finding, next action, prepared-by/date. |
| Interpretation patterns | Largest contributor, vital few, focus decision, next method, caution wording. |
| Mistakes | Unsorted bars, mixed time periods, overlapping categories, missing counts, demo data presented as project evidence. |
| Review checklist | Data period shown, source shown, categories clear, counts sorted, conclusion written, next method identified. |
| Python assist rule | Use Python for raw logs, large data, repeated generation, reproducibility, or final reviewed evidence. |

### Python Assist Policy

Python should be optional by default and recommended only when it adds clear value.

For QCC method-template work, the product positioning is PowerPoint-first, Python-assisted.
PowerPoint is the primary teaching, working, and presentation surface.
Python is used selectively when PowerPoint cannot create, validate, scale, or reproduce the analysis reliably.
Markdown remains the canonical written method reference.

For the broader project, the positioning remains:

```text
PowerPoint teaches and presents.
Markdown governs method knowledge.
Python assists with rigorous analysis and evidence.
```

Use PowerPoint directly when:

| Condition | Example |
|---|---|
| The method is qualitative or visual. | 5W2H, Fishbone, 5 Whys, SIPOC, Poka-Yoke. |
| The chart is simple and the data is small. | Pareto with a few categories, simple histogram, simple line chart. |
| The output is for training, workshop use, or draft QCC discussion. | Template demo, copied working slide, early team review. |
| Users need fast manual adjustment and presentation control. | Slide layout, annotations, before/after photos, team comments. |

Use Python assist when:

| Condition | Example |
|---|---|
| The calculation is difficult or error-prone in PowerPoint. | Control limits, process capability, regression, DOE. |
| The source data is large or raw. | Thousands of defect records, transaction logs, inspection records. |
| The analysis needs validation. | Missing values, invalid counts, wrong subgroup size, inconsistent periods. |
| The chart needs to be regenerated repeatedly. | Weekly review, many departments, many product lines. |
| The output is final reviewed evidence. | Competition deck, management review, audit-related evidence. |
| Traceability is important. | Need source file, filters, parameters, method version, and generated caption. |

This policy changes the previous assumption that Python scripts are the first practical execution surface for all data-dependent methods.
The new policy is more selective:

```text
PowerPoint first.
Python assist when PowerPoint cannot create, validate, scale, or reproduce the analysis reliably.
```

### Evidence Level Policy

Final competition or audit materials should require reproducible evidence for data-dependent conclusions.
Python is one recommended way to create that evidence, but not the only acceptable way for simple PowerPoint-native charts.

Recommended evidence levels:

| Evidence level | Use case | Requirement |
|---|---|---|
| Level 1: Teaching / draft | Training, workshop, early discussion. | PowerPoint template edits are acceptable. |
| Level 2: Normal QCC project | Internal project presentation. | PowerPoint-native chart is acceptable if source data, date range, and review checklist are preserved. |
| Level 3: Competition / management review | Formal review or award presentation. | Require source data, calculation table, method checklist, and versioned template. Python is recommended for chart methods with raw data or repeated analysis. |
| Level 4: Audit / high-risk evidence | Audit-related, safety-critical, regulatory, or customer-impact evidence. | Require a reproducible evidence package. Python or another validated analysis path should generate or verify the result. |

### Method Implementation Classification

Each QCC method should be classified by its first recommended implementation mode.

| Implementation mode | Description | Examples | Python role |
|---|---|---|---|
| Template-native worksheet | The method is mostly structured thinking, explanation, or qualitative analysis. | 5W2H, 5 Whys, Poka-Yoke, PDPC. | None or optional export only. |
| Template-native diagram | The method is visual and requires flexible editing. | Fishbone, SIPOC, Flowchart, Tree Diagram, Affinity Diagram. | None initially. |
| PowerPoint-native chart | The chart can be created safely with embedded PowerPoint chart data for normal use. | Pareto, simple Histogram, simple Scatter, simple Trend Chart. | Optional for large data or final evidence. |
| Python-assisted chart | The method can be shown in PowerPoint but calculation or validation is risky manually. | Control Chart, Process Capability, before/after statistical verification. | Recommended. |
| Python-first analysis | The method requires structured calculation, modeling, or multi-factor analysis. | DOE, regression, advanced capability, complex FMEA ranking. | Primary analysis path. |

Recommended first-slice method modes:

| Method | First mode | Rationale |
|---|---|---|
| 5W2H | Template-native worksheet | Easy to teach and edit in slides. |
| Check Sheet | Template-native worksheet | PowerPoint can show the format; Excel or CSV may hold larger data. |
| Pareto Chart | PowerPoint-native chart with optional Python assist | Small category counts are easy in PowerPoint; raw logs benefit from Python. |
| Fishbone Diagram | Template-native diagram | Flexible visual editing matters more than automation. |
| 5 Whys | Template-native worksheet | Best as a simple guided table. |
| SIPOC | Template-native diagram/table | Usually a structured editable slide. |
| Histogram | PowerPoint-native chart with optional Python assist | Simple data can be charted manually; large numeric data benefits from Python. |
| Scatter Diagram | PowerPoint-native chart with optional Python assist | Simple scatter is PowerPoint-friendly; correlation/regression benefits from Python. |
| Control Chart | Python-assisted chart | Control limits and rule interpretation are too error-prone manually. |
| Process Capability | Python-first analysis | Requires assumptions, stability checks, and formula correctness. |
| DOE | Python-first analysis | Too advanced for manual slide templates as the analysis source. |

### Existing Template Incorporation

Existing user-created PowerPoint templates should be treated as source assets, not automatically accepted product assets.
They can preserve practical QCC knowledge, but they should pass method-kit review before becoming official.

Recommended incorporation process:

| Step | Action |
|---|---|
| 1 | Collect existing templates into a `templates/incoming/` area. |
| 2 | Identify method, QCC stage, target user, and template owner. |
| 3 | Review against the method-kit quality standard. |
| 4 | Keep useful layouts, examples, chart structures, and wording. |
| 5 | Remove unclear placeholders, unsupported formulas, stale examples, and undocumented assumptions. |
| 6 | Add missing method guidance, interpretation patterns, mistakes, and facilitator checklist. |
| 7 | Register the cleaned version in the template catalog. |
| 8 | Mark the original as source reference, not the official kit. |

Recommended repository distinction:

```text
templates/incoming/        # user-created or legacy templates, not yet approved
method-kits/<method-id>/   # reviewed official method kits
templates/catalog.yml      # official template registry
```

## Expected Behavior Changes

| ID | Expected behavior change |
|---|---|
| B1 | Users can open a QCC method template and understand the method without reading Python code first. |
| B2 | Users can copy a blank working slide from a method kit into their own QCC deck. |
| B3 | Users can edit simple charts and worksheets directly in PowerPoint when the method is PowerPoint-native. |
| B4 | Users receive clear guidance on when PowerPoint is enough and when Python assist is recommended. |
| B5 | Users can use Markdown method guides as the canonical written reference for method purpose, usage, cautions, and review. |
| B6 | Reviewers can use facilitator checklists to judge whether a completed method slide is acceptable. |
| B7 | Final high-rigor charts can still be linked to source data, method parameters, warnings, and evidence metadata where needed. |
| B8 | Python scripts become optional assist tools instead of mandatory paths for every method. |
| B9 | Future automated PPTX generation remains possible because templates can still use stable IDs and placeholders. |
| B10 | The project avoids producing simple placeholder decks that look systematic but do not help users apply QCC methods. |

## Architecture Impact

The architecture should be adjusted from a Python-centered asset pipeline to a method-kit-centered repository model.
The Python package remains useful, but it is no longer the primary user workflow for every method.

Recommended repository boundaries:

| Area | Responsibility |
|---|---|
| `method-kits/<method-id>/` | Complete method kit containing template, method guide, examples, review checklist, and optional Python assist. |
| `templates/ppt/methods/` | PowerPoint method templates, versioned and cataloged. |
| `docs/methods/` | Canonical Markdown guides for method explanation and review. |
| `docs/template-standards/` | Standards for slide structure, visual style, editing instructions, and facilitator checks. |
| `qcc_toolkit/assist/` | Optional Python assist functions for complex, validated, or repeatable analyses. |
| `qcc_toolkit/evidence/` | Evidence-package models for final reviewed outputs. |
| `examples/` | Complete example QCC projects showing PowerPoint-first and Python-assisted workflows. |
| `templates/catalog.yml` | Mapping of method IDs, template files, Markdown guides, implementation mode, and optional Python assist. |

Recommended conceptual flow for simple methods:

```text
Markdown method guide
  -> PowerPoint method template
    -> User edits worksheet/chart directly
      -> User copies completed slide into QCC deck
        -> Optional evidence note records source/date/context
```

Recommended conceptual flow for Python-assisted methods:

```text
Markdown method guide
  -> PowerPoint method template
    -> User prepares source data
      -> Python assist validates and calculates
        -> Generated chart/table/caption/metadata
          -> User inserts output into QCC slide
            -> Evidence package preserved for review
```

The method catalog should record which path is recommended for each method.

Example catalog fields:

```yaml
method_id: pareto_chart
method_name: Pareto Chart
qcc_stages:
  - understand_current_condition
  - analyze_causes
implementation_mode: powerpoint_native_chart
ppt_template: templates/ppt/methods/pareto-chart-template.pptx
markdown_guide: docs/methods/pareto-chart.md
python_assist: optional
python_assist_reason:
  - large_raw_data
  - reproducible_final_evidence
  - repeated_generation
```

## Testing and Verification Strategy

Testing should focus on whether method kits are useful, internally consistent, and safe to apply.
The verification strategy should test both content quality and analytical correctness where Python is involved.

| Test area | Strategy |
|---|---|
| Template completeness checks | Confirm each method kit includes required sections: overview, stage fit, use/not-use guidance, inputs, procedure, demo, blank slide, interpretation, mistakes, checklist, and Python assist decision. |
| Template usability review | Manually review whether a QCC user can complete the method using the template without additional explanation. |
| Chart editability checks | Confirm PowerPoint-native chart templates contain editable chart data, not only static screenshots. |
| Demo-data labeling checks | Confirm demo charts are clearly labeled as demo examples and not project evidence. |
| Markdown-template consistency checks | Confirm each PowerPoint template maps to a Markdown guide and the key guidance does not contradict it. |
| Facilitator checklist review | Confirm each method has a practical review checklist that can be used in training or project review. |
| Python assist tests | For Python-assisted methods, test formulas, validation, generated captions, and metadata using known fixtures. |
| Reproducibility tests | For evidence-generating Python assist, confirm the same inputs and parameters regenerate the same calculated outputs. |
| Template catalog checks | Confirm every method kit is registered with method ID, stage, implementation mode, template path, guide path, and optional Python assist path. |
| Visual quality review | Review slide readability, chart clarity, typography, placeholder wording, and practical copyability. |

Verification evidence should include a template audit report, sample completed method kits, revised Pareto template, checklist results, and passing tests for any Python assist included in the slice.

## Rollout and Rollback

Rollout should begin with a small set of improved method kits rather than the full QCC method library.
The first improvement slice should prove the quality bar before scaling to every method.

Recommended first kit set:

| Method kit | Reason |
|---|---|
| Pareto Chart | Best test of PowerPoint-native chart plus optional Python assist. |
| 5W2H | Best test of structured worksheet template. |
| Fishbone Diagram | Best test of editable visual root-cause template. |
| 5 Whys | Best test of guided logic-chain template. |
| Check Sheet | Best bridge between data collection and later charting. |

Rollout posture:

| Area | Approach |
|---|---|
| Template release | Release templates as draft method kits until reviewed with sample QCC users. |
| Python assist | Include only optional assist for Pareto raw-data generation if useful; defer broader Python assist. |
| Catalog | Register each method kit in a template catalog from the first slice. |
| Compatibility | Version templates and guides so users can identify which kit version they used. |
| Evidence policy | Treat final high-rigor evidence as reproducible where Python assist is used, but allow simple PowerPoint-native outputs for ordinary draft/project use. |

Rollback should be handled by keeping prior templates available, versioning method kits, and marking superseded templates clearly.
If a revised template proves less usable than the earlier version, revert the template while preserving the Markdown guide and lessons learned for the next revision.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| PowerPoint templates remain too shallow | Users continue to see templates as useless placeholders. | Use the method-kit quality standard and facilitator checklist before calling a template complete. |
| Python is overused | Users face unnecessary friction for simple QCC work. | Apply the Python assist policy and method implementation classification. |
| Python is underused | Final evidence may become hard to validate or reproduce. | Recommend Python assist for complex, high-risk, large, repeated, or reviewed data-dependent analyses. |
| Markdown and PowerPoint drift apart | Users receive inconsistent method guidance. | Treat Markdown as canonical method text and review templates against it. |
| Manual chart edits create wrong conclusions | Users may present visually polished but analytically incorrect charts. | Add chart-edit instructions, review checklists, and Python assist triggers for risky cases. |
| Template catalog becomes stale | Users cannot find the correct template or method guide. | Add catalog checks and require every method kit to declare method ID, stage, mode, and paths. |
| Full PPT automation is attempted too early | Development effort shifts away from template usefulness. | Defer automated PPTX generation until method kits, placeholders, and evidence package formats stabilize. |
| Project loses QCC focus | The repository becomes a generic template library. | Keep QCC stage fit and method logic required in every method kit. |
| Template visual design dominates method quality | Slides look good but do not teach or guide analysis. | Verify method completeness, interpretation guidance, and review checklists before visual polish. |
| Improvement direction appears to conflict with existing vision wording | Confusion about whether the project is Python-first or PowerPoint-first. | Treat this proposal as a vision refinement: PowerPoint-first for method-template work, Markdown as method authority, and Python-assisted for rigorous analysis and evidence. |

## Resolved Questions

| ID | Question | Decision |
|---|---|---|
| RQ1 | Should the project adopt "PowerPoint-first, Python-assisted" as the primary positioning phrase for template work? | Yes. Use it for method-template work. Keep the broader evidence-quality framing for the overall toolkit. |
| RQ2 | Should the existing create-project proposal be amended or superseded? | Amend or supersede the create-project proposal before downstream specification if reviewers accept this direction. Preserve evidence-quality principles, but revise the first-slice user workflow. |
| RQ3 | What is the exact minimum slide set required for every method kit? | Define a minimum content set rather than a fixed slide count: overview, stage fit, use/not-use, inputs, steps, editable working slide, demo, blank copy slide, interpretation patterns, mistakes, checklist, Python assist decision, and evidence note. |
| RQ4 | How should existing user-created PowerPoint templates be incorporated? | Treat them as source examples. Migrate them into official method kits only after content, formula, usability, and review-checklist assessment. |
| RQ5 | Which methods need Python assist in the first improvement slice? | Include optional Pareto raw-data assist only if useful. Defer Control Chart, Process Capability, DOE, regression, and advanced analysis until the method-kit standard is proven. |
| RQ6 | Should template charts use embedded PowerPoint formulas? | Yes for simple, transparent, documented formulas. Use Python assist for complex formulas, validation-heavy charts, or high-rigor evidence. |
| RQ7 | Should final competition or audit materials require Python-generated evidence? | Require reproducible evidence for data-dependent conclusions. Python is recommended or required depending on risk, complexity, and review level, but simple PowerPoint-native charts may be acceptable with source data and checklist evidence. |

## Downstream Specification Details

| ID | Detail | Owner artifact |
|---|---|---|
| DQ1 | Exact slide layout, typography, placeholder naming, and chart style. | PPT method-kit specification |
| DQ2 | Exact method-guide front matter and section wording. | Method documentation specification |
| DQ3 | Exact template catalog schema. | Template catalog specification |
| DQ4 | Evidence-level policy wording for competition, audit, and ordinary project use. | Evidence policy specification |
| DQ5 | Exact formula documentation rules for embedded PowerPoint charts. | PPT chart standard |

## Decision Log

| Date | Decision | Reason | Alternatives rejected or deferred |
|---|---|---|---|
| 2026-07-08 | Propose improving method templates through PowerPoint-first, Python-assisted method kits. | User feedback indicates PowerPoint templates are the main practical workflow, and Python should be used selectively. | Python-first improvement for all methods; template-only product. |
| 2026-07-08 | Treat method templates as method kits rather than simple PPT files. | A useful QCC method asset needs teaching, working, interpretation, review, and optional evidence support. | Placeholder decks with template variables only. |
| 2026-07-08 | Use Python when PowerPoint cannot create, validate, scale, or reproduce the analysis reliably. | Reduces user friction while preserving rigor where needed. | Mandatory Python scripts for every method; no Python assist at all. |
| 2026-07-08 | Keep Markdown guides as canonical method documentation. | Markdown is easier to review, version, diff, and keep consistent than slide-only text. | PPT-only method guidance. |
| 2026-07-08 | Defer full automated PPTX generation. | Template content quality and placeholders need to stabilize first. | Automated deck generation as the first improvement. |
| 2026-07-08 | Use Pareto Chart, 5W2H, Fishbone, 5 Whys, and Check Sheet as the first improved method-kit set. | These cover chart, worksheet, diagram, logic-chain, and data-collection template types. | Improving every method at once. |
| 2026-07-08 | Treat this proposal as a vision refinement for method-template work. | Proposal review found that the PowerPoint-first workflow changes product-surface priority even while preserving evidence-quality principles. | Treating the change as only fitting current vision. |
| 2026-07-08 | Resolve the proposal questions into direction-level decisions. | Proposal review found the questions had clear recommended answers and should not block specification. | Leaving all seven items as open questions. |

## Initial Intent Preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Improve the generated QCC method templates because the current one is too simple and useless. | in scope | Problem, Goals, Recommended Direction, Method Template Quality Standard |
| Use Python only when PowerPoint cannot create the needed charts or analysis. | in scope | Goals, Python Assist Policy, Decision Log |
| Keep PowerPoint templates as the primary practical user workflow. | in scope | Recommended Direction, Architecture Impact, Expected Behavior Changes |
| Preserve best practices for evidence and method quality. | in scope | Testing and Verification Strategy, Risks and Mitigations |
| Keep Markdown documentation for method knowledge. | in scope | Goals, Recommended Direction, Architecture Impact |
| Avoid overbuilding full automation too early. | in scope | Non-goals, Rollout and Rollback, Decision Log |
| Preserve advanced analysis for later. | deferred follow-up | Non-goals, Method Implementation Classification, Resolved Questions |
| Update the broader project direction if needed. | in scope | Vision fit, Resolved Questions, Next Artifacts |

## Scope Budget

| Work item | Treatment | Reason |
|---|---|---|
| Positioning refinement from Python-first to PowerPoint-first, Python-assisted for method templates | core to this proposal | The improvement changes the user-facing priority and needs explicit direction. |
| Method-kit quality standard | core to this proposal | This defines what "useful template" means. |
| Minimum method-kit content set | core to this proposal | Prevents shallow template generation from recurring. |
| Evidence-level policy | core to this proposal | Avoids the false choice between always requiring Python and always accepting manual PowerPoint. |
| Existing template incorporation process | core to this proposal | Preserves practical user-created assets while protecting quality. |
| PowerPoint template improvements | first-slice candidate | The main user value is better templates. |
| Markdown method guide alignment | same-slice dependency | Template content needs canonical method guidance. |
| Template catalog | first-slice candidate | Method kits need traceability across PPT, Markdown, and optional Python assist. |
| Pareto Chart improved method kit | first-slice candidate | Best concrete example for chart template improvement. |
| 5W2H, Fishbone, 5 Whys, Check Sheet kits | first-slice candidate | Proves different template types beyond charts. |
| Optional Python assist for Pareto raw data | separate implementation slice | Useful only if PowerPoint-native Pareto is insufficient for raw logs or final evidence. |
| Control Chart and Process Capability Python assist | deferable follow-up | More rigorous calculations should follow after template standards stabilize. |
| Full automated PPTX generation | deferable follow-up | Useful later, but too brittle before templates stabilize. |
| Web UI or dashboard | out of scope | Not needed to improve method-template usefulness. |
| Enterprise quality workflows | out of scope | Outside QCC method-template improvement. |

## Next Artifacts

| Artifact | Purpose |
|---|---|
| Proposal review closeout | Confirm the review amendments are accepted and the proposal can move downstream. |
| Vision or create-proposal amendment | Align the controlling product direction with PowerPoint-first, Python-assisted method-template work. |
| PPT method-kit specification | Define required slide/content sections, style rules, placeholder rules, demo labeling, and review checklist requirements. |
| Method documentation specification | Define Markdown method guide structure and how it maps to PowerPoint templates. |
| Template catalog specification | Define method IDs, template IDs, implementation modes, template paths, guide paths, and optional Python assist fields. |
| Improved Pareto Chart method kit | Create the first high-quality template kit using the new standard. |
| Template review checklist | Provide a reusable checklist for approving each method kit. |
| Python assist policy document | Define when Python is recommended, optional, or unnecessary by method type. |

## Follow-on Artifacts

| Artifact | Status |
|---|---|
| `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/proposal-review-r1.md` | Approved proposal review with no material findings. |
| `docs/changes/2026-07-08-improve-qcc-method-templates/review-log.md` | Review log and proposal status settlement. |

## Readiness

Accepted and ready for the next upstream alignment artifact.

This proposal is not spec-ready by itself and is not implementation-ready.
The next useful step is to amend the controlling vision or create-proposal wording, then draft a PPT method-kit specification and improve the Pareto Chart method kit against that standard.
