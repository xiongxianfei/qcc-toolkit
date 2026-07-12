# Explain Change: Expand Core QCC Method Kits

## Summary

This change promotes Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H into canonical Markdown-first method kits.
It also finishes the migration away from the deleted `docs/methods/` guide surface by updating active navigation, catalog references, tests, and present-tense documentation to point at `method-kits/`.

The implementation keeps the approved product direction:
Markdown method guidance remains canonical, PowerPoint and Python assets remain optional execution aids, generated visuals remain conceptual teaching aids, and the change does not add Control Chart, SPC, process capability, or broad automation.

## Problem

The repository already had official method kits for Pareto Chart, Flowchart / Process Map, Histogram, and Scatter Diagram.
Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H remained on the older `docs/methods/` surface.

The team chose deletion rather than compatibility notices for old method pages.
That made two things necessary:

- promote the four selected methods into canonical `method-kits/` guides;
- remove live dependencies on deleted `docs/methods/*.md` files while preserving extracted source material in `docs/methods-key-content.md`.

## Decision Trail

| Decision point | Outcome | Durable source |
|---|---|---|
| Proposal decision | Promote Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H; defer sustainment methods and statistical-control methods. | `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md` |
| Proposal review R1 | Required resolving the conflict between compatibility notices and actual deletion. | `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/proposal-review-r1.md` |
| Review resolution | Accepted deletion, preserved extracted content, and required downstream cleanup of live references. | `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-resolution.md` |
| Proposal review R2 | Approved the revised direction. | `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/proposal-review-r2.md` |
| Feature spec | Defined R1-R22, including method-kit requirements, deleted-reference cleanup, catalog behavior, and non-goals. | `specs/expand-core-qcc-method-kits.md` |
| Architecture assessment | Recorded that no separate architecture change was required because the durable boundaries remained Markdown guides, catalog references, and focused checks. | `docs/changes/2026-07-10-expand-core-qcc-method-kits/architecture-assessment.md` |
| Execution plan | Split implementation into M1 Check Sheet, M2 Fishbone plus 5 Whys, M3 5W2H, and M4 navigation/catalog/deleted-reference cleanup. | `docs/plans/2026-07-10-expand-core-qcc-method-kits.md` |
| Test spec | Mapped requirements to focused Markdown, artifact-consistency, catalog, scope-guard, and manual-review proof. | `specs/expand-core-qcc-method-kits.test.md` |
| Code reviews | M1, M2, M3, and M4 all closed cleanly with no material findings. | `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-log.md` |

## Requirement Map

| Requirement | Implementation summary |
|---|---|
| R1-R4 | Added four canonical method kits with reviewable metadata, required sections, and QCC project-story connections. |
| R5-R6 | Check Sheet distinguishes observation sheets from task checklists and limits output to structured observation data. |
| R7-R8 | Fishbone Diagram separates facts from hypotheses, records evidence status, and avoids verified-root-cause claims. |
| R9-R10 | 5 Whys allows branching, avoids exact-five and blame traps, and treats chains as provisional hypotheses. |
| R11-R13 | 5W2H supports problem-framing and action-planning modes without replacing root-cause analysis or proving action effectiveness. |
| R14-R16 | README, project-story links, project-map text, and catalog entries now use canonical method-kit paths instead of deleted guide paths. |
| R17-R18 | `docs/methods-key-content.md` remains the extracted source check used by the new guides. |
| R19-R20 | Generated visuals remain optional, conceptual-only, reviewed, text-light, and stored with prompt records. |
| R21 | Scope guards confirm no Control Chart, SPC, process capability, broad automation, or named-tool tutorial was introduced. |
| R22 | Focused checks cover required sections, method-specific safeguards, navigation, deleted-reference cleanup, canonical catalog behavior, and out-of-scope guardrails. |

## Diff Rationale By Area

