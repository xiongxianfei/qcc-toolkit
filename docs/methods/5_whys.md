---
method_id: 5_whys
method_name: 5 Whys
qcc_stages:
  - analyze_causes
method_type: template_guided
supports_generated_chart: false
first_slice_status: template_guided
---

# 5 Whys

## Legacy optional-aid note

This guide belongs to the earlier first-slice method-guide surface.
Under the current Markdown-first direction, official method kits live under `method-kits/`.
PowerPoint templates and Python aids are optional execution aids and do not override method-kit guidance.

## Summary

5 Whys traces a problem through repeated why questions to expose a possible root cause.
In the first slice it is a template-guided method.

## Purpose

5 Whys helps a QCC team trace one focused problem or suspected cause through evidence-backed why links.
It produces a root-cause candidate for verification, not automatic proof.

## QCC stage fit

Use it during Analyze Causes for one focused problem or suspected cause at a time.

## When to use

Use 5 Whys when the team can follow a cause chain with observable facts and verification.

## When not to use

Do not use it for broad problems with many independent causes.
Do not stop at a convenient answer that has not been checked.

## Inputs required

Inputs include the problem statement, each why answer, evidence for each link, final suspected root cause, and verification status.

## Outputs produced

The method produces a cause chain and a root-cause candidate for verification or countermeasure design.

## Procedure

1. Start with one problem statement.
2. Ask why it occurred.
3. Record an answer that can be checked.
4. Continue asking why until the chain reaches an actionable cause.
5. Verify the chain with evidence before countermeasures.

## PowerPoint template workflow

1. Open the 5 Whys PowerPoint method template.
2. Review the completed DEMO EXAMPLE - not project evidence slide.
3. Replace the why-chain answers and evidence checks with project facts.
4. Copy the blank working slide or worksheet into the project deck.
5. Record the source, date range, verification status, and prepared-by/date.
6. Use the facilitator checklist before selecting countermeasures.

PowerPoint is enough for teaching, draft, and normal 5 Whys use.

## Blank working slide or worksheet

The blank working slide or worksheet should include the starting problem, why-chain rows, evidence checks, candidate root cause, source, date range, key conclusion, next action, and prepared-by/date.
Keep weak links visible instead of hiding uncertainty.

## Interpretation guidance

The chain is useful when every link is plausible and checked.
If a link cannot be verified, return to data collection or a broader cause method.

## Interpretation patterns

- Cause chain: "The evidence-backed why chain suggests [candidate root cause]."
- Verification status: "[Cause] is verified by [evidence] / still needs [check]."
- Next action: "Verify [link] before choosing a countermeasure."
- Caution wording: "The fifth answer is not automatically the root cause."

## Common mistakes

Common mistakes include branching into several problems, using opinions as answers, and assuming the fifth answer is automatically the root cause.
Other review risks are skipping evidence checks, missing source or date range, stopping at a convenient answer, and treating demo content as project evidence.

## Example

Use the 5 Whys PowerPoint template after a Fishbone branch or Pareto category has been selected for deeper analysis.

## Related methods

Related upstream methods include Fishbone Diagram and Pareto Chart.
Related downstream methods include Poka-Yoke and countermeasure records.

## Formula or logic notes

No first-slice formula is implemented for 5 Whys.
The method is a structured cause-chain worksheet.

## Python assist decision

Python assist is not normally needed for 5 Whys because the method is a template-native reasoning worksheet.
PowerPoint is enough when the output is a training example, draft why chain, or normal QCC project analysis.
Use Python only later if verification evidence comes from a large dataset or if high-rigor claims need reproducible supporting evidence.

## Evidence levels and source notes

- Level 1 teaching/draft: PowerPoint edits are sufficient.
- Level 2 normal QCC project: preserve source, date range, evidence checks, and facilitator checklist evidence.
- Level 3 competition or management review: preserve source records, checklist, and the versioned template used.
- Level 4 audit or high-risk evidence: support data-dependent claims with a reproducible evidence package or another validated analysis path.

## Review checklist

- Confirm the starting problem is narrow.
- Confirm each why answer follows from the previous answer.
- Confirm evidence is recorded for each important link.
- Confirm the final cause is verified before countermeasure selection.
- Confirm the facilitator checklist verifies source, date range, key conclusion, and next action.
