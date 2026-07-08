# QCC Toolkit First Slice Test Spec

## Status

active

## Related spec and plan

- Spec: [qcc-toolkit-first-slice.md](qcc-toolkit-first-slice.md)
- Plan: [docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md](../docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md)
- Architecture: [docs/architecture/system/architecture.md](../docs/architecture/system/architecture.md)
- ADRs:
  - [ADR-20260708-python-local-first-stack.md](../docs/adr/ADR-20260708-python-local-first-stack.md)
  - [ADR-20260708-evidence-package-boundary.md](../docs/adr/ADR-20260708-evidence-package-boundary.md)

## Input artifact identities

| Input | Path | Status / Review state | Identity |
| --- | --- | --- | --- |
| Feature spec | `specs/qcc-toolkit-first-slice.md` | approved | Status line says `approved`; spec-review record `docs/changes/2026-07-07-create-qcc-toolkit/reviews/spec-review-r1.md`. |
| Spec review | `docs/changes/2026-07-07-create-qcc-toolkit/reviews/spec-review-r1.md` | approved, no material findings | Review ID `spec-review-r1`; eventual test-spec readiness was conditionally-ready after architecture. |
| Architecture | `docs/architecture/system/architecture.md` | approved | Status line says `approved`; architecture-review record `architecture-review-r1`. |
| Architecture review | `docs/changes/2026-07-07-create-qcc-toolkit/reviews/architecture-review-r1.md` | approved, no material findings | Review ID `architecture-review-r1`; next stage was plan. |
| Plan | `docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md` | active | Plan lifecycle state is `active`; plan-review record `plan-review-r1`. |
| Plan review | `docs/changes/2026-07-07-create-qcc-toolkit/reviews/plan-review-r1.md` | approved, no material findings | Review ID `plan-review-r1`; immediate next stage was test-spec. |
| ADR | `docs/adr/ADR-20260708-python-local-first-stack.md` | accepted | Establishes local-first Python stack and optional PNG export boundary. |
| ADR | `docs/adr/ADR-20260708-evidence-package-boundary.md` | accepted | Establishes evidence package as the authoritative data-dependent record. |

## Testing strategy

