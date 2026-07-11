# Expand Core QCC Method Kits Plan

## Status

- Status: active

## Purpose / big picture

This plan sequences the approved four-method expansion into small documentation and validation milestones.
The work promotes Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H into official Markdown-first method kits and cleans up live references to deleted `docs/methods/` files.

## Source artifacts

- Proposal: `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md`
- Spec: `specs/expand-core-qcc-method-kits.md`
- Architecture: `docs/changes/2026-07-10-expand-core-qcc-method-kits/architecture-assessment.md`
- Test spec: `specs/expand-core-qcc-method-kits.test.md` pending

## Context and orientation

Canonical method kits live under `method-kits/`.
Extracted legacy content is preserved in `docs/methods-key-content.md`.
The old `docs/methods/` files are intentionally deleted and must not be restored as compatibility notices.
Known live reference surfaces include README, `docs/qcc-project-story.md`, `templates/ppt/catalog.yml`, focused docs tests, catalog tests, artifact-consistency tests, and present-tense documentation.

## Non-goals

- Do not add Control Chart, SPC, process capability, broad automation, or named-tool tutorials.
- Do not restore `docs/methods/` compatibility pages.
- Do not add runtime Python behavior unless required only for focused documentation checks.

## Requirements covered

| Requirement | Milestone |
|---|---|
| R1-R6, R17-R18 | M1 |
| R7-R10, R17-R18 | M2 |
| R11-R13, R17-R18 | M3 |
| R14-R16, R22 | M4 |
| R19-R21 | M1-M4 |

## Current Handoff Summary

- Current milestone: M3
- Milestone state: review-requested
- Last reviewed milestone: M2
- Review status: M3 implementation complete; code-review pending
- Remaining milestones: M3, M4
- Next stage: code-review M3
- Final closeout readiness: not ready
- Reason: M3 5W2H method kit, focused proof, and manual review evidence are ready for review; M3 is not closed until code-review is clean and any required review-resolution is complete.

## Milestones

### M1. Check Sheet Method Kit

- Milestone state: closed
- Goal: Create `method-kits/check-sheet.md` using extracted legacy content and the approved Check Sheet safeguards.
- Requirements: R1-R6, R17-R19, R21
- Likely files: `method-kits/check-sheet.md`, optional metadata if existing method-kit conventions require it, focused tests.
- Tests/proof: shared-section checks, Check Sheet safeguard checks, extracted-content use review, manual method-correctness review.
- Validation: focused pytest command from test spec plus manual review note.
- Result: Added `method-kits/check-sheet.md`, M1-focused tests in `tests/test_markdown_first_method_guidance.py`, and `docs/changes/2026-07-10-expand-core-qcc-method-kits/manual-method-kit-review.md`.
- Review: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/code-review-m1-r1.md` closed M1 cleanly with no material findings.
- Risks: weak observation-definition guidance or checklist/check-sheet confusion.
- Rollback: remove the new kit and related tests for this milestone.

### M2. Fishbone Diagram and 5 Whys Method Kits

- Milestone state: closed
- Goal: Create `method-kits/fishbone-diagram.md` and `method-kits/five-whys.md` as paired cause-analysis guides.
- Requirements: R1-R4, R7-R10, R17-R21
- Likely files: the two method kits, optional prompt records/media only if reviewed visuals are actually included, focused tests.
- Tests/proof: Fishbone and 5 Whys safeguard checks, output-boundary checks, optional visual-policy proof, manual method-correctness review.
- Validation: focused pytest command from test spec plus manual review note.
- Result: Added `method-kits/fishbone-diagram.md`, `method-kits/five-whys.md`, M2-focused tests in `tests/test_markdown_first_method_guidance.py`, and M2 manual proof in `docs/changes/2026-07-10-expand-core-qcc-method-kits/manual-method-kit-review.md`.
- Review: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/code-review-m2-r1.md` closed M2 cleanly with no material findings.
- Risks: overclaiming root cause or treating 5 Whys as exactly five mandatory steps.
- Rollback: remove the new kits, optional media, prompt records, and related tests for this milestone.

### M3. 5W2H Method Kit

- Milestone state: review-requested
- Goal: Create `method-kits/five-w-two-h.md` with problem-framing and action-planning modes.
- Requirements: R1-R4, R11-R13, R17-R19, R21
- Likely files: 5W2H method kit and focused tests.
- Tests/proof: two-mode guidance checks, owner/due-date/dependency/verification fields, output-boundary checks, manual method-correctness review.
- Validation: focused pytest command from test spec plus manual review note.
- Result: Added `method-kits/five-w-two-h.md`, M3-focused tests in `tests/test_markdown_first_method_guidance.py`, and M3 manual proof in `docs/changes/2026-07-10-expand-core-qcc-method-kits/manual-method-kit-review.md`.
- Risks: merging problem framing and action planning without distinguishing the two modes.
- Rollback: remove the new kit and related tests for this milestone.

### M4. Navigation, Catalog, Deleted References, And Closeout Checks

