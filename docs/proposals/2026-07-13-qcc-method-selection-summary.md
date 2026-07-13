# Proposal: Create a QCC Method Selection Summary

## Status

accepted

This proposal records a recommended direction for creating a concise, stage-aware QCC method-selection summary.
It is an accepted decision.
It is not a specification, an implementation plan, or verification evidence.

## Problem

QCC Toolkit is expanding from individual Markdown method guides into a broader method library.
Users need a fast way to determine which method is appropriate at a given point in a QCC project without opening every method guide or relying on prior quality-management experience.

A method list alone does not solve this problem.
Several QCC methods can support the same stage, and one method can support several stages.
A stage-only matrix can therefore become rigid or misleading, while a method-only index does not explain why a method should be selected.

The repository needs one concise, canonical summary that helps users select a method using three factors:

```text
QCC stage
+ project question
+ available evidence or input
```

The summary should guide users to the detailed method files while preserving interpretation limits.
It should not become a second source of full method instructions, a generic quality-method encyclopedia, or an automated recommendation engine.

## Goals

| ID | Goal |
|---|---|
| G1 | Create one canonical QCC method-selection summary under `method-kits/README.md`. |
| G2 | Help users select methods using QCC stage, immediate project question, and available evidence or input. |
| G3 | Provide both a stage-oriented view and a project-question-oriented view. |
| G4 | Distinguish each method's primary use from supporting uses instead of assigning one rigid stage. |
| G5 | Show whether a method guide is available, planned, deferred, or advanced. |
| G6 | Include concise interpretation guardrails so the selector does not encourage unsupported conclusions. |
| G7 | Link users to the canonical detailed method guide rather than duplicating full procedures. |
| G8 | Keep the summary Markdown-first, tool-neutral, concise, and easy to maintain. |
| G9 | Establish a maintenance rule so every method addition, rename, or status change updates the summary. |
| G10 | Verify the selector with representative user and reviewer scenarios before treating it as complete. |

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not add or implement new QCC methods through this proposal. |
| NG2 | Do not reproduce full method procedures, formulas, chart recipes, worked examples, or review checklists in the summary. |
| NG3 | Do not define a new QCC stage model or organization-specific terminology system. |
| NG4 | Do not require every method to belong to only one stage. |
| NG5 | Do not prescribe a specific charting, spreadsheet, presentation, statistical, or programming tool. |
| NG6 | Do not build an interactive wizard, recommendation algorithm, web interface, or automated method-selection engine in this slice. |
| NG7 | Do not add Control Chart, SPC, process capability, or other advanced statistical guidance beyond status and handoff labels. |
| NG8 | Do not create a separate catalog or metadata schema unless a later need for automation or generated navigation is demonstrated. |
| NG9 | Do not maintain the same stage-method matrix independently in multiple files. |

## Vision fit

fits the current vision

The current project direction uses QCC stage workflow as the organizing frame for method guidance and treats Markdown as the primary user-facing surface.
A concise method-selection summary makes those principles actionable without introducing a new product identity, runtime architecture, or tool-specific workflow.

The proposal also supports the evidence-quality principle that users should select a method based on the question being answered and the available evidence, not because a chart or template is familiar.

## Context

The accepted Markdown-first direction establishes that method knowledge should be expressed through clear Markdown guides, image-assisted teaching should remain conceptual, and manual method or chart guidance should remain tool-neutral.

Related method-expansion work covers or proposes coverage for:

- Pareto Chart;
- Flowchart / Process Map;
- Histogram;
- Scatter Diagram;
- Check Sheet;
- Fishbone Diagram;
- 5 Whys;
- 5W2H.

Control Chart and formal SPC remain separate because stability claims, control-limit logic, sampling assumptions, and run-rule interpretation require stronger safeguards.
Standard Work, Visual Control, and Monitoring Plan remain later sustainment guidance.

As the number of method guides grows, navigation by file name alone becomes less useful.
Users need a short decision aid that answers two common entry questions:

1. "Which method fits my current QCC stage?"
2. "Which method answers the question I have right now?"

The selector should support both entry paths and direct users to one canonical detailed guide per method.

## Options considered

