# QCC Method Selection Summary Implementation Rationale

## Change

M1 adds the canonical method selector at `method-kits/README.md`.
The selector lets users start from either project question or QCC stage, then check the evidence or input needed before choosing a method.
It links only existing method guides and keeps Control Chart, SPC, process capability, Standard Work, Visual Control, and Monitoring Plan as status-labeled future or advanced guidance.

The root `README.md` now links to the selector and keeps method-kit navigation stage-neutral.
`docs/qcc-project-story.md` links to the selector while preserving its existing high-level QCC story map.

## Why

The approved spec requires one canonical detailed stage-method selection surface.
Keeping the selector under `method-kits/README.md` avoids duplicate matrices in root or project-story navigation while still making method choice visible from the main user entry points.

## Proof

Focused tests were added before production documentation and initially failed because `method-kits/README.md` did not exist.
After implementation, focused selector/navigation proof passed, the broader Markdown-first documentation regression passed, and manual scenario review recorded MP1-MP4 as passed for implementation handoff.

## Scope

This change is documentation-only.
It does not add new QCC methods, runtime behavior, generated navigation, machine-readable catalogs, web UI, chart calculations, or tool-specific workflow.
