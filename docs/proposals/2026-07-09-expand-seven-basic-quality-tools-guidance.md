# Expand Seven Basic Quality Tools Guidance: Flowchart, Histogram, and Scatter Diagram

## Status

accepted

## Problem

QCC Toolkit now has a Markdown-first project-story guide and a complete Pareto method kit, but the method-kit surface does not yet cover the remaining common Seven Basic Quality Tools needed for a coherent QCC learning path.
Users can see that Flowchart, Histogram, Scatter Diagram, and Control Chart are future methods, but there is no accepted direction for which methods should come next or how to keep the expansion aligned with the Markdown-first product identity.

Adding methods without a proposal risks turning the repository into disconnected tool pages.
Adding the statistically heavier methods too early risks weak evidence guidance, unsafe interpretations, and automation pressure before manual chart-quality standards are mature.

## Goals

- Add a decision record for the next Seven Basic Quality Tools expansion.
- Prioritize Flowchart, Histogram, and Scatter Diagram as the next method-kit slice.
- Keep QCC project-story fit explicit for each method.
- Preserve Markdown method guides as the primary product surface.
- Preserve manual chart and diagram creation guidance as a core competency.
- Include necessary conceptual teaching images and prompt records that help users demonstrate each method idea and common chart or diagram defects.
- Define enough scope boundaries that Control Chart, named-tool tutorials, and automation do not slip into the first expansion slice.
- Prepare the direction for a behavior spec.

## Non-goals

- Do not implement the guides in this proposal.
- Do not add Control Chart in this slice.
- Do not add statistical process control rules, control-limit calculations, process capability, or run-rule automation yet.
- Do not build chart-rendering automation for Histogram or Scatter Diagram in this slice.
- Do not create named-tool tutorials for spreadsheets, presentation tools, statistics packages, or programming languages.
- Do not treat generated teaching images as final charts, quantitative evidence, or proof of method correctness.
- Do not require generated images for every subsection; include only images that materially improve method demonstration.
- Do not delete or rewrite older optional `docs/methods/` or PowerPoint assets as part of this proposal.
- Do not add web UI, dashboard, CAPA/EQMS workflow, release automation, hosted CI, or external services.

## Vision fit

fits the current vision

This proposal fits the current vision because `VISION.md` has been updated to the accepted Markdown-first direction.
It expands QCC method knowledge through Markdown-first method kits, tool-neutral chart and diagram recipes, evidence guidance, and review checklists.
It does not make a charting, presentation, statistics, or programming tool the center of the product.
It keeps generated images conceptual and keeps final data-dependent charts tied to source data, scope, assumptions, interpretation, and review status.

## Context

Current repository state:

- `docs/qcc-project-story.md` explains how QCC methods connect across problem selection, current-state grasp, cause analysis, countermeasure planning, verification, and standardization.
- `method-kits/pareto-chart.md` is the first complete Markdown-first method kit.
- `docs/methods/check_sheet.md`, `docs/methods/fishbone_diagram.md`, and `docs/methods/pareto_chart.md` exist as older optional method guides.
- `templates/ppt/` and `qcc_toolkit/` remain optional execution aids.
- No Control Chart support, advanced QCC methods, hosted CI, or release automation exists.

External quality-method references support the direction:

- ASQ lists Flowchart, Histogram, Scatter Diagram, Pareto Chart, Check Sheet, Fishbone, and Control Chart among common quality tools and templates.
- ASQ describes Flowchart as useful for representing process steps, Histogram for frequency distribution, and Scatter Diagram for relationships between input and output.
- JUSE publication listings frame QC circle work around problem solving, QC tools, task-achieving procedures, and control/improve methods.

Reference sources:

- ASQ Quality Tools: https://asq.org/quality-resources/quality-tools
- JUSE Publications in English: https://www.juse.or.jp/english/publications/
- JUSE QC Circle overview: https://www.juse.or.jp/english/qc/

