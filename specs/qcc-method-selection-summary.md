# QCC Method Selection Summary Specification

## Status

approved

## Related proposal

- Proposal: [Create a QCC Method Selection Summary](../docs/proposals/2026-07-13-qcc-method-selection-summary.md)
- Proposal review: [proposal-review-r1](../docs/changes/2026-07-13-qcc-method-selection-summary/reviews/proposal-review-r1.md)

## Goal and context

This specification defines the observable behavior for a concise method-selection summary at `method-kits/README.md`.
The summary helps users select QCC methods by combining QCC stage, immediate project question, and available evidence or input.

The selector must preserve the QCC project-story relationship between methods and stages without implying that one method belongs to only one stage.
It must also preserve each method's interpretation limits, link to canonical detailed guides when they exist, and keep future or advanced methods visibly separate from available guidance.

## Upstream status settlement

- Upstream artifact: `docs/proposals/2026-07-13-qcc-method-selection-summary.md`
- Review evidence: `docs/changes/2026-07-13-qcc-method-selection-summary/reviews/proposal-review-r1.md`
- Previous status: draft
- New status: accepted
- Settlement result: updated
- Settlement blocker: none

## Glossary

| Term | Meaning |
|---|---|
| Selector | The canonical method-selection summary at `method-kits/README.md`. |
| QCC stage | A story step from `docs/qcc-project-story.md`: Problem selection, Current-state grasp, Cause analysis, Countermeasure planning, Verification, or Standardization and control. |
| Primary use | A method-stage relationship where the method directly answers a common project question for that stage. |
| Supporting use | A method-stage relationship where the method helps prepare, focus, interpret, or hand off work in that stage but is not the main method for the stage question. |
| Available method | A method with an existing canonical guide under `method-kits/`. |
| Planned method | A method accepted for later coverage but without a canonical guide in this slice. |
| Deferred / advanced method | A method that needs stronger safeguards or a separate proposal before guidance is added. |
| Future sustainment guidance | Later guidance for holding gains after verification, such as Standard Work, Visual Control, or Monitoring Plan. |

## Examples first

Example E1: choosing a method from the stage view
Given a user is in Current-state grasp and needs to understand how often packaging defects occur by type
When the user reads the selector
Then the selector shows Check Sheet as a primary method for structured observation and Pareto Chart as a primary or supporting method for ranked category counts.

Example E2: avoiding a stage-only overclaim
Given a user is in Cause analysis and sees Pareto Chart listed as a supporting method
When the user reads the limitation
Then the selector states that Pareto Chart can focus category investigation but does not prove root cause.

Example E3: selecting by project question
Given a user asks "Do two measured variables appear related?"
When the user reads the question-oriented selector
Then the selector directs the user to Scatter Diagram, requires paired numeric observations as input, and states that apparent relationship does not prove causation.

Example E4: distinguishing future sustainment guidance
Given a user is in Standardization and control
When the user reads the stage view
Then the selector shows Standard Work, Visual Control, and Monitoring Plan as future sustainment guidance rather than linked available method guides.

## Requirements

