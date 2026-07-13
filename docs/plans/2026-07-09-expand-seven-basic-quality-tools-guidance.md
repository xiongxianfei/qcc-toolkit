# Expand Seven Basic Quality Tools Guidance Plan

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-applicable

## Purpose / big picture

This plan sequences the approved Flowchart / Process Map, Histogram, and Scatter Diagram expansion into small reviewable implementation milestones.

The implementation must keep the repository Markdown-first, tool-neutral, and safe around generated images.
Method guidance comes before generated teaching visuals.
Generated visuals remain conceptual aids and never final quantitative evidence.

## Source artifacts

- Proposal: `docs/proposals/2026-07-09-expand-seven-basic-quality-tools-guidance.md`
- Spec: `specs/expand-seven-basic-quality-tools-guidance.md`
- Spec review: `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/reviews/spec-review-r1.md`
- Architecture: not required; architecture assessment in `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/change.yaml`
- Existing architecture reference: `docs/architecture/markdown-method-guidance/architecture.md`
- Test spec: `specs/expand-seven-basic-quality-tools-guidance.test.md`

## Context and orientation

The existing Markdown-first method-guidance architecture already defines the relevant repository boundaries:

- `method-kits/<method-id>.md` for user-facing method guides.
- `method-kits/metadata/<method-id>.yml` when machine-readable metadata is needed.
- `media/prompts/<method-id>/<image-id>.md` for per-image prompt records.
- `media/<method-id>/` for reviewed conceptual teaching visuals.
- `docs/qcc-project-story.md` and `README.md` for project-story and method-kit navigation.
- `tests/test_markdown_first_method_guidance.py` and `tests/test_artifact_consistency.py` as likely focused validation surfaces.

Implementation should follow existing Pareto method-kit patterns where they fit, but should keep this slice simpler when the spec does not require separate metadata sidecars.

## Non-goals

- Do not add Control Chart.
- Do not add SPC rules, control limits, process capability, subgroup logic, or run-rule automation.
- Do not add chart-rendering automation for Histogram or Scatter Diagram.
- Do not create named-tool tutorials.
- Do not treat generated images as final charts or project evidence.
- Do not remove older optional method guides, templates, Python aids, or PowerPoint assets.

## Requirements covered

| Requirement | Milestone or evidence surface |
|---|---|
| R1 | M1 |
| R2 | M1 |
| R3 | M1 |
| R4 | M1, M3 |
| R5 | M1 |
| R6 | M1 |
| R7 | M1 |
| R8 | M1 |
| R9 | M1, M3 |
| R10 | M1, M3 |
| R11 | M2 |
| R12 | M2 |
| R13 | M2 |
| R14 | M2 |
| R15 | M2 |
| R16 | M2 |
| R17 | M2 |
| R18 | M2 |
| R19 | M3 |
| R20 | M3 |
| R21 | M3 |
| R22 | M3 |

## Current Handoff Summary

- Current milestone: final closeout
- Milestone state: pr-open
- Last reviewed milestone: M3 - Wire Navigation And Focused Validation
- Review status: code-review M3 R1 clean-with-notes
- Remaining implementation milestones: none
- Next stage: PR review
- Final closeout readiness: PR handoff complete
- Reason: M1, M2, and M3 are closed; no review-resolution finding remains open; explain-change is recorded; final local verify passed; PR #4 is open.

## Milestones

### M1 - Author Three Method Kits

- Milestone state: closed
- Goal: Add official Markdown-first method kits for Flowchart / Process Map, Histogram, and Scatter Diagram.
- Requirements: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10
- Files:
  - `method-kits/flowchart.md`
  - `method-kits/histogram.md`
  - `method-kits/scatter-diagram.md`
- Tests and proof:
  - Focused structure checks for required method-kit files and shared sections.
  - Method-specific checks for Flowchart boundaries, decisions, handoffs, rework, and current-state distinction.
  - Method-specific checks for Histogram numeric-data, sample-size, bin-width, outlier, and no-stability cautions.
  - Method-specific checks for Scatter paired-data, axes, outlier, and no-root-cause-proof cautions.
  - Scope-guard checks that Control Chart, SPC, and chart automation are not introduced.
- Steps:
  - Use existing Pareto method-kit style for section shape and evidence discipline.
  - Keep front matter lightweight and reviewable.
  - Include image-assisted demonstration notes that identify expected prompt/image assets without using images as evidence.
- Validation:
  - Run focused documentation tests added or updated in M3 once available.
  - Run direct file inspection before M3 test coverage exists.
- Result: Closed by code-review M1 R2 after CR-M1-001 was resolved.
- Risks:
  - Method pages could become generic definitions.
  - Histogram and Scatter guidance could overclaim statistical meaning.
- Rollback:
  - Remove the three new method-kit files and any links added in later milestones.

### M2 - Add Prompt Records And Conceptual Teaching Visuals