The practical product implication is that QCC Toolkit should finish low-to-medium-risk Seven Basic Quality Tools guidance before taking on Control Chart.

Coverage model for this proposal:

- Pareto Chart already has a complete Markdown-first method kit.
- Check Sheet and Fishbone Diagram already have older optional method guides and templates, but they are not expanded by this proposal.
- Flowchart / Process Map, Histogram, and Scatter Diagram are the next new Markdown-first method-kit targets.
- Each new method should include necessary conceptual teaching images or good/bad examples when they materially improve user understanding.
- Control Chart remains outside this proposal because it needs separate SPC-specific treatment.

## Options Considered

| Option | Description | Benefits | Costs and risks | Verdict |
|---|---|---|---|---|
| O0. Do nothing | Keep only Pareto as a complete method kit and rely on older optional guides. | No near-term scope or review cost. | Method-kit model remains too thin; users still lack common method coverage. | Rejected. |
| O1. Add only Flowchart | Add a single non-statistical method kit first. | Lowest risk; strengthens current-state and process-understanding guidance. | Leaves data-chart gap for Histogram and Scatter Diagram. | Reasonable fallback. |
| O2. Add Flowchart, Histogram, and Scatter Diagram | Add the next three method kits as one related Seven Basic Quality Tools expansion slice. | Completes a useful low-to-medium-risk set before Control Chart; covers process flow, distribution, and relationship questions. | Broader review burden; Histogram and Scatter need careful interpretation limits. | Recommended. |
| O3. Add all remaining Seven Basic Quality Tools including Control Chart | Add Flowchart, Histogram, Scatter Diagram, and Control Chart together. | Most complete surface by name. | Control Chart brings statistical-control rules, sampling assumptions, false-signal risks, and likely architecture/test burden. | Rejected for first expansion. |
| O4. Build chart automation first | Add Python chart specifications and renderers before authoring the Markdown guides. | Could make later outputs reproducible. | Conflicts with current product focus; delays method guidance and increases tool identity risk. | Rejected. |
| O5. Add named spreadsheet tutorials | Create step-by-step named-tool recipes for the three methods. | May feel immediately practical to some users. | Violates current first-slice tool-neutral direction unless user testing proves need. | Deferred follow-up. |

Decision criteria:

- Fit with the Markdown-first vision.
- Contribution to the QCC project story.
- Manual creation teachability.
- Evidence and interpretation safety.
- Reviewability through local Markdown and link checks.
- Avoidance of premature automation or named-tool lock-in.
- Statistical risk suitable for the next slice.

## Recommended Direction

Proceed with O2: add Markdown-first method kits for Flowchart, Histogram, and Scatter Diagram as the next Seven Basic Quality Tools expansion slice.

The recommended sequence within the later spec and plan should be:

1. Flowchart / Process Map as the process-understanding method.
2. Histogram as the distribution and variation method.
3. Scatter Diagram as the relationship-exploration method.

Control Chart should be recorded as a separate follow-up proposal or later slice because it requires statistical-process-control guidance, control-limit behavior, sampling conditions, and stronger interpretation safeguards.

This proposal deliberately prioritizes method guidance and evidence habits over automation.
If later user testing shows that a specific chart is too hard to create manually, named-tool or Python-assisted recipes can be proposed separately.

## Expected Behavior Changes

Users should gain official Markdown-first guidance for:

- choosing Flowchart when the project question is about process sequence, handoffs, rework, decision points, or failure locations;
- choosing Histogram when the project question is about distribution, spread, shape, outliers, or before/after variation;
- choosing Scatter Diagram when the project question is about whether two measured variables appear related;
- understanding where each method fits in the QCC project story;
- manually creating each chart or diagram with reviewable source data or process facts;
- using conceptual images or good/bad examples to demonstrate the method idea and common visual defects;
- interpreting outputs safely without unsupported causal, stability, or improvement claims.

