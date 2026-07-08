# Change Explanation: Create QCC Toolkit

## Status

draft

## M1 package scaffold

M1 creates the minimal Python package and quality-gate surface required before later QCC method behavior can be implemented.

The scaffold adds `pyproject.toml`, the `qcc_toolkit` import package, a typed package marker, and an import smoke test.
It does not implement Pareto behavior, method registries, evidence packages, charts, templates, scripts, or reports.

The package metadata follows the approved local-first Python stack decision:

- package name: `qcc-toolkit`;
- import name: `qcc_toolkit`;
- supported Python range: 3.11 through 3.14;
- first-slice runtime dependencies: pandas, Plotly, and Pydantic;
- development checks: pytest, Ruff, and mypy.

The import smoke test exists so M1 has executable proof before later milestones add method behavior.
