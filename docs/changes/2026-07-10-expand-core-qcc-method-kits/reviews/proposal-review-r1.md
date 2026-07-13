# Proposal Review R1: Expand Core QCC Method Kits

## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: PR-MK-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-log.md`
- Review resolution: `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-resolution.md`
- Open blockers: PR-MK-001
- Immediate next stage: isolated stop before spec

## Material Findings

## Finding PR-MK-001

- Finding ID: PR-MK-001
- Severity: major
- Location: `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md:29`, `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md:30`, `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md:96`, `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md:104`, `docs/proposals/2026-07-10-expand-core-qcc-method-kits.md:208`
- Evidence: The proposal says not to delete legacy `docs/methods/` paths immediately, says each corresponding legacy page is retained as a concise notice, and lists compatibility targets for those paths. The current working tree deletes `docs/methods/5_whys.md`, `docs/methods/5w2h.md`, `docs/methods/check_sheet.md`, `docs/methods/fishbone_diagram.md`, and `docs/methods/pareto_chart.md`; `find docs/methods -maxdepth 1 -type f -print` returns no files. Existing live references still point at those removed paths in `templates/ppt/catalog.yml:21`, `templates/ppt/catalog.yml:84`, `templates/ppt/catalog.yml:128`, `templates/ppt/catalog.yml:176`, `templates/ppt/catalog.yml:224`, and `docs/qcc-project-story.md:151` through `docs/qcc-project-story.md:154`.
- Required outcome: Reconcile the proposal with the actual legacy-guide transition before using it for a feature specification. Either restore the legacy paths as compatibility notices and keep the proposal's current compatibility policy, or revise the proposal to accept deletion and route all broken catalog/navigation/spec references into the next required behavior contract.
- Safe resolution path: Prefer restoring concise notices at the legacy paths because that matches the accepted proposal, preserves inbound links, and avoids invalidating current catalog and project-story references. If deletion is now the intended policy, revise the proposal's non-goals, expected behavior, resolved questions, rollout/rollback, risks, scope budget, and downstream specification details to explicitly govern extraction-only deletion and required reference updates.
- needs-decision rationale: Owner decision needed only if the team wants deletion rather than compatibility notices; otherwise the safe default is to restore notices and proceed with the existing proposal direction.

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal identifies a real workflow gap between current official method kits and older guide-surface methods. |
| User value | pass | The proposed methods improve observation quality, cause-hypothesis structure, causal-chain discipline, and action/problem framing. |
| Option diversity | pass | The proposal compares deferral, one-method promotion, four-method promotion, sustainment expansion, and Control Chart/SPC. |
| Decision rationale | pass | The selected method set follows QCC evidence flow and defers higher-risk SPC scope. |
| Scope control | concern | The written scope is clear, but the current working tree removed the legacy paths that the proposal says to retain as compatibility notices. |
| Architecture awareness | pass | The proposal correctly keeps runtime architecture out of scope and makes architecture conditional on durable boundary or automation changes. |
| Testability | pass | The proposal names content, navigation, canonical-source, reviewer-task, user-task, and visual-policy proof. |
| Risk honesty | concern | The duplicate-guidance risk is named, but the present deletion state creates a stronger broken-reference compatibility risk that the proposal no longer reflects. |
| Rollout realism | block | The rollout depends on legacy notices introduced with each method kit, but the legacy files have already been removed in the working tree. |
| Readiness for spec | block | A spec would inherit contradictory guidance unless the proposal or working tree is reconciled first. |

## Scope Preservation Review

- Scope-preservation result: pass

| Initial user goal | Proposal treatment | Review result |
|---|---|---|
| Generate a proposal for creating new quality management methods | in scope | pass |
| Follow best practices for method creation | in scope | pass |
| Preserve QCC Toolkit's Markdown-first identity | in scope | pass |
| Decide which quality management methods should come next | in scope | pass |
| Incorporate targeted review amendments from July 10, 2026 | in scope | pass |

## Scope Budget Review

| Work item | Treatment | Review result |
|---|---|---|
| Check Sheet method kit | first-slice candidate | pass |
| Fishbone Diagram method kit | core to this proposal | pass |
| 5 Whys method kit | core to this proposal | pass |
| 5W2H method kit | core to this proposal | pass |
| README and QCC project-story navigation | same-slice dependency | pass |
| Legacy notice conversion | same-slice dependency | concern; the files have been deleted, so the planned same-slice dependency is no longer represented in the working tree. |
| Focused documentation checks | same-slice dependency | pass |
| Conceptual teaching images and prompt records | separate implementation slice | pass |
| Standard Work / Visual Control / Monitoring Plan | deferable follow-up | pass |
| Control Chart, SPC rules, and process capability | separate proposal | pass |
| Automation or chart rendering for new methods | separate proposal | pass |

## Vision Fit Review

The `Vision fit` section uses the required value `fits the current vision`.
That claim is supported by `VISION.md`, which makes Markdown method guides the primary surface, treats manual chart creation as a core competency, treats generated images as conceptual aids only, and keeps specific tools secondary.

No vision conflict or exception is required.

## Recommended Proposal Edits

Required before spec:

- Reconcile legacy-path policy with the current deletion state.
- If retaining compatibility notices, restore `docs/methods/check_sheet.md`, `docs/methods/fishbone_diagram.md`, `docs/methods/5_whys.md`, `docs/methods/5w2h.md`, and `docs/methods/pareto_chart.md` as concise notices or revise the proposal to state when those notices will be created.
- If deletion is intended instead, update the proposal to replace the legacy-notice policy with extraction/deletion policy and explicitly require updates to `templates/ppt/catalog.yml`, `docs/qcc-project-story.md`, and any tests or docs that still rely on removed legacy guide paths.
- Keep the current method set, SPC deferral, visual policy, and content-focused verification strategy; those parts are ready for downstream specification after the compatibility issue is resolved.

## Recommendation

- Recommendation: changes-requested
- Reason: The proposal is strategically sound and aligned with the current vision, but it is not ready for spec while its legacy compatibility policy conflicts with the current working tree and live repository references.
- Next step: resolve PR-MK-001 by either restoring legacy notices or revising the proposal to govern deletion and reference updates.
- Immediate next stage: isolated stop before spec
