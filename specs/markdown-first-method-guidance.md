# Markdown-First Method Guidance Spec

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-09-markdown-first-method-guides.md`
- Proposal status: accepted
- Proposal review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/proposal-review-r1.md`

This spec turns the accepted Markdown-first QCC method-guidance direction into observable behavior.
It does not define implementation milestones or approve code changes.

## Goal and context

QCC Toolkit MUST make Markdown method guides the primary user-facing surface for QCC method education, application, chart-quality guidance, interpretation, and review.

The system MUST use image-assisted demonstration only for conceptual teaching.
Generated images MUST NOT be treated as final quantitative evidence charts.

The system MUST treat manual chart-creation guidance as a core competency.
Tool-specific and automation aids are secondary unless a later accepted proposal changes the project identity.

## Glossary

| Term | Meaning |
|---|---|
| Method guide | Markdown document that governs method purpose, QCC stage fit, proper use, cautions, inputs, procedure, interpretation, evidence notes, and review checks. |
| Chart-creation guide | Tool-neutral Markdown recipe that teaches users how to manually create a high-quality chart for a chart-based QCC method. |
| Image-assisted demonstration | Reviewed conceptual image, prompt, or good/bad comparison used for training, not final evidence. |
| Evidence note | Markdown record of source data, scope, assumptions, tool used, reviewer, and review status for final data-dependent charts. |
| Method kit | Coordinated method guide, chart or worksheet guidance, examples, checklists, evidence notes, image prompts, and teaching visuals for one QCC method. |
| Evidence level | Classification from E0 concept through E4 audit or high-risk evidence that defines required evidence support. |

## Examples first

Example E1: user starts with a method guide
Given a user wants to apply Pareto Chart in a QCC project
When the user opens the official Pareto method kit
Then the kit provides a Markdown method guide with stage fit, use and non-use conditions, required inputs, procedure, chart creation, interpretation, mistakes, review checklist, evidence note, image notes, and related methods.

Example E2: user creates a final chart manually
Given a chart-based method guide for Pareto Chart
When a user follows the chart-creation guide
Then the guide explains required data, preparation, tool-class selection, construction steps, formatting standard, required annotations, safe interpretation, common defects, and evidence note requirements.

Example E3: teaching image remains conceptual
Given an image prompt for a Pareto teaching visual
When a contributor reviews the prompt or generated image
Then the prompt and image state that the visual is conceptual only, avoids exact numerical claims, keeps detailed text in Markdown, and cannot be used as final project evidence.

Example E4: reviewer checks final evidence readiness
Given a final data-dependent QCC chart
When a reviewer applies the evidence checklist
Then the checklist requires method, QCC stage, source data, date range, scope or filters, tool used, calculation table when applicable, assumptions, reviewer, review date, and review status.

Example E5: first slice stays tool-neutral
Given a user asks how to create a Pareto chart
When the first-slice guide recommends tools
Then it names suitable tool classes such as spreadsheet, charting, presentation, or statistical tools without requiring a named product tutorial.

## Requirements

