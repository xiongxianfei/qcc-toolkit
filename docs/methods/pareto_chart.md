---
method_id: pareto_chart
method_name: Pareto Chart
qcc_stages:
  - understand_current_condition
  - analyze_causes
method_type: data_chart
supports_generated_chart: true
first_slice_status: supported
---

# Pareto Chart

## Summary

A Pareto Chart ranks categories by frequency so a QCC team can see which problems contribute most to the current condition.
In this toolkit, Pareto is the first complete data-chart method.

## QCC stage fit

Use Pareto during Understand Current Condition to identify the largest categories in baseline data.
Use it during Analyze Causes when category counts help prioritize where deeper cause analysis should start.

## When to use

Use Pareto when defect, error, delay, complaint, or event categories can be counted consistently.
It is useful when the team needs to focus effort on the largest contributors before selecting countermeasures.

## When not to use

Do not use Pareto when categories are undefined, overlapping, or created after seeing the answer.
Do not use it as proof of root cause; it shows concentration of observed categories, not why they occurred.

## Inputs required

The first slice supports event-record data and category-count data.
For event-record data, provide one row per event and a category column; each row counts as one occurrence.
For category-count data, provide a category column and a numeric count column.
Counts must be non-negative, categories must not be blank, and the dataset must not be empty.

## Outputs produced

The method produces a calculated table, chart specification, interactive HTML chart, deterministic caption, warnings, metadata, and evidence README or manifest.
Optional PNG export is allowed when local static export support is available.

## Procedure

1. Define the category labels before counting.
2. Collect event records or category-count data.
3. Validate required columns and count values.
4. Calculate frequency, percentage, cumulative_count, and cumulative_percentage.
5. Sort categories by descending count.
6. Review the top categories before selecting the next QCC method.

## Interpretation guidance

Read the tallest bars first and compare the cumulative percentage line against the team's practical threshold.
The top category or top few categories are candidates for deeper cause analysis, not automatic countermeasures.

## Common mistakes

Common mistakes include mixing unlike categories, counting the same event twice, using categories that hide important stratification, and treating Pareto rank as proof of root cause.

## Example

Use the planned `examples/scripts/generate_pareto.py` script with the `reduce-packing-label-errors` example project when M5 adds the runnable starter workflow.
Until then, the Python API tests show the calculation and evidence package behavior.

## Related methods

Related upstream methods include Check Sheet and Stratification.
Related downstream methods include Fishbone Diagram and 5 Whys.

## Formula or logic notes

The implemented calculation convention groups rows by category, sums category frequency, calculates percentage as category count divided by total count, and calculates cumulative_count and cumulative_percentage in ranked order.
The sort order is descending count, then case-insensitive category name, then original category string for deterministic ties.
This convention is implemented in Python and is the authority for generated Pareto evidence.

## Review checklist

- Confirm the category definition was stable before data collection.
- Confirm event-record data or category-count data was selected intentionally.
- Confirm the calculated total matches the source data.
- Confirm the chart caption and warnings are included with the evidence package.
- Confirm slide use refers back to the generated evidence package.
