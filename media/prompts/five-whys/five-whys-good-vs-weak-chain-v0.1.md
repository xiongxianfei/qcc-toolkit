# Image Prompt: five-whys-good-vs-weak-chain-v0.1.png

This prompt is conceptual only and does not create final project evidence.

## Prompt record path

`media/prompts/five-whys/five-whys-good-vs-weak-chain-v0.1.md`

## Output file

`media/five-whys/five-whys-good-vs-weak-chain-v0.1.png`

## Purpose

Create a conceptual teaching visual for the 5 Whys method.
The image uses a synthetic late-shipment example to contrast a weak blame-based chain with a stronger evidence-supported chain that remains provisional until checked.

## Intended use

Training and explanation only.
Not final project evidence.
Not proof of root cause.
Not a rule that exactly five questions are required.
Not evidence that the example chain explains any real project.

## Final prompt

Create a high-quality educational bitmap illustration for a Quality Control Circle 5 Whys method.
Use a clean professional whiteboard style with two side-by-side panels and readable short labels.

Title: `5 Whys: vague blame vs evidence-supported chain`.

Left panel title: `Weak chain`.
Show a simple downward chain:

- `Problem: Late shipment`
- `Why? People were careless`
- `Why? Not enough attention`

End with a crossed-out person/blame icon labeled `Blame / no evidence`.
Make the weak chain gray and visibly unsupported.

Right panel title: `Stronger chain`.
Show a connected causal chain:

- `Problem: Late shipment`
- `Packing queue exceeded capacity`
- `Peak orders were not leveled`
- `Staffing plan used average volume only`
- `Provisional system cause`

Add green fact-supported check marks on the observed or fact-supported links.
Add a side branch from `Peak orders were not leveled` to `Supplier delay? verify` with an amber question mark.
Use a bottom legend with four status markers: `Fact-supported`, `Needs verification`, `Rejected`, `Open`.

Avoid root cause confirmed, proven, solved, success, verified improvement, final evidence, exact production data, private names, or company names.
Do not imply exactly five questions are required.
Do not present personal blame as an acceptable stopping point.
The visual must remain a conceptual teaching aid only.

## Negative constraints

Do not include real operational data.
Do not include private names, company names, credentials, or production-specific identifiers.
Do not include exact project values.
Do not imply the final answer is verified root cause.
Do not imply exactly five questions are mandatory.
Do not stop at personal blame.
Do not imply that the stronger chain is complete, proven, or sufficient for final countermeasure selection without checking.
Do not render detailed method instructions inside the image.
Keep detailed method instructions in Markdown.

## Conceptual-only policy

This image may teach the difference between a speculative chain and a better supported chain.
It must not be used as evidence that a causal chain is proven.

## Manual review

| Check | Status | Notes |
|---|---|---|
| Conceptual only | pass | Synthetic late-shipment example only; no project context or operational dataset. |
| Text-light | pass | The image uses short cards, status symbols, and a compact legend. |
| Weak versus stronger contrast | pass | Weak side stops at blame and no evidence; stronger side follows process conditions. |
| Branching visible | pass | `Supplier delay? verify` remains a branch rather than being forced into the main chain. |
| Evidence status visible | pass | Legend distinguishes fact-supported, needs verification, rejected, and open status. |
| No exact-five rule | pass | The chain is not presented as exactly five required questions. |
| No private identifiers | pass | No company, department, person, supplier, or production names. |
| No proof claims | pass | The image says `Provisional system cause` and uses verification markers without claiming root-cause proof. |

Review status: passed.
Reviewer: Codex.
Review date: 2026-07-12.
