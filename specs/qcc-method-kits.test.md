# QCC Method Kits Test Spec

## Status

active

## Related spec and plan

- Spec: [qcc-method-kits.md](qcc-method-kits.md)
- Plan: [docs/plans/2026-07-08-improve-qcc-method-templates.md](../docs/plans/2026-07-08-improve-qcc-method-templates.md)
- Architecture: [docs/architecture/method-kits/architecture.md](../docs/architecture/method-kits/architecture.md)

## Input artifact identities

| Input | Path | Status / Review state | Identity |
|---|---|---|---|
| Feature spec | `specs/qcc-method-kits.md` | approved | Status says `approved`; review record `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md`. |
| Spec review | `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md` | approved, no material findings | Review ID `spec-review-r1`; eventual test-spec readiness condition was architecture and plan. |
| Architecture | `docs/architecture/method-kits/architecture.md` | approved | Status says `approved`; review record `architecture-review-r1`. |
| Architecture review | `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/architecture-review-r1.md` | approved, no material findings | Review ID `architecture-review-r1`; next stage was plan. |
| Plan | `docs/plans/2026-07-08-improve-qcc-method-templates.md` | active | Plan lifecycle state is `active`; review record `plan-review-r1`. |
| Plan review | `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/plan-review-r1.md` | approved, no material findings | Review ID `plan-review-r1`; immediate next stage was test-spec. |

## Testing strategy