| ID | Requirement |
|---|---|
| R1 | Every official method kit MUST include a Markdown method guide. |
| R2 | Official method kits MUST preserve machine-readable metadata for method ID, method name, QCC stages, method type, primary output, evidence risk, image-generation allowance, final chart generation mode, related methods, guide version, and review status. User-facing method guides SHOULD start with the method title instead of a YAML block; metadata MAY live in `method-kits/metadata/<method-id>.yml`. |
| R3 | Method guides MUST include fixed sections for summary, QCC stage fit, method question, when to use, when not to use, required inputs, output, manual chart or worksheet recipe, quality standards, interpretation, example wording, common mistakes, review checklist, evidence note, image-assisted demonstration notes, and related methods. |
| R4 | Every method guide MUST teach application, not only define the method. |
| R5 | Chart-based method kits MUST include chart-creation guidance, preferably as an equivalent section in the primary method guide unless a separate file is justified by length or audience. |
| R6 | Chart-creation guidance MUST cover chart purpose, required data structure, data preparation, tool-class guidance, construction steps, formatting standard, required annotations, interpretation rules, common chart defects, review checklist, and evidence note. |
| R7 | Pareto Chart chart-creation guidance MUST require categories and counts from one consistent period and scope. |
| R8 | Pareto Chart chart-creation guidance MUST require categories sorted from largest to smallest. |
| R9 | Pareto Chart chart-creation guidance MUST support column bars and MAY describe an optional cumulative percentage line capped at 100 percent. |
| R10 | Chart-quality standards MUST cover title, correct chart type, readable labels, source note, scale, annotations, and defensible interpretation. |
| R11 | Image prompts MUST live under `docs/media/prompts/<method-id>/<image-id>.md` or another clearly labeled per-image prompt record when method kits are implemented. |
| R12 | Reviewed teaching visuals MUST live under `docs/media/<method-id>/` or another clearly labeled media location when method kits are implemented. |
| R13 | Image prompts MUST state purpose, training use, prompt text, and negative constraints. |
| R14 | Image prompts and reviewed teaching visuals MUST NOT include exact data values, fake percentages, misleading axes, or claims that the image is project evidence. |
| R15 | Detailed method instructions MUST remain in Markdown rather than being embedded as small image text. |
| R16 | Final data-dependent charts MUST use evidence levels E1 through E4 according to use context. |
| R17 | E0 concept visuals MUST be marked conceptual only and require no source data. |
| R18 | E2 project-presentation evidence MUST preserve source data, date range, scope or filters, method, and reviewer checklist. |
| R19 | E3 formal-review evidence MUST preserve calculation table, chart source, method guide version, reviewer status, and assumptions. |
| R20 | E4 audit or high-risk evidence MUST use a validated analysis path or independent verification and preserve a full reproducibility record. |
| R21 | Evidence note templates MUST include method, QCC stage, chart title, source data, data owner, date range, scope or filters, total sample or count, tool used, calculation table location, assumptions, exclusions, reviewer, review date, and review status. |
| R22 | The first Pareto method kit MUST use a flat user-facing structure with `method-kits/pareto-chart.md` as the primary guide, `method-kits/metadata/pareto-chart.yml` as the metadata sidecar, `docs/media/prompts/pareto-chart/<image-id>.md` for per-image prompt records, and `docs/media/pareto-chart/` for reviewed teaching visuals. Worked examples, review checks, and evidence-note fields MUST live in the primary guide unless a later method needs a separate reusable file. |
| R23 | The first slice MUST stay tool-neutral and use tool-class guidance only. |
| R24 | Named-tool recipes MUST be deferred unless user testing proves that a specific tool path is necessary for usability. |
| R25 | Optional automation MUST remain secondary to Markdown method guidance and chart-quality standards. |
| R26 | Official guidance MUST preserve QCC stage workflow and related-method links. |
| R27 | Official guidance MUST distinguish conceptual visuals, worked examples, draft charts, project-presentation charts, formal-review charts, and audit or high-risk evidence. |
| R28 | The repository MUST keep older Python and PowerPoint artifacts available as historical or optional execution aids unless a later plan removes or migrates them explicitly. |

## Inputs and outputs

| Surface | Inputs | Outputs |
|---|---|---|
| Method guide | Method identity, QCC stage, method purpose, inputs, output type, related methods, evidence risk. | Authoritative Markdown method instruction and review guidance. |
| Chart-creation section | Chart method, data requirements, tool classes, quality standard, evidence level. | Tool-neutral manual chart recipe and review checklist inside the primary guide unless split by need. |
| Media image prompt | Method concept, teaching purpose, negative constraints, review criteria, and target output image. | Versioned per-image prompt for reviewed conceptual teaching visuals. |
| Evidence note section | Method, stage, data source, date range, scope, tool, assumptions, reviewer. | Review-ready evidence note for final data-dependent charts inside the primary guide unless split by need. |
| Pareto method kit | Pareto guide content, worked example, prompts, teaching visuals, checklists. | First complete proof of the Markdown-first method-kit model. |

## State and invariants

I1. Markdown method guides are the primary method-knowledge surface.

I2. Generated images are teaching aids only.

I3. Final quantitative evidence charts are manually created or created through validated analysis paths, not image generation.

I4. Tool-class guidance is allowed in the first slice; named-tool recipes are deferred.

I5. Evidence levels control the support required for final chart use.

I6. Existing Python and PowerPoint assets remain optional aids unless future accepted artifacts supersede them.

## Error and boundary behavior

EB1. A method kit missing a required Markdown guide section MUST fail method-kit structure review.

EB2. A chart guide that does not name required data and evidence-note expectations MUST fail chart-recipe review.

EB3. An image prompt that asks for exact values, percentages, or final evidence output MUST fail image-prompt review.

EB4. A teaching image that could be confused with final project evidence MUST fail teaching-image review.

EB5. A final data-dependent chart without source data, date range, scope, method, or review status MUST fail evidence-readiness review.