| ID | Requirement |
|---|---|
| R1 | The selector MUST be located at `method-kits/README.md`. |
| R2 | The selector MUST present method selection as a combination of QCC stage, immediate project question, and available evidence or input. |
| R3 | The selector MUST use the canonical QCC stage labels from `docs/qcc-project-story.md`: Problem selection, Current-state grasp, Cause analysis, Countermeasure planning, Verification, and Standardization and control. |
| R4 | The selector MUST include a quick selection view organized by project question. |
| R5 | The selector MUST include a stage-oriented view organized by QCC stage. |
| R6 | The stage-oriented view MUST distinguish primary use from supporting use. |
| R7 | The selector MUST NOT present any available method as mandatory for exactly one stage. |
| R8 | The selector MUST show the expected input or evidence needed before selecting a method. |
| R9 | The selector MUST show a concise typical output for each stage relationship. |
| R10 | The selector MUST show an important interpretation limitation for each available method. |
| R11 | The selector MUST link only existing canonical method guide files. |
| R12 | Planned, deferred, advanced, or future sustainment methods MUST appear as plain text with visible status labels until a canonical guide exists. |
| R13 | The selector MUST identify all available method guides present in `method-kits/` at implementation time. |
| R14 | The selector MUST include a maintenance note requiring method additions, renames, removals, status changes, and stage-fit changes to update the selector in the same change. |
| R15 | The root `README.md` MUST link to the selector instead of duplicating the stage-method matrix. |
| R16 | Because `docs/qcc-project-story.md` exists, it MUST link to the selector instead of duplicating any new detailed selection matrix. |
| R17 | The selector MUST NOT reproduce full method procedures, formulas, chart recipes, worked examples, or review checklists. |
| R18 | The selector MUST NOT create a machine-readable method registry, metadata sidecar, recommendation algorithm, wizard, web interface, or chart-generation behavior. |

## Method and stage relationship

The selector must use this relationship model.
The matrix is the content contract for `method-kits/README.md`; the final wording may be concise, but the primary and supporting relationships must remain visible.

| QCC stage | Primary use | Supporting use | Typical output | Important limitation |
|---|---|---|---|---|
| Problem selection | 5W2H; Check Sheet; Pareto Chart | Flowchart / Process Map when process scope is unclear | Focused problem statement, first observations, baseline focus reason | Selection evidence does not prove root cause or solution effectiveness. |
| Current-state grasp | Check Sheet; Flowchart / Process Map; Pareto Chart; Histogram | 5W2H for scope clarification | Baseline data, process map, distribution view, observed pattern | Current-state description must not be reported as cause proof. |
| Cause analysis | Fishbone Diagram; 5 Whys; Scatter Diagram | Pareto Chart for focused categories; Flowchart / Process Map for process locations; Check Sheet or Histogram for additional facts | Cause hypotheses, checked facts, relationship clues, rejected assumptions | Hypotheses and apparent relationships require verification before root-cause claims. |
| Countermeasure planning | 5W2H | Fishbone Diagram and 5 Whys as source context for the selected cause; Flowchart / Process Map for locating the change | Owner, action, due date, expected mechanism, verification method | Action clarity does not prove the action is correct or effective. |
| Verification | Check Sheet; Pareto Chart; Histogram; Scatter Diagram | Flowchart / Process Map for deciding where to observe or compare process change | Comparable before/after evidence and cautious interpretation | Before/after evidence needs comparable scope, definitions, period logic, and measurement rules. |
| Standardization and control | Future sustainment guidance: Standard Work; Visual Control; Monitoring Plan | Check Sheet or monitoring checklist when later guidance defines the control method | New standard, monitoring plan, owner, cadence, trigger for follow-up | Sustainment guidance is future coverage unless a canonical method guide exists. |

## Project-question relationship

The selector must include a question-oriented view with at least these rows.
Rows may be shortened for readability, but they must preserve the method direction, required input, and safe boundary.

| Project question | Method direction | Evidence or input needed | Safe boundary |
|---|---|---|---|
| How should observations be collected consistently? | Check Sheet | Observation purpose, operational definitions, period, scope, categories or units | Records observations; does not prove cause. |
| How does the process actually flow? | Flowchart / Process Map | Process boundaries, observed steps, handoffs, decisions, rework, source facts | Shows sequence and handoffs; does not prove which step caused the problem. |
| Which categories contribute most to the problem? | Pareto Chart | Stable categories, counts, consistent period and scope | Prioritizes recorded categories; does not prove root cause. |
| What does the distribution of numeric data look like? | Histogram | Numeric observations, unit, sample size, period, scope, bin rationale | Shows distribution and variation; does not prove process stability. |
| Do two measured variables appear related? | Scatter Diagram | Paired numeric observations, variable units, pairing rule, period, scope | Shows an apparent relationship; does not prove causation. |
| What possible causes should be investigated? | Fishbone Diagram | One precise effect, current-state evidence, context-appropriate categories | Organizes cause hypotheses; does not verify them. |
| How might one suspected causal chain work? | 5 Whys | Focused problem or suspected cause, evidence for each link, verification status | Develops a causal hypothesis chain; repeated why questions do not prove root cause. |
| How should the problem or action be made concrete? | 5W2H | Problem background or selected action, scope, owner or affected roles, timing, impact or resource | Clarifies a problem or action; does not prove the action will work or has worked. |

