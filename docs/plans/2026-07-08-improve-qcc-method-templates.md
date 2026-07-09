# Improve QCC Method Templates Plan

## Status

- Plan lifecycle state: active
- Terminal disposition: not-applicable
- Plan review: approved
- Test spec: approved

## Purpose / big picture

This plan sequences the approved QCC Method Kits spec into reviewable implementation milestones.
The work improves QCC method templates from shallow placeholder decks into PowerPoint-first, Python-assisted method kits with Markdown guidance, catalog traceability, review checklists, evidence-level guidance, and optional Python assist where useful.

Readiness is not Done.
Implementation handoff is allowed after approved plan-review, test-spec, and test-spec-review; final closeout still requires implementation, code-review, explain-change, verify, and PR handoff.

## Source artifacts

- Proposal: [docs/proposals/2026-07-08-improve-qcc-method-templates.md](../proposals/2026-07-08-improve-qcc-method-templates.md)
- Spec: [specs/qcc-method-kits.md](../../specs/qcc-method-kits.md)
- Architecture: [docs/architecture/method-kits/architecture.md](../architecture/method-kits/architecture.md)
- Proposal review: [docs/changes/2026-07-08-improve-qcc-method-templates/reviews/proposal-review-r1.md](../changes/2026-07-08-improve-qcc-method-templates/reviews/proposal-review-r1.md)
- Spec review: [docs/changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md](../changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md)
- Architecture review: [docs/changes/2026-07-08-improve-qcc-method-templates/reviews/architecture-review-r1.md](../changes/2026-07-08-improve-qcc-method-templates/reviews/architecture-review-r1.md)
- Test spec: [specs/qcc-method-kits.test.md](../../specs/qcc-method-kits.test.md)
- Test spec review: [docs/changes/2026-07-08-improve-qcc-method-templates/reviews/test-spec-review-r1.md](../changes/2026-07-08-improve-qcc-method-templates/reviews/test-spec-review-r1.md)

## Context and orientation

The repository already contains first-slice Markdown method guides, real PPTX method templates, source notes, template catalog validation, and a Pareto evidence engine.
This change raises the quality bar for those assets and records method-kit behavior as the official unit of work.

The implementation must preserve the source-of-truth split:

- PowerPoint method kits teach, guide work, provide demo examples, and give users copyable working slides.
- Markdown method guides govern method knowledge and facilitator review guidance.
- Python assist is optional or recommended only when analysis complexity, raw data, validation, repetition, or evidence rigor requires it.
- Evidence packages remain authoritative for high-rigor data-dependent conclusions where Python assist is used.

## Non-goals

- Do not require Python for every QCC method or chart.
- Do not implement full automated PPTX generation.
- Do not create a web UI, dashboard, CAPA/EQMS workflow, desktop app, or document-management system.
- Do not add Control Chart, Process Capability, DOE, regression, or advanced statistical methods.
- Do not change existing Pareto evidence package behavior unless the approved spec explicitly requires it.

## Requirements covered

| Requirement range | Milestones |
|---|---|
| R1-R10 | M1, M2, M3 |
| R11-R17 | M1, M2 |
| R18-R21 | M1, M4 |
| R22-R29 | M2, M3 |
| R30-R34 | M1, M2, M3, M4 |
| R35-R39 | M4 |
| R40 | All milestones as scope guardrail |
| R41-R44 | M5 |
| R45-R52 | M6 |
| EB1-EB7 | M1, M4 |
| O1-O5 | M1, M4 |
| S1-S4 | M2, M3, M4 |
| UX1-UX5 | M2, M3 |
| P1-P2 | M1, M2 |

## Current Handoff Summary

- Current milestone: M6
- Current milestone state: review-requested
- Last reviewed milestone: M5
- Review status: proposal-review approved; spec-review approved; architecture-review approved; plan-review approved; test-spec-review approved
- Remaining in-scope implementation milestones: M6
- Next stage: code-review M6
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1, M2, M3, M4, and M5 are closed by code review; M6 Fishbone diagram-quality implementation is review-requested; explain-change and verify must be refreshed after M6 review.

## Milestones

### M1. Method-kit catalog contract and validation

- Milestone state: closed
- Goal: Extend catalog/source validation so official method kits, implementation modes, Python assist status, evidence levels, and incoming/source distinction are machine-checkable where practical.
- Requirements: R1-R21, R30-R34, EB1-EB4, O1-O5, P1
- Files/components likely touched:
  - `templates/ppt/catalog.yml`
  - `qcc_toolkit/templates/`
  - `tests/test_template_catalog*.py`
  - optional `docs/template-standards/`
