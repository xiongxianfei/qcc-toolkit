# Extracted Key Content From Legacy Method Guides

## Status

Extracted from the legacy `docs/methods/` guide surface before removing those source files.
The official Markdown-first method-kit surface lives under `method-kits/`.
PowerPoint templates and Python aids remain optional execution aids and do not override method-kit guidance.

## Check Sheet

Source file removed: `docs/methods/check_sheet.md`

- Method ID: `check_sheet`
- QCC stage: Understand Current Condition
- Method type: template-guided worksheet
- Chart support: no generated chart
- Purpose: collect QCC observations consistently before analysis.
- Primary use: repeatable counts by category, location, shift, time period, or other agreed stratification.
- Avoid when: the observation definition is unclear or collectors cannot collect data consistently.
- Inputs: observation definition, category list, collection period, collector, and tally area.
- Output: completed tally worksheet that can feed Pareto, Histogram, or Stratification.
- Core procedure: define what counts as one observation, define categories and collection context, tally during the agreed period, review totals and collection problems, and convert validated tallies into data for later analysis.
- Interpretation boundary: the sheet shows what happened and how often; it does not prove root cause.
- Common mistakes: changing categories midstream, ambiguous "other" notes, mixed collection periods, missing source or date range, unclear observation definitions, and treating demo content as project evidence.
- Evidence guidance: preserve source, date range, collection rules, filters, checklist evidence, and versioned template or source data when rigor requires it.
- Review checks: clear observation definition, mutually understandable categories, stated collection period, no root-cause overclaiming, and visible source/date/conclusion/next-action review fields.

## Fishbone Diagram

Source file removed: `docs/methods/fishbone_diagram.md`

- Method ID: `fishbone_diagram`
- QCC stage: Analyze Causes
- Method type: template-guided diagram
- Chart support: no generated chart
- Purpose: organize suspected causes for one clearly stated effect before verification.
- Primary use: brainstorm and organize possible causes before evidence checks.
- Avoid when: the effect statement is vague or the team wants to treat listed causes as proof.
- Inputs: effect statement, cause categories, short visible cause labels, and verification detail for selected causes.
- Output: cause map and shortlist of causes needing evidence or verification.
- Core procedure: write one effect statement, select process-fit branches, add short visible causes, keep verification detail in the plan, combine duplicates, mark causes needing evidence, and select follow-up checks or 5 Whys chains.
- Interpretation boundary: a Fishbone Diagram is a structured hypothesis map, not root-cause proof.
- Diagram quality: one effect statement, process-fit branches, testable cause statements, visible verification markers, and evidence/source fields.
- Four-layer structure: effect, branch category, short visible cause, and verification detail.
- Verification marker legend: `[S]` suspected, `[V?]` selected for verification, `[V]` verified, `[X]` rejected.
- Cause wording: use testable statements rather than vague labels or symptoms.
- Common mistakes: listing symptoms as causes, mixing several effects, voting without verification, missing source or date range, unclear effect wording, marking causes verified without evidence, and treating demo content as project evidence.
- Evidence guidance: preserve source, date range or session date, assumptions, verification status, facilitator checklist evidence, and source records for higher-rigor review.
- Review checks: effect statement matches evidence, causes are verifiable, suspected and verified causes are distinguished, next verification actions are recorded, and source/date/conclusion/next action are visible.

## 5 Whys

Source file removed: `docs/methods/5_whys.md`

- Method ID: `5_whys`
- QCC stage: Analyze Causes
- Method type: template-guided worksheet
- Chart support: no generated chart
- Purpose: trace one focused problem or suspected cause through evidence-backed why links.
- Primary use: follow a cause chain with observable facts and verification.
- Avoid when: the problem is broad with many independent causes or the team stops at a convenient unchecked answer.
- Inputs: problem statement, why answers, evidence for each link, final suspected root cause, and verification status.
- Output: cause chain and root-cause candidate for verification or countermeasure design.
- Core procedure: start with one problem statement, ask why it occurred, record a checkable answer, continue until an actionable cause is reached, and verify the chain before countermeasures.
- Interpretation boundary: a why chain is useful when every important link is plausible and checked; the fifth answer is not automatically the root cause.
- Common mistakes: branching into several problems without structure, using opinions as answers, assuming the fifth answer is automatically root cause, skipping evidence checks, missing source or date range, stopping at a convenient answer, and treating demo content as project evidence.
- Evidence guidance: preserve source, date range, evidence checks, facilitator checklist evidence, and source records for higher-rigor review.
- Review checks: narrow starting problem, each answer follows from the prior answer, evidence is recorded for important links, final cause is verified before countermeasure selection, and source/date/conclusion/next action are visible.