- Milestone state: closed
- Goal: Add necessary imagegen prompt records and conceptual teaching visuals for each method.
- Requirements: R11, R12, R13, R14, R15, R16, R17, R18
- Files:
  - `media/prompts/flowchart/*.md`
  - `media/prompts/histogram/*.md`
  - `media/prompts/scatter-diagram/*.md`
  - `media/flowchart/*`
  - `media/histogram/*`
  - `media/scatter-diagram/*`
  - method-kit links back to those assets
- Tests and proof:
  - Prompt-record checks for purpose, intended use, final prompt, negative constraints, conceptual-only policy, output path, and review status.
  - Manual teaching-image review records or checklist entries confirming images are text-light, conceptual-only, non-private, and not final evidence.
  - Guard checks against exact fake values, fake percentages, causal proof, process-stability claims, and production identifiers.
- Steps:
  - Generate images only after M1 method text and review criteria are stable.
  - Use the imagegen workflow for bitmap assets.
  - Persist generated project-bound images under method-scoped media paths.
  - Keep detailed instructions in Markdown instead of image text.
- Validation:
  - Run prompt-record and link checks.
  - Manually inspect generated images and record review status in prompt records or image notes.
- Result: Closed by code-review M2 R2 after CR-M2-001 was resolved.
- Risks:
  - Generated images may look authoritative or contain inaccurate text.
  - Binary visual quality cannot be proven by text diff alone.
- Rollback:
  - Remove or unlink misleading visuals while keeping method guides authoritative.

### M3 - Wire Navigation And Focused Validation

- Milestone state: closed
- Goal: Link the new method kits from README and the QCC project story, then add focused local checks for this slice.
- Requirements: R4, R9, R10, R19, R20, R21, R22
- Files:
  - `README.md`
  - `docs/qcc-project-story.md`
  - focused tests under `tests/`
  - optional updates to artifact-consistency tests
- Tests and proof:
  - README links resolve to the three method kits.
  - QCC project-story references place methods in the right project stages.
  - Focused tests cover required method-kit sections, method-specific cautions, prompt-record constraints, link integrity, and out-of-scope guardrails.
  - Full local validation runs when the implementation touches shared tests or repository-wide checks.
- Steps:
  - Add method-kit navigation entries without turning README into a landing page.
  - Add QCC story references where each method naturally supports the project flow.
  - Extend existing tests rather than creating a parallel validation style.
- Validation:
  - Run focused pytest for changed documentation surfaces.
  - Run broader local validation if test or package surfaces are touched.
- Result: Closed by code-review M3 R1 with no blocking or required-change findings.
- Risks:
  - Navigation links could imply Control Chart is included or that older optional guides are replaced.
- Rollback:
  - Revert README/story links and focused test additions for this slice.

## Validation plan

| Command or proof | Purpose |
|---|---|
| `pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` | Focused method-kit, prompt-record, and artifact-consistency checks after implementation. |
| `pytest` | Broad local regression check when shared tests or repository-wide checks change. |
| `git diff --check` | Whitespace and patch hygiene. |
| Manual image review checklist | Confirm generated visuals are conceptual-only, text-light, non-private, and not final evidence. |

## Risks and recovery

- Risk: The scope grows into Control Chart or SPC.
  - Recovery: Remove Control Chart/SPC content and route it to a separate proposal.
- Risk: Generated images are misleading, too text-heavy, or look like final evidence.
  - Recovery: Remove or replace the image and keep Markdown guidance as the authoritative surface.
- Risk: New tests overfit exact prose and make guide edits brittle.
  - Recovery: Use stable section, phrase, and policy checks for required commitments rather than whole-document snapshots.
- Risk: Manual chart guidance is too generic.
  - Recovery: Tighten method-specific creation steps and review checklists inside M1 before generating images.

## Dependencies

- Accepted proposal and proposal-review R3 are complete.
- Approved spec and spec-review R1 are complete.
- Architecture assessment is `architecture-not-required`.
- Implementation depends on approved plan-review, active test spec, and approved test-spec-review.
- Image generation depends on stable method text and review criteria from M1.

## Progress

