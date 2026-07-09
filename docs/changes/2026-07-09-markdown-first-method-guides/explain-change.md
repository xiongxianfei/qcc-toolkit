# Explain Change: Markdown-First Method Guides

## Summary

This change accepts the Markdown-first method-guide direction and aligns the highest-level project identity artifacts with it.

Prior project artifacts emphasized Python-first implementation, generated evidence objects, and later PowerPoint-first, Python-assisted method-template work.
The new identity centers Markdown method guides, manual chart-creation guidance, reviewed teaching visuals, and evidence checklists.
PowerPoint templates, Python scripts, charting tools, presentation tools, and statistical tools remain useful execution aids, but they no longer define the product.

## Why it changed

The accepted proposal at `docs/proposals/2026-07-09-markdown-first-method-guides.md` records user feedback that generated chart images and presentation templates did not meet the required quality bar.
The stronger product center is to teach users how to understand QCC methods and create high-quality charts manually in suitable tools, with generated images used only for conceptual demonstration.

## Positioning delta

| Area | Before | After |
|---|---|---|
| Product category | PowerPoint-first, Python-assisted QCC method-kit and evidence toolkit. | Markdown-first QCC method-guide and chart-quality guidance system. |
| Primary surface | PowerPoint method templates, with Markdown and Python support. | Markdown method guides, chart-creation recipes, review checklists, and evidence notes. |
| Generated images | Not a defined primary boundary. | Teaching and conceptual aids only, never final quantitative evidence. |
| Manual chart guidance | Supporting guidance inside method kits. | Core product competency. |
| Tools | PowerPoint and Python had defined first-class roles. | Specific tools are optional execution choices. |

The supporting strategic-positioning rationale is recorded at `docs/vision/strategic-positioning.md`.
The accepted proposal also resolves DQ1-DQ6 as handoff guidance for method-guide, chart-creation, image-assisted demonstration, evidence, Pareto-kit, and tool-neutrality specifications.

## Files changed by this positioning update

| File | Reason |
|---|---|
| `CONSTITUTION.md` | Align highest operational governance with Markdown-first identity and image/evidence boundaries. |
| `AGENTS.md` | Align concise agent-facing operating rules with the constitution. |
| `VISION.md` | Replace the old PowerPoint-first vision with the current Markdown-first project identity. |
| `README.md` | Replace only the generated vision front-matter block from `VISION.md`. |
| `docs/vision/strategic-positioning.md` | Record the strategic rationale for the material repositioning. |
| `docs/proposals/2026-07-09-markdown-first-method-guides.md` | Mark the proposal accepted and record follow-on artifacts. |
| `docs/changes/2026-07-09-markdown-first-method-guides/change.yaml` | Record causal links required for the substantive vision update. |
| `docs/proposals/2026-07-07-create-qcc-toolkit.md` | Mark the earlier template-backed/Python-powered direction as superseded by the Markdown-first proposal. |
| `docs/proposals/2026-07-08-improve-qcc-method-templates.md` | Mark the earlier PowerPoint-first method-template direction as superseded by the Markdown-first proposal. |
| `specs/qcc-toolkit-first-slice.md` | Note that its related proposal was superseded after implementation. |
| `specs/qcc-method-kits.md` | Note that its related proposal was superseded after implementation. |
| `docs/project-map.md` | Refresh current-state proposal-history and identity references. |

## Validation

This is a governance and vision update, not an implementation change.
Relevant validation is artifact inspection, README marker validation, word-count checks for `VISION.md`, and Markdown/search checks.
Python tests are not required to prove this documentation-only repositioning, but lower-level specs and package metadata may need follow-up alignment before implementation work continues under the new direction.