- Tests to add/update:
  - Catalog accepts complete official kit metadata.
  - Catalog rejects missing required paths.
  - Catalog rejects duplicate official method-kit ownership.
  - Catalog distinguishes official kits from incoming/source templates.
  - Catalog validates implementation mode and Python assist status.
- Validation commands:
  - `python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py`
  - `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - `python -m ruff check qcc_toolkit tests`
  - `python -m mypy qcc_toolkit`
- Expected observable result: Reviewers can inspect and validate official kit metadata and incoming/source status before template content is expanded.
- Implementation evidence:
  - Added explicit catalog fields for official/source classification, method name, implementation mode, Python assist status and reasons, minimum content metadata, evidence levels, chart editability, and Python-assisted artifact paths.
  - Updated catalog validation to reject incomplete official method-kit metadata, missing source notes, missing chart editability metadata for chart modes, and missing Python-assisted artifact paths for recommended/required assist paths.
  - Migrated the five first-slice catalog entries with official method-kit metadata and expected implementation modes.
  - Updated catalog acceptance and failure tests before implementation.
- Risks:
  - Catalog schema may become too broad before template structure is stable.
  - Existing first-slice catalog entries may need migration.
- Rollback/recovery:
  - Keep new fields additive where possible.
  - Preserve existing catalog validation behavior for first-slice paths while adding stricter official-kit checks.

### M2. Improved Pareto Chart method kit

- Milestone state: closed
- Goal: Upgrade Pareto Chart into the first complete PowerPoint-native chart method kit with optional Python assist guidance.
- Requirements: R1-R13, R18-R19, R22-R23, R26-R34, R38-R40, UX1-UX5, P2
- Files/components likely touched:
  - `docs/methods/pareto_chart.md`
  - `templates/ppt/methods/pareto-chart-template.pptx`
  - `templates/ppt/sources/pareto-chart.md`
  - `templates/ppt/catalog.yml`
  - `tools/build_ppt_templates.py`
  - template and guide tests
- Tests to add/update:
  - Pareto guide contains method-kit required sections.
  - Pareto template/source notes contain demo, blank slide, edit instructions, interpretation patterns, mistakes, checklist, evidence/source note, and Python assist rule.
  - Pareto catalog entry declares `powerpoint_native_chart` and optional Python assist.
  - Pareto template remains editable or documents any non-editable chart reason.
- Validation commands:
  - `python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py`
  - `python tools/build_ppt_templates.py`
  - `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - `python -m ruff check .`
- Expected observable result: A QCC user can open the Pareto kit, learn the method, edit a simple chart, copy a blank project slide, and know when Python assist is recommended.
- Implementation evidence:
  - Added Pareto guide sections for purpose, PowerPoint workflow, edit instructions, blank copyable slide, interpretation patterns, Python assist decision, and evidence levels/source notes.
  - Expanded Pareto source notes with the full method-kit section contract, edit guidance, common mistakes, facilitator checklist, Python assist triggers, and evidence/source note expectations.
  - Updated `tools/build_ppt_templates.py` so the Pareto PPTX builds as a 10-slide method kit with purpose, QCC stage fit, use/not-use, required inputs, edit instructions, interpretation patterns, mistakes, checklist, evidence/source note, completed demo, and blank project slide surfaces.
  - Regenerated `templates/ppt/methods/pareto-chart-template.pptx`.
  - Added guide/source/PPTX tests before implementation.
  - Catalog entry was unchanged in M2 because M1 already declared Pareto as `powerpoint_native_chart` with optional Python assist and chart editability metadata.
  - MP1 manual template review was recorded in `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md`.
- Risks:
  - PPTX binary review remains difficult.
  - Embedded formulas can be overwritten by users.
- Rollback/recovery:
  - Keep source notes and deterministic builder evidence aligned with binary templates.
  - Add review checklist items for formula overwrite risk.

### M3. Worksheet and diagram method kits

- Milestone state: closed
- Goal: Upgrade 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram into complete template-native method kits.
- Requirements: R1-R10, R18-R19, R22, R24-R25, R30-R32, R35-R39, UX1-UX5
- Files/components likely touched:
  - `docs/methods/5w2h.md`
  - `docs/methods/5_whys.md`
  - `docs/methods/check_sheet.md`
  - `docs/methods/fishbone_diagram.md`
  - matching PPTX templates and source notes
  - `templates/ppt/catalog.yml`
  - template and guide tests
- Tests to add/update:
  - Each method guide contains required method-kit guidance.
  - Each source note/template exposes demo example, blank working slide or worksheet, interpretation patterns, mistakes, facilitator checklist, Python assist decision, and evidence/source note.
  - Catalog declares correct implementation modes.
  - No template claims unsupported final data-dependent calculations.