- 2026-07-09: Plan drafted for bounded workflow autoprogression to test-spec-review.
- 2026-07-09: Plan-review R1 approved the plan with no material findings.
- 2026-07-09: Test specification authored for test-spec-review.
- 2026-07-09: Test-spec-review R1 approved the proof map with no material findings.
- 2026-07-09: M1 implementation started. Pre-proof confirmed `method-kits/flowchart.md`, `method-kits/histogram.md`, and `method-kits/scatter-diagram.md` were missing before implementation.
- 2026-07-09: M1 added the three method-kit guides. README navigation, QCC project-story links, focused pytest coverage, prompt records, and teaching visuals remain unchanged by design because they are assigned to M2 or M3.
- 2026-07-09: Code-review M1 R1 requested changes for CR-M1-001 because the guides missed the spec-required `interpretation limits` section name.
- 2026-07-10: Review-resolution accepted CR-M1-001 and renamed `## Interpretation rules` to `## Interpretation limits` in all three M1 method kits.
- 2026-07-10: Code-review M1 R2 found no blocking or required-change findings, closed CR-M1-001, and closed M1. The next stage is implement M2.
- 2026-07-10: M2 pre-proof failed as expected because required prompt records and media assets were missing before implementation.
- 2026-07-10: M2 generated six conceptual teaching visuals with the imagegen workflow, added prompt records and manual review notes, copied assets under method-scoped `media/<method-id>/` paths, and linked them from the three method kits.
- 2026-07-10: Code-review M2 R1 requested changes for CR-M2-001 because the Scatter good-versus-weak prompt and visual include an unsupported causal-arrow cue that conflicts with the Scatter method-kit image policy.
- 2026-07-10: Review-resolution accepted CR-M2-001, removed the causal-arrow request from the Scatter good-versus-weak prompt, replaced the generated image without a causal or trend arrow, and reran M2 targeted proof.
- 2026-07-10: Code-review M2 R2 found no blocking or required-change findings, closed CR-M2-001, and closed M2. The next stage is implement M3.
- 2026-07-10: M3 implementation started. Focused pre-proof failed as expected because README and QCC project-story navigation did not yet link the three new method kits.
- 2026-07-10: M3 added README method-kit navigation, QCC project-story references for Flowchart / Process Map, Histogram, and Scatter Diagram, and focused tests for required method-kit sections, prompt/media links, navigation, scope guards, and legacy optional-aid preservation.
- 2026-07-10: Code-review M3 R1 found no blocking or required-change findings, closed M3, and moved the plan to final closeout readiness.
- 2026-07-10: Explain-change recorded the final reviewed diff rationale in `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/explain-change.md`; final verify is next.
- 2026-07-10: Final verify passed focused pytest, full pytest, Ruff, mypy, and `git diff --check`; PR handoff is next.
- 2026-07-10: PR #4 opened at https://github.com/xiongxianfei/qcc-toolkit/pull/4; the plan remains active pending PR review outcome.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-09 | Use three implementation milestones: method guides, prompt/images, navigation/validation. | This keeps method content stable before image generation and keeps validation changes reviewable. | Generate images first; implement all artifacts in one unreviewable batch. |
| 2026-07-09 | Reuse existing Markdown-first architecture and media boundaries. | The approved spec does not add a new runtime, metadata schema, external service, or automation boundary. | Create a new architecture package for paths already governed by the existing architecture. |

## Surprises and discoveries

- None.

## Validation notes

- M1 implementation and CR-M1-001 resolution validation has run; M2 and M3 validation remains pending.
- 2026-07-09 M1 pre-proof: targeted Python file-existence check failed as expected because the three method-kit files were missing before implementation.
- 2026-07-09 M1 direct content proof: targeted Python assertions passed for required shared sections, lightweight metadata fields, method-specific Flowchart / Process Map guidance, Histogram cautions, Scatter Diagram cautions, tool-neutral manual creation guidance, conceptual-only image policy, final-evidence boundary, and scope guards.
- 2026-07-09 M1 diff hygiene: `git diff --check` passed.
- 2026-07-10 CR-M1-001 resolution proof: targeted Python assertions passed for exact `## Interpretation limits` sections and absence of the old `## Interpretation rules` heading.
- 2026-07-10 CR-M1-001 diff hygiene: `git diff --check` passed.
- 2026-07-10 M2 pre-proof: targeted Python check failed as expected because required prompt records and media assets did not exist before implementation.
- 2026-07-10 M2 manual image review: six generated teaching visuals passed conceptual-only, text-light, no exact fake values, no private identifiers, and no proof/stability claim checks. Review notes are recorded in the prompt records.
- 2026-07-10 M2 prompt/media/link proof: targeted Python assertions passed for prompt-record fields, output paths, media files, conceptual-only constraints, required visual purposes, and method-kit links.
- 2026-07-10 M2 diff hygiene: `git diff --check` passed.
- 2026-07-10 CR-M2-001 resolution proof: targeted Python assertions passed for absence of causal-arrow requests in the Scatter good-versus-weak prompt, presence of non-causal weak-side defects, prompt/media/link consistency, manual review note update, and project media asset presence.
- 2026-07-10 CR-M2-001 manual image review: replacement Scatter good-versus-weak image shows weak-side unlabeled/missing-unit and clutter defects without a causal or trend arrow.
- 2026-07-10 CR-M2-001 diff hygiene: `git diff --check` passed.
- 2026-07-10 M3 pre-proof: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` failed as expected before navigation updates because README and QCC project-story links were missing.
- 2026-07-10 M3 focused validation: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` passed with 17 tests.
- 2026-07-10 M3 broad validation: `.venv/bin/python -m pytest` passed with 98 tests.
- 2026-07-10 M3 diff hygiene: `git diff --check` passed.

## Outcome and retrospective

- Pending.

## Readiness

- See `Current Handoff Summary`.
- PR handoff is complete; awaiting PR review.
