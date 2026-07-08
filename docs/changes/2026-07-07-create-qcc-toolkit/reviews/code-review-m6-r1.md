# Code Review M6 R1: Report-Ready Outputs and First-Slice Integration

## Status

completed

## Review status

clean-with-notes

## Material findings

None.

## Recording status

recorded

## Reviewed scope

- Milestone: M6. Report-ready outputs and full first-slice integration
- Reviewed commit: `3f247f6`
- Plan: `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
- Spec: `specs/qcc-toolkit-first-slice.md`
- Test spec: `specs/qcc-toolkit-first-slice.test.md`

## Review inputs

- `git show --stat --oneline 3f247f6`
- `git show --no-ext-diff --unified=80 --no-renames 3f247f6 -- qcc_toolkit/reports.py`
- `git show --no-ext-diff --unified=80 --no-renames 3f247f6 -- examples/scripts/generate_pareto.py qcc_toolkit/__init__.py`
- `git show --no-ext-diff --unified=80 --no-renames 3f247f6 -- tests/test_reports.py tests/test_first_slice_integration.py`
- `git show --no-ext-diff --unified=80 --no-renames 3f247f6 -- tests/test_scope_guards.py tests/test_artifact_consistency.py`
- `git show --no-ext-diff --unified=80 --no-renames 3f247f6 -- README.md examples/projects/reduce-packing-label-errors/README.md examples/projects/reduce-packing-label-errors/report/.gitignore examples/projects/reduce-packing-label-errors/report/.gitkeep`
- Plan M6 handoff and validation notes
- Spec requirements R39-R44 and R45-R50
- Test-spec proof items T20-T22

## Diff summary

M6 adds project-level report generation in `qcc_toolkit.reports`, exporting `QccProjectReport` and `build_qcc_project_report` through the public package surface. The Pareto starter script now writes the existing method evidence package and then creates project-level `report/report.md` and `report/report.html`.

The report output references the generated chart artifact, chart specification, calculated table, caption, warnings, metadata, and evidence README. It includes the expected source-of-truth wording that the evidence package is the authoritative calculation record and manually edited slides are presentation artifacts.

The milestone also adds focused tests for report links and warnings, a first-slice integration test through the starter script, scope guard checks, artifact consistency checks, and README updates for the evidence-to-report workflow.

## Review checklist

- Requirements R39-R44: pass. The example workflow now creates report-ready Markdown and simple local HTML that reference the generated evidence package and preserve evidence authority.
- Requirements R45-R47: pass. No web UI, dashboard, CAPA/EQMS workflow, automated PPTX generation, Control Chart support, or AI-generated conclusion path was added.
- Requirements R48-R50: pass for M6 scope. Artifact consistency and full-regeneration checks remain automated or documented, and prior reproducibility coverage remains in the suite.
- Test-spec T20: pass. `tests/test_reports.py` checks report references, warning visibility, and authority language.
- Test-spec T21: pass. `tests/test_scope_guards.py` protects first-slice exclusions.
- Test-spec T22: pass. `tests/test_artifact_consistency.py` checks lifecycle and catalog path consistency.
- Architecture alignment: pass. Report generation consumes evidence artifacts and does not move formulas, validation, or chart calculations into report or slide code.
- Scope control: pass. The HTML report is a simple local artifact and does not introduce a document editor or new hosted rendering surface.

## Validation rerun

- `PATH=.venv/bin:$PATH python -m pytest tests/test_reports.py tests/test_scope_guards.py tests/test_artifact_consistency.py tests/test_first_slice_integration.py` passed with 4 tests.
- `PATH=.venv/bin:$PATH python -m pytest tests` passed with 57 tests.
- `PATH=.venv/bin:$PATH python -m ruff check .` passed.
- `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit` passed.
- `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed and validated 5 entries.
- `git diff --check` passed.
- Direct temporary-project probe regenerated `evidence/pareto`, `report/report.md`, and `report/report.html`; the report included the chart and warnings references, authoritative calculation record language, presentation-artifact language, and local HTML doctype.

## Residual risks and notes

- The HTML report is intentionally simple escaped local HTML. This is acceptable for M6 because Markdown remains the required report-ready output and HTML is a lightweight local presentation artifact.
- Final branch readiness is not claimed here. M7, explain-change, final verify, and PR handoff still need to run.

## Review resolution

not-required

## Milestone closeout

closed

## Immediate next stage

implement M7
