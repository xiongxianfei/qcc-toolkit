# Histogram

Status: draft
Guide version: 0.1.0
Method ID: histogram
Method name: Histogram
Method type: chart
QCC stages: understand current condition; verify effects
Evidence risk: medium
Image policy: conceptual teaching images only
Automation policy: manual chart creation first; no chart-rendering automation in this slice

## Summary

A Histogram shows how numeric observations are distributed across intervals.
It helps a QCC team understand spread, shape, concentration, gaps, and outliers before selecting or verifying countermeasures.
This guide teaches manual chart creation and safe interpretation, not only the chart definition.

## QCC stage fit

Use Histogram during current-state grasp when the team needs to understand variation in a numeric measure.
Use it during verification when the team compares before and after distributions with matching scope and measurement rules.
Use it with caution whenever sample size, measurement method, or bin-width choices could change the apparent shape.

## What question this method answers

How are numeric observations distributed, and what does the spread, shape, or outlier pattern suggest for the next QCC step?

## When to use

Use Histogram when observations are numeric, collected from one defined scope and period, and numerous enough to show a meaningful distribution.
It is useful for cycle time, waiting time, defect size, measurement error, weight, temperature, count-per-unit, or other numeric quality measures.
It works well when the team needs to see spread rather than only an average.

## When not to use

Do not use Histogram for category counts; use a category method instead.
Do not use it when the sample is too small to support a visible distribution.
Do not use it when measurement rules changed during the period.
Do not claim a histogram proves process stability, root cause, or countermeasure effectiveness by itself.

## Required inputs

- Numeric observations.
- Measurement unit.
- Date range or observation period.
- Process, product, location, team, or other scope definition.
- Data source or owner.
- Sample size.
- Exclusions or missing-value rules.
- Bin-width or interval-choice rationale.

## Output

The output is a frequency distribution chart with adjacent bars for numeric intervals.
The output should include a title, axis labels, units, source note, sample size, date range, scope, binning note, key observation, and evidence note.

## Manual chart or diagram recipe

Prepare one numeric column, choose intervals carefully, count how many observations fall into each interval, and draw adjacent bars.
Keep the source data, bin choices, and evidence note reviewable.
Use the chart to understand variation, not to prove stability.

## Chart purpose

A Histogram answers what the distribution of a numeric measure looks like.
It supports current-state understanding and before/after review when measurement conditions are comparable.

## Required data structure

Use numeric observations in one column or one reviewable list.
Each observation should share the same unit and measurement rule.
Record the period, scope, sample size, and exclusions.

## Data preparation

Remove or explain nonnumeric entries.
Check for changed measurement rules or mixed populations.
Record missing-value handling and exclusions.
Choose a bin width that shows shape without hiding meaningful variation or creating noise.
Keep outliers visible unless there is a documented data-quality reason to exclude them.

## Tool-selection guidance

Use spreadsheet tools, charting tools, presentation tools, statistical tools, or data-analysis tools when the source table and bin counts remain reviewable.
Use a validated analysis path or independent verification for formal-review, audit, or high-risk evidence.
Do not require a named product.

## Chart construction steps

1. Confirm the data is numeric and uses one unit.
2. Confirm observations come from one defined period and scope.
3. Count the sample size.
4. Inspect the minimum, maximum, and possible outliers.
5. Choose a bin width and record the rationale.
6. Count observations in each bin.
7. Draw adjacent bars with no gaps between intervals unless the tool convention requires a small visual separation.
8. Label the horizontal axis with measurement units and the vertical axis with frequency.
9. Add source note, sample size, date range, scope, and binning note.
10. Write an interpretation that describes shape and limits without claiming process stability.

## Formatting standard

Use a clear title, correct chart type, readable labels, source note, correct scale, suitable bins, visible outliers, and defensible interpretation.
Avoid distorted axes, decorative effects, and bins that hide important variation.

## Required annotations

- Measurement name and unit.
- Source data.
- Date range or observation period.
- Scope or filters.
- Sample size.
- Bin-width or interval note.
- Exclusions.
- Key observation.
- Evidence level and review status when used as final project material.

## Interpretation rules

