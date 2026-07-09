# Chart Creation Guide: Pareto Chart

## Chart purpose

A Pareto Chart answers where counted problems are concentrated.
It supports a QCC focus decision before deeper cause analysis.

## Required data structure

Use categories and counts.
Each row should contain one category and one non-negative count.
All categories must come from one consistent period and scope.
Keep the source data and category definitions with the chart.

## Data preparation

Clean blank category names.
Combine only categories that share the same definition.
Do not mix date ranges, products, lines, locations, or filters unless the scope intentionally includes them.
Calculate total count and percent of total.
If using a cumulative line, calculate cumulative count and cumulative percentage after sorting.

## Tool-selection guidance

Use spreadsheet tools, charting tools, presentation tools, or data-analysis tools when the source table and calculations remain reviewable.
Use statistical tools or a validated analysis path when the chart supports formal review, audit, high-risk evidence, or repeated generation.
The first slice uses tool classes only and does not require a named product.

## Chart construction steps

1. Create a two-column table with category and count.
2. Confirm all counts use one consistent period and scope.
3. Sort categories from largest to smallest by descending count.
   Review rule: sort categories from largest to smallest before creating the chart.
4. Create column bars using the sorted categories.
5. Optionally add a cumulative percentage line capped at 100 percent.
6. Add a clear title that names the problem, period, and scope.
7. Add readable category labels, count axis, and cumulative percentage axis if used.
8. Add a source note with source data, date range, scope or filters, and total count.
9. Annotate the selected vital few only when the annotation supports the next QCC action.

## Formatting standard

Use a clear title, correct chart type, readable labels, source note, correct scale, appropriate annotations, and defensible interpretation.
Column bars are the required base chart form.
The optional cumulative percentage line should never exceed 100 percent.

## Required annotations

- Source data.
- Date range.
- Scope or filters.
- Total sample or count.
- Sorting rule.
- Key finding.
- Next action.
- Evidence level and review status when used as final chart evidence.

## Interpretation rules

Safe interpretations identify the largest category, the top few categories, and the next analysis step.
Unsafe interpretations claim that rank proves root cause, permanent improvement, process stability, or countermeasure effectiveness.

## Common chart defects

- Missing source data.
- Mixed date ranges.
- Categories not sorted by descending count.
- Overlapping categories.
- Unreadable category labels.
- Cumulative percentage line not capped at 100 percent.
- Conclusion not tied to the visible data.

## Review checklist

Use pass/fail checks for categories and counts, one consistent period and scope, descending count sort, column bars, optional cumulative percentage line, source note, readable labels, and defensible interpretation.

## Evidence note

Attach an evidence note before final use.
The evidence note must preserve source data, date range, scope or filters, total sample or count, tool used, assumptions, exclusions, reviewer, review date, and review status.
