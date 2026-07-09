# Markdown-First Method Guidance Architecture

## Status

- approved

## Related artifacts

- Proposal: [Markdown-First QCC Method Guides](../../proposals/2026-07-09-markdown-first-method-guides.md)
- Spec: [Markdown-First Method Guidance Spec](../../../specs/markdown-first-method-guidance.md)
- Spec review: [Spec Review R1](../../changes/2026-07-09-markdown-first-method-guides/reviews/spec-review-r1.md)
- Plan: [Markdown-First Method Guidance Plan](../../plans/2026-07-09-markdown-first-method-guidance.md)
- ADRs: No new ADR required for this package. This architecture applies the accepted Markdown-first product direction to repository boundaries without changing the local-first Python stack or evidence-package ADRs.

## Introduction and Goals

This package defines the architecture for the Markdown-first QCC method-guidance system.
It makes the repository boundaries visible before implementation of method-guide templates, chart-creation guidance, image prompt conventions, evidence-note policies, and the first Pareto method kit.

The architecture goals are:

- Keep Markdown method guides as the authoritative method-knowledge surface.
- Keep image prompts and teaching visuals conceptual-only and reviewable.
- Keep manual chart-creation guidance and evidence notes first-class.
- Preserve existing PowerPoint and Python assets as optional execution aids.
- Make future automation consume method guidance and quality standards rather than define them.

## Architecture Constraints

| Constraint | Architectural response |
|---|---|
| `CONSTITUTION.md` makes Markdown, conceptual images, and manual chart guidance core identity. | New method-kit boundaries put Markdown guide, chart recipe, evidence note, prompt, and teaching visuals ahead of optional tool aids. |
| The first slice must remain tool-neutral. | Method kits include tool-class guidance and defer named-tool recipes. |
| Image generation cannot create final evidence. | Prompt and teaching-visual assets are stored as conceptual-only reviewed training artifacts. |
| Existing Python/PPT assets remain useful. | Legacy `docs/methods`, `templates/ppt`, and `qcc_toolkit` assets are treated as optional or historical surfaces until explicit migration. |
| Implementation must be locally reviewable. | Markdown, CSV, prompt files, and review checklists are plain-text-first where possible; binary teaching visuals require review notes. |

## Context and Scope

QCC Toolkit is a repository-centered guidance system.
Contributors author method kits, examples, prompts, and review checklists.
QCC users consume Markdown guides and use suitable external tools to create final charts.
Reviewers inspect method-kit completeness, teaching-image boundaries, and evidence readiness.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

In scope:

- `method-kits/<method-id>.md` as the official one-file method-guide boundary.
- `media/prompts/<method-id>.md` as the official prompt-record boundary.
- `media/<method-id>/` as the official media boundary for reviewed teaching visuals.
- `docs/chart-creation/`, `docs/evidence/`, and `docs/tool-guidance/` as shared guidance surfaces.
- compatibility with current `docs/methods/`, `templates/ppt/`, and `qcc_toolkit/` assets.

Out of scope:

- runtime service architecture;
- hosted image generation;
- automated slide-deck generation;
- named-tool tutorial library;
- advanced statistical automation.

## Solution Strategy

The selected architecture is a method-kit-centered documentation architecture.

```text
QCC stage
  -> method kit
    -> method-kits/<method-id>.md as the primary user-facing guide
    -> media/prompts/<method-id>.md for prompt records
    -> media/<method-id>/ for reviewed teaching visuals
      -> optional tool recipe or automation aid
```

The main tradeoff is deliberate restraint.
The repository becomes easier to review and improve because the authoritative knowledge is Markdown and structured examples, but users still create final charts in suitable external tools or validated analysis paths.

## Building Block View

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

| Area | Responsibility | Key rule |
|---|---|---|
| `method-kits/<method-id>.md` | Official one-file method guide with method explanation, chart or worksheet recipe, worked example, review checklist, evidence note, and media links. | One method guide should be one Markdown file until a method genuinely needs multiple guide files. |
| `media/prompts/<method-id>.md` | Prompt text for reviewed teaching visuals used by the method guide. | Prompt records are centralized and traceable. |
| `media/<method-id>/` | Reviewed teaching visuals used by the method guide. | Visual assets stay outside the method guide while remaining easy to link. |
| `docs/chart-creation/` | Shared chart-quality standards and reusable chart-making principles. | Standards are tool-neutral and reused by chart-based kits. |
| `docs/evidence/` | Evidence levels and evidence-note templates. | Final data-dependent charts preserve source, scope, assumptions, and review status. |
| `docs/tool-guidance/` | Optional tool-class or later named-tool guidance. | Named tools are deferred until user testing justifies them. |
| `docs/methods/` | Existing Markdown method guides. | Existing guides can be migrated or referenced during transition. |
| `templates/ppt/` | Existing PowerPoint templates and catalog. | Optional execution or historical aid, not current product identity. |
| `qcc_toolkit/` | Existing Python evidence code. | Optional validated analysis aid, not the primary method-guidance surface. |

