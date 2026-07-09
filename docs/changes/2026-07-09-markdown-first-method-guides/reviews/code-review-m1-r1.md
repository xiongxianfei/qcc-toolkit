# Code Review M1 R1: Shared Guidance Templates and Validation

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m1-r1.md`, `docs/changes/2026-07-09-markdown-first-method-guides/review-log.md`, `docs/changes/2026-07-09-markdown-first-method-guides/change.yaml`, `docs/plans/2026-07-09-markdown-first-method-guidance.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement next milestone
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m1-r1.md`
- Review log: `docs/changes/2026-07-09-markdown-first-method-guides/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M1
- Milestone closeout: closed
- Remaining implementation milestones: M2, M3
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `ba94570` (`M1: add markdown-first guidance templates`)
- Tracked governing branch state: local `main` at commit `ba94570`
- Governing artifacts:
  - `CONSTITUTION.md`
  - `AGENTS.md`
  - `docs/proposals/2026-07-09-markdown-first-method-guides.md`
  - `specs/markdown-first-method-guidance.md`
  - `specs/markdown-first-method-guidance.test.md`
  - `docs/architecture/markdown-method-guidance/architecture.md`
  - `docs/plans/2026-07-09-markdown-first-method-guidance.md`
  - `docs/changes/2026-07-09-markdown-first-method-guides/reviews/test-spec-review-r1.md`
- Validation evidence:
  - `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py`
  - `git diff --check`

## Diff Summary

M1 adds the shared Markdown-first method-guidance surfaces and their focused validation.
The implementation introduces a reusable method-kit template under `method-kits/_template/`, shared chart-quality guidance under `docs/chart-creation/`, evidence levels and an evidence-note template under `docs/evidence/`, tool-class guidance under `docs/tool-guidance/`, and focused pytest checks in `tests/test_markdown_first_method_guidance.py`.

The same commit also records the accepted proposal, updated governance and vision artifacts, approved spec, approved architecture, approved plan, approved test spec, and upstream lifecycle reviews needed to make the M1 implementation reviewable from tracked repository state.

No Pareto method kit, named-tool tutorial, generated teaching image, final quantitative chart generation, Python evidence behavior, or PowerPoint template behavior is implemented in M1.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | M1 implements shared templates and checks assigned by the plan to R1-R21, R23-R24, and R26-R27. Pareto-specific R7-R9 and R22 remain assigned to M2; optional-aid alignment R25 and R28 remain assigned to M3. |
| Test coverage | pass | `tests/test_markdown_first_method_guidance.py` directly checks method-guide front matter and sections, chart-creation sections, image prompt constraints, evidence levels, evidence-note fields, tool-class guidance, and review checklist wording. |
| Edge cases | pass | The focused tests cover EC1 method-guide section completeness, EC2 tool-class guidance, EC3 E4 validated-path evidence, EC4 prompt rejection of fake precise values, and EC5 named-tool recipe deferral. |
| Error handling | pass | M1 adds repository documentation checks, not runtime IO or user-data processing. Missing artifacts, missing front matter, missing sections, unsafe prompt wording, and missing evidence fields fail through pytest assertions. |
| Architecture boundaries | pass | New files follow the approved method-kit-centered boundaries: `method-kits/_template/`, `docs/chart-creation/`, `docs/evidence/`, `docs/tool-guidance/`, and kit-local `assets/teaching-visuals/`. |
| Compatibility | pass | Existing Python and PowerPoint assets are not deleted. The new guidance positions them as optional aids through governance and vision updates while preserving prior implementation surfaces. |
| Security/privacy | pass | Prompt and evidence docs prohibit private operational data, customer names, employee names, supplier names, patient data, credentials, and unnecessary private raw rows. No network calls, services, dependencies, or telemetry are added. |
| Derived artifact currency | pass | Change metadata, review log, plan index, active plan, proposal/spec/architecture/test-spec records, README, vision, governance, and project map are updated together in tracked state. |
| Unrelated changes | pass | The broad governance and lifecycle artifact updates are part of the accepted Markdown-first direction and make the M1 implementation reviewable; product implementation remains bounded to shared templates and checks. |
| Validation evidence | pass | Reviewer reran `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py`; 16 tests passed. `git diff --check` also passed. |

## No-Finding Rationale

The implemented M1 files provide the required shared templates and validation surfaces without expanding into M2 Pareto kit content or M3 optional-aid compatibility work.
The new focused tests exercise the required M1 artifact paths and contract fields directly, and the existing method-guide and method-kit checks still pass.
The image-generation boundary is explicit in both prompt and chart-quality guidance, and final chart evidence remains tied to evidence levels and evidence-note fields.
Tool guidance uses classes of tools rather than named-product recipes, matching the first-slice non-goal.

## Residual Risks

- The shared templates are intentionally generic; M2 must prove that they produce a usable Pareto method kit.
- No binary teaching visuals are included in M1, so manual teaching-image review remains deferred to M2 when visuals or good/bad examples are added.
- System Python lacks pytest in this workspace; local validation used the repository virtualenv.

## Handoff

M1 is closed by this clean review.
The next stage is implementation of M2 according to the active plan.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
