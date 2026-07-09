# Proposal: Markdown-First QCC Method Guides with Image-Assisted Demonstration

## Status

accepted

This proposal records a revised product direction for QCC Toolkit method guidance.
It is an accepted decision, but it is not a specification, an implementation plan, or verification evidence.

This proposal responds to user feedback that programmatically generated chart images and presentation templates did not meet the required quality bar.
It proposes a more practical direction: use Markdown as the primary product surface, use image-generation only for teaching and conceptual demonstration, and treat high-quality manual chart-creation guidance as a core competency.

This proposal supersedes the earlier direction that centered generated templates or generated chart assets as primary deliverables for method use.

## Problem

The project has attempted generated chart images and generated presentation templates, but the output quality has not met user expectations.
The generated assets were too simple, visually weak, and not useful enough as practical QCC method materials.

The core user need is not automatic generation of every chart or slide.
The core user need is clear, reliable guidance that helps people understand QCC methods and create high-quality charts using suitable tools.

Users need method guides that explain method purpose, QCC stage fit, proper use, misuse prevention, chart-making process, interpretation, and review quality.

The project also needs to avoid over-committing to any single authoring tool, scripting language, or slide-generation path.
Those tools may be useful in some contexts, but they should not define the product.

## Goals

| ID | Goal |
|---|---|
| G1 | Make Markdown method guides the primary user-facing asset for QCC method education and application. |
| G2 | Use image-generation only for conceptual teaching visuals, visual explanations, and good/bad examples, not for final quantitative evidence charts. |
| G3 | Treat manual chart-creation guidance as a core competency of the project. |
| G4 | Provide tool-neutral chart-making recipes that help users create high-quality charts using suitable charting, spreadsheet, presentation, or statistical tools. |
| G5 | Explain each QCC method clearly: purpose, QCC stage fit, when to use, when not to use, required inputs, procedure, interpretation, mistakes, and review checklist. |
| G6 | Preserve QCC stage workflow as the organizing frame for method guidance. |
| G7 | Establish quality standards for charts: clear title, correct chart type, readable labels, visible data source, correct scale, appropriate annotations, and defensible interpretation. |
| G8 | Create reusable image-generation prompts and reviewed teaching images where they improve understanding. |
| G9 | Avoid generating polished final presentation templates or exact numerical charts when the quality or reliability is insufficient. |
| G10 | Keep optional tool-specific aids as secondary material, not the project identity. |
| G11 | Keep the project small enough to deliver high-quality method guidance before expanding into automation, applications, or advanced analytics. |

## Non-goals

| ID | Non-goal |
|---|---|
| NG1 | Do not generate final quantitative evidence charts using image-generation. |
| NG2 | Do not treat generated images as project evidence. |
| NG3 | Do not make any specific authoring, charting, scripting, or presentation tool the primary identity of the project. |
| NG4 | Do not continue producing low-value placeholder presentation templates as primary deliverables. |
| NG5 | Do not build full automated slide-deck generation as part of this proposal. |
| NG6 | Do not build a no-code desktop application, web dashboard, enterprise quality system, document-management system, or broad charting platform. |
| NG7 | Do not implement advanced statistical automation before the method-guide and manual chart-creation standards are proven. |
| NG8 | Do not define implementation tickets, schedules, or development milestones in this proposal. |
| NG9 | Do not remove the possibility of future automation; simply make it secondary to documentation and chart-making guidance. |

## Vision fit

proposes a vision revision

At drafting time, prior project artifacts emphasized Python-first implementation, generated evidence objects, and later PowerPoint-first, Python-assisted method-template work.
This proposal preserves the useful principles from those directions: QCC stage focus, explainability, reviewability, and resistance to dashboard or document-editor scope.

However, it revises the primary user-facing direction.
The project becomes Markdown-first, image-assisted, and tool-neutral rather than code-first, generated-template-first, or PowerPoint-first.
The vision and governance artifacts are updated by the follow-on artifacts for this proposal before this direction becomes implementation-ready.

Recommended revised vision sentence:

```md
QCC Toolkit is a Markdown-first guide system for Quality Control Circle methods.
It helps users understand, apply, explain, and review QCC methods through clear method documentation, image-assisted teaching visuals, and practical manual chart-creation guidance.
Specific charting, analysis, or presentation tools are optional execution choices rather than the project identity.
```

## Context

Previous project direction evolved through several stages.
The original direction emphasized a programmable toolkit for QCC evidence, with generated charts and report-ready outputs.
A later direction moved toward practical method templates because users needed easier adoption assets.
A subsequent attempt generated a method template and chart demonstration, but the quality was not sufficient for real use.

The latest user feedback identifies a better product center:

```text
Markdown explains the method.
Image-generation demonstrates the concept.
Manual chart guidance teaches users how to create high-quality charts with suitable tools.
Optional automation is used only when it clearly adds value.
```

This direction shifts the project from producing generated visual artifacts to producing high-quality instructional assets.
The project becomes more useful if it teaches users how to make good QCC charts, rather than trying to automatically generate charts or templates whose quality is not acceptable.

The project should still preserve QCC rigor.
A manual chart is acceptable only when users understand the data, chart type, scale, labeling, source note, interpretation, and review checklist.
The guide should make those expectations explicit.

## Options Considered

| Option | Name | Summary | Benefits | Costs / risks | Decision |
|---|---|---|---|---|---|
| O1 | Continue generated chart/template direction | Continue trying to generate polished charts and presentation templates. | Could reduce manual work if quality improves. | Prior attempts did not meet quality requirements; risks continued low-value output. | Rejected for current direction. |
| O2 | Tool-specific template library | Create templates for one dominant presentation or charting tool. | Familiar for some users; easier to demonstrate fixed workflows. | Locks the product to one tool, creates maintenance burden, and does not generalize well. | Rejected as the main direction. |
| O3 | Markdown-first method guides with image-assisted demonstration | Build high-quality Markdown guides, conceptual visuals, manual chart recipes, examples, and review checklists. | Best fit with current user feedback; tool-neutral; easier to review, version, improve, and teach. | Requires strong writing, examples, and visual review discipline. | Recommended direction. |
| O4 | Full automation platform | Build an application that selects methods, generates charts, and exports reports. | Could help later at scale. | Premature; does not solve guide quality; higher delivery and maintenance risk. | Deferred follow-up. |
| O5 | Static reference documentation only | Write definitions of each method without chart-making guidance or visuals. | Simple to produce and maintain. | Not practical enough; users still need help creating charts and reviewing output quality. | Rejected as incomplete. |
| O6 | Specialist statistical-tool cookbook | Focus mainly on advanced statistical software workflows. | Useful for high-rigor methods. | Too narrow for ordinary QCC teams and basic methods. | Deferred as optional advanced guides. |

## Recommended Direction

Create QCC Toolkit as a Markdown-first, image-assisted, tool-neutral QCC method guide system.

The primary product unit should be a QCC method guide, not a generated slide deck or generated chart.
Each method guide should explain the method, teach the chart or worksheet creation process, show conceptual visuals, and provide review criteria.

Recommended method-kit shape:

```text
method-kits/<method-id>/
  README.md
  guide.md                       # primary user-facing guide
  examples/
    sample-data.csv              # when useful
    worked-example.md
  support/
    image-prompts.md
    evidence-note-template.md
    teaching-examples.md
    reviewer-notes.md
```

The guide should be tool-neutral by default.
It may refer to classes of tools such as spreadsheet tools, charting tools, presentation tools, or statistical tools, but it should not require a specific one.
Optional tool-specific recipes can be added later only when they are useful and maintainable.

Core rule:

```text
Generated images teach concepts.
Manual charts communicate project evidence.
Markdown governs method knowledge and chart quality.
```

Image-generation should be used for conceptual method illustration, good/bad chart layout comparison when reviewed, QCC stage-flow illustration, and non-numerical diagram examples.
It should not be used for exact numerical chart evidence, final project charts, audit evidence, or competition evidence.

