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

## Legacy optional-aid note

This guide belongs to the earlier first-slice method-guide surface.
Under the current Markdown-first direction, the official Pareto method guide lives at `method-kits/pareto-chart.md`.
PowerPoint templates and Python aids are optional execution aids and do not override method-kit guidance.

## Summary

A Pareto Chart ranks categories by frequency so a QCC team can see which problems contribute most to the current condition.
In this toolkit, Pareto is the first complete data-chart method.

## Purpose

Pareto Chart identifies the vital few categories contributing most to a visible problem.
It answers: which counted category should the QCC team study first?
For ordinary project discussion, the PowerPoint template is an optional teaching, editing, and presentation aid.
Python assist is optional for raw logs, repeated generation, validation, or higher-rigor evidence.

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
Categories must be non-overlapping, defined before counting, and collected over a consistent data period.

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

## PowerPoint template workflow

1. Open the Pareto Chart PowerPoint template.
2. Read the purpose, QCC stage fit, required inputs, and misuse cautions.
3. Review the completed demo example labeled as not project evidence.
4. For a small category-count dataset, edit the embedded chart data directly in PowerPoint.
5. Copy the blank copyable project slide into the QCC deck.
6. Record data source, date range, filters, and calculation notes on the slide.
7. Use Python assist when the dataset is raw, large, repeated, validation-heavy, or used for high-rigor evidence.

## PowerPoint edit instructions

Right-click the chart and choose Edit Data.
Replace the demo categories and counts with project values.
Keep categories non-overlapping and use one consistent data period.
Use the chart data table to sort counts descending before writing the conclusion.
Verify cumulative values if the slide includes a cumulative line or cumulative table.
Confirm formula cells were not overwritten before using the slide in review.
Do not present the demo data as project evidence.

## Chart decision guide

Use the chart to support a focus decision, not to prove root cause.
The decision supported is which category or vital few should receive follow-up analysis first.
The pattern to look for is one dominant category, a steep drop after the vital few, or a long tail that needs regrouping.
A safe conclusion says where counted problems are concentrated during the stated date range.
An overclaim to avoid is saying the chart proves root cause, process stability, or permanent improvement.

## Chart variant library

Use a simple count Pareto for draft focus decisions.
Use Cumulative Pareto when the team needs top-share or threshold wording.
Use Before/after Pareto comparison only when the before and after periods are comparable and use the same source and category rules.
Use Focus annotation to mark the selected vital few and name the next method.

## Chart quality checklist

Every completed Pareto slide should show Source, Date range, Filters, category definitions, sorting rule, key finding, and next action.
When percentages or thresholds are used, the working data should include Percent and Cumulative percent fields.
Use a Formula check before review to confirm percentage and cumulative percent cells are visible or documented and were not overwritten.
Use Python assist when raw data, repeated generation, validation-heavy formulas, or high-rigor evidence make manual PowerPoint editing too risky.

## Blank copyable project slide

The blank copyable project slide should contain a project title, editable chart or chart image area, source, date range, filters, key finding, next action, prepared-by, and prepared-date fields.
Use it as a working QCC slide for normal project review.
For high-rigor evidence, link the slide back to the generated evidence package or another validated analysis path.

## Interpretation guidance

Read the tallest bars first and compare the cumulative percentage line against the team's practical threshold.
The top category or top few categories are candidates for deeper cause analysis, not automatic countermeasures.

## Interpretation patterns

- Largest contributor: "The largest contributor is `[category]`, with `[count]` cases during `[date range]`."
- top-three share: "The top-three categories account for `[percentage]` of counted cases, so the team will focus analysis there first."
- Focus decision: "The next action is to investigate `[category]` using Fishbone Diagram or 5 Whys."
- Caution wording: "This chart prioritizes observed categories; it does not prove root cause."

## Common mistakes

Common mistakes include mixing unlike categories, counting the same event twice, using categories that hide important stratification, and treating Pareto rank as proof of root cause.
Other review risks include unsorted bars, mixed time periods, overlapping categories, missing counts, overwritten formula cells, and demo data presented as project evidence.

## Python assist decision

PowerPoint is enough for training, draft discussion, and small manually counted category tables when the slide preserves source and date range.
Use Python assist for raw defect logs, large row counts, repeated weekly generation, complex validation, final competition evidence, audit/high-risk evidence, or when a reviewer needs reproducible calculation metadata.
Python assist should generate or verify the calculated table, chart, caption, warnings, and evidence package.

## Evidence levels and source notes

- Level 1 teaching/draft: PowerPoint template edits are acceptable.
- Level 2 normal QCC project: PowerPoint-native chart edits are acceptable when source data, date range, filters, and checklist evidence are preserved.
- Level 3 competition or management review: preserve source data, calculation table, method checklist, and versioned template; Python assist is recommended for raw-data or repeated chart methods.
- Level 4 audit or high-risk evidence: require a reproducible evidence package or another validated analysis path before finalizing the data-dependent conclusion.

## Example

Use the worked example in `method-kits/pareto-chart.md` for the current
Markdown-first Pareto demonstration.
Bundled example scripts and example project folders are no longer part of the
supported repository surface.

## Related methods

Related upstream methods include Check Sheet and Stratification.
Related downstream methods include Fishbone Diagram and 5 Whys.

## Formula or logic notes

The implemented calculation convention groups rows by category, sums category frequency, calculates percentage as category count divided by total count, and calculates cumulative_count and cumulative_percentage in ranked order.
The sort order is descending count, then case-insensitive category name, then original category string for deterministic ties.
This convention is implemented in Python as an optional validated analysis aid for generated Pareto evidence.

## Review checklist

- Confirm the data period and source are visible on the slide.
- Confirm categories are non-overlapping and counted over a consistent data period.
- Confirm counts are sorted descending.
- Confirm formula cells were not overwritten when embedded formulas are used.
- Confirm the key finding and next action are written.
- Confirm the next method is identified when deeper cause analysis is needed.
- Confirm Python assist was used or considered when the output is final, repeated, raw-data-driven, or high-rigor.
- Confirm the category definition was stable before data collection.
- Confirm event-record data or category-count data was selected intentionally.
- Confirm the calculated total matches the source data.
- Confirm the chart caption and warnings are included with the evidence package.
- Confirm slide use refers back to the generated evidence package.
