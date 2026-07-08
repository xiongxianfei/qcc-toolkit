# Code Review M3 R3: CR-M3-001 Strict Rereview

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r3.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: implement M4
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r3.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: closed
- Remaining implementation milestones: M4, M5, M6, M7
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `4d4a418` (`M3: strictly remove Plotly CDN URLs`)
- Prior review: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r2.md`
- Prior finding: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/findings/CR-M3-001.md`
- Review resolution state: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Tracked governing branch state: branch `proposal/create-qcc-toolkit`
- Governing artifacts:
  - `specs/qcc-toolkit-first-slice.md`
  - `specs/qcc-toolkit-first-slice.test.md`
  - `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`
  - `docs/architecture/system/architecture.md`
  - `docs/adr/ADR-20260708-python-local-first-stack.md`
  - `docs/adr/ADR-20260708-evidence-package-boundary.md`
- Validation evidence:
  - Reviewer rerun: `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py`
  - Direct generated HTML inspection for Plotly CDN strings.
  - Plan validation notes record full-suite, Ruff, mypy, and `git diff --check` evidence from implementation handoff.

## Diff Summary

The strict remediation keeps Plotly self-contained HTML rendering with `include_plotlyjs=True`.
It post-processes generated HTML to replace `https://cdn.plot.ly` URL strings before writing `chart.html`.
It also extends `tests/test_chart_rendering.py` with the exact regression assertion `assert "https://cdn.plot.ly" not in chart_html`.

## Findings

No blocking or required-change findings.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | The generated `chart.html` remains the required local interactive chart artifact for R33 and no longer contains the Plotly CDN URL string that violated the local-first boundary in S3 and the architecture. |
| Test coverage | pass | `tests/test_chart_rendering.py` now asserts `Plotly.newPlot` exists, CDN script output is absent, and the exact forbidden string `https://cdn.plot.ly` is absent. Reviewer rerun of `PATH=.venv/bin:$PATH python -m pytest tests/test_chart_rendering.py` passed with 3 tests. |
| Edge cases | pass | The prior missed case, an inert bundled `https://cdn.plot.ly/un/` URL string inside self-contained Plotly JavaScript, is directly covered by the new exact assertion and direct generated-output inspection. |
| Error handling | pass | The diff does not change invalid input, optional PNG skip warning, overwrite, or evidence-package failure handling. |
| Architecture boundaries | pass | The renderer still builds HTML from the chart spec and evidence writer; it does not add network calls, services, telemetry, UI scope, or formula logic outside the method engine. |
| Compatibility | pass | Public API shape and evidence-package file names are unchanged; the change is limited to generated HTML contents and regression coverage. |
| Security/privacy | pass | Direct generated-output inspection shows no Plotly CDN URL string remains in `chart.html`; the change does not add secrets, credentials, telemetry, or raw row-level metadata. |
| Derived artifact currency | pass | Plan, review-resolution, review-log, and change metadata are updated to reflect strict CR-M3-001 remediation and M3 rereview. |
| Unrelated changes | pass | The reviewed code diff is scoped to `qcc_toolkit/evidence.py` and `tests/test_chart_rendering.py`; lifecycle edits are scoped to M3 review state. |
| Validation evidence | pass | Reviewer reran the focused chart-rendering test and directly generated/inspected HTML: `Plotly.newPlot=True`, `cdn_url=False`, `cdn_src=False`, `script_charset=False`. |

## No-Finding Rationale

CR-M3-001 required generated `chart.html` to be local/offline and required a test that fails on Plotly CDN URLs or CDN-style output.
The remediation now uses self-contained Plotly HTML mode, removes remaining Plotly CDN URL strings from the generated artifact, and adds the exact assertion requested by the finding and user instruction.
The focused regression test and direct generated-output inspection both prove the named missed edge case is resolved.

## Residual Risks

- The post-processing assumes Plotly's bundled JavaScript can tolerate replacement of the default CDN URL string.
  The generated chart still contains `Plotly.newPlot`, and the current test proves the artifact is generated without the forbidden URL, but broader browser rendering behavior should remain part of later manual or integration review if chart interactivity becomes a release gate.
- This is a milestone-local rereview only.
  M4-M7 remain open, so this review does not claim final verification, branch readiness, PR readiness, or CI success.

## Handoff

M3 is closed.
The next workflow stage is `implement M4`.
Final closeout is not ready because M4-M7, explain-change, verify, and PR handoff have not occurred.
