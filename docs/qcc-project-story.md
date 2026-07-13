# QCC Project Story

Status: draft
Guide version: 0.1.0

## Purpose

A QCC project should read as one connected improvement story, not as a folder of unrelated charts.
This guide shows how the common QCC stages connect method choices, evidence, interpretation, and review.

Markdown method guides govern method knowledge.
Generated or teaching images are conceptual aids only.
Final charts need source data, scope, assumptions, interpretation, and review status.

Use this guide before selecting a new method or chart type.
Do not start with a chart type before the project question is clear.

## Project story map

| Story step | Project question | Typical methods | Evidence handoff |
|---|---|---|---|
| Problem selection | Which problem is worth working on now? | 5W2H, Check Sheet, Pareto Chart | Problem statement, baseline scope, selection reason |
| Current-state grasp | What is happening, where, when, and how often? | Check Sheet, Pareto Chart, Flowchart / Process Map, Histogram | Baseline data, period, scope, observed pattern |
| Cause analysis | Why is the current condition happening? | Fishbone Diagram, 5 Whys, Pareto Chart for focused categories, Scatter Diagram | Cause hypotheses, checked facts, analysis limits |
| Countermeasure planning | What action will address the likely cause? | 5W2H, action tables, risk checks | Owner, action, due date, expected mechanism |
| Verification | Did the countermeasure change the result? | Before/after Check Sheet, Pareto Chart, Histogram, Scatter Diagram | Comparable before/after evidence and interpretation |
| Standardization and control | How will the team hold the gain? | Standard work, checklist, visual control, monitoring plan | New standard, monitoring plan, owner, review cadence |

## Problem selection

Problem selection turns many possible issues into one focused QCC theme.
The team should name the customer, process, product, location, time period, and observed impact.

Good problem selection usually uses simple facts first:

- 5W2H to frame what is known and unknown.
- Check Sheet to collect first observations.
- Pareto Chart when counted categories help select the focus.

The output is not a solution.
It is a justified problem statement with scope and baseline reason.

## Current-state grasp

Current-state grasp asks what is actually happening before the team argues about causes.
The team should collect enough data to describe the current condition without overstating precision.

Use Check Sheet when the team needs structured counting at the worksite.
Use Pareto Chart when the team already has clean category counts from one consistent period and scope.
Use [Flowchart / Process Map](../method-kits/flowchart.md) when the key uncertainty is process sequence, handoff, queue, rework, or decision flow.
Use [Histogram](../method-kits/histogram.md) when numeric data needs review for numeric spread, shape, or outlier behavior.

The output should include source data, date range, scope or filters, total count or sample size, and any known data-quality limits.

## Cause analysis

Cause analysis connects the current-state pattern to plausible reasons.
Fishbone Diagram helps the team organize possible causes.
5 Whys helps test a focused causal chain.
Pareto Chart can help decide which category deserves deeper cause analysis, but it does not prove root cause.
Use [Scatter Diagram](../method-kits/scatter-diagram.md) only when paired numeric variables appear related and the team needs to decide whether a relationship is worth deeper cause analysis.
Scatter Diagram does not prove root cause.

Do not treat the tallest Pareto bar as root cause.
Do not accept a cause because it is easy to act on.
Record which facts support the cause hypothesis and which assumptions still need checking.

The output should distinguish observed facts, suspected causes, rejected causes, and remaining unknowns.

## Countermeasure planning

Countermeasure planning turns a checked cause hypothesis into a controlled action.
The plan should explain why the action should affect the cause, not only who will do what.

Use 5W2H to make the action concrete:

- What will change.
- Why the action addresses the cause.
- Where it applies.
- When it starts and when it will be checked.
- Who owns the action.
- How the team will implement and verify it.
- How much resource, effort, or risk is expected when that is relevant.

Do not treat an action list as verified improvement.
An action plan is only a planned intervention until comparable evidence shows the result.

## Verification

Verification checks whether the countermeasure changed the result under a comparable scope.
Before/after comparisons should use the same category definitions, period logic, process scope, and measurement method unless the guide explicitly records the difference.

Use Check Sheet or Pareto Chart for simple post-action counting when the measurement question is categorical.
Use [Histogram](../method-kits/histogram.md) for numeric before/after distribution comparison when the measurement scope and binning are comparable.
Histogram does not prove process stability.
Use [Scatter Diagram](../method-kits/scatter-diagram.md) when paired numeric variables appear related and the team needs to check whether the relationship changed under a comparable scope.

The output should state what changed, what did not change, whether the evidence is comparable, and what follow-up is needed.

## Standardization and control

Standardization turns a verified improvement into normal work.
The team should update the work standard, training material, checklist, handoff rule, visual control, or monitoring routine that keeps the result from drifting.

The output should identify the new standard, owner, effective date, training or communication action, monitoring cadence, and trigger for reopening the problem.

## Evidence handoff

Every stage should leave enough evidence for the next stage to use safely.

| Handoff | Minimum evidence |
|---|---|
| Problem selection to current-state grasp | Problem statement, scope, reason for focus, known data gaps |
| Current-state grasp to cause analysis | Source data, date range, scope, counts or observations, safe interpretation |
| Cause analysis to countermeasure planning | Checked cause hypothesis, supporting facts, assumptions, rejected causes |
| Countermeasure planning to verification | Action owner, due date, expected mechanism, verification method |
| Verification to standardization | Before/after result, comparability notes, remaining risk |
| Standardization to next project | New standard, monitoring plan, review cadence, unresolved follow-ups |

Final charts and worksheets should carry the relevant evidence level and review status from the evidence guidance.
Generated visuals remain conceptual teaching aids and do not replace source data, construction choices, interpretation, or review evidence.

## Review checklist

Use this checklist when reviewing a QCC project story.

| Check | Pass | Fail | Notes |
|---|---|---|---|
| problem statement names scope, impact, and reason for focus |  |  |  |
| current-state evidence uses a defined period and source |  |  |  |
| method choices match the project question |  |  |  |
| cause analysis distinguishes facts from assumptions |  |  |  |
| countermeasures explain how they address the likely cause |  |  |  |
| verification uses comparable before/after evidence or states limits |  |  |  |
| standardization names the new standard, owner, and monitoring cadence |  |  |  |
| final charts preserve source data, scope, assumptions, interpretation, and review status |  |  |  |

Review result:

- Reviewer:
- Review date:
- Review status:
- Required fixes:

## Method links

- [Pareto Chart](../method-kits/pareto-chart.md)
- [Flowchart / Process Map](../method-kits/flowchart.md)
- [Histogram](../method-kits/histogram.md)
- [Scatter Diagram](../method-kits/scatter-diagram.md)
- [Check Sheet](../method-kits/check-sheet.md)
- [Fishbone Diagram](../method-kits/fishbone-diagram.md)
- [5 Whys](../method-kits/five-whys.md)
- [5W2H](../method-kits/five-w-two-h.md)
- [Evidence levels](evidence/evidence-levels.md)
- [Evidence note template](evidence/evidence-note-template.md)
- [Chart quality standard](chart-creation/chart-quality-standard.md)
