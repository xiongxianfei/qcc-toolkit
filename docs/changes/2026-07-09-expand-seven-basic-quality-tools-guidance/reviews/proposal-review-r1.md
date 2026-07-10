# Proposal Review R1: Expand Seven Basic Quality Tools Guidance

## Result

- Skill: proposal-review
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-07-09-expand-seven-basic-quality-tools-guidance/review-log.md`
- Review resolution: not-required
- Open blockers: none
- Immediate next stage: spec on separate user request

## Material Findings

None.

## Review Dimensions

| Dimension | Result | Notes |
|---|---|---|
| Problem clarity | pass | The proposal explains that adding methods without a direction risks disconnected tool pages and unsafe statistical guidance. |
| User value | pass | The user value is clearer QCC method coverage for process flow, distribution, and relationship questions. |
| Option diversity | pass | Options include do nothing, Flowchart-only, three-method expansion, Control Chart inclusion, automation-first, and named-tool tutorials. |
| Decision rationale | pass | The recommendation follows risk ordering: Flowchart first, then Histogram, then Scatter Diagram, with Control Chart deferred. |
| Scope control | pass | Non-goals exclude Control Chart, SPC rules, automation, named-tool tutorials, web UI, dashboard, CAPA/EQMS, and external services. |
| Architecture awareness | pass | The proposal identifies method-kit files, optional media/prompts, README and project-story links, lightweight front matter, optional metadata/catalog files, and architecture triggers. |
| Testability | pass | The proposal names structure, front matter, link, tool-neutrality, manual-creation, method-specific, and evidence-note checks. |
| Risk honesty | pass | The proposal names title ambiguity, Histogram bin/sample risk, Scatter causation risk, Flowchart genericity, scope breadth, automation creep, named-tool creep, and data sensitivity. |
| Rollout realism | pass | Rollout requires spec first, architecture only if triggered, small implementation slices, and rollback to Flowchart-only or draft status if needed. |
| Readiness for spec | pass | Proposal-level questions are resolved, and detailed choices are routed to downstream specification artifacts. |

## Scope Preservation Review

- Scope-preservation result: pass

| Initial user goal | Proposal treatment | Review result |
|---|---|---|
| Start a proposal for "Complete Seven Basic Quality Tools: Flowchart, Histogram, Scatter Diagram" | in scope | pass; title was amended to avoid implying Control Chart is included. |
| Follow best practices | in scope | pass; proposal records method-specific guardrails and testing strategy. |
| Expand QCC methods | in scope | pass; Flowchart, Histogram, and Scatter Diagram are core to this proposal. |
| Avoid disconnected method pages | in scope | pass; proposal ties method expansion to QCC project-story guidance. |

## Scope Budget Review

| Work item | Treatment | Review result |
|---|---|---|
| Flowchart / Process Map method kit | core to this proposal | pass |
| Histogram method kit | core to this proposal | pass |
| Scatter Diagram method kit | core to this proposal | pass |
| Control Chart method kit | separate proposal | pass |
| Python chart automation | deferable follow-up | pass |
| Named-tool recipes | deferable follow-up | pass |
| Teaching images and prompts for the new methods | deferable follow-up | pass |

## Vision Fit Review

The `Vision fit` section uses the required value `fits the current vision`.
That claim is supported by `VISION.md`, which makes Markdown method guides the primary surface, treats manual chart creation as a core competency, treats generated images as conceptual aids only, and keeps specific tools secondary.

No vision conflict or exception is required.

## Recommended Proposal Edits

- Recommended edits: none required before spec.

Optional downstream attention:

- In the feature spec, define exact front matter fields narrowly enough to avoid recreating heavy metadata sidecars.
- In the feature spec or test spec, define manual creation and evidence-note checks for each method using stable requirement and test IDs.
- Keep Control Chart outside the spec scope unless a later owner decision explicitly changes the proposal.

## Recommendation

- Recommendation: approved
- Reason: The amended proposal has clear user value, preserves the Markdown-first vision, records scope boundaries, resolves proposal-level questions, and has enough method-specific quality guidance for spec authoring.
- Next step: write a feature spec for Flowchart / Process Map, Histogram, and Scatter Diagram when the user requests downstream work.
- Immediate next stage: spec on separate user request
