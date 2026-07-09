# Change Explanation: Improve QCC Method Templates

## Status

superseded-by-m5

## Summary

This change turns QCC method templates from shallow placeholder decks into PowerPoint-first, Python-assisted method kits.
The implemented slice keeps PowerPoint as the primary teaching, working, and presentation surface; Markdown as the canonical method reference; and Python as selective evidence assist for raw, repeated, complex, validation-heavy, or high-rigor work.

The final reviewed implementation includes:

- vision and positioning updates for the accepted direction;
- an approved method-kit spec, architecture package, plan, and test spec;
- stricter template catalog metadata and validation;
- complete first-slice method kits for Pareto Chart, 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram;
- evidence-level, incoming-template, and method-kit review standards;
- automated tests, manual package/text review evidence, and clean code reviews for M1 through M4.

At explain-change completion, final verify and PR handoff had not run yet.
Final verify is now recorded in `verify-report.md`; PR handoff remains pending.

After PR handoff, M5 added a Pareto chart-quality upgrade in response to feedback that charts were still too weak.
This explanation is historical for the M1-M4 reviewed diff and must be refreshed after M5 code review.

## Problem

The accepted proposal responded to feedback that the generated QCC method template was too simple to be useful.
The previous template had method identifiers, basic placeholders, demo labels, and a small editable chart/table, but it did not teach the method deeply enough or help users apply, review, and present the method with confidence.

The proposal also changed the product-surface priority for method-template work.
Many QCC users can work effectively in PowerPoint for common methods, so Python should not be required for every chart or worksheet.
Python remains important where PowerPoint is weak: validation, raw data, repeated generation, reproducibility, complex calculations, and evidence packaging.

## Decision Trail

| Source | Decision used |
|---|---|
| Proposal | Adopt PowerPoint-first, Python-assisted QCC method kits. |
| Proposal review | Accept the direction after amendments, including vision revision, minimum kit content, evidence levels, and incoming-template handling. |
| Vision update | Reframe `VISION.md`, README front matter, and strategic positioning around “PowerPoint teaches and presents, Markdown governs method knowledge, Python generates traceable QCC evidence.” |
| Spec | Requirements R1-R40 define official method-kit content, catalog behavior, evidence levels, incoming-template boundaries, and scope guardrails. |
| Architecture | Use a method-kit-centered repository model with official kits, incoming/source templates, catalog validation, optional Python assist, and evidence guidance. |
| Plan | Implement in four milestones: M1 catalog contract, M2 Pareto kit, M3 template-native kits, M4 closeout standards. |
| Test spec | Map requirements to T1-T12, manual proof MP1-MP3, and validation commands CMD1-CMD8. |
| Code reviews | M1, M2, M3, and M4 all closed clean-with-notes with no material findings. |

## Diff Rationale By Area

