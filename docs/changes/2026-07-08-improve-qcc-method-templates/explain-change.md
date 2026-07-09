# Change Explanation: Improve QCC Method Templates

## Status

current-after-final-verify

## Summary

This change upgrades QCC method templates from shallow placeholder decks into PowerPoint-first, Python-assisted method kits.
The reviewed implementation keeps PowerPoint as the primary teaching, editing, copying, and presentation surface.
It keeps Markdown as the canonical method guidance surface.
It keeps Python as an optional assist layer for complex, repeated, validation-heavy, or presentation-readability cases.

The final reviewed slice includes M1 through M6:

- M1 catalog contract and validation.
- M2 complete Pareto method kit.
- M3 complete template-native kits for 5W2H, 5 Whys, Check Sheet, and Fishbone.
- M4 evidence-level, incoming-template, and closeout standards.
- M5 Pareto chart-quality upgrade.
- M6 Fishbone diagram-quality, Python SVG, overlap, obstruction, and four-layer architecture upgrades.

All implementation milestones are closed by code review.
Final verify is refreshed after M6 and records branch-ready evidence for PR handoff.

## Problem

The original QCC method templates were too simple to be useful.
They had identifiers, placeholders, demo labels, and basic chart/table surfaces, but they did not teach users how to apply, edit, interpret, review, or present the method confidently.

Follow-up feedback added two sharper problems.
First, charts are important and the Pareto template needed stronger chart decision, variant, and quality guidance.
Second, the Fishbone template and generated Fishbone image were unreadable when cause content became dense or overlapping.
The final Fishbone follow-up requested support for a four-layer architecture without making the diagram body crowded again.

## Decision Trail

| Source | Decision used |
|---|---|
| Accepted proposal | Adopt PowerPoint-first, Python-assisted QCC method kits. |
| Proposal review | Accept after amendments: vision revision, minimum kit content, evidence levels, and incoming-template process. |
| Vision | Preserve the split: PowerPoint teaches and presents; Markdown governs method knowledge; Python generates traceable QCC evidence. |
| Spec | `specs/qcc-method-kits.md` R1-R54 define method-kit content, catalog behavior, evidence levels, chart quality, Fishbone quality, and Python SVG behavior. |
| Test spec | `specs/qcc-method-kits.test.md` T1-T15 and MP1-MP4 define automated and manual proof. |
| Architecture | `docs/architecture/method-kits/architecture.md` keeps official kits, source/incoming templates, catalog validation, optional Python assist, and evidence guidance separate. |
| Plan | `docs/plans/2026-07-08-improve-qcc-method-templates.md` implements M1-M6. |
| Code reviews | M1-M6 all closed `clean-with-notes` with no material findings. |

## Diff Rationale By Area