| Option | Description | Benefits | Costs and risks | Decision |
|---|---|---|---|---|
| O0: Keep only a flat method index | List methods alphabetically with links. | Smallest maintenance burden. | Does not help users choose; assumes prior method knowledge. | Rejected. |
| O1: Stage-only matrix | Map methods to QCC stages in one table. | Familiar QCC-story structure; easy to scan. | Too rigid; several methods span stages; does not start from the user's immediate question. | Rejected as incomplete. |
| O2: Question-only selector | Map project questions directly to methods. | Practical for new users; decision-oriented. | Does not show QCC story placement or supporting-stage use. | Rejected as incomplete. |
| O3: Combined stage and question selector | Provide a quick question table, stage table, method status, and interpretation guardrails. | Balances discoverability, QCC workflow, flexibility, and safety. | Requires disciplined maintenance and careful wording. | Recommended. |
| O4: Interactive recommendation wizard | Ask users questions and automatically recommend methods. | Could become highly usable later. | Premature; introduces product logic, maintenance, and validation burden before the written selection model is proven. | Deferred follow-up. |
| O5: Full method encyclopedia | Put definitions and abbreviated procedures for every method in one summary. | Everything appears in one place. | Duplicates canonical guides, becomes long, and creates drift. | Rejected. |

## Recommended direction

Proceed with O3: create a single Markdown selection guide at:

```text
method-kits/README.md
```

The guide should be the canonical navigation and selection surface for the method library.
The root `README.md` and any QCC project-story document should link to it rather than maintaining separate copies of the same matrix.

The selector should use this decision model:

```text
1. Identify the current QCC stage.
2. State the immediate project question.
3. Confirm the evidence or input available.
4. Select the method that answers that question with those inputs.
5. Open the detailed method guide before applying it.
6. Preserve the method's interpretation limits when reporting the result.
```

### Recommended summary sections

| Section | Purpose |
|---|---|
| Introduction | Explain that stage, question, and available evidence should be considered together. |
| Quick selection by project question | Help users start from the immediate question they need to answer. |
| Selection by QCC stage | Show primary methods, supporting methods, expected output, and key limitation by stage. |
| Method status | Distinguish available, planned, deferred, and advanced guidance. |
| Selection guardrails | Prevent prioritization, association, brainstorming, or planning outputs from being overclaimed as proof. |
| Detailed method links | Link only to canonical method files that exist. |
| Maintenance note | Define how additions, renames, stage changes, and status changes update the summary. |

### Selection dimensions

The stage view should not present one method as mandatory for one stage.
It should use terms such as:

```text
Primary use
Supporting use
Typical output
Important limitation
```

The question view should use practical prompts such as:

| Project question | Method direction |
|---|---|
| How should observations be collected consistently? | Check Sheet |
| How does the process actually flow? | Flowchart / Process Map |
| Which categories contribute most to the problem? | Pareto Chart |
| What does the distribution of numeric data look like? | Histogram |
| Do two measured variables appear related? | Scatter Diagram |
| What possible causes should be investigated? | Fishbone Diagram |
| How might one suspected causal chain work? | 5 Whys |
| How should the problem or action be made concrete? | 5W2H |

These rows are directional navigation, not a substitute for the detailed guide.

### Interpretation guardrails

The selector should include concise boundaries for safe use:

| Method | Safe interpretation boundary |
|---|---|
| Check Sheet | Records observations; does not prove cause. |
| Flowchart / Process Map | Shows process sequence and handoffs; does not prove which step caused the problem. |
| Pareto Chart | Prioritizes recorded categories; does not prove root cause. |
| Histogram | Shows distribution and variation; does not prove process stability. |
| Scatter Diagram | Shows an apparent relationship; does not prove causation. |
| Fishbone Diagram | Organizes cause hypotheses; does not verify them. |
| 5 Whys | Develops a fact-checked causal hypothesis chain; asking repeatedly does not itself prove root cause. |
| 5W2H | Clarifies a problem or action; does not prove that the action will work or has worked. |

### Method status

The selector should clearly distinguish:

```text
Available
Planned
Deferred / advanced
Future sustainment guidance
```

Only existing method files should be linked.
Planned or deferred methods should be shown as plain text with a visible status label until a canonical guide exists.

## Expected behavior changes

