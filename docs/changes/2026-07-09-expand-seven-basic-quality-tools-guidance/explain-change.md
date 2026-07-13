# Explain Change: Expand Seven Basic Quality Tools Guidance

## Summary

This change adds the next Markdown-first Seven Basic Quality Tools guidance slice:
Flowchart / Process Map, Histogram, and Scatter Diagram.

It adds official method kits, conceptual teaching visuals with prompt records, README and QCC project-story navigation, focused documentation tests, and lifecycle review evidence.
Control Chart, SPC rules, chart-rendering automation, named-tool tutorials, and final-evidence generated charts remain out of scope.

## Problem

The repository had a Markdown-first QCC project-story guide and a complete Pareto method kit, but it did not yet provide the next common method-kit surfaces needed for a coherent QCC learning path.

The accepted proposal selected Flowchart / Process Map, Histogram, and Scatter Diagram as the next low-to-medium-risk expansion before Control Chart.
The goal was to teach each method as part of a QCC project story rather than as disconnected tool pages.

## Decision Trail

| Decision surface | Decision | Resulting change |
|---|---|---|
| Proposal | Proceed with Flowchart / Process Map, Histogram, and Scatter Diagram; defer Control Chart and automation. | Added three Markdown method kits and scope guards. |
| Spec | R1-R22 define method-kit structure, method-specific content, image prompt records, conceptual-only media policy, navigation, tests, and legacy preservation. | Implemented method guides, media, prompt records, links, and focused tests. |
| Architecture assessment | Architecture not required; existing Markdown-first method-guidance boundaries apply. | Reused `method-kits/`, `media/prompts/`, `media/`, README, story guide, and docs tests. |
| Plan | M1 author guides, M2 add prompts/images, M3 wire navigation and validation. | Implemented and reviewed each milestone separately. |
| Code review | CR-M1-001 and CR-M2-001 were accepted and resolved; M3 R1 was clean. | Renamed interpretation headings and replaced the Scatter weak-side causal-arrow visual. |

## Diff Rationale By Area

| Area | Files | Reason | Source artifact | Evidence |
|---|---|---|---|---|
| Method kits | `method-kits/flowchart.md`, `method-kits/histogram.md`, `method-kits/scatter-diagram.md` | Add official Markdown-first guides with metadata, QCC stage fit, manual recipes, quality standards, interpretation limits, evidence notes, review checklists, image notes, and related methods. | R1-R8 | T1-T5; M1 reviews |
| Flowchart guidance | `method-kits/flowchart.md` | Teach current-state process boundaries, steps, decisions, handoffs, queues, rework loops, failure locations, and current/future-state distinction. | R5 | T2 |
| Histogram guidance | `method-kits/histogram.md` | Teach numeric data preparation, sample-size and bin-width cautions, outliers, distribution-shape interpretation, before/after cautions, and no-stability limits. | R6 | T3 |
| Scatter guidance | `method-kits/scatter-diagram.md` | Teach paired numeric observations, x/y variables, axis labels and units, outliers, correlation-versus-causation limits, and no-root-cause-proof limits. | R7 | T4 |
| Prompt records | `media/prompts/flowchart/*.md`, `media/prompts/histogram/*.md`, `media/prompts/scatter-diagram/*.md` | Preserve image purpose, intended use, final prompt, negative constraints, conceptual-only policy, output path, and review status. | R11, R13, R14, R15 | T8; MAN1 |
| Teaching visuals | `media/flowchart/*.png`, `media/histogram/*.png`, `media/scatter-diagram/*.png` | Provide necessary conceptual demonstrations and good-versus-weak examples for each method without treating images as evidence. | R12, R16, R17, R18 | T9; MAN1 |
| Navigation | `README.md`, `docs/qcc-project-story.md` | Make the new methods discoverable and place them in current-state grasp, cause analysis, and verification stages. | R4, R19, R20 | T6 |
| Focused tests | `tests/test_markdown_first_method_guidance.py` | Add deterministic checks for required sections, method-specific cautions, prompt/media linkage, navigation, scope guards, and legacy preservation. | R21, R22 | T1-T9 |
| Lifecycle artifacts | `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/*`, `docs/plans/2026-07-09-expand-seven-basic-quality-tools-guidance.md`, `docs/plan.md` | Record proposal/spec/review/test/plan state, milestone progress, review findings, review-resolution, and final-closeout readiness. | Repository workflow and constitution | Review records and plan state |

## Tests Added Or Changed

