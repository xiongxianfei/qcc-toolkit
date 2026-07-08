import pytest

from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.contracts import (
    ParetoParameters,
    ParetoValidationError,
    WarningCategory,
)


def test_rejects_empty_input() -> None:
    with pytest.raises(ParetoValidationError, match="empty"):
        calculate_pareto([], ParetoParameters(category_column="defect_type"))


def test_rejects_missing_category_column() -> None:
    with pytest.raises(ParetoValidationError, match="defect_type"):
        calculate_pareto(
            [{"other": "Wrong label"}],
            ParetoParameters(category_column="defect_type"),
        )


@pytest.mark.parametrize(
    ("records", "expected_message"),
    [
        ([{"defect_type": ""}], "blank"),
        ([{"defect_type": "   "}], "blank"),
        ([{"defect_type": None}], "null"),
    ],
)
def test_rejects_blank_or_null_category_values(
    records: list[dict[str, object]], expected_message: str
) -> None:
    with pytest.raises(ParetoValidationError, match=expected_message):
        calculate_pareto(records, ParetoParameters(category_column="defect_type"))


def test_rejects_missing_count_column() -> None:
    with pytest.raises(ParetoValidationError, match="count"):
        calculate_pareto(
            [{"defect_type": "Wrong label"}],
            ParetoParameters(category_column="defect_type", count_column="count"),
        )


@pytest.mark.parametrize(
    ("count", "expected_message"),
    [(-1, "negative"), ("many", "numeric"), (True, "numeric")],
)
def test_rejects_invalid_counts(count: object, expected_message: str) -> None:
    with pytest.raises(ParetoValidationError, match=expected_message):
        calculate_pareto(
            [{"defect_type": "Wrong label", "count": count}],
            ParetoParameters(category_column="defect_type", count_column="count"),
        )


def test_rejects_zero_total_count_without_dividing_by_zero() -> None:
    with pytest.raises(ParetoValidationError, match="zero"):
        calculate_pareto(
            [
                {"defect_type": "Wrong label", "count": 0},
                {"defect_type": "Smudged print", "count": 0},
            ],
            ParetoParameters(category_column="defect_type", count_column="count"),
        )


def test_extra_columns_do_not_change_calculation_input() -> None:
    base = [{"defect_type": "Wrong label", "count": 3}]
    with_extra = [{"defect_type": "Wrong label", "count": 3, "ignored": "x"}]

    assert calculate_pareto(
        base, ParetoParameters(category_column="defect_type", count_column="count")
    ).rows == calculate_pareto(
        with_extra,
        ParetoParameters(category_column="defect_type", count_column="count"),
    ).rows


def test_warning_categories_distinguish_required_warning_types() -> None:
    assert [category.value for category in WarningCategory] == [
        "validation_error",
        "data_caution",
        "export_skipped",
        "interpretation_caution",
    ]