- Validation commands:
  - `python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py`
  - `python tools/build_ppt_templates.py`
  - `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
- Expected observable result: The first method-kit set proves worksheet, logic-chain, data-collection, and diagram kit patterns without over-automating qualitative methods.
- Implementation evidence:
  - Added method-kit guide sections for 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram covering purpose, PowerPoint workflow, blank working slide or worksheet, interpretation patterns, Python assist decision, and evidence levels/source notes.
  - Expanded matching PowerPoint source notes with required method-kit sections: purpose, QCC stage fit, use/not-use, inputs, completed demo, blank working surface, interpretation, mistakes, checklist, assist decision, and evidence/source note.
  - Updated `tools/build_ppt_templates.py` with template-native guidance data and generated 10-slide decks for the four worksheet/diagram kits.
  - Regenerated `templates/ppt/methods/5w2h-template.pptx`, `templates/ppt/methods/5-whys-template.pptx`, `templates/ppt/methods/check-sheet-template.pptx`, and `templates/ppt/methods/fishbone-diagram-template.pptx`.
  - Added guide/source/PPTX tests before implementation; the initial targeted run failed for missing non-chart method-kit sections and 4-slide PPTX decks.
  - Catalog entry implementation modes were unchanged because M1 already declared the correct `template_native_worksheet` and `template_native_diagram` modes.
  - MP2 manual template review was recorded in `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md`.
- Risks:
  - Template content may become visually crowded.
  - Method guidance may drift from PowerPoint source notes.
- Rollback/recovery:
  - Keep method guides canonical and source notes concise.
  - Split dense content across slides rather than removing required guidance.

### M4. Incoming-template and evidence-level closeout

- Milestone state: closed
- Goal: Add incoming-template handling, evidence-level guidance, and final consistency checks across official method kits.
- Requirements: R18-R21, R30-R39, EB5-EB7, O1-O5, S1-S4, AC1-AC8
- Files/components likely touched:
  - `templates/incoming/` or documented incoming-template placeholder
  - `docs/template-standards/`
  - `templates/ppt/catalog.yml`
  - `tests/`
  - `docs/changes/2026-07-08-improve-qcc-method-templates/`
- Tests to add/update:
  - Incoming/source templates are distinguishable from official kits.
  - Privacy review guidance exists for incoming templates.
  - Evidence levels are documented and referenced from method kits.
  - Artifact consistency checks map official kits to guides, templates, source notes, and catalog entries.
- Validation commands:
  - `python -m pytest`
  - `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml`
  - `python -m ruff check .`
  - `python -m mypy qcc_toolkit`
  - `git diff --check`
- Expected observable result: The full first method-kit set is internally consistent, cataloged, and ready for final review.
- Implementation evidence:
  - Added `docs/template-standards/evidence-levels.md` to define Level 1 through Level 4 evidence expectations and the manual PowerPoint boundary.
  - Added `docs/template-standards/incoming-templates.md` and `templates/incoming/README.md` to keep incoming templates separate, unofficial, and privacy-reviewed before migration.
  - Added `docs/template-standards/method-kit-review-checklist.md` to define demo, source/date, method logic, checklist, Python assist, and evidence/source review failures.
  - Added `tests/test_method_kit_closeout.py` for evidence-level guidance, incoming-template privacy/source handling, review-checklist failure conditions, and official-kit cross-artifact consistency.
  - Extended catalog tests so incoming/source entries remain disjoint from official entries and can be validated as source assets without claiming official ownership.
  - Recorded MP3 package/text inspection for the final official method-kit set in `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md`.
- Risks:
  - Evidence-level guidance may become too policy-heavy for templates.
  - Incoming-template folders may invite unreviewed private files.
- Rollback/recovery:
  - Keep incoming area documentation-first unless real source templates are intentionally added.
  - Add explicit privacy warnings before accepting incoming assets.

### M5. Pareto chart-quality upgrade

- Milestone state: closed
- Goal: Improve chart usefulness in the Pareto method kit with chart decision, variant, and quality-check surfaces.
- Requirements: R41-R44, AC9
- Files/components touched:
  - `docs/template-standards/chart-template-standard.md`
  - `docs/methods/pareto_chart.md`
  - `templates/ppt/sources/pareto-chart.md`
  - `templates/ppt/methods/pareto-chart-template.pptx`
  - `tools/build_ppt_templates.py`
  - `tests/test_template_assets.py`
  - `tests/test_method_kit_closeout.py`
  - `specs/qcc-method-kits.md`
  - `specs/qcc-method-kits.test.md`
- Tests added:
  - Pareto source notes declare chart decision, variant, and chart-quality surfaces.
  - Pareto PPTX exposes chart decision, variant, and chart-quality surfaces.
  - Chart template standard defines the reusable chart quality bar.
- Expected observable result: Pareto is a stronger chart template with chart decision guidance, an actual chart variant slide, cumulative/before-after/focus-annotation guidance, and a reviewer-oriented chart quality checklist.
- Implementation evidence:
  - Added `docs/template-standards/chart-template-standard.md`.
  - Added Pareto guide/source-note guidance for Chart decision guide, Chart variant library, Chart quality checklist, Percent, Cumulative percent, and Formula check.
  - Updated `tools/build_ppt_templates.py` with three additional Pareto chart-quality slides, including a chart variant library slide with an embedded chart.
  - Regenerated `templates/ppt/methods/pareto-chart-template.pptx`.
  - Added failing tests first; the targeted run failed for missing chart-standard, source-note, and PPTX surfaces, then passed after implementation.
- Validation:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_pareto_source_notes_declare_chart_quality_standard tests/test_template_assets.py::test_pareto_pptx_exposes_chart_quality_surfaces tests/test_method_kit_closeout.py::test_chart_template_standard_defines_chart_quality_bar` failed before implementation as expected.
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_pareto_source_notes_declare_chart_quality_standard tests/test_template_assets.py::test_pareto_pptx_exposes_chart_quality_surfaces tests/test_method_kit_closeout.py::test_chart_template_standard_defines_chart_quality_bar` passed: 3 passed.
  - `.venv/bin/python -m pytest tests/test_template_assets.py tests/test_method_kit_closeout.py tests/test_method_guides.py` passed: 20 passed.
  - `.venv/bin/python -m pytest` passed: 79 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
- Risks:
  - More Pareto slides may make the deck feel larger.
  - Variant guidance is still package/text checked, not rendered with PowerPoint.
- Rollback/recovery:
  - Revert the M5 generator/source/test changes and regenerate the Pareto PPTX if the chart-focused deck becomes too heavy.

### M6. Fishbone diagram-quality upgrade

- Milestone state: review-requested
- Goal: Improve Fishbone usefulness with diagram decision guidance, verification markers, testable cause wording, a cleaner editable fishbone diagram surface, optional Python-generated SVG output, and a cause verification plan.
- Requirements: R45-R52
- Files/components touched:
  - `docs/methods/fishbone_diagram.md`
  - `templates/ppt/sources/fishbone-diagram.md`
  - `templates/ppt/methods/fishbone-diagram-template.pptx`
  - `tools/build_ppt_templates.py`
  - `tests/test_template_assets.py`
  - `tests/test_method_guides.py`
  - `specs/qcc-method-kits.md`
  - `specs/qcc-method-kits.test.md`
  - `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md`
  - `qcc_toolkit/fishbone.py`
  - `examples/scripts/generate_fishbone.py`
  - `examples/projects/reduce-packing-label-errors/evidence/fishbone/fishbone.svg`
  - `examples/projects/reduce-packing-label-errors/evidence/fishbone/README.md`
  - `examples/projects/reduce-packing-label-errors/README.md`
  - `tests/test_fishbone_generation.py`
  - `tests/test_generate_fishbone_script.py`
- Tests added:
  - Fishbone source notes declare diagram quality, verification marker, cause wording, editable diagram, and verification-plan surfaces.
  - Fishbone PPTX exposes diagram quality, marker legend, editable diagram, evidence/source, and verification-plan surfaces.
  - Fishbone guide contains diagram quality, marker legend, cause wording, and verification-plan guidance.
  - Fishbone source/PPTX expose visual-design rules for centered composition, short labels, branch label capsules, status badges, and details kept in the verification plan.
  - Fishbone Python SVG renderer and starter script generate a readable static presentation asset.
- Expected observable result: Fishbone is a stronger template-native diagram kit that helps users create a testable cause map without overclaiming that brainstorming proves root cause.
- Implementation evidence:
  - Added Fishbone guide/source-note sections for Diagram quality guide, Verification marker legend, Cause wording guide, Editable fishbone diagram, and Cause verification plan.
  - Updated `tools/build_ppt_templates.py` with four Fishbone-specific slides, including an editable fishbone diagram surface with branch/cause boxes and evidence/source fields.
  - Refined the generated Fishbone diagram surface to use a centered spine, aligned branches, branch label capsules, short cause labels, compact status badges, and a separate evidence/verification panel.
  - Added `qcc_toolkit.fishbone`, `examples/scripts/generate_fishbone.py`, and a synthetic generated SVG example under `examples/projects/reduce-packing-label-errors/evidence/fishbone/`.
  - Updated the Fishbone catalog entry from unavailable Python assist to optional SVG assist.
  - Regenerated `templates/ppt/methods/fishbone-diagram-template.pptx`; other generated PPTX files remained unchanged.
  - Added failing tests first; the targeted run failed for missing diagram-quality guide/source/PPTX surfaces, then passed after implementation.
  - Added failing visual-design proof after follow-up feedback; the targeted run failed for missing visual-design terms, then passed after refinement.
  - Added failing Python SVG proof after follow-up feedback; the targeted run failed because the renderer and script did not exist, then passed after implementation.
- Validation:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces tests/test_method_guides.py::test_fishbone_guide_contains_diagram_quality_guidance` failed before implementation as expected.
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces tests/test_method_guides.py::test_fishbone_guide_contains_diagram_quality_guidance` passed: 3 passed.
  - `.venv/bin/python -m pytest tests/test_template_assets.py tests/test_method_guides.py tests/test_method_kit_closeout.py` passed: 23 passed.
  - `.venv/bin/python tools/build_ppt_templates.py` passed.
  - `git diff --exit-code -- templates/ppt/methods/5w2h-template.pptx templates/ppt/methods/5-whys-template.pptx templates/ppt/methods/check-sheet-template.pptx templates/ppt/methods/pareto-chart-template.pptx` passed.
  - `.venv/bin/python -m pytest` passed: 82 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
  - MP4 package/text inspection found 14 Fishbone slides with required diagram-quality terms present.
  - Follow-up visual-design proof `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces` failed before refinement because the source/PPTX lacked visual-design rule terms.
  - Follow-up visual-design proof passed after refinement: 2 passed.
  - `.venv/bin/python tools/build_ppt_templates.py` passed after refinement.
  - `git diff --exit-code -- templates/ppt/methods/5w2h-template.pptx templates/ppt/methods/5-whys-template.pptx templates/ppt/methods/check-sheet-template.pptx templates/ppt/methods/pareto-chart-template.pptx` passed after refinement.
  - `.venv/bin/python -m pytest` passed after refinement: 82 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed after refinement: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed after refinement.
  - `.venv/bin/python -m mypy qcc_toolkit` passed after refinement.
  - `git diff --check` passed after refinement.
  - `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py` failed before implementation as expected because the Fishbone Python renderer and script did not exist.
  - `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py` passed after implementation: 5 passed.
  - `.venv/bin/python examples/scripts/generate_fishbone.py --output examples/projects/reduce-packing-label-errors/evidence/fishbone` passed.
  - `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py tests/test_template_catalog.py tests/test_method_guides.py tests/test_template_assets.py` passed: 29 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed after SVG assist update: validated 5 template catalog entries.
- Risks:
  - No PowerPoint or LibreOffice renderer is available in this environment, so M6 visual proof uses package/text extraction rather than rendered screenshots.
  - The Fishbone deck is larger than the other template-native decks.
- Rollback/recovery:
  - Revert the M6 generator/source/test changes and regenerate the Fishbone PPTX if the diagram-quality slides make the deck too heavy.

## Validation plan

| Command or check | Purpose |
|---|---|
| `python -m pytest` | Run full local test suite after implementation milestones. |
| `python -m pytest tests/test_template_assets.py tests/test_method_kit_closeout.py tests/test_method_guides.py` | Target chart/template quality proof. |
| `python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py tests/test_template_catalog_failures.py` | Target method-guide, template, and catalog proof. |
| `python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | Validate catalog traceability and method-kit metadata. |
| `python tools/build_ppt_templates.py` | Regenerate PPTX templates from deterministic source where applicable. |
| `python -m ruff check .` | Lint changed Python and test code. |
| `python -m mypy qcc_toolkit` | Type-check package changes. |
| Manual visual review of generated PPTX files | Confirm slide readability, copyability, demo labeling, and chart editability that cannot be fully proven by text checks. |
| `git diff --check` | Catch whitespace errors before handoff. |