## Method status relationship

The selector must classify methods as follows unless implementation-time repository contents prove a different available-guide state.

| Method or guidance | Selector status | Link behavior |
|---|---|---|
| Check Sheet | Available | Link to `method-kits/check-sheet.md`. |
| Flowchart / Process Map | Available | Link to `method-kits/flowchart.md`. |
| Pareto Chart | Available | Link to `method-kits/pareto-chart.md`. |
| Histogram | Available | Link to `method-kits/histogram.md`. |
| Scatter Diagram | Available | Link to `method-kits/scatter-diagram.md`. |
| Fishbone Diagram | Available | Link to `method-kits/fishbone-diagram.md`. |
| 5 Whys | Available | Link to `method-kits/five-whys.md`. |
| 5W2H | Available | Link to `method-kits/five-w-two-h.md`. |
| Control Chart / SPC / process capability | Deferred / advanced | Do not link unless a canonical guide exists after a separate accepted proposal. |
| Standard Work / Visual Control / Monitoring Plan | Future sustainment guidance | Do not link unless a canonical guide exists after later sustainment coverage. |

## Inputs and outputs

Inputs:

- Existing QCC project-story guidance in `docs/qcc-project-story.md`.
- Existing canonical method guides under `method-kits/`.
- Existing root navigation in `README.md`.
- Existing method-guide interpretation limits and required-input statements.

Outputs:

- One selector at `method-kits/README.md`.
- Root navigation link from `README.md` to `method-kits/README.md`.
- QCC project-story link from `docs/qcc-project-story.md` to `method-kits/README.md`.
- No new runtime output, generated catalog, data file, image, chart, or API.

## State and invariants

- The selector is the only canonical detailed stage-method selection matrix.
- Other documents may link to the selector but must not maintain an independently detailed duplicate matrix.
- Existing method guides remain the canonical source for full procedures, chart recipes, examples, and review checklists.
- Available method links must resolve to files that exist.
- Future or advanced guidance must remain unlinked status text until a canonical guide exists.
- Method-stage relationships are advisory selection guidance, not compatibility guarantees for automation.

## Error and boundary behavior

- If a method guide does not exist, the selector must not link to it.
- If a stage has no available primary method guide, the selector must state the status plainly instead of inventing guidance.
- If a method appears in more than one stage, the selector must show primary and supporting roles rather than forcing one stage.
- If a project question could fit more than one method, the selector must use input or evidence conditions to distinguish the choices.
- If a method output cannot support a causal, stability, or effectiveness conclusion, the selector must state that limitation.

## Compatibility and migration

This change is documentation-only.
It does not change public Python APIs, data schemas, chart specification fields, project-folder formats, generated artifacts, or template placeholders.

The selector should preserve current method names and file paths unless implementation-time inspection shows a guide has moved.
If a method file is renamed or removed later, the selector must be updated in the same change.

Rollback is additive.
If the selector proves confusing, remove or revise `method-kits/README.md` and restore simple navigation links without changing the method guides.

## Observability

Observability is documentation proof rather than runtime telemetry.

The change must be observable through:

- file existence for `method-kits/README.md`;
- link checks or targeted file inspection for every linked guide;
- root and QCC project-story navigation checks;
- review evidence that the selector contains question view, stage view, method status, interpretation guardrails, detailed links, and maintenance note;
- recorded manual scenario review for representative user and reviewer tasks.

## Security and privacy

The selector must not include real customer data, private operational data, secrets, credentials, or private machine paths.
Examples and scenarios must remain generic or synthetic.

