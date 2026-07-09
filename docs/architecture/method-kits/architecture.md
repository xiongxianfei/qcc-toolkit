# QCC Method Kits Architecture

## Status

- approved

## Related artifacts

- Proposal: [Improve QCC Method Templates](../../proposals/2026-07-08-improve-qcc-method-templates.md)
- Spec: [QCC Method Kits Spec](../../../specs/qcc-method-kits.md)
- Spec review: [Spec Review R1](../../changes/2026-07-08-improve-qcc-method-templates/reviews/spec-review-r1.md)
- Existing system architecture: [QCC Toolkit First-Slice Architecture](../system/architecture.md)
- ADRs:
  - No new ADR required for this package. This architecture applies the accepted PowerPoint-first, Python-assisted method-kit direction to repository boundaries and validation responsibilities without changing the existing local-first Python stack or evidence-package authority ADRs.

## Introduction and Goals

This package defines the architecture for official QCC method kits.
It explains how PowerPoint templates, Markdown guides, template catalog metadata, incoming templates, optional Python assist, and evidence guidance fit together before implementation planning.

The architecture goal is to prevent shallow placeholder decks from becoming official method assets.
Official method kits are coordinated, reviewable assets that teach the method, provide a working PowerPoint surface, preserve canonical written guidance, and route users to Python assist only when it adds rigor.

## Architecture Constraints

| Constraint | Architectural response |
|---|---|
| PowerPoint is the primary method-template workflow. | Official kits center on editable PowerPoint templates, demo examples, and blank copyable slides or worksheets. |
| Markdown governs method knowledge. | Every official kit links to a canonical Markdown guide with method purpose, stage fit, cautions, interpretation, and review checklist. |
| Python is selective assist. | Python assist is optional, recommended, or required by method mode and evidence level rather than mandatory for every method. |
| Incoming templates are not official assets. | User-created or legacy templates stay in an incoming/source area until reviewed and migrated. |
| Catalog drift must be detectable. | Catalog validation owns official kit registration, path checks, implementation mode checks, and incoming/source distinction. |
| Existing Pareto evidence behavior must remain stable. | Method-kit changes do not replace the first-slice evidence package contract unless a later spec changes it. |
| No full automated PPTX generation is required. | Templates are versioned PowerPoint assets; automation can follow after kit contracts stabilize. |

## Context and Scope

QCC Toolkit users interact with method kits through local repository assets and PowerPoint.
The system boundary includes official method-kit folders or equivalent cataloged assets, PowerPoint templates, Markdown guides, template catalog metadata, incoming template storage, optional sample data, optional Python assist, and generated evidence references.

See [diagrams/context.mmd](diagrams/context.mmd) for the C4 system context view.

In scope:

- official method-kit structure;
- template catalog responsibilities;
- incoming-template intake boundary;
- method implementation mode classification;
- evidence-level decision guidance;
- optional Python assist linkage.

Out of scope:

- full automated PPTX generation;
- web UI or dashboard;
- enterprise quality workflow;
- advanced statistical methods beyond the accepted first method-kit set.

## Solution Strategy

The selected approach is a method-kit-centered repository model.

```text
Markdown method guide
  -> PowerPoint method template
    -> catalog entry and review checklist
      -> user edits template directly when method is simple
      -> Python assist when data, calculation, validation, or evidence rigor requires it
```

The main tradeoff is explicit.
The toolkit optimizes for practical PowerPoint use and reviewable method guidance, while keeping Python available for rigor instead of making it the first workflow for every method.

The architecture separates three asset states:

- official method kits, which satisfy the spec minimum and are cataloged;
- incoming/source templates, which preserve useful user-created materials but are not official;
- generated evidence packages, which remain authoritative for high-rigor data-dependent outputs.

## Building Block View

See [diagrams/container.mmd](diagrams/container.mmd) for the C4 container view.

| Area | Responsibility | Key rules |
|---|---|---|
| Official method kits | Coordinate guide, template, demo, blank working slide, checklist, evidence notes, sample data, and optional assist. | A kit is official only when cataloged and complete against the method-kit standard. |
| Markdown guides | Govern method purpose, usage guidance, cautions, interpretation, and review checklist. | Guides are the canonical written method reference. |
| PowerPoint templates | Provide the teaching, working, copyable, and presentation surface. | Templates label demo content and distinguish blank project slides. |
| Template catalog | Registers official kits, implementation modes, paths, assist status, and validation metadata. | Catalog validation rejects missing paths, duplicate ownership, and invalid official/incoming classification. |
| Incoming templates | Store user-created or legacy source templates before review. | Incoming templates are not official and are screened for privacy, formulas, assumptions, and method fit. |
| Python assist | Provides optional or required validation, calculation, generated outputs, and reproducibility support. | Assist paths are linked from catalog metadata only when useful for the method mode or evidence level. |
| Evidence guidance | Explains whether PowerPoint-only, Python-assisted, or reproducible evidence is expected. | Guidance is based on teaching/draft, normal project, formal review, and high-risk evidence levels. |

### Method implementation modes

| Mode | Primary surface | Python role |
|---|---|---|
| `template_native_worksheet` | PowerPoint worksheet and Markdown guide. | None or optional export later. |
| `template_native_diagram` | PowerPoint diagram and Markdown guide. | None initially. |
| `powerpoint_native_chart` | Editable PowerPoint chart with sample data and formula guidance. | Optional for raw data, repeated generation, or higher evidence levels. |
| `python_assisted_chart` | PowerPoint presentation template plus Python-generated output. | Recommended for validation-heavy calculations. |
| `python_first_analysis` | Python or specialized analysis path plus presentation template. | Primary analysis path for advanced methods. |

