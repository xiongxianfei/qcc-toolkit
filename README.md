# GitHub Repository Template

<!-- vision:start -->
QCC Toolkit is a template-backed, Python-powered toolkit for building traceable Quality Control Circle project evidence. It helps teams learn and apply QCC methods through reusable PowerPoint method templates, preserve method knowledge through Markdown guides, and generate reliable project charts through Python-based validation, calculation, chart generation, interpretation, and metadata.

Most quality-improvement tooling starts from generic statistics, generic charting, dashboards, or manual office-document preparation. QCC Toolkit starts from the QCC method story and the way QCC teams actually present their work: reusable method templates, project-story slides, and evidence charts.

QCC Toolkit is for QCC facilitators, quality engineers, improvement teams, educators, and analysts who want to keep the convenience of QCC PowerPoint templates while improving the reliability, traceability, and reproducibility of the evidence inserted into them.

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
