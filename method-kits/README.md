# QCC Method Selection Summary

Use this selector to choose a QCC method by looking at three things together:

1. Current QCC stage.
2. The immediate project question.
3. The available evidence or input.

The rows below are directional navigation, not full instructions. Open the detailed method guide before applying a method, and preserve the method's interpretation limits when reporting the result.

## Quick selection by project question

| Project question | Method direction | Evidence or input needed | Safe boundary |
|---|---|---|---|
| How should observations be collected consistently? | [Check Sheet](check-sheet.md) | Observation purpose, operational definitions, period, scope, categories or units | Records observations; does not prove cause. |
| How does the process actually flow? | [Flowchart / Process Map](flowchart.md) | Process boundaries, observed steps, handoffs, decisions, rework, source facts | Shows sequence and handoffs; does not prove which step caused the problem. |
| Which categories contribute most to the problem? | [Pareto Chart](pareto-chart.md) | Stable categories, counts, consistent period and scope | Prioritizes recorded categories; does not prove root cause. |
| What does the distribution of numeric data look like? | [Histogram](histogram.md) | Numeric observations, unit, sample size, period, scope, bin rationale | Shows distribution and variation; does not prove process stability. |
| Do two measured variables appear related? | [Scatter Diagram](scatter-diagram.md) | Paired numeric observations, variable units, pairing rule, period, scope | Shows an apparent relationship; does not prove causation. |
| What possible causes should be investigated? | [Fishbone Diagram](fishbone-diagram.md) | One precise effect, current-state evidence, context-appropriate categories | Organizes cause hypotheses; does not verify them. |
| How might one suspected causal chain work? | [5 Whys](five-whys.md) | Focused problem or suspected cause, evidence for each link, verification status | Develops a fact-checked causal hypothesis chain; repeated why questions do not prove root cause. |
| How should the problem or action be made concrete? | [5W2H](five-w-two-h.md) | Problem background or selected action, scope, owner or affected roles, timing, impact or resource | Clarifies a problem or action; does not prove the action will work or has worked. |

## Selection by QCC stage

| QCC stage | Primary use | Supporting use | Typical output | Important limitation |
|---|---|---|---|---|
| Problem selection | [5W2H](five-w-two-h.md); [Check Sheet](check-sheet.md); [Pareto Chart](pareto-chart.md) | [Flowchart / Process Map](flowchart.md) when process scope is unclear | Focused problem statement, first observations, baseline focus reason | Selection evidence does not prove root cause or solution effectiveness. |
| Current-state grasp | [Check Sheet](check-sheet.md); [Flowchart / Process Map](flowchart.md); [Pareto Chart](pareto-chart.md); [Histogram](histogram.md) | [5W2H](five-w-two-h.md) for scope clarification | Baseline data, process map, distribution view, observed pattern | Current-state description must not be reported as cause proof. |
| Cause analysis | [Fishbone Diagram](fishbone-diagram.md); [5 Whys](five-whys.md); [Scatter Diagram](scatter-diagram.md) | [Pareto Chart](pareto-chart.md) for focused categories; [Flowchart / Process Map](flowchart.md) for process locations; [Check Sheet](check-sheet.md) or [Histogram](histogram.md) for additional facts | Cause hypotheses, checked facts, relationship clues, rejected assumptions | Hypotheses and apparent relationships require verification before root-cause claims. |
| Countermeasure planning | [5W2H](five-w-two-h.md) | [Fishbone Diagram](fishbone-diagram.md) and [5 Whys](five-whys.md) as source context for the selected cause; [Flowchart / Process Map](flowchart.md) for locating the change | Owner, action, due date, expected mechanism, verification method | Action clarity does not prove the action is correct or effective. |
| Verification | [Check Sheet](check-sheet.md); [Pareto Chart](pareto-chart.md); [Histogram](histogram.md); [Scatter Diagram](scatter-diagram.md) | [Flowchart / Process Map](flowchart.md) for deciding where to observe or compare process change | Comparable before/after evidence and cautious interpretation | Before/after evidence needs comparable scope, definitions, period logic, and measurement rules. |
| Standardization and control | Future sustainment guidance: Standard Work; Visual Control; Monitoring Plan | [Check Sheet](check-sheet.md) or monitoring checklist when later guidance defines the control method | New standard, monitoring plan, owner, cadence, trigger for follow-up | Sustainment guidance is future coverage unless a canonical method guide exists. |