For every chart-based QCC method, the guide should include a manual chart recipe.
The recipe should teach users how to make a high-quality chart, not merely define the chart.
Recommended sections include chart purpose, required data, data preparation, tool selection guidance, step-by-step creation, formatting standard, interpretation, common mistakes, review checklist, and evidence note.

The first slice should prove the documentation and chart-guidance standard with Pareto Chart, Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H.
Pareto Chart should be the first complete method kit because it is common, chart-based, easy to understand, and exposes chart-quality issues clearly.

## Expected Behavior Changes

| ID | Expected behavior change |
|---|---|
| B1 | Users start with a Markdown guide to understand a QCC method before creating charts or worksheets. |
| B2 | Users learn how to create high-quality charts manually using suitable tools. |
| B3 | Users use image-generated visuals as teaching aids, not as final project charts. |
| B4 | Users can distinguish conceptual visuals, worked examples, draft charts, and reviewed evidence charts. |
| B5 | Users preserve source data, date range, filters, assumptions, and review checklist for final data-dependent charts. |
| B6 | Reviewers can judge chart quality using method-specific checklists. |
| B7 | The repository stops prioritizing generated presentation templates whose quality is not useful enough. |
| B8 | Optional tool-specific or automation aids become secondary, not mandatory. |
| B9 | Future automation remains possible because method guidance and chart-quality standards are explicit first. |
| B10 | The project becomes easier to improve through documentation review, example review, and visual teaching review. |

## Architecture Impact

The repository should shift from a generated-asset architecture to a method-guide-centered architecture.

Recommended repository boundaries:

| Area | Responsibility |
|---|---|
| `docs/methods/` | Canonical Markdown method guides. |
| `docs/chart-creation/` | Shared chart-quality standards, tool-selection guidance, and generic chart-making principles. |
| `method-kits/<method-id>/` | Complete method kit containing guide, examples, checklists, visuals, and prompts. |
| `method-kits/<method-id>/image-prompts/` | Versioned prompts for conceptual teaching visuals. |
| `method-kits/<method-id>/examples/` | Worked examples, sample data, good/bad examples, and review notes. |
| `docs/review-checklists/` | Shared facilitator and chart-review checklists. |
| `assets/teaching-visuals/` | Reviewed non-evidence visuals used in guides. |
| `docs/tool-guidance/` | Optional class-based or tool-specific guidance when needed. |
| `docs/evidence/` | Evidence note templates and review-readiness policies. |

Recommended conceptual flow:

```text
QCC stage
  -> Method guide
    -> Required inputs
      -> Manual chart or worksheet recipe
        -> Conceptual teaching visual if helpful
          -> User-created chart or worksheet
            -> Interpretation guide
              -> Review checklist
                -> Evidence note for final use
```

This flow makes documentation quality and chart-making instruction the core system.
Automation can still be added later, but it should consume the same method definitions and quality standards rather than define them.

## Testing and Verification Strategy

Testing should focus on guide usefulness, visual quality, chart-instruction quality, and reviewability.

| Test area | Strategy |
|---|---|
| Method-guide completeness | Confirm every guide includes summary, stage fit, use/not-use, inputs, procedure, interpretation, mistakes, checklist, and related methods. |
| Chart-recipe review | Confirm chart-based methods provide enough instruction for a user to create the chart manually without hidden steps. |
| Tool-neutrality review | Confirm guides do not depend on one specific tool unless a separate optional recipe is clearly labeled. |
| Image prompt review | Confirm prompts are versioned, purpose-specific, and restricted to conceptual or teaching use. |
| Teaching-image review | Manually review generated images for clarity, correctness, professionalism, and absence of misleading quantitative claims. |
| Good/bad example review | Confirm examples teach recognizable quality differences and do not introduce incorrect method logic. |
| Evidence checklist review | Confirm final chart guidance records source data, date range, scope, filters, assumptions, and reviewer status. |
| Method consistency review | Confirm related method guides use consistent QCC stage names, terminology, and review expectations. |
| User task test | Ask a representative user to create a chart from the guide and record where instructions are unclear. |
| Reviewer task test | Ask a facilitator or reviewer to assess the created chart using the checklist. |
| Link and structure checks | Confirm internal links, image paths, example paths, and method IDs remain valid. |

