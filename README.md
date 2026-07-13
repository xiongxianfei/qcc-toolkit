# QCC Toolkit

<!-- vision:start -->
QCC Toolkit is a Markdown-first guide system for applying Quality Control Circle methods and creating reviewable QCC project evidence. It helps teams understand, apply, explain, and review QCC methods through clear method documentation, practical manual chart-creation guidance, reviewed teaching visuals, and evidence checklists.

Most quality-improvement tooling starts from a tool: a spreadsheet, a statistics package, a charting library, a dashboard, or a slide deck. QCC Toolkit starts from the QCC method question: what the method is for, when it fits the QCC story, how the output should be made, how it should be interpreted, and how a reviewer can judge whether it is acceptable.

QCC Toolkit is for QCC facilitators, quality engineers, improvement teams, educators, and analysts who need to teach, apply, review, or present QCC methods with clearer guidance and stronger chart-quality discipline.

See [VISION.md](VISION.md) for goals, non-goals, and falsifiability.
<!-- vision:end -->

## Current Guide Surface

The canonical Markdown-first method guides live under `method-kits/`.
Use those guides before using older templates or automation.
Use the [QCC Method Selection Summary](method-kits/README.md) to choose
a method by QCC stage, project question, and available evidence.
Use the [QCC Project Story](docs/qcc-project-story.md) guide to connect
method choices across problem selection, current-state grasp, cause analysis,
countermeasure planning, verification, and standardization.

## Method kits

| Method | Type |
|---|---|
| [QCC Method Selection Summary](method-kits/README.md) | Selector |
| [Pareto Chart](method-kits/pareto-chart.md) | Chart |
| [Flowchart / Process Map](method-kits/flowchart.md) | Diagram |
| [Histogram](method-kits/histogram.md) | Chart |
| [Scatter Diagram](method-kits/scatter-diagram.md) | Chart |
| [Check Sheet](method-kits/check-sheet.md) | Worksheet |
| [Fishbone Diagram](method-kits/fishbone-diagram.md) | Diagram |
| [5 Whys](method-kits/five-whys.md) | Worksheet |
| [5W2H](method-kits/five-w-two-h.md) | Worksheet |

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

## License

Licensed under Apache-2.0.