## Risks and recovery

| Risk | Recovery |
|---|---|
| PPTX files are hard to review in diffs. | Keep source notes, catalog metadata, deterministic builder output, and targeted PPTX inspections aligned. |
| Method-kit content becomes too broad for one milestone. | Keep Pareto in M2 and worksheet/diagram kits in M3. |
| Catalog schema changes break existing tests. | Add compatibility-focused tests first and migrate entries intentionally. |
| Manual visual review is skipped or weak. | Test-spec should name manual visual proof as required evidence for template readability and copyability. |
| Python assist policy becomes too vague. | Require explicit assist status and reason fields in catalog/source notes. |

## Dependencies

- Accepted proposal and approved proposal review.
- Approved `specs/qcc-method-kits.md`.
- Approved `docs/architecture/method-kits/architecture.md`.
- Existing first-slice template builder, catalog validator, method guides, and PPTX assets.
- Local Python environment with current project dev dependencies.

## Progress

- 2026-07-08: Plan drafted after approved proposal, spec, and architecture.
- 2026-07-08: Plan review approved the milestone sequence and validation approach.
- 2026-07-08: Test-spec review approved the proof map and allowed implementation handoff.
- 2026-07-08: M1 implementation completed and moved to code-review handoff.
- 2026-07-08: M1 code review completed clean-with-notes and closed the milestone.
- 2026-07-08: M2 implementation completed and moved to code-review handoff.
- 2026-07-08: M2 code review completed clean-with-notes and closed the milestone.
- 2026-07-08: M3 implementation completed and moved to code-review handoff.
- 2026-07-08: M3 code review completed clean-with-notes and closed the milestone.
- 2026-07-09: M4 implementation completed and moved to code-review handoff.
- 2026-07-09: M4 code review completed clean-with-notes and closed the final implementation milestone.
- 2026-07-09: Explain-change completed from the final reviewed diff and moved the workflow to verify.
- 2026-07-09: Final verify passed with local branch-ready evidence and moved the workflow to PR handoff.
- 2026-07-09: M5 Pareto chart-quality implementation completed and moved to code-review handoff after open PR feedback that charts remained too weak.
- 2026-07-09: M5 code review completed clean-with-notes and closed the milestone.
- 2026-07-09: M6 Fishbone diagram-quality implementation completed and moved to code-review handoff after follow-up feedback to improve the Fishbone template according to best practices.
- 2026-07-09: M6 Fishbone visual-design refinement completed after feedback that the generated diagram looked unattractive.
- 2026-07-09: M6 optional Python Fishbone SVG assist completed after feedback that the generated PowerPoint diagram remained unreadable.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-08 | Split implementation into catalog contract, Pareto kit, worksheet/diagram kits, and closeout. | Keeps each milestone reviewable and matches the main risk areas. | One large template rewrite milestone. |
| 2026-07-08 | Keep incoming-template handling late in the plan. | Official kit metadata and content patterns should stabilize before adding source-template intake behavior. | Adding incoming assets before official kit standard is proven. |
| 2026-07-08 | Use manual visual review as required proof for PPTX usability. | Automated checks can inspect metadata and text, but cannot fully prove slide readability or copyability. | Claiming visual quality from catalog or unit tests alone. |
| 2026-07-08 | Keep M1 catalog fields additive while making official entries stricter. | Existing first-slice entries can migrate without changing PPTX generation or Pareto evidence behavior. | Replacing the catalog format or making template content checks depend on opaque PPTX inspection in M1. |
| 2026-07-08 | Treat optional Pareto assist differently from Python-assisted method modes. | Pareto has optional raw-data/reproducibility help, while `python_assisted_chart` and `python_first_analysis` require sample input, runnable assist, output example, and reproducibility note. | Requiring full Python-assisted artifacts for every optional assist method. |
| 2026-07-08 | Expand only Pareto in M2 while leaving worksheet and diagram kits for M3. | The approved plan uses Pareto to prove the PowerPoint-native chart kit before scaling the pattern. | Updating every method guide and template in the same milestone. |
| 2026-07-08 | Keep full visual rendering as a recorded limitation for MP1. | PowerPoint and LibreOffice are not available in this environment; deterministic generation, package checks, and `python-pptx` layout/text extraction are the available local proof. | Claiming a PowerPoint-rendered visual review without tool evidence. |
| 2026-07-08 | Use a shared template-native slide pattern for 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram. | The methods need the same minimum kit surfaces but method-specific guidance; shared layout reduces drift while preserving content differences. | Hand-authoring unrelated slide structures for each non-chart method. |
| 2026-07-09 | Keep incoming-template handling documentation-first for M4. | The approved slice needs a safe holding area and review policy, not real unreviewed user templates. | Adding sample incoming PPTX files or treating incoming assets as official catalog entries. |
| 2026-07-09 | Add a narrow M5 Pareto chart-quality upgrade instead of broadening every template at once. | User feedback specifically says chart quality remains weak; Pareto is the first chart-native kit and can prove the stronger standard. | Rewriting every method template again; adding Histogram/Trend/Scatter before the chart standard is proven. |
| 2026-07-09 | Add a narrow M6 Fishbone diagram-quality upgrade instead of broadening every diagram template at once. | Follow-up feedback specifically asked to improve `fishbone-diagram-template.pptx`; Fishbone is the first diagram-native kit and can prove the stronger diagram standard. | Rewriting every template-native method again; adding unrelated diagram methods. |
| 2026-07-09 | Keep Fishbone diagram labels short and move verification detail to the plan slide. | Dense cause boxes made the generated diagram unattractive and harder to scan. | Keeping full cause/evidence sentences inside the fishbone diagram. |
| 2026-07-09 | Add optional Python-generated SVG for Fishbone instead of replacing the editable PowerPoint template. | The user still needs a readable presentation asset, while PowerPoint remains useful for editing and teaching. | Making Python the only Fishbone workflow; adding new rendering dependencies. |

