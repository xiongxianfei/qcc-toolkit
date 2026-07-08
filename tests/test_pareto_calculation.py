import pytest

from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.contracts import ParetoParameters
from qcc_toolkit.methods import PARETO_CHART


def test_category_count_pareto_matches_known_fixture() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "Wrong label", "count": 50, "ignored": "x"},
            {"defect_type": "Smudged print", "count": 30},
            {"defect_type": "Missing barcode", "count": 15},
            {"defect_type": "Damaged label", "count": 5},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    assert result.method_id == PARETO_CHART
    assert result.total_count == 100
    assert [
        (
            row.rank,
            row.category,
            row.count,
            row.percentage,
            row.cumulative_count,
            row.cumulative_percentage,
        )
        for row in result.rows
    ] == [
        (1, "Wrong label", 50, 50.0, 50, 50.0),
        (2, "Smudged print", 30, 30.0, 80, 80.0),
        (3, "Missing barcode", 15, 15.0, 95, 95.0),
        (4, "Damaged label", 5, 5.0, 100, 100.0),
    ]


def test_event_record_pareto_counts_records_by_category() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "Wrong label"},
            {"defect_type": "Wrong label"},
            {"defect_type": "Smudged print"},
        ],
        ParetoParameters(category_column="defect_type"),
    )

    assert [(row.category, row.count) for row in result.rows] == [
        ("Wrong label", 2),
        ("Smudged print", 1),
    ]
    assert result.total_count == 3
    assert result.count_column is None


def test_ties_sort_by_category_after_descending_count() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "B", "count": 10},
            {"defect_type": "A", "count": 10},
            {"defect_type": "C", "count": 5},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    assert [row.category for row in result.rows] == ["A", "B", "C"]
    assert [row.rank for row in result.rows] == [1, 2, 3]


def test_same_inputs_produce_same_calculation_result() -> None:
    records = [
        {"defect_type": "B", "count": 10},
        {"defect_type": "A", "count": 10},
    ]
    parameters = ParetoParameters(category_column="defect_type", count_column="count")

    assert calculate_pareto(records, parameters) == calculate_pareto(
        records, parameters
    )


def test_percentage_handles_non_integer_counts() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "A", "count": 1.5},
            {"defect_type": "B", "count": 0.5},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    assert result.total_count == pytest.approx(2.0)
    assert result.rows[0].percentage == pytest.approx(75.0)