| File or area | Change | Reason | Source artifact | Test or evidence |
|---|---|---|---|---|
| `method-kits/check-sheet.md` | Added the official Check Sheet method kit. | Establishes canonical guidance for structured observation data, definitions, scope, categories, blank/unknown/other rules, pilot collection, and handoff to later analysis. | R1-R6, R17-R19, R21; M1. | T1-T5, T12, T14; MP1, MP5; M1 code-review R1. |
| `method-kits/fishbone-diagram.md` | Added the official Fishbone Diagram method kit. | Provides canonical cause-hypothesis guidance with one effect statement, context categories, fact/hypothesis separation, evidence status, and verification handoff. | R1-R4, R7-R8, R17-R21; M2. | T1-T4, T6, T12-T14; MP2, MP5, MP6; M2 code-review R1. |
| `method-kits/five-whys.md` | Added the official 5 Whys method kit. | Provides canonical causal-chain guidance that avoids exact-five, single-chain, blame, and proof-by-repetition misuse. | R1-R4, R9-R10, R17-R21; M2. | T1-T4, T7, T12-T14; MP3, MP5, MP6; M2 code-review R1. |
| `method-kits/five-w-two-h.md` | Added the official 5W2H method kit. | Provides canonical problem-framing and action-planning guidance with owners, due dates, dependencies, verification measures, expected evidence, targets, assumptions, and constraints. | R1-R4, R11-R13, R17-R19, R21; M3. | T1-T4, T8, T12, T14; MP4, MP5; M3 code-review R1. |
| `README.md` | Changed the current guide surface from Pareto-only language to the `method-kits/` root and added the four new method-kit rows. | Makes official guides discoverable and avoids treating Pareto as the only canonical guide. | R14, AC7. | T9; M4 code-review R1. |
| `docs/qcc-project-story.md` | Updated method links for Check Sheet, Fishbone Diagram, 5 Whys, and 5W2H to canonical `method-kits/` paths. | Removes live navigation dependencies on deleted guide files. | R14-R15, AC7-AC8. | T9-T10; M4 code-review R1. |
| `docs/project-map.md` | Replaced present-tense `docs/methods/` guide-surface claims with `method-kits/` and `docs/methods-key-content.md` source-material language. | Keeps current-state documentation aligned with the deleted-path decision. | R15, EC1, AC8. | T10; reviewer reference scan in M4 code-review R1. |
| `templates/ppt/catalog.yml` | Marked official entries as available method kits and pointed `markdown_guide` and `method_kit` at canonical method-kit files. | Prevents the active template catalog from referencing deleted `docs/methods/*.md` files. | R16, EC2, AC8. | T11; catalog validator; M4 code-review R1. |
| `qcc_toolkit/templates/__init__.py` | Added optional `method_kit_status` and `method_kit` fields, validated available method-kit paths, required available method kits to match active guide paths, and supported inline or metadata-sidecar method IDs. | Catalog validation had to keep working after official entries moved from legacy front-matter guides to canonical method kits. Pareto uses a metadata sidecar; the new kits use inline `Method ID:` text. | R16, EC2. | `tests/test_template_catalog.py`, `tests/test_template_catalog_failures.py`, catalog validator, M4 reviewer probe. |
| `tests/test_markdown_first_method_guidance.py` | Added focused method-kit checks across M1-M3. | Proves required sections, method-specific safeguards, extracted-content use, visual policy, and scope guardrails. | T1-T8, T12-T14. | Focused pytest results recorded in plan and `change.yaml`. |
| `tests/test_artifact_consistency.py` | Added deleted-guide absence, live-reference, and canonical-catalog assertions. | Proves active surfaces do not rely on deleted guide paths and official catalog entries point to canonical kits. | T9-T11, R15-R16. | M4 focused pytest and reviewer rerun. |
| `tests/test_method_guides.py` | Converted legacy `docs/methods/` guide checks into registry-to-canonical-kit checks. | The old guide directory is intentionally empty, so tests now enforce canonical method-kit existence instead of legacy guide contracts. | R15, NG4, AC8. | M4 focused pytest. |
| `tests/test_template_catalog.py` | Required official catalog entries to use `method-kits/*.md`, match `method_kit`, and declare available status. | Locks the active catalog to canonical method-kit paths. | R16, T11. | M4 focused pytest. |
| `tests/test_template_catalog_failures.py` | Updated fixtures to use canonical method-kit paths while preserving mismatch and duplicate failure coverage. | Keeps negative catalog tests meaningful after legacy paths were deleted. | R16, EC2. | M4 focused pytest and reviewer mismatch probe. |
| `tests/test_method_kit_closeout.py` | Allowed method IDs to be present inline or through metadata links while requiring canonical guide paths. | Matches the repository's two canonical method-kit metadata styles. | R16, T11. | M4 focused pytest. |
| `docs/media/check-sheet/`, `docs/media/fishbone-diagram/`, `docs/media/five-whys/`, `docs/media/five-w-two-h/` | Added one reviewed conceptual teaching visual for each new method kit. | Provides high-quality visual demonstrations while keeping images conceptual and non-evidence. | R19-R20, T13, MP6. | Prompt/media link tests and manual image review notes. |
| `docs/media/prompts/check-sheet/`, `docs/media/prompts/fishbone-diagram/`, `docs/media/prompts/five-whys/`, `docs/media/prompts/five-w-two-h/` | Added per-image prompt records with purpose, output path, negative constraints, conceptual-only policy, and manual review status. | Preserves image-generation traceability and prevents generated visuals from being treated as project evidence. | R19-R20, T13, MP6. | Prompt/media link tests. |
| Workflow artifacts | Updated plan, plan index, change metadata, review log, review records, and this explanation. | Keeps durable workflow state aligned with closed milestones and final closeout handoff. | Workflow rules; plan closeout rules. | Code-review records M1-M4; `git diff --check`. |

