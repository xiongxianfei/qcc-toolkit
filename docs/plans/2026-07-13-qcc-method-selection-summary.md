# QCC Method Selection Summary Plan

## Status

- Status: active

## Purpose / big picture

This plan sequences the approved method-selection summary into one documentation implementation slice.
The work creates the canonical `method-kits/README.md` selector, links the root README and QCC project-story guide to it, and adds focused proof that the selector preserves stage fit, method status, link safety, and interpretation boundaries.

## Source artifacts

- Proposal: `docs/proposals/2026-07-13-qcc-method-selection-summary.md`
- Spec: `specs/qcc-method-selection-summary.md`
- Architecture: `docs/changes/2026-07-13-qcc-method-selection-summary/architecture-assessment.md`
- Test spec: `specs/qcc-method-selection-summary.test.md`

## Context and orientation

Canonical detailed method guides live under `method-kits/`.
The selector will also live in that directory as `method-kits/README.md`.
The QCC story stage model lives in `docs/qcc-project-story.md`.
Root navigation lives in `README.md`.

The selector is documentation-only.
It must not create a runtime method registry, generated catalog, recommendation algorithm, web interface, or chart-generation behavior.

## Non-goals

- Do not implement new QCC methods.
- Do not rewrite detailed method guides.
- Do not create a new QCC stage model.
- Do not duplicate full method procedures, formulas, examples, chart recipes, or review checklists in the selector.
- Do not add automation, generated navigation, or machine-readable metadata.
- Do not add advanced Control Chart, SPC, process capability, Standard Work, Visual Control, or Monitoring Plan guidance beyond status and handoff labels.

## Requirements covered

| Requirement | Milestone |
|---|---|
| R1-R18 | M1 |

## Current Handoff Summary

- Current milestone: M1
- Milestone state: review-requested
- Last reviewed milestone: none
- Review status: implementation complete; code-review pending
- Remaining milestones: M1 review
- Next stage: code-review M1
- Final closeout readiness: not ready
- Reason: M1 selector, navigation, tests, and manual scenario proof are implemented and locally validated; code-review has not run yet.

## Milestones

### M1. Method Selection Summary And Navigation

- Milestone state: review-requested
- Goal: Add the canonical method-selection summary and link navigation surfaces to it.
- Requirements: R1-R18
- Likely files: `method-kits/README.md`, `README.md`, `docs/qcc-project-story.md`, focused documentation tests, optional manual scenario review note.
- Tests/proof: write or update focused tests before production docs for selector structure, available method links, future-method non-links, root/project-story navigation, no duplicated full procedures, stage labels, guardrails, and representative scenario mapping.
- Validation: focused pytest command, manual scenario review, and `git diff --check`.
- Result: implemented; awaiting code-review.
- Risks: selector becomes too long, duplicates method-guide procedures, overstates method conclusions, or creates stale duplicate stage matrices.
- Rollback: remove `method-kits/README.md`, restore prior navigation links, and remove selector-specific tests or proof notes.

## Validation plan

| Command/proof | Purpose |
|---|---|
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -k 'method_selection or qcc_project_story or navigation or method_links'` | Focused selector, navigation, and link proof if implemented in existing test files. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` | Broader documentation regression check for method-kit and artifact consistency surfaces. |
| Manual scenario review recorded in change evidence | Confirm representative user and reviewer scenarios map to defensible methods and limitations. |
| `git diff --check` | Whitespace and patch hygiene. |

## Risks and recovery

- Risk: stage-method mapping becomes rigid or implies one method belongs to only one stage.
  - Recovery: preserve primary/supporting language and revise any mandatory-stage wording before review.
- Risk: selector duplicates detailed method procedures and creates drift.
  - Recovery: shorten selector rows and link to method guides for procedures, examples, formulas, and checklists.
- Risk: planned or advanced methods become dead links.
  - Recovery: show future methods as status text until their canonical guides exist.
- Risk: manual scenario proof is too informal to verify.
  - Recovery: record each scenario, selected method, required input, and interpretation boundary in a reviewable table.

## Dependencies

- Accepted proposal and approved proposal-review.
- Approved spec and clean spec-review.
- Architecture assessment recorded as not required.
- Test specification and clean test-spec-review before implementation.

## Progress

- 2026-07-13: Plan created after approved proposal-review R3, approved spec-review R1, and architecture-not-required assessment.
- 2026-07-13: Plan-review R1 approved the plan with no material findings.
- 2026-07-13: Test specification drafted for selector structure, links, status, guardrails, scope, navigation, and manual scenario proof.
- 2026-07-13: Test-spec-review R1 requested manual proof procedure detail; TSR-MS-001 was resolved by expanding MP1-MP4.
- 2026-07-13: Test-spec-review R2 approved the proof map with no material findings.
- 2026-07-13: M1 implementation started by adding focused selector/navigation tests before production documentation; first focused run failed for missing `method-kits/README.md`, proving the intended gap.
- 2026-07-13: M1 added `method-kits/README.md`, root and project-story navigation links, manual scenario review evidence, and workflow rationale metadata.
- 2026-07-13: M1 reached `review-requested` after focused and broad documentation checks passed locally.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-13 | Use one implementation milestone. | The change is a narrow documentation selector plus navigation and focused proof. | Split selector and navigation into separate milestones. |
| 2026-07-13 | Put proof before production docs in M1. | The constitution requires behavior changes to start from tests or executable proof when practical. | Write docs first and inspect manually afterward. |
| 2026-07-13 | Keep root README method-kit navigation stage-neutral. | The selector is now the canonical detailed stage-method selection surface, so root navigation should link to it instead of repeating stage relationships. | Keep a stage column in the root method-kit table. |

## Surprises and discoveries

- Existing `docs/qcc-project-story.md` already contains a high-level story map. M1 preserved that project-story context and added a selector link instead of replacing it with the new detailed selector matrix.

## Validation notes

- Tests first: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -k 'method_selection or qcc_project_story or navigation or method_links'` failed before production docs with 3 failures for missing `method-kits/README.md`.
- Focused validation after implementation: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -k 'method_selection or qcc_project_story or navigation or method_links'` passed with 5 selected tests.
- Broad documentation regression after implementation: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` passed with 34 tests.
- Manual scenario proof: `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` records MP1-MP4 as passed for implementation handoff.
- Patch hygiene: `git diff --check` passed.

## Outcome and retrospective

- M1 implemented the canonical selector and navigation handoff. Code-review is still required before milestone closeout.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review of M1.
