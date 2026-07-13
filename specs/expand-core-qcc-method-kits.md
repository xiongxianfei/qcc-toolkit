# Expand Core QCC Method Kits Spec

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md`
- Proposal status: accepted
- Proposal review: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/proposal-review-r2.md`

## Goal and context

QCC Toolkit will promote Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H into official Markdown-first method kits.
The change also removes the old `docs/methods/` guide surface from live navigation and catalog references.
Extracted legacy content remains available in `docs/methods-key-content.md` as source material, not as a parallel guide surface.

## Glossary

| Term | Meaning |
|---|---|
| Official method kit | Canonical Markdown-first guide under `method-kits/`. |
| Deleted legacy guide | Former full guide under `docs/methods/` that is no longer retained as a compatibility page. |
| Extracted legacy content | Summary file at `docs/methods-key-content.md` preserving useful content from deleted legacy guides. |
| Deleted-reference cleanup | Updating catalog, navigation, tests, and present-tense docs so they do not rely on removed `docs/methods/` files. |
| Evidence status | Label that separates observed facts, plausible hypotheses, unknowns, rejected claims, and items requiring verification. |

## Examples first

Example E1: Check Sheet method-kit use
Given a team needs to collect defect observations consistently
When the user opens `method-kits/check-sheet.md`
Then the guide explains observation purpose, operational definitions, collection scope, category rules, blank/unknown/other handling, pilot collection, and handoff to later analysis.

Example E2: Fishbone method-kit use
Given a team has one clearly stated effect to analyze
When the user opens `method-kits/fishbone-diagram.md`
Then the guide explains context-appropriate branches, fact versus hypothesis separation, evidence status, and follow-up verification.

Example E3: 5 Whys method-kit use
Given a team investigates one selected suspected cause
When the user opens `method-kits/five-whys.md`
Then the guide explains that exactly five questions are not required, branching is allowed, facts or verification status belong on each link, and the chain is not proof by repetition.

Example E4: 5W2H method-kit use
Given a team needs to frame a problem or define an action
When the user opens `method-kits/five-w-two-h.md`
Then the guide supports both problem-framing mode and action-planning mode with owners, due dates, dependencies, verification measure, expected evidence, target or acceptance condition, assumptions, and constraints.

Example E5: deleted legacy references
Given `docs/methods/*.md` files have been removed
When a contributor runs focused artifact checks
Then README, `docs/qcc-project-story.md`, `templates/ppt/catalog.yml`, and present-tense docs do not point to deleted legacy guide paths.

## Requirements

| ID | Requirement |
|---|---|
| R1 | The repository MUST add `method-kits/check-sheet.md`, `method-kits/fishbone-diagram.md`, `method-kits/five-whys.md`, and `method-kits/five-w-two-h.md` as official Markdown-first method kits. |
| R2 | Each new method kit MUST include reviewable metadata for method ID, method name, method type, QCC stages, status, guide version, image policy, and automation policy. |
| R3 | Each new method kit MUST include sections for summary, QCC stage fit, method question, when to use, when not to use, required inputs, output, manual recipe, quality standards, interpretation limits, common mistakes, evidence note, review checklist, image-assisted demonstration notes, and related methods. |
| R4 | Each new method kit MUST explain how the method connects to the QCC project story rather than presenting the method as a disconnected tool page. |
| R5 | Check Sheet guidance MUST distinguish a check sheet from a generic checklist and cover observation purpose, operational definitions, observation period and scope, relevant context, category rules, blank/unknown/other handling, sampling or coverage guidance, pilot collection, and handoff to later analysis. |
| R6 | Check Sheet guidance MUST state that its output is structured observation data, not a conclusion or verified cause. |
| R7 | Fishbone Diagram guidance MUST cover one precise effect statement, context-appropriate categories, no mandatory reliance on one category model, fact versus hypothesis separation, evidence status, and prioritization for further checking. |
| R8 | Fishbone Diagram guidance MUST state that its output is a structured set of cause hypotheses, not verified root cause. |
| R9 | 5 Whys guidance MUST state that exactly five questions are not required, one linear chain may be insufficient, branching is acceptable, each answer needs fact support or verification status, personal blame should be avoided, and the stopping point should be an actionable system or process cause supported by evidence. |
| R10 | 5 Whys guidance MUST state that its output is a causal hypothesis chain with verification status, not proof by repetition. |
| R11 | 5W2H guidance MUST support problem-framing mode and action-planning mode. |
| R12 | 5W2H action-planning guidance MUST cover owner, due date, dependencies, verification measure, expected evidence, target or acceptance condition, assumptions, and constraints where relevant. |
| R13 | 5W2H guidance MUST state that the method improves clarity but does not replace root-cause analysis or prove that an action worked. |
| R14 | README and `docs/qcc-project-story.md` MUST link or reference the new method kits in the QCC stages where they fit. |
| R15 | Live catalog, navigation, test, and present-tense documentation surfaces MUST NOT rely on deleted `docs/methods/*.md` files. |
| R16 | `templates/ppt/catalog.yml` MUST either reference existing canonical method-kit paths or explicitly classify removed guide paths as historical text only; it MUST NOT point official active entries at missing files. |
| R17 | `docs/methods-key-content.md` MUST remain available as extracted source material for this change. |
| R18 | The new method kits MUST use `docs/methods-key-content.md` as a source check so useful legacy guidance is not lost. |
| R19 | Generated teaching visuals MUST NOT be required for every guide. |
| R20 | If optional generated visuals are added, they MUST be conceptual, reviewed, text-light, clearly not evidence, and stored only in non-empty method-scoped media paths. |
| R21 | The change MUST NOT add Control Chart, SPC rules, control-limit calculations, run-rule automation, process capability, broad statistical automation, or named-tool tutorials. |
| R22 | Focused local checks MUST verify required sections, method-specific safeguards, navigation, deleted-reference cleanup, canonical source behavior, and out-of-scope guardrails. |

