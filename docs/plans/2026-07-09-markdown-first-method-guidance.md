# Markdown-First Method Guidance Plan

## Status

- Plan lifecycle state: active
- Terminal disposition: not applicable

## Purpose / big picture

This plan sequences the accepted Markdown-first method-guidance direction into reviewable implementation milestones.
The work creates the guidance templates, validation checks, and first Pareto method kit needed to prove that Markdown can govern QCC method knowledge, image-assisted teaching, manual chart creation, and evidence readiness.

## Source artifacts

- Proposal: `docs/proposals/2026-07-09-markdown-first-method-guides.md`
- Spec: `specs/markdown-first-method-guidance.md`
- Spec review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/spec-review-r1.md`
- Architecture: `docs/architecture/markdown-method-guidance/architecture.md`
- Architecture review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/architecture-review-r1.md`
- Test spec: pending at plan authoring; expected `specs/markdown-first-method-guidance.test.md`

## Context and orientation

Current repository state includes older `docs/methods/`, `templates/ppt/`, and `qcc_toolkit/` first-slice assets.
Those assets are not removed by this plan.
They remain optional aids or historical implementation surfaces while new method-kit artifacts establish the Markdown-first structure.

The new implementation surfaces are expected to include `method-kits/`, shared chart-creation guidance, evidence guidance, image prompt conventions, reviewed teaching-visual locations, and tests or checks for those structures.

## Non-goals

- Do not implement final quantitative chart generation with image generation.
- Do not build a web app, dashboard, full slide-deck generator, or enterprise quality workflow.
- Do not add named-tool tutorials in the first implementation slice.
- Do not delete existing Python or PowerPoint assets as part of this plan.
- Do not implement advanced statistical automation.

## Requirements covered

| Requirement IDs | Milestone |
|---|---|
| R1-R4, R26 | M1 |
| R5-R10, R23-R24 | M1, M2 |
| R11-R15, R27 | M1, M2 |
| R16-R21 | M1, M2 |
| R22 | M2 |
| R25, R28 | M3 |

## Current Handoff Summary

- Current milestone: M2
- Current milestone state: review-requested
- Last reviewed milestone: M1
- Review status: code-review M1 clean-with-notes
- Remaining in-scope implementation milestones: M2, M3
- Next stage: code-review M2
- Final closeout readiness: not ready
- Reason: M2 Pareto method kit is implemented with passing targeted validation and ready for code-review.

## Milestones

### M1 - Shared Guidance Templates and Validation

- Milestone state: closed
- Goal: create shared Markdown method-guide, chart-creation, image-prompt, evidence-note, and review-checklist templates plus structure checks.
- Requirements: R1-R21, R23-R24, R26-R27
- Likely files: `docs/chart-creation/`, `docs/evidence/`, `docs/tool-guidance/`, `method-kits/_template/`, `tests/`
- Tests/proof: structure checks for guide sections, front matter, prompt constraints, evidence-note fields, tool-neutrality, and link/path integrity.
- Validation: focused pytest tests for new checks; `python -m pytest` before milestone closeout when feasible.
- Risks: validation may become too rigid before user testing.
- Rollback: remove new templates/checks or mark them draft before official method-kit use.

### M2 - Pareto Method Kit

- Milestone state: review-requested
- Goal: build `method-kits/pareto-chart/` as the first complete Markdown-first method kit.
- Requirements: R5-R10, R16-R22, R26-R27
- Likely files: `method-kits/pareto-chart/README.md`, `method-guide.md`, `chart-creation-guide.md`, `interpretation-guide.md`, `review-checklist.md`, `evidence-note-template.md`, examples, prompts, and teaching-visual placeholders or reviewed assets.
- Tests/proof: kit completeness, sample-data validity, evidence-note coverage, prompt conceptual-only checks, good/bad example review notes, and guide link checks.
- Validation: focused method-kit tests and Markdown inspections; manual review evidence for teaching visuals when binary visuals are included.
- Risks: Pareto content may drift from existing `docs/methods/pareto-chart.md`.
- Rollback: keep kit draft and leave existing method guide as the active reference until resolved.

### M3 - Compatibility, Catalog, and Optional Aid Alignment

- Milestone state: planned
- Goal: align existing method guides, PowerPoint templates, Python aids, project map notes, and any catalog or index surfaces so they clearly remain optional or historical aids under the Markdown-first direction.
- Requirements: R25, R28
- Likely files: `docs/methods/`, `templates/ppt/catalog.yml`, `README.md`, `docs/project-map.md`, tests or docs indexes as needed.
- Tests/proof: compatibility checks that existing assets are not silently promoted over method kits, and docs checks that optional aids do not contradict the new evidence boundary.
- Validation: focused artifact consistency tests; broader `python -m pytest` before final implementation closeout when feasible.
- Risks: touching older implementation surfaces could create broad churn.
- Rollback: revert optional-aid labeling changes while keeping method-kit artifacts intact.

