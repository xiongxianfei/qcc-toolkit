# Markdown-First Method Guidance Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/markdown-first-method-guidance.md`
- Plan: `docs/plans/2026-07-09-markdown-first-method-guidance.md`
- Architecture: `docs/architecture/markdown-method-guidance/architecture.md`
- Architecture review: `docs/changes/2026-07-09-markdown-first-method-guides/reviews/architecture-review-r1.md`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
|---|---|---|---|
| Proposal | `docs/proposals/2026-07-09-markdown-first-method-guides.md` | accepted, proposal-review approved | `proposal-review-r1` |
| Feature spec | `specs/markdown-first-method-guidance.md` | approved, spec-review approved | `spec-review-r1` |
| Architecture | `docs/architecture/markdown-method-guidance/architecture.md` | approved, architecture-review approved | `architecture-review-r1` |
| Plan | `docs/plans/2026-07-09-markdown-first-method-guidance.md` | active, plan-review approved | `plan-review-r1` |

## Testing strategy

Use automated Markdown and artifact-structure tests for deterministic repository checks.
Use manual proof only for reviewed binary teaching visuals, because visual quality and conceptual clarity cannot be fully proven from file structure.

Unit-style tests validate metadata files, required sections, evidence fields, prompt constraints, evidence levels, and tool-neutral language.
Integration tests validate complete method-kit directories and cross-links.
Smoke tests run focused pytest selections during milestones and broad pytest before final implementation closeout when feasible.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1 | T1, T6 | integration | Official kits must include Markdown guides. |
| R2 | T1 | unit | Front matter fields are checked. |
| R3 | T2 | unit | Required section headings are checked. |
| R4 | T3 | manual, integration | Application guidance is reviewed through required sections and reviewer checklist. |
| R5 | T4, T6 | integration | Chart-based kits require chart-creation guidance. |
| R6 | T4 | unit | Chart guide sections are checked. |
| R7 | T7 | integration | Pareto data-period and scope requirements are checked in chart guide. |
| R8 | T7 | integration | Pareto sorting requirement is checked. |
| R9 | T7 | integration | Pareto chart type and cumulative-line guidance are checked. |
| R10 | T4, T8 | unit, manual | Chart-quality standard fields and good/bad examples are checked. |
| R11 | T5 | integration | Image prompt directory path is checked. |
| R12 | T5, T8 | integration, manual | Teaching visual location and review evidence are checked. |
| R13 | T5 | unit | Prompt required sections are checked. |
| R14 | T5, T8 | unit, manual | Prompt and visual negative constraints are checked. |
| R15 | T5, T8 | manual | Text-light image policy is reviewed. |
| R16 | T9 | unit | Evidence levels are checked. |
| R17 | T9 | unit | E0 concept rule is checked. |
| R18 | T9, T10 | unit | E2 project-presentation evidence fields are checked. |
| R19 | T9, T10 | unit | E3 formal-review evidence fields are checked. |
| R20 | T9, T10 | unit, manual | E4 validated-path requirement is checked. |
| R21 | T10 | unit | Evidence note fields are checked. |
| R22 | T6 | integration | Pareto kit required files are checked. |
| R23 | T11 | unit | First-slice tool-neutral policy is checked. |
| R24 | T11 | unit | Named-tool recipes fail without user-test evidence marker. |
| R25 | T12 | integration | Optional automation remains secondary. |
| R26 | T1, T2, T6 | integration | QCC stage and related-method links are checked. |
| R27 | T9, T10 | unit | Evidence-state distinctions are checked. |
| R28 | T12 | integration | Existing Python/PPT assets are preserved and labeled optional or historical. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | T1, T2, T6 | Complete Pareto method-kit guide structure. |
| E2 | T4, T7 | Manual Pareto chart-creation guidance. |
| E3 | T5, T8 | Conceptual-only prompt and visual review. |
| E4 | T9, T10 | Evidence checklist and evidence-note fields. |
| E5 | T11 | Tool-class guidance without named-tool requirement. |

## Edge case coverage