## Runtime View

### Official method-kit use

1. User opens the official method kit through the catalog, guide, or template path.
2. User reads the method overview, QCC stage fit, use/not-use guidance, required inputs, and checklist.
3. User reviews the completed demo example.
4. User copies the blank working slide or worksheet into a project deck.
5. User edits the PowerPoint worksheet, diagram, or chart directly when the method mode allows it.
6. User records evidence/source notes and writes a conclusion using interpretation patterns.
7. Facilitator reviews the slide against checklist criteria.
8. If evidence level or data complexity triggers Python assist, user follows the assist path before finalizing the data-dependent conclusion.

### Incoming-template migration

1. A user-created or legacy template is placed in the incoming/source area.
2. The template is tagged with known method, stage, owner/source, and review notes when available.
3. Reviewer checks content, private data, formulas, assumptions, method fit, and missing kit sections.
4. Useful layout or wording is migrated into an official method kit.
5. The official kit is cataloged only after required content and review checks are satisfied.

### Catalog validation

1. Validation loads the template catalog.
2. Validation checks official entries for required metadata, paths, implementation mode, assist status, and ownership.
3. Validation distinguishes official kits from incoming/source templates.
4. Validation fails with entry and field context when a required contract is missing.

## Deployment View

Method kits are repository assets distributed with the local toolkit.
They do not require a server, database, hosted service, telemetry, or cloud storage.

| Artifact | Deployment concern |
|---|---|
| PowerPoint templates | Versioned binary assets with reviewable source notes or metadata where practical. |
| Markdown guides | Versioned plain-text method references. |
| Catalog YAML | Versioned registry validated by local checks. |
| Incoming templates | Non-official source assets that may contain private or unsupported content until reviewed. |
| Python assist | Local scripts, notebooks, or package entry points linked only when useful. |
| Evidence packages | User-generated local outputs for reproducible data-dependent conclusions. |

Full automated PPTX generation is deferred.
The architecture preserves future automation by keeping stable IDs, catalog metadata, placeholders, and evidence package references.

## Crosscutting Concepts

### Source of truth

PowerPoint owns teaching layout, working slides, demo examples, and copyable presentation patterns.
Markdown owns method guidance and review criteria.
Python owns validation, formulas, generated outputs, reproducibility metadata, and evidence packages where assist is used.

### Reviewability

Official kits need enough text or metadata for reviewers to inspect completeness without opening opaque binary content alone.
Binary PowerPoint assets should be paired with source notes, catalog fields, or generated checks where practical.

### Privacy

Incoming templates are treated as untrusted source assets until reviewed.
They may contain private names, real data, hidden notes, unsupported formulas, or undocumented assumptions.

### Evidence rigor

Evidence levels prevent two bad defaults: requiring Python for every draft and accepting manual PowerPoint for every final conclusion.
The kit explains when PowerPoint is enough and when reproducible evidence is needed.

## Architecture Decisions

No new ADR is required for this package.
The accepted proposal and approved spec define the product direction, while this architecture records the repository and validation boundaries needed to implement it.
Existing ADRs for local-first Python and evidence-package authority remain valid.

## Quality Requirements

| Quality | Scenario | Measure |
|---|---|---|
| Usability | A QCC user opens an official method kit. | The kit exposes method guidance, demo, blank working slide, interpretation patterns, mistakes, and checklist without requiring Python code first. |
| Reviewability | A reviewer checks method-kit completeness. | Required kit content, catalog metadata, implementation mode, and assist status are inspectable through documented artifacts or validation output. |
| Traceability | A completed data-dependent chart is used for formal review. | The kit guidance points to source/date notes and Python assist or reproducible evidence when risk level requires it. |
| Drift resistance | A template, guide, or assist path moves. | Catalog validation fails with entry and field context. |
| Privacy | An incoming template contains real names or hidden assumptions. | It remains non-official until reviewed and cleaned. |

## Risks and Technical Debt

| Risk | Handling |
|---|---|
| Binary PPTX assets are hard to review. | Pair official templates with source notes, catalog metadata, and validation checks where practical. |
| Method-kit completeness checks become too shallow. | Test-spec should combine automated catalog/source checks with targeted manual visual review. |
| Python assist policy is misapplied. | Evidence-level guidance and implementation modes keep assist recommendations explicit. |
| Incoming templates leak private data. | Incoming templates remain non-official and require privacy review before migration. |
| Future PPTX automation changes placeholder expectations. | Stable IDs and catalog metadata preserve future automation paths without requiring automation now. |

## Glossary

| Term | Meaning |
|---|---|
| Official method kit | A method kit that satisfies the spec minimum and is registered as official in the catalog. |
| Incoming template | User-created or legacy source template not yet approved as an official kit. |
| Evidence level | Guidance category for draft, normal project, formal review, and high-risk evidence expectations. |
| Python assist | Optional or recommended local Python path for validation, calculation, generation, or reproducibility. |

## Next artifacts

- Architecture review.
- Execution plan after architecture review approval.

## Follow-on artifacts

- `docs/changes/2026-07-08-improve-qcc-method-templates/reviews/architecture-review-r1.md` - approved architecture review with no material findings.

## Readiness

Approved and ready for execution planning.

This architecture is not implementation-ready by itself.
