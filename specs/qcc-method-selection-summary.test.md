# QCC Method Selection Summary Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/qcc-method-selection-summary.md`
- Plan: `docs/plans/2026-07-13-qcc-method-selection-summary.md`
- Architecture/ADRs: `docs/changes/2026-07-13-qcc-method-selection-summary/architecture-assessment.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Feature spec | `specs/qcc-method-selection-summary.md` | approved | Status says approved; reviewed by `spec-review-r1`. |
| Spec review | `docs/changes/2026-07-13-qcc-method-selection-summary/reviews/spec-review-r1.md` | approved | No material findings. |
| Architecture assessment | `docs/changes/2026-07-13-qcc-method-selection-summary/architecture-assessment.md` | architecture-not-required | Existing Markdown documentation boundaries cover the change. |
| Plan | `docs/plans/2026-07-13-qcc-method-selection-summary.md` | active | Reviewed by `plan-review-r1`. |
| Plan review | `docs/changes/2026-07-13-qcc-method-selection-summary/reviews/plan-review-r1.md` | approved | No material findings. |

## Testing strategy

Use focused Markdown and artifact-consistency tests for deterministic repository checks.
Use manual scenario review for representative user and reviewer scenarios where judgment about method fit and interpretation boundaries is required.
No runtime, chart-rendering, API, migration, or generated-output tests are required because the approved change is documentation-only.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1 | integration | Verifies selector path exists. |
| R2 | T1, T2, T3 | contract | Verifies stage-question-evidence selection model and both entry views. |
| R3 | T3 | contract | Verifies canonical stage labels from QCC project-story. |
| R4 | T2 | contract | Verifies quick selection by project question. |
| R5 | T3 | contract | Verifies stage-oriented view. |
| R6, R7 | T3 | contract | Verifies primary/supporting use and no one-stage-only claim. |
| R8, R9 | T2, T3 | contract | Verifies expected input/evidence and typical output. |
| R10 | T4 | contract | Verifies interpretation boundaries for available methods. |
| R11, R12, R13 | T5 | integration | Verifies available links resolve and future methods are unlinked status text. |
| R14 | T6 | contract | Verifies maintenance note. |
| R15, R16 | T7 | integration | Verifies README and QCC project-story navigation link to selector without duplicating new matrix. |
| R17, R18 | T8 | contract | Verifies no full procedures, no generated catalog, no wizard, and no automation contract. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T3, MP1 | Stage view maps Current-state grasp to Check Sheet and Pareto Chart with proper role language. |
| E2 | T3, T4, MP2 | Cause analysis stage limits Pareto support to category focus, not root-cause proof. |
| E3 | T2, T4, MP3 | Question view maps paired numeric relationship to Scatter Diagram and causation boundary. |
| E4 | T3, T5, MP4 | Standardization and control uses future sustainment status without linking missing guides. |

## Edge case coverage

| Edge case | Covered by | Notes |
|---|---|---|
| EC1 | T3 | Multi-stage methods remain primary/supporting, not duplicated full guidance. |
| EC2 | T5 | Future sustainment guidance is status text until guides exist. |
| EC3 | T2 | Question-first users can navigate without stage knowledge. |
| EC4 | T2, T3, MP1 | Required input/evidence helps users pick collection or clarification methods when inputs are missing. |
| EC5 | T4 | Common overclaims have safe interpretation boundaries. |
| EC6 | T6 | Maintenance note covers later availability and relationship changes. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -k 'method_selection or qcc_project_story or navigation or method_links'` | planned-for-implementation | implement | M1 | M1 code-review | Failing assertions block M1 review handoff. | Zero collected tests is failure because focused selector checks are expected after implementation. | Plan validation notes and code-review record. | Local repository inspection only; no network or destructive side effects. |
| CMD2 | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` | existing/configured | implement | M1 | M1 code-review | Failing assertions block M1 review handoff. | Zero collected tests is failure because these files already contain tests. | Plan validation notes and code-review record. | Local repository inspection only; no network or destructive side effects. |
| CMD3 | `git diff --check` | existing/configured | implement | M1 | M1 code-review | Whitespace errors block M1 review handoff. | Not applicable. | Plan validation notes and code-review record. | Local diff inspection only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | T1-T8 | MP1-MP4 | CMD1, CMD2, CMD3 | Focused pytest output, manual scenario review note, plan validation notes. | M1 code-review | Tests should be added or updated before production documentation changes where practical. |

## Test cases

### T1. Selector exists and states the selection model

- Covers: R1, R2
- Level: integration
- Command IDs: CMD1
- Fixture/setup: repository checkout after M1 implementation.
- Steps: Assert `method-kits/README.md` exists and contains the stage, question, and available evidence/input decision model.
- Expected result: Selector exists and its introduction describes the combined selection model.
- Failure proves: The canonical selector is missing or the selection model is not visible.
- Evidence artifact: focused pytest output.
- Automation location: `tests/test_markdown_first_method_guidance.py` or `tests/test_artifact_consistency.py`.
- Required by milestone: M1

### T2. Question-oriented view covers method directions and inputs

- Covers: R2, R4, R8, R10, E3, EC3, EC4
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/README.md`.
- Steps: Assert the question view covers Check Sheet, Flowchart / Process Map, Pareto Chart, Histogram, Scatter Diagram, Fishbone Diagram, 5 Whys, and 5W2H with required input/evidence and safe boundary text.
- Expected result: Each required project question maps to a method direction, input/evidence condition, and interpretation boundary.
- Failure proves: Question-first users cannot select methods safely.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

