# Test Spec Review R1: QCC Method Selection Summary

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-MS-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-13-qcc-method-selection-summary/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/2026-07-13-qcc-method-selection-summary/review-log.md`
- Review resolution: `docs/changes/2026-07-13-qcc-method-selection-summary/review-resolution.md`
- Open blockers: TSR-MS-001
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: manual proof procedure gap

## Findings

### TSR-MS-001 - Manual proof procedures are underspecified

- Finding ID: TSR-MS-001
- Severity: major
- Location: `specs/qcc-method-selection-summary.test.md`, `## Manual QA checklist`
- Evidence: MP1-MP4 name stable manual proof IDs and high-level checks, but they do not specify exact steps, required environment, pass condition, failure condition, or owning stage. The test-spec-review contract requires manual proof to be exact, justified, owned, evidenced, and bounded to cases where automation is impractical.
- Required outcome: Each manual proof ID must include enough procedural detail for implementation and review to execute or audit the scenario proof without guessing.
- Safe resolution path: Expand the manual QA checklist to include automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, and owning stage for MP1-MP4. Do not change the approved requirements or add new scenario scope.

## Review Dimensions

| Dimension | Verdict | Notes |
|---|---|---|
| Governing-contract alignment | pass | The test spec maps to the approved spec, architecture assessment, and plan. |
| Requirement coverage | pass | R1-R18 map to automated tests or manual proof. |
| Example coverage | pass | E1-E4 map to test IDs and manual proof IDs. |
| Negative and boundary coverage | pass | Future-method links, no-duplication, overclaiming, and automation scope are covered. |
| Proof-level adequacy | concern | Automated proof is adequate, but manual proof procedures need more detail. |
| Milestone mapping | pass | M1 maps to tests, manual proof IDs, commands, and evidence artifacts. |
| Command validity | pass | Commands are classified with owners, milestones, failure behavior, zero-test behavior, and side-effect boundaries. |
| Fixture and data design | pass | Fixtures are local Markdown files and method-kit paths. |
| Manual-proof boundary | block | Manual proof IDs lack exact executable/auditable procedure fields. |
| Observability | pass | Automated failures should identify missing selector, links, sections, status, or guardrails. |
| Determinism and isolation | pass | Planned checks are local repository inspections with no network or external side effects. |
| Scope and non-goals | pass | Proof map does not add runtime, charting, automation, or advanced-method scope. |
| Execution economics | pass | Focused checks are separated from broader documentation regression. |
| Traceability | pass | Requirement, example, edge case, test, command, milestone, and manual proof IDs are linked. |
| Implementation handoff | block | Implementation handoff needs clearer MP1-MP4 execution detail. |

## Recommendation

- Recommendation: changes-requested
- Next step: revise manual proof procedures, resolve TSR-MS-001, then rerun test-spec-review.
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
