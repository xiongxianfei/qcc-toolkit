---
method_id: pareto_chart
method_name: Pareto Chart
qcc_stages:
  - understand_current_condition
  - analyze_causes
method_type: chart
primary_output: ranked_category_chart
evidence_risk: medium
imagegen_allowed: conceptual_only
final_chart_generation: manual_tool_guided
related_methods:
  upstream:
    - check_sheet
    - stratification
  downstream:
    - fishbone_diagram
    - five_whys
guide_version: 0.1.0
review_status: draft
---

# Pareto Chart

## Summary

A Pareto Chart ranks counted categories from largest to smallest so a QCC team can see where problems are concentrated.
It helps the team focus analysis on the vital few categories before moving into cause analysis.

## QCC stage fit

Use Pareto Chart during Understand Current Condition to summarize baseline defect, delay, complaint, or error categories.
Use it during Analyze Causes when category counts help decide where Fishbone Diagram or 5 Whys should start.

## What question this method answers

Which counted category or small group of categories contributes most to the current problem during the stated period and scope?

## When to use

Use Pareto Chart when categories are defined before counting, each event belongs to one category, and counts are collected over one consistent period and scope.
It works well after Check Sheet data collection or stratification of a larger problem.

## When not to use

Do not use Pareto Chart when categories overlap, the period changes by category, counts are estimates, or the team needs proof of root cause.
The chart prioritizes observed categories; it does not prove why those categories occurred.

## Required inputs

- Category names.
- Count for each category.
- One consistent date range.
- One consistent process, product, location, team, or other scope definition.
- Source data owner or source system.
- Category definition notes when names could be interpreted differently.

## Output

The output is a ranked category chart, usually column bars, with an optional cumulative percentage line capped at 100 percent.
The output should include a source note, date range, scope or filters, key finding, next action, and evidence note.

## Manual chart or worksheet recipe

Use `chart-creation-guide.md` for the full recipe.
At minimum, prepare a table with categories and counts, sort categories from largest to smallest, create column bars, optionally add a cumulative percentage line, and add the evidence note fields before final use.

## Quality standards

The chart needs a clear title, correct chart type, readable labels, source note, correct scale, appropriate annotations, and defensible interpretation.
The conclusion should identify the largest contributor, the top few categories when useful, and the next QCC method or action.

## Interpretation guide

Read the largest bars first.
Use the cumulative line only to describe concentration, not to declare root cause.
If the top categories are close together, avoid over-focusing on one category without checking definitions and source quality.

## Example conclusion wording

- "The largest contributor is `[category]`, with `[count]` cases during `[date range]`."
- "The top three categories account for `[share]` of counted cases, so the team will investigate those categories first."
- "The next action is to study `[category]` with Fishbone Diagram or 5 Whys."
- "This chart prioritizes observed categories; it does not prove root cause."

## Common mistakes

- Mixing categories from different periods or scopes.
- Sorting alphabetically instead of by descending count.
- Using overlapping category definitions.
- Hiding the source data or date range.
- Treating the tallest bar as a proven cause.
- Adding fake precision or unsupported thresholds.

## Review checklist

- Does the chart use categories and counts from one consistent period and scope?
- Are categories sorted from largest to smallest by count?
- Are the title, labels, source note, date range, and scope readable?
- Is the cumulative percentage line capped at 100 percent if used?
- Does the interpretation avoid root-cause overclaims?
- Is the evidence note complete for the intended evidence level?

## Evidence note for final charts

For final data-dependent charts, complete `evidence-note-template.md`.
Preserve source data, date range, scope or filters, total sample or count, tool used, assumptions, exclusions, reviewer, review date, and review status.

## Image-assisted demonstration notes

Image prompts in this kit are for conceptual teaching only.
Generated images must not include exact project values, fake percentages, misleading axes, or claims of final project evidence.

## Related methods

Upstream methods include Check Sheet and Stratification.
Downstream methods include Fishbone Diagram and 5 Whys.