Reviewers should be able to check that each method guide includes method purpose, QCC stage fit, use and non-use conditions, required inputs, manual recipe, interpretation limits, evidence note expectations, common mistakes, review checklist, and related methods.
Reviewers should also be able to check that every generated image is conceptual-only, text-light, free of fake precise values, and linked to a reviewed prompt record.

Expected method-to-story fit:

| Method | Primary project-story use | Main user question | Primary output |
|---|---|---|---|
| Flowchart / Process Map | Current-state grasp and cause analysis preparation | How does the process actually flow, and where do handoffs, decisions, queues, rework, or failures occur? | Current-state process diagram with evidence notes. |
| Histogram | Current-state grasp and verification | How are numeric observations distributed, and did the spread or shape change after action? | Frequency distribution chart with sample, binning, and interpretation notes. |
| Scatter Diagram | Cause analysis and verification planning | Do two measured variables appear related enough to justify deeper investigation or controlled verification? | Paired-variable plot with causation and outlier cautions. |

Expected teaching-image set:

| Method | Necessary conceptual image | Purpose | Avoid |
|---|---|---|---|
| Flowchart / Process Map | Current-state process flow with start/end, steps, decisions, handoffs, queue, rework loop, and failure location. | Demonstrate how process sequence and handoffs become visible before cause analysis. | Tiny text, exact production names, private process details, decorative generic workflow art. |
| Flowchart / Process Map | Good versus weak process map comparison. | Show that boundaries, decisions, handoffs, and rework loops matter. | Treating the image as a complete SOP or verified process record. |
| Histogram | Conceptual distribution with bins, spread, outlier, and sample-size note. | Demonstrate distribution shape and variation without fake project values. | Exact counts, fake percentages, process-stability claims, misleading axes. |
| Histogram | Good versus weak histogram layout comparison. | Show bin-width, labeling, source note, and interpretation defects. | Overly precise numerical claims or before/after proof without evidence. |
| Scatter Diagram | Conceptual paired-variable plot with visible trend, outlier, and correlation-versus-causation caution. | Demonstrate relationship exploration and interpretation limits. | Regression claims, root-cause proof claims, fake correlation coefficients. |
| Scatter Diagram | Good versus weak scatter layout comparison. | Show axis labels, units, outlier handling, and causation warning. | Unsupported causal arrows or implied verified countermeasure effect. |

## Architecture Impact

Expected touched boundaries:

- Markdown method files under `method-kits/`, expected as `method-kits/flowchart.md`, `method-kits/histogram.md`, and `method-kits/scatter-diagram.md`.
- Method media and prompt records for necessary conceptual images under paths selected by the downstream spec, preferably a simple method-scoped structure such as `media/<method>/`.
- QCC project-story links in `docs/qcc-project-story.md`.
- README method-kit index.
- Lightweight front matter inside each method file.
- Optional metadata or catalog files only if the downstream spec decides they are necessary.
- Optional artifact consistency tests for method-kit structure and cross-links.

No runtime architecture change is expected for the recommended first expansion.
No calculation engine, renderer, report artifact, database, web UI, external service, or persistent data format should be required unless a later spec deliberately adds optional automation.

Architecture documentation may still be required by governance if the later spec changes durable method-kit repository boundaries, metadata schemas, public method registries, generated navigation, or evidence-level policy.

The downstream spec should keep the default repository shape simple:

```text
method-kits/flowchart.md
method-kits/histogram.md
method-kits/scatter-diagram.md
```

Generated bitmap assets should be created through the `imagegen` skill using the built-in image generation path by default, then persisted into the repository when they are project-bound.
Prompt records should preserve the final prompt, purpose, negative constraints, conceptual-only policy, output path, and review status.
Generated visuals must not imply final evidence, precise values, or validated project results.

## Testing and Verification Strategy

Likely proof should include:

