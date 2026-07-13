# QCC Method Selection Summary Change Rationale

## Summary

This change adds one canonical QCC method-selection summary at `method-kits/README.md`.
The selector helps users choose a method by combining QCC stage, immediate project question, and available evidence or input.

The root `README.md` and `docs/qcc-project-story.md` now link to that selector instead of maintaining a detailed duplicate stage-method matrix.
Focused documentation tests and manual scenario review prove the selector structure, link behavior, interpretation guardrails, and representative method-selection scenarios.

## Problem

The method library had several detailed method guides, but users had to know which guide to open.
A flat method list did not explain method fit.
A stage-only matrix risked implying that each method belonged to only one rigid stage.

The accepted problem statement required a concise selector that supports two entry paths:

- start from the current QCC stage;
- start from the immediate project question.

The selector also needed to show the evidence or input needed before selecting a method and the safe interpretation boundary for each method.

## Decision Trail

| Source | Decision or requirement | How this change follows it |
|---|---|---|
| Proposal | Create one canonical selector under `method-kits/README.md`. | Added `method-kits/README.md` as the detailed selector and linked other navigation surfaces to it. |
| Proposal | Combine stage, project question, and available evidence or input. | The selector introduction states those three inputs and both selector tables include question, stage, evidence/input, output, and limitation context. |
| Spec R1-R5 | Add selector, question view, and stage-oriented view using canonical QCC stage labels. | `method-kits/README.md` includes `Quick selection by project question` and `Selection by QCC stage`. |
| Spec R6-R7 | Distinguish primary use from supporting use and avoid one-stage-only method claims. | The stage table has `Primary use` and `Supporting use` columns. |
| Spec R8-R10 | Show expected evidence/input, typical outputs, and interpretation limits. | The question table includes `Evidence or input needed`; the stage table includes `Typical output` and `Important limitation`; guardrails are repeated in a dedicated table. |
| Spec R11-R13 | Link only existing method guides and classify future or advanced guidance as status text. | Available methods link to existing files; Control Chart/SPC/process capability and sustainment guidance are unlinked status rows. |
| Spec R14 | Document maintenance behavior. | The selector maintenance note requires updates for method additions, renames, removals, status changes, and stage-fit changes. |
| Spec R15-R16 | Root README and QCC project-story guide link to the selector instead of duplicating the new detailed matrix. | `README.md` and `docs/qcc-project-story.md` now link to the selector; the root table is stage-neutral. |
| Spec R17-R18 | Avoid full procedures, formulas, worked examples, generated catalogs, wizards, and automation behavior. | The selector stays as Markdown navigation and leaves full method instructions in detailed guides. |
| Architecture assessment | No runtime architecture required. | The change is documentation and tests only. |
| Plan M1 | Implement one documentation slice with focused proof. | M1 added selector, navigation, automated checks, and manual scenario proof. |

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test or evidence |
|---|---|---|---|---|
| `method-kits/README.md` | Added the canonical selector with question view, stage view, method status, guardrails, detailed links, and maintenance note. | Gives users one concise selection surface without duplicating full method procedures. | Spec R1-R14, R17-R18; plan M1. | `test_method_selection_summary_selection_model_and_question_view`, `test_method_selection_summary_stage_view_status_and_guardrails`, `test_method_selection_navigation_maintenance_and_scope_guards`. |
| `README.md` | Linked to the selector and changed the method-kit table from stage-mapped navigation to stage-neutral navigation. | Keeps root navigation discoverable while avoiding a second detailed stage-method matrix. | Spec R15; plan decision to keep root stage-neutral. | Navigation and scope assertions in `test_method_selection_navigation_maintenance_and_scope_guards`. |
| `docs/qcc-project-story.md` | Added a selector link in the opening guidance and method links section. | Lets users move from project-story context to method selection without replacing the high-level story map. | Spec R16. | Existing QCC project-story tests plus selector navigation assertions. |
| `tests/test_markdown_first_method_guidance.py` | Added focused selector tests and constants for available method links and manual scenario evidence. | Provides deterministic proof for selector structure, link safety, guardrails, future guidance status, maintenance behavior, and scope exclusions. | Test spec T1-T8. | Focused pytest command selects 5 tests and passes. |
| `docs/changes/2026-07-13-qcc-method-selection-summary/manual-scenario-review.md` | Added MP1-MP4 scenario review. | Records bounded human judgment for representative method-fit cases that are clearer than brittle text matching alone. | Test spec MP1-MP4. | Manual scenario proof is read by automated navigation/scope test. |
| `docs/proposals/2026-07-13-qcc-method-selection-summary.md` | Recorded the accepted proposal and lifecycle/refinement history. | Preserves the product decision, tradeoffs, goals, non-goals, and rollout reasoning for the selector. | Proposal workflow. | Proposal-review records R1-R3. |
| `specs/qcc-method-selection-summary.md` | Added the approved behavior contract for the selector. | Defines observable requirements, content relationships, status behavior, invariants, and acceptance criteria. | Spec workflow. | Spec-review R1 approved with no material findings. |
| `specs/qcc-method-selection-summary.test.md` | Added the proof map and validation commands. | Maps requirements, examples, edge cases, and manual proof to concrete tests and validation. | Test-spec workflow. | Test-spec-review R2 approved after TSR-MS-001 resolution. |
| `docs/plans/2026-07-13-qcc-method-selection-summary.md` | Added and maintained the execution plan, validation notes, review state, and final-closeout handoff. | Tracks milestone state and prevents implementation, review, and final-closeout stages from blurring together. | Plan workflow. | Plan-review R1, code-review M1 R1, final holistic code-review R1. |
| `docs/changes/2026-07-13-qcc-method-selection-summary/*` | Added change metadata, architecture assessment, review records, review log, review resolution, and this rationale. | Preserves durable lifecycle evidence for proposal, spec, test-spec, implementation, review, and final closeout. | Workflow and stage skills. | Review log records no open findings. |
| `docs/plan.md` | Updated the plan index as the change moved through implementation, review, and final closeout. | Keeps repository-level lifecycle bookkeeping current. | Workflow planned-initiative rules. | Current plan points to `explain-change`. |

