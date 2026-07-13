# Expand Seven Basic Quality Tools Guidance Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/expand-seven-basic-quality-tools-guidance.md`
- Plan: `docs/plans/2026-07-09-expand-seven-basic-quality-tools-guidance.md`
- Architecture/ADRs: not required; architecture assessment is recorded in `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/change.yaml`

## Input artifact identities

| Input | Path | Status / Review state | Identity |
|---|---|---|---|
| Proposal | `docs/proposals/2026-07-09-expand-seven-basic-quality-tools-guidance.md` | accepted | Proposal review R3 approved post-imagegen scope. |
| Feature spec | `specs/expand-seven-basic-quality-tools-guidance.md` | approved | Spec-review R1 approved the contract. |
| Spec review | `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/reviews/spec-review-r1.md` | approved | No material findings. |
| Architecture assessment | `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/change.yaml` | architecture-not-required | Existing Markdown-first architecture owns method-kit and media boundaries. |
| Plan | `docs/plans/2026-07-09-expand-seven-basic-quality-tools-guidance.md` | active | Plan-review R1 approved the milestone sequence. |
| Plan review | `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/reviews/plan-review-r1.md` | approved | No material findings. |

## Testing strategy

Unit-style documentation tests should inspect Markdown files, prompt records, and navigation links using deterministic file reads.
Integration-style artifact checks should confirm cross-file consistency among method kits, prompt records, media paths, README, and `docs/qcc-project-story.md`.
Manual proof is required only for generated teaching-image visual quality because binary image usefulness, misleading visual authority, and text legibility cannot be fully verified by text tests.

No end-to-end browser, service, network, external image-generation, migration, or release-owned validation is required for this slice.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1 | T1 | unit | Confirms three method-kit files exist. |
| R2 | T1 | unit | Confirms lightweight metadata/front matter fields. |
| R3 | T1 | unit | Confirms shared method-kit sections. |
| R4 | T2, T6 | unit, integration | Confirms QCC project-story fit in method text and navigation. |
| R5 | T2 | unit | Confirms Flowchart / Process Map required content. |
| R6 | T3 | unit | Confirms Histogram required content and cautions. |
| R7 | T4 | unit | Confirms Scatter Diagram required content and cautions. |
| R8 | T5 | unit | Confirms manual creation guidance and tool-neutrality. |
| R9 | T7 | unit | Confirms Control Chart and SPC scope guards. |
| R10 | T7 | unit | Confirms chart-rendering automation scope guard. |
| R11 | T8 | unit | Confirms prompt records for each method. |
| R12 | T9, MAN1 | integration, manual | Confirms media assets are linked and manually reviewed. |
| R13 | T8 | unit | Confirms required prompt-record fields. |
| R14 | T8, T9, MAN1 | unit, integration, manual | Confirms negative constraints and visual review. |
| R15 | T8, MAN1 | unit, manual | Confirms text-light image policy and Markdown-owned instructions. |
| R16 | T9, MAN1 | integration, manual | Confirms Flowchart visual set. |
| R17 | T9, MAN1 | integration, manual | Confirms Histogram visual set. |
| R18 | T9, MAN1 | integration, manual | Confirms Scatter visual set. |
| R19 | T6 | integration | Confirms README links. |
| R20 | T6 | integration | Confirms QCC project-story links. |
| R21 | T1, T2, T3, T4, T5, T6, T7, T8, T9, MAN1 | unit, integration, manual | Confirms focused checks exist for required surfaces. |
| R22 | T7 | unit | Confirms legacy optional surfaces remain available. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | T2 | Flowchart current-state guidance coverage. |
| E2 | T3 | Histogram variation and no-stability guidance coverage. |
| E3 | T4 | Scatter paired-variable and no-causation guidance coverage. |
| E4 | T8, T9, MAN1 | Prompt-record and generated-image review coverage. |
| E5 | T6 | README and QCC project-story navigation coverage. |

## Edge case coverage