- Markdown structure checks for all three method kits.
- Front-matter checks for method ID, method name, method type, QCC stages, status, guide version, image policy, and automation policy.
- Link checks from README, project-story guide, related-method sections, and method files.
- Text checks for tool-neutral guidance and absence of named-tool recipe commitments.
- Manual chart or diagram creation checks for purpose, inputs, data preparation, construction steps, quality standards, interpretation limits, common mistakes, evidence note, and review checklist.
- Prompt-record checks for purpose, intended use, final prompt, negative constraints, conceptual-only wording, output path, and review status.
- Teaching-image checks or manual review records confirming images are conceptual-only, text-light, non-private, and not usable as final quantitative evidence.
- Method-specific checklist checks:
  - Flowchart includes start/end points, process steps, decision points, handoffs, rework loops, and current versus future-state distinction.
  - Histogram includes numeric data, binning/bin-width caution, sample size caution, distribution shape, outliers, and no process-stability claim.
  - Scatter Diagram includes paired numeric observations, axis labeling, correlation-versus-causation caution, outlier handling, and no root-cause proof claim.
- Evidence-note checks requiring source data or process facts, date range or observation period, scope, assumptions, interpretation, reviewer, and review status.
- Focused pytest for changed documentation surfaces.
- Full local pytest, Ruff, mypy when implementation touches tests or package code.

Manual review should be used for all generated teaching visuals.
Generated images remain conceptual aids only and cannot be used as final chart evidence.

## Rollout and Rollback

Rollout:

- Write a spec for the three-method expansion.
- Add architecture only if the spec changes durable boundaries, metadata contracts, generated navigation, or optional automation responsibilities.
- Implement the methods in small reviewable slices, preferably one method kit per implementation milestone.
- Generate necessary conceptual teaching images after the guide text and review criteria for each method are stable.
- Store each image with a matching prompt record and review note before linking it from the method guide.
- Keep Control Chart as a named follow-up, not a hidden extra milestone.

Rollback:

- If the proposal is rejected, archive it and make no product changes.
- If a later implementation proves too broad, reduce the slice to Flowchart first and defer Histogram and Scatter Diagram.
- If Histogram or Scatter Diagram guidance cannot meet evidence-quality expectations without automation, keep the Markdown guide draft and route automation through a separate proposal.
- If an image is misleading, too text-heavy, or could be confused with evidence, remove or replace it while keeping the written method guide authoritative.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Seven Basic Quality Tools framing could imply Control Chart is included now. | Use an "expand guidance" title and defer Control Chart explicitly. |
| Histogram guidance may create false confidence from weak sample sizes or poor bin choices. | Require sample-size, binning, outlier, and interpretation cautions in the later spec. |
| Scatter Diagram guidance may be misread as causal proof. | Require correlation-versus-causation and outlier cautions in the later spec. |
| Flowchart guidance could become generic process-mapping content detached from QCC. | Tie it to current-state grasp, failure-location discovery, handoff/rework analysis, and verification planning. |
| Adding three methods at once could be too broad. | Plan one method kit per implementation milestone and allow fallback to Flowchart-only. |
| Optional automation may creep into the slice. | Keep Python/chart rendering out of scope unless a later accepted proposal adds it. |
| Named-tool tutorials may crowd out tool-neutral guidance. | Keep named tools deferred until user testing proves a specific recipe is necessary. |
| Generated images may look authoritative even when they are only conceptual. | Require prompt records, conceptual-only labels, negative constraints, and manual review before linking images. |
| Image text may be inaccurate or unreadable. | Keep generated visuals text-light and carry detailed instructions in Markdown. |
| Image generation could accidentally include fake data or private-looking details. | Prompts must forbid exact data values, fake percentages, private names, credentials, and production-specific identifiers. |
| Source data or process details may be sensitive. | Evidence guidance should record context without requiring users to expose unnecessary private raw rows. |

## Resolved Questions

