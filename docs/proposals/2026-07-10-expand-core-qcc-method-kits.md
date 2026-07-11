# Expand Core QCC Method Kits

## Status

accepted

## Problem

QCC Toolkit now has official Markdown-first method kits for Pareto Chart, Flowchart / Process Map, Histogram, and Scatter Diagram.
The QCC project story still depends on Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H, but those methods currently remain on the older optional-aid guide surface.
That creates an uneven user journey: teams can learn several chart and diagram outputs through the newer method-kit standard, but the methods that collect observations, organize cause hypotheses, test causal chains, and turn countermeasures into concrete actions are not yet promoted to the same evidence-oriented guide format.

The next method expansion should close that workflow gap without turning the repository into a generic quality-method encyclopedia, a statistical platform, or a tool-specific template collection.

## Goals

- Promote the next core QCC methods into official Markdown-first method kits.
- Preserve the best-practice pattern that each method starts from the QCC project question, not from a chart or software tool.
- Strengthen evidence flow from problem framing through current-state grasp, cause analysis, and countermeasure planning, with explicit handoffs to verification and standardization methods.
- Make interpretation limits explicit so teams do not treat data collection, cause brainstorming, causal chains, or action planning as stronger evidence than they are.
- Keep manual chart, worksheet, and diagram creation guidance central and tool-neutral.
- Add focused review checks so method guides can be inspected for required sections, cautions, evidence-note expectations, links, canonical-source behavior, and out-of-scope guardrails.

## Non-goals

- Do not add Control Chart, SPC rules, control-limit calculations, run-rule interpretation, or process capability in this proposal.
- Do not add broad statistical automation or new chart-rendering backends.
- Do not create named-tool tutorials for spreadsheets, presentation software, statistics packages, diagramming tools, or programming languages as the primary guide surface.
- Do not keep duplicate full method guidance in both `method-kits/` and legacy `docs/methods/` pages after a method kit becomes canonical.
- Do not restore legacy `docs/methods/` pages as compatibility notices.
- Do not leave live navigation, catalog, tests, or documentation pointing to deleted `docs/methods/` files.
- Do not redefine QCC stages, evidence levels, chart-quality standards, or the project vision.
- Do not add CAPA, EQMS, dashboard, release, or hosted workflow functionality.

## Vision fit

fits the current vision

This proposal extends the current Markdown-first method-guide direction recorded in root `VISION.md`.
It keeps method knowledge, chart-quality expectations, interpretation cautions, and review criteria in Markdown.
It treats optional templates and automation as secondary aids.
It also preserves the rule that generated or illustrative visuals can teach concepts but cannot become final quantitative project evidence.

## Context

The current README exposes official method kits for Pareto Chart, Flowchart / Process Map, Histogram, and Scatter Diagram.
The project story guide still names Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H as typical QCC methods across problem selection, current-state grasp, cause analysis, countermeasure planning, and verification.

The prior seven basic quality tools expansion deliberately added Flowchart, Histogram, and Scatter Diagram while excluding Control Chart and SPC automation.
That exclusion remains sound because control-limit logic and stability claims need tighter interpretation safeguards than a broad method-kit expansion should absorb.

The repository previously contained legacy optional-aid method guides for Check Sheet, Fishbone Diagram, 5 Whys, 5W2H, and Pareto Chart under `docs/methods/`.
Their key content has been extracted to `docs/methods-key-content.md`, and the team has decided to delete the old guide files rather than retain compatibility notices.
The official method-kit surface should follow the newer Markdown-first structure and should not inherit PowerPoint-first framing as the primary user experience.
Because deletion breaks any live references to `docs/methods/`, the downstream specification must govern reference updates for template catalog entries, project-story navigation, tests, and documentation that still cite those removed paths.

## Options Considered

