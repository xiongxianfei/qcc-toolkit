# Code Review M5 R1: Starter Script and Synthetic Example Project

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m5-r1.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement M6
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m5-r1.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M5
- Milestone closeout: closed
- Remaining implementation milestones: M6, M7
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `a6f0760` (`M5: add Pareto starter script and synthetic project`)
- Tracked governing branch state: branch `proposal/create-qcc-toolkit`
- Governing artifacts:
  - `specs/qcc-toolkit-first-slice.md`
  - `specs/qcc-toolkit-first-slice.test.md`
  - `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
  - `docs/architecture/system/architecture.md`
  - `CONSTITUTION.md`
- Validation evidence:
  - `PATH=.venv/bin:$PATH python -m pytest tests/test_generate_pareto_script.py tests/test_example_project_e2e.py tests/test_example_project_structure.py tests/test_synthetic_data_only.py tests/test_reproducibility.py`
  - `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - Direct reviewer regeneration into `/tmp/qcc-review-m5/project/evidence/pareto`
  - Direct reviewer missing-column failure probe
  - Direct reviewer output-containment failure probe
  - `PATH=.venv/bin:$PATH python -m pytest tests`
  - `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests examples`
  - `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit`
  - `git diff --check`

## Diff Summary

M5 replaces the catalog placeholder Pareto starter script with a functional local CSV script.
The script accepts explicit input, category column, optional count column, project path, and output path arguments.
It reads local CSV records, delegates Pareto calculation and evidence writing to the public package API, writes method-scoped evidence output, returns non-zero on user-visible failures, and rejects output paths outside the selected project folder.

M5 also adds the synthetic `reduce-packing-label-errors` dataset, updates the example project README with the documented regeneration command, adds an ignored evidence output directory, and adds M5 tests for script delegation, end-to-end regeneration, missing-input and missing-column failure, example structure, synthetic-data markers, and reproducible calculated table/chart spec output.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | The diff addresses M5-owned R1-R2, R21-R24, R25, R32, R42, R48-R50, AC1, AC2, AC5, AC6, AC7, and AC9 without adding excluded UI, telemetry, dashboard, CAPA/EQMS, automated PPTX, Control Chart, or AI-conclusion scope. |
| Test coverage | pass | M5 adds `tests/test_generate_pareto_script.py`, `tests/test_example_project_e2e.py`, `tests/test_example_project_structure.py`, `tests/test_synthetic_data_only.py`, and `tests/test_reproducibility.py`; focused M5 tests passed with 7 tests. |
| Edge cases | pass | Tests and reviewer probes cover missing input file, missing required column, synthetic-data markers, reproducible output, and output path containment. Existing lower-layer tests continue covering empty data, invalid counts, blank categories, and evidence overwrite behavior. |
| Error handling | pass | Missing-column and output-containment probes returned non-zero and did not write success metadata or evidence files. |
| Architecture boundaries | pass | The starter script parses CLI/CSV inputs and delegates formulas, chart spec construction, captions, warnings, metadata, and evidence writing to public package APIs. |
| Compatibility | pass | Existing public package APIs remain unchanged; M4 catalog paths now point to functional M5 script and example-project paths. |
| Security/privacy | pass | The example data is explicitly synthetic, generated evidence excludes raw row dumps, the script uses local files only, and the output path must stay inside the selected project folder. |
| Derived artifact currency | pass | Template catalog validation still passes with 5 entries, and the plan/change metadata are updated by this review to close M5 and hand off to M6. Generated example evidence remains reproducible but ignored to avoid committing large self-contained Plotly HTML. |
| Unrelated changes | pass | The reviewed diff is scoped to M5 script behavior, synthetic example data, M5 tests, and lifecycle documentation. |
| Validation evidence | pass | Focused M5 tests, catalog validation, direct regeneration/failure probes, full tests, Ruff, mypy, and `git diff --check` passed during review. |

## No-Finding Rationale

The M5 script behavior is exercised both through direct unit-style monkeypatch delegation tests and subprocess end-to-end tests against the synthetic example project.
The generated evidence probe confirmed the required evidence files, successful metadata, chart spec method ID, calculated table content, and absence of a Plotly CDN URL in `chart.html`.
Failure probes confirmed missing-column and outside-project output paths fail before success metadata is written.

M6 still owns the broader report-ready output integration, but M5 provides the local script and synthetic project needed for that integration.

## Residual Risks

- M6 still owns full report-ready workflow integration and first-slice acceptance across reports.
- M7 still owns lifecycle closeout preparation.
- The starter script is intentionally CSV-first; Excel-like input support remains outside this M5 implementation unless a later spec expands it.

## Handoff

M5 is closed.
The next stage is `implement M6`.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
