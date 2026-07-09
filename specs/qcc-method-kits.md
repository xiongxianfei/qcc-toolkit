# QCC Method Kits Spec

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-08-improve-qcc-method-templates.md`
- Proposal status: accepted
- Proposal review: `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/proposal-review-r1.md`

This spec turns the accepted PowerPoint-first, Python-assisted method-kit direction into observable behavior.
It does not define implementation milestones or approve code changes.

## Goal and context

The system MUST let users learn, apply, copy, present, and review QCC methods through method kits instead of shallow placeholder decks.

PowerPoint is the primary method-template workflow.
Markdown is the canonical written method reference.
Python assist is selective and used when PowerPoint cannot create, validate, scale, or reproduce the analysis reliably.

The first spec slice covers the method-kit standard, catalog behavior, evidence-level guidance, incoming-template handling, and the first improved method-kit set: Pareto Chart, 5W2H, Fishbone Diagram, 5 Whys, and Check Sheet.

## Glossary

| Term | Meaning |
|---|---|
| Method kit | A coordinated set of method guide, PowerPoint template, demo example, blank working slide or worksheet, review checklist, evidence/source guidance, catalog entry, and optional Python assist. |
| PowerPoint-native method | A method that ordinary users can teach, edit, and present reliably in PowerPoint. |
| Python-assisted method | A method whose calculation, validation, scale, repeated generation, or evidence needs exceed safe manual PowerPoint editing. |
| Method guide | Markdown document that governs method purpose, QCC stage fit, usage guidance, cautions, interpretation, and review checklist. |
| Template catalog | Machine-readable registry that maps method IDs to templates, guides, implementation modes, and optional Python assist. |
| Evidence level | Guidance level that tells users how much traceability is needed for draft, normal project, formal review, or high-risk evidence. |
| Incoming template | User-created or legacy PowerPoint template collected as source material but not yet accepted as an official method kit. |

## Examples first

Example E1: user opens a complete Pareto method kit
Given the Pareto Chart method kit is registered in the catalog
When a user opens the kit
Then the kit provides a Markdown guide, PowerPoint template, completed demo example, blank copyable project slide, sample data table, chart-editing instructions, interpretation patterns, common mistakes, facilitator checklist, Python assist decision guidance, evidence/source note guidance, and catalog entry.

Example E2: user edits a PowerPoint-native chart
Given a Pareto template with a small category-count table
When a user replaces categories and counts in PowerPoint
Then the template gives visible instructions to sort counts descending, verify cumulative values when used, preserve source/date notes, and avoid presenting demo data as project evidence.

Example E3: reviewer checks a completed method slide
Given a completed project slide from a method kit
When a facilitator reviews it
Then the kit provides checklist items for data/source visibility, QCC stage fit, correct method use, conclusion wording, next action, and Python assist triggers.

Example E4: Python assist is recommended for high-rigor evidence
Given a user has raw defect logs with many rows or needs competition-review evidence
When the user consults the method kit
Then the kit recommends Python assist or another validated reproducible path before finalizing the data-dependent conclusion.

Example E5: incoming template remains unofficial until reviewed
Given a user-created Fishbone template is placed in the incoming template area
When the system or reviewer catalogs official method kits
Then the incoming template is not treated as official until it passes method-kit review and is registered as an official catalog entry.

## Requirements

| ID | Requirement |
|---|---|
| R1 | Every official method kit MUST include a Markdown method guide. |
| R2 | Every official method kit MUST include a PowerPoint method template. |
| R3 | Every official method kit MUST include a completed demo example that is clearly labeled as demo content, not project evidence. |
| R4 | Every official method kit MUST include a blank copyable project slide or worksheet. |
| R5 | Every official method kit MUST include interpretation patterns for writing method-specific conclusions. |
| R6 | Every official method kit MUST include common mistakes and review risks. |
| R7 | Every official method kit MUST include a facilitator checklist with pass/fail or equivalent review criteria. |
| R8 | Every official method kit MUST include Python assist decision guidance. |
| R9 | Every official method kit MUST include evidence/source note guidance for source, date range, filters, assumptions, and calculation notes. |
| R10 | Every official method kit MUST have a template catalog entry. |
| R11 | Chart method kits MUST include an editable PowerPoint chart or a documented reason why the chart is not editable in PowerPoint. |
| R12 | Chart method kits MUST include a sample data table. |
| R13 | Chart method kits MUST include chart-editing instructions for categories, values, labels, formulas, and review checks. |
| R14 | Python-assisted method kits MUST include sample input data. |
| R15 | Python-assisted method kits MUST include a runnable assist script or notebook. |
| R16 | Python-assisted method kits MUST include a generated output example. |
| R17 | Python-assisted method kits MUST include a metadata or reproducibility note. |
| R18 | The template catalog MUST identify each method kit's method ID, method name, QCC stages, implementation mode, PowerPoint template path, Markdown guide path, and Python assist status. |
| R19 | The template catalog MUST reject official entries that reference missing template, guide, source-note, sample-data, script, notebook, or example-output paths. |
| R20 | The template catalog MUST reject duplicate official method-kit ownership for the same method unless the duplicate is explicitly classified as an alternate. |
| R21 | The template catalog MUST distinguish official method kits from incoming or source templates. |
| R22 | The first improved method-kit set MUST include Pareto Chart, 5W2H, Fishbone Diagram, 5 Whys, and Check Sheet. |
| R23 | The Pareto Chart kit MUST be classified as `powerpoint_native_chart` with optional Python assist. |
| R24 | 5W2H, 5 Whys, and Check Sheet MUST be classified as `template_native_worksheet` unless a downstream accepted spec changes the mode. |
| R25 | Fishbone Diagram MUST be classified as `template_native_diagram`. |
| R26 | The Pareto Chart kit MUST include purpose, stage fit, required data, edit instructions, realistic demo, blank slide, interpretation patterns, mistakes, review checklist, Python assist rule, and evidence/source notes. |
| R27 | The Pareto Chart kit MUST state that categories need to be non-overlapping and counts need a consistent data period. |
| R28 | PowerPoint-native chart kits MAY use embedded spreadsheet formulas only when formulas are simple, visible or documented, and covered by review guidance. |
| R29 | PowerPoint-native chart kits MUST recommend Python assist when formulas become complex, validation-heavy, repeated, raw-data-driven, or high-rigor. |
| R30 | The method-kit guidance MUST define evidence levels for teaching/draft, normal QCC project, competition or management review, and audit or high-risk evidence. |
| R31 | Level 1 teaching/draft use MUST allow PowerPoint template edits as sufficient evidence. |
| R32 | Level 2 normal QCC project use MUST allow PowerPoint-native charts when source data, date range, and checklist evidence are preserved. |
| R33 | Level 3 competition or management review use MUST require source data, calculation table, method checklist, and versioned template; Python assist MUST be recommended for raw-data or repeated chart methods. |
| R34 | Level 4 audit or high-risk evidence use MUST require a reproducible evidence package or another validated analysis path. |
| R35 | Incoming templates MUST be collected separately from official method kits. |
| R36 | Incoming templates MUST NOT be registered as official method kits until reviewed against the method-kit quality standard. |
| R37 | Official method kits MUST preserve QCC stage fit and method logic; generic template assets without QCC method context MUST NOT be accepted as official kits. |
| R38 | Official method kits MUST keep Markdown guidance and PowerPoint content consistent for method purpose, inputs, cautions, interpretation, review checklist, and Python assist triggers. |
| R39 | Method kits MUST NOT claim that manually edited PowerPoint charts are authoritative final evidence for reviewed, high-risk, or validation-heavy data-dependent conclusions. |
| R40 | The first improved method-kit slice MUST NOT require full automated PPTX generation. |
| R41 | Chart method kits MUST include a chart decision guide that identifies the decision supported, pattern to look for, safe conclusion, and overclaim to avoid. |
| R42 | Chart method kits SHOULD include a chart variant library for common presentation and analysis variants relevant to the method. |
| R43 | Chart method kits MUST include a chart quality checklist covering source, date range, filters, chart labels, calculation or formula checks, key finding, and next action. |
| R44 | The Pareto Chart kit MUST include Cumulative Pareto, Before/after Pareto comparison, and Focus annotation guidance. |
| R45 | Diagram method kits SHOULD include a diagram quality guide that defines the diagram decision, good structure, review risks, and overclaim to avoid. |
| R46 | The Fishbone Diagram kit MUST include an editable fishbone diagram surface with one effect statement, editable cause branches, cause text boxes, verification markers, and evidence/source fields. |
| R47 | The Fishbone Diagram kit MUST include cause wording guidance that distinguishes vague symptoms from testable cause statements. |
| R48 | The Fishbone Diagram kit MUST include a verification plan surface that records selected causes, verification method, owner, due date, and status. |
| R49 | The Fishbone Diagram kit MUST keep the editable diagram visually low-density by using short cause labels on the fishbone and moving detailed verification text to the verification plan. |
| R50 | The Fishbone Diagram kit SHOULD use a centered fishbone composition with clear spine, aligned branches, branch label capsules, and compact status badges. |
| R51 | The Fishbone Diagram kit MAY provide optional Python assist that generates a readable static SVG diagram when editable PowerPoint shapes are insufficient. |
| R52 | Python-generated Fishbone output MUST remain a presentation asset that preserves source/session notes and does not claim root-cause proof. |

## Inputs and outputs

| Surface | Inputs | Outputs |
|---|---|---|
| Method kit | Method guide, PowerPoint template, demo content, blank working slide, checklist, optional sample data, optional Python assist. | Reviewable official kit that users can learn from, copy, edit, present, and review. |
| Template catalog | Official kit entries, implementation modes, paths, Python assist status, incoming/source classification when applicable. | Validated registry of official kits and non-official source templates. |
| Incoming template intake | User-created or legacy PowerPoint file plus method, stage, owner, and source notes when known. | Source asset that remains unofficial until reviewed and migrated. |
| Evidence guidance | Method type, project risk level, data complexity, review context. | User-facing recommendation for PowerPoint-only, Python-assisted, or reproducible evidence workflow. |

## State and invariants

I1. Official method kits are the user-facing method-template unit.

I2. Markdown guides remain canonical for method explanation and review guidance.

I3. PowerPoint templates remain authoritative for teaching layout, working slides, visual examples, and copyable project-slide patterns.

I4. Python assist remains authoritative for complex formulas, validation, generated evidence, and reproducible data-dependent outputs when used.

I5. Incoming templates are source assets, not official kits.

I6. Demo examples and project evidence remain distinguishable.

I7. The absence of Python assist for a method does not make manually edited charts authoritative for high-rigor evidence.

## Error and boundary behavior

EB1. Catalog validation MUST fail for missing required official kit paths.

EB2. Catalog validation MUST fail when an official method kit lacks a required minimum content declaration or equivalent verifiable metadata.

EB3. Catalog validation MUST fail when a chart method kit has neither an editable chart declaration nor a documented non-editability reason.

EB4. Catalog validation MUST fail when a Python-assisted method kit lacks sample input, runnable assist path, generated output example, or reproducibility note.

EB5. Review checklists MUST identify demo data presented as project evidence as a failure condition.

EB6. Review checklists MUST identify missing data source or data period as a failure condition for data-dependent chart slides.

EB7. Incoming templates with unknown method, stage, owner, or unsupported formulas MUST remain source assets until reviewed.

## Compatibility and migration

This change is pre-1.0.
Method IDs, template IDs, catalog fields, implementation modes, guide paths, and template paths are compatibility surfaces once documented.

Existing first-slice templates can be migrated into official method kits by adding missing required content, source notes, checklist coverage, catalog metadata, and Python assist guidance.

The change MUST preserve existing first-slice Pareto evidence package behavior unless a downstream accepted spec explicitly changes Python evidence behavior.

Rollback is handled by keeping prior templates available or marking superseded templates clearly.

## Observability

O1. A reviewer MUST be able to identify every official method kit from the catalog.

O2. A reviewer MUST be able to tell whether a method kit is template-native, PowerPoint-native chart, Python-assisted, or Python-first analysis.

O3. A reviewer MUST be able to tell whether Python assist is unavailable, optional, recommended, or required for a method kit.

O4. A reviewer MUST be able to inspect whether required method-kit content exists.

O5. A reviewer MUST be able to distinguish official kits from incoming/source templates.

## Security and privacy

S1. Method-kit examples MUST use synthetic or approved non-sensitive sample data unless the repository explicitly documents permission to include a dataset.

S2. Incoming user-created templates MUST NOT be treated as safe to publish until reviewed for private data, real customer names, employee names, supplier names, patient data, credentials, hidden notes, and unsupported formulas.

S3. Python assist examples MUST NOT require secrets, credentials, telemetry, network services, or external data transfer.

S4. Evidence/source notes MUST guide users to record source context without embedding unnecessary raw private rows into public templates.

## Accessibility and UX

UX1. Method-kit PowerPoint content MUST be understandable without reading Python code first.

UX2. Method-kit Markdown guides MUST be readable as plain Markdown.

UX3. Blank copyable slides or worksheets MUST be visibly separate from completed demo examples.

UX4. Chart templates MUST provide enough visible guidance for users to avoid common editing mistakes.

UX5. Interpretation patterns MUST help users write conclusions without overstating what the method proves.

## Performance expectations

P1. Catalog validation for the first improved method-kit set SHOULD complete as part of the normal local validation suite without requiring external services.

P2. Optional Python assist for Pareto raw data SHOULD support the existing synthetic example scale and ordinary small QCC project datasets without requiring a server.

## Edge cases

EC1. A method has no chart.
The kit still needs method guide, PowerPoint template, demo, blank worksheet or slide, interpretation patterns, mistakes, checklist, Python assist decision, evidence/source note, and catalog entry.

EC2. A chart is PowerPoint-native but formula cells are overwritten.
The review checklist needs to flag overwritten formula cells or missing formula checks when formulas are used.

EC3. A template has a useful visual layout but weak method guidance.
It remains an incoming/source template until the method-kit standard is satisfied.

EC4. A method has both PowerPoint-native and Python-assisted paths.
The kit needs to explain when each path is acceptable and how evidence level changes the recommendation.

EC5. A completed slide is visually polished but lacks source/date notes.
For data-dependent methods, checklist review fails until source context is recorded.

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | This spec does not require Python for every method or chart. |
| NG2 | This spec does not implement full automated PPTX generation. |
| NG3 | This spec does not turn QCC Toolkit into a generic PowerPoint template marketplace. |
| NG4 | This spec does not add a web UI, dashboard, CAPA/EQMS workflow, desktop app, or document-management system. |
| NG5 | This spec does not add Control Chart, Process Capability, DOE, regression, or advanced statistical methods. |
| NG6 | This spec does not replace existing evidence package behavior for Pareto unless a downstream accepted spec changes that behavior. |

## Acceptance criteria

| ID | Acceptance criterion |
|---|---|
| AC1 | The first improved method-kit set is registered with method IDs, implementation modes, template paths, guide paths, and Python assist status. |
| AC2 | Each first-slice official method kit satisfies the minimum required content set. |
| AC3 | Pareto Chart kit includes chart-specific requirements: editable chart or reason, sample data table, chart-editing instructions, and Python assist rule. |
| AC4 | Official method kits include facilitator checklists that flag missing source/date notes, demo data used as project evidence, and unsafe method conclusions. |
| AC5 | Incoming/source templates are distinguishable from official method kits and are not treated as official catalog entries before review. |
| AC6 | Evidence-level guidance exists and distinguishes draft, normal project, formal review, and high-risk evidence expectations. |
| AC7 | Catalog validation or equivalent documented checks can detect missing paths, duplicate official ownership, and missing required metadata. |
| AC8 | No full PPTX automation, web UI, dashboard, enterprise quality workflow, or advanced statistical method is required by this slice. |
| AC9 | Pareto Chart kit exposes chart decision, variant, and quality-check surfaces in the guide, source notes, and PowerPoint template. |

## Open questions

None.

## Next artifacts

| Artifact | Purpose |
|---|---|
| Spec review | Validate the behavior contract before architecture and planning. |
| Architecture assessment and architecture artifacts if required | Decide and record durable boundaries for method kits, catalog, incoming templates, and optional Python assist. |
| Execution plan | Sequence the first implementation slice after approved spec and architecture decisions. |
| Test specification | Map requirements and edge cases to concrete tests or proof before implementation. |

## Follow-on artifacts

| Artifact | Status |
|---|---|
| `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md` | Approved spec review with no material findings. |

## Readiness

Approved and ready for architecture assessment.

This spec is not plan-ready by itself and is not implementation-ready.