| Option | Core idea | Value | Cost | Decision |
|---|---|---|---|---|
| O0: Defer new methods | Keep the current four official method kits and leave legacy guides as-is. | No new scope or maintenance burden. | Leaves major QCC story gaps in the official guide surface. | Rejected because users still need evidence-quality guidance for data collection, cause analysis, and countermeasure planning. |
| O1: Promote one method only | Add Check Sheet as the next official method kit. | Smallest useful slice; improves upstream data quality for Pareto, Histogram, and verification. | Does not address cause-analysis and action-planning gaps. | Accepted as the first implementation slice, but not enough as the whole product direction. |
| O2: Promote four core workflow methods | Add Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H as official method kits. | Covers the main non-SPC gaps in the QCC story while staying method-guide centered. | Requires careful consistency checks across four guides and references formerly pointing to `docs/methods/`. | Recommended and accepted. |
| O3: Add sustaining methods too | Add the four core methods plus Standard Work / Visual Control / Monitoring Plan. | Better covers standardization and control. | Larger scope and may require clearer boundaries between QCC method guidance and operational management practice. | Deferred as a separate sustainment-method follow-up. |
| O4: Add Control Chart/SPC next | Add Control Chart, control limits, and stability interpretation. | High user value for verification and control when done well. | High risk of incorrect claims, likely architecture and statistical validation needs. | Rejected for this proposal; route through a separate proposal/spec when ready. |

## Recommended Direction

Create official Markdown-first method kits for four core QCC workflow methods:

```text
method-kits/check-sheet.md
method-kits/fishbone-diagram.md
method-kits/five-whys.md
method-kits/five-w-two-h.md
```

The recommended implementation order is:

1. Check Sheet
2. Fishbone Diagram and 5 Whys
3. 5W2H

Check Sheet should be the first implementation slice because the quality of later analysis depends on the quality of collected observations.
Fishbone Diagram and 5 Whys should be authored as separate guides but reviewed together because users need a clear explanation of how the two methods differ and connect.
5W2H should follow to make problem framing and countermeasure planning concrete, including owner, timing, dependencies, verification approach, expected evidence, and assumptions.

Standard Work, Visual Control, and Monitoring Plan remain a deferred follow-up.
The current method kits should include explicit handoffs to verification, standardization, and sustainment, but they should not attempt to define those practices fully.
A later proposal should decide whether these become separate guides or one coherent sustainment-method slice.

Control Chart/SPC should remain a separate proposal because it would introduce stronger statistical interpretation and potential calculation contracts.

## Expected Behavior Changes

- The repository gains official method-kit files for Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H under `method-kits/`.
- README method-kit navigation and `docs/qcc-project-story.md` point users to the new method kits in the QCC stages where they fit.
- Legacy `docs/methods/` files are not retained as compatibility notices.
- Extracted legacy content remains available in `docs/methods-key-content.md` as source material for the new method kits.
- The same method guidance is not maintained independently in both `method-kits/` and legacy `docs/methods/` pages.
- Primary navigation favors the official method kits and does not link to deleted legacy pages.
- Each new guide follows the established method-kit structure: summary, stage fit, method question, use and non-use guidance, inputs, output, manual recipe, quality standards, interpretation limits, common mistakes, evidence note, review checklist, image-assisted demonstration notes, and related methods.
- Focused local checks verify guide structure, method-specific cautions, expected navigation links, deleted-reference cleanup, canonical-source behavior, and out-of-scope guardrails.

Expected deleted legacy paths and replacement targets are:

| Deleted legacy path | Replacement target |
|---|---|
| `docs/methods/check_sheet.md` | `method-kits/check-sheet.md` |
| `docs/methods/fishbone_diagram.md` | `method-kits/fishbone-diagram.md` |
| `docs/methods/5_whys.md` | `method-kits/five-whys.md` |
| `docs/methods/5w2h.md` | `method-kits/five-w-two-h.md` |
| `docs/methods/pareto_chart.md` | `method-kits/pareto-chart.md` |

The feature specification must require updates for any live references to those removed paths, including `templates/ppt/catalog.yml`, `docs/qcc-project-story.md`, existing tests, and durable docs whose present-tense claims would otherwise remain false.

Optional images and prompt records should use method-scoped media paths only when a reviewed visual is actually included:

```text
media/check-sheet/
media/fishbone-diagram/
media/five-whys/
media/five-w-two-h/
```

Do not create empty media directories.