## Inputs and outputs

| Surface | Inputs | Outputs |
|---|---|---|
| Method kits | Proposal decisions, extracted legacy content, current method-kit standard, QCC project-story roles. | Four canonical Markdown-first guides under `method-kits/`. |
| Navigation | Method-kit paths and QCC stage roles. | README and project-story links to canonical guides. |
| Deleted-reference cleanup | Existing references to removed `docs/methods/` files. | Updated or removed references that no longer point to missing files. |
| Optional media | Reviewed conceptual visual need and prompt record. | Method-scoped media only when used. |

## State and invariants

I1. Markdown method kits are the canonical method guidance surface.

I2. `docs/methods-key-content.md` is preserved as extracted source material, not as a canonical method guide.

I3. Manual method and chart/worksheet creation guidance remains central.

I4. Generated visuals remain conceptual-only teaching aids.

I5. Specific tools, PowerPoint templates, and Python aids remain optional execution choices.

## Error and boundary behavior

EB1. A new method kit missing required shared sections fails documentation checks.

EB2. A method kit missing method-specific safeguards fails focused checks.

EB3. A live link, catalog entry, or present-tense docs claim pointing to a removed `docs/methods/*.md` file fails deleted-reference checks unless explicitly marked as historical archival evidence.

EB4. A generated visual that implies final evidence, verified cause, verified improvement, exact fake values, or process stability fails review.

EB5. Any Control Chart, SPC, process capability, named-tool tutorial, or broad automation addition fails scope-guard checks.

## Compatibility and migration

This change intentionally deletes the old `docs/methods/` guide files rather than preserving compatibility notices.
The migration path is to update live references to canonical method-kit paths or to mark historical references as historical records.
Rollback uses `docs/methods-key-content.md` as the extraction source if old content needs to be recovered.

## Observability

O1. Reviewers can inspect the four method-kit files and confirm required sections and safeguards.

O2. Reviewers can inspect README and `docs/qcc-project-story.md` and confirm canonical navigation.

O3. Reviewers can inspect `templates/ppt/catalog.yml`, tests, and present-tense docs and confirm no live missing `docs/methods/` dependency remains.

O4. Reviewers can trace content preservation through `docs/methods-key-content.md`.

## Security and privacy

S1. Method guides, examples, prompt records, and visuals MUST NOT contain secrets, credentials, private records, customer names, employee names, patient data, supplier names, or production-specific identifiers.

S2. Example data MUST be synthetic, generic, or explicitly non-sensitive.

S3. This change MUST NOT add network calls, telemetry, hosted integrations, or external services.

## Accessibility and UX

UX1. Method kits MUST be readable as plain Markdown.

UX2. Essential instructions MUST live in Markdown, not only in images.

UX3. Review checklists MUST be concrete enough for a facilitator to apply without specialized software.

## Performance expectations

P1. Focused documentation and artifact-consistency checks SHOULD run locally without network access.

P2. The change SHOULD avoid broad runtime validation for documentation-only edits unless existing governance requires it.

## Edge cases

EC1. A deleted legacy path appears only in historical change evidence.
Historical references may remain if they are clearly historical and not active navigation, catalog, or present-tense behavior.

EC2. A template catalog entry needs a Markdown guide path.
It should point to an existing canonical method kit or be reclassified so validation does not require a missing file.

EC3. A guide has no generated image.
That is acceptable when Markdown examples communicate the method adequately.

EC4. 5 Whys branches into multiple chains.
The guide should allow branching and require verification status instead of forcing a single chain.

EC5. A Check Sheet includes an "other" category.
The guide should require rules for using and reviewing "other" observations.

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not implement Control Chart, SPC rules, control limits, run rules, or process capability. |
| NG2 | Do not add broad statistical automation or rendering backends. |
| NG3 | Do not create named-tool tutorials as the primary guide. |
| NG4 | Do not restore `docs/methods/` pages as compatibility notices. |
| NG5 | Do not treat generated visuals as project evidence. |

## Acceptance criteria

| ID | Criteria |
|---|---|
| AC1 | Four new method-kit files exist at the canonical paths named in R1. |
| AC2 | Focused checks confirm shared sections and metadata for all four guides. |
| AC3 | Focused checks confirm Check Sheet safeguards and output boundary. |
| AC4 | Focused checks confirm Fishbone Diagram safeguards and output boundary. |
| AC5 | Focused checks confirm 5 Whys safeguards and output boundary. |
| AC6 | Focused checks confirm 5W2H two-mode guidance, planning fields, and output boundary. |
| AC7 | README and `docs/qcc-project-story.md` point to canonical method kits. |
| AC8 | Active catalog/navigation/test/present-tense docs no longer rely on deleted `docs/methods/*.md` files. |
| AC9 | Scope-guard checks confirm no Control Chart, SPC, process capability, broad automation, or named-tool tutorial was introduced. |
| AC10 | Manual reviewer proof confirms the guides are method-correct and do not overclaim causation, verification, or improvement. |

## Open questions

None.

## Next artifacts

- Spec review.
- Architecture assessment.
- Execution plan.
- Test specification and test-spec review.

## Follow-on artifacts

None yet

## Readiness

Ready for spec review.