## Roadmap coverage and implementation status

This table covers the accepted QCC method roadmap for the toolkit.
Available guide means a canonical Markdown method guide exists in `method-kits/`.
Optional Python support is separate from guide availability.

| Method or guidance | Guide status | Optional Python support | Link behavior |
|---|---|---|---|
| [5W2H](five-w-two-h.md) | Available guide | No Python assist planned for this worksheet. | Existing canonical guide. |
| SIPOC | Planned | No Python assist planned for this scoping method. | Plain status text until a canonical guide exists. |
| [Flowchart / Process Map](flowchart.md) | Available guide | No Python assist planned for this diagram. | Existing canonical guide. |
| [Check Sheet](check-sheet.md) | Available guide | No Python assist planned for this worksheet. | Existing canonical guide. |
| Sampling | Planned | No Python assist planned until sampling guidance is specified. | Plain status text until a canonical guide exists. |
| Stratification | Planned | No Python assist planned until stratification guidance is specified. | Plain status text until a canonical guide exists. |
| [Pareto Chart](pareto-chart.md) | Available guide | Optional Python evidence package support exists for Pareto. | Existing canonical guide. |
| [Fishbone Diagram](fishbone-diagram.md) | Available guide | No Python assist planned for this diagram. | Existing canonical guide. |
| [5 Whys](five-whys.md) | Available guide | No Python assist planned for this worksheet. | Existing canonical guide. |
| [Histogram](histogram.md) | Available guide | Markdown guide only; no Python chart generator is implemented. | Existing canonical guide. |
| [Scatter Diagram](scatter-diagram.md) | Available guide | Markdown guide only; no Python chart generator is implemented. | Existing canonical guide. |
| Control Chart / SPC | Deferred / advanced | No Python control-chart support is implemented. | Plain status text until separate advanced guidance exists. |
| Process capability | Deferred / advanced | No Python capability support is implemented. | Plain status text until separate advanced guidance exists. |
| Poka-Yoke records | Planned | No Python assist planned until mistake-proofing record guidance is specified. | Plain status text until a canonical guide exists. |
| Standard Work | Future sustainment guidance | No Python assist planned until sustainment guidance is specified. | Plain status text until later sustainment guidance exists. |
| Visual Control | Future sustainment guidance | No Python assist planned until sustainment guidance is specified. | Plain status text until later sustainment guidance exists. |
| Monitoring Plan | Future sustainment guidance | No Python assist planned until sustainment guidance is specified. | Plain status text until later sustainment guidance exists. |

## Selection guardrails

| Method | Safe interpretation boundary |
|---|---|
| [Check Sheet](check-sheet.md) | Records observations; does not prove cause. |
| [Flowchart / Process Map](flowchart.md) | Shows process sequence and handoffs; does not prove which step caused the problem. |
| [Pareto Chart](pareto-chart.md) | Prioritizes recorded categories; does not prove root cause. |
| [Histogram](histogram.md) | Shows distribution and variation; does not prove process stability. |
| [Scatter Diagram](scatter-diagram.md) | Shows an apparent relationship; does not prove causation. |
| [Fishbone Diagram](fishbone-diagram.md) | Organizes cause hypotheses; does not verify them. |
| [5 Whys](five-whys.md) | Develops a fact-checked causal hypothesis chain; repeated why questions do not prove root cause. |
| [5W2H](five-w-two-h.md) | Clarifies a problem or action; does not prove the action will work or has worked. |

## Detailed method links

- [Check Sheet](check-sheet.md)
- [Flowchart / Process Map](flowchart.md)
- [Pareto Chart](pareto-chart.md)
- [Histogram](histogram.md)
- [Scatter Diagram](scatter-diagram.md)
- [Fishbone Diagram](fishbone-diagram.md)
- [5 Whys](five-whys.md)
- [5W2H](five-w-two-h.md)

## Maintenance note

Update this selector in the same change as any method addition, rename, removal, status change, or stage-fit change.
Link only canonical guides that exist under `method-kits/`.
Keep full method procedures, formulas, chart recipes, worked examples, and review checks in the detailed method guides.
Other navigation surfaces should link here instead of maintaining another detailed selection matrix.
