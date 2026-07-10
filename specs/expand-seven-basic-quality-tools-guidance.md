# Expand Seven Basic Quality Tools Guidance Spec

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-09-expand-seven-basic-quality-tools-guidance.md`
- Proposal status: accepted
- Proposal review: `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/reviews/proposal-review-r3.md`

This spec turns the accepted proposal for Flowchart / Process Map, Histogram, and Scatter Diagram guidance into observable repository behavior.
It extends the approved Markdown-first method-guidance model without changing the project identity.

## Goal and context

QCC Toolkit MUST add Markdown-first method kits for Flowchart / Process Map, Histogram, and Scatter Diagram.

The new method kits MUST help users understand where each method fits in a QCC project story, how to create the output manually, how to interpret it safely, and how to review the output.
The kits MUST include necessary conceptual teaching images and prompt records when visuals materially improve method demonstration.

Generated visuals remain conceptual teaching aids only.
They MUST NOT be final quantitative charts, project evidence, proof of root cause, proof of process stability, or proof of improvement.

## Glossary

| Term | Meaning |
|---|---|
| Flowchart / Process Map | A current-state process diagram used to understand sequence, handoffs, decisions, queues, rework loops, and failure locations. |
| Histogram | A frequency distribution chart for numeric observations used to understand spread, shape, and outliers. |
| Scatter Diagram | A paired-variable plot used to explore whether two measured variables appear related. |
| Conceptual teaching image | Reviewed generated or created visual used to teach a method idea or common defect, not to present final evidence. |
| Prompt record | Markdown record containing purpose, intended use, final prompt, negative constraints, output path, conceptual-only policy, and review status for a teaching image. |
| Good/bad comparison | Teaching visual that contrasts an acceptable layout or interpretation habit with a weak or misleading one. |

## Examples first

Example E1: Flowchart / Process Map current-state use
Given a QCC team is trying to understand where defects enter a process
When the user opens the Flowchart / Process Map method kit
Then the guide explains how to define start/end boundaries, map steps, decisions, handoffs, queues, rework loops, and failure locations before cause analysis.

Example E2: Histogram variation use
Given a QCC team has numeric observations from one scoped period
When the user opens the Histogram method kit
Then the guide explains how to prepare numeric data, choose bins carefully, label the chart, identify spread and outliers, and avoid claiming process stability.

Example E3: Scatter Diagram relationship use
Given a QCC team has paired numeric observations for two variables
When the user opens the Scatter Diagram method kit
Then the guide explains how to define x/y variables, plot paired observations, label axes and units, inspect outliers, and avoid treating correlation as root-cause proof.

Example E4: conceptual teaching images
Given a contributor adds a generated histogram teaching image
When a reviewer checks the image and prompt record
Then the image is text-light, conceptual-only, free of exact fake values or percentages, linked to a prompt record, and not usable as final evidence.

Example E5: project-story navigation
Given a user reads `docs/qcc-project-story.md` or the README method index
When the user looks for methods for current-state grasp, cause analysis preparation, or verification planning
Then Flowchart / Process Map, Histogram, and Scatter Diagram are linked with their proper QCC project-story roles.

## Requirements

| ID | Requirement |
|---|---|
| R1 | The repository MUST add `method-kits/flowchart.md`, `method-kits/histogram.md`, and `method-kits/scatter-diagram.md` as official Markdown-first method kits. |
| R2 | Each new method kit MUST include lightweight front matter or equivalent reviewable metadata for method ID, method name, method type, QCC stages, status, guide version, image policy, and automation policy. |
| R3 | Each new method kit MUST include sections for summary, QCC stage fit, method question, when to use, when not to use, required inputs, output, manual chart or diagram recipe, quality standards, interpretation limits, common mistakes, evidence note, review checklist, image-assisted demonstration notes, and related methods. |
| R4 | Each new method kit MUST explain how the method connects to the QCC project story rather than presenting the method as a disconnected tool page. |
| R5 | The Flowchart / Process Map guide MUST cover start and end boundaries, process steps, decision points, handoffs, queues or waiting points, rework loops, failure or defect locations, and current-state versus future-state distinction. |
| R6 | The Histogram guide MUST cover numeric data requirements, sample-size caution, bin-width caution, outlier handling, distribution-shape interpretation, before/after comparison cautions, and a statement that a histogram does not prove process stability. |
| R7 | The Scatter Diagram guide MUST cover paired numeric observations, x/y variable definitions, axis labels and units, outlier handling, correlation-versus-causation caution, and a statement that a scatter diagram does not prove root cause by itself. |
| R8 | Each new method kit MUST teach manual creation steps and chart or diagram quality standards without requiring a named spreadsheet, presentation, statistics, diagramming, or programming tool. |
| R9 | The repository MUST NOT add Control Chart, SPC rules, control-limit calculations, process capability, or run-rule automation as part of this change. |
| R10 | The repository MUST NOT add chart-rendering automation for Histogram or Scatter Diagram as part of this change. |
| R11 | The repository MUST add necessary conceptual teaching-image prompt records for each method under `docs/media/prompts/<method-id>/` or another existing approved prompt-record location. |
| R12 | When generated teaching images are added, they MUST live under `docs/media/<method-id>/` or another existing approved teaching-visual location and MUST be linked from the relevant method guide. |
| R13 | Prompt records MUST preserve purpose, intended use, final prompt, negative constraints, conceptual-only policy, output path, and review status. |
| R14 | Generated teaching images and prompt records MUST NOT include exact fake data values, fake percentages, private names, credentials, production-specific identifiers, causal proof claims, process-stability claims, or final-evidence claims. |
| R15 | Teaching visuals MUST be text-light and MUST keep detailed instructions in Markdown. |
| R16 | Flowchart / Process Map teaching visuals MUST include a current-state process-flow concept and a good-versus-weak process map comparison. |
| R17 | Histogram teaching visuals MUST include a conceptual distribution and a good-versus-weak histogram comparison. |
| R18 | Scatter Diagram teaching visuals MUST include a conceptual paired-variable pattern and a good-versus-weak scatter comparison. |
| R19 | README method-kit navigation MUST link to the three new method kits when implemented. |
| R20 | `docs/qcc-project-story.md` MUST link or reference the three new method kits in the project stages where they fit. |
| R21 | Local documentation checks MUST verify required method-kit sections, required method-specific cautions, prompt-record constraints, conceptual-only image policy, and expected links. |
| R22 | Existing optional `docs/methods/`, `templates/ppt/`, and `qcc_toolkit/` assets MUST remain available unless a later accepted proposal explicitly changes them. |

## Inputs and outputs

| Surface | Inputs | Outputs |
|---|---|---|
| Flowchart / Process Map method kit | Current-state process facts, process boundaries, handoffs, decisions, queues, rework loops, and failure locations. | Tool-neutral Markdown guide for creating and reviewing a current-state process map. |
| Histogram method kit | Numeric observations, sample scope, date range or observation period, and binning choices. | Tool-neutral Markdown guide for creating and reviewing a histogram with interpretation cautions. |
| Scatter Diagram method kit | Paired numeric observations, x/y variable definitions, units, and observation scope. | Tool-neutral Markdown guide for creating and reviewing a scatter diagram with causation cautions. |
| Prompt records | Teaching purpose, method concept, negative constraints, output path, review state. | Reviewable Markdown prompt records for conceptual teaching visuals. |
| Teaching visuals | Approved imagegen output or equivalent conceptual image asset. | Text-light conceptual visual linked from the method guide and reviewed as E0 teaching material. |
| Navigation | Method-kit paths and QCC project-story roles. | README and project-story links to the new official method kits. |

## State and invariants

I1. Markdown method kits remain the authoritative method guidance.

I2. Manual chart and diagram creation remains a core competency.

I3. Generated images remain conceptual-only teaching aids and never final quantitative evidence.

I4. Tool-neutral guidance remains the first-slice default for these three methods.

I5. Control Chart remains out of scope until a separate accepted proposal addresses SPC-specific interpretation safeguards.

I6. Existing Markdown-first media and prompt-record locations remain the preferred repository boundary.

## Error and boundary behavior

EB1. A new method kit missing a required shared section MUST fail method-kit structure checks.

EB2. A Flowchart / Process Map guide missing boundaries, decisions, handoffs, rework loops, or current-state distinction MUST fail method-specific checks.

EB3. A Histogram guide missing numeric-data, sample-size, bin-width, outlier, or no-stability cautions MUST fail method-specific checks.

EB4. A Scatter Diagram guide missing paired-observation, axis, outlier, or correlation-versus-causation cautions MUST fail method-specific checks.

EB5. A prompt record missing purpose, final prompt, negative constraints, conceptual-only policy, output path, or review status MUST fail prompt-record checks.

EB6. A teaching visual or prompt that implies exact project data, final evidence, root-cause proof, process stability, or verified improvement MUST fail image-policy review.

EB7. A README or project-story link to a missing method kit MUST fail link or artifact-consistency checks.

## Compatibility and migration

This change adds new method-kit files and media assets without deleting legacy optional assets.

The new compatibility surfaces are method IDs `flowchart`, `histogram`, and `scatter-diagram`; their guide section names; prompt-record conventions; media paths; README links; and QCC project-story links.

No migration is required for existing Pareto, Check Sheet, Fishbone, Python, or PowerPoint assets.

Rollback can remove the new method kits, prompt records, media links, and navigation entries while leaving the accepted proposal and review records as historical evidence.

## Observability

O1. A reviewer MUST be able to inspect the three method-kit files and confirm required shared sections.

O2. A reviewer MUST be able to inspect method-specific text and confirm each required caution.

O3. A reviewer MUST be able to inspect prompt records and confirm conceptual-only policy and negative constraints.

O4. A reviewer MUST be able to inspect media links and distinguish generated teaching visuals from final evidence charts.

O5. A reviewer MUST be able to trace README and QCC project-story navigation to each new method kit.

## Security and privacy

S1. Prompt records and teaching visuals MUST NOT contain secrets, credentials, private machine paths, private operational records, customer names, employee names, patient data, supplier names, or production-specific identifiers.

S2. Example data described in method kits MUST be synthetic, generic, or explicitly non-sensitive.

S3. Evidence-note guidance SHOULD help users record source context without requiring public exposure of private raw rows.

S4. This change MUST NOT add runtime dependencies, network calls, telemetry, external services, or hosted image-generation integrations.

## Accessibility and UX

UX1. Method kits MUST be readable as plain Markdown.

UX2. Teaching visuals MUST remain text-light so essential instructions are available in Markdown.

UX3. Good/bad examples MUST make quality differences understandable without relying on tiny embedded text.

UX4. Review checklists MUST use concrete checks that a reviewer can apply without specialized software.

## Performance expectations

P1. Required documentation checks SHOULD run locally without network access.

P2. The change SHOULD avoid expensive broad validation for every edit by adding focused artifact-consistency checks for the new method-kit surfaces.

## Edge cases

EC1. A method has no generated image yet.
The method guide may remain draft only if the plan or implementation records the missing image as incomplete; a completed method kit that claims image-assisted demonstration must include the required prompt record and image review state.

EC2. Image text is inaccurate or unreadable.
The image fails review and must be replaced, revised, or unlinked while the Markdown guide remains authoritative.

EC3. Histogram data is too small or poorly binned.
The guide must caution users that interpretation may be weak and that the histogram does not prove stability.

EC4. Scatter plot shows a strong apparent relationship.
The guide must still warn that a scatter diagram does not prove root cause without deeper cause analysis or designed verification.

EC5. A process map looks like a final SOP.
The guide and image notes must clarify whether the map is current-state observation, proposed future state, or verified standard work.

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not add Control Chart in this change. |
| NG2 | Do not add SPC rules, control limits, process capability, subgroup logic, or run-rule automation. |
| NG3 | Do not add chart-rendering automation for Histogram or Scatter Diagram. |
| NG4 | Do not create named-tool tutorials for spreadsheets, presentation tools, statistics packages, diagramming tools, or programming languages. |
| NG5 | Do not treat generated images as final charts, project evidence, proof of method correctness, root-cause proof, or stability proof. |
| NG6 | Do not remove older optional method guides, templates, Python aids, or PowerPoint assets. |

## Acceptance criteria

| ID | Criteria |
|---|---|
| AC1 | The three new method-kit files exist and include required shared sections. |
| AC2 | Method-specific checks confirm required Flowchart, Histogram, and Scatter Diagram guidance and cautions. |
| AC3 | Prompt records exist for the required conceptual teaching visuals and include required prompt-record fields. |
| AC4 | Teaching visuals, when added, are stored in method-scoped media paths, linked from method guides, and reviewed as conceptual-only. |
| AC5 | README and `docs/qcc-project-story.md` link or reference the three new method kits in the correct context. |
| AC6 | Focused local documentation tests cover required sections, method-specific cautions, prompt-record constraints, link integrity, and out-of-scope guardrails. |
| AC7 | No Control Chart, SPC automation, named-tool tutorial, or chart-rendering automation is introduced. |

## Open questions

None.

## Next artifacts

| Artifact | Purpose |
|---|---|
| Spec review | Confirm this behavior contract is complete, testable, and aligned with the accepted proposal. |
| Architecture assessment | Decide whether the change reuses existing Markdown-first architecture or requires a new architecture package. |
| Execution plan | Sequence method-kit, prompt-record, image-review, navigation, and validation work. |
| Test specification | Map requirements and examples to focused checks and manual image-review proof before implementation. |

## Follow-on artifacts

None yet

## Readiness

Approved by workflow settlement after clean spec-review R1.
Ready for execution planning.