| ID | Question | Decision |
|---|---|---|
| RQ1 | Should "Flowchart" be named "Flowchart / Process Map" in user-facing navigation? | Yes. Use "Flowchart / Process Map" as the user-facing title and `flowchart` as the stable method ID. |
| RQ2 | Should Histogram and Scatter Diagram get optional assistance later? | Defer. This slice proves manual guidance and evidence expectations. Optional assistance can be proposed later if user testing shows manual creation is too slow, error-prone, or insufficient for reviewed evidence. |
| RQ3 | Should method metadata introduce a Seven Basic Quality Tools grouping field? | Not as a required durable contract in this slice. Optional front matter may be used for navigation, but required metadata should wait until catalog, generated navigation, or validation needs are clear. |
| RQ4 | Should Control Chart be the next proposal after this slice? | Likely, but not automatic. It should follow only after Histogram and Scatter Diagram guidance are reviewed and the project is ready for SPC-specific interpretation safeguards. |
| RQ5 | Should generated teaching images be part of this slice? | Yes. Include necessary conceptual images and prompt records when they materially improve demonstration of the method idea or common defects. Generate them through the imagegen skill after guide text and review criteria stabilize. |

## Open Questions

None that block proposal acceptance.
The review resolved the proposal-level questions above; detailed choices remain assigned to downstream specification artifacts.

## Downstream Specification Details

| ID | Detail | Owner artifact |
|---|---|---|
| DQ1 | Exact front matter fields for Flowchart, Histogram, and Scatter Diagram. | Feature spec |
| DQ2 | Exact method-guide section template. | Feature spec |
| DQ3 | Exact chart-quality checklist for Histogram and Scatter Diagram. | Test specification |
| DQ4 | Exact evidence-note wording for process facts and data-dependent charts. | Feature spec |
| DQ5 | Exact image and prompt-record paths for Flowchart, Histogram, and Scatter Diagram. | Feature spec |
| DQ6 | Exact conceptual teaching-image set and review checklist for each method. | Feature spec and test specification |
| DQ7 | Exact imagegen prompt constraints and saved output naming convention. | Feature spec and implementation plan |

Minimum shared guide sections for the downstream spec:

- summary;
- QCC stage fit;
- method question;
- when to use;
- when not to use;
- required inputs;
- output;
- manual chart or diagram recipe;
- quality standards;
- interpretation limits;
- common mistakes;
- evidence note;
- review checklist;
- image-assisted demonstration notes;
- related methods.

## Method-specific Best-practice Notes

### Flowchart / Process Map

The Flowchart / Process Map guide should focus on current-state understanding, not generic diagramming.

Required content should include:

- start and end boundaries;
- process steps;
- decision points;
- handoffs;
- queues or waiting points;
- rework loops;
- failure or defect locations;
- distinction between current state and future state.

The image set should show a current-state process map and a good-versus-weak process map comparison.
Images should demonstrate layout quality and process thinking, not serve as a verified process record.

### Histogram

The Histogram guide should focus on variation interpretation.

Required content should include:

- numeric data requirement;
- sample size caution;
- bin-width caution;
- outlier handling;
- distribution shape interpretation;
- before/after comparison cautions;
- statement that histogram does not prove process stability.

The image set should show a conceptual histogram distribution and a good-versus-weak histogram comparison.
Images should avoid exact counts, fake percentages, and any process-stability claim.

### Scatter Diagram

The Scatter Diagram guide should focus on relationship exploration without causal overclaiming.

Required content should include:

- paired numeric observations;
- clear x/y variable definitions;
- axis labels and units;
- outlier handling;
- correlation-versus-causation warning;
- statement that scatter does not prove root cause by itself;
- recommendation to follow up with cause analysis or designed verification when appropriate.

