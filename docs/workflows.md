# Workflow Guide

## Status

- Owner skill: workflow
- Purpose: project-local workflow and artifact-location guide
- Last reviewed: 2026-07-07
- Guide status: current
- Project-local customizations: QCC Toolkit uses the default RigorLoop artifact layout, with `VISION.md` and `CONSTITUTION.md` as standing governance artifacts.

## Source Rank

Use this order when deciding artifact placement:

1. Explicit user path or change ID.
2. Existing active artifact metadata, active plan metadata, or active change metadata.
3. Approved specs or schemas.
4. This workflow guide for artifact types it specifies.
5. Stage-skill portable default.
6. Block on ambiguity.

`CONSTITUTION.md` remains the highest operational authority. `VISION.md` remains the project-identity authority.

## Lifecycle Graph

```text
proposal
-> proposal-review
-> spec
-> spec-review
-> architecture, when required
-> architecture-review, when required
-> plan
-> plan-review
-> test-spec
-> test-spec-review, when required
-> implement
-> code-review
-> review-resolution, when triggered
-> ci-maintenance, when triggered
-> explain-change
-> verify
-> pr
```

Manual single-skill invocations remain isolated unless the user explicitly asks to continue through the full workflow or an active workflow-managed context requires continuation.

## Stage Obligations

| Stage | Obligation | Required input | Output artifact | Blocks downstream when |
| --- | --- | --- | --- | --- |
| vision | standing | Project identity or owner direction | `VISION.md`, README vision block, optional `docs/vision/strategic-positioning.md` | Project scope or identity is unclear |
| constitution | standing | Project purpose and governance needs | `CONSTITUTION.md`, optional `AGENTS.md` | Governance rules are missing or contradictory |
| project-map | living reference | Current repository state | `docs/project-map.md` | Routing depends on repo structure that is undocumented or stale |
| workflow | living reference | Adopted lifecycle and artifact placement needs | `docs/workflows.md` | Artifact placement is missing, stale, or ambiguous |
| explore | on-demand | Unsettled product or technical direction | Exploration artifact or chat decision summary | Options or problem framing are too unclear to propose |
| research | on-demand | Current external facts or uncertain platform behavior | Research artifact or cited summary | External facts are needed for a safe decision |
| proposal | mandatory for nontrivial product direction | Problem, goals, options, and fit question | `docs/proposals/<change-id>.md` | Scope, tradeoff, or decision is not accepted |
| proposal-review | mandatory after proposal | Proposal artifact | `docs/changes/<change-id>/reviews/proposal-review-r<n>.md` | Material findings or non-approval remain unresolved |
| spec | mandatory for behavior changes | Accepted direction | `specs/<slug>.md` | Observable behavior lacks approved requirements |
| spec-review | mandatory after spec | Spec artifact | `docs/changes/<change-id>/reviews/spec-review-r<n>.md` | Material findings or non-approval remain unresolved |
| architecture | conditional | Approved spec and architecture trigger | `docs/architecture/<scope>/architecture.md` or ADR | Cross-boundary or durable design is not recorded |
| architecture-review | conditional | Architecture artifact | `docs/changes/<change-id>/reviews/architecture-review-r<n>.md` | Material findings or non-approval remain unresolved |
| plan | mandatory for multi-step or risky work | Approved upstream artifacts | `docs/plans/YYYY-MM-DD-<slug>.md`, `docs/plan.md` | Milestones, validation, or recovery path are unclear |
| plan-review | mandatory after plan | Plan artifact | `docs/changes/<change-id>/reviews/plan-review-r<n>.md` | Material findings or non-approval remain unresolved |
| test-spec | mandatory before implementation | Approved spec and plan | `specs/<slug>.test.md` | Proof map is missing or untraceable |
| test-spec-review | conditional | Test spec artifact | `docs/changes/<change-id>/reviews/test-spec-review-r<n>.md` | Required proof coverage is unapproved |
| implement | mandatory for code changes | Approved plan and proof map | Code/tests plus updated plan evidence | Implementation milestones are incomplete |
| code-review | mandatory after implementation | Final or milestone diff and validation evidence | `docs/changes/<change-id>/reviews/code-review-<milestone>-r<n>.md` | Material findings, inconclusive review, or missing holistic review |
| review-resolution | conditional | Material findings or blocking review outcomes | `docs/changes/<change-id>/review-resolution.md` | Findings remain open or need re-review |
| ci-maintenance | conditional | CI change or CI gap trigger | CI config and validation notes | CI evidence is required and unavailable or stale |
| explain-change | mandatory before final verify for code changes | Diff, requirements, design, tests, reviews | `docs/changes/<change-id>/explain-change.md` | Meaningful changes lack traceable rationale |
| verify | mandatory before PR handoff | Final artifacts, diff, validation evidence | `docs/changes/<change-id>/verify-report.md` | Branch-readiness evidence is missing or failing |
| pr | final handoff | Clean verify evidence | Pull request body or handoff notes | PR summary or reviewer notes are incomplete |
| learn | periodic/on-demand | Incident, repeated mistake, or explicit trigger | `docs/learn/sessions/YYYY-MM-DD-<slug>.md` | Lesson is required to prevent recurrence |