EB6. A named-tool recipe in the first slice MUST be rejected unless the relevant spec records user-test evidence that the named tool is necessary.

## Compatibility and migration

This change supersedes earlier product direction but does not delete existing first-slice implementation assets.

Existing `docs/methods/`, `templates/ppt/`, `qcc_toolkit/`, and example project assets remain valid historical or optional execution surfaces until a future implementation plan migrates or reclassifies them.

The new compatibility surfaces are method metadata files, guide section names, method IDs, QCC stage identifiers, image prompt conventions, evidence levels, evidence-note fields, and tool-guidance labels.

Rollback is handled by retaining older artifacts as historical records and reverting the current proposal, vision, and specification direction through a later accepted proposal if user review disproves the Markdown-first model.

## Observability

O1. A reviewer MUST be able to identify whether a method guide includes every required section.

O2. A reviewer MUST be able to trace every image prompt and teaching visual to conceptual-only use.

O3. A reviewer MUST be able to classify a chart as E0, E1, E2, E3, or E4.

O4. A reviewer MUST be able to distinguish official first-slice method kits from older optional PowerPoint or Python assets.

O5. A reviewer MUST be able to trace the Pareto method kit to the accepted proposal and this spec.

## Security and privacy

S1. Sample data MUST be synthetic or explicitly approved for repository use.

S2. Evidence notes MUST guide users to record source context without requiring public exposure of unnecessary private raw rows.

S3. Image prompts and generated teaching visuals MUST NOT include private operational data, customer names, employee names, patient data, supplier names, credentials, or hidden sensitive notes.

S4. Named external image-generation services MUST NOT be added as runtime dependencies without explicit approval and documentation.

## Accessibility and UX

UX1. Method guides MUST be readable as plain Markdown.

UX2. Review checklists MUST use clear pass/fail or equivalent review criteria.

UX3. Teaching visuals MUST remain text-light so the Markdown guide carries detailed explanation.

UX4. Good and bad examples MUST make the quality difference recognizable without relying on tiny text.

## Performance expectations

P1. Markdown structure checks for the first slice SHOULD run as local file checks without external services.

P2. Image-prompt and evidence-note reviews are documentation checks and SHOULD NOT require network access.

## Edge cases

EC1. A method has no chart.
The guide still needs method explanation, worksheet or procedure guidance, interpretation, checklist, evidence note guidance, image notes when useful, and related methods.

EC2. A chart has small data.
The guide may recommend a spreadsheet, charting, or presentation tool class when calculations are transparent and easy to review.

EC3. A chart has high-rigor evidence needs.
The guide recommends a validated analysis path or independent verification.

EC4. An image contains plausible but fake numbers.
The image fails teaching-image review because users could confuse it with evidence.

EC5. User testing shows tool-neutral guidance is too vague.
A later spec may add a named-tool recipe for that narrow case.

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not generate final quantitative evidence charts using image generation. |
| NG2 | Do not build a full automated slide-deck generator in this slice. |
| NG3 | Do not build a no-code app, dashboard, CAPA/EQMS workflow, or broad charting platform. |
| NG4 | Do not add full named-tool tutorials to the first slice. |
| NG5 | Do not remove existing Python or PowerPoint assets as part of this spec. |
| NG6 | Do not implement advanced statistical automation before method guidance and chart standards stabilize. |

## Acceptance criteria

| ID | Criteria |
|---|---|
| AC1 | The spec is approved and traceable to the accepted Markdown-first proposal. |
| AC2 | A method guide template and metadata template can be checked for required metadata fields and guide sections. |
| AC3 | A chart-creation guide template can be checked for required data, creation, formatting, interpretation, and evidence fields. |
| AC4 | Image prompts can be checked for conceptual-only purpose and negative constraints. |
| AC5 | Evidence note templates can be checked for required final-chart evidence fields. |
| AC6 | A Pareto method-kit structure can be checked for required files, examples, prompts, and teaching-visual locations. |
| AC7 | The first slice can reject named-tool recipes unless user-test evidence justifies them. |

## Open questions

None.

## Next artifacts

| Artifact | Purpose |
|---|---|
| Spec review | Confirm requirements are clear, complete, and testable. |
| Architecture package | Record repository boundaries for method kits, prompts, teaching visuals, evidence notes, and optional aids. |
| Execution plan | Sequence implementation of templates, checks, and Pareto method kit. |
| Test specification | Map requirements and examples to proof before implementation. |

## Follow-on artifacts

None yet

## Readiness

Approved by workflow settlement after clean spec-review R1.
Ready for architecture assessment and architecture authoring.