| Area | Files | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|---|
| Vision and positioning | `VISION.md`, `README.md`, `docs/vision/strategic-positioning.md` | Reframed the project around PowerPoint-first, Python-assisted method kits. | The accepted proposal changed the primary user workflow for method-template work. | Proposal review and vision update. | Review log and `change.yaml`. |
| Catalog contract | `qcc_toolkit/templates/__init__.py`, `templates/ppt/catalog.yml` | Added stricter method/template metadata and validation for official/source status, implementation mode, required content, evidence levels, and Python assist. | Method kits need traceable registration across PowerPoint, Markdown, and optional Python assist. | R10, R18-R21, T1-T2. | Catalog tests and catalog validation passed. |
| Pareto method kit | `docs/methods/pareto_chart.md`, `templates/ppt/sources/pareto-chart.md`, `templates/ppt/methods/pareto-chart-template.pptx` | Expanded Pareto into a practical chart kit with edit instructions, demo, blank slide, interpretation, mistakes, checklist, source notes, and Python triggers. | Pareto is the first PowerPoint-native chart kit and needed to be usable without Python for simple category counts. | R1-R13, R23, R26-R29, T3-T5, MP1. | M2 code review clean. |
| Pareto chart quality | `tools/build_ppt_templates.py`, Pareto guide/source/PPTX, `docs/template-standards/chart-template-standard.md`, tests | Added chart decision guide, variant library, chart quality checklist, percent/cumulative percent guidance, and formula checks. | User feedback said charts are very important and templates remained too weak. | R41-R44, AC9, T13. | M5 code review clean. |
| Template-native method kits | 5W2H, 5 Whys, Check Sheet, and Fishbone guides/source/PPTX files | Added full method-kit surfaces for qualitative and worksheet/diagram methods. | These methods should remain PowerPoint-native rather than forcing Python. | R22, R24-R25, R30-R32, T6-T8, MP2. | M3 code review clean. |
| Fishbone method kit | `docs/methods/fishbone_diagram.md`, `templates/ppt/sources/fishbone-diagram.md`, `templates/ppt/methods/fishbone-diagram-template.pptx`, `tools/build_ppt_templates.py` | Added diagram-quality guidance, verification markers, cause wording guidance, clean editable diagram, cause verification plan, visual-design rules, and four-layer architecture. | Fishbone needed to become a practical cause-analysis working asset without overclaiming root-cause proof or becoming unreadable. | R45-R50, T14, MP4. | M6 code review clean; PPTX package inspection found 15 slides and four-layer terms. |
| Fishbone Python SVG assist | `qcc_toolkit/fishbone.py`, `examples/scripts/generate_fishbone.py`, generated SVG/README, tests | Added optional static SVG generation, fixed top/bottom lanes, explicit cause and branch-label boxes, connector metadata, connector-obstruction tests, four-layer metadata, and a Layer 4 footer panel. | The editable PPTX diagram and earlier generated SVG were reported unreadable/overlapping; Python assist needed a readable presentation asset. | R51-R54, T15. | M6 code review reran focused tests: 32 passed. |
| Evidence and intake standards | `docs/template-standards/evidence-levels.md`, `docs/template-standards/incoming-templates.md`, `docs/template-standards/method-kit-review-checklist.md`, `templates/incoming/README.md` | Added evidence-level guidance, incoming-template quarantine/review process, and reusable review checklist. | The proposal required preserving evidence rigor without accepting unreviewed user templates as official assets. | R30-R39, T8-T12. | M4 code review clean. |
| Lifecycle records | `docs/changes/2026-07-08-improve-qcc-method-templates/*`, `docs/plan.md`, active plan | Recorded proposal/spec/architecture/plan/test-spec reviews, code reviews, manual review evidence, current handoff state, and this explanation. | Durable workflow evidence prevents decisions and review outcomes from existing only in chat. | `CONSTITUTION.md`, `docs/workflows.md`. | M6 review log and plan state show M6 closed. |

## Tests Added Or Changed

| Test area | Files | What it proves | Why this level fits |
|---|---|---|---|
| Catalog contract and failures | `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py` | Official kits, required metadata, path ownership, Python assist metadata, and failure cases are enforced. | Catalog validation owns discoverability and compatibility. |
| Method guides | `tests/test_method_guides.py` | Markdown guides contain required method-kit and Fishbone four-layer guidance. | Markdown is the canonical method knowledge surface. |
| PPTX/source assets | `tests/test_template_assets.py` | Source notes and generated PPTX package XML expose required method-kit, chart-quality, and Fishbone-quality surfaces. | Package/text inspection is the available automated proof for PPTX assets. |
| Closeout standards | `tests/test_method_kit_closeout.py` | Evidence levels, incoming-template standards, chart template standard, and review checklist exist. | Standards are documentation contracts. |
| Fishbone SVG renderer | `tests/test_fishbone_generation.py` | SVG includes fixed lanes, visible cause limits, four-layer metadata, cause/branch-label boxes, and no connector crosses text boxes. | Geometry metadata makes the readability regression testable. |
| Fishbone script | `tests/test_generate_fishbone_script.py` | The starter script writes `fishbone.svg` and README guidance. | Script behavior is the user-facing Python assist path. |
| Scope guards | `tests/test_scope_guards.py` and related artifact checks | Out-of-scope dashboard, CAPA/EQMS, full PPTX automation, and advanced methods are not introduced. | Non-goal preservation is a compatibility and product-focus risk. |

## Validation Evidence Available Before Final Verify

