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
| EB1-EB7 | M1, M4 |
| O1-O5 | M1, M4 |
| S1-S4 | M2, M3, M4 |
| UX1-UX5 | M2, M3 |
| P1-P2 | M1, M2 |

## Current Handoff Summary

- Current milestone: M1
- Current milestone state: review-requested
- Last reviewed milestone: none
- Review status: proposal-review approved; spec-review approved; architecture-review approved; plan-review approved; test-spec-review approved
- Remaining in-scope implementation milestones: M1, M2, M3, M4
- Next stage: code-review M1
- Final closeout readiness: not-ready
- Reason final closeout is or is not ready: M1 is implemented and awaiting code-review; M2-M4 implementation, code-review, explain-change, verify, and PR handoff are still pending.

## Milestones

### M1. Method-kit catalog contract and validation

- Milestone state: review-requested
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

- Milestone state: planned
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
- Risks:
  - PPTX binary review remains difficult.
  - Embedded formulas can be overwritten by users.
- Rollback/recovery:
  - Keep source notes and deterministic builder evidence aligned with binary templates.
  - Add review checklist items for formula overwrite risk.

### M3. Worksheet and diagram method kits

- Milestone state: planned
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
- Risks:
  - Template content may become visually crowded.
  - Method guidance may drift from PowerPoint source notes.
- Rollback/recovery:
  - Keep method guides canonical and source notes concise.
  - Split dense content across slides rather than removing required guidance.

### M4. Incoming-template and evidence-level closeout

- Milestone state: planned
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
- Risks:
  - Evidence-level guidance may become too policy-heavy for templates.
  - Incoming-template folders may invite unreviewed private files.
- Rollback/recovery:
  - Keep incoming area documentation-first unless real source templates are intentionally added.
  - Add explicit privacy warnings before accepting incoming assets.

## Validation plan

| Command or check | Purpose |
|---|---|
| `python -m pytest` | Run full local test suite after implementation milestones. |
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

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-08 | Split implementation into catalog contract, Pareto kit, worksheet/diagram kits, and closeout. | Keeps each milestone reviewable and matches the main risk areas. | One large template rewrite milestone. |
| 2026-07-08 | Keep incoming-template handling late in the plan. | Official kit metadata and content patterns should stabilize before adding source-template intake behavior. | Adding incoming assets before official kit standard is proven. |
| 2026-07-08 | Use manual visual review as required proof for PPTX usability. | Automated checks can inspect metadata and text, but cannot fully prove slide readability or copyability. | Claiming visual quality from catalog or unit tests alone. |
| 2026-07-08 | Keep M1 catalog fields additive while making official entries stricter. | Existing first-slice entries can migrate without changing PPTX generation or Pareto evidence behavior. | Replacing the catalog format or making template content checks depend on opaque PPTX inspection in M1. |
| 2026-07-08 | Treat optional Pareto assist differently from Python-assisted method modes. | Pareto has optional raw-data/reproducibility help, while `python_assisted_chart` and `python_first_analysis` require sample input, runnable assist, output example, and reproducibility note. | Requiring full Python-assisted artifacts for every optional assist method. |

## Surprises and discoveries

- `/usr/bin/python` does not have `pytest`; the project dev environment is `.venv/bin/python`, which was used for M1 validation.

## Validation notes

- M1 expected failing proof:
  - `python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` failed before implementation because `/usr/bin/python` has no `pytest`.
  - `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` then failed against the old catalog model with missing `official_templates`, `implementation_mode`, `chart_editability`, and Python assist validation branches.
- M1 targeted validation:
  - `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` passed: 11 passed.
  - `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` passed: validated 5 template catalog entries.
  - `.venv/bin/python -m ruff check qcc_toolkit tests` passed.
  - `.venv/bin/python -m mypy qcc_toolkit` passed.

## Outcome and retrospective

- Filled after implementation and verification.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review M1.
- M1 is not closed until code-review completes.
