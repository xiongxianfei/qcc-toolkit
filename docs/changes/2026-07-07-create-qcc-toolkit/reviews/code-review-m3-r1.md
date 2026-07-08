# Code Review M3 R1: Chart Specifications and Evidence Packages

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r1.md`, `docs/changes/2026-07-07-create-qcc-toolkit/reviews/findings/CR-M3-001.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M3-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3, M4, M5, M6, M7
- Required review-resolution: yes
- Finding IDs: CR-M3-001
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `4879210` (`M3: generate Pareto chart specs and evidence packages`)
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
  - `PATH=.venv/bin:$PATH python -m ruff check qcc_toolkit tests`
  - `PATH=.venv/bin:$PATH python -m mypy qcc_toolkit`

## Diff Summary

M3 adds renderer-independent Pareto chart specifications, Plotly HTML rendering, optional PNG exporter handling, evidence package writing, warning serialization, and a Markdown report fragment.
It also adds tests for chart spec structure, rendering behavior, PNG skip warnings, evidence package files and metadata, overwrite behavior, warning serialization, and reproducibility of chart specs and calculated tables.

## Findings

### CR-M3-001: HTML chart output depends on Plotly CDN

- Severity: major
- Location: `qcc_toolkit/evidence.py:182`
- Evidence: `_render_plotly_html()` calls `figure.to_html(full_html=True, include_plotlyjs="cdn")`, which writes an HTML artifact that references an external CDN for Plotly JavaScript.
  The approved spec says the first slice must run locally by default and must not transmit project data over a network.
  The architecture states that the first slice is local-first, performs no network transmission, and needs no external service.
  The test spec also says network calls are not expected and should require upstream approval.
- Required outcome: Generated `chart.html` must be usable as a local evidence artifact without depending on an external CDN or network resource.
  The M3 tests should assert the generated HTML does not contain external Plotly CDN references.
- Safe resolution path: Use Plotly's self-contained HTML mode, such as `include_plotlyjs=True`, or another local/offline rendering approach.
  Add a test that fails if `chart.html` contains a Plotly CDN URL or `include_plotlyjs="cdn"` style output.
  Rerun M3 validation after the fix.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | concern | The chart spec, evidence package files, optional PNG warning, report output, and metadata largely match R30-R44, R49, and R50, but CR-M3-001 violates the local-first/network boundary for the required HTML artifact. |
| Test coverage | concern | T7-T10 are covered by tests, and reviewer-run validation passes, but no test catches external CDN references in generated `chart.html`. |
| Edge cases | pass | Tests cover PNG unavailable warnings, explicit overwrite behavior, stale method-owned PNG removal, warning serialization, deterministic chart spec output, and deterministic calculated table output. |
| Error handling | pass | Existing output folders fail unless `overwrite=True`; optional PNG unavailability records an `export_skipped` warning and preserves non-PNG artifacts. |
| Architecture boundaries | concern | Package boundaries match the architecture, but `include_plotlyjs="cdn"` conflicts with the local-first renderer boundary. |
| Compatibility | pass | Public facade exports the new chart/evidence/report functions and preserves the package version surface through `_version.py`. |
| Security/privacy | concern | The implementation does not send network traffic during generation, but the produced HTML requires a network resource to render interactively, which is inconsistent with the local-first first-slice boundary. |
| Derived artifact currency | pass | Plan, change metadata, and change explanation were updated to M3 review-requested state before review. |
| Unrelated changes | pass | Product changes are limited to M3 chart, evidence, report, and test surfaces; lifecycle changes are workflow records. |
| Validation evidence | pass | Reviewer reran `pytest tests`, Ruff, and mypy successfully in the local `.venv`; passing checks do not cover CR-M3-001. |

## Direct-Proof Gaps

- No current test proves `chart.html` is self-contained or free of external CDN references.

## Residual Risks

- M3 remains open until CR-M3-001 is resolved and rereviewed.
- Starter script and example-project regeneration remain assigned to M5.
- Method guides, templates, and catalog validation remain assigned to M4.

## Handoff

M3 requires review-resolution for CR-M3-001.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