## Method-specific safeguards

| Method | Required guidance | Output boundary |
|---|---|---|
| Check Sheet | Distinguish a check sheet from a generic checklist; require a clear observation purpose, operational definitions, observation period and scope, relevant location, shift, product, or process context, understandable categories, rules for blank, unknown, and other observations, sampling or coverage guidance, a short pilot before full collection, and handoff to stratification, Pareto, Histogram, or another analysis method. | Structured observation data, not a conclusion and not a verified cause. |
| Fishbone Diagram | Require one precise effect or problem statement at the head, context-appropriate categories without mandatory reliance on one model such as 6M, explicit separation of observed facts from proposed causes, evidence status such as observed, plausible, unknown, or requires verification, and prioritization of causes for further checking. | Structured cause hypotheses, not verified root cause. |
| 5 Whys | State that exactly five questions are not required, one linear chain may be insufficient, branches are acceptable when several mechanisms are plausible, each answer should be supported by facts or marked for verification, personal blame should be avoided, the stopping point should be an actionable system or process cause supported by evidence, and the final chain remains provisional until checked. | Causal hypothesis chain with verification status, not proof by repetition. |
| 5W2H | Support problem-framing mode and action-planning mode. Problem-framing mode clarifies what happened, why it matters, where, when, who is affected or involved, how it appears, and how much impact exists. Action-planning mode defines what will be done, why, where, when, by whom, how, and with how much cost, effort, resource, or expected effect. Require owner, due date, dependencies, verification measure, expected evidence, target or acceptance condition, assumptions, and constraints where relevant. | Clarity for framing or action planning; it does not replace root-cause analysis or prove that an action worked. |

## Visual policy

Visuals are optional and method-specific.
Do not require a generated image for every guide.

| Method | Visual recommendation | Reason |
|---|---|---|
| Check Sheet | No generated image initially. | A worked table and annotated Markdown example are more useful and precise. |
| Fishbone Diagram | One conceptual visual recommended. | The spatial structure is central to understanding the method. |
| 5 Whys | Optional good-versus-bad chain visual. | It may help contrast fact-grounded analysis with speculation, but a Markdown table may be sufficient. |
| 5W2H | No generated image initially. | A two-mode table and worked example communicate the method better. |

For Fishbone, a conceptual visual should show the defined effect, major cause branches, example subcauses, visual distinction between facts and hypotheses, and an indication that causes require verification.
For 5 Whys, any visual should emphasize facts versus assumptions, branching when needed, verification status, and no requirement to stop at exactly five questions.

Generated visuals should remain conceptual, text-light, reviewed, and clearly not evidence.
They should never contain invented project evidence or exact quantitative conclusions.

## Architecture Impact

The preferred architecture impact is limited to the Markdown method-guide boundary, navigation docs, method-scoped media when used, deletion of legacy guide paths, reference cleanup, and documentation validation tests.

No new runtime architecture is expected for the recommended direction.
The proposal does not require new Python public APIs, statistical calculation modules, rendering backends, data schemas, persistent storage, network calls, telemetry, or external services.

An architecture note should be conditional, not mandatory.
It is only needed if the downstream specification changes durable repository boundaries, metadata contracts, automation interfaces, media conventions, or compatibility policy beyond the deleted-path policy accepted here.
Because this proposal now accepts deleting the legacy guide paths rather than preserving compatibility notices, the downstream feature specification should explicitly decide whether that deletion is still inside the existing Markdown-first architecture or whether a short architecture note is needed to record the boundary change.

If later slices add automation for any of these methods, that work should receive a separate spec and architecture assessment because method contracts, data validation, evidence metadata, and report artifacts would become compatibility surfaces.

## Testing and Verification Strategy

The downstream spec should define focused documentation checks before implementation.
The main proof should be content-focused:

| Verification area | Required proof |
|---|---|
| Guide completeness | Every required section exists and contains meaningful guidance. |
| Method correctness | A qualified reviewer confirms that the method is described accurately. |
| Interpretation safety | The guide does not overclaim causation, improvement, or verification. |
| Navigation | README, project story, and related-method links resolve correctly. |
| Deleted references | No live navigation, catalog, test, or present-tense documentation relies on deleted `docs/methods/` files. |
| Canonical source | Official method kits are the only full method-guide source for promoted methods; extracted legacy content is source material, not a parallel guide surface. |
| User task | A representative user can apply the method using the guide. |
| Reviewer task | A facilitator can evaluate the result using the included checklist. |
| Visual policy | Any generated image is conceptual, reviewed, text-light, and clearly not evidence. |

Repository-wide Python, Ruff, and type-checking commands should run only when required by existing repository governance or when related code changes.
They are not the main proof for this documentation-centered change.

## Rollout and Rollback

Rollout includes additive method-kit and navigation changes plus deletion-aware reference cleanup.
Each new method kit should be introduced with updates to any catalog, navigation, test, and documentation references that previously pointed at the deleted legacy file.
The Check Sheet slice should establish the first quality bar before patterns are copied across the other three methods.

Rollback can remove the new method-kit files, navigation entries, prompt records, media links, and focused checks.
If rollback needs the old method content, it should use `docs/methods-key-content.md` as the extraction source instead of assuming deleted `docs/methods/` files remain available.
No data migration is expected.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Method sprawl | The toolkit becomes a loose encyclopedia of quality terms. | Limit this proposal to methods already present in the QCC project story and legacy guide surface. |
| End-to-end overclaiming | The four methods may be presented as completing verification or standardization. | State that they provide handoffs to verification and standardization rather than fully defining those later practices. |
| Broken references after deletion | Catalog, navigation, tests, or documentation may still point to removed `docs/methods/` files. | Require the feature spec and implementation to update or remove every live reference to deleted legacy paths. |
| Lost legacy guidance detail | Useful wording from deleted guides may not reach the new method kits. | Use `docs/methods-key-content.md` as source material during spec and implementation. |
| Overclaiming causes | Users may treat Fishbone or 5 Whys outputs as verified root cause. | Require interpretation limits and evidence-status guidance that separate hypotheses from checked facts. |
| Weak data collection guidance | Check Sheets may be treated as simple forms without sampling, category, location, or period discipline. | Require clear data-collection scope, category definitions, observation rules, pilot collection, and review checks. |
| Tool-specific drift | Guides may become spreadsheet, slide, or template tutorials. | Keep method kits tool-neutral and route tool-specific aids to secondary surfaces. |
| Generated-image misuse | Teaching visuals could be mistaken for project evidence. | Keep generated visuals optional, conceptual-only, text-light, reviewed, and linked to prompt records when used. |
| Scope creep into SPC | Control Chart or capability concepts may leak into verification guidance. | Keep SPC and process capability explicitly out of scope and route them to a separate proposal. |

## Resolved questions

| ID | Question | Decision |
|---|---|---|
| RQ1 | Should Standard Work / Visual Control / Monitoring Plan be part of the same change? | No. Treat them as a separate sustainment-method follow-up. The current guides should provide handoffs to verification and standardization without fully defining those practices. |
| RQ2 | What should happen to the legacy `docs/methods/` pages? | Delete the legacy guide files rather than retaining compatibility notices. Preserve extracted key content in `docs/methods-key-content.md`, and require downstream cleanup of live references to deleted paths. |
| RQ3 | Which teaching visuals are necessary? | Require none by default. Recommend one conceptual Fishbone visual, make a 5 Whys good/bad visual optional, and use worked Markdown examples rather than generated images for Check Sheet and 5W2H. |
| RQ4 | Should Check Sheet be implemented before the other methods? | Yes. Use Check Sheet as the first implementation slice, followed by Fishbone and 5 Whys, then 5W2H. |

## Downstream specification details