## Surprises and discoveries

- `/usr/bin/python` does not have `pytest`; the project dev environment is `.venv/bin/python`, which was used for M1 validation.
- No PowerPoint or LibreOffice renderer is available in this environment for MP1; the manual review used package/text/layout inspection and records that limitation.
- No PowerPoint or LibreOffice renderer is available in this environment for MP2; the manual review used deterministic PPTX package/text inspection and records that limitation.
- No PowerPoint or LibreOffice renderer is available in this environment for MP3; the manual review used deterministic PPTX package/text inspection and records that limitation.

## Validation notes

- M1 expected failing proof:
  - `python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` failed before implementation because `/usr/bin/python` has no `pytest`.
  - `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` then failed against the old catalog model with missing `official_templates`, `implementation_mode`, `chart_editability`, and Python assist validation branches.
- M1 targeted validation:
  - `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` passed: 11 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check qcc_toolkit tests` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
- M2 expected failing proof:
  - `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` failed before implementation with missing Pareto guide sections, missing source-note method-kit sections, and only 4 Pareto PPTX slides.
- M2 targeted validation:
  - `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` passed: 14 passed.
  - `.venv/bin/python tools/build_ppt_templates.py` passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - MP1 manual review recorded package/text/layout inspection for the Pareto template.
- M3 expected failing proof:
  - `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` failed before implementation with missing template-native guide sections, missing source-note method-kit sections, and only 4 slides in each non-chart PPTX deck.
- M3 targeted validation:
  - `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` passed: 17 passed.
  - `.venv/bin/python tools/build_ppt_templates.py` passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
  - MP2 manual review recorded package/text inspection for 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram.
- M3 code review:
  - `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m3-r1.md` recorded clean-with-notes with no material findings.
  - Reviewer-rerun `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` passed: 17 passed.
  - Reviewer-rerun `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - Reviewer-rerun `git diff --check` passed.
  - Reviewer direct PPTX package inspection found each M3 template has 10 slides and no missing required M3 method-kit surface terms.