## Artifact Registry

```yaml
artifact_locations:
  agent_rules:
    owner: constitution
    path: AGENTS.md
    required_when: agent-facing operating rules are needed
    notes: concise entry point that links to CONSTITUTION.md

  constitution:
    owner: constitution
    path: CONSTITUTION.md
    required_when: project governance is created or changed
    notes: highest operational authority

  vision:
    owner: vision
    path: VISION.md
    required_when: project identity is created or changed
    notes: product identity and scope

  project_map:
    owner: project-map
    path: docs/project-map.md
    required_when: repository structure or boundaries need durable orientation
    notes: current-state map, not a backlog

  workflow_guide:
    owner: workflow
    path: docs/workflows.md
    required_when: RigorLoop is adopted or project-local artifact routing is needed
    notes: project-local workflow and artifact-location guide

  proposal:
    owner: proposal
    path: docs/proposals/<change-id>.md
    required_when: proposal stage is active
    notes: decision-oriented change proposal

  spec:
    owner: spec
    path: specs/<slug>.md
    required_when: feature behavior requires a durable contract
    notes: approved feature contract with stable requirement IDs

  test_spec:
    owner: test-spec
    path: specs/<slug>.test.md
    required_when: proof map is required before implementation
    notes: active proof-planning surface

  architecture_record:
    owner: architecture
    path: docs/architecture/<scope>/architecture.md
    required_when: architecture is required
    notes: current architecture package or project-local equivalent

  adr:
    owner: architecture
    path: docs/adr/ADR-YYYYMMDD-<slug>.md
    required_when: durable architecture decision is required
    notes: architecture decision record

  plan_index:
    owner: plan / workflow
    path: docs/plan.md
    required_when: planning exists
    notes: global index, not detailed milestone journal

  change_plan:
    owner: plan
    path: docs/plans/YYYY-MM-DD-<slug>.md
    required_when: workflow-managed change has an execution plan
    notes: detailed plan for one change

  change_metadata:
    owner: workflow
    path: docs/changes/<change-id>/change.yaml
    required_when: formal workflow-managed lifecycle recording begins
    notes: metadata and validation ledger

  formal_review_record:
    owner: review skills
    path: docs/changes/<change-id>/reviews/<stage>-r<n>.md
    required_when: formal review is recorded
    notes: formal review artifact

  review_log:
    owner: review skills
    path: docs/changes/<change-id>/review-log.md
    required_when: formal reviews exist
    notes: review and finding index

  review_resolution:
    owner: review-resolution
    path: docs/changes/<change-id>/review-resolution.md
    required_when: material findings or blocking outcomes require disposition
    notes: finding disposition record

  explain_change:
    owner: explain-change
    path: docs/changes/<change-id>/explain-change.md
    required_when: final explanation is required
    notes: human-readable change rationale

  verify_report:
    owner: verify
    path: docs/changes/<change-id>/verify-report.md
    required_when: verify stage runs
    notes: branch-readiness evidence

  pr_handoff:
    owner: pr
    external_surface: pull_request_body
    required_when: PR stage is reached
    notes: local handoff file only when project policy requires it

  learn_session:
    owner: learn
    path: docs/learn/sessions/YYYY-MM-DD-<slug>.md
    required_when: learn trigger occurs
    notes: historical learning evidence, not live routing authority
```

## Artifact Location Table