Verification evidence should include reviewed method guides, reviewed teaching images, completed user-task tests, reviewer checklist results, and a sample method kit such as Pareto Chart.

## Rollout and Rollback

Rollout should start with one complete method kit and then expand to a small first-slice set.

| Step | Description |
|---|---|
| 1 | Create the shared method-guide template and chart-creation guide template. |
| 2 | Create the Pareto Chart method kit as the first complete example. |
| 3 | Review the Pareto kit with at least one user and one reviewer. |
| 4 | Improve the template based on review findings. |
| 5 | Expand to Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H. |
| 6 | Add optional tool-specific recipes only after the general guide proves useful. |
| 7 | Add automation or advanced analysis only after method guidance and chart standards stabilize. |

Rollback should be handled by marking prior generated-template proposals as superseded only after this proposal is accepted.
Generated assets from earlier experiments can be retained as prototypes or archived examples, but they should not be promoted as official method kits unless they pass the new quality standard.

If the Markdown-first approach fails user review, the project should revisit whether the product should become a curated template library, a training course, or a full software tool.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Guides become too theoretical | Users still cannot create usable charts. | Require manual chart-creation recipes, worked examples, and user task testing. |
| Images look attractive but teach incorrect ideas | Users may misunderstand the method. | Use reviewed prompts, manual visual review, and a policy that images are conceptual only. |
| Tool-neutral guidance becomes vague | Users may not know what to do in their actual software. | Provide generic steps first, then optional tool-class or tool-specific addenda when needed. |
| The project loses evidence rigor | Final charts may be visually good but poorly supported. | Require evidence checklists for data-dependent charts. |
| The project becomes only documentation | Users may want runnable support later. | Keep optional automation as a deferred extension once guide standards are stable. |
| Manual chart creation creates inconsistent visuals | Reviewers may see uneven quality. | Add chart-quality standards and good/bad examples. |
| Generated images include inaccurate text or labels | Training assets look unprofessional or misleading. | Keep detailed text in Markdown; use images mainly for visual concepts. |
| Prior proposals conflict with the new direction | Contributors may be confused. | Mark this proposal as a vision revision and superseding direction if accepted. |
| Advanced methods need more rigor than manual guidance | Users may misuse complex methods. | For complex methods, recommend validated analysis tools and stronger review checklists. |
| Scope expands into every charting tool | Maintenance becomes unmanageable. | Keep tool-specific recipes optional and limited to high-value cases. |

## Open Questions

No proposal-level open questions remain after this proposal.
The main direction is decided by this accepted proposal: Markdown-first, image-assisted, tool-neutral manual chart guidance.

The following downstream details should be resolved in specifications:

| ID | Downstream detail | Owner artifact |
|---|---|---|
| DQ1 | Exact Markdown method-guide template and front matter. | Method guide specification. |
| DQ2 | Exact chart-creation guide template. | Manual chart-creation specification. |
| DQ3 | Image-generation prompt structure, review checklist, and storage convention. | Image-assisted demonstration specification. |
| DQ4 | First Pareto Chart method-kit content. | Pareto Chart method kit. |
| DQ5 | Evidence checklist policy for final data-dependent charts. | Evidence and review policy. |
| DQ6 | Whether optional tool-specific recipes should be included in the first slice. | Tool guidance decision record. |

## Resolved Downstream Decisions

These decisions are accepted handoff guidance for downstream specifications.
Specifications may refine field names and examples, but they should not reopen the product direction without a new proposal or decision record.

