"""Generate a Pareto evidence package from local CSV data."""

from __future__ import annotations

import argparse
import csv
import sys
from collections.abc import Sequence
from pathlib import Path

from qcc_toolkit import (
    ChartInputContext,
    ParetoParameters,
    ParetoValidationError,
    calculate_pareto,
    write_pareto_evidence_package,
)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the Pareto starter script."""

    parser = _build_parser()
    args = parser.parse_args(argv)
    input_path = Path(args.input)
    project_path = Path(args.project)
    output_path = Path(args.output)

    try:
        _validate_paths(input_path, project_path, output_path)
        records = _read_csv_records(
            input_path,
            category_column=args.category_column,
            count_column=args.count_column,
        )
        result = calculate_pareto(
            records,
            ParetoParameters(
                category_column=args.category_column,
                count_column=args.count_column,
            ),
        )
        write_pareto_evidence_package(
            result,
            output_path,
            input_context=ChartInputContext(
                source_data=_source_data_reference(input_path, project_path),
            ),
            overwrite=True,
        )
    except (OSError, ValueError, ParetoValidationError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"Pareto evidence package written to {output_path}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a local Pareto evidence package from CSV data.",
    )
    parser.add_argument("--input", required=True, help="Input CSV data path.")
    parser.add_argument(
        "--category-column",
        required=True,
        help="Column containing defect or issue categories.",
    )
    parser.add_argument(
        "--count-column",
        help="Optional numeric count column. Omit for event-record input.",
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project folder that owns the generated evidence.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Method-scoped output folder for generated evidence.",
    )
    return parser


def _validate_paths(input_path: Path, project_path: Path, output_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input data file does not exist: {input_path}")
    if not input_path.is_file():
        raise ValueError(f"Input data path is not a file: {input_path}")

    project_resolved = project_path.resolve(strict=False)
    output_resolved = output_path.resolve(strict=False)
    if not _is_relative_to(output_resolved, project_resolved):
        raise ValueError(
            f"Output path must be inside the project folder: {output_path}"
        )


def _read_csv_records(
    input_path: Path,
    *,
    category_column: str,
    count_column: str | None,
) -> list[dict[str, object]]:
    with input_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        _validate_columns(
            fieldnames,
            category_column=category_column,
            count_column=count_column,
        )

        records: list[dict[str, object]] = []
        for row_number, row in enumerate(reader, start=2):
            record: dict[str, object] = {
                category_column: row.get(category_column),
            }
            if count_column is not None:
                record[count_column] = _parse_count(
                    row.get(count_column),
                    row_number=row_number,
                    count_column=count_column,
                )
            records.append(record)
    return records


def _validate_columns(
    fieldnames: Sequence[str],
    *,
    category_column: str,
    count_column: str | None,
) -> None:
    missing = [category_column]
    if count_column is not None:
        missing.append(count_column)
    missing = [column for column in missing if column not in fieldnames]
    if missing:
        raise ValueError(
            "Input CSV is missing required column(s): " + ", ".join(missing)
        )


def _parse_count(value: str | None, *, row_number: int, count_column: str) -> float:
    if value is None or not value.strip():
        raise ValueError(
            f"Input CSV row {row_number} has a blank count value in "
            f"'{count_column}'."
        )
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(
            f"Input CSV row {row_number} count in '{count_column}' must be numeric."
        ) from exc


def _source_data_reference(input_path: Path, project_path: Path) -> str:
    input_resolved = input_path.resolve(strict=False)
    project_resolved = project_path.resolve(strict=False)
    if _is_relative_to(input_resolved, project_resolved):
        return input_resolved.relative_to(project_resolved).as_posix()
    return str(input_path)


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    raise SystemExit(main())
