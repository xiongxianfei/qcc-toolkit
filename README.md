# GitHub Repository Template

<!-- vision:start -->
QCC Toolkit is a PowerPoint-first, Python-assisted toolkit for applying Quality Control Circle methods and preserving traceable project evidence. It helps teams learn, use, and present QCC methods through practical PowerPoint method kits, keeps method knowledge reviewable through Markdown guides, and uses Python when PowerPoint is weak: complex calculations, validation, large or raw datasets, repeated generation, reproducible charts, and evidence packaging.

Most quality-improvement tooling starts from generic statistics, charting, dashboards, or office-document preparation. QCC Toolkit starts from how QCC teams actually work: they learn methods from templates, discuss them in project slides, copy working examples, and present evidence as part of a QCC story.

QCC Toolkit is for QCC facilitators, quality engineers, improvement teams, educators, and analysts who want the speed and familiarity of reusable PowerPoint templates while improving the clarity, reviewability, and reproducibility of the evidence behind data-dependent conclusions.

See [VISION.md](VISION.md) for goals, non-goals, and falsifiability.
<!-- vision:end -->

A small, language-agnostic template for starting a new GitHub repository with only the essentials.

## Included

- `README.md` — project overview and setup notes
- `LICENSE` — project license
- `CONTRIBUTING.md` — contribution guidelines
- `CODE_OF_CONDUCT.md` — community expectations
- `SECURITY.md` — vulnerability reporting instructions
- `.gitignore` — common local files to ignore

## Use this template

1. Create a new repository from this template.
2. Replace placeholder text with project-specific details.
3. Keep only the files your project will actively maintain.
4. Add tests, scripts, and CI only after the project has real commands to run.

## Recommended repository settings

- Use `main` as the default branch.
- Require pull requests before merging when collaborating.
- Prefer small, focused pull requests.
- Protect important branches from force pushes.

## License

Licensed under Apache-2.0.

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