| Edge case | Covered by | Notes |
|---|---|---|
| EC1 method has no chart | T2, T3 | Required worksheet/procedure and evidence sections remain present. |
| EC2 small data chart | T4, T11 | Tool-class guidance can recommend simple suitable tool classes. |
| EC3 high-rigor evidence | T9, T10 | E4 requires validated path or independent verification. |
| EC4 image with fake numbers | T5, T8 | Prompt and visual review reject fake precise values. |
| EC5 tool-neutral guidance too vague | T11, M3 review | Named-tool recipe requires user-test evidence in later spec. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `python -m pytest tests/test_method_guides.py tests/test_method_kit_closeout.py` | existing/configured | implement | M1 | M1 code-review | Failing tests block milestone review. | Zero collected tests fail the command under pytest strict config. | plan validation notes and code-review record | Local read/write only through pytest temp paths. |
| CMD2 | `python -m pytest tests/test_artifact_consistency.py` | existing/configured | implement | M3 | M3 code-review | Failing tests block milestone review. | Zero collected tests fail the command under pytest strict config. | plan validation notes and code-review record | Local repository inspection only. |
| CMD3 | `python -m pytest` | existing/configured | implement | M3 | final implementation closeout | Failing tests block final implementation closeout. | Zero collected tests fail the command under pytest strict config. | final code-review or verify evidence | Local test suite; no network required by design. |
| CMD4 | Markdown/link/prompt inspection command or focused pytest added by implementation | planned-for-implementation | implement | M1 | M1 code-review | Failing checks block official template promotion. | Zero checked files fail when official templates exist. | M1 validation notes | Local repository inspection only. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
|---|---|---|---|---|---|---|
| M1 | T1, T2, T4, T5, T9, T10, T11 | none | CMD1, CMD4 | M1 validation notes and code-review record | M1 code-review | Shared templates and checks must exist before Pareto kit promotion. |
| M2 | T3, T6, T7, T8, T10 | MAN1 when binary teaching visuals are added | CMD1, CMD4 | M2 validation notes, visual review notes if applicable | M2 code-review | Pareto kit proves the full model. |
| M3 | T11, T12 | none | CMD2, CMD3 | M3 validation notes and final code-review evidence | M3 code-review and final closeout | Compatibility and optional-aid alignment. |

## Test cases

T1. Method kit metadata
- Covers: R1, R2, R26, E1
- Level: unit
- Command IDs: CMD1, CMD4
- Fixture/setup: official method-kit guide Markdown files and metadata files.
- Steps: parse metadata and assert required keys and allowed values; assert user-facing guides start with the method title.
- Expected result: every official kit has method ID, stages, type, output, evidence risk, imagegen policy, final chart mode, related methods, version, and review status without forcing YAML into the user-facing guide opening.
- Failure proves: method identity and compatibility surfaces are incomplete.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T2. Required method-guide sections
- Covers: R3, R26, E1, EC1
- Level: unit
- Command IDs: CMD1, CMD4
- Fixture/setup: official method guide Markdown.
- Steps: assert required section headings exist in order or accepted equivalent order.
- Expected result: every official guide includes the required method instruction and review sections.
- Failure proves: guide is not complete enough for users or reviewers.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T3. Application guidance review
- Covers: R4, E1, EC1
- Level: manual
- Command IDs: none
- Fixture/setup: completed method guide and review checklist.
- Steps: reviewer confirms the guide teaches application, not only definitions.
- Expected result: review notes identify method purpose, procedure, interpretation, mistakes, and checklist coverage.
- Failure proves: guide quality is too theoretical.
- Evidence artifact: method-kit review notes.
- Automation location: manual proof.
- Required by milestone: M2

T4. Chart-creation guide completeness
- Covers: R5, R6, R10, E2, EC2
- Level: unit
- Command IDs: CMD1, CMD4
- Fixture/setup: chart-creation guide Markdown files.
- Steps: assert required sections and quality-standard fields are present.
- Expected result: chart guides cover data, preparation, tool class, construction, formatting, annotation, interpretation, defects, checklist, and evidence note.
- Failure proves: chart guidance is not executable.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T5. Image prompt constraints
- Covers: R11, R13, R14, R15, E3, EC4
- Level: unit
- Command IDs: CMD4
- Fixture/setup: prompt Markdown files under `docs/media/prompts/<method-id>/`.
- Steps: assert prompt files include purpose, use, prompt, negative constraints, conceptual-only wording, and no forbidden final-evidence language.
- Expected result: prompts are explicitly teaching-only and avoid exact numerical evidence requests.
- Failure proves: image-generation boundary is unsafe.
- Evidence artifact: focused check output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T6. Pareto method-kit required assets
- Covers: R1, R5, R22, R26, E1
- Level: integration
- Command IDs: CMD1, CMD4
- Fixture/setup: `method-kits/pareto-chart.md`, `method-kits/metadata/pareto-chart.yml`, `docs/media/prompts/pareto-chart/`, and `docs/media/pareto-chart/`.
- Steps: assert the flat method file, prompt path, inline worked example, and teaching-visual locations exist or have explicit pending-review markers allowed by implementation spec.
- Expected result: Pareto kit contains the first complete proof-kit structure.
- Failure proves: the first slice does not prove the proposed model.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M2

T7. Pareto chart-creation rules
- Covers: R7, R8, R9, E2
- Level: integration
- Command IDs: CMD1, CMD4
- Fixture/setup: Pareto chart-creation guide.
- Steps: inspect guide text or structured metadata for consistent period/scope, category/count data, descending sort, column bars, and cumulative-line guidance.
- Expected result: Pareto chart guidance includes all required construction rules.
- Failure proves: users cannot create a defensible Pareto chart from the guide.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M2