Unit tests prove deterministic method IDs, stage IDs, Pareto validation, calculation, warnings, captions, and report metadata.
Integration tests prove public API boundaries, evidence package writing, renderer fallback behavior, template catalog validation, and report output wiring.
End-to-end tests prove the synthetic `reduce-packing-label-errors` project regenerates Pareto evidence from local data through the starter script.
Smoke tests prove package import, editable install, command entry points, and script execution.
No manual proof is required by this test spec.
Human review of static PPT template visual quality remains part of downstream code review and PR review, but it is not a substitute for automated catalog, path, placeholder, demo-label, and evidence-package checks.
Contract tests prove public APIs, template catalog fields, method-guide front matter, evidence metadata fields, and chart specification fields.
Migration tests are minimal because no old implementation data exists; compatibility tests focus on stable IDs, metadata version fields, and reproducibility across repeated runs under the same package version.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T16, T17 | e2e | Synthetic project ID and project folder are verified through example project tests. |
| R2 | T18 | integration | Fixtures and generated examples are scanned for synthetic-only data markers and absence of known private data files. |
| R3 | T3, T5, T15 | unit | Pareto is registered and implemented as the first complete data-chart method. |
| R4 | T11, T12 | contract | Template-guided methods are present in guides, catalog, and template assets. |
| R5 | T2, T11 | contract | Method IDs are stable and referenced consistently. |
| R6 | T12 | contract | Template IDs are unique and stable in catalog entries. |
| R7 | T11 | contract | Method guide front matter is validated. |
| R8 | T11 | contract | Required guide sections are validated. |
| R9 | T11, T4 | contract | Pareto guide input-shape claims are checked against validation behavior. |
| R10 | T11, T5 | unit | Pareto calculation convention is checked against guide formula notes. |
| R11 | T12, T14 | contract | Template files or accepted placeholder assets exist for all first-slice methods. |
| R12 | T12, T14 | contract | Demo-label declarations are checked through reviewable template catalog or template-source metadata. |
| R13 | T12, T14 | contract | Placeholder contracts are checked through catalog and template-source metadata. |
| R14 | T12 | contract | `templates/ppt/catalog.yml` existence is checked. |
| R15 | T12 | contract | One catalog entry per first-slice template is checked. |
| R16 | T12 | contract | Required catalog fields are checked. |
| R17 | T12 | contract | Pareto catalog entry includes script and example project. |
| R18 | T13 | integration | Missing referenced paths fail catalog validation. |
| R19 | T13 | integration | Duplicate template IDs fail catalog validation. |
| R20 | T13 | integration | Ambiguous method-template ownership fails unless alternate template is explicit. |
| R21 | T15, T16 | smoke | Starter script accepts required CLI inputs. |
| R22 | T1, T16, T21 | smoke | Local install/import and local script execution require no server or network call. |
| R23 | T15 | integration | Starter script delegates to public API seams. |
| R24 | T15 | integration | Starter script does not implement formula logic directly. |
| R25 | T4, T16 | integration | Missing required columns fail before final artifacts. |
| R26 | T4 | unit | Empty input validation fails. |
| R27 | T4 | unit | Negative count validation fails. |
| R28 | T4 | unit | Null or blank category handling follows the documented rule. |
| R29 | T5 | unit | Calculation result fields are checked. |
| R30 | T7 | contract | Chart spec contains bars and cumulative line when supported. |
| R31 | T7, T9 | contract | Chart spec and metadata preserve method and input context. |
| R32 | T9 | integration | Evidence package required files are checked. |
| R33 | T8, T9 | integration | HTML chart artifact is required. |
| R34 | T8 | integration | PNG chart is produced when static export is available. |
| R35 | T8 | integration | PNG skip warning is produced when export is unavailable. |
| R36 | T6 | unit | Captions are deterministic. |
| R37 | T6 | unit | Interpretation is deterministic and transparent. |
| R38 | T4, T8, T10 | unit | Warning categories are structured and distinguishable. |
| R39 | T20 | integration | Markdown report references Pareto evidence. |
| R40 | T20 | integration | HTML report is checked when renderer support is available. |
| R41 | T20 | integration | Reports preserve links to artifacts, tables, captions, warnings, and metadata. |
| R42 | T19 | e2e | Repeated generation produces equivalent table and chart spec. |
| R43 | T9, T20 | integration | Manifest/report identifies slide-ready generated assets. |
| R44 | T9, T20, T21 | integration | Evidence package and report checks keep generated evidence authoritative; slide edits are outside the calculation record. |
| R45 | T21 | contract | Package and examples do not add web UI, dashboard, CAPA/EQMS, workflow, or document editor surfaces. |
| R46 | T21 | contract | No automated PPTX generation is required or invoked. |
| R47 | T21 | contract | Control Chart implementation is absent from first-slice public support. |
| R48 | T12, T13, T22 | integration | Automated checks validate IDs, paths, catalog entries, and guide links. |
| R49 | T16, T17 | e2e | Synthetic project regeneration command produces expected evidence. |
| R50 | T19 | e2e | Reproducibility check compares repeated result and chart spec. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T16, T17 | Valid synthetic project generation through starter script. |
| E2 | T4, T16 | Invalid input rejection and no success metadata. |
| E3 | T12, T13 | Template catalog traceability and failure modes. |
| E4 | T11, T12, T14, T21 | Template-guided methods do not claim data-dependent calculation support. |
| E5 | T19 | Repeated Pareto generation compares calculated table and chart spec. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 | T5 | unit | Ties use documented deterministic order. |
| EC2 | T6, T7 | unit | One-category result avoids vital-few implication in caption and chart spec. |
| EC3 | T6, T11 | unit | Many-category behavior is documented or warning-producing. |
| EC4 | T4 | unit | Zero total count avoids divide-by-zero. |
| EC5 | T4 | unit | Extra columns do not alter calculation unexpectedly. |
| EC6 | T9 | integration | Existing output folder behavior is explicit. |
| EC7 | T8 | integration | Missing static image export produces warning and non-PNG artifacts. |
| EC8 | T13 | integration | Guide method-ID mismatch fails catalog validation. |
| EC9 | T13 | integration | Guide without matching template is classified as intentional or coverage gap. |
| EC10 | T9, T20, T21 | integration | Manual slide edits do not replace evidence package authority. |