| Stage | Commands or checks | Result |
|---|---|---|
| M1-M4 | Targeted milestone tests, catalog validation, Ruff, mypy, `git diff --check` | passed; M1-M4 code reviews clean |
| M4 broad check | `.venv/bin/python -m pytest` | 76 passed |
| M5 | Pareto chart-quality targeted tests, full pytest, catalog validation, Ruff, mypy, generator checks, `git diff --check` | passed; M5 code review clean |
| M6 implementation | Fishbone guide/source/PPTX tests, SVG renderer tests, script tests, catalog checks, generator runs | passed through each follow-up refinement |
| M6 code review | `PATH=.venv/bin:$PATH python -m pytest tests/test_fishbone_generation.py tests/test_generate_fishbone_script.py tests/test_template_assets.py tests/test_method_guides.py tests/test_template_catalog.py` | 32 passed |
| M6 code review | `PATH=.venv/bin:$PATH python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | validated 5 entries |
| M6 code review | `git diff --check` | passed |
| M6 manual/package inspection | `fishbone-diagram-template.pptx` package text | 15 slides; four-layer terms present |

Hosted CI is not claimed.
Final `verify` has run after M6 and records branch-ready local evidence.

## Review Resolution Summary

No material findings were recorded.
There is no `review-resolution.md` for this change because all review rounds were approved or clean-with-notes with no material findings.

Review records include proposal, spec, architecture, plan, test-spec, and code reviews M1 through M6 under `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/`.
The latest review is `code-review-m6-r2.md`.

## Alternatives Rejected

| Alternative | Why it was not used |
|---|---|
| Keep Python-first as the primary method-template workflow. | The accepted proposal found this added friction for common PowerPoint-native QCC methods. |
| Build template-only PowerPoint assets. | That would lose validation, reproducibility, and traceability for reviewed data-dependent conclusions. |
| Put Fishbone Layer 4 details inside the diagram body. | That would recreate the unreadable/obscured content problem. Layer 4 belongs in the verification plan or evidence/source fields. |
| Make Python the only Fishbone workflow. | Fishbone remains template-native; Python SVG is optional presentation assist when readability is poor. |
| Start full automated PPTX generation. | The proposal and spec defer this until method-kit content and placeholders stabilize. |
| Add web UI, dashboard, CAPA/EQMS, or advanced statistical methods. | These are explicit non-goals for this slice. |
| Accept real incoming user templates as official assets immediately. | Incoming templates may contain private or weak content; they must remain source assets until reviewed. |

## Scope Control

This change preserves the approved boundaries:

- PowerPoint remains the default workflow for simple method templates.
- Markdown remains the canonical written guide.
- Python remains optional assist, not a mandatory path for every method.
- Pareto remains PowerPoint-native with optional Python assist triggers.
- Fishbone remains template-native, with optional Python SVG for static readable presentation output.
- Layer 4 Fishbone verification detail is supported without crowding the diagram body.
- Full automated PPTX generation, web UI, dashboards, CAPA/EQMS, and advanced statistical methods remain out of scope.
- Incoming templates remain untrusted source assets until reviewed.

## Risks And Follow-Ups

| Risk or gap | Current handling | Follow-up |
|---|---|---|
| No PowerPoint, LibreOffice, or SVG raster renderer is available. | Tests use deterministic generation, PPTX package/text inspection, and SVG geometry metadata. | Final verify should repeat available checks; future environments can add screenshot proof. |
| Binary PPTX review remains difficult. | Source notes, deterministic builder, package checks, and review records explain generated content. | Consider visual regression proof when a renderer is available. |
| Fishbone PPTX is larger after adding four-layer guidance. | M6 review notes this as a residual risk, not a blocker. | User testing should confirm the extra slide improves training and project use. |
| Evidence policy may need organization-specific enforcement. | Level 1-Level 4 guidance is documented. | Later specs can define competition/audit enforcement. |
| More QCC methods remain outside this slice. | The first method set proves chart, worksheet, diagram, logic-chain, and data-collection patterns. | Add Control Chart and Process Capability only after template standards stabilize. |

## Readiness

All implementation milestones M1 through M6 are closed by code review.
This explanation refreshes the explain-change artifact after M6.
Final verify records branch-ready local evidence.

Next stage is PR handoff.
