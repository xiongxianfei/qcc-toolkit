from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.contracts import ParetoParameters, WarningCategory
from qcc_toolkit.interpretation import build_pareto_interpretation


def test_pareto_caption_is_deterministic() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "Wrong label", "count": 50},
            {"defect_type": "Smudged print", "count": 30},
            {"defect_type": "Missing barcode", "count": 20},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    first = build_pareto_interpretation(result)
    second = build_pareto_interpretation(result)

    assert first == second
    assert first.caption == (
        "Pareto Chart: Wrong label is the top category with 50 of 100 "
        "observations (50.0%). The top 2 categories account for 80 of 100 "
        "observations (80.0%)."
    )


def test_one_category_interpretation_avoids_vital_few_language() -> None:
    result = calculate_pareto(
        [{"defect_type": "Wrong label", "count": 10}],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    interpretation = build_pareto_interpretation(result)

    assert "vital few" not in interpretation.caption.lower()
    assert "only one category" in interpretation.summary
    assert [
        warning.category for warning in interpretation.warnings
    ] == [WarningCategory.INTERPRETATION_CAUTION]


def test_many_category_interpretation_records_data_caution() -> None:
    result = calculate_pareto(
        [{"defect_type": f"Defect {index}", "count": 1} for index in range(1, 13)],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    interpretation = build_pareto_interpretation(result)

    assert any(
        warning.category is WarningCategory.DATA_CAUTION
        and warning.code == "pareto_many_categories"
        for warning in interpretation.warnings
    )
