# Code Review M3 R2: CR-M3-001 Rereview

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r2.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`, `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`, `docs/changes/2026-07-07-create-qcc-toolkit/change.yaml`, `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md`, `docs/plan.md`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M3-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r2.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3, M4, M5, M6, M7
- Required review-resolution: yes
- Finding IDs: CR-M3-001
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `d208bf7` (`M3: resolve local HTML rendering review finding`)
- Prior review: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/code-review-m3-r1.md`
- Prior finding: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/findings/CR-M3-001.md`
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
  - Direct generated HTML inspection for Plotly CDN strings.

## Diff Summary

The resolution changes Plotly rendering from `include_plotlyjs="cdn"` to `include_plotlyjs=True`.
It also updates `tests/test_chart_rendering.py` to reject external Plotly CDN script tags.

## Findings

### CR-M3-001: failed-remediation

- Severity: major
- Location: `tests/test_chart_rendering.py:24-27`; generated `chart.html`
- Evidence: The requested resolution said to add a test that fails if `chart.html` contains a Plotly CDN URL or `include_plotlyjs="cdn"` style output.
  The new test rejects `src="https://cdn.plot.ly` and `<script charset=`, but it does not reject all Plotly CDN URLs.
  Direct generated HTML inspection still finds `https://cdn.plot.ly/un/` inside the bundled Plotly JavaScript.
  Reviewer command output:

```text
src_cdn= False
cdn_url= True
cdn_index= 190745
nURL:{valType:"string",noBlank:!0,dflt:"https://cdn.plot.ly/un/"},mapboxAccessToken...
```

- Required outcome: Either make generated `chart.html` contain no `https://cdn.plot.ly` URL string and add a regression test for that condition, or update the accepted resolution/finding to explicitly permit inert CDN URL strings embedded inside self-contained Plotly JavaScript while still rejecting external CDN script loading.
- Safe resolution path: Prefer the stricter implementation requested by the finding and user instruction: add `assert "https://cdn.plot.ly" not in chart_html` and adjust rendering or post-processing so the generated HTML passes. If the team wants to allow inert bundled Plotly default URLs, route that as an explicit owner/spec decision before marking CR-M3-001 closed.

## Checklist Coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | concern | The external script dependency is removed, but the accepted review-resolution wording and user instruction required a test that fails on Plotly CDN URLs in `chart.html`; the current output still contains `https://cdn.plot.ly/un/`. |
| Test coverage | concern | Tests pass but do not prove the required no-Plotly-CDN-URL condition. |
| Edge cases | concern | The CDN-script form is covered; the literal CDN URL case is not. |
| Error handling | pass | No change to invalid input, PNG skip, or overwrite handling. |
| Architecture boundaries | concern | The generated artifact is closer to local-first behavior, but the approved proof condition remains unmet. |
| Compatibility | pass | Public API shape is unchanged. |
| Security/privacy | concern | No runtime network call is made during generation, but the proof surface still contains a CDN URL string that the required test was supposed to reject. |
| Derived artifact currency | pass | Change metadata and review-resolution state were updated before rereview. |
| Unrelated changes | pass | The diff is scoped to CR-M3-001 and lifecycle records. |
| Validation evidence | pass | Reviewer reran `pytest tests`, Ruff, and mypy successfully; direct HTML inspection exposes the remaining proof gap. |

## Residual Risks

- M3 remains open until CR-M3-001 is resolved or the accepted resolution is explicitly revised.

## Handoff

M3 requires review-resolution for CR-M3-001.
This review does not claim final verification, branch readiness, PR readiness, or CI success.