The image set should show a conceptual paired-variable scatter pattern and a good-versus-weak scatter comparison.
Images should avoid causal arrows, regression claims, and fake correlation coefficients.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Start a proposal for "Complete Seven Basic Quality Tools: Flowchart, Histogram, Scatter Diagram" | in scope | Problem, Goals, Recommended Direction; title amended to avoid implying Control Chart is included |
| Follow best practices | in scope | Context, Testing and Verification Strategy, Risks and Mitigations |
| Expand QCC methods | in scope | Expected Behavior Changes, Scope budget |
| Avoid disconnected method pages | in scope | Problem, Recommended Direction, Rollout and Rollback |
| Generate necessary images with imagegen to demonstrate ideas | in scope | Expected Behavior Changes, Architecture Impact, Testing and Verification Strategy, Scope budget |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Flowchart / Process Map method kit | core to this proposal | Low statistical risk and fills a current-state/process-understanding gap. |
| Histogram method kit | core to this proposal | Covers distribution and variation before more advanced control methods. |
| Scatter Diagram method kit | core to this proposal | Covers relationship exploration with manageable interpretation cautions. |
| Control Chart method kit | separate proposal | Higher statistical-control risk and likely needs stronger rules and proof. |
| Python chart automation | deferable follow-up | Useful later, but not needed to prove Markdown-first guidance. |
| Named-tool recipes | deferable follow-up | Current project direction is tool-neutral until user testing justifies named-tool paths. |
| Necessary conceptual images and prompt records for the new methods | same-slice dependency | Needed to demonstrate method ideas and common defects; generated images remain conceptual and are not final evidence charts. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-09 | Draft the next-method proposal around Flowchart, Histogram, and Scatter Diagram. | These methods extend the Seven Basic Quality Tools surface while avoiding Control Chart statistical-control risk. | Do nothing; add all remaining methods including Control Chart; start with automation. |
| 2026-07-09 | Keep Control Chart out of this first expansion. | Control Chart needs stronger assumptions, control-limit interpretation, and likely separate test/design treatment. | Treat Control Chart as another simple chart page. |
| 2026-07-09 | Keep guidance Markdown-first and tool-neutral. | This preserves the accepted project vision and avoids making a spreadsheet, statistics package, presentation tool, or Python path the product identity. | Named-tool tutorials and automation-first implementation. |
| 2026-07-09 | Rename the proposal from "Complete" to "Expand" Seven Basic Quality Tools guidance. | The slice excludes Control Chart, so the old title overclaimed completion. | Keep the original title and rely on non-goals to clarify scope. |
| 2026-07-09 | Treat separate metadata files as optional in this slice. | Lightweight front matter is enough until catalog, validation, or generated navigation needs are clear. | Require `method-kits/metadata/` sidecars up front. |
| 2026-07-09 | Accept the amended proposal direction. | Review recommended acceptance after title, structure, resolved-question, and method-standard amendments. | Leave the proposal in draft after amendments. |
| 2026-07-09 | Add coverage model, decision criteria, method-to-story fit, and shared guide-section handoff detail. | These clarify the accepted direction for spec authoring without changing scope. | Leave spec authors to infer these details from scattered proposal sections. |
| 2026-07-09 | Include necessary conceptual teaching images and prompt records in the method slice. | Users need visuals to demonstrate method ideas and common defects, but images must remain conceptual aids generated through the imagegen workflow and reviewed before use. | Treat all images as optional later follow-up; use generated visuals as quantitative evidence. |

## Next Artifacts

| Artifact | Purpose |
|---|---|
| Feature spec | Define observable behavior and guide contracts for Flowchart, Histogram, and Scatter Diagram. |
| Architecture assessment | Decide whether metadata grouping, method-kit boundaries, or optional future automation require architecture updates. |
| Execution plan | Sequence method-kit implementation after the spec and any required architecture work. |
| Test specification | Map method-guide, metadata, evidence, link, interpretation, image-prompt, and image-review checks before implementation. |
| Refreshed proposal review | Review the post-R2 image-scope update before downstream spec relies on it. |

## Follow-on Artifacts

None yet

## Readiness

Ready for feature spec authoring.
This proposal does not authorize architecture, plan, or implementation work until the downstream workflow artifacts are complete.