| Edge case | Covered by | Notes |
|---|---|---|
| EC1 | T8, T9 | Completed method-kit image claims require prompt records and media links. |
| EC2 | MAN1 | Manual review rejects inaccurate, unreadable, or misleading generated image text. |
| EC3 | T3 | Histogram guide must include small sample and binning cautions. |
| EC4 | T4 | Scatter guide must include no-root-cause-proof and correlation-versus-causation cautions. |
| EC5 | T2, MAN1 | Flowchart guide and visual review distinguish current-state map from SOP/evidence. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py` | planned-for-implementation | implement | M3 | M3 code-review | Failing assertions block M3 review handoff. | Zero collected tests is failure because focused docs checks are expected. | M3 validation notes in active plan and later review evidence. | Local read-only test run; no network, publication, or destructive side effects. |
| CMD2 | `pytest` | existing/configured | implement | M3 | M3 code-review when shared tests or package surfaces change | Failure blocks M3 review handoff or requires scoped rationale if not applicable. | Zero collected tests is failure because pytest is configured for repository tests. | M3 validation notes in active plan and later review evidence. | Local test run; no network, publication, or destructive side effects expected. |
| CMD3 | `git diff --check` | existing/configured | implement | M1 | M1 code-review | Whitespace errors block review handoff. | Not applicable. | Each milestone validation notes. | Local Git check only. |
| CMD4 | Manual image review checklist | planned-for-implementation | implement/reviewer | M2 | M2 code-review | Missing or failed checklist blocks M2 review handoff for linked teaching visuals. | Not applicable. | Prompt records or image-review notes under `media/prompts/<method-id>/`. | Manual inspection of local generated assets; no external calls required during review. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
|---|---|---|---|---|---|---|
| M1 | T1, T2, T3, T4, T5, T7 | none | CMD3 | Plan validation notes and code-review packet. | M1 code-review | Focused pytest may not exist until M3, so M1 requires direct file inspection plus diff hygiene. |
| M2 | T8, T9 | MAN1 | CMD3, CMD4 | Prompt records, image-review notes, plan validation notes, code-review packet. | M2 code-review | Imagegen output must be manually reviewed before method-guide links are considered complete. |
| M3 | T1, T2, T3, T4, T5, T6, T7, T8, T9 | MAN1 when images are linked | CMD1, CMD2 when triggered, CMD3 | Test output, plan validation notes, code-review packet. | M3 code-review | M3 completes focused automated coverage and navigation checks. |

## Test cases

T1. New method-kit files and shared sections
- Covers: R1, R2, R3, AC1
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Repository with implemented method-kit files.
- Steps: Read `method-kits/flowchart.md`, `method-kits/histogram.md`, and `method-kits/scatter-diagram.md`; assert required metadata/front matter and shared headings.
- Expected result: All three files exist and include required metadata and guide sections.
- Failure proves: The method kits are incomplete or not reviewable as Markdown-first guides.
- Evidence artifact: `tests/test_markdown_first_method_guidance.py` or equivalent focused test output.
- Automation location: planned in `tests/test_markdown_first_method_guidance.py` or a similarly scoped docs test.
- Required by milestone: M3

T2. Flowchart / Process Map required guidance
- Covers: R4, R5, E1, EC5, AC2
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented Flowchart / Process Map method kit.
- Steps: Read `method-kits/flowchart.md`; assert QCC project-story fit, start/end boundaries, process steps, decision points, handoffs, queues, rework loops, failure or defect locations, and current-state versus future-state distinction.
- Expected result: Flowchart guidance covers current-state process understanding and does not become generic diagramming advice.
- Failure proves: The guide lacks required process-map substance or QCC fit.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs test.
- Required by milestone: M3

T3. Histogram required guidance
- Covers: R6, E2, EC3, AC2
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented Histogram method kit.
- Steps: Read `method-kits/histogram.md`; assert numeric data requirement, sample-size caution, bin-width caution, outlier handling, distribution-shape interpretation, before/after cautions, and no process-stability claim.
- Expected result: Histogram guidance teaches variation interpretation with explicit limits.
- Failure proves: Users could overinterpret weak histogram evidence.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs test.
- Required by milestone: M3

T4. Scatter Diagram required guidance
- Covers: R7, E3, EC4, AC2
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented Scatter Diagram method kit.
- Steps: Read `method-kits/scatter-diagram.md`; assert paired numeric observations, x/y variable definitions, axis labels and units, outlier handling, correlation-versus-causation warning, and no root-cause-proof claim.
- Expected result: Scatter guidance teaches relationship exploration without causal overclaiming.
- Failure proves: Users could mistake correlation for proof of root cause.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs test.
- Required by milestone: M3

T5. Tool-neutral manual creation guidance
- Covers: R8, AC6
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented method kits.
- Steps: Read all three method kits; assert manual chart or diagram recipe content and absence of required named-tool tutorials.
- Expected result: Guides teach creation steps and quality standards while staying tool-neutral.
- Failure proves: The implementation violates the project identity or leaves manual creation under-specified.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs test.
- Required by milestone: M3

T6. README and QCC project-story navigation
- Covers: R4, R19, R20, E5, AC5
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Implemented method kits plus README and project-story updates.
- Steps: Read `README.md` and `docs/qcc-project-story.md`; assert links or references to the three method kits and correct project-stage context.
- Expected result: Users can discover the new methods from repository navigation and project-story guidance.
- Failure proves: Method kits are disconnected pages.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs or artifact-consistency test.
- Required by milestone: M3

T7. Scope guards and legacy preservation
- Covers: R9, R10, R22, AC7
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented repository state.
- Steps: Check changed method-kit and navigation surfaces for absence of Control Chart implementation, SPC rules, control-limit calculations, process capability, run-rule automation, Histogram/Scatter renderers, and named-tool tutorial commitments; assert older optional guide/template/Python surfaces still exist.
- Expected result: The slice stays within approved scope and preserves legacy optional assets.
- Failure proves: The implementation exceeded the proposal/spec boundary or removed unrelated assets.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs or artifact-consistency test.
- Required by milestone: M3

T8. Prompt-record completeness and negative constraints
- Covers: R11, R13, R14, R15, E4, EC1, AC3
- Level: unit
- Command IDs: CMD1
- Fixture/setup: Implemented prompt records for each required teaching visual.
- Steps: Read `media/prompts/flowchart/`, `media/prompts/histogram/`, and `media/prompts/scatter-diagram/`; assert purpose, intended use, final prompt, negative constraints, conceptual-only policy, output path, and review status.
- Expected result: Prompt records are complete and forbid fake data, fake percentages, private identifiers, final-evidence claims, causal proof claims, and process-stability claims.
- Failure proves: Image generation cannot be reviewed safely.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs test.
- Required by milestone: M3

T9. Teaching visual path and link consistency
- Covers: R12, R14, R16, R17, R18, EC1, AC4
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Implemented prompt records, media assets, and method-guide links.
- Steps: Assert each required prompt output path exists under the method-scoped media directory, each method guide links to its teaching visuals or review notes, and required visual purposes are represented for each method.
- Expected result: Visual assets are discoverable, method-scoped, and tied to prompt records.
- Failure proves: The teaching-image set is incomplete or untraceable.
- Evidence artifact: Focused pytest output.
- Automation location: planned docs or artifact-consistency test.
- Required by milestone: M3

MAN1. Generated teaching-image conceptual review
- Covers: R12, R14, R15, R16, R17, R18, E4, EC2, EC5, AC4
- Level: manual
- Command IDs: CMD4
- Fixture/setup: Generated or created teaching visuals exist locally at their prompt-record output paths.
- Steps: Reviewer opens each image and checks that it is conceptual-only, text-light, readable, non-private, free of exact fake values or percentages, free of causal arrows or proof claims, free of process-stability claims, and not confused with final evidence.
- Expected result: Each image passes the checklist or is removed, regenerated, or unlinked before review handoff.
- Failure proves: The visual may mislead users or violate the generated-image evidence boundary.
- Evidence artifact: Prompt record or adjacent review note with review status, reviewer, date, and pass/fail notes.
- Automation location: manual review record.
- Required by milestone: M2 and M3 when images are linked.

## Fixtures and data

Fixtures are repository Markdown files, prompt records, generated teaching visuals, README, and `docs/qcc-project-story.md`.
Example method-kit data must be synthetic or generic.
No private operational datasets are required.

## Mocking/stubbing policy

No mocks or stubs are required.
Tests should inspect repository files directly.
Image generation itself is not mocked in the proof map; generated image review is manual and evidence-based.

## Migration or compatibility tests

T7 covers compatibility by asserting older optional `docs/methods/`, `templates/ppt/`, and `qcc_toolkit/` surfaces remain available.
No data migration tests are required.

## Observability verification

T1 through T9 verify reviewer-visible artifacts and links.
No logs, metrics, traces, or audit events are introduced.

## Security/privacy verification

T8 and MAN1 verify prompt records and teaching visuals do not contain private identifiers, secrets, credentials, production details, fake precise values, or final-evidence claims.

## Performance checks

No performance-specific tests are required.
The focused documentation tests should remain local file checks without network access.

## Manual QA checklist

MAN1 is required for all linked generated teaching visuals.
Manual review is justified because binary teaching visuals can be misleading even when prompt records pass text checks.

## What not to test and why

- Do not test Control Chart behavior because it is out of scope.
- Do not test SPC calculations, control limits, process capability, subgrouping, or run rules because they are out of scope.
- Do not test Histogram or Scatter Diagram rendering automation because chart automation is out of scope.
- Do not test named spreadsheet, statistics, diagramming, presentation, or programming-tool tutorials because named-tool tutorials are out of scope.
- Do not test generated images as quantitative evidence because generated visuals are conceptual teaching aids only.

## Uncovered gaps

None.

## Next artifacts

| Artifact | Purpose |
|---|---|
| Test-spec review | Confirm proof-map adequacy before implementation. |
| Implementation M1 | Add the three method kits after test-spec-review approval. |

## Follow-on artifacts

None yet

## Readiness

Ready for test-spec-review.
Implementation remains blocked until test-spec-review is approved.
