# Code Review M3 R1: Compatibility, Catalog, and Optional Aid Alignment

## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m3-r1.md`, `docs/changes/2026-07-09-markdown-first-method-guides/review-log.md`, `docs/changes/2026-07-09-markdown-first-method-guides/review-resolution.md`, `docs/plans/2026-07-09-markdown-first-method-guidance.md`, `docs/plan.md`, `docs/changes/2026-07-09-markdown-first-method-guides/change.yaml`
- Open blockers: none
- Next stage: review-resolution
- Review status: changes-requested
- Material findings: CR-M3-R1-F1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m3-r1.md`
- Review log: `docs/changes/2026-07-09-markdown-first-method-guides/review-log.md`
- Review resolution: `docs/changes/2026-07-09-markdown-first-method-guides/review-resolution.md`
- Reviewed milestone: M3
- Milestone closeout: resolution-needed
- Remaining implementation milestones: M3
- Required review-resolution: yes
- Finding IDs: CR-M3-R1-F1
- Verify readiness: not-claimed

## Review Inputs

- Diff/review surface: commit `999cec9` (`M3: align optional aids with markdown-first guidance`).
- Tracked governing branch state: `HEAD` on `main`; working tree was clean before review artifact recording.
- Governing artifacts: `CONSTITUTION.md`; `specs/markdown-first-method-guidance.md` R25, R28, I1, I6, O4; `specs/markdown-first-method-guidance.test.md` T12; `docs/architecture/markdown-method-guidance/architecture.md`; `docs/plans/2026-07-09-markdown-first-method-guidance.md` M3.
- Validation evidence inspected: M3 plan validation notes for focused artifact consistency tests, full pytest, ruff, mypy, template catalog validation, and `git diff --check`.
- Direct files inspected: `README.md`, `templates/ppt/catalog.yml`, `docs/methods/*.md`, `docs/project-map.md`, `qcc_toolkit/evidence.py`, `qcc_toolkit/reports.py`, `tests/test_artifact_consistency.py`, `tests/test_first_slice_integration.py`, `tests/test_reports.py`.

## Diff Summary

M3 updates the README and project map to point readers to the Pareto method kit as the current Markdown-first guide surface.
It adds optional-aid metadata to the PowerPoint template catalog, labels legacy `docs/methods/` guides as earlier optional-aid surfaces, and updates project-level generated report copy to describe generated outputs as optional aids alongside the method kit.
It also adds artifact consistency tests and adjusts integration assertions away from PowerPoint-template-first wording.

## Findings

## Finding CR-M3-R1-F1

- Finding ID: CR-M3-R1-F1
- Severity: major
- Location: `qcc_toolkit/reports.py:11`, `qcc_toolkit/reports.py:27`, `qcc_toolkit/evidence.py:134`, `tests/test_artifact_consistency.py:66`
- Evidence: `write_pareto_evidence_package()` still writes `report.md` through `build_pareto_markdown_report(files, interpretation.caption)`. That helper still emits only `The evidence package is the authoritative calculation record.` after `## Generated assets` and does not mark those generated assets as optional aids alongside the method kit. The new artifact-consistency test only concatenates source text from `qcc_toolkit/evidence.py` and `qcc_toolkit/reports.py`, so the updated project-report wording can satisfy `optional` and `method kit` while this public generated evidence report remains unaligned.
- Required outcome: All generated report surfaces in the M3 review scope must consistently describe generated assets as optional aids alongside the method kit and must not leave a generated evidence report without the Markdown-first boundary.
- Safe resolution path: Update `build_pareto_markdown_report()` to include the same optional-aid and method-kit boundary used by the project report, then add or update a direct test for `build_pareto_markdown_report()` or generated evidence-package `report.md` output. Rerun the focused compatibility tests plus the relevant report/evidence tests.
- needs-decision rationale: none

## Checklist Coverage

| Check | Result | Evidence |
|---|---|---|
| Spec alignment | concern | R25/R28 require optional automation to remain secondary and older Python/PPT assets to remain optional or historical. Most touched surfaces satisfy this, but generated evidence `report.md` from `build_pareto_markdown_report()` misses the boundary. |
| Test coverage | concern | `tests/test_artifact_consistency.py` checks source-text concatenation for `optional` and `method kit`, but does not directly assert the public `build_pareto_markdown_report()` output. |
| Edge cases | concern | T12's generated Python aid surface includes both project reports and evidence-package reports; only project report output has direct optional-aid wording. |
| Error handling | pass | M3 does not change invalid-state, permission, or fallback behavior. |
| Architecture boundaries | pass | The diff preserves method-kit primacy and keeps existing Python/PPT assets as optional aids without changing runtime architecture or dependencies. |
| Compatibility | concern | Existing assets are preserved, but one generated public report remains partially aligned and can still be read without the method-kit boundary. |
| Security/privacy | pass | No new secrets, external calls, telemetry, raw-data logging, or dependency changes were introduced. |
| Derived artifact currency | pass | No generated PPTX or binary teaching assets were changed; catalog validation remains the relevant derived-contract check. |
| Unrelated changes | pass | The diff is scoped to README, project map, optional-aid labels, generated report copy, workflow metadata, and tests for M3. |
| Validation evidence | pass | The cited validation commands are relevant, but passing validation does not cover the missed `build_pareto_markdown_report()` output. |

## No-Finding Rationale

Not applicable.
This first-pass review found one material issue requiring review-resolution before M3 can close.

## Direct-Proof Gaps

- No direct test currently asserts the `build_pareto_markdown_report()` output or generated evidence-package `report.md` includes optional-aid and method-kit boundary wording.

## Milestone Handoff State

- Reviewed milestone: M3
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Remaining in-scope implementation milestones: M3
- Next stage: review-resolution
- Final closeout readiness: not ready; M3 has an unresolved review finding.