Unit and contract tests verify catalog schema, implementation modes, Python assist status, method-guide sections, source-note content, and official/incoming classification.
Integration tests verify catalog validation failure modes, generated PPTX/template metadata where practical, and cross-artifact consistency between catalog, guides, source notes, templates, and optional assist paths.
Smoke tests run the existing template catalog validator, template builder, and targeted test files.
Manual QA is required for PPTX readability, copyability, demo labeling, editable chart/table usability, and non-overlap of slide text because those qualities cannot be fully proven by metadata or source-text tests.
Migration checks verify that existing first-slice assets remain registered and that Pareto evidence behavior is not changed by method-kit work.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1 | T3, T12 | contract | Markdown guide exists and is linked for every official kit. |
| R2 | T5, T11, T12 | integration/manual | PowerPoint template exists and is visually checked. |
| R3 | T4, T5, T11 | integration/manual | Demo example exists and is labeled as not project evidence. |
| R4 | T4, T5, T6, T11 | integration/manual | Blank copyable slide or worksheet exists. |
| R5 | T3, T4, T6 | contract | Interpretation patterns are present. |
| R6 | T3, T4, T6 | contract | Common mistakes are present. |
| R7 | T3, T4, T6 | contract | Facilitator checklist exists. |
| R8 | T3, T4, T6, T10 | contract | Python assist decision guidance exists. |
| R9 | T3, T4, T6, T8 | contract | Evidence/source note guidance exists. |
| R10 | T1, T12 | contract | Catalog entry exists for each official kit. |
| R11 | T4, T5, T11 | integration/manual | Chart kit has editable chart or documented reason. |
| R12 | T4, T5 | integration | Chart kit has sample data table. |
| R13 | T4, T5 | integration | Chart-editing instructions exist. |
| R14 | T10 | integration | Python-assisted kit metadata requires sample input when applicable. |
| R15 | T10 | integration | Python-assisted kit metadata requires runnable assist path when applicable. |
| R16 | T10 | integration | Python-assisted kit metadata requires generated output example when applicable. |
| R17 | T10 | integration | Python-assisted kit metadata requires reproducibility note when applicable. |
| R18 | T1 | contract | Catalog required fields are validated. |
| R19 | T2 | integration | Missing paths fail catalog validation. |
| R20 | T2 | integration | Duplicate official ownership fails unless alternate is explicit. |
| R21 | T1, T9 | contract | Official and incoming/source states are distinguished. |
| R22 | T1, T12 | contract | First method-kit set is registered. |
| R23 | T1, T4, T10 | contract | Pareto mode and optional assist status are declared. |
| R24 | T1, T6 | contract | Worksheet method modes are declared. |
| R25 | T1, T6 | contract | Fishbone diagram mode is declared. |
| R26 | T4, T5, T11 | integration/manual | Pareto required content exists and is visually checked. |
| R27 | T3, T4 | contract | Pareto category and period cautions exist. |
| R28 | T4, T5, T11 | integration/manual | Embedded formula guidance is visible or documented when formulas are used. |
| R29 | T4, T8, T10 | contract | Python assist triggers for complexity and rigor exist. |
| R30 | T8 | contract | Evidence levels are defined. |
| R31 | T8 | contract | Level 1 draft guidance permits PowerPoint edits. |
| R32 | T8 | contract | Level 2 normal project guidance preserves source/date/checklist expectations. |
| R33 | T8, T10 | contract | Level 3 formal-review guidance recommends assist for raw/repeated chart methods. |
| R34 | T8, T10 | contract | Level 4 high-risk guidance requires reproducible evidence or validated path. |
| R35 | T9 | integration | Incoming templates are collected or documented separately. |
| R36 | T9 | integration | Incoming templates are not official before review. |
| R37 | T1, T3, T6, T9 | contract | Official kits preserve QCC stage fit and method logic. |
| R38 | T12 | integration | Markdown and PowerPoint source guidance are consistency-checked. |
| R39 | T7, T8, T10 | contract | Kits do not claim manual charts are authoritative for high-rigor data conclusions. |
| R40 | T7, T12 | contract | Scope guard confirms no full PPTX automation is required. |
| R41 | T13 | contract | Chart decision guide exists for Pareto. |
| R42 | T13 | integration | Pareto includes a chart variant library. |
| R43 | T13 | contract | Pareto includes chart quality checklist fields and formula checks. |
| R44 | T13 | integration | Pareto includes cumulative, before/after, and focus annotation guidance. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 | T1, T3, T4, T5, T11, T12 | Complete Pareto kit content and visual usability. |
| E2 | T4, T5, T11 | PowerPoint-native Pareto chart editing guidance and manual visual check. |
| E3 | T3, T4, T6, T11 | Facilitator checklist coverage. |
| E4 | T8, T10 | Python assist recommendation for high-rigor evidence. |
| E5 | T9 | Incoming template remains unofficial until reviewed. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1 no-chart method | T6 | contract | Worksheet/diagram kits still need required method-kit content. |
| EC2 overwritten formula cells | T4, T11 | manual/contract | Pareto checklist flags formula overwrite risk when formulas exist. |
| EC3 useful layout but weak method guidance | T9 | integration | Incoming templates remain unofficial until standard is met. |
| EC4 mixed PowerPoint-native and Python-assisted paths | T10 | contract | Assist status and reasons explain both paths. |
| EC5 polished slide without source/date notes | T4, T8, T11 | manual/contract | Checklist and visual QA flag missing source/date notes. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
|---|---|---|---|---|---|---|---|---|---|
| CMD1 | `python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` | existing/configured | M1 implementer | M1 | M1 | Blocks M1 closeout when catalog tests fail. | Zero collected tests fail. | M1 validation notes | Local tests only. |
| CMD2 | `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | existing/configured | M1 implementer | M1 | M1 | Blocks milestone closeout when catalog validation fails. | not applicable | catalog validation output | Reads local catalog and paths only. |
| CMD3 | `python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` | existing/configured | M2/M3 implementer | M2 | M2 | Blocks milestone closeout when guide/template/catalog tests fail. | Zero collected tests fail. | milestone validation notes | Local tests only. |
| CMD4 | `python tools/build_ppt_templates.py` | existing/configured | M2/M3 implementer | M2 | M2 | Blocks template milestone closeout when template build fails. | not applicable | builder output and generated PPTX files | Writes repository PPTX assets only. |
| CMD5 | `python -m pytest` | existing/configured | M4 implementer | M4 | M4 | Blocks M4 and final closeout when full tests fail. | Zero collected tests fail. | full pytest output | Local tests only. |
| CMD6 | `python -m ruff check .` | existing/configured | milestone implementer | M1 | M1 | Blocks milestone closeout when lint fails. | not applicable | Ruff output | Local static analysis only. |
| CMD7 | `python -m mypy qcc_toolkit` | existing/configured | milestone implementer | M1 | M1 | Blocks milestone closeout when type checks fail unless plan records a scoped exception. | not applicable | mypy output | Local static analysis only. |
| CMD8 | `git diff --check` | existing/configured | M4 implementer | M4 | M4 | Blocks handoff when whitespace errors exist. | not applicable | git diff output | Read-only diff check. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
|---|---|---|---|---|---|---|
| M1 | T1, T2, T10 | none | CMD1, CMD2, CMD6, CMD7 | catalog tests and validation output | M1 code-review | Establishes metadata and validation before content expansion. |
| M2 | T3, T4, T5, T8, T10, T11 | MP1 | CMD2, CMD3, CMD4, CMD6, CMD7 | Pareto guide/source/template evidence and manual visual checklist | M2 code-review | Manual proof is required for Pareto template readability and copyability. |
| M3 | T3, T5, T6, T7, T8, T11 | MP2 | CMD2, CMD3, CMD4, CMD6, CMD7 | worksheet/diagram guide/source/template evidence and manual visual checklist | M3 code-review | Manual proof is required for non-chart template usability. |
| M4 | T1, T2, T7, T8, T9, T10, T12 | MP3 | CMD1, CMD2, CMD5, CMD6, CMD7, CMD8 | full test output, catalog validation, final consistency notes | M4 code-review | Full consistency and privacy/source-template proof happen here. |

## Test cases

### T1. Catalog accepts complete official method-kit metadata

- Covers: R10, R18, R21, R22, R23, R24, R25, R37
- Level: contract
- Command IDs: CMD1, CMD2
- Fixture/setup: Updated `templates/ppt/catalog.yml`.
- Steps: Validate official entries include required fields, implementation mode, Python assist status, and official/incoming classification.
- Expected result: All first method-kit entries pass validation with the expected modes and assist statuses.
- Failure proves: Official kits cannot be reliably discovered or reviewed.
- Evidence artifact: catalog test and validator output.
- Automation location: `tests/test_template_catalog.py`.
- Required by milestone: M1.

### T2. Catalog rejects invalid official kit metadata

- Covers: R19, R20, EB1, EB2, EB3, EB4
- Level: integration
- Command IDs: CMD1
- Fixture/setup: Invalid catalog fixtures with missing paths, duplicate ownership, missing minimum content metadata, missing chart editability metadata, and incomplete Python assist metadata.
- Steps: Run catalog failure tests.
- Expected result: Invalid fixtures fail with entry and field context.
- Failure proves: Catalog drift or incomplete official kits can pass unnoticed.
- Evidence artifact: catalog failure test output.
- Automation location: `tests/test_template_catalog_failures.py`.
- Required by milestone: M1.

### T3. Method guides contain required method-kit guidance

- Covers: R1, R5, R6, R7, R8, R9, R27, R37
- Level: contract
- Command IDs: CMD3
- Fixture/setup: Method guides for Pareto, 5W2H, 5 Whys, Check Sheet, and Fishbone.
- Steps: Parse or scan guides for method-kit sections, cautions, interpretation, mistakes, checklist, assist decision, and evidence/source guidance.
- Expected result: Each official guide contains required sections; Pareto contains category/period cautions.
- Failure proves: Markdown no longer governs enough method knowledge for official kits.
- Evidence artifact: method-guide test output.
- Automation location: `tests/test_method_guides.py`.
- Required by milestone: M2 and M3.

### T4. Pareto kit content satisfies chart-specific contract

- Covers: R3, R4, R11, R12, R13, R23, R26, R28, R29, EC2, EC5
- Level: integration
- Command IDs: CMD2, CMD3, CMD4
- Fixture/setup: Pareto guide, source note, catalog entry, and PPTX template.
- Steps: Check source/catalog/template metadata for editable chart or documented reason, sample table, edit instructions, blank slide, demo label, interpretation patterns, mistakes, checklist, evidence notes, and assist rule.
- Expected result: Pareto kit satisfies all chart-specific requirements.
- Failure proves: The first chart kit remains a shallow placeholder.
- Evidence artifact: template asset and catalog test output.
- Automation location: `tests/test_template_assets.py`, `tests/test_template_catalog.py`.
- Required by milestone: M2.

### T5. PowerPoint template assets expose required user-facing surfaces

- Covers: R2, R3, R4, R11, R12, R13, R26, R28
- Level: integration
- Command IDs: CMD3, CMD4
- Fixture/setup: Generated or checked-in PPTX files and source notes.
- Steps: Inspect PPTX package metadata, expected placeholders, demo labels, blank slide markers, and source-note declarations.
- Expected result: Required user-facing surfaces exist in official templates.
- Failure proves: Official templates do not expose required working assets.
- Evidence artifact: template asset test output.
- Automation location: `tests/test_template_assets.py`.
- Required by milestone: M2 and M3.

### T6. Worksheet and diagram kits satisfy template-native contract

- Covers: R1-R10, R22, R24, R25, R30-R32, R35-R39, EC1
- Level: integration
- Command IDs: CMD2, CMD3, CMD4
- Fixture/setup: 5W2H, 5 Whys, Check Sheet, and Fishbone guides/source notes/templates.
- Steps: Check each kit for demo, blank working surface, interpretation, mistakes, checklist, evidence/source guidance, and correct implementation mode.
- Expected result: Template-native kits meet required content without claiming unsupported calculations.
- Failure proves: Non-chart methods are over-automated or under-specified.
- Evidence artifact: guide/template/catalog test output.
- Automation location: `tests/test_method_guides.py`, `tests/test_template_assets.py`.
- Required by milestone: M3.

### T7. Scope guard rejects unsupported automation and advanced-method claims

- Covers: R39, R40, NG1-NG6
- Level: contract
- Command IDs: CMD5
- Fixture/setup: Repository file inventory and public method/template metadata.
- Steps: Check that this slice does not require full PPTX automation, web UI, dashboard, EQMS workflow, Control Chart, Process Capability, DOE, regression, or authoritative manual-chart claims.
- Expected result: Out-of-scope surfaces remain absent or explicitly deferred.
- Failure proves: Implementation expanded beyond approved scope.
- Evidence artifact: scope guard test output.
- Automation location: `tests/test_scope_guards.py`.
- Required by milestone: M3 and M4.

### T8. Evidence-level guidance is present and consistent

- Covers: R30, R31, R32, R33, R34, R39, EC4, EC5
- Level: contract
- Command IDs: CMD3, CMD5
- Fixture/setup: Template standards, guides, source notes, and/or catalog evidence-level fields.
- Steps: Verify draft, normal project, formal review, and high-risk evidence expectations are documented and referenced from kits.
- Expected result: Guidance permits PowerPoint for draft/simple work and requires reproducible evidence for high-risk data-dependent conclusions.
- Failure proves: Users receive unclear or unsafe evidence guidance.
- Evidence artifact: documentation/source consistency test output.
- Automation location: `tests/test_method_guides.py` or `tests/test_artifact_consistency.py`.
- Required by milestone: M2, M3, and M4.

### T9. Incoming templates remain non-official until reviewed

- Covers: R21, R35, R36, R37, EB7, S2, EC3
- Level: integration
- Command IDs: CMD1, CMD2, CMD5
- Fixture/setup: Incoming-template documentation or fixture entries.
- Steps: Verify incoming/source entries are separate from official kits and cannot satisfy official catalog requirements without review metadata.
- Expected result: Incoming templates are source assets only and include privacy/formula review guidance.
- Failure proves: Unreviewed templates can become official or leak unsafe content.
- Evidence artifact: catalog/source-template test output.
- Automation location: `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py`.
- Required by milestone: M4.

### T10. Python assist status and reasons are explicit

- Covers: R8, R14, R15, R16, R17, R23, R29, R33, R34, EC4
- Level: contract
- Command IDs: CMD1, CMD2, CMD3
- Fixture/setup: Catalog entries and method-kit source notes.
- Steps: Validate assist status values and required assist metadata for optional or Python-assisted methods.
- Expected result: Pareto is optional assist; methods without assist do not imply unavailable evidence rigor; Python-assisted entries require sample input, runnable path, output example, and reproducibility note.
- Failure proves: Users cannot tell when Python is enough, optional, recommended, or required.
- Evidence artifact: catalog and source-note test output.
- Automation location: `tests/test_template_catalog.py`, `tests/test_method_guides.py`.
- Required by milestone: M1 and M2.

### T11. Manual visual QA confirms template usability

- Covers: R2, R3, R4, R11, R26, R28, UX1-UX5, EC2, EC5
- Level: manual
- Command IDs: none
- Fixture/setup: Built or checked-in official PPTX files for the first method-kit set.
- Steps: Open each template and inspect slide readability, demo labeling, blank slide copyability, chart/table editability, source/date note placement, and absence of incoherent overlap.
- Expected result: Reviewer records pass/fail checklist for each official kit.
- Failure proves: Automated checks passed but the template is not practically usable.
- Evidence artifact: `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md` or equivalent milestone handoff notes.
- Automation location: manual QA checklist.
- Required by milestone: M2, M3, and M4.

### T12. Cross-artifact consistency check covers final kit set

- Covers: R1-R40, AC1-AC8
- Level: integration
- Command IDs: CMD2, CMD5, CMD8
- Fixture/setup: Final guides, templates, source notes, catalog, tests, and method-kit standards.
- Steps: Run full tests, catalog validation, and consistency checks mapping official kits to required artifacts.
- Expected result: All official kits have matching guide, template, source note, catalog entry, implementation mode, assist status, and required proof evidence.
- Failure proves: Final method-kit set is incomplete or internally inconsistent.
- Evidence artifact: full validation output and consistency test output.
- Automation location: `tests/test_artifact_consistency.py`, `tests/test_acceptance.py`.
- Required by milestone: M4.

### T13. Pareto chart-quality surfaces are present

- Covers: R41, R42, R43, R44, AC9
- Level: integration
- Command IDs: CMD3, CMD4, CMD5
- Fixture/setup: Pareto guide, source note, and generated PPTX template.
- Steps: Check for Chart decision guide, Chart variant library, Chart quality checklist, safe conclusion, overclaim warning, Cumulative Pareto, Before/after Pareto comparison, Focus annotation, Percent, Cumulative percent, and Formula check.
- Expected result: The Pareto kit gives chart-specific decision, variant, and quality-review support beyond generic method guidance.
- Failure proves: The chart template remains too weak for practical QCC chart use.
- Evidence artifact: guide/source/PPTX package test output.
- Automation location: `tests/test_template_assets.py` and `tests/test_method_kit_closeout.py`.
- Required by milestone: M5.

## Fixtures and data

- Existing synthetic Pareto example data remains the only data source for Python assist proof unless a later accepted spec adds more.
- Catalog fixtures should include valid official kit entries, missing path entries, duplicate ownership entries, incoming/source entries, and incomplete Python assist entries.
- Template fixtures use the checked-in PPTX files and reviewable source notes.
- Manual QA uses the generated or checked-in official PPTX method templates.

## Mocking/stubbing policy

Tests may use temporary catalog files and temporary directories for validation failure cases.
Tests must not mock the catalog validator when the requirement is catalog validation behavior.
Tests may avoid opening PowerPoint itself; PPTX package inspection and source-note checks are acceptable for automation.
Manual QA covers the visual behavior that package inspection cannot prove.

## Migration or compatibility tests

Compatibility checks cover method IDs, template IDs, implementation modes, catalog fields, guide paths, template paths, source-note paths, and existing Pareto evidence behavior.
Existing first-slice catalog entries should migrate intentionally and remain valid under the updated catalog contract.

## Observability verification

Observability is reviewer-facing rather than runtime telemetry.
Tests verify that reviewers can identify official kits, implementation modes, Python assist status, required content, and incoming/source distinctions from catalog and source artifacts.

## Security/privacy verification

Tests and manual review verify incoming-template guidance treats source templates as untrusted until reviewed.
Checks should look for privacy-review wording covering real customer names, employee names, supplier names, patient data, credentials, hidden notes, and unsupported formulas.
No test should require real private data.

## Performance checks

Catalog validation and targeted template/guide tests should complete as part of the normal local validation suite.
No separate benchmark is required for this documentation/template-heavy slice.

## Manual QA checklist

| Manual proof ID | Check | Evidence |
|---|---|---|
| MP1 | Pareto template is readable, demo-labeled, copyable, and chart/table editing guidance is usable. | Manual template review notes before M2 code-review. |
| MP2 | 5W2H, 5 Whys, Check Sheet, and Fishbone templates are readable, demo-labeled, copyable, and not overcrowded. | Manual template review notes before M3 code-review. |
| MP3 | Final method-kit set has no incoherent text overlap and source/evidence notes are visible enough for review. | Manual template review notes before M4 code-review. |

## What not to test and why

- Do not test full automated PPTX generation; it is out of scope.
- Do not test web UI, dashboard, EQMS, CAPA, or desktop-app behavior; those are out of scope.
- Do not test Control Chart, Process Capability, DOE, regression, or advanced statistical methods; those are deferred.
- Do not test real private incoming templates; use synthetic fixtures and manual privacy review guidance.
- Do not treat screenshots alone as proof of method correctness; method guidance and catalog/source checks carry the contract.

## Uncovered gaps

None.

## Next artifacts

- Implementation M1 after approved test-spec-review.

## Follow-on artifacts

- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/test-spec-review-r1.md` - approved test-spec review with no material findings.

## Readiness

Approved and ready for implementation M1.

This test spec is not implementation, not code-review evidence, and not verification evidence.