## 5W2H

Source file removed: `docs/methods/5w2h.md`

- Method ID: `5w2h`
- QCC stage: Define Problem
- Method type: template-guided worksheet
- Chart support: no generated chart
- Purpose: turn a broad concern into a specific, reviewable problem statement.
- Primary use: clarify a vague, broad, or context-poor problem statement.
- Avoid when: the team has not measured enough facts or is using the method as a substitute for actual measurement.
- Inputs: problem background, observed condition, affected process, time period, people or roles involved, current handling method, and measurable impact.
- Output: structured problem definition that can guide Check Sheet design, Pareto analysis, and target setting.
- Core procedure: answer what, why, where, when, who, how, and how much.
- Interpretation boundary: 5W2H narrows the project to a measurable problem; it does not prove root cause.
- Common mistakes: writing opinions instead of observations, defining the solution inside the problem statement, omitting measurable impact, missing source or date range, mixing several problems, and treating demo content as project evidence.
- Evidence guidance: preserve source, date range, assumptions, facilitator checklist evidence, and source data or records for higher-rigor review.
- Review checks: each W/H answer is specific, the problem statement does not prescribe the countermeasure, measurable impact is stated or marked unknown, follow-up collection is linked when facts are missing, and source/date/conclusion/next action are visible.

## Pareto Chart

Source file removed: `docs/methods/pareto_chart.md`

- Method ID: `pareto_chart`
- QCC stages: Understand Current Condition and Analyze Causes
- Method type: data chart
- Chart support: generated chart supported
- Current official guide: `method-kits/pareto-chart.md`
- Purpose: rank counted categories by frequency so a QCC team can identify the largest contributors to the current condition.
- Primary use: countable defect, error, delay, complaint, or event categories with consistent category definitions.
- Avoid when: categories are undefined, overlapping, created after seeing the answer, or treated as proof of root cause.
- Inputs: event-record data with one row per event and a category column, or category-count data with category and numeric count columns.
- Data rules: counts are non-negative, categories are nonblank, datasets are nonempty, categories are non-overlapping, and collection uses one consistent data period.
- Outputs: calculated table, chart specification, interactive HTML chart, deterministic caption, warnings, metadata, and evidence README or manifest.
- Core procedure: define categories before counting, collect records or counts, validate columns and count values, calculate frequency, percentage, cumulative count, and cumulative percentage, sort descending, and review top categories before selecting the next method.
- Interpretation boundary: Pareto supports a focus decision; it does not prove root cause, process stability, or permanent improvement.
- Chart quality: show source, date range, filters, category definitions, sorting rule, key finding, next action, percent and cumulative percent when used, and formula or calculation checks.
- Common mistakes: mixing unlike categories, double-counting events, hiding stratification, treating rank as proof of root cause, unsorted bars, mixed time periods, overlapping categories, missing counts, overwritten formulas, and demo data presented as evidence.
- Python assist guidance: PowerPoint is enough for training, draft discussion, and small manual category tables; Python assist is appropriate for raw logs, large row counts, repeated generation, complex validation, high-rigor evidence, or reproducible calculation metadata.
- Evidence guidance: preserve source data, calculation table, method checklist, versioned template, and evidence package when needed for competition, management, audit, or high-risk review.
- Review checks: visible data period and source, non-overlapping categories, consistent data period, descending counts, formula integrity, key finding and next action, next method identified, stable category definition, intentional data mode, calculated total matches source, caption and warnings included, and slide refers back to the evidence package.

## Cross-method Rules Preserved

- Treat generated or demo visuals as teaching aids, not final project evidence.
- Preserve source, date range, assumptions, interpretation, and review status for final QCC evidence.
- Keep optional PowerPoint and Python aids secondary to Markdown-first method guidance.
- Do not treat observation counts, cause maps, why chains, action framing, or Pareto rank as proof of root cause.
- Use later evidence checks before selecting countermeasures or claiming improvement.