Safe interpretations describe center, spread, shape, gaps, clusters, skew, and outliers.
Unsafe interpretations claim that the process is stable, that a cause is proven, or that a countermeasure worked without additional evidence.
Before/after comparisons need matching measurement rules, scope, period logic, and binning choices.

## Common chart defects

- Nonnumeric data plotted as if numeric.
- Missing sample size.
- Bin width too wide to show shape.
- Bin width too narrow for the sample size.
- Outliers hidden or removed without rationale.
- Mixed products, shifts, locations, or periods without explanation.
- Claiming process stability from distribution shape alone.

## Quality standards

The histogram should have one numeric measure, consistent units, appropriate bins, readable labels, visible outliers, source context, and cautious interpretation.
The guide or chart note should explain why the binning is suitable for the project question.

## Interpretation guide

Start by reading the axis units and sample size.
Look at where observations concentrate, how wide the spread is, whether the shape is skewed, whether there are multiple peaks, and whether outliers need investigation.
Use the chart to decide whether to stratify, collect more data, investigate outliers, or compare after a countermeasure.

Safe conclusions:

- "Most observations fall between `[range]` during `[period]`."
- "The distribution is wider than the team expected, so the next step is to stratify by `[factor]`."
- "One outlier is visible and needs source-data review before interpretation."
- "This histogram describes variation; it does not prove process stability."

Unsafe overclaims:

- Do not claim stability from a histogram alone.
- Do not claim a before/after improvement unless scope and measurement rules match.
- Do not hide outliers to make the chart look cleaner.
- Do not use generated images as final histogram evidence.

## Example conclusion wording

- "The current distribution is concentrated around `[range]`, with visible spread from `[low]` to `[high]`."
- "The chart suggests possible stratification by `[factor]`; the team will check that before choosing a countermeasure."
- "This histogram is useful for current-state understanding, but it does not prove the process is stable."

## Common mistakes

- Using a histogram for categories instead of numeric observations.
- Reporting only the average and ignoring spread.
- Choosing bins that make the chart support a preferred story.
- Comparing before/after histograms with different bin widths or scopes.
- Removing outliers without a documented reason.
- Treating the chart as proof of stability or root cause.

## Review checklist

Use this checklist before treating a histogram as official QCC project material.

| Check | Pass | Fail | Notes |
|---|---|---|---|
| observations are numeric |  |  |  |
| one measurement unit is used |  |  |  |
| date range and scope are recorded |  |  |  |
| sample size is visible |  |  |  |
| bin width is suitable and documented |  |  |  |
| outliers are visible or exclusion is justified |  |  |  |
| labels and units are readable |  |  |  |
| source data and exclusions are recorded |  |  |  |
| interpretation avoids stability, root-cause, or improvement overclaims |  |  |  |
| evidence note includes reviewer and review status |  |  |  |

Review result:

- Reviewer:
- Review date:
- Review status:
- Required fixes:

## Evidence note for final charts

For final data-dependent charts, complete this evidence note when the histogram is being prepared for project use.

Evidence note fields:

- Method: Histogram
- QCC stage:
- Chart title:
- Numeric measure:
- Unit:
- Source data:
- Data owner:
- Date range:
- Scope / filters:
- Sample size:
- Bin-width rationale:
- Tool used:
- Calculation table location:
- Assumptions:
- Exclusions:
- Reviewer:
- Review date:
- Review status:

## Image-assisted demonstration notes

Image-assisted material for this method is conceptual only.
Generated visuals must not include exact counts, fake percentages, misleading axes, process-stability claims, or final-evidence claims.
Generated visuals are not final evidence.
Detailed method instructions stay in Markdown.

Expected M2 teaching visuals:

- Conceptual distribution with bins, spread, outlier, and sample-size note.
- Good-versus-weak histogram comparison showing bin-width, labeling, source note, and interpretation defects.

## Related methods

- Check Sheet: collect numeric observations before making the histogram.
- Flowchart / Process Map: identify where in the process the numeric measurement should be taken.
- Pareto Chart: prioritize counted categories before measuring numeric variation.
- Scatter Diagram: explore whether the numeric measure appears related to another variable.
- 5 Whys: investigate a visible outlier or distribution pattern after confirming the data.
