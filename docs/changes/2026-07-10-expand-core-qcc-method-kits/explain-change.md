# Explain Change: Expand Core QCC Method Kits

## Status

Active rationale record.

## M1 Check Sheet Method Kit

| Surface | Change | Why | Requirement / proof |
|---|---|---|---|
| `method-kits/check-sheet.md` | Added the official Markdown-first Check Sheet method kit. | M1 requires a canonical guide that teaches observation purpose, operational definitions, period/scope, collection context, category rules, blank/unknown/other handling, pilot collection, evidence note, and review checklist. | Spec R1-R6, R17-R19, R21; test spec T1-T5, T12, T14; manual proof MP1 and MP5. |
| `tests/test_markdown_first_method_guidance.py` | Added M1-focused tests for Check Sheet structure, metadata, observation safeguards, extracted-content use, and scope guardrails. | The test spec requires proof before implementation, and the guide must be checked for both common method-kit structure and Check Sheet-specific misuse risks. | Test spec T1-T5, T12, T14. |
| `docs/changes/2026-07-10-expand-core-qcc-method-kits/manual-method-kit-review.md` | Added manual proof for Check Sheet method correctness and extracted legacy content use. | Method correctness and overclaiming boundaries need reviewer-readable proof in addition to string checks. | Test spec MP1 and MP5. |
| `docs/plans/2026-07-10-expand-core-qcc-method-kits.md`, `docs/plan.md`, `change.yaml` | Updated M1 state and validation evidence for code-review handoff. | The implement stage owns current milestone state, progress, and validation notes before handing the slice to code-review. | Implement workflow requirements. |

## M2 Fishbone Diagram and 5 Whys Method Kits

| Surface | Change | Why | Requirement / proof |
|---|---|---|---|
| `method-kits/fishbone-diagram.md` | Added the official Markdown-first Fishbone Diagram method kit. | M2 requires a canonical guide that teaches one precise effect statement, context-appropriate categories, fact versus hypothesis separation, evidence status, prioritization for checking, and the boundary that the output is cause hypotheses rather than verified root cause. | Spec R1-R4, R7-R8, R17-R21; test spec T1-T4, T6, T12-T14; manual proof MP2, MP5, and MP6. |
| `method-kits/five-whys.md` | Added the official Markdown-first 5 Whys method kit. | M2 requires a canonical guide that avoids exact-five and single-chain overclaims, permits branching, requires fact support or verification status, avoids personal blame, and treats the chain as provisional until checked. | Spec R1-R4, R9-R10, R17-R21; test spec T1-T4, T7, T12-T14; manual proof MP3, MP5, and MP6. |
| `tests/test_markdown_first_method_guidance.py` | Added M2-focused tests for cause-analysis guide structure, metadata, Fishbone safeguards, 5 Whys safeguards, extracted-content use, visual policy, and scope guardrails. | The test spec requires proof before implementation, including direct checks for method-specific misuse risks and source-content preservation. | Test spec T1-T4, T6-T7, T12-T14. |
| `docs/changes/2026-07-10-expand-core-qcc-method-kits/manual-method-kit-review.md` | Added manual proof for Fishbone and 5 Whys method correctness, extracted legacy content use, and visual policy. | Method correctness, evidence-boundary safety, and visual-policy compliance need reviewer-readable proof in addition to string checks. | Test spec MP2, MP3, MP5, and MP6. |
| `docs/plans/2026-07-10-expand-core-qcc-method-kits.md`, `docs/plan.md`, `change.yaml` | Updated M2 state and validation evidence for code-review handoff. | The implement stage owns current milestone state, progress, decisions, discoveries, and validation notes before handing the slice to code-review. | Implement workflow requirements. |

## Validation Evidence

| Command | Result |
|---|---|
| `/usr/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` | Failed because `/usr/bin/python` has no `pytest` module installed. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` before implementation | Failed as expected because `method-kits/check-sheet.md` did not exist. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'check_sheet_method_kit'` after implementation | Passed: 3 passed, 14 deselected. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` | Passed: 17 passed. |
| `git diff --check` | Passed. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` before implementation | Failed as expected because the M2 method-kit files did not exist. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py -k 'm2_cause_analysis or fishbone_method_kit or five_whys_method_kit'` after implementation | Passed: 4 passed, 17 deselected. |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py` | Passed: 21 passed. |
| `git diff --check` | Passed. |

## Remaining Gates

- Code-review M2.
- M3-M4 implementation and code-review loops.
- Final explain-change refresh before verify.
- Verify and PR handoff after all milestones close.