## Tests Added Or Changed

| Test or proof | What it proves | Requirement coverage | Why this level is appropriate |
|---|---|---|---|
| T1-T4 in `tests/test_markdown_first_method_guidance.py` | Canonical files, reviewable metadata, required sections, and QCC project-story connections exist as method kits are introduced. | R1-R4. | Markdown guidance can be checked deterministically with focused repository tests. |
| T5 | Check Sheet has observation discipline and output-boundary safeguards. | R5-R6, E1, EC5. | Method misuse risk is content-specific and suited to contract checks plus manual review. |
| T6 | Fishbone has effect-statement, fact/hypothesis, evidence-status, and non-proof safeguards. | R7-R8, E2. | Cause-analysis overclaiming is a content safety risk. |
| T7 | 5 Whys avoids exact-five, single-chain, blame, and proof-by-repetition misuse. | R9-R10, E3, EC4. | Causal-chain misuse is a content safety risk. |
| T8 | 5W2H supports two modes and action-planning fields while preserving output limits. | R11-R13, E4. | Problem/action confusion is a content safety risk. |
| T9-T10 in `tests/test_artifact_consistency.py` | README, project-story, catalog, tests, and present-tense docs do not depend on deleted guide paths. | R14-R15, E5, EC1. | Repository-wide active-reference checks are more reliable than manual link inspection alone. |
| T11 in catalog tests and validator | Official catalog entries point at existing canonical method kits and mismatches still fail. | R16, EC2. | Catalog behavior includes code validation, so executable checks are appropriate. |
| T12 and MP5 | Extracted legacy content remains available and was used as source material. | R17-R18. | Content preservation needs both deterministic checks and reviewer-readable evidence. |
| T13 and MP6 | Reviewed images are conceptual-only, linked from method guides, and paired with prompt records. | R19-R20. | Visual policy is a documentation and review concern; generated images need traceability and manual review notes. |
| T14 | Out-of-scope terms and features were not introduced. | R21. | Scope guardrails are best checked as focused repository assertions. |
| Manual proof MP1-MP6 | Method correctness, output boundaries, extracted-content use, and visual-policy compliance. | R5-R20. | Domain correctness cannot be fully proven by string checks. |

## Validation Evidence Available Before Final Verify

