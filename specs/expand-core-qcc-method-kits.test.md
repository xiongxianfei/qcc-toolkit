# Expand Core QCC Method Kits Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/expand-core-qcc-method-kits.md`
- Plan: `docs/plans/2026-07-10-expand-core-qcc-method-kits.md`
- Architecture/ADRs: `docs/changes/2026-07-10-expand-core-qcc-method-kits/architecture-assessment.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Feature spec | `specs/expand-core-qcc-method-kits.md` | approved | Status says approved; reviewed by `spec-review-r1`. |
| Spec review | `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/spec-review-r1.md` | approved | No material findings. |
| Architecture assessment | `docs/changes/2026-07-10-expand-core-qcc-method-kits/architecture-assessment.md` | architecture-not-required | Recorded after approved spec review. |
| Plan | `docs/plans/2026-07-10-expand-core-qcc-method-kits.md` | active | Reviewed by `plan-review-r1`. |
| Plan review | `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/plan-review-r1.md` | approved | No material findings. |

## Testing strategy

Use focused Markdown and artifact-consistency tests for deterministic repository checks.
Use manual review for method correctness, evidence-status clarity, output-boundary safety, and generated-visual policy when visuals are added.
Use catalog validation when catalog entries remain active after deleted-reference cleanup.
No end-to-end runtime test is required unless implementation changes Python catalog behavior.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1 | integration | Verifies four canonical files exist. |
| R2 | T2 | contract | Verifies metadata fields or approved equivalent. |
| R3 | T3 | contract | Verifies shared sections. |
| R4 | T4 | contract | Verifies QCC project-story connection. |
| R5, R6 | T5, MP1 | contract/manual | Check Sheet safeguards and method correctness. |
| R7, R8 | T6, MP2 | contract/manual | Fishbone safeguards and method correctness. |
| R9, R10 | T7, MP3 | contract/manual | 5 Whys safeguards and method correctness. |
| R11, R12, R13 | T8, MP4 | contract/manual | 5W2H safeguards and method correctness. |
| R14 | T9 | integration | README and project-story navigation. |
| R15, R16 | T10, T11 | integration | Deleted references and catalog behavior. |
| R17, R18 | T12, MP5 | contract/manual | Extracted content remains available and is used as source material. |
| R19, R20 | T13, MP6 | contract/manual | Visual policy. |
| R21 | T14 | contract | Scope guard. |
| R22 | T1-T14, MP1-MP6 | contract/manual | Focused checks and manual proof. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T5, MP1 | Check Sheet guidance and manual review. |
| E2 | T6, MP2 | Fishbone guidance and manual review. |
| E3 | T7, MP3 | 5 Whys guidance and manual review. |
| E4 | T8, MP4 | 5W2H guidance and manual review. |
| E5 | T10, T11 | Deleted-reference and catalog checks. |

## Edge case coverage

| Edge case | Covered by | Notes |
|---|---|---|
| EC1 | T10 | Historical references may remain only when not live/present-tense dependencies. |
| EC2 | T11 | Catalog must not require missing active guide paths. |
| EC3 | T13 | No generated image is acceptable by default. |
| EC4 | T7, MP3 | 5 Whys branching and non-exact-five rule. |
| EC5 | T5, MP1 | Check Sheet "other" category handling. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_scope_guards.py` | planned-for-implementation | implement | M4 | M4 code-review | Failing assertions block milestone review. | Zero collected tests is failure because focused checks are expected. | Plan validation notes and code-review record. | Local repository inspection only; no network or destructive side effects. |
| CMD2 | `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | existing/configured | implement | M4 | M4 code-review | Validation failure blocks M4 review handoff. | Not applicable. | Plan validation notes and code-review record. | Local catalog validation only. |
| CMD3 | `git diff --check` | existing/configured | implement | each milestone | each milestone code-review | Whitespace errors block review handoff. | Not applicable. | Plan validation notes and code-review record. | Local diff inspection only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | T1, T2, T3, T4, T5, T12, T14 | MP1, MP5 | CMD1, CMD3 | Plan validation notes, focused pytest output, manual review note. | M1 code-review | CMD1 may run only focused assertions relevant to M1 until M4 completes all paths. |
| M2 | T1, T2, T3, T4, T6, T7, T12, T13, T14 | MP2, MP3, MP5, MP6 if visuals added | CMD1, CMD3 | Plan validation notes, focused pytest output, manual review note. | M2 code-review | Fishbone and 5 Whys reviewed together. |
| M3 | T1, T2, T3, T4, T8, T12, T14 | MP4, MP5 | CMD1, CMD3 | Plan validation notes, focused pytest output, manual review note. | M3 code-review | 5W2H two-mode guidance is required. |
| M4 | T9, T10, T11, T14 | none | CMD1, CMD2, CMD3 | Plan validation notes, catalog validation output, focused pytest output. | M4 code-review | Full deleted-reference cleanup and catalog behavior required. |

## Test cases

### T1. Canonical method-kit files exist

- Covers: R1
- Level: integration
- Command IDs: CMD1
- Fixture/setup: repository checkout after each relevant milestone.
- Steps: Assert the four expected `method-kits/*.md` paths exist as they are introduced by milestone.
- Expected result: Required paths exist for completed milestones.
- Failure proves: canonical files are missing.
- Evidence artifact: focused pytest output.
- Automation location: `tests/test_markdown_first_method_guidance.py` or `tests/test_artifact_consistency.py`.
- Required by milestone: M1-M3

### T2. Method-kit metadata is reviewable

- Covers: R2
- Level: contract
- Command IDs: CMD1
- Fixture/setup: new method-kit files.
- Steps: Assert each completed kit exposes method ID, name, type, QCC stages, status, guide version, image policy, and automation policy through metadata or approved equivalent text.
- Expected result: Required metadata is present and parseable enough for review.
- Failure proves: guide cannot be reviewed consistently.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1-M3

### T3. Shared sections exist

- Covers: R3
- Level: contract
- Command IDs: CMD1
- Fixture/setup: new method-kit files.
- Steps: Assert required shared headings exist.
- Expected result: Every completed guide has the required method-kit structure.
- Failure proves: guide structure is incomplete.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1-M3

### T4. QCC project-story connection exists

- Covers: R4
- Level: contract
- Command IDs: CMD1
- Fixture/setup: new method-kit files.
- Steps: Assert each completed kit states its QCC project-story role and handoffs.
- Expected result: No guide reads as a disconnected tool page.
- Failure proves: stage-fit guidance is missing.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1-M3

### T5. Check Sheet safeguards

- Covers: R5, R6, E1, EC5
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/check-sheet.md`.
- Steps: Assert required Check Sheet terms and output-boundary cautions appear.
- Expected result: Guide distinguishes check sheet from checklist and covers observation discipline.
- Failure proves: Check Sheet guidance is unsafe or incomplete.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

### T6. Fishbone safeguards

- Covers: R7, R8, E2
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/fishbone-diagram.md`.
- Steps: Assert effect statement, categories, fact/hypothesis separation, evidence status, prioritization, and non-proof boundary.
- Expected result: Guide avoids root-cause overclaiming.
- Failure proves: Fishbone guidance is unsafe or incomplete.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M2

### T7. 5 Whys safeguards

- Covers: R9, R10, E3, EC4
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/five-whys.md`.
- Steps: Assert no exact-five requirement, branching allowance, fact/verification support, blame avoidance, actionable cause, and non-proof boundary.
- Expected result: Guide treats the chain as provisional evidence.
- Failure proves: 5 Whys guidance is unsafe or incomplete.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M2

### T8. 5W2H safeguards

- Covers: R11, R12, R13, E4
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/five-w-two-h.md`.
- Steps: Assert problem-framing mode, action-planning mode, required planning fields, and non-proof boundary.
- Expected result: Guide separates framing from action planning and avoids improvement claims.
- Failure proves: 5W2H guidance is unsafe or incomplete.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M3

### T9. Canonical navigation

- Covers: R14
- Level: integration
- Command IDs: CMD1
- Fixture/setup: README and `docs/qcc-project-story.md`.
- Steps: Assert canonical method-kit links appear in appropriate QCC project-story contexts.
- Expected result: Users navigate to `method-kits/`, not deleted guides.
- Failure proves: official guides are undiscoverable or stale links remain.
- Evidence artifact: focused pytest output.
- Automation location: artifact-consistency test.
- Required by milestone: M4

### T10. Deleted-reference cleanup

- Covers: R15, E5, EC1
- Level: integration
- Command IDs: CMD1
- Fixture/setup: repository Markdown, YAML, and tests.
- Steps: Scan live navigation, catalog, tests, and present-tense docs for active references to deleted `docs/methods/*.md`.
- Expected result: No active missing-path dependency remains; historical references are clearly historical if retained.
- Failure proves: deletion broke live references.
- Evidence artifact: focused pytest output.
- Automation location: artifact-consistency test.
- Required by milestone: M4

### T11. Catalog behavior after deletion

- Covers: R16, E5, EC2
- Level: integration
- Command IDs: CMD1, CMD2
- Fixture/setup: `templates/ppt/catalog.yml`.
- Steps: Validate catalog and assert official active entries do not point at missing deleted guides.
- Expected result: Catalog validation succeeds or intentionally reclassified historical entries are accepted by tested rules.
- Failure proves: catalog still depends on deleted files.
- Evidence artifact: catalog validation output.
- Automation location: catalog tests and validator.
- Required by milestone: M4

### T12. Extracted legacy content remains available and used

- Covers: R17, R18
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `docs/methods-key-content.md` and new method kits.
- Steps: Assert extraction file exists and each new method guide includes key concepts traceable to extracted content.
- Expected result: Useful legacy guidance is preserved without reviving old guide paths.
- Failure proves: deletion lost important source content.
- Evidence artifact: focused pytest output and manual review note.
- Automation location: focused docs test.
- Required by milestone: M1-M3

### T13. Visual policy

- Covers: R19, R20
- Level: contract
- Command IDs: CMD1
- Fixture/setup: method kits, optional media, and prompt records.
- Steps: Assert visuals are not required for every method and any added visual has prompt/review evidence and no final-evidence claims.
- Expected result: Visual policy follows conceptual-only constraints.
- Failure proves: generated-image policy is violated.
- Evidence artifact: focused pytest output and manual image review when relevant.
- Automation location: focused media test.
- Required by milestone: M2 when visuals are added; otherwise M4 guardrail

### T14. Out-of-scope guardrails

- Covers: R21
- Level: contract
- Command IDs: CMD1
- Fixture/setup: repository diff and relevant docs.
- Steps: Assert no Control Chart, SPC rules, control limits, process capability, broad automation, or named-tool tutorial scope is introduced.
- Expected result: Proposal non-goals are preserved.
- Failure proves: implementation exceeded approved scope.
- Evidence artifact: focused pytest output.
- Automation location: scope guard test.
- Required by milestone: M1-M4

## Fixtures and data

Fixtures are repository Markdown files, YAML catalog files, optional prompt/media files, and focused tests.
No private or production data is needed.

## Mocking/stubbing policy

No mocking is expected.
If catalog validation needs temporary fixtures, tests should use isolated temporary files rather than mutating repository assets.

## Migration or compatibility tests

T10 and T11 cover deletion migration and catalog compatibility.
Historical references may remain only when they are not active live dependencies.

## Observability verification

Failures should name the missing method, missing section, stale path, or violated guardrail.
No runtime logs, metrics, or traces are required.

## Security/privacy verification

Manual and automated checks should reject private operational names, secrets, credentials, or production-specific identifiers in examples, prompt records, and visuals.

## Performance checks

No performance benchmarks are required.
Focused docs checks should run locally without network access.

## Manual QA checklist

| Manual proof ID | Check | Required milestone |
|---|---|---|
| MP1 | Qualified reviewer confirms Check Sheet method correctness and no cause-proof overclaiming. | M1 |
| MP2 | Qualified reviewer confirms Fishbone method correctness and fact/hypothesis boundary. | M2 |
| MP3 | Qualified reviewer confirms 5 Whys method correctness, branching allowance, and no proof-by-repetition claim. | M2 |
| MP4 | Qualified reviewer confirms 5W2H two-mode behavior and no improvement-proof claim. | M3 |
| MP5 | Reviewer confirms extracted legacy content was consulted and important guidance was preserved. | M1-M3 |
| MP6 | Reviewer confirms optional visuals, if any, are conceptual-only and not final evidence. | M2 or M4 |

## What not to test and why

- Do not test Control Chart or SPC behavior because it is out of scope.
- Do not test runtime chart rendering for the new methods because no automation is approved.
- Do not require generated images for every method because the spec explicitly makes visuals optional.

## Uncovered gaps

None.

## Next artifacts

- Test-spec review.
- Implementation after clean test-spec-review.

## Follow-on artifacts

None yet

## Readiness

Ready for test-spec-review.