| ID | Detail |
|---|---|
| DQ1 | Exact heading order and front matter for the four method files. |
| DQ2 | Exact Check Sheet operational-definition and sampling guidance. |
| DQ3 | Exact hypothesis and evidence-status notation for Fishbone and 5 Whys. |
| DQ4 | Exact two-mode structure for 5W2H. |
| DQ5 | Exact user-task and reviewer-task acceptance scenarios. |
| DQ6 | Exact replacement or removal behavior for every live reference to deleted `docs/methods/` paths, including template catalog, project-story links, tests, and present-tense documentation. |
| DQ7 | Exact media-path and prompt-record behavior if optional visuals are included. |

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate a proposal for creating new quality management methods | in scope | Problem, Recommended Direction, Expected Behavior Changes |
| Follow best practices for method creation | in scope | Goals, Method-specific safeguards, Testing and Verification Strategy, Risks and Mitigations |
| Preserve QCC Toolkit's Markdown-first identity | in scope | Vision fit, Non-goals, Architecture Impact |
| Decide which quality management methods should come next | in scope | Options Considered, Recommended Direction, Scope budget |
| Incorporate targeted review amendments from July 10, 2026 | in scope | Status, Goals, Method-specific safeguards, Resolved questions, Next Artifacts |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Check Sheet method kit | first-slice candidate | Highest upstream value because better observation data improves later charts and verification. |
| Fishbone Diagram method kit | core to this proposal | Fills the main cause-hypothesis organization gap. |
| 5 Whys method kit | core to this proposal | Complements Fishbone by testing one likely causal chain with fact checks. |
| 5W2H method kit | core to this proposal | Connects problem framing and countermeasure planning to reviewable action detail. |
| README and QCC project-story navigation | same-slice dependency | New official method kits need discoverable workflow placement. |
| Deleted legacy reference cleanup | same-slice dependency | Deleting `docs/methods/` files requires catalog, navigation, tests, and present-tense docs to stop relying on those paths. |
| Focused documentation checks | same-slice dependency | Method-guide structure, canonical links, deleted-reference cleanup, and cautions need durable proof. |
| Conceptual teaching images and prompt records | separate implementation slice | Useful where they improve comprehension, but not required by default for every method. |
| Standard Work / Visual Control / Monitoring Plan | deferable follow-up | Valuable for standardization, but broader than the current core method-kit gap. |
| Control Chart, SPC rules, and process capability | separate proposal | Higher interpretation and calculation risk requires separate proposal/spec/architecture treatment. |
| Automation or chart rendering for new methods | separate proposal | Would create method contracts, data validation, output, and compatibility surfaces beyond this guide expansion. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-10 | Draft proposal recommended four core method kits: Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H. | These methods fill the largest QCC story gaps while staying aligned with Markdown-first, tool-neutral guidance. | Defer all new methods; add Control Chart/SPC now; add broad quality-management encyclopedia scope. |
| 2026-07-10 | Review verdict accepted the proposal after targeted amendments. | The method set and scope were sound, but the proposal needed clearer lifecycle scope, method safeguards, legacy-source policy, and downstream artifact routing. | Leave open questions unresolved; keep duplicate legacy guidance; require architecture and test-spec artifacts by default. |
| 2026-07-10 | Check Sheet was selected as the first implementation slice. | Later analysis quality depends on reliable observation data. | Implement all four methods in one large slice. |
| 2026-07-10 | Legacy pages will be deleted rather than retained as compatibility notices. | The team chose deletion to avoid preserving old guide paths; extracted key content remains available as source material in `docs/methods-key-content.md`. | Keep full duplicate legacy guidance; restore legacy paths as notices. |
| 2026-07-10 | Standard Work, Visual Control, and Monitoring Plan remain a deferred follow-up. | They matter for sustainment but are a distinct product slice from promoting the four core legacy methods. | Include them in this method-kit expansion. |
| 2026-07-10 | Control Chart/SPC remains a separate proposal. | Stability claims, control-limit logic, and run rules need stronger safeguards than this broad method-guide expansion. | Include SPC in this proposal. |

## Next Artifacts

- Feature specification for the four-method expansion, including acceptance checks, deleted-reference cleanup, and use of extracted legacy content.
- Execution plan after the feature specification is accepted.
- Conditional architecture note if the specification concludes deletion of legacy guide paths changes durable repository boundaries, metadata contracts, or automation interfaces.

## Follow-on Artifacts

None yet.

## Readiness

Ready for feature specification.