## Validation commands

| Command ID | Command | Classification | Owner | Owning milestone | First required milestone | Failure behavior | Zero-test behavior | Evidence artifact | Safe mode / side-effect boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CMD1 | `python -m pip install -e .` | planned-for-implementation | M1 implementer | M1 | M1 | Blocks M1 closeout if install fails. | not applicable | M1 validation notes | Local environment only; no publish or network service. |
| CMD2 | `python -m pytest` | planned-for-implementation | M1 implementer | M1 | M1 | Blocks milestone closeout when tests fail. | Zero collected tests fail after M1. | pytest output in validation notes | Local test execution only. |
| CMD3 | `python -m pytest tests` | planned-for-implementation | M1 implementer | M1 | M1 | Blocks milestone closeout when tests fail. | Zero collected tests fail after M1. | pytest output in validation notes | Local test execution only. |
| CMD4 | `python -m ruff check .` | planned-for-implementation | M1 implementer | M1 | M1 | Blocks milestone closeout when lint fails. | not applicable | Ruff output in validation notes | Local static analysis only. |
| CMD5 | `python -m ruff check qcc_toolkit tests` | planned-for-implementation | M1 implementer | M1 | M2 | Blocks milestone closeout when lint fails. | not applicable | Ruff output in validation notes | Local static analysis only. |
| CMD6 | `python -m ruff check qcc_toolkit tests examples` | planned-for-implementation | M5 implementer | M5 | M5 | Blocks M5 closeout when package, tests, or examples lint fails. | not applicable | Ruff output in validation notes | Local static analysis only. |
| CMD7 | `python -m mypy qcc_toolkit` | planned-for-implementation | M1 implementer | M1 | M1 | Blocks milestone closeout when type checks fail unless plan records a scoped decision to relax. | not applicable | mypy output in validation notes | Local static analysis only. |
| CMD8 | `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | planned-for-implementation | M4 implementer | M4 | M4 | Blocks M4 closeout when catalog validation fails. | not applicable | catalog validation output | Reads local catalog and paths only. |
| CMD9 | `python examples/scripts/generate_pareto.py --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv --category-column defect_type --count-column count --project examples/projects/reduce-packing-label-errors --output examples/projects/reduce-packing-label-errors/evidence/pareto` | planned-for-implementation | M5 implementer | M5 | M5 | Blocks M5 and later closeout when evidence generation fails. | not applicable | generated evidence package and script output | Writes only under the selected example output path. |
| CMD10 | `git status --short` | existing/configured | milestone implementer | not applicable | M7 | Used to report worktree state; does not by itself block tests. | not applicable | final lifecycle validation notes | Read-only git status. |

## Milestone proof map

| Milestone | Required test IDs | Manual proof IDs | Command IDs | Evidence artifacts | Required before | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | T1, T22 | none | CMD1, CMD2, CMD3, CMD4, CMD7 | `tests/`, `pyproject.toml`, validation notes | M1 code-review | Planned commands become real in this milestone. |
| M2 | T2, T3, T4, T5, T6 | none | CMD3, CMD5, CMD7 | unit test outputs and fixture data | M2 code-review | Focus on contracts and calculation before rendering. |
| M3 | T7, T8, T9, T10, T19 | none | CMD3, CMD5, CMD7 | chart spec snapshots, evidence package fixtures | M3 code-review | PNG unavailable path must be covered without requiring PNG export dependency. |
| M4 | T11, T12, T13, T14, T22 | none | CMD3, CMD5, CMD7, CMD8 | docs/methods, template catalog, template placeholder evidence | M4 code-review | Template visual quality remains a reviewer concern, not a separate manual proof gate. |
| M5 | T15, T16, T17, T18, T19, T24 | none | CMD3, CMD6, CMD7, CMD9 | synthetic project, script output, evidence package | M5 code-review | Starter script must remain a public-API wrapper and reject unsafe paths. |
| M6 | T20, T21, T23 | none | CMD2, CMD4, CMD7, CMD9 | report outputs, README workflow, acceptance evidence | M6 code-review | End-to-end acceptance checks happen here. |
| M7 | T23 | none | CMD2, CMD4, CMD7, CMD10 | lifecycle records and final validation notes | final verify handoff | No new product behavior expected. |

## Test cases

### T1. Package scaffold imports and local tooling exists

- Covers: R22, R48, R49, R50
- Level: smoke
- Command IDs: CMD1, CMD2, CMD3, CMD4, CMD7
- Fixture/setup: Fresh checkout after M1.
- Steps: Install editable package, import `qcc_toolkit`, and run configured baseline commands.
- Expected result: Package imports and configured checks run with at least one collected smoke test.
- Failure proves: The repository is not ready for test-driven implementation milestones.
- Evidence artifact: M1 validation notes.
- Automation location: `tests/test_import.py` and configured tooling.
- Required by milestone: M1.

### T2. Stage and method IDs are stable

- Covers: R3, R5, R31, R42
- Level: unit
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: First-slice method and stage registry.
- Steps: Assert expected method IDs and QCC stage IDs are present and stable.
- Expected result: `pareto_chart` and template-guided method IDs are present, with no duplicate IDs.
- Failure proves: Public compatibility IDs are missing or unstable.
- Evidence artifact: unit test output.
- Automation location: `tests/test_registry.py`.
- Required by milestone: M2.

### T3. Pareto is the first complete data-chart method

- Covers: R3, R4, R5
- Level: contract
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Method registry after M2.
- Steps: Inspect registry metadata for method type and first-slice status.
- Expected result: Pareto is data-chart supported; Check Sheet, 5W2H, Fishbone, and 5 Whys are template-guided.
- Failure proves: First-slice method classification drifted.
- Evidence artifact: contract test output.
- Automation location: `tests/test_method_registry.py`.
- Required by milestone: M2.

### T4. Pareto input validation rejects invalid data

- Covers: R9, R21, R25, R26, R27, R28, R38, E2, EC4, EC5
- Level: unit
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Data fixtures for missing category, empty data, negative counts, nonnumeric counts, blank categories, zero-total counts, and extra columns.
- Steps: Run Pareto validation on each fixture.
- Expected result: Invalid fixtures fail with clear validation errors or documented warnings; extra columns do not change the calculation input.
- Failure proves: Invalid or misleading Pareto inputs can generate evidence.
- Evidence artifact: unit test output.
- Automation location: `tests/test_pareto_validation.py`.
- Required by milestone: M2.

### T5. Pareto calculation matches known fixture

- Covers: R10, R29, R30, R42, EC1
- Level: unit
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Known defect counts with expected percentages, cumulative values, ranks, and tie ordering.
- Steps: Run calculation and compare fields to explicit expected values.
- Expected result: Category, count, percentage, cumulative value, and rank match fixture expectations.
- Failure proves: Pareto formula or ordering is incorrect.
- Evidence artifact: unit test output.
- Automation location: `tests/test_pareto_calculation.py`.
- Required by milestone: M2.

### T6. Captions and interpretation are deterministic

- Covers: R36, R37, R38, EC2, EC3
- Level: unit
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Normal, one-category, and many-category Pareto results.
- Steps: Generate caption and interpretation twice for each fixture.
- Expected result: Output is identical across runs and avoids unsupported conclusions.
- Failure proves: Captions or interpretation are opaque, nondeterministic, or misleading.
- Evidence artifact: unit test output.
- Automation location: `tests/test_interpretation.py`.
- Required by milestone: M2.

### T7. Pareto chart specification is renderer-independent

- Covers: R30, R31
- Level: contract
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Pareto calculation fixture and method metadata.
- Steps: Build chart spec and assert bar, cumulative line, metadata, selected columns, parameters, and version fields.
- Expected result: Chart spec contains required semantic fields without requiring renderer output.
- Failure proves: Rendering and method logic are coupled or chart metadata is missing.
- Evidence artifact: chart-spec snapshot.
- Automation location: `tests/test_chart_spec.py`.
- Required by milestone: M3.

### T8. Chart rendering writes HTML and handles optional PNG

- Covers: R33, R34, R35, R38, EC7
- Level: integration
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Chart spec fixture with renderer available and static export disabled or unavailable.
- Steps: Render chart artifacts in both modes.
- Expected result: HTML is produced; PNG is produced when available; skipped PNG is recorded as warning when unavailable.
- Failure proves: Optional export behavior can fail the whole evidence run or hide missing PNG.
- Evidence artifact: renderer test output and warning fixture.
- Automation location: `tests/test_chart_rendering.py`.
- Required by milestone: M3.

### T9. Evidence package contains required files and metadata

- Covers: R31, R32, R35, R41, R43, R44, EC6
- Level: integration
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Temporary output directory and Pareto result fixture.
- Steps: Write evidence package twice under controlled output behavior.
- Expected result: Required files exist, metadata is structured, output-folder behavior is explicit, and no success metadata appears for failed writes.
- Failure proves: Evidence package is incomplete or ambiguous.
- Evidence artifact: temporary evidence package assertion output.
- Automation location: `tests/test_evidence_package.py`.
- Required by milestone: M3.

### T10. Warning artifacts distinguish warning categories

- Covers: R35, R38
- Level: unit
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Validation, data caution, export skip, and interpretation warning samples.
- Steps: Serialize warnings and inspect type/category fields.
- Expected result: Each warning category is distinguishable and machine-readable.
- Failure proves: Reports and future UI cannot safely interpret warning state.
- Evidence artifact: unit test output.
- Automation location: `tests/test_warnings.py`.
- Required by milestone: M3.

### T11. Method guides have required front matter and sections

- Covers: R4, R5, R7, R8, R9, R10, E4
- Level: contract
- Command IDs: CMD3, CMD5, CMD7
- Fixture/setup: Markdown guides under `docs/methods/`.
- Steps: Parse guide front matter and headings.
- Expected result: Every first-slice guide has required front matter, sections, and method ID alignment.
- Failure proves: Method knowledge surface is incomplete or drifted.
- Evidence artifact: docs check output.
- Automation location: `tests/test_method_guides.py`.
- Required by milestone: M4.

### T12. Template catalog covers first-slice templates

- Covers: R6, R11, R12, R13, R14, R15, R16, R17, E3, E4
- Level: contract
- Command IDs: CMD3, CMD5, CMD7, CMD8
- Fixture/setup: `templates/ppt/catalog.yml`, method guides, template assets, and script/example paths.
- Steps: Validate catalog schema, required fields, unique IDs, and referenced paths.
- Expected result: Every first-slice template is traceable to method ID, guide, expected placeholders, expected assets, and script/example where applicable.
- Failure proves: Template traceability is broken.
- Evidence artifact: catalog validation output.
- Automation location: `tests/test_template_catalog.py`.
- Required by milestone: M4.

### T13. Template catalog validation fails on bad entries

- Covers: R18, R19, R20, R48, EC8, EC9
- Level: integration
- Command IDs: CMD3, CMD5, CMD7, CMD8
- Fixture/setup: Mutated catalog fixtures with missing paths, duplicate template IDs, mismatched guide method IDs, and unclassified coverage gaps.
- Steps: Run catalog validator against invalid fixtures.
- Expected result: Validation fails with catalog entry and field details.
- Failure proves: Catalog drift can pass silently.
- Evidence artifact: catalog validation test output.
- Automation location: `tests/test_template_catalog_failures.py`.
- Required by milestone: M4.

### T14. PPT template catalog and source metadata declare required review facts

- Covers: R11, R12, R13, AC4, AC11, AC12
- Level: integration
- Command IDs: CMD3, CMD5, CMD7, CMD8
- Fixture/setup: Static PPT template assets, template catalog entries, and any reviewable template-source or sidecar metadata used for placeholder and demo-label declarations.
- Steps: Validate that each first-slice template has a catalog entry, file path, method ID, template ID, expected placeholders, expected assets, and demo-label declaration in a reviewable source.
- Expected result: Template metadata is sufficient for automated traceability checks and downstream code reviewers can inspect the same declared facts.
- Failure proves: Binary or static template assets are not traceable enough for review.
- Evidence artifact: template catalog and metadata validation output.
- Automation location: `tests/test_template_assets.py`.
- Required by milestone: M4.

### T15. Starter script delegates to public API

- Covers: R21, R22, R23, R24, AC5
- Level: integration
- Command IDs: CMD3, CMD6, CMD7
- Fixture/setup: Starter script and public API spy or monkeypatch seam.
- Steps: Run script in a controlled test and assert it calls public API operations rather than duplicating formula logic.
- Expected result: Script parses CLI inputs and delegates validation/calculation/evidence generation.
- Failure proves: Script became a second implementation path.
- Evidence artifact: script integration test output.
- Automation location: `tests/test_generate_pareto_script.py`.
- Required by milestone: M5.

### T16. Pareto starter script regenerates evidence from synthetic data

- Covers: R1, R21, R22, R25, R32, R49, E1, E2, AC1, AC2, AC7
- Level: e2e
- Command IDs: CMD3, CMD6, CMD7, CMD9
- Fixture/setup: `examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv`.
- Steps: Run the documented script command and inspect the output directory.
- Expected result: Evidence package exists with expected artifacts and successful exit code.
- Failure proves: User-facing first-slice workflow is broken.
- Evidence artifact: generated evidence package and command output.
- Automation location: `tests/test_example_project_e2e.py`.
- Required by milestone: M5.

### T17. Synthetic project has expected structure

- Covers: R1, R49, E1
- Level: smoke
- Command IDs: CMD3, CMD6, CMD7
- Fixture/setup: Example project directory.
- Steps: Assert project README, data path, expected script path, and evidence output convention.
- Expected result: Project has stable ID and expected local folder structure.
- Failure proves: Example project is not reproducible from documented paths.
- Evidence artifact: smoke test output.
- Automation location: `tests/test_example_project_structure.py`.
- Required by milestone: M5.

### T18. Examples contain no real customer data

- Covers: R2, AC9
- Level: integration
- Command IDs: CMD3, CMD6, CMD7
- Fixture/setup: Example data, generated evidence, template sample text, and reports.
- Steps: Run deterministic checks for synthetic markers and banned private-data fixtures; review generated data source descriptions.
- Expected result: Examples are synthetic and contain no known private/customer data files.
- Failure proves: Privacy boundary is violated.
- Evidence artifact: privacy fixture check output.
- Automation location: `tests/test_synthetic_data_only.py`.
- Required by milestone: M5.

### T19. Pareto regeneration is reproducible

- Covers: R42, R50, E5, AC6
- Level: e2e
- Command IDs: CMD3, CMD6, CMD7, CMD9
- Fixture/setup: Same synthetic input data, parameters, filters, output roots, and toolkit version.
- Steps: Generate evidence twice and compare calculated table plus chart spec.
- Expected result: Table and chart spec are equivalent under the same toolkit version.
- Failure proves: Evidence generation is not reproducible.
- Evidence artifact: reproducibility comparison report.
- Automation location: `tests/test_reproducibility.py`.
- Required by milestone: M5 and M6.

### T20. Report-ready outputs reference evidence artifacts

- Covers: R39, R40, R41, R43, AC2
- Level: integration
- Command IDs: CMD2, CMD4, CMD7, CMD9
- Fixture/setup: Generated Pareto evidence package.
- Steps: Build Markdown and optional HTML report outputs and inspect artifact links and warning visibility.
- Expected result: Reports reference chart, table, caption, warnings, metadata, and evidence README or manifest.
- Failure proves: Reports require manual reconstruction or hide warnings.
- Evidence artifact: report artifact test output.
- Automation location: `tests/test_reports.py`.
- Required by milestone: M6.

### T21. First-slice scope exclusions are enforced

- Covers: R37, R45, R46, R47, AC10
- Level: contract
- Command IDs: CMD2, CMD4, CMD7
- Fixture/setup: Package public API, examples, scripts, and docs inventory.
- Steps: Assert no web UI, dashboard, CAPA/EQMS, automated PPTX generation requirement, Control Chart public support, or AI conclusion path is present.
- Expected result: Excluded surfaces are absent or explicitly marked deferred.
- Failure proves: First-slice scope expanded without accepted spec change.
- Evidence artifact: scope guard test output.
- Automation location: `tests/test_scope_guards.py`.
- Required by milestone: M6.

### T22. Lifecycle and path consistency checks pass

- Covers: R48
- Level: smoke
- Command IDs: CMD2, CMD4
- Fixture/setup: Proposal, spec, architecture, plan, review log, catalog, guides, scripts, and example paths.
- Steps: Run project artifact consistency checks.
- Expected result: Lifecycle statuses and artifact paths do not contradict each other.
- Failure proves: Downstream agents cannot trust lifecycle state or path references.
- Evidence artifact: lifecycle consistency output.
- Automation location: `tests/test_artifact_consistency.py`.
- Required by milestone: M1, M4, M6, and M7.

### T23. First-slice acceptance criteria are satisfied

- Covers: AC1, AC2, AC3, AC4, AC5, AC6, AC7, AC8, AC9, AC10, AC11, AC12
- Level: e2e
- Command IDs: CMD2, CMD4, CMD7, CMD9, CMD10
- Fixture/setup: Completed M1-M6 implementation.
- Steps: Run full test suite, regenerate example evidence, verify catalog/docs paths, confirm scope guard tests, and record worktree status.
- Expected result: All acceptance criteria pass and lifecycle evidence is ready for code-review and verify stages.
- Failure proves: First-slice implementation is incomplete.
- Evidence artifact: M7 validation notes and test output.
- Automation location: `tests/test_acceptance.py` plus lifecycle checks.
- Required by milestone: M7.

### T24. Missing input files and unsafe output paths fail safely

- Covers: EB1, S6, R22, R25
- Level: integration
- Command IDs: CMD3, CMD6, CMD7, CMD9
- Fixture/setup: Pareto starter script, a missing input path, a temporary project root, and output path traversal attempts such as `../outside-project`.
- Steps: Run the script or public IO layer with a missing input file and with an output path that would escape the selected project or output root.
- Expected result: Missing input files fail with a clear error and no success metadata; path traversal attempts fail without writing outside the selected project or output path.
- Failure proves: Local-first script execution can create ambiguous success states or unsafe filesystem writes.
- Evidence artifact: script boundary test output.
- Automation location: `tests/test_script_io_safety.py`.
- Required by milestone: M5.

## Fixtures and data

| Fixture | Purpose | Owner milestone |
|---|---|---|
| `tests/fixtures/pareto/category_counts.csv` | Known category-count Pareto calculation fixture. | M2 |
| `tests/fixtures/pareto/event_records.csv` | Event-record input fixture if event-record support is implemented in first slice. | M2 |
| `tests/fixtures/pareto/invalid_*.csv` | Missing column, empty, negative count, nonnumeric count, blank category, and zero-total validation fixtures. | M2 |
| `tests/fixtures/catalog/*.yml` | Valid and invalid catalog fixtures. | M4 |
| `examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv` | Synthetic user-facing example data. | M5 |
| `tests/fixtures/rendering/png_unavailable` | Fixture or monkeypatch for static export unavailable behavior. | M3 |
| `tests/fixtures/io/unsafe_paths.yml` | Missing input and path traversal cases for script and IO boundary checks. | M5 |

All committed example data must be synthetic.
Fixtures must not include real customer, production, employee, supplier, patient, or private operational data.

## Mocking/stubbing policy

Mocking is allowed for optional PNG export unavailability so CI does not depend on local Kaleido behavior.
Mocking is allowed to prove starter scripts call public APIs rather than internal calculation functions.
Mocking is not allowed for Pareto formula tests, catalog path validation, evidence package file presence, warning serialization, or reproducibility checks.
Filesystem tests should use temporary directories except the documented example project regeneration test.
Network calls are not expected; any attempted network call in first-slice execution should fail a test or require upstream approval.

## Migration or compatibility tests

No migration from existing implementation data is required because no prior package exists.
Compatibility tests still cover stable method IDs, template IDs, catalog field names, evidence metadata fields, chart spec fields, and version metadata.
T2, T7, T9, T12, T19, and T22 provide first-slice compatibility coverage.

## Observability verification

Observability proof is file and command based.
T16 checks starter script success output and generated evidence path.
T4 and T16 check user-visible validation errors.
T9 and T10 check metadata and structured warning artifacts.
T20 checks report-visible warning state.
No metrics, traces, or remote audit events are required in the first slice.

## Security/privacy verification

T18 verifies synthetic-only examples.
T21 verifies no web UI, network service, telemetry, secrets, or automated PPTX scope is introduced.
T9 verifies ordinary output path behavior through temporary output directories.
T24 verifies missing input files and path traversal attempts fail safely.
CSV or Excel-like formula execution prevention must be covered in IO parsing tests when Excel-like input support is implemented; until then, CSV-only parsing must document that formulas are treated as inert text.

## Performance checks

Performance is checked in T16 or a focused performance variant after M5.
The synthetic Pareto evidence generation command should complete within 10 seconds on a typical developer laptop, excluding dependency installation and unusually slow static image export.
Pareto calculation should support at least 10,000 input rows without manual pre-aggregation; this can be covered by a generated in-memory fixture in M2 or M3.
Performance tests should avoid strict timing in CI unless the environment is stable; use local timing evidence or a generous CI threshold when necessary.

## Manual QA checklist

No separate manual proof is required by this test spec.
Downstream code review and PR review may inspect static PPT assets for visual quality, but merge approval is not counted as a substitute for automated formula, validation, catalog, evidence package, reproducibility, or script tests.

Recommended reviewer focus:

| Reviewer focus | Automated proof that must still exist |
|---|---|
| PPT templates look usable as QCC teaching and presentation assets. | T12 and T14 validate catalog entries, file paths, placeholders, expected assets, and demo-label declarations. |
| Demo labels are visually understandable in the template. | T12 and T14 validate declared demo-label metadata; reviewer feedback can request visual improvements during PR review. |
| Generated evidence remains the calculation record after slide edits. | T9, T20, and T21 validate evidence package authority and report/evidence references. |

## What not to test and why

- Do not test Control Chart behavior because Control Chart is explicitly outside the required first vertical proof slice.
- Do not test automated PPTX generation because the first slice uses static templates and slide-ready assets.
- Do not test web UI, dashboard, CAPA/EQMS, approval workflow, or document-editor behavior because they are excluded scope.
- Do not require pixel-perfect chart image tests; chart-spec assertions are the semantic proof, with optional rendering smoke tests.
- Do not test AI-generated interpretation because the core first slice must not use opaque AI-generated conclusions.
- Do not test external network services because first-slice execution is local-first and should not require network calls.

## Uncovered gaps

None that require returning to spec or architecture before test-spec-review.

Known implementation-time refinements:

- Exact public API names will be settled in M1-M2 and checked by public-API tests.
- Exact PPT binary inspection depth may depend on available tooling; visual review remains part of downstream code review and PR review rather than a separate manual proof gate.
- Exact HTML report renderer behavior is optional and should not block Markdown report proof.

## Next artifacts

- Fresh test-spec review at `docs/changes/2026-07-07-create-qcc-toolkit/reviews/test-spec-review-r2.md`.
- Implementation M1 only after clean test-spec review approval.

## Follow-on artifacts

- Test-spec review R1: `docs/changes/2026-07-07-create-qcc-toolkit/reviews/test-spec-review-r1.md`
- Review resolution: `docs/changes/2026-07-07-create-qcc-toolkit/review-resolution.md`

## Readiness

Approved for implementation handoff by `docs/changes/2026-07-07-create-qcc-toolkit/reviews/test-spec-review-r2.md`.
Implementation may proceed to M1 according to the approved plan.
