# Review Resolution: Markdown-First Method Guides

## Status

- Current review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m3-r1.md`
- Current stage: code-review
- Reviewed milestone: M3
- Closeout status: closed
- Open findings: none

## Resolution Overview

| Finding | Final disposition | Owner decision needed | Re-review |
|---|---|---:|---|
| CR-M3-R1-F1 | resolved | no | closed by `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m3-r2.md` |

## Finding Disposition

### CR-M3-R1-F1

- Status: resolved
- Severity: major
- Required outcome: All generated report surfaces in the M3 review scope must consistently describe generated assets as optional aids alongside the method kit.
- Safe resolution path: Update `build_pareto_markdown_report()` to include optional-aid and method-kit boundary wording, add direct test coverage for that generated report output, and rerun focused compatibility/report tests before returning M3 to code review.
- Owner decision needed: no
- Resolution: `build_pareto_markdown_report()` now marks generated assets as optional aids alongside the method kit and identifies the evidence package as the authoritative calculation record only for the optional generated path. `tests/test_reports.py` now directly asserts that generated Pareto report output contains that boundary wording.
- Validation:
  - `.venv/bin/python -m pytest tests/test_reports.py -q` passed: 2 passed.
  - `.venv/bin/python -m pytest tests/test_artifact_consistency.py tests/test_first_slice_integration.py -q` passed: 4 passed.
  - `.venv/bin/python -m pytest` passed: 103 passed.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed: no issues in 13 source files.
  - `git diff --check` passed.

## Closeout Checklist

| Check | Status |
|---|---|
| All material findings have final dispositions. | closed |
| No finding requires owner decision. | closed |
| Required validation evidence is recorded. | closed |
| Same-stage re-review closed the original non-approval outcome. | closed |
| Review log records the re-review. | closed |