| Artifact type | Canonical path | Owner skill | Required when | Notes |
| --- | --- | --- | --- | --- |
| Agent rules | `AGENTS.md` | `constitution` | Agent-facing rules are needed | Concise entry point |
| Constitution | `CONSTITUTION.md` | `constitution` | Governance is created or changed | Highest operational authority |
| Vision | `VISION.md` | `vision` | Project identity is created or changed | Product scope authority |
| Project map | `docs/project-map.md` | `project-map` | Repo orientation is needed | Current-state map |
| Workflow guide | `docs/workflows.md` | `workflow` | RigorLoop is adopted or routing needs a local guide | This file |
| Proposals | `docs/proposals/<change-id>.md` | `proposal` | Proposal stage | Decision artifact |
| Specs | `specs/<slug>.md` | `spec` | Spec stage | Behavior contract |
| Test specs | `specs/<slug>.test.md` | `test-spec` | Test-spec stage | Active proof map |
| Architecture | `docs/architecture/<scope>/architecture.md` | `architecture` | Architecture required | Architecture package |
| ADRs | `docs/adr/ADR-YYYYMMDD-<slug>.md` | `architecture` | Durable architecture decision | ADR |
| Plan index | `docs/plan.md` | `plan` / `workflow` | Planning exists | Global index |
| Plans | `docs/plans/YYYY-MM-DD-<slug>.md` | `plan` | Workflow-managed change | Detailed plan |
| Change metadata | `docs/changes/<change-id>/change.yaml` | `workflow` | Formal change lifecycle | Metadata ledger |
| Formal review records | `docs/changes/<change-id>/reviews/<stage>-r<n>.md` | review skill | Formal review | Review evidence |
| Review log | `docs/changes/<change-id>/review-log.md` | review skills | Formal review exists | Review index |
| Review resolution | `docs/changes/<change-id>/review-resolution.md` | review-resolution | Findings require disposition | Resolution evidence |
| Explain change | `docs/changes/<change-id>/explain-change.md` | `explain-change` | Final explanation | Change rationale |
| Verify report | `docs/changes/<change-id>/verify-report.md` | `verify` | Verify stage | Branch-readiness proof |
| PR handoff | Pull request body | `pr` | PR stage | Local handoff only when project policy requires it |
| Learn session | `docs/learn/sessions/YYYY-MM-DD-<slug>.md` | `learn` | Learn trigger | Historical rationale |

## Review Record Placement

| Review type | Path | Creates review-log entry? | Creates review-resolution? |
| --- | --- | ---: | ---: |
| Proposal review | `docs/changes/<change-id>/reviews/proposal-review-r<n>.md` | yes | only when findings or blockers require disposition |
| Spec review | `docs/changes/<change-id>/reviews/spec-review-r<n>.md` | yes | only when findings or blockers require disposition |
| Architecture review | `docs/changes/<change-id>/reviews/architecture-review-r<n>.md` | yes | only when findings or blockers require disposition |
| Plan review | `docs/changes/<change-id>/reviews/plan-review-r<n>.md` | yes | only when findings or blockers require disposition |
| Test-spec review | `docs/changes/<change-id>/reviews/test-spec-review-r<n>.md` | yes | only when findings or blockers require disposition |
| Code review | `docs/changes/<change-id>/reviews/code-review-<milestone>-r<n>.md` | yes | only when findings or blockers require disposition |

## Plan Surfaces

| Surface | Path | Purpose |
| --- | --- | --- |
| Plan index | `docs/plan.md` | Small global index of active, blocked, and recently completed work |
| Change plan | `docs/plans/YYYY-MM-DD-<slug>.md` | Detailed execution plan for one workflow-managed change |
| Change metadata | `docs/changes/<change-id>/change.yaml` | Metadata, validation, and evidence ledger |

## Guide Ownership

| Question | Primary source | Secondary source |
| --- | --- | --- |
| Why does this project exist? | `VISION.md` | README vision summary |
| What governance rules apply? | `CONSTITUTION.md` | `AGENTS.md` |
| Where does an artifact go? | `docs/workflows.md` | stage-skill portable default |
| What does the repository contain? | `docs/project-map.md` | README links |
| What work is active? | `docs/plan.md` | active change pack |
| What happened in one change? | `docs/changes/<change-id>/` | plan index |
| How do I perform one stage? | `.agents/skills/<stage>/SKILL.md` | this workflow guide |
| Why did a rule change? | proposal, spec, or learn session | workflow guide after accepted update |

## Customization Rules

- Record project-local path customizations in the artifact registry and table.
- Do not rely on chat history or learn sessions as live routing authority.
- If a stage skill's portable default conflicts with this guide, use this guide for the project-local workflow and record the drift for validation.
- If this guide conflicts with `CONSTITUTION.md`, `VISION.md`, a governing spec, or a schema, stop and resolve the conflict before writing new artifacts.
- Unknown artifact types block instead of using inferred paths.
- New change IDs use `YYYY-MM-DD-slug` unless the user or active change metadata provides a different explicit ID.

## Migration Notes

- This guide is the first project-local workflow guide.
- No historical workflow-managed artifacts exist yet, so no migration is required.
- Forward placement for new workflow-managed artifacts follows this guide.

## Validation Notes

- Created from `.agents/skills/workflow/assets/workflows-skeleton.md` on 2026-07-07.
- Filled all skeleton placeholders with QCC Toolkit paths and current governance sources.
- Validated against `CONSTITUTION.md`, `AGENTS.md`, and the workflow skill default paths by direct inspection.
- No package, test, lint, or CI commands exist yet, so guide validation is documentation inspection only.
