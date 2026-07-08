# Code Review M4 R2: Catalog Guide Ownership Rereview

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m4-r2.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement M5
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m4-r2.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Reviewed milestone: M4
- Milestone closeout: closed
- Remaining implementation milestones: M5, M6, M7
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `6da87ba` (`M4: resolve catalog guide ownership review finding`)
- Tracked governing branch state: branch `proposal/create-qcc-toolkit`
- Prior finding under rereview: CR-M4-001
- Governing artifacts:
  - `specs/qcc-toolkit-first-slice.md`
  - `specs/qcc-toolkit-first-slice.test.md`
  - `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
  - `docs/architecture/system/architecture.md`
  - `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Validation evidence:
  - `PATH=.venv/bin:$PATH python -m pytest tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id tests/test_template_catalog_failures.py tests/test_template_catalog.py tests/test_method_guides.py tests/test_template_assets.py`
  - `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - Direct reviewer mutation probe for a Pareto catalog entry referencing `docs/methods/check_sheet.md`
  - `PATH=.venv/bin:$PATH python -m pytest tests`
  - `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests examples`
  - `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit`
  - `git diff --check`

## Diff Summary

The remediation adds Markdown guide front-matter ownership validation to `validate_template_catalog()`.
For each catalog entry, validation now reads the referenced `markdown_guide`, extracts its front matter `method_id`, compares it with the catalog entry `method_id`, and raises `CatalogValidationError` with the template ID, guide path, declared method ID, and expected method ID when they differ.
The remediation also adds a negative test for a Pareto template entry that incorrectly points to the Check Sheet guide.

## Findings

No blocking or required-change findings.

## Prior Finding Reconciliation

| Finding ID | Rereview result | Evidence |
|---|---|---|
| CR-M4-001 | resolved | `tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id` passed, and the direct mutation probe raised `CatalogValidationError` with `pareto_chart_template markdown_guide docs/methods/check_sheet.md declares method_id 'check_sheet', expected 'pareto_chart'.` |

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | EC8 requires mismatched guide method IDs to fail validation; EB9 requires catalog validation errors to identify the catalog entry and field. The remediation implements both for the reviewed path. |
| Test coverage | pass | The new negative test covers the prior gap, and the focused M4 suite passed with 13 tests. |
| Edge cases | pass | Missing paths, duplicate template IDs, duplicate method ownership, and mismatched guide ownership are now covered in catalog failure tests. |
| Error handling | pass | The mismatch error includes the template ID, `markdown_guide` field and path, actual guide `method_id`, and expected catalog `method_id`. |
| Architecture boundaries | pass | The fix remains inside `qcc_toolkit.templates` and does not move formula ownership into docs, templates, scripts, or examples. |
| Compatibility | pass | Public API names remain unchanged; validation is stricter for an invalid catalog state required to fail by the spec. |
| Security/privacy | pass | The change reads local Markdown guide files only and adds no network calls, telemetry, secrets, web UI, CAPA/EQMS, automated PPTX generation, or Control Chart scope. |
| Derived artifact currency | pass | Review-resolution, review log, change metadata, plan index, and active plan are updated by this review record. |
| Unrelated changes | pass | The reviewed diff is limited to catalog validation and its negative test. |
| Validation evidence | pass | Focused M4 tests, catalog CLI validation, full tests, Ruff, mypy, direct mutation proof, and `git diff --check` passed during rereview. |

## No-Finding Rationale

The prior finding was specific: catalog validation accepted a catalog entry whose `method_id` did not match the referenced Markdown guide front matter.
The remediation closes that behavior by validating the referenced guide's `method_id` during catalog validation and by adding a regression test for the mismatched-guide case.
The direct mutation proof independently confirmed the failing invalid state now raises `CatalogValidationError` with enough entry and path detail for a reviewer or user to correct the catalog.

## Residual Risks

- M5 still owns functional Pareto starter script behavior, synthetic project data, and regenerated evidence.
- M6 still owns integrated report-ready workflow output.
- M7 still owns lifecycle closeout preparation.

## Handoff

M4 is closed.
The next stage is `implement M5`.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