T8. Teaching visual review
- Covers: R10, R12, R14, R15, E3, EC4
- Level: manual
- Command IDs: none
- Fixture/setup: candidate good/bad examples or teaching visuals.
- Steps: reviewer checks conceptual-only status, no exact fake values, text-light design, method correctness, and no evidence confusion.
- Expected result: review notes approve or reject each teaching visual.
- Failure proves: visual teaching aid is unsafe or misleading.
- Evidence artifact: method-kit visual review notes.
- Automation location: manual proof.
- Required by milestone: M2

T9. Evidence level policy
- Covers: R16, R17, R18, R19, R20, R27, E4, EC3
- Level: unit
- Command IDs: CMD4
- Fixture/setup: evidence policy Markdown or structured evidence-level definitions.
- Steps: assert E0-E4 exist and contain required evidence expectations.
- Expected result: evidence levels distinguish concept, draft, project presentation, formal review, and audit/high-risk evidence.
- Failure proves: final chart evidence support is ambiguous.
- Evidence artifact: focused check output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T10. Evidence note template fields
- Covers: R18, R19, R20, R21, R27, E4
- Level: unit
- Command IDs: CMD1, CMD4
- Fixture/setup: evidence-note template Markdown files.
- Steps: assert required evidence-note fields are present.
- Expected result: final chart evidence notes preserve source, period, scope, tool, assumptions, exclusions, reviewer, and review status.
- Failure proves: reviewers cannot judge evidence readiness.
- Evidence artifact: pytest output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1

T11. Tool-neutrality enforcement
- Covers: R23, R24, E5, EC2, EC5
- Level: unit
- Command IDs: CMD4
- Fixture/setup: first-slice method-kit guides and tool guidance docs.
- Steps: scan for named-tool recipe markers and require explicit user-test evidence marker for any named-tool recipe.
- Expected result: first-slice guidance remains tool-class based.
- Failure proves: scope expanded into named-tool tutorials.
- Evidence artifact: focused check output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M1 and M3

T12. Optional aid compatibility
- Covers: R25, R28
- Level: integration
- Command IDs: CMD2, CMD3
- Fixture/setup: existing `docs/methods/`, `templates/ppt/`, `qcc_toolkit/`, and new method-kit surfaces.
- Steps: check that existing Python/PPT assets are retained and not described as overriding Markdown-first method guidance.
- Expected result: older assets remain optional or historical aids, and current method-kit guidance is primary.
- Failure proves: superseded direction still governs current user-facing identity.
- Evidence artifact: artifact consistency output and code-review record.
- Automation location: tests added or extended under `tests/`.
- Required by milestone: M3

## Fixtures and data

- `docs/templates/method-guide.md` and `docs/templates/image-prompts.md` provide template fixtures once M1 implements it.
- `method-kits/pareto-chart.md` provides inline synthetic Pareto sample data once M2 implements it.
- Existing synthetic example data may be reused only when it does not imply image-generated final evidence.

## Mocking/stubbing policy

No external services are required.
Image-generation output is represented by checked-in reviewed assets or pending-review placeholders.
Tests must not call image-generation services.

## Migration or compatibility tests

T12 covers compatibility with existing Python and PowerPoint assets.
No data migration is required.

## Observability verification

Test failures must name the missing section, field, prompt constraint, evidence level, or artifact path.
Manual review notes must name the visual or guide reviewed and the checklist result.

## Security/privacy verification

T5 and T8 verify prompt and visual boundaries.
T10 verifies evidence-note fields without requiring public raw private rows.
Sample data checks must confirm synthetic or approved sample data before official kit promotion.

## Performance checks

No performance-sensitive runtime is introduced.
Structure and Markdown checks should complete as ordinary local pytest checks.

## Manual QA checklist

MAN1. Teaching visual review
- Automation rationale: visual clarity and evidence-confusion risk require human judgment.
- Exact steps: inspect each candidate teaching image or good/bad example against conceptual-only, no fake numeric claims, text-light design, method correctness, and professional training quality.
- Required environment: local image viewer or rendered documentation preview.
- Evidence artifact: method-kit visual review notes stored with the kit or change evidence.
- Pass condition: reviewer records approved status and any required caveats.
- Failure condition: reviewer identifies misleading numbers, excessive text, method error, or evidence confusion.
- Owning stage: implement M2 and code-review M2.

## What not to test and why

- Do not test image-generation service output quality automatically; the repository does not depend on a service.
- Do not test named-tool tutorials in the first slice; named-tool recipes are out of scope.
- Do not test final quantitative chart generation from image generation; it is explicitly prohibited.
- Do not retest all Pareto calculation behavior unless implementation changes existing Python evidence code.

## Uncovered gaps

None.

## Next artifacts

- Test-spec review.
- Implementation after approved test-spec review.

## Follow-on artifacts

None yet

## Readiness

Active proof map ready for test-spec-review.
