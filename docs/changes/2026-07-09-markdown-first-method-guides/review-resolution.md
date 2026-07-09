# Review Resolution: Markdown-First Method Guides

## Status

- Current review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/code-review-m3-r1.md`
- Current stage: review-resolution
- Reviewed milestone: M3
- Open findings: CR-M3-R1-F1

## Finding Disposition

### CR-M3-R1-F1

- Status: open
- Severity: major
- Required outcome: All generated report surfaces in the M3 review scope must consistently describe generated assets as optional aids alongside the method kit.
- Safe resolution path: Update `build_pareto_markdown_report()` to include optional-aid and method-kit boundary wording, add direct test coverage for that generated report output, and rerun focused compatibility/report tests before returning M3 to code review.
- Owner decision needed: no
