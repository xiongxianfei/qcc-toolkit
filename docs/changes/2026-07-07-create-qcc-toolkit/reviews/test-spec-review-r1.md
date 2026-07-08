# Test Spec Review R1: QCC Toolkit First Slice

## Result

- Skill: test-spec-review
- Review status: changes-requested
- Material findings: TSR-001, TSR-002
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/2026-07-07-create-qcc-toolkit/review-log.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`
- Open blockers: TSR-001 and TSR-002 block implementation handoff
- Immediate next stage: test-spec revision
- Implementation handoff: not-allowed
- Stop condition: none

## Findings

## Finding TSR-001

- Finding ID: TSR-001
- Severity: material
- Location: `specs/qcc-toolkit-first-slice.test.md`, requirement coverage map and example coverage map
- Evidence: The requirement coverage map still references `M1`, `M2`, and `M3` as manual proof IDs for R11, R12, R13, and R44, and the example coverage map references `M1` for E4. The active manual proof IDs are `MAN1`, `MAN2`, and `MAN3` in the manual QA checklist and milestone proof map. Because `M1`, `M2`, and `M3` are also implementation milestone IDs, these rows are ambiguous.
- Required outcome: All requirement and example coverage rows that rely on manual evidence must reference the stable manual proof IDs or automated test IDs that actually provide the proof.
- Safe resolution path: Update R11 and R12 coverage to reference `MAN1` where demo-label or binary template inspection is required, update R13 coverage to reference `MAN2` where placeholder inspection is required, update R44 coverage to reference `MAN3` where manual slide-edit authority is required, and replace the E4 `M1` reference with the relevant test or manual proof ID. Keep milestone IDs only in the milestone proof map.
- needs-decision rationale: none

## Finding TSR-002

- Finding ID: TSR-002
- Severity: material
- Location: `specs/qcc-toolkit-first-slice.test.md`, manual QA checklist and security/privacy verification
- Evidence: The manual QA checklist defines `MAN1`, `MAN2`, and `MAN3` only as a check plus required milestone. The test-spec-review rules require manual proof to name a stable ID, automation rationale, exact steps, required environment, evidence artifact, pass condition, failure condition, and owning stage. The security/privacy section also states that T9 verifies output path behavior through temporary output directories, but the proof map does not name an explicit path-traversal or missing-input-file negative test for spec requirements S6 and EB1.
- Required outcome: Manual proofs must be executable review instructions, and required boundary/security behavior must have explicit automated proof or an explicit not-applicable rationale.
- Safe resolution path: Expand `MAN1`, `MAN2`, and `MAN3` into full manual proof records with automation rationale, exact steps, required environment, evidence artifact, pass/fail conditions, and owning stage. Add or amend automated test cases for missing input files and output path traversal, or record a precise not-applicable rationale if implementation design makes either case impossible.
- needs-decision rationale: none

## Review Dimensions

| Dimension | Verdict | Evidence |
|---|---|---|
| Governing-contract alignment | pass | The test spec follows the approved Pareto-centered first slice, local-first architecture, static-template boundary, and plan milestones. |
| Requirement coverage | concern | R1-R50 are present, but R11, R12, R13, R44, and E4 contain ambiguous manual proof references. |
| Example coverage | concern | E1-E5 are represented, but E4 references `M1` where a manual proof or test ID is expected. |
| Negative and boundary coverage | concern | Invalid Pareto data, catalog failures, PNG fallback, and reproducibility are covered; missing input file and path traversal proof are not explicit. |
| Proof-level adequacy | pass | Unit, integration, e2e, smoke, contract, and manual levels are mostly appropriate to behavior and risk. |
| Milestone mapping | pass | M1-M7 map cleanly to implementation boundaries and validation commands. |
| Command validity | pass | Planned commands identify classification, owner, milestone, failure behavior, zero-test behavior, evidence artifact, and side-effect boundary. |
| Fixture and data design | pass | Fixtures are deterministic, local, synthetic, and milestone-owned. |
| Manual-proof boundary | block | Manual proofs have stable IDs but lack required executable proof metadata. |
| Observability | pass | The proof map checks exit paths, output paths, structured warnings, metadata, report visibility, and failure evidence. |
| Determinism and isolation | pass | Reproducibility, no network calls, temp directories, deterministic captions, and generated fixtures are covered. |
| Scope and non-goals | pass | Scope guards cover web UI, dashboard, CAPA/EQMS, automated PPTX, Control Chart, advanced methods, and AI conclusions. |
| Execution economics | pass | Focused checks are introduced by milestone and expensive or optional rendering behavior is bounded. |
| Traceability | concern | ID traceability is strong overall, but stale manual proof references must be corrected before handoff. |
| Implementation handoff | block | Implementation cannot proceed until TSR-001 and TSR-002 are resolved and the revised test spec is re-reviewed. |

## Readiness

The active test spec is reviewable and close, but not approved.
Implementation remains blocked until a revised test spec resolves TSR-001 and TSR-002 and receives a fresh test-spec-review approval.