| Area | Files | Change | Reason | Evidence |
|---|---|---|---|---|
| Vision and positioning | `VISION.md`, `README.md`, `docs/vision/strategic-positioning.md` | Reframed the project around PowerPoint-first, Python-assisted method kits while preserving Markdown and Python evidence roles. | Proposal Vision fit and accepted positioning required a vision revision. | Proposal review approved; vision update recorded in `change.yaml`. |
| Governance artifacts | `docs/proposals/2026-07-08-improve-qcc-method-templates.md`, `specs/qcc-method-kits.md`, `docs/architecture/method-kits/architecture.md`, diagrams, `docs/plans/2026-07-08-improve-qcc-method-templates.md`, `specs/qcc-method-kits.test.md` | Added the accepted proposal, approved behavior contract, architecture boundaries, execution plan, and proof map. | The change affects user workflow, catalog semantics, template assets, and evidence expectations, so it needed durable source artifacts before implementation. | Proposal/spec/architecture/plan/test-spec reviews all approved with no material findings. |
| Workflow records | `docs/changes/2026-07-08-improve-qcc-method-templates/*`, `docs/plan.md` | Recorded change metadata, review log, manual template review, code reviews, and this explanation. | Keeps lifecycle evidence reviewable and prevents chat-only decisions. | Review log shows no material findings; M1-M4 are closed. |
| Catalog model and validator | `qcc_toolkit/templates/__init__.py`, `templates/ppt/catalog.yml` | Added official/source status, method names, implementation modes, Python assist status/reasons, required content, evidence levels, chart editability, source files, and stricter path/ownership validation. | Satisfies R10, R18-R21, EB1-EB4, O1-O5, and T1/T2/T10. | Catalog tests and `qcc_toolkit.templates validate` pass. |
| Pareto method kit | `docs/methods/pareto_chart.md`, `templates/ppt/sources/pareto-chart.md`, `templates/ppt/methods/pareto-chart-template.pptx` | Expanded Pareto into a complete PowerPoint-native chart kit with purpose, stage fit, edit instructions, realistic demo, blank copyable slide, interpretation, mistakes, checklist, source notes, and optional Python assist triggers. | Satisfies R1-R13, R23, R26-R29, T3-T5, T8, T10, and MP1. | M2 tests passed; MP1 package/text/layout review recorded. |
| Template-native method kits | `docs/methods/5w2h.md`, `docs/methods/5_whys.md`, `docs/methods/check_sheet.md`, `docs/methods/fishbone_diagram.md`, matching source notes and PPTX files | Expanded 5W2H, 5 Whys, Check Sheet, and Fishbone Diagram into complete worksheet/diagram kits without requiring Python. | Satisfies R1-R10, R22, R24-R25, R30-R32, R37-R39, EC1, T3, T5-T8, and MP2. | M3 tests passed; MP2 package/text review recorded. |
| PPTX builder | `tools/build_ppt_templates.py` | Added deterministic method-kit slide generation for Pareto and template-native decks. | Keeps binary PPTX assets reproducible and paired with reviewable source notes while avoiding full automated report-generation scope. | Builder passed in M2 and M3; generated PPTX package checks pass. |
| Template standards | `docs/template-standards/evidence-levels.md`, `docs/template-standards/incoming-templates.md`, `docs/template-standards/method-kit-review-checklist.md`, `templates/incoming/README.md` | Added evidence levels, incoming-template quarantine/review rules, and a reusable method-kit approval checklist. | Satisfies R30-R39, EB5-EB7, S1-S4, EC3-EC5, T8, T9, and T12. | M4 closeout tests and code review passed. |
| Tests | `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py`, `tests/test_method_guides.py`, `tests/test_template_assets.py`, `tests/test_method_kit_closeout.py` | Added contract, integration, scope, closeout, and failure-path tests for the method-kit system. | Proves the new catalog contract, required method-kit surfaces, source/official distinction, and evidence-level rules. | Full pytest passed: 76 tests. |

## Tests Added Or Changed

| Test ID | Test files | What it proves | Why this level fits |
|---|---|---|---|
| T1 | `tests/test_template_catalog.py` | Official first-slice kits are registered with method IDs, modes, assist status, paths, required content, and evidence levels. | Contract-level catalog proof is enough because the behavior is metadata discovery. |
| T2 | `tests/test_template_catalog_failures.py` | Missing paths, missing required metadata, duplicate ownership, missing chart editability, and incomplete Python-assisted metadata fail validation. | Integration-style fixture tests prove validator failure branches. |
| T3 | `tests/test_method_guides.py` | Markdown guides include required method-kit guidance. | Markdown is canonical method knowledge, so text-level contract checks are appropriate. |
| T4-T5 | `tests/test_template_assets.py` | Pareto source notes, PPTX package contents, editable chart data, demo labels, and blank/project surfaces exist. | PPTX package inspection is the practical automated proof available locally. |
| T6 | `tests/test_method_guides.py`, `tests/test_template_assets.py` | Worksheet and diagram kits satisfy the template-native method-kit contract. | Combines canonical Markdown checks with generated PPTX package checks. |
| T7 | `tests/test_template_assets.py`, `tests/test_scope_guards.py` | The slice does not claim unsupported automation, advanced methods, or authoritative manual high-risk chart evidence. | Scope guard tests are appropriate for non-goal preservation. |
| T8 | `tests/test_method_guides.py`, `tests/test_method_kit_closeout.py` | Evidence-level guidance exists and preserves PowerPoint convenience plus high-rigor evidence boundaries. | Documentation contract checks match the user-facing policy surface. |
| T9 | `tests/test_method_kit_closeout.py`, `tests/test_template_catalog*.py` | Incoming/source templates stay non-official until reviewed. | Combines documentation checks and catalog semantics. |
| T10 | `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py` | Python assist status and required Python-assisted artifacts are explicit. | Catalog validation owns assist discoverability. |
| T11 | `docs/changes/2026-07-08-improve-qcc-method-templates/manual-template-review.md` | PPTX readability/copyability/demo/source surfaces were manually inspected at package/text level. | No PowerPoint or LibreOffice renderer is available, so the manual proof records that limitation. |
| T12 | `tests/test_method_kit_closeout.py`, `tests/test_artifact_consistency.py`, `tests/test_acceptance.py` | Final official kit set is internally consistent across catalog, guides, source notes, templates, and standards. | Cross-artifact integration checks match the final closeout risk. |

## Validation Evidence Available Before Final Verify

Implementation and review recorded these checks:

