# Proposal Review R2: Expand Core QCC Method Kits

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-10-expand-core-qcc-method-kits/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-07-10-expand-core-qcc-method-kits/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: spec on separate user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal describes the workflow gap between existing official method kits and older noncanonical method content. |
| User value | pass | The selected methods improve observation quality, cause analysis discipline, causal-chain review, and problem/action framing. |
| Option diversity | pass | Options include deferral, one-method promotion, four-method promotion, sustainment expansion, and Control Chart/SPC. |
| Decision rationale | pass | The recommendation follows evidence-flow ordering and avoids the higher interpretation risk of Control Chart/SPC. |
| Scope control | pass | Non-goals now explicitly exclude restoring legacy pages as notices and exclude leaving live references to deleted `docs/methods/` files. |
| Architecture awareness | pass | The proposal limits expected impact to Markdown method-guide boundaries, navigation, media if used, deleted-path cleanup, and documentation validation; architecture is conditional if deletion changes durable boundaries. |
| Testability | pass | The proposal names guide completeness, method correctness, interpretation safety, navigation, deleted-reference cleanup, canonical source, user task, reviewer task, and visual-policy proof. |
| Risk honesty | pass | The proposal now names broken references after deletion and lost legacy detail, with mitigations through reference cleanup and `docs/methods-key-content.md`. |
| Rollout realism | pass | Rollout explicitly includes additive method kits plus deletion-aware catalog, navigation, test, and documentation cleanup. |
| Readiness for spec | pass | Proposal-level questions are resolved, and remaining choices are appropriately routed to the feature specification. |

## Scope Preservation Review

- Scope-preservation result: pass

| Initial user goal | Proposal treatment | Review result |
|---|---|---|
| Generate a proposal for creating new quality management methods | in scope | pass |
| Follow best practices for method creation | in scope | pass |
| Preserve QCC Toolkit's Markdown-first identity | in scope | pass |
| Decide which quality management methods should come next | in scope | pass |
| Incorporate targeted review amendments from July 10, 2026 | in scope | pass |
| Choose deletion rather than compatibility notices | in scope | pass; proposal now treats deletion as accepted policy and requires deleted-reference cleanup. |

## Scope Budget Review

| Work item | Treatment | Review result |
|---|---|---|
| Check Sheet method kit | first-slice candidate | pass |
| Fishbone Diagram method kit | core to this proposal | pass |
| 5 Whys method kit | core to this proposal | pass |
| 5W2H method kit | core to this proposal | pass |
| README and QCC project-story navigation | same-slice dependency | pass |
| Deleted legacy reference cleanup | same-slice dependency | pass |
| Focused documentation checks | same-slice dependency | pass |
| Conceptual teaching images and prompt records | separate implementation slice | pass |
| Standard Work / Visual Control / Monitoring Plan | deferable follow-up | pass |
| Control Chart, SPC rules, and process capability | separate proposal | pass |
| Automation or chart rendering for new methods | separate proposal | pass |

## Vision Fit Review

The `Vision fit` section uses the required value `fits the current vision`.
That claim is supported by `VISION.md`, which makes Markdown method guides the primary surface, treats manual chart creation as a core competency, treats generated images as conceptual aids only, and keeps specific tools secondary.

No vision conflict or exception is required.

## Prior Finding Review

| Finding ID | Prior status | R2 result |
|---|---|---|
| PR-MK-001 | closed in `review-resolution.md` | pass; the proposal now accepts deletion rather than compatibility notices and routes deleted-reference cleanup into the feature specification. |

## Recommended Proposal Edits

- Recommended edits: none required before spec.

Optional downstream attention:

- The feature spec should list each deleted legacy path and each known live reference surface that must be updated or removed.
- The feature spec should decide whether deletion of `docs/methods/` requires a short architecture note or remains inside the existing Markdown-first architecture.
- The execution plan should sequence Check Sheet first, then Fishbone Diagram and 5 Whys together, then 5W2H.

## Recommendation

- Recommendation: approved
- Reason: The proposal is aligned with the current vision, preserves scope boundaries, resolves the prior legacy-path contradiction, and is specific enough for feature specification.
- Next step: write a feature specification for the four-method expansion, including deleted-reference cleanup and use of `docs/methods-key-content.md` as source material.
- Immediate next stage: spec on separate user request