| Test ID | Implemented proof | What it proves |
|---|---|---|
| T1 | `test_next_basic_quality_tool_method_kits_have_required_sections` | The three method kits exist and include required metadata and shared sections. |
| T2 | Same focused method-kit test with Flowchart terms | Flowchart covers boundaries, decisions, handoffs, queues, rework, failure locations, and current/future-state distinction. |
| T3 | Same focused method-kit test with Histogram terms | Histogram includes numeric data, sample size, bin width, outliers, distribution shape, before/after, and no-stability cautions. |
| T4 | Same focused method-kit test with Scatter terms | Scatter includes paired observations, x/y variables, axes/units, outliers, correlation, and no-root-cause-proof cautions. |
| T5 | Method-kit text checks and existing named-tool checks | The guides teach manual creation without requiring named tools. |
| T6 | `test_next_basic_quality_tool_navigation_links_story_fit_and_scope_guards` | README and project-story links exist and place the methods in the right QCC stages. |
| T7 | Scope-guard assertions | Control Chart, SPC rules, control limits, process capability, run-rule automation, and renderers are not introduced. |
| T8 | `test_next_basic_quality_tool_prompt_records_and_media_are_linked` | Prompt records include required sections, constraints, output paths, and passed review status. |
| T9 | Prompt/media/link assertions | Media files exist, are method-scoped, and are linked from method guides and prompt records. |
| MAN1 | Prompt-record manual review notes | Generated teaching visuals are conceptual-only, text-light, non-private, and not final evidence. |

## Validation Evidence Before Final Verify

| Stage | Evidence |
|---|---|
| M1 | Direct content proof passed; `git diff --check` passed. |
| M1 review-resolution | Exact `## Interpretation limits` proof passed; `git diff --check` passed. |
| M2 | Prompt/media/link proof passed; manual image review passed; `git diff --check` passed. |
| M2 review-resolution | Scatter prompt/image remediation proof passed; manual image review passed; `git diff --check` passed. |
| M3 | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` passed with 17 tests; `.venv/bin/python -m pytest` passed with 98 tests; `git diff --check` passed. |
| M3 code review | The same focused pytest, full pytest, and `git diff --check` passed during review. |

Hosted CI status is not claimed.
No hosted CI result was observed.

## Review Resolution Summary

| Finding | Disposition | Resolution |
|---|---|---|
| CR-M1-001 | accepted and closed | Renamed `## Interpretation rules` to `## Interpretation limits` in all three method kits. |
| CR-M2-001 | accepted and closed | Removed the Scatter causal-arrow request and replaced the weak-side visual with non-causal defects. |

Review-resolution record: `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/review-resolution.md`.

Code-review M3 R1 found no blocking or required-change findings.

## Alternatives Rejected

| Alternative | Reason rejected |
|---|---|
| Add Control Chart in this slice | Control Chart needs SPC-specific assumptions, control limits, false-signal cautions, and stronger interpretation safeguards. |
| Build Histogram or Scatter chart automation first | The accepted direction is Markdown-first and tool-neutral; automation remains secondary. |
| Create named spreadsheet or statistics-package tutorials | Named-tool tutorials would shift the product identity away from method guidance and chart-quality expectations. |
| Add method pages without project-story links | The proposal explicitly rejected disconnected tool pages. |
| Use generated images as final charts | The constitution and spec require generated images to remain conceptual teaching aids only. |

## Scope Control

The change does not add:

- Control Chart support.
- SPC rules, control-limit calculations, process capability, subgroup logic, or run-rule automation.
- Histogram or Scatter rendering automation.
- Named spreadsheet, presentation, statistics-package, or programming tutorials.
- Web UI, dashboard, CAPA/EQMS workflow, release automation, hosted CI, or external service integration.
- Removal of existing optional `docs/methods/`, `templates/ppt/`, or `qcc_toolkit/` assets.

## Risks And Follow-Ups

| Risk | Current mitigation | Follow-up |
|---|---|---|
| Generated images could be mistaken for evidence. | Prompt records, method guides, and tests require conceptual-only and not-final-evidence boundaries. | Keep image review manual for future generated visuals. |
| Histogram and Scatter could be overinterpreted. | Method guides and tests require no-stability and no-root-cause-proof cautions. | Consider optional assistance only after manual guidance is reviewed in use. |
| Control Chart remains a Seven Basic Quality Tools gap. | Proposal and spec intentionally defer it. | Treat Control Chart as a separate proposal with SPC safeguards. |
| Tests could become brittle if they overfit prose. | Tests use required headings, core phrases, and policy checks rather than full snapshots. | Keep future edits tied to stable requirement language. |

## Readiness

This explanation is the durable rationale surface required before final verification.
Final verification still needs to run and record branch-readiness evidence before PR handoff.