| Stage | Commands or checks | Result |
|---|---|---|
| M1 | `.venv/bin/python -m pytest tests/test_template_catalog.py tests/test_template_catalog_failures.py` | 11 passed |
| M1 | `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | validated 5 entries |
| M1 | `.venv/bin/python -m ruff check qcc_toolkit tests` | passed |
| M1 | `.venv/bin/python -m mypy qcc_toolkit` | passed |
| M2 | `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` | 14 passed |
| M2 | `.venv/bin/python tools/build_ppt_templates.py` | passed |
| M2 | catalog validation, Ruff, mypy | passed |
| M2 | MP1 manual package/text/layout review | recorded; no renderer available |
| M3 | expected failing proof for missing template-native method-kit surfaces | failed before implementation as expected |
| M3 | `.venv/bin/python -m pytest tests/test_method_guides.py tests/test_template_assets.py tests/test_template_catalog.py` | 17 passed |
| M3 | `.venv/bin/python tools/build_ppt_templates.py` | passed |
| M3 | catalog validation, Ruff, mypy, `git diff --check` | passed |
| M3 | MP2 manual package/text review | recorded; no renderer available |
| M4 | expected failing proof for missing template-standard documents and incoming README | failed before implementation as expected |
| M4 | `.venv/bin/python -m pytest tests/test_method_kit_closeout.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_artifact_consistency.py tests/test_acceptance.py tests/test_scope_guards.py` | 20 passed |
| M4 | `.venv/bin/python -m pytest` | 76 passed |
| M4 | catalog validation, Ruff, mypy, `git diff --check` | passed |
| M4 | MP3 manual package/text review | recorded; no renderer available |
| M4 code review | reviewer reran targeted M4 tests, full pytest, catalog validation, Ruff, mypy, and `git diff --check` | passed |

Hosted CI status is not claimed.
Final `verify` has not run yet.

## Review Resolution Summary

No material findings were recorded.
There is no `review-resolution.md` for this change because all relevant review rounds were approved or clean-with-notes with no material findings.

Review records:

- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/proposal-review-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/architecture-review-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/plan-review-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/test-spec-review-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m1-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m2-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m3-r1.md`
- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/code-review-m4-r1.md`

## Alternatives Rejected

| Alternative | Why it was not used |
|---|---|
| Keep Python-first as the primary method-template workflow. | The accepted proposal found this added friction for common PowerPoint-native QCC methods. |
| Build template-only PowerPoint assets. | That would lose validation, reproducibility, and traceability for reviewed data-dependent conclusions. |
| Start with full automated PPTX generation. | The proposal and spec deferred this until method-kit content, placeholders, and evidence contracts stabilize. |
| Add web UI, dashboard, CAPA/EQMS, or desktop app scope. | These are explicit non-goals for this method-template improvement. |
| Add Control Chart, Process Capability, DOE, regression, or other advanced methods. | The first slice proves the method-kit structure before expanding into advanced statistical workflows. |
| Add real incoming user templates now. | M4 intentionally records the quarantine and privacy review policy before accepting source assets that may contain private data. |

## Scope Control

This change preserves the approved boundaries:

- Python is not required for every QCC method or chart.
- Simple qualitative methods stay template-native.
- Pareto remains PowerPoint-native with optional Python assist.
- Existing Pareto evidence package behavior is preserved.
- Full automated PPTX generation remains deferred.
- No web UI, dashboard, enterprise workflow, or advanced statistical method support is added.
- Incoming templates are source assets only until reviewed and migrated.
- Manual PowerPoint charts are not claimed as authoritative final evidence for high-risk or validation-heavy data-dependent conclusions.

## Risks And Follow-Ups

| Risk or gap | Current handling | Follow-up |
|---|---|---|
| Binary PPTX assets are hard to review in diffs. | Source notes, deterministic builder output, catalog metadata, package checks, and manual review notes are included. | Final verify should re-check generated assets and catalog consistency. |
| No PowerPoint or LibreOffice renderer is available in this environment. | Manual proof uses package/text/layout inspection and records the limitation. | A future environment with a renderer can add screenshot or visual regression proof. |
| Incoming templates may contain private data. | `templates/incoming/README.md` and incoming-template standards treat them as untrusted source assets. | Add an intake checklist or automated scanner when real incoming files are accepted. |
| Evidence policy may need organization-specific enforcement. | The first slice defines Level 1 through Level 4 expectations. | Later specs can define competition/audit enforcement and evidence-package requirements. |
| More QCC methods remain outside this slice. | The first kit set proves chart, worksheet, diagram, logic-chain, and data-collection patterns. | Add Control Chart and Process Capability only after method-kit standards are stable. |

## Readiness

All implementation milestones are closed by code review.
This explanation completes the explain-change stage and hands off to final `verify`.

The branch is not PR-body-ready from this artifact alone.
Final verification is recorded in `verify-report.md`; PR handoff remains pending.
