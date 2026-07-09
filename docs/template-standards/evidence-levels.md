# QCC Method Kit Evidence Levels

## Purpose

This standard defines how much evidence traceability a QCC method kit should require for different review contexts.
It prevents two unsafe defaults: requiring Python for every draft and treating a manual PowerPoint chart as final evidence for every reviewed conclusion.

## Evidence Levels

| Level | Use case | Minimum evidence expectation |
|---|---|---|
| Level 1 | teaching/draft | PowerPoint template edits are sufficient when the output is a training example, workshop draft, or early team discussion. Demo content must remain labeled as demo, not project evidence. |
| Level 2 | normal QCC project | PowerPoint-native charts or worksheets are acceptable when source data, date range, assumptions, and checklist evidence are preserved with the completed slide. |
| Level 3 | competition or management review | Preserve source data, calculation table where data are summarized, method checklist, and versioned template. Python assist is recommended for raw-data or repeated chart methods. |
| Level 4 | audit or high-risk evidence | Require a reproducible evidence package or another validated analysis path before finalizing data-dependent conclusions. |

## Required Source Notes

Every final project slide or worksheet should record:

- source data or source record owner;
- date range;
- filters;
- assumptions;
- calculation notes when a count, percentage, ranking, or generated output is used;
- prepared-by/date;
- method-kit version or template identity when the output is used for formal review.

## Manual PowerPoint Boundary

Manual PowerPoint editing is acceptable for Level 1 and many Level 2 uses.
For Level 3 and Level 4 data-dependent conclusions, a manual PowerPoint chart is not authoritative final evidence by itself.
The user must preserve source data and review evidence, and use Python assist or another validated analysis path when the data are raw, large, repeated, validation-heavy, high-risk, or audit-related.

## Method-Kit Alignment

Method guides and PowerPoint source notes should use the same evidence-level names:

- teaching/draft;
- normal QCC project;
- competition or management review;
- audit or high-risk evidence.

Catalog entries should keep the matching machine-readable values:

- `teaching_draft`;
- `normal_qcc_project`;
- `competition_management_review`;
- `audit_high_risk`.
