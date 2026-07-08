"""Deterministic summaries for QCC method results."""

from dataclasses import dataclass

from qcc_toolkit.analysis import ParetoResult, ParetoRow
from qcc_toolkit.contracts import QccWarning, WarningCategory


@dataclass(frozen=True)
class ParetoInterpretation:
    """Deterministic Pareto caption, summary, and non-blocking warnings."""

    caption: str
    summary: str
    warnings: tuple[QccWarning, ...] = ()


def build_pareto_interpretation(result: ParetoResult) -> ParetoInterpretation:
    """Build deterministic interpretation text from a Pareto result."""

    warnings: list[QccWarning] = []
    top_row = result.rows[0]

    if len(result.rows) == 1:
        warnings.append(
            QccWarning(
                category=WarningCategory.INTERPRETATION_CAUTION,
                code="pareto_one_category",
                message=(
                    "Pareto result has only one category; do not infer a "
                    "meaningful vital-few comparison."
                ),
            )
        )
        caption = (
            f"Pareto Chart: all {top_row.count:g} observations are in "
            f"'{top_row.category}'."
        )
        summary = (
            "The result has only one category, so it is useful as a count "
            "summary but not as a prioritization comparison."
        )
        return ParetoInterpretation(
            caption=caption,
            summary=summary,
            warnings=tuple(warnings),
        )

    if len(result.rows) > 10:
        warnings.append(
            QccWarning(
                category=WarningCategory.DATA_CAUTION,
                code="pareto_many_categories",
                message=(
                    "Pareto result has more than 10 categories; review whether "
                    "stratification or category grouping is needed."
                ),
            )
        )

    top_rows = _rows_to_threshold(result, threshold=80.0)
    final_top_row = top_rows[-1]
    caption = (
        f"Pareto Chart: {top_row.category} is the top category with "
        f"{top_row.count:g} of {result.total_count:g} observations "
        f"({top_row.percentage:.1f}%). The top {len(top_rows)} categories "
        f"account for {final_top_row.cumulative_count:g} of "
        f"{result.total_count:g} observations "
        f"({final_top_row.cumulative_percentage:.1f}%)."
    )
    summary = (
        f"The top ranked category is '{top_row.category}'. Review the top "
        f"{len(top_rows)} categories before selecting countermeasures."
    )
    return ParetoInterpretation(
        caption=caption,
        summary=summary,
        warnings=tuple(warnings),
    )


def _rows_to_threshold(
    result: ParetoResult, threshold: float
) -> tuple[ParetoRow, ...]:
    selected: list[ParetoRow] = []
    for row in result.rows:
        selected.append(row)
        if row.cumulative_percentage >= threshold:
            break
    return tuple(selected)


__all__ = ["ParetoInterpretation", "build_pareto_interpretation"]