## Tests Added Or Changed

| Test or proof | What it proves | Why this level is appropriate |
|---|---|---|
| `test_method_selection_summary_selection_model_and_question_view` | The selector exists, states the stage-question-evidence model, and covers the required project-question rows with method, input, and boundary text. | Text-level documentation behavior is deterministic and can be checked directly. |
| `test_method_selection_summary_stage_view_status_and_guardrails` | The stage view uses canonical stages, primary/supporting language, available method links, unlinked future guidance, and interpretation boundaries. | Direct file inspection is enough because the change is Markdown-only. |
| `test_method_selection_navigation_maintenance_and_scope_guards` | Root and project-story navigation point to the selector, maintenance rules exist, scope exclusions are preserved, and manual scenario evidence exists. | This catches duplicate-matrix drift and scope creep without requiring runtime tests. |
| Manual proof MP1-MP4 | Representative users can map observation collection, defect prioritization, paired-variable exploration, and sustainment guidance to defensible methods and limits. | Scenario judgment combines method fit and interpretation safety, which is clearer as bounded manual proof. |

## Validation Evidence Available Before Final Verify

Implementation-stage evidence:

```sh
.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -k 'method_selection or qcc_project_story or navigation or method_links'
```

Result: failed before production docs with 3 failures for missing `method-kits/README.md`, then passed after implementation with 5 selected tests.

```sh
.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py
```

Result: passed with 34 tests after implementation.

```sh
git diff --check
```

Result: passed after implementation.

Review-side evidence:

- Code-review M1 R1 reran focused selector/navigation tests, broader documentation tests, and patch hygiene successfully.
- Final holistic code-review R1 reran focused selector/navigation tests, broader documentation tests, and branch-range patch hygiene successfully.

Hosted CI status: not observed.
Final verify status: not claimed by this artifact.

## Review Resolution Summary

Two upstream review findings were opened and resolved before implementation:

| Finding | Source review | Disposition |
|---|---|---|
| PR-MS-001 | Proposal-review R2 | Closed after lifecycle/readiness/follow-on text was updated. |
| TSR-MS-001 | Test-spec-review R1 | Closed after MP1-MP4 manual proof procedures were expanded. |

No material findings were opened by code-review M1 R1 or final holistic code-review R1.

## Alternatives Rejected

| Alternative | Why it was not used |
|---|---|
| Keep only a flat method index | It would not help users choose a method safely. |
| Keep a detailed stage-method matrix in the root README | It would duplicate the selector and create drift risk. |
| Replace the QCC project-story map with the selector | The project-story guide still serves a different high-level narrative purpose. |
| Link planned or advanced methods before guides exist | That would create dead links and imply unsupported guidance is available. |
| Add a generated catalog, metadata registry, wizard, or recommendation algorithm | The accepted scope is Markdown-first documentation, not automation. |
| Add Control Chart, SPC, process capability, Standard Work, Visual Control, or Monitoring Plan procedures | Those remain deferred, advanced, or future sustainment guidance outside this slice. |

## Scope Control

The change does not add or rewrite detailed method guides.
It does not add new QCC methods.
It does not define a new QCC stage model.
It does not add Python APIs, chart-generation behavior, generated catalogs, runtime registries, web UI, PowerPoint behavior, external services, or tool-specific workflow.

Detailed procedures, formulas, chart recipes, worked examples, and review checks remain in the detailed method guides.

## Risks And Follow-Ups

No follow-up is required before final verify.

The main residual risk is maintenance drift.
Future changes that add, rename, remove, reclassify, or change the status of a method must update `method-kits/README.md` in the same change.

Final verification still needs to run after this explanation.
PR readiness is not claimed here.