| ID | Decision |
|---|---|
| DQ1 | Method guides use structured Markdown front matter and fixed sections for summary, QCC stage fit, method question, use and non-use conditions, inputs, output, manual chart or worksheet recipe, quality standards, interpretation, example wording, mistakes, review checklist, evidence note, image-assisted demonstration notes, and related methods. |
| DQ2 | Chart-creation guidance is tool-neutral but executable, covering chart purpose, required data structure, preparation, tool-class guidance, construction steps, formatting standard, annotations, interpretation rules, chart defects, review checklist, and evidence note. It may live inside the primary guide to reduce user-facing file count. |
| DQ3 | Image-generation is governed as a teaching-visual system. Prompt files and reviewed teaching notes may live under `method-kits/<method-id>/support/` so users start from the guide, and images remain conceptual only, text-light, method-correct, and not final evidence. |
| DQ4 | The first Pareto kit proves the model with `README.md`, primary `guide.md`, worked example, sample data, and support material for reviewed good/bad examples, prompts, evidence notes, and reviewer notes. |
| DQ5 | Final data-dependent charts use evidence levels from E0 concept through E4 audit or high-risk evidence. Project and formal evidence levels preserve source data, date range, scope or filters, method, tool used, calculation table when applicable, assumptions, reviewer, date, and review status. |
| DQ6 | The first slice stays tool-neutral and uses tool-class guidance only. Named-tool recipes are deferred until user testing shows where tool-neutral guidance is insufficient. |

Recommended method-guide front matter:

```yaml
---
method_id: pareto_chart
method_name: Pareto Chart
qcc_stages:
  - understand_current_condition
  - analyze_causes
method_type: chart
primary_output: chart
evidence_risk: medium
imagegen_allowed: conceptual_only
final_chart_generation: manual_tool_guided
related_methods:
  upstream:
    - check_sheet
    - stratification
  downstream:
    - fishbone_diagram
    - five_whys
guide_version: 0.1.0
review_status: draft
---
```

Recommended evidence levels:

| Level | Use case | Evidence expectation |
|---|---|---|
| E0 - Concept | Training image or conceptual guide visual. | Mark as conceptual only; no source data required. |
| E1 - Draft | Team discussion or learning exercise. | Show data period and source when available. |
| E2 - Project presentation | Normal QCC project slide. | Preserve source data, date range, scope or filter, method, and reviewer checklist. |
| E3 - Formal review | Management, competition, or customer-facing review. | Preserve calculation table, chart source, method guide version, reviewer status, and assumptions. |
| E4 - Audit or high-risk | Safety-critical, customer-impact, or audit evidence. | Use a validated analysis path or independent verification and preserve a full reproducibility record. |

## Decision Log

| Date | Decision | Reason | Alternatives rejected or deferred |
|---|---|---|---|
| 2026-07-09 | Propose Markdown-first QCC method guides as the primary product surface. | Generated images and presentation templates did not meet the required quality bar. | Generated-template-first and generated-chart-first directions. |
| 2026-07-09 | Use image-generation only for conceptual teaching and demonstration. | It can improve learning visuals but is not reliable enough for quantitative evidence charts. | Image-generated final charts. |
| 2026-07-09 | Treat manual chart-creation guidance as a core competency. | Users need to know how to create high-quality charts with suitable tools. | Static definitions without chart-making procedure. |
| 2026-07-09 | Keep the guide tool-neutral by default. | Specific tools are optional execution choices and should not define the project. | One-tool-first positioning. |
| 2026-07-09 | Use Pareto Chart as the first complete method-kit example. | It is common, chart-based, easy to understand, and exposes chart-quality issues clearly. | Starting with advanced statistical methods. |
| 2026-07-09 | Defer automation and generated presentation assets. | They should follow only after method guidance and chart-quality standards are strong. | Full automation or generated slide decks first. |
| 2026-07-09 | Resolve downstream DQ1-DQ6 as specification handoff guidance. | The accepted direction should not be reopened while writing the next specs. | Leaving method-guide, chart-creation, image, evidence, and tool-neutrality decisions implicit. |
| 2026-07-09 | Mark earlier Python/generated-evidence and PowerPoint-first proposals as superseded. | Contributors need a clear current governing direction. | Keeping older accepted proposals as active direction. |

## Next Artifacts