| Stage | Command or proof | Result |
|---|---|---|
| M1 precheck | `/usr/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` | Failed because `/usr/bin/python` had no `pytest` module installed. |
| M1 red test | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` | Failed before implementation because `method-kits/check-sheet.md` did not exist. |
| M1 focused | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` | Passed after implementation: 3 passed, 14 deselected. |
| M1 focused file | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` | Passed: 17 passed. |
| M1 hygiene | `git diff --check` | Passed. |
| M2 red test | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` | Failed before implementation because M2 method-kit files did not exist. |
| M2 focused | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` | Passed after implementation: 4 passed, 17 deselected. |
| M2 focused file | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` | Passed: 21 passed. |
| M2 hygiene | `git diff --check` | Passed. |
| M3 red test | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'five_w_two_h_method_kit'` | Failed before implementation because `method-kits/five-w-two-h.md` did not exist. |
| M3 focused | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'five_w_two_h_method_kit'` | Passed after implementation: 3 passed, 21 deselected. |
| M3 focused file | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` | Passed: 24 passed. |
| M3 hygiene | `git diff --check` | Passed. |
| M4 red test | `.venv/bin/python -m pytest tests/test_artifact_consistency.py tests/test_template_catalog.py tests/test_method_kit_closeout.py -k 'deleted_legacy or catalog_points or template_catalog or official_method_kits'` | Failed before implementation because active docs and catalog entries still referenced deleted `docs/methods/` paths. |
| M4 focused suite | `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py tests/test_method_guides.py tests/test_template_catalog.py tests/test_template_catalog_failures.py tests/test_scope_guards.py tests/test_method_kit_closeout.py tests/test_acceptance.py` | Passed: 53 passed. |
| M4 catalog | `.venv/bin/python -m qcc_toolkit.templates validate templates/ppt/catalog.yml` | Passed: validated 5 template catalog entries. |
| M4 hygiene | `git diff --check` | Passed. |
| M4 review probes | Targeted deleted-reference, canonical-catalog, mismatched-guide, and catalog-validation probes rerun during code-review M4. | Passed. |

No hosted CI result is claimed here.
Final `verify` has not run yet.

## Review Resolution Summary

One material proposal-review finding was recorded before implementation.

| Finding | Disposition | Resolution |
|---|---|---|
| PR-MK-001 | closed / accepted | The team chose deletion rather than compatibility notices. The proposal, spec, plan, tests, and M4 cleanup were aligned to that decision. |

No material code-review findings were recorded for M1, M2, M3, or M4.
No review-resolution work is required after code-review M4.

## Alternatives Rejected

| Alternative | Why rejected |
|---|---|
| Restore legacy `docs/methods/` compatibility notices. | The team explicitly wanted deletion rather than compatibility notices, and the spec records that migration path. |
| Implement all four method kits in one large slice. | The plan chose smaller reviewable milestones so Check Sheet could establish the evidence standard first, Fishbone and 5 Whys could be reviewed together, and 5W2H could be checked separately. |
| Add Standard Work, Visual Control, or Monitoring Plan in this change. | The accepted proposal deferred sustainment practices to a later slice. |
| Add Control Chart, SPC rules, process capability, or run-rule automation. | Those methods carry higher statistical and validation risk and are explicit non-goals. |
| Require generated visuals for every guide before method text was reviewed. | The visual policy made generated images optional and method-specific. Images were added later only after the method kits and review boundaries existed. |
| Make PowerPoint or Python the primary method surface. | The constitution and spec keep Markdown method guidance canonical and tool-specific assets optional. |

## Scope Control

The implementation did not add:

- Control Chart, SPC rules, control limits, run rules, or process capability;
- broad statistical automation or rendering backends;
- named-tool tutorials as the primary guide;
- generated visuals treated as project evidence;
- legacy `docs/methods/` compatibility pages;
- network calls, telemetry, hosted integrations, or external services.

## Risks And Follow-Ups

| Risk or follow-up | Status |
|---|---|
| Historical records still contain old `docs/methods/` paths. | Accepted by EC1 when clearly historical. M4 tests and review scans focus on active surfaces. |
| Catalog validation now supports two method-ID declaration styles. | Covered by catalog tests, mismatch tests, catalog validation, and M4 code-review probes. |
| Final lifecycle readiness is not yet complete. | Final local `verify` is complete, but PR handoff still needs its own evidence. |
| Sustainment methods remain outside this change. | Deferred by proposal decision; a future proposal should decide the sustainment-method slice. |

## Current Handoff

All implementation milestones are closed.
Code-review M4 closed cleanly with no material findings.

This explanation completes the durable change rationale for final closeout.
Final local verify is recorded in `verify-report.md`.
Next stage: `pr`.