- Milestone state: planned
- Goal: Update README, project-story links, catalog references, focused tests, and present-tense documentation so no live surface relies on deleted `docs/methods/*.md` files.
- Requirements: R14-R16, R22
- Likely files: `README.md`, `docs/qcc-project-story.md`, `templates/ppt/catalog.yml`, tests, docs that make present-tense claims about `docs/methods/`.
- Tests/proof: deleted-reference scan, catalog validation or adjusted catalog tests, artifact-consistency checks, scope guards, full relevant documentation check.
- Validation: focused pytest command, catalog validator if catalog remains active, `git diff --check`.
- Result: pending
- Risks: historical references may be over-edited; catalog validation may need deliberate schema or fixture adjustment.
- Rollback: restore previous references only if the deleted method surface is also restored by an accepted upstream decision.

## Validation plan

| Command/proof | Purpose |
|---|---|
| `python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_scope_guards.py` | Focused documentation, catalog, deleted-reference, and scope checks. |
| `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | Catalog path and metadata validation if catalog remains active after reference cleanup. |
| `git diff --check` | Whitespace and patch hygiene. |
| Manual method-kit review | Confirm method correctness, output boundaries, evidence status, and no overclaiming. |

## Risks and recovery

- Risk: deleted-reference cleanup touches historical documents too broadly.
  - Recovery: keep historical records when clearly historical; update only live references and present-tense claims.
- Risk: catalog requires missing Markdown guide paths.
  - Recovery: point active entries to canonical method kits or revise catalog validation under spec-governed behavior.
- Risk: manual review finds method guidance too thin.
  - Recovery: revise the affected kit before code-review handoff.

## Dependencies

- Approved spec and clean spec review.
- Architecture assessment recorded as not required.
- Active test spec and clean test-spec-review before implementation.

## Progress

- 2026-07-10: Plan created after approved proposal-review R2 and approved spec-review R1.
- 2026-07-10: Test spec and test-spec-review R1 completed; workflow auto target reached before implementation.
- 2026-07-10: M1 implemented Check Sheet method kit, focused M1 tests, and manual method-kit review note.
- 2026-07-10: M1 code-review R1 closed cleanly and handed off to implement M2.
- 2026-07-11: M2 implemented Fishbone Diagram and 5 Whys method kits, focused M2 tests, and manual method-kit review note.
- 2026-07-11: M2 code-review R1 closed cleanly and handed off to implement M3.
- 2026-07-11: M3 implemented 5W2H method kit, focused M3 tests, and manual method-kit review note.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-10 | Sequence Check Sheet first. | Reliable observations improve every later analysis method. | Implement all four guides in one large slice. |
| 2026-07-10 | Review Fishbone and 5 Whys together. | Users need their relationship and boundaries to be clear. | Treat them as unrelated method pages. |
| 2026-07-10 | Put deleted-reference cleanup in the final milestone. | It needs all canonical target paths available. | Update references before target guides exist. |
| 2026-07-10 | Keep Check Sheet visual guidance Markdown-only for M1. | The approved visual policy says no generated image is initially needed for Check Sheet, and a worked table/checklist is more precise. | Generate a conceptual image in M1. |
| 2026-07-11 | Keep Fishbone and 5 Whys visual guidance Markdown-only for M2. | The spec does not require generated visuals, and M2 can prove visual policy by keeping images optional and not adding empty media directories. | Add optional conceptual images before the guides are reviewed. |
| 2026-07-11 | Keep 5W2H visual guidance Markdown-only for M3. | The accepted visual policy says a two-mode table and worked guidance communicate 5W2H better than generated images. | Add a generated 5W2H teaching image in M3. |

## Surprises and discoveries

- M1 validation used `.venv/bin/python` because `/usr/bin/python` and `/usr/bin/python3` do not have pytest installed.
- M2 tests intentionally preserved exact legacy concepts such as "structured hypothesis map", "verification marker", and "evidence for each link", which required small wording adjustments during implementation.
- M3 tests initially conflicted by requiring the safety phrase "does not prove root cause" while forbidding the substring "proves root cause"; the forbidden overclaim check was narrowed to unsafe positive claims.

## Validation notes

- 2026-07-10: `/usr/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` failed because `/usr/bin/python` has no `pytest` module installed.
- 2026-07-10: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` failed as expected before implementation: 3 failed because `method-kits/check-sheet.md` did not exist.
- 2026-07-10: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` passed after implementation: 3 passed, 14 deselected.
- 2026-07-10: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` passed: 17 passed.
- 2026-07-10: `git diff --check` passed.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` failed as expected before implementation: 4 failed because `method-kits/fishbone-diagram.md` and `method-kits/five-whys.md` did not exist.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` passed after implementation: 4 passed, 17 deselected.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` passed: 21 passed.
- 2026-07-11: `git diff --check` passed.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'five_w_two_h_method_kit'` failed as expected before implementation: 3 failed because `method-kits/five-w-two-h.md` did not exist.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'five_w_two_h_method_kit'` passed after implementation: 3 passed, 21 deselected.
- 2026-07-11: `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` passed: 24 passed.
- 2026-07-11: `git diff --check` passed.

## Outcome and retrospective

- Pending implementation.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review M3.