| ID | Expected behavior change |
|---|---|
| B1 | Users can open `method-kits/README.md` and identify a suitable method without inspecting every guide. |
| B2 | Users can start from either their QCC stage or their immediate project question. |
| B3 | Users understand that several methods may support the same stage and that one method may support several stages. |
| B4 | Users can distinguish available guides from planned, deferred, or advanced guidance. |
| B5 | Users are directed to the canonical method file before applying a method. |
| B6 | Users see the main interpretation limitation before selecting a method. |
| B7 | Root navigation and QCC project-story navigation point to one canonical selection summary. |
| B8 | Contributors update one summary when method availability, naming, or stage fit changes. |
| B9 | Reviewers can evaluate whether a selected method fits the project question and available evidence. |

## Architecture impact

The recommended change is documentation-only and should not introduce runtime architecture.

Expected touched boundaries:

```text
method-kits/README.md
README.md
optional link from docs/qcc-project-story.md
optional documentation checks
```

The proposal does not require:

- a runtime method registry;
- a metadata sidecar;
- a generated catalog;
- a database;
- a recommendation engine;
- chart-generation code;
- external services.

If later work introduces generated navigation, filtering, or an interactive selector, that change should receive separate specification and architecture review because the method-stage mapping would become a durable machine-readable contract.

## Testing and verification strategy

Verification should focus on selection usefulness, consistency, safety, and navigation.

| Test area | Strategy |
|---|---|
| Structure review | Confirm the summary includes question view, stage view, status, guardrails, and detailed links. |
| Link checks | Confirm every linked method file exists and every root/project-story link resolves. |
| Stage consistency review | Compare stage names and method fit against the canonical QCC story and detailed method guides. |
| Status consistency review | Confirm available, planned, and deferred labels match actual repository state. |
| Duplication review | Confirm full procedures and checklists remain in method files rather than being duplicated in the selector. |
| Interpretation-safety review | Confirm the summary does not present prioritization, association, hypothesis generation, or action planning as causal or effectiveness proof. |
| User task test | Give representative users short QCC scenarios and confirm they can choose an appropriate method and explain why. |
| Reviewer task test | Ask a QCC facilitator or reviewer to assess whether the selection and stated limitation are defensible. |
| Maintenance test | Add or rename a sample method in a review fixture and confirm the expected summary update is clear. |

Representative user scenarios should include at least:

- collecting inconsistent defect observations;
- locating handoffs or rework in a process;
- prioritizing defect categories;
- understanding numeric variation;
- exploring a possible variable relationship;
- organizing possible causes;
- examining one suspected causal chain;
- defining a countermeasure action.

The selector should be considered successful only when users choose a defensible method without inferring a stronger conclusion than the method supports.

## Rollout and rollback

### Rollout

1. Draft `method-kits/README.md` using the accepted method names and canonical QCC stage terminology.
2. Add the quick question view, stage view, status table, guardrails, and existing method links.
3. Link the root `README.md` to the selector.
4. Link the QCC project-story guide to the selector if that guide exists.
5. Review the selector with at least one representative user and one QCC reviewer.
6. Adjust wording based on selection errors, ambiguity, or overclaiming found during review.
7. Treat the selector as canonical only after review is complete.

### Rollback

Rollback is additive and low risk.
If the selector proves confusing, remove or revise `method-kits/README.md` and restore the prior root navigation.
Individual method guides remain unchanged.
No data migration, runtime rollback, or compatibility migration is expected.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Stage-only thinking | Users assume one method belongs to only one stage. | Combine stage and project-question views; use primary and supporting use labels. |
| Oversimplified selection | Users choose a method without checking required inputs or limitations. | Require the selector to link to the full guide and mention available evidence as part of the decision model. |
| Method overclaiming | Users treat Pareto, Scatter, Fishbone, or 5 Whys as proof. | Put concise interpretation limits directly in the summary. |
| Duplicate sources of truth | README, project story, and method selector drift apart. | Keep one canonical matrix in `method-kits/README.md`; other documents link to it. |
| Stale status | Planned methods appear available or removed methods remain linked. | Update the selector in the same change as every method addition, rename, move, or retirement. |
| Dead links | Planned methods are linked before their guide exists. | Link only available method files; show future methods as status text. |
| Summary becomes too long | Users stop using it as a selector. | Keep procedures, examples, formulas, and full checklists in detailed guides. |
| Method sprawl | The summary becomes a broad quality encyclopedia. | Include only methods accepted into the QCC project-story scope. |
| Organizational terminology differences | Users may use different stage labels. | Use canonical stage names and allow local terminology to be explained elsewhere, not duplicated in the selector. |
| Premature automation | A simple documentation need becomes a recommendation engine. | Defer machine-readable catalogs and interactive selection until user-tested written guidance is stable. |

