# Pareto Chart Template Source Notes

template_id: pareto_chart_method_template
method_id: pareto_chart
asset_kind: pptx_source_notes

DEMO EXAMPLE - not project evidence.

## Method kit sections

Purpose: identify the vital few categories contributing most to the current condition.
QCC stage fit: Understand Current Condition and Analyze Causes.
When to use: counted defect, error, delay, complaint, or event categories.
When not to use: categories are overlapping, time periods are mixed, or the team needs proof of root cause.
Required inputs: category, count, source, date range, filters, and calculation notes.
PowerPoint edit instructions: Right-click chart, choose Edit Data, replace categories and counts, sort descending, and verify formula cells were not overwritten.
Completed demo example: shows sample defect rows and is labeled as not project evidence.
Blank copyable project slide: includes title, chart area, source, date range, key finding, next action, prepared-by, and prepared-date fields.
Interpretation patterns: largest contributor, top-three share, focus decision, next method, and caution wording.
Common mistakes: unsorted bars, overlapping categories, mixed time periods, missing source, overwritten formulas, and demo data used as project evidence.
Facilitator checklist: source visible, date range visible, categories clear, counts sorted, conclusion written, next action identified, and Python assist trigger reviewed.
Python assist decision: use PowerPoint for small draft category-count data; use Python for raw logs, repeated generation, validation-heavy work, or high-rigor evidence.
Evidence/source note: record source, date range, filters, assumptions, calculation notes, template version, and whether Python assist generated or verified the output.

## Slide placeholders

- {{method_name}}
- {{qcc_stage}}
- {{demo_label}}
- {{chart_image}}
- {{calculated_table}}
- {{caption}}
- {{data_context}}
- {{warnings}}

## Presentation pattern

Use these source notes as the reviewable contract for the generated PowerPoint template.
The deck includes a data-entry slide with editable defect categories and counts plus an embedded PowerPoint chart for draft use.
The final slide should show the generated Pareto chart image, calculated table reference, caption, data context, and warnings from the evidence package.
The generated evidence package remains the calculation record.