### T3. Stage-oriented view uses canonical stages and primary/supporting roles

- Covers: R2, R3, R5, R6, R7, R8, R9, E1, E2, E4, EC1, EC4
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/README.md`.
- Steps: Assert the stage view covers Problem selection, Current-state grasp, Cause analysis, Countermeasure planning, Verification, and Standardization and control, and includes primary use, supporting use, typical output, and important limitation language.
- Expected result: Stage view preserves QCC story context without assigning methods to exactly one rigid stage.
- Failure proves: Stage-method guidance is incomplete or misleading.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

### T4. Interpretation guardrails prevent method overclaims

- Covers: R10, E2, E3, EC5
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/README.md`.
- Steps: Assert guardrails are present for all available methods and include no-cause, no-stability, no-causation, no-root-cause-proof, or no-effectiveness-proof language as appropriate.
- Expected result: Selector prevents prioritization, association, brainstorming, causal-chain, and action-planning outputs from being overclaimed.
- Failure proves: Selector can lead users to unsafe conclusions.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

### T5. Method status and link behavior are safe

- Covers: R11, R12, R13, E4, EC2
- Level: integration
- Command IDs: CMD1, CMD2
- Fixture/setup: `method-kits/README.md` and current `method-kits/*.md` files.
- Steps: Assert every available linked method guide exists, and Control Chart/SPC/process capability plus Standard Work/Visual Control/Monitoring Plan remain unlinked status text unless canonical guides exist.
- Expected result: Available methods link to real guides and future methods do not create dead links.
- Failure proves: Selector introduces stale status or dead links.
- Evidence artifact: focused pytest output.
- Automation location: focused docs or artifact-consistency test.
- Required by milestone: M1

### T6. Maintenance note covers later method changes

