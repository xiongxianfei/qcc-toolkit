---
method_id:
method_name:
qcc_stages:
  - define_problem
method_type:
primary_output:
evidence_risk:
imagegen_allowed: conceptual_only
final_chart_generation: manual_tool_guided
related_methods:
  upstream: []
  downstream: []
guide_version: 0.1.0
review_status: draft
---

# Method Name

## Summary

Explain the method in plain language.
This guide should teach application, not only define the method.

## QCC stage fit

Name the QCC stage or stages where the method belongs and explain why.

## What question this method answers

State the decision, comparison, or understanding this method supports.

## When to use

List the conditions that make this method appropriate.

## When not to use

List conditions where the method can mislead, add little value, or require a stronger method.

## Required inputs

Describe required data, categories, team inputs, process context, or assumptions.

## Output

Describe the expected chart, worksheet, diagram, decision, or review artifact.

## Manual chart or worksheet recipe

Explain how a user creates the chart, worksheet, or diagram manually with a suitable class of tool.
For chart-based methods, include the chart-creation sections below in this guide so the user has one primary document.

## Chart purpose

Explain the quality question this chart answers and the QCC decision it supports.

## Required data structure

Define required columns, categories, counts, units, dates, subgroups, limits, or filters.

## Data preparation

Explain sorting, grouping, cleaning, missing-value handling, exclusions, and consistency checks.

## Tool-selection guidance

Name suitable tool classes, such as spreadsheet tools, charting tools, presentation tools, statistical tools, or data-analysis tools.
Do not require a named product in the first slice.

## Chart construction steps

Provide generic steps that work across suitable tool classes.

## Formatting standard

Apply the shared chart-quality standard: clear title, correct chart type, readable labels, source note, correct scale, appropriate annotations, and defensible interpretation.

## Required annotations

Describe required notes for source data, date range, scope or filters, sample size, assumptions, and review status.

## Interpretation rules

Explain what users may conclude and what they must not overclaim.

## Common chart defects

List common defects such as wrong chart type, inconsistent scope, unreadable labels, missing source note, distorted scale, unsupported annotation, or weak interpretation.

## Quality standards

Name the required title, labels, source note, scale, annotations, and defensible interpretation checks that apply.

## Interpretation guide

Explain safe conclusions, unsafe overclaims, and how to connect the result to the QCC project story.

## Example conclusion wording

Provide short sentence patterns a user can adapt.

## Common mistakes

List practical mistakes that would make the method output weak, misleading, or hard to review.

## Review checklist

Use pass/fail criteria for method purpose, QCC stage fit, inputs, output quality, interpretation, evidence note, and review status.

| Check | Pass | Fail | Notes |
|---|---|---|---|
| method purpose is clear and matches the QCC question |  |  |  |
| QCC stage fit is stated and defensible |  |  |  |
| required inputs are present or limitations are documented |  |  |  |
| source data, date range, and scope are recorded when data-dependent |  |  |  |
| chart or worksheet follows the method quality standard |  |  |  |
| interpretation avoids unsupported causal or statistical claims |  |  |  |
| evidence note includes reviewer and review status |  |  |  |
| image-assisted material is conceptual only |  |  |  |
| final quantitative evidence is created or verified with a suitable tool path, not image generation |  |  |  |

## Evidence note for final charts

For final data-dependent charts, preserve source data, date range, scope or filters, tool used, assumptions, reviewer, review date, and review status.
Use a separate support evidence-note template only when the chart is being prepared for final project use.

## Image-assisted demonstration notes

Use generated or reviewed images only as conceptual teaching aids.
Do not use image generation for final quantitative evidence charts.
Keep image prompts and maintainer review notes in `support/` so the main guide remains the user entry point.

## Related methods

List upstream and downstream methods that commonly connect to this method.
