# Explain Change: Markdown-First Method Guides

## Summary

This change moves QCC Toolkit from a generated-template-centered direction to a Markdown-first method-guidance system.
The implementation adds shared method-kit standards, creates the first complete Pareto Chart method kit, and labels older PowerPoint and Python assets as optional execution aids.

The practical product rule behind the diff is:

```text
Markdown governs method knowledge and chart quality.
Image prompts and teaching visuals explain concepts.
Manual chart guidance teaches users how to create evidence charts.
PowerPoint templates and Python automation remain optional aids.
```

The change is reviewed through M1, M2, and M3.
All implementation milestones are closed by code review.
Final verify and PR handoff are still downstream stages and are not claimed here.

## Problem

The accepted proposal records that generated chart images and generated presentation templates did not meet the required quality bar for QCC method work.
Users still need clear guidance for applying methods, creating high-quality charts manually, preserving evidence support, and reviewing outputs.

The prior repository already had useful Python and PowerPoint assets.
The problem was that those assets could still appear to define the product identity.
The accepted direction instead requires official Markdown method kits and chart-quality guidance to be primary.

## Decision Trail

| Decision point | Outcome | Source |
|---|---|---|
| Product direction | Adopt Markdown-first, image-assisted, tool-neutral method guidance. | `docs/proposals/2026-07-09-markdown-first-method-guides.md` |
| Proposal status | Accepted; not itself a spec or implementation plan. | `docs/proposals/2026-07-09-markdown-first-method-guides.md` |
| Requirements | Implement method-kit structure, chart recipes, image prompt boundaries, evidence notes, Pareto kit, tool-neutrality, and optional-aid compatibility. | `specs/markdown-first-method-guidance.md` R1-R28 |
| Architecture | Use `method-kits/<method-id>/` as the official per-method boundary and preserve `templates/ppt/` and `qcc_toolkit/` as optional aids. | `docs/architecture/markdown-method-guidance/architecture.md` |
| Plan | Split delivery into M1 shared templates, M2 Pareto kit, and M3 compatibility alignment. | `docs/plans/2026-07-09-markdown-first-method-guidance.md` |
| Reviews | M1 and M2 closed cleanly; M3 needed one fix and then closed on re-review. | `docs/changes/2026-07-09-markdown-first-method-guides/review-log.md` |

No new ADR was required because the architecture applies the accepted Markdown-first direction without changing the existing local-first Python stack or evidence-package ADRs.

## Diff Rationale By Area