- M4 expected failing proof:
  - `.venv/bin/python -m pytest tests/test_method_kit_closeout.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_artifact_consistency.py tests/test_acceptance.py tests/test_scope_guards.py` failed before implementation because `docs/template-standards/evidence-levels.md`, `docs/template-standards/incoming-templates.md`, `docs/template-standards/method-kit-review-checklist.md`, and `templates/incoming/README.md` did not exist.
- M4 targeted validation:
  - `.venv/bin/python -m pytest tests/test_method_kit_closeout.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_artifact_consistency.py tests/test_acceptance.py tests/test_scope_guards.py` passed: 20 passed.
  - `.venv/bin/python -m pytest` passed: 76 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
  - MP3 manual review recorded package/text inspection for all five official method kits.
- M4 code review:
  - `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m4-r1.md` recorded clean-with-notes with no material findings.
  - Reviewer-rerun `.venv/bin/python -m pytest tests/test_method_kit_closeout.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_artifact_consistency.py tests/test_acceptance.py tests/test_scope_guards.py` passed: 20 passed.
  - Reviewer-rerun `.venv/bin/python -m pytest` passed: 76 passed.
  - Reviewer-rerun `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - Reviewer-rerun `.venv/bin/python -m ruff check .` passed.
  - Reviewer-rerun `.venv/bin/python -m mypy qcc_toolkit` passed.
  - Reviewer-rerun `git diff --check` passed.
- M5 expected failing proof:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_pareto_source_notes_declare_chart_quality_standard tests/test_template_assets.py::test_pareto_pptx_exposes_chart_quality_surfaces tests/test_method_kit_closeout.py::test_chart_template_standard_defines_chart_quality_bar` failed before implementation because the chart standard, Pareto source-note chart-quality section, and 13-slide Pareto PPTX surfaces did not exist.
- M5 targeted validation:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_pareto_source_notes_declare_chart_quality_standard tests/test_template_assets.py::test_pareto_pptx_exposes_chart_quality_surfaces tests/test_method_kit_closeout.py::test_chart_template_standard_defines_chart_quality_bar` passed: 3 passed.
  - `.venv/bin/python -m pytest tests/test_template_assets.py tests/test_method_kit_closeout.py tests/test_method_guides.py` passed: 20 passed.
  - `.venv/bin/python -m pytest` passed: 79 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
- M5 code review:
  - `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m5-r1.md` recorded clean-with-notes with no material findings.
  - Reviewer-rerun `.venv/bin/python tools/build_ppt_templates.py` passed.
  - Reviewer-rerun `git diff --exit-code -- templates/ppt/methods/pareto-chart-template.pptx` passed.
  - Reviewer-rerun `.venv/bin/python -m pytest tests/test_template_assets.py tests/test_method_kit_closeout.py tests/test_method_guides.py` passed: 20 passed.
  - Reviewer-rerun `.venv/bin/python -m pytest` passed: 79 passed.
  - Reviewer-rerun `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - Reviewer-rerun `.venv/bin/python -m ruff check .` passed.
  - Reviewer-rerun `.venv/bin/python -m mypy qcc_toolkit` passed.
  - Reviewer-rerun `git diff --check` passed.
