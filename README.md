# QCC Toolkit

<!-- vision:start -->
QCC Toolkit is a Markdown-first guide system for applying Quality Control Circle methods and creating reviewable QCC project evidence. It helps teams understand, apply, explain, and review QCC methods through clear method documentation, practical manual chart-creation guidance, reviewed teaching visuals, and evidence checklists.

Most quality-improvement tooling starts from a tool: a spreadsheet, a statistics package, a charting library, a dashboard, or a slide deck. QCC Toolkit starts from the QCC method question: what the method is for, when it fits the QCC story, how the output should be made, how it should be interpreted, and how a reviewer can judge whether it is acceptable.

QCC Toolkit is for QCC facilitators, quality engineers, improvement teams, educators, and analysts who need to teach, apply, review, or present QCC methods with clearer guidance and stronger chart-quality discipline.

See [VISION.md](VISION.md) for goals, non-goals, and falsifiability.
<!-- vision:end -->

## Current Guide Surface

The canonical Markdown-first Pareto method guide currently lives at
`method-kits/pareto-chart.md`.
Use that guide before using older templates or automation.

## Method kits

| Method | Type | QCC stage |
|---|---|---|
| [Pareto Chart](method-kits/pareto-chart.md) | Chart | Understand Current Condition / Analyze Causes |

PowerPoint templates and Python automation are optional execution aids.
They remain available for teaching, presentation, reproducible calculations,
and historical first-slice compatibility, but they do not override the method
kit or chart-quality standards.

## Local development

QCC Toolkit is packaged as `qcc-toolkit` with the import package
`qcc_toolkit`.

Install the package and development tools in a Python 3.11-3.14 environment:

```sh
python -m pip install -e ".[dev]"
```

Run the baseline checks:

```sh
python -m pytest
python -m ruff check .
python -m mypy qcc_toolkit
```

## First Slice Example

Generate Pareto evidence and a report-ready Markdown/HTML summary from the
synthetic packing-label example:

```sh
python examples/scripts/generate_pareto.py \
  --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv \
  --category-column defect_type \
  --count-column count \
  --project examples/projects/reduce-packing-label-errors \
  --output examples/projects/reduce-packing-label-errors/evidence/pareto
```

The command writes method evidence under `evidence/pareto` and report-ready
project output under `report/`.

## License

Licensed under Apache-2.0.
