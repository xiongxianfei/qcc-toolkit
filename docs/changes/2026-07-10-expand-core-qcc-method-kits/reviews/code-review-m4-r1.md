## Result

- Skill: code-review
- Status: completed
- Artifacts changed: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/code-review-m4-r1.md`, `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-log.md`, `docs/changes/2026-07-10-expand-core-qcc-method-kits/change.yaml`, `docs/plans/2026-07-10-expand-core-qcc-method-kits.md`, `docs/plan.md`
- Open blockers: none
- Next stage: final closeout
- Review status: clean-with-notes
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/code-review-m4-r1.md`
- Review log: `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-log.md`
- Review resolution: not-required
- Reviewed milestone: M4 - Navigation, Catalog, Deleted References, And Closeout Checks
- Milestone closeout: closed
- Remaining implementation milestones: none
- Required review-resolution: no
- Finding IDs: none
- Verify readiness: not-claimed

## Review inputs

- Diff/review surface: local diff for M4 navigation, catalog, deleted-reference, validator, tests, and lifecycle handoff artifacts.
- Tracked governing branch state: approved proposal, spec, test spec, plan, M1-M3 review records, M4 implementation, and M4 validation evidence are present in the working tree.
- Governing artifacts:
  - `CONSTITUTION.md`
  - `specs/expand-core-qcc-method-kits.md`
  - `specs/expand-core-qcc-method-kits.test.md`
  - `docs/plans/2026-07-10-expand-core-qcc-method-kits.md`
- Validation evidence:
  - Plan notes record the M4 focused tests failing before implementation because active docs and catalog entries still referenced deleted `docs/methods/` paths.
  - `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_scope_guards.py tests/test_method_kit_closeout.py tests/test_acceptance.py` passed with 53 tests.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed and validated 5 template catalog entries.
  - Reviewer reran targeted probes for deleted-reference cleanup, canonical catalog entries, mismatched guide validation, and catalog validation; all passed.

## Diff summary

M4 updates active navigation and catalog surfaces to canonical `method-kits/` paths.
`README.md` now describes the canonical method-kit root and lists Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H.
`docs/qcc-project-story.md` points the method links to canonical kits.
`docs/project-map.md` no longer presents `docs/methods/` as an active guide surface and instead identifies `docs/methods-key-content.md` as extracted source material.

`templates/ppt/catalog.yml` now marks all official first-slice entries as available method kits and sets each active `markdown_guide` to the canonical method-kit path.
`qcc_toolkit/templates/__init__.py` loads and validates optional `method_kit_status` and `method_kit` fields, requires available method-kit entries to match the active guide path, and accepts method IDs declared either inline in the method kit or in a metadata sidecar.

Tests now assert deleted legacy guide files are absent, active surfaces do not depend on deleted guide paths, official catalog entries point to canonical method kits, and the remaining first-slice method registry has canonical method-kit files.

## Findings

No blocking or required-change findings.

## Checklist coverage

| Check | Verdict | Evidence |
|---|---|---|
| Spec alignment | pass | Spec R14-R16 and R22 require canonical README/project-story links, no live deleted-path dependencies, official catalog entries that do not point at missing files, and focused local checks. The diff updates README, project-story, project-map, catalog, validator, and focused tests accordingly. |
| Test coverage | pass | `tests/test_artifact_consistency.py`, `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py`, `tests/test_method_guides.py`, and `tests/test_method_kit_closeout.py` cover deleted-reference cleanup, canonical catalog paths, validator mismatch behavior, and registry-to-kit consistency. |
| Edge cases | pass | Test spec EC1 and EC2 are covered: historical references remain outside live surfaces, and active catalog entries point to existing canonical method kits. Reviewer `rg` found deleted-path references only in extracted source material, historical proposals/plans/reviews, and guard-test constants. |
| Error handling | pass | The validator still fails mismatched guide method IDs. Reviewer reran `tests/test_template_catalog_failures.py::test_catalog_validation_fails_for_mismatched_guide_method_id`, which passed. |
| Architecture boundaries | pass | The change stays within Markdown navigation, catalog metadata, validator support, tests, and workflow records. It adds no new dependency, service, rendering backend, statistical automation, or external integration. |
| Compatibility | pass | The team-approved deletion decision is preserved: no compatibility notices are restored, and active references move to canonical method kits while historical references remain archival. |
| Security/privacy | pass | The diff contains generic documentation, local path metadata, and tests only. It adds no secrets, user data, network calls, telemetry, or external service dependency. |
| Derived artifact currency | pass | No generated images or derived binaries are changed in M4. Catalog validation and focused tests confirm the active catalog is synchronized with the canonical method-kit paths. |
| Unrelated changes | pass | The reviewed implementation surface matches M4 scope: navigation, catalog, deleted-reference checks, validator support, and lifecycle state. |
| Validation evidence | pass | M4 validation recorded 53 focused tests passing, catalog validator passing for 5 entries, and `git diff --check` passing. Reviewer additionally reran targeted deleted-reference/catalog probes and catalog validation. |

## No-finding rationale

The implementation satisfies the final M4 contract without restoring deleted guide files.
Active navigation and catalog surfaces point to existing canonical method kits, the validator supports the repository's two current method-ID declaration styles, and focused tests exercise the highest-risk deleted-reference and catalog-regression paths.
The remaining deleted-path strings are in extracted source material, historical workflow records, or guard tests, which is allowed by EC1 and does not create a live dependency.

## Residual risks

This is not final verification or PR readiness.
The full final closeout still needs the downstream lifecycle sequence, including durable change explanation and final verification.

## Milestone handoff

M4 is closed by this clean first-pass review.
No review-resolution is required.
No implementation milestones remain.
The next stage is final closeout, starting with `explain-change` unless workflow routing adds another required closeout step.