## Runtime View

No long-running runtime is introduced.
The important operational flows are authoring and review flows.

### Method-kit authoring flow

1. Contributor creates or updates a method kit.
2. Contributor writes Markdown guide, chart or worksheet recipe, evidence note, examples, and prompt files.
3. Contributor adds reviewed teaching visuals or records that visuals are pending.
4. Local checks validate front matter, required sections, paths, evidence levels, and conceptual-only prompt constraints.
5. Reviewer applies guide, chart-recipe, prompt, teaching-image, and evidence checklist review.

### User application flow

1. User opens the method guide.
2. User selects a suitable tool class from the chart-creation guide.
3. User manually creates the chart or worksheet.
4. User records source data, date range, scope, assumptions, tool used, and review status.
5. Reviewer checks the final chart against the review checklist and evidence level.

### Image-assisted demonstration flow

1. Contributor writes a prompt with purpose, use, prompt text, and negative constraints.
2. Image generation may produce a teaching visual.
3. Reviewer confirms conceptual-only status, method correctness, text-light design, and no fake numeric evidence.
4. Approved image is stored as a teaching visual with review evidence.

## Deployment View

This change deploys as repository content.
There is no server, database, telemetry path, external API, or hosted image service dependency.

| Artifact | Deployment concern |
|---|---|
| Markdown guides and templates | Versioned in Git and readable without specialized tooling. |
| Sample data | Synthetic or approved non-sensitive data only. |
| Teaching images | Binary assets require review notes and conceptual-only classification. |
| Optional Python aids | Continue to run locally when used; no new runtime dependency is required by this architecture. |
| Optional PowerPoint assets | Remain downloadable/editable user aids but are no longer the controlling product identity. |

## Crosscutting Concepts

| Concept | Rule |
|---|---|
| Source of truth | Markdown method guides and chart-quality standards govern method knowledge. |
| Image boundary | Images teach concepts and never provide final quantitative evidence. |
| Evidence levels | E0 through E4 determine how much support final chart use needs. |
| Tool neutrality | First-slice guidance names tool classes, not named products. |
| Reviewability | Every official kit must be inspectable through Markdown structure, checklist fields, prompt constraints, and evidence notes. |
| Privacy | Examples and prompts avoid private operational data and hidden sensitive content. |

## Architecture Decisions

No new ADRs are required.
The durable product direction is recorded in the accepted proposal, `VISION.md`, and this architecture package.
Existing ADRs for local-first Python and evidence-package boundaries remain valid for optional automation aids.

## Quality Requirements

| Quality | Scenario | Measure |
|---|---|---|
| Reviewability | A reviewer opens a method kit change. | Required guide sections, prompt files, evidence notes, examples, and review checklist entries are visible in repository artifacts. |
| Tool neutrality | A first-slice guide gives chart-making guidance. | It names tool classes and does not require a named product tutorial. |
| Evidence rigor | A user prepares a final data-dependent chart. | Evidence note fields capture source, scope, assumptions, tool, reviewer, and status. |
| Safety | A generated teaching image is added. | Review evidence confirms conceptual-only use and no fake precise quantitative claims. |
| Maintainability | Future automation is added. | Automation references method guidance and evidence standards rather than redefining them. |

## Risks and Technical Debt

- Existing specs and architecture packages still describe implemented Python/PPT first-slice behavior.
  They remain historical until explicitly superseded or amended.
- Binary teaching visuals need manual review evidence because text diff cannot prove visual quality.
- Tool-neutral guidance may become vague; user task tests are required before adding named-tool recipes.
- Method kits introduce new directory surfaces that need validation to prevent broken links and incomplete guides.

## Glossary

| Term | Meaning |
|---|---|
| Method kit | Per-method documentation and teaching package centered on Markdown guidance. |
| Teaching visual | Reviewed conceptual image that supports explanation but is not final evidence. |
| Evidence level | Classification from E0 to E4 that defines evidence support required for chart use. |
| Tool-class guidance | Guidance that names a class of tool, such as spreadsheet or statistical tool, without mandating a named product. |

## Next artifacts

- Architecture review.
- Execution plan after clean architecture review.

## Follow-on artifacts

None yet.

## Readiness

Approved by workflow settlement after clean architecture-review R1.
Ready for execution planning.