| Artifact | Purpose |
|---|---|
| Method guide specification | Define the standard Markdown guide structure, front matter, terminology, and checklist sections. |
| Manual chart-creation specification | Define chart-quality standards and reusable chart-making recipe structure. |
| Image-assisted demonstration specification | Define prompt standards, image review rules, and storage conventions. |
| Evidence checklist specification | Define what users should preserve for final data-dependent charts. |
| Pareto Chart method kit | Build the first complete method guide, manual chart recipe, conceptual visuals, good/bad examples, and checklist. |

## Follow-on Artifacts

| Artifact | Purpose |
|---|---|
| `CONSTITUTION.md` | Align highest-level governance with the Markdown-first direction. |
| `AGENTS.md` | Align concise agent-facing identity rules with the constitution. |
| `VISION.md` | Record the current Markdown-first project identity and scope. |
| `README.md` | Sync generated vision front-matter from `VISION.md`. |
| `docs/vision/strategic-positioning.md` | Record supporting rationale for the material repositioning. |
| `docs/changes/2026-07-09-markdown-first-method-guides/change.yaml` | Record change metadata and causal links for the substantive vision update. |
| `docs/changes/2026-07-09-markdown-first-method-guides/explain-change.md` | Explain the positioning delta and affected artifacts. |
| `docs/project-map.md` | Refresh current-state identity and risk notes after the vision change. |
| `docs/proposals/2026-07-07-create-qcc-toolkit.md` | Mark the earlier create-toolkit direction superseded by this proposal. |
| `docs/proposals/2026-07-08-improve-qcc-method-templates.md` | Mark the earlier PowerPoint-first method-template direction superseded by this proposal. |

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Focus on Markdown. | in scope | Goals, Recommended Direction, Architecture Impact |
| Use image-generation skill to demonstrate methods. | in scope | Goals, Recommended Direction, Testing and Verification Strategy |
| Treat manual chart creation guidance as a core competency. | in scope | Goals, Recommended Direction |
| Clearly instruct users how to generate high-quality charts. | in scope | Problem, Goals, Testing and Verification Strategy |
| Let users choose suitable tools. | in scope | Non-goals, Recommended Direction |
| Avoid centering any specific programming or presentation tool. | in scope | Non-goals, Recommended Direction |
| Generate a proposal rather than directly editing implementation files. | in scope | Status, Readiness |
| Preserve best practices. | in scope | Testing and Verification Strategy, Risks and Mitigations, Rollout and Rollback |
| Keep future automation possible but not central. | deferred follow-up | Non-goals, Architecture Impact, Scope Budget |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Vision revision from PowerPoint/Python focus to Markdown-first method guidance | core to this proposal | The proposal changes the primary user-facing direction. |
| Markdown method-guide structure | core to this proposal | This becomes the main product surface. |
| Manual chart-creation guide standard | core to this proposal | This is the project's proposed core competency. |
| Image-generation policy | core to this proposal | Image use needs strict boundaries to prevent misleading evidence. |
| Pareto Chart method kit | first-slice candidate | Best concrete example to validate the direction. |
| Check Sheet, Fishbone, 5 Whys, and 5W2H guides | first-slice candidate | Proves the guide standard across data, diagram, logic-chain, and planning methods. |
| Good/bad chart examples | same-slice dependency | Needed to teach chart quality effectively. |
| User and reviewer task testing | same-slice dependency | Needed to verify guide usefulness. |
| Optional tool-specific recipes | deferable follow-up | Useful only after the general guide standard is proven. |
| Automation scripts or generated chart assets | deferable follow-up | They may help later but are no longer the primary direction. |
| Generated presentation templates | deferable follow-up | Prior results did not meet quality; revisit only if quality can be controlled. |
| Full application or dashboard | out of scope | Not needed for Markdown-first method guidance. |
| Enterprise quality workflows | out of scope | Outside the QCC method-guide scope. |

## Readiness

Accepted and ready for downstream specification.

This proposal is accepted, but it is not implementation-ready by itself.
The next useful step is to create or revise the method guide specification, manual chart-creation specification, image-assisted demonstration specification, and first Pareto Chart method kit.
