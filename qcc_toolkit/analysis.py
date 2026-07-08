"""QCC method calculations."""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from math import isfinite
from numbers import Real

from qcc_toolkit.contracts import ParetoParameters, ParetoValidationError, QccWarning
from qcc_toolkit.methods import PARETO_CHART


@dataclass(frozen=True)
class ParetoRow:
    """A single ranked Pareto calculation row."""

    category: str
    count: float
    percentage: float
    cumulative_count: float
    cumulative_percentage: float
    rank: int


@dataclass(frozen=True)
class ParetoResult:
    """Validated Pareto calculation result."""

    method_id: str
    qcc_stage: str
    category_column: str
    count_column: str | None
    total_count: float
    rows: tuple[ParetoRow, ...]
    warnings: tuple[QccWarning, ...] = ()


def calculate_pareto(
    records: Iterable[Mapping[str, object]],
    parameters: ParetoParameters,
) -> ParetoResult:
    """Validate records and calculate Pareto rows.

    Supports category-count input when ``count_column`` is configured and
    event-record input when it is omitted.
    """

    materialized_records = list(records)
    if not materialized_records:
        raise ParetoValidationError(
            "Pareto input dataset is empty.",
            code="pareto_empty_dataset",
        )

    category_counts: dict[str, float] = {}
    for row_number, record in enumerate(materialized_records, start=1):
        category = _read_category(record, parameters.category_column, row_number)
        count = _read_count(record, parameters.count_column, row_number)
        category_counts[category] = category_counts.get(category, 0.0) + count

    total_count = sum(category_counts.values())
    if total_count == 0:
        raise ParetoValidationError(
            "Pareto input has zero total count.",
            code="pareto_zero_total",
        )

    sorted_items = sorted(
        category_counts.items(),
        key=lambda item: (-item[1], item[0].casefold(), item[0]),
    )
    rows: list[ParetoRow] = []
    cumulative_count = 0.0
    for rank, (category, count) in enumerate(sorted_items, start=1):
        cumulative_count += count
        rows.append(
            ParetoRow(
                category=category,
                count=_normalize_number(count),
                percentage=_round_percentage(count, total_count),
                cumulative_count=_normalize_number(cumulative_count),
                cumulative_percentage=_round_percentage(cumulative_count, total_count),
                rank=rank,
            )
        )

    return ParetoResult(
        method_id=PARETO_CHART,
        qcc_stage=parameters.qcc_stage,
        category_column=parameters.category_column,
        count_column=parameters.count_column,
        total_count=_normalize_number(total_count),
        rows=tuple(rows),
    )


def _read_category(
    record: Mapping[str, object], category_column: str, row_number: int
) -> str:
    if category_column not in record:
        raise ParetoValidationError(
            f"Pareto input row {row_number} is missing category column "
            f"'{category_column}'.",
            code="pareto_missing_category_column",
        )

    value = record[category_column]
    if value is None:
        raise ParetoValidationError(
            f"Pareto input row {row_number} has a null category value.",
            code="pareto_null_category",
        )

    category = str(value).strip()
    if not category:
        raise ParetoValidationError(
            f"Pareto input row {row_number} has a blank category value.",
            code="pareto_blank_category",
        )
    return category


def _read_count(
    record: Mapping[str, object], count_column: str | None, row_number: int
) -> float:
    if count_column is None:
        return 1.0

    if count_column not in record:
        raise ParetoValidationError(
            f"Pareto input row {row_number} is missing count column "
            f"'{count_column}'.",
            code="pareto_missing_count_column",
        )

    value = record[count_column]
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ParetoValidationError(
            f"Pareto input row {row_number} count must be numeric.",
            code="pareto_nonnumeric_count",
        )

    count = float(value)
    if not isfinite(count):
        raise ParetoValidationError(
            f"Pareto input row {row_number} count must be finite.",
            code="pareto_nonfinite_count",
        )
    if count < 0:
        raise ParetoValidationError(
            f"Pareto input row {row_number} count must not be negative.",
            code="pareto_negative_count",
        )
    return count


def _round_percentage(part: float, total: float) -> float:
    return round((part / total) * 100.0, 10)


def _normalize_number(value: float) -> float:
    return int(value) if value.is_integer() else value


__all__ = ["ParetoResult", "ParetoRow", "calculate_pareto"]