- Covers: R14, EC6
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/README.md`.
- Steps: Assert the selector includes a maintenance note requiring additions, renames, removals, status changes, and stage-fit changes to update the selector in the same change.
- Expected result: Contributor maintenance behavior is explicit.
- Failure proves: Selector can become stale without a documented maintenance rule.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

### T7. Root and QCC project-story navigation point to selector

- Covers: R15, R16
- Level: integration
- Command IDs: CMD1, CMD2
- Fixture/setup: `README.md`, `docs/qcc-project-story.md`, and `method-kits/README.md`.
- Steps: Assert README and QCC project-story link to `method-kits/README.md` and do not duplicate the new detailed selector matrix.
- Expected result: One canonical matrix exists in the selector; other documents link to it.
- Failure proves: Duplicate source-of-truth risk remains.
- Evidence artifact: focused pytest output.
- Automation location: artifact-consistency test.
- Required by milestone: M1

### T8. Scope guardrails prevent procedure and automation creep

- Covers: R17, R18
- Level: contract
- Command IDs: CMD1
- Fixture/setup: `method-kits/README.md`.
- Steps: Assert the selector does not contain full procedures, formula sections, chart recipes, worked examples, review checklists, generated catalog/schema claims, wizard wording, algorithm claims, or chart-generation behavior.
- Expected result: Selector remains concise Markdown navigation and does not become an implementation or method encyclopedia.
- Failure proves: Selector exceeds approved scope.
- Evidence artifact: focused pytest output.
- Automation location: focused docs test.
- Required by milestone: M1

## Fixtures and data

Fixtures are repository Markdown files and existing method-kit files.
No customer data, generated chart data, private operational data, or external service fixtures are required.

## Mocking/stubbing policy

No mocks or stubs are needed.
Tests should inspect local files directly.

## Migration or compatibility tests

No runtime migration tests are required.
Compatibility proof is limited to preserving existing method guide paths, linking only existing guides, and avoiding new automation or machine-readable contracts.

## Observability verification

Runtime observability is not applicable.
Documentation observability is provided by file existence, link checks, structure checks, status checks, and manual scenario review evidence.

## Security/privacy verification

Automated or manual checks should confirm the selector uses generic or synthetic scenario wording only and does not include real customer data, private operational data, secrets, credentials, private machine paths, or external-tool data-sharing instructions.

## Performance checks

Runtime performance checks are not applicable.
Manual review should confirm the selector remains concise enough to scan and does not copy full method-guide procedures.

## Manual QA checklist

| Manual proof ID | Automation rationale | Required environment | Exact steps | Pass condition | Failure condition | Evidence artifact | Owning stage |
|---|---|---|---|---|---|---|---|
| MP1 | Scenario judgment checks method fit and limitation wording together, which is clearer as bounded manual proof than brittle text matching alone. | Local repository with implemented selector and method guides. | Read the selector as a user with inconsistent defect observations; record the selected method, required input, and stated boundary. | Selection maps to Check Sheet or Check Sheet before Pareto, and the note preserves that observations do not prove cause. | Selection skips observation collection, maps directly to root cause, or omits the no-cause boundary. | `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` | implement M1 before code-review |
| MP2 | Scenario judgment checks whether prioritization is distinguished from causation. | Local repository with implemented selector and method guides. | Read the selector as a user prioritizing defect categories; record the selected method, required input, and stated boundary. | Selection maps to Pareto Chart with category counts, period, scope, and no-root-cause boundary. | Selection treats Pareto rank as root-cause proof or omits category-count input conditions. | `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` | implement M1 before code-review |
| MP3 | Scenario judgment checks relationship exploration and causation boundary together. | Local repository with implemented selector and method guides. | Read the selector as a user asking whether two measured variables appear related; record the selected method, required input, and stated boundary. | Selection maps to Scatter Diagram with paired numeric observations and no-causation boundary. | Selection permits unpaired data, claims causation, or omits pairing and unit requirements. | `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` | implement M1 before code-review |
| MP4 | Reviewer judgment checks future sustainment status wording and dead-link safety. | Local repository with implemented selector and method guides. | Review the Standardization and control row and method status table; record whether future sustainment guidance is clearly labeled and unlinked unless guides exist. | Standard Work, Visual Control, and Monitoring Plan are status-labeled as future sustainment guidance and do not link to missing guides. | Future guidance appears available, links to missing guides, or implies unsupported sustainment procedures. | `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` | implement M1 before code-review |

## What not to test and why

- Do not test Control Chart, SPC, process capability, Standard Work, Visual Control, or Monitoring Plan procedure content because this slice only labels their status.
- Do not test chart rendering, calculations, Python APIs, generated catalogs, or recommendation algorithms because the spec excludes them.
- Do not test every detailed method-guide procedure because the selector links to those guides rather than duplicating them.

## Uncovered gaps

None.

## Next artifacts

- Test-spec review for this proof map.
- Implementation of M1 after test-spec-review approval.

## Follow-on artifacts

- [Test Spec Review R1](../docs/changes/2026-07-13-qcc-method-selection-summary/reviews/test-spec-review-r1.md)
- [Test Spec Review R2](../docs/changes/2026-07-13-qcc-method-selection-summary/reviews/test-spec-review-r2.md)

## Readiness

Approved for implementation handoff.

Implementation may begin at M1 on a separate request or workflow continuation.
