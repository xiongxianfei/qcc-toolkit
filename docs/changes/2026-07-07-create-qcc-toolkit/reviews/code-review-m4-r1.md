# Code Review M4 R1: Method Guides and Template Catalog

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m4-r1.md`, `docs/changes/2026-07-07-create-qcc-toolkit/reviews/findings/CR-M4-001.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M4-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Reviewed milestone: M4
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M4, M5, M6, M7
- Required review-resolution: yes
- Finding IDs: CR-M4-001
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `b01b817` (`M4: add method guides and template catalog`)
- Tracked governing branch state: branch `proposal/create-qcc-toolkit`
- Governing artifacts:
  - `specs/qcc-toolkit-first-slice.md`
  - `specs/qcc-toolkit-first-slice.test.md`
  - `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
  - `docs/architecture/system/architecture.md`
  - `docs/adr/ADR-20260708-python-local-first-stack.md`
  - `docs/adr/ADR-20260708-evidence-package-boundary.md`
- Validation evidence:
  - `PATH=.venv/bin:$PATH python -m pytest tests`
  - `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests examples`
  - `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit`
  - `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - Reviewer direct catalog mutations for missing `markdown_guide`, `python_generator`, `example_project`, and mismatched guide method ID.

## Diff Summary

M4 adds Markdown method guides for the first-slice methods, reviewable PPT placeholder source files, a `templates/ppt/catalog.yml` catalog, a `qcc_toolkit.templates` catalog validation API and CLI, placeholder future paths for the M5 Pareto starter script and example project, and tests for method-guide and template-catalog contracts.

## Findings

### CR-M4-001: Catalog accepts mismatched method guide ownership

- Severity: major
- Location: `qcc_toolkit/templates/__init__.py:76-123`; `tests/test_template_catalog_failures.py:8-110`
- Evidence: T13 requires mutated catalog fixtures with missing paths, duplicate template IDs, mismatched guide method IDs, and unclassified coverage gaps.
  R48 requires automated checks to verify method IDs, template IDs, catalog paths, guide paths, script paths, and example project paths are consistent.
  The validator checks referenced paths and duplicate ownership, but it does not read the referenced guide front matter and compare guide `method_id` to catalog `method_id`.
  Reviewer mutation result:

```text
unexpected pass: mismatched catalog method_id and guide method_id was accepted
```

- Required outcome: Catalog validation must fail when a template entry's `markdown_guide` front matter declares a different `method_id` than the catalog entry.
  The M4 negative tests must include this mismatched guide method ID case.
- Safe resolution path: Parse the referenced Markdown guide front matter during catalog validation, compare its `method_id` with the catalog entry `method_id`, raise `CatalogValidationError` with entry and path details on mismatch, and add a failing-first test to `tests/test_template_catalog_failures.py`.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | concern | Method guides, template placeholder sources, catalog entries, and M4 CLI mostly align with R4-R20, R43, R48, AC3, AC4, AC8, AC11, and AC12, but CR-M4-001 leaves guide-method consistency unverified. |
| Test coverage | concern | Focused M4 tests and full `pytest tests` pass, but `tests/test_template_catalog_failures.py` omits the T13 mismatched guide method ID negative fixture. |
| Edge cases | concern | Missing template, missing guide, missing generator, missing example project, duplicate template ID, and duplicate method ownership are covered by tests or reviewer probes; mismatched guide method ownership is not rejected. |
| Error handling | concern | Catalog validation raises clear `CatalogValidationError` for missing paths and duplicate IDs, but not for guide ownership mismatch. |
| Architecture boundaries | pass | The implementation keeps template validation in `qcc_toolkit.templates`, leaves starter script functionality to M5, and does not move formula ownership into docs or templates. |
| Compatibility | pass | Public exports add template catalog types and validation functions without changing existing M1-M3 APIs. |
| Security/privacy | pass | Added examples are placeholders and method/template metadata; no real customer data, secrets, network calls, telemetry, web UI, CAPA/EQMS, automated PPTX, or Control Chart support were introduced. |
| Derived artifact currency | pass | Active plan, plan index, change metadata, and explanation were updated to M4 review-requested before review. |
| Unrelated changes | pass | The diff is scoped to M4 docs, template placeholders, catalog validator, tests, and lifecycle records. |
| Validation evidence | pass | Reviewer reran focused M4 tests, catalog CLI validation, full tests, Ruff, and mypy successfully; passing validation does not cover CR-M4-001. |

## Direct-Proof Gaps

- No automated M4 test proves mismatched catalog `method_id` and guide front-matter `method_id` fails validation.

## Residual Risks

- M4 remains open until CR-M4-001 is resolved and rereviewed.
- Functional starter script behavior, synthetic project data, regenerated evidence, and report integration remain assigned to later milestones.

## Handoff

M4 requires review-resolution for CR-M4-001.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