The selector must not encourage users to paste sensitive data into external tools or services.
Tool choice remains secondary and tool-neutral.

## Accessibility and UX

The selector must be readable as plain Markdown.
Tables must have clear headers and concise cells.
Links must use descriptive method names rather than opaque file paths as visible text.
The selector must support two entry paths: by project question and by QCC stage.

## Performance expectations

Not applicable for runtime performance.

The selector should remain concise enough for a user to scan without reading every detailed guide first.
Full procedures, formulas, examples, and checklists belong in method guides.

## Edge cases

EC1. A method supports several stages.
The selector shows primary and supporting use instead of duplicating full guidance in each stage.

EC2. A stage lists future sustainment guidance.
The selector labels the guidance as future sustainment and does not link missing files.

EC3. A user asks a method question without knowing the QCC stage.
The question-oriented view provides the first navigation path and then points to the detailed guide.

EC4. A user starts from a QCC stage but lacks required input.
The stage view must expose the needed evidence or point the user toward a method that collects or clarifies it.

EC5. A method's output is commonly overclaimed.
The selector must include the safe interpretation boundary before sending the user to the detailed guide.

EC6. A later method addition changes availability.
The same change must update method status, stage relationships when applicable, and detailed links.

## Non-goals

- Do not implement new methods.
- Do not rewrite detailed method guides.
- Do not add a new QCC stage model.
- Do not require every method to belong to only one stage.
- Do not prescribe a charting, spreadsheet, presentation, statistical, or programming tool.
- Do not build an interactive wizard, recommendation algorithm, web UI, generated catalog, or metadata registry.
- Do not add Control Chart, SPC, process capability, Standard Work, Visual Control, or Monitoring Plan guidance beyond status and handoff labels.
- Do not duplicate full method procedures, formulas, chart recipes, worked examples, or review checklists in the selector.

## Acceptance criteria

| ID | Criterion |
|---|---|
| AC1 | `method-kits/README.md` exists and contains an introduction explaining the stage-question-evidence selection model. |
| AC2 | The selector contains a project-question view covering Check Sheet, Flowchart / Process Map, Pareto Chart, Histogram, Scatter Diagram, Fishbone Diagram, 5 Whys, and 5W2H. |
| AC3 | The selector contains a stage-oriented view covering Problem selection, Current-state grasp, Cause analysis, Countermeasure planning, Verification, and Standardization and control. |
| AC4 | The stage-oriented view distinguishes primary use from supporting use. |
| AC5 | Every available method guide listed in the status table links to an existing file. |
| AC6 | Planned, deferred, advanced, and future sustainment methods are not linked unless their canonical guide exists. |
| AC7 | The selector includes interpretation guardrails for all available methods. |
| AC8 | The selector does not duplicate full procedures, formulas, chart recipes, worked examples, or review checklists from method guides. |
| AC9 | `README.md` links to `method-kits/README.md` without duplicating the detailed matrix. |
| AC10 | `docs/qcc-project-story.md` links to `method-kits/README.md` without duplicating the new detailed selector matrix. |
| AC11 | Verification records at least the representative scenarios from the proposal and shows that each scenario maps to a defensible method and limitation. |
| AC12 | Documentation checks or targeted inspection confirm no dead links were introduced by the selector. |

## Open questions

None.

The exact final wording of individual table cells may be refined during implementation as long as the stage relationships, input requirements, status rules, and guardrails in this specification are preserved.

## Next artifacts

- Spec review for this draft.
- Execution plan for the documentation implementation after spec approval.
- Test specification or verification checklist for links, structure, stage consistency, status consistency, duplication limits, and scenario review.

## Follow-on artifacts

- [Spec Review R1](../docs/changes/2026-07-13-qcc-method-selection-summary/reviews/spec-review-r1.md)

## Readiness

Approved for architecture assessment and execution planning.

This specification is approved.
It is not an execution plan, test specification, implementation evidence, or verification evidence.