- M6 expected failing proof:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces tests/test_method_guides.py::test_fishbone_guide_contains_diagram_quality_guidance` failed before implementation because the Fishbone guide, source notes, and PPTX did not include diagram-quality surfaces.
  - Follow-up visual-design proof `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces` failed before refinement because the Fishbone source notes and PPTX did not include visual-design rule terms.
  - Follow-up Python SVG proof `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py` failed before implementation because `qcc_toolkit.fishbone` and `examples/scripts/generate_fishbone.py` did not exist.
- M6 targeted validation:
  - `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces tests/test_method_guides.py::test_fishbone_guide_contains_diagram_quality_guidance` passed: 3 passed.
  - `.venv/bin/python -m pytest tests/test_template_assets.py tests/test_method_guides.py tests/test_method_kit_closeout.py` passed: 23 passed.
  - `.venv/bin/python tools/build_ppt_templates.py` passed.
  - `git diff --exit-code -- templates/ppt/methods/5w2h-template.pptx templates/ppt/methods/5-whys-template.pptx templates/ppt/methods/check-sheet-template.pptx templates/ppt/methods/pareto-chart-template.pptx` passed.
  - `.venv/bin/python -m pytest` passed: 82 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check .` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.
  - `git diff --check` passed.
  - Follow-up visual-design proof `.venv/bin/python -m pytest tests/test_template_assets.py::test_fishbone_source_notes_declare_diagram_quality_standard tests/test_template_assets.py::test_fishbone_pptx_exposes_diagram_quality_surfaces` passed: 2 passed.
  - Follow-up `.venv/bin/python tools/build_ppt_templates.py` passed.
  - Follow-up `git diff --exit-code -- templates/ppt/methods/5w2h-template.pptx templates/ppt/methods/5-whys-template.pptx templates/ppt/methods/check-sheet-template.pptx templates/ppt/methods/pareto-chart-template.pptx` passed.
  - Follow-up `.venv/bin/python -m pytest` passed: 82 passed.
  - Follow-up `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - Follow-up `.venv/bin/python -m ruff check .` passed.
  - Follow-up `.venv/bin/python -m mypy qcc_toolkit` passed.
  - Follow-up `git diff --check` passed.
  - Follow-up Python SVG proof `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py` passed: 5 passed.
  - Follow-up `.venv/bin/python examples/scripts/generate_fishbone.py --output examples/projects/reduce-packing-label-errors/evidence/fishbone` passed.
  - Follow-up `.venv/bin/python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py tests/test_template_catalog.py tests/test_method_guides.py tests/test_template_assets.py` passed: 29 passed.
  - Follow-up `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - MP4 package/text inspection found `fishbone-diagram-template.pptx` has 14 slides and required diagram-quality and visual-design terms.

## Outcome and retrospective

- Implementation and code review are complete across M1 through M4.
- M5 implementation and code review are complete.
- M6 implementation is complete and awaiting code review.
- Explain-change is recorded in `docs/changes/2026-07-08-improve-qcc-method-templates/explain-change.md`.
- The previous final verification is superseded by M5 and M6 and must be refreshed.
- The existing PR remains open but needs refreshed explain-change/verify/PR handoff after M6.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review M6.
- PR body/open readiness from the previous verify report is superseded until M6 code review, explain-change, verify, and PR handoff are refreshed.