| Area / files | Change | Reason | Source artifact | Test or evidence |
|---|---|---|---|---|
| Governance and vision: `CONSTITUTION.md`, `AGENTS.md`, `VISION.md`, `README.md`, `docs/vision/strategic-positioning.md` | Repositioned the project as Markdown-first, image-assisted, tool-neutral, and manual-chart-guidance-centered. | The accepted proposal superseded earlier Python/generated-template and PowerPoint-first directions. | Proposal goals and vision revision; constitution source-of-truth rules. | Proposal/spec/review records; README marker inspection through artifact tests. |
| Proposal/spec/lifecycle artifacts | Added the accepted proposal, feature spec, test spec, architecture package, plan, reviews, review-resolution, and change metadata. | This was a substantive workflow-managed change requiring durable decision, requirement, design, plan, proof, and review records. | `docs/workflows.md`; `CONSTITUTION.md`; `specs/markdown-first-method-guidance.md`. | Proposal/spec/architecture/plan/test-spec/code reviews recorded under the change pack. |
| M1 shared templates: `method-kits/_template/`, `docs/chart-creation/`, `docs/evidence/`, `docs/tool-guidance/` | Added standard method-guide, chart-creation, review-checklist, image-prompt, chart-quality, evidence-level, evidence-note, and tool-selection guidance. | Official method kits need reusable structure before individual kits can be created consistently. | Spec R1-R21, R23-R24, R26-R27; plan M1. | `tests/test_markdown_first_method_guidance.py`; M1 code review. |
| M2 Pareto method kit: `method-kits/pareto-chart/` | Added README, method guide, chart-creation guide, interpretation guide, review checklist, evidence note, synthetic sample data, worked example, reviewed good/bad examples, image prompts, and teaching-visual location. | Pareto Chart is the first complete proof that the Markdown-first kit model can teach method use, manual chart creation, interpretation, and review. | Spec R5-R10, R16-R22, R26-R27; plan M2. | Pareto kit tests in `tests/test_markdown_first_method_guidance.py`; M2 code review. |
| M3 compatibility: `README.md`, `docs/project-map.md`, `templates/ppt/catalog.yml`, `docs/methods/*.md` | Labeled older method guides, PowerPoint templates, and catalog entries as optional or historical aids under the Markdown-first direction. | Existing useful assets should remain available but must not override method-kit guidance. | Spec R25, R28; test spec T12; architecture optional-aid boundaries. | `tests/test_artifact_consistency.py`; M3 reviews. |
| Generated evidence/report wording: `qcc_toolkit/evidence.py`, `qcc_toolkit/reports.py` | Updated generated README and report text so generated outputs are optional aids alongside method kits and authoritative only for the optional generated path. | Python automation remains useful, but generated outputs must not appear to be the primary product surface. | Spec R25, R28; architecture `qcc_toolkit/` optional aid boundary. | `tests/test_first_slice_integration.py`; `tests/test_reports.py`; CR-M3-R1-F1 resolution. |
| Test updates | Added or extended structure, kit, compatibility, generated-report, and integration assertions. | The new behavior is documentation-heavy, so proof needs to check required files, sections, prompt constraints, evidence fields, optional-aid labels, and generated report wording. | Test spec T1-T12 and command map CMD1-CMD4. | Focused pytest runs and full local pytest recorded in the plan. |
| Review records and plan state | Recorded M1, M2, M3 R1, M3 R2, review-resolution, and current handoff state. | The workflow requires formal review receipts and milestone-aware state before final closeout. | `docs/workflows.md`; code-review skill rules. | `review-log.md`; `review-resolution.md`; active plan handoff. |

## Tests Added Or Changed

| Test file | What changed | What it proves | Requirement or test-spec link |
|---|---|---|---|
| `tests/test_markdown_first_method_guidance.py` | Added checks for method-kit templates, chart-quality standards, evidence levels, evidence notes, prompt constraints, tool-neutral guidance, and the Pareto kit. | Official templates and the first Pareto kit include required sections, files, evidence fields, prompt boundaries, and synthetic data. | R1-R24, R26-R27; T1-T11. |
| `tests/test_artifact_consistency.py` | Added checks that README/project map/catalog/legacy guides label method kits as primary and older assets as optional aids. | Existing Python and PowerPoint surfaces are preserved but not promoted above method kits. | R25, R28; T12. |
| `tests/test_first_slice_integration.py` | Updated generated project report assertion from PowerPoint-template language to optional-aid method-kit language. | The integration output reflects current Markdown-first positioning. | R25, R28; T12. |
| `tests/test_reports.py` | Added direct output coverage for `build_pareto_markdown_report()`. | Generated Pareto evidence-package reports include optional-aid and method-kit boundary wording. | CR-M3-R1-F1; R25, R28; T12. |

The test level is intentionally mixed.
Structure and wording contracts use repository inspection because the product surface is Markdown documentation.
Generated report behavior uses direct function and integration tests because report text is produced by Python code.

## Validation Evidence Available Before Final Verify

The following local evidence is recorded in the plan and review records before final verify:

| Stage | Command or proof | Result |
|---|---|---|
| M1 handoff | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py` | 16 passed |
| M1 handoff | `git diff --check` | passed |
| M2 handoff | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_method_guides.py tests/test_method_kit_closeout.py` | 20 passed |
| M2 handoff | `git diff --check` | passed |
| M3 handoff | `.venv/bin/python -m pytest tests/test_artifact_consistency.py` | 3 passed |
| M3 handoff | `.venv/bin/python -m pytest` | 102 passed |
| M3 handoff | `.venv/bin/python -m ruff check .` | passed |
| M3 handoff | `.venv/bin/python -m mypy qcc_toolkit` | no issues in 13 source files |
| M3 handoff | `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | validated 5 entries |
| M3 resolution | `.venv/bin/python -m pytest tests/test_reports.py -q` | 2 passed |
| M3 resolution | `.venv/bin/python -m pytest tests/test_artifact_consistency.py tests/test_first_slice_integration.py -q` | 4 passed |
| M3 resolution | `.venv/bin/python -m pytest` | 103 passed |
| M3 resolution | `.venv/bin/python -m ruff check .` | passed |
| M3 resolution | `.venv/bin/python -m mypy qcc_toolkit` | no issues in 13 source files |
| M3 re-review | `.venv/bin/python -m pytest tests/test_reports.py tests/test_artifact_consistency.py tests/test_first_slice_integration.py -q` | 6 passed |
| M3 re-review | `git diff --check` | passed |

Hosted CI was not observed.
Final verify has not run for this change.

## Review Resolution Summary

One material code-review finding was recorded:

| Finding | Disposition | Summary |
|---|---|---|
| CR-M3-R1-F1 | resolved | `build_pareto_markdown_report()` still emitted generated evidence report text without the optional-aid and method-kit boundary. The helper was updated and direct generated-report output coverage was added. |

The detailed disposition is in `docs/changes/2026-07-09-markdown-first-method-guides/review-resolution.md`.
Code Review M3 R2 closed M3 with no material findings.

## Alternatives Rejected

| Alternative | Why rejected | Source |
|---|---|---|
| Continue generated chart/template direction | Prior attempts did not meet the quality bar and risked low-value output. | Accepted proposal options O1/O3. |
| Make PowerPoint templates the primary product | The accepted direction makes specific tools optional execution choices rather than identity. | Proposal goals/non-goals; spec R25/R28. |
| Delete older Python and PowerPoint assets during this change | Existing assets remain useful and the spec says to preserve them as optional or historical aids unless a later plan migrates them. | Spec R28; plan M3 decision log. |
| Add named-tool tutorials in the first slice | The first slice must stay tool-neutral unless user testing proves a named tool is necessary. | Spec R23/R24; test spec T11. |
| Add generated binary teaching visuals in M2 | M2 could prove the review structure with Markdown good/bad teaching notes; binary visuals require manual visual review evidence. | Plan M2 decision log and MAN1 note. |
| Build a full automation platform or dashboard | Out of scope for the accepted Markdown-first method-guidance direction. | Proposal non-goals; spec non-goals. |

## Scope Control

The change preserves these non-goals:

- It does not generate final quantitative evidence charts through image generation.
- It does not remove existing Python or PowerPoint assets.
- It does not create named-tool tutorials.
- It does not build a web app, dashboard, slide-deck generator, or enterprise quality workflow.
- It does not add new dependencies, network calls, telemetry, or image-generation service integration.
- It does not implement advanced statistical automation.

## Risks And Follow-Ups

| Risk or follow-up | Status |
|---|---|
| Method guides could become too theoretical without user testing. | Still a product risk; first real user/reviewer task tests should follow method-kit creation. |
| Binary teaching visuals are not yet included. | Intentional. Future binary visuals need manual conceptual-only visual review evidence. |
| Older first-slice specs still describe already-built Python/PPT behavior. | The project map records this; future specs should align new work with the Markdown-first direction. |
| No hosted CI exists. | Final verify cannot claim hosted CI. |
| Plan remains active until final closeout completes. | Explain-change is now recorded; verify and PR handoff remain. |

## Current Handoff

The active plan says no implementation milestones remain.
M1, M2, and M3 are closed by code review.

This explain-change artifact completes the rationale stage.
The next lifecycle stage is `verify`.
