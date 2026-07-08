# Constitution

## Project Purpose

QCC Toolkit is a template-backed, Python-powered evidence system for Quality Control Circle methods and projects. It serves QCC facilitators, quality engineers, improvement teams, educators, and analysts who need reusable QCC method templates, version-controlled method guidance, data validation, statistical analysis, chart generation, interpretation, metadata, and report-ready evidence.

Project work MUST preserve the core product identity from [VISION.md](VISION.md): PowerPoint teaches and presents, Markdown governs method knowledge, and Python generates traceable QCC evidence.

## Source Of Truth Order

When sources conflict, agents MUST follow this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved specs under `specs/` or `docs/changes/<change-id>/`
4. Architecture documents under `docs/architecture/`
5. Execution plans and test specifications
6. Tests and verified behavior
7. Code
8. Chat instructions

Chat MAY clarify the current task, but durable project rules MUST be recorded in repository artifacts.

## Spec-Driven Rules

Behavior changes MUST have a spec before implementation when they affect public API, QCC stage semantics, method contracts, statistical calculations, chart outputs, report artifacts, configuration, compatibility, security, privacy, or user-facing workflow.

Specs SHOULD identify requirements with stable IDs so tests, reviews, and implementation notes can trace back to them.

Trivial edits MAY proceed without a new spec when they do not change behavior, compatibility, or project commitments. The agent MUST state the reason when skipping a spec for a nontrivial-looking change.

## Test-Driven Rules

Implementation work that changes behavior MUST start from a test, fixture, or executable proof that can fail before the change and pass after it.

Bug fixes MUST include a regression test or a documented reason why the bug cannot be reproduced automatically.

Statistical calculations, data validation, chart specifications, and report metadata MUST be tested against explicit expected values or structured snapshots. Visual output tests SHOULD verify semantic chart specifications before relying on image comparisons.

Agents MUST NOT claim behavior is correct only from inspection when a local test or executable proof is practical.

## Architecture Rules

The toolkit SHOULD keep these boundaries clear:

- QCC project and stage model
- method contracts and data validation
- statistical calculation logic
- chart specification
- rendering backends
- interpretation and report artifacts

Calculation logic MUST NOT depend on a rendering backend. Rendering code MUST preserve chart metadata needed for review. Report generation MUST NOT hide the data, parameters, assumptions, warnings, or method context behind presentation-only output.

Cross-boundary changes, persistent data formats, public APIs, plugin-like extension points, or dependency choices MUST have architecture documentation before implementation.

## Security And Privacy Rules

Secrets, credentials, private machine paths, and private user data MUST NOT be committed, logged, or embedded in generated artifacts.

Input datasets MAY contain sensitive operational or quality data. Code and docs MUST treat user data as private by default, avoid unnecessary logging of raw rows, and prefer explicit user control for exported reports.

New dependencies MUST be justified by product value, maintenance health, license compatibility, and security risk. Agents MUST NOT add network calls, telemetry, or external services without explicit approval and documentation.

## Compatibility Rules

Public Python APIs, QCC stage identifiers, method parameter names, data schemas, chart specification fields, configuration files, and report artifact formats are compatibility surfaces once released or documented.

Breaking changes MUST be called out in the relevant spec or proposal and SHOULD include a migration path or deprecation plan.

QCC terminology MAY be configurable, but stable internal stage identifiers MUST remain consistent so methods, charts, reports, and tests do not fragment across local labels.

## Verification Rules

Before claiming completion, agents MUST run the relevant local checks for the changed surface and report the commands and outcomes.

When no package, test, lint, type, or CI commands exist yet, agents MUST say so explicitly and use the most direct available verification, such as file inspection, Markdown checks, or targeted scripts.

Agents MUST NOT claim CI passed unless the CI result was actually observed.

## Review Rules

Use proposal review when scope, product fit, or tradeoffs are unclear. Use spec review when requirements need validation. Use architecture review for cross-component, persistent, security, performance, or hard-to-reverse design decisions. Use plan review for multi-step implementation. Use code review after implementation and before final readiness claims.

Small documentation-only or narrowly scoped mechanical changes MAY skip formal review, but the agent MUST still verify the actual diff.

## Documentation Rules

Documentation MUST be updated when a change affects project purpose, public behavior, QCC stage semantics, method contracts, data schemas, chart evidence metadata, report output expectations, security posture, compatibility, or workflow.

`VISION.md` records project identity and scope. `CONSTITUTION.md` records governance. Specs record behavior. Architecture docs record durable design. Plans record execution. Tests record proof. These artifacts MUST NOT be substituted for each other.

Learned process rules SHOULD be captured in durable docs when they would prevent repeated mistakes.

## Agent Behavior Rules

Agents MUST make assumptions explicit when repository artifacts are missing or ambiguous.

Agents MUST NOT make unrelated refactors, broad template cleanup, dependency churn, or formatting-only rewrites during a scoped change unless the user asks for them.

Agents MUST preserve existing user changes in the working tree and MUST NOT revert files they did not intentionally change.

Agents MUST NOT fabricate commands, test results, CI status, benchmark numbers, research findings, or source citations.

Agents SHOULD prefer small, reviewable changes that keep QCC evidence traceability intact.

## Standard Workflow And Manual Skill Use

The recommended standard workflow for substantive changes is:

1. Check `VISION.md` and this constitution for fit.
2. Explore or research only when assumptions are uncertain.
3. Write or update a proposal when product direction or tradeoffs need approval.
4. Write or update a spec for observable behavior.
5. Write or update architecture documentation for cross-boundary or durable design.
6. Create an execution plan for multi-step work.
7. Define tests or proof before implementation.
8. Implement the scoped change.
9. Review the code and resolve findings.
10. Verify with local commands and available CI evidence.
11. Prepare PR notes when the branch is ready.

Individual skills MAY be invoked manually for isolated work, but completion claims MUST still include evidence appropriate to the lifecycle stage. A workflow is not complete merely because a skill ran; it is complete when the required artifact, review, or verification evidence exists.

## Current Repository Assumptions

The repository is at the first-slice closeout stage for QCC Toolkit.
It currently has vision artifacts, governance artifacts, workflow guidance, a project map, an accepted proposal, an approved first-slice spec, an approved architecture package, an active test spec, an implementation plan, reviewed M1-M7 implementation milestones, method guides, reviewable PPT template placeholder assets, a template catalog, a Pareto evidence engine, starter script, synthetic example project, report-ready outputs, tests, review records, review-resolution evidence, and a completed explain-change artifact.
It does not currently have hosted CI workflows, release automation, automated PPTX generation, web UI, dashboard, CAPA/EQMS workflow, Control Chart support, or advanced QCC methods.
Agents MUST avoid claiming hosted CI status, PR readiness, merge readiness, release readiness, or unsupported QCC method behavior until the relevant verification, PR, release, or implementation artifacts exist.