## Validation plan

| Command or proof | Purpose |
|---|---|
| `python -m pytest tests/test_method_guides.py tests/test_method_kit_closeout.py` | Reuse or extend existing guide and method-kit checks. |
| `python -m pytest tests/test_artifact_consistency.py` | Check cross-artifact references after new directories are added. |
| `python -m pytest` | Broad local regression before final implementation closeout when feasible. |
| Manual teaching-image review evidence | Required only when binary teaching visuals are added. |
| Markdown/link inspection | Required for prompt, evidence-note, and chart-recipe documentation surfaces. |

## Risks and recovery

| Risk | Recovery |
|---|---|
| New method-kit structure duplicates existing `docs/methods` content. | Keep migration notes explicit and only promote the new kit after review checks pass. |
| Tool-neutral instructions are too vague. | Capture user-task review findings and defer named-tool recipes until justified. |
| Generated teaching visuals mislead users. | Require conceptual-only prompt checks and manual visual review before official use. |
| Scope expands into automation or slide generation. | Enforce non-goals and keep optional aids secondary. |

## Dependencies

- Approved spec and architecture package.
- Test-spec and test-spec-review before implementation.
- Existing pytest configuration in `pyproject.toml`.
- Existing method-guide and method-kit tests as reusable proof surfaces.

## Progress

- 2026-07-09: Plan authored for bounded workflow autoprogression to test-spec-review.
- 2026-07-09: Plan review approved with no material findings.
- 2026-07-09: Test specification authored and test-spec review approved with no material findings.
- 2026-07-09: M1 implementation started for shared guidance templates and validation checks.
- 2026-07-09: Added M1 focused tests before implementation; initial focused run failed because required M1 template and guidance artifacts were missing.
- 2026-07-09: Implemented shared method-guide, chart-creation, image-prompt, review-checklist, evidence-level, evidence-note, chart-quality, and tool-selection templates.
- 2026-07-09: M1 targeted validation passed and M1 moved to review-requested.
- 2026-07-09: Code review M1 R1 returned clean-with-notes, recorded no material findings, and closed M1.
- 2026-07-09: M2 implementation started for the Pareto method kit.
- 2026-07-09: Added M2 Pareto method-kit tests before implementation; the focused run failed because required Pareto kit assets were missing.
- 2026-07-09: Implemented the Pareto method kit with method guide, chart recipe, interpretation guide, review checklist, evidence note, synthetic sample data, worked example, reviewed good/bad teaching notes, conceptual image prompts, and teaching-visual location.
- 2026-07-09: Added Pareto kit review notes as manual proof that the guide teaches application and that no binary teaching visuals are included in M2.
- 2026-07-09: M2 targeted validation passed and M2 moved to review-requested.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-09 | Use three implementation milestones. | Separates shared standards, Pareto proof kit, and compatibility alignment. | One large implementation milestone that would hide review boundaries. |
| 2026-07-09 | Keep old Python/PPT surfaces as optional aids. | The accepted proposal supersedes product identity but not implemented historical assets. | Deleting or broadly rewriting older assets in the same slice. |
| 2026-07-09 | Add focused M1 validation in a new test module. | Existing tests cover older method guides and template closeout; M1 needs direct checks for the new Markdown-first shared templates. | Hiding M1 checks inside older PowerPoint-first test surfaces. |
| 2026-07-09 | Use reviewed Markdown teaching notes for M2 good/bad examples. | M2 can prove the teaching-review structure without introducing binary teaching visuals before visual review is needed. | Adding unreviewed PNG placeholders or generated visual assets. |

## Surprises and discoveries

- Existing plans remain active for PR handoff, so this plan is added as a separate active initiative.
- System Python does not have pytest installed; validation used the repository virtualenv at `.venv/bin/python`.
- M2 did not add binary teaching visuals, so MAN1 binary visual review is not triggered; reviewed Markdown good/bad teaching notes are included instead.

## Validation notes

- `python -m pytest tests/test_markdown_first_method_guidance.py` failed before implementation because `method-kits/_template/method-guide.md`, `method-kits/_template/chart-creation-guide.md`, `method-kits/_template/image-prompts/concept-visual.md`, `docs/evidence/evidence-levels.md`, and `docs/tool-guidance/tool-selection.md` did not exist.
- `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` passed after implementation: 5 passed.
- `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_method_kit_closeout.py` passed during implementation: 11 passed.
- `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py` passed for M1 handoff: 16 passed.
- `git diff --check` passed.
- `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` failed before Pareto kit implementation because the required `method-kits/pareto-chart/` assets did not exist.
- `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` passed after Pareto kit implementation: 9 passed.
- `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_method_kit_closeout.py` passed during M2 implementation: 11 passed.
- `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py` passed for M2 handoff: 20 passed.
- `git diff --check` passed for M2 handoff.

## Outcome and retrospective

- M1 is closed by clean code review. M2 implementation is complete and ready for code-review.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review M2.