## Open questions

No proposal-level open questions remain.
The recommended direction, location, selection dimensions, and maintenance model are defined by this proposal.

The following downstream details should be resolved during content specification or drafting:

| ID | Downstream detail | Owner artifact |
|---|---|---|
| DQ1 | Exact wording and length of the quick-question table. | Method-selection summary specification. |
| DQ2 | Exact primary and supporting method mapping for each QCC stage. | Method-selection summary specification. |
| DQ3 | Actual available/planned/deferred status based on repository contents at implementation time. | Implementation review. |
| DQ4 | Exact user and reviewer scenarios used for acceptance. | Verification checklist. |
| DQ5 | Whether `docs/qcc-project-story.md` exists and should link to the selector in the same change. | Implementation plan. |

## Decision log

| Date | Decision | Reason | Alternatives rejected or deferred |
|---|---|---|---|
| 2026-07-13 | Propose one canonical method-selection summary at `method-kits/README.md`. | Keeps selection discoverable and avoids duplicate matrices. | Flat index only; duplicate summaries in several files. |
| 2026-07-13 | Combine stage, project question, and available evidence in the selection model. | Stage alone is too rigid and question alone loses QCC-story context. | Stage-only matrix; question-only selector. |
| 2026-07-13 | Include quick-question and stage-oriented views. | Supports both novice and experienced user entry paths. | One-view summary. |
| 2026-07-13 | Show method status and link only existing guides. | Prevents dead links and makes planned coverage visible. | Link future placeholder files. |
| 2026-07-13 | Keep interpretation limits in the selector. | Method selection can be unsafe when users overclaim what outputs prove. | Leave all cautions only in detailed guides. |
| 2026-07-13 | Defer interactive method selection and machine-readable catalogs. | The written selection model should be proven before becoming a durable software contract. | Interactive wizard or metadata-first implementation. |

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Create a summary for selecting QCC methods at different stages. | in scope | Problem, Goals, Recommended direction, Expected behavior changes |
| Follow best practices for the summary. | in scope | Options considered, Testing and verification strategy, Risks and mitigations |
| Keep the summary concise rather than creating many files. | in scope | Recommended direction, Architecture impact, Non-goals |
| Preserve the Markdown-first project direction. | in scope | Vision fit, Recommended direction |
| Help users choose methods safely. | in scope | Goals, Interpretation guardrails, Verification strategy |
| Avoid tool-specific identity and unnecessary automation. | in scope | Non-goals, Architecture impact, Decision log |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Canonical `method-kits/README.md` selector | core to this proposal | Primary user-facing change. |
| Quick selection by question | core to this proposal | Best entry point for users who do not know formal stage terminology. |
| Selection by QCC stage | core to this proposal | Preserves QCC project-story context. |
| Interpretation guardrails | same-slice dependency | Necessary to prevent unsafe method conclusions. |
| Method availability/status table | same-slice dependency | Prevents dead links and sets realistic expectations. |
| Root README link | same-slice dependency | Makes the selector discoverable. |
| QCC project-story link | first-slice candidate | Useful when the document exists and does not duplicate the matrix. |
| Documentation link and consistency checks | first-slice candidate | Provides durable proof without runtime architecture. |
| User and reviewer scenario testing | same-slice dependency | Verifies the selector is practical and safe. |
| Detailed method-guide changes | out of scope | This proposal selects and links methods; it does not rewrite them. |
| Machine-readable catalog | deferable follow-up | Useful only when automation or generated navigation is needed. |
| Interactive recommendation wizard | separate proposal | Creates new product behavior and validation requirements. |
| New QCC methods | separate proposal | Method expansion should remain independently reviewed. |

## Next artifacts

- Spec review for the method-selection summary specification.
- Execution plan after the summary specification is approved.
- Verification checklist for link, consistency, user-task, and reviewer-task checks.

## Follow-on artifacts

- [QCC Method Selection Summary Specification](../../specs/qcc-method-selection-summary.md)

## Readiness

Accepted and ready for downstream specification review.

This proposal is accepted, but it is not an implementation plan or verification evidence.
The next useful step is spec review for the method-selection summary specification rather than runtime architecture design.
