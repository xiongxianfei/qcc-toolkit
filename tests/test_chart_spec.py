from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.charts import ChartInputContext, build_pareto_chart_spec
from qcc_toolkit.contracts import ParetoParameters


def test_pareto_chart_spec_is_renderer_independent() -> None:
    result = calculate_pareto(
        [
            {"defect_type": "Wrong label", "count": 50},
            {"defect_type": "Smudged print", "count": 30},
            {"defect_type": "Missing barcode", "count": 20},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )

    spec = build_pareto_chart_spec(
        result,
        input_context=ChartInputContext(
            source_data="data/packing_label_defects.csv",
            filters={"period": "baseline"},
        ),
    )

    assert spec.method_id == "pareto_chart"
    assert spec.qcc_stage == "understand_current_condition"
    assert spec.selected_columns == {
        "category": "defect_type",
        "count": "count",
    }
    assert spec.input_context.source_data == "data/packing_label_defects.csv"
    assert spec.input_context.filters == {"period": "baseline"}
    assert spec.run_metadata.toolkit_version == "0.0.0"
    assert spec.run_metadata.chart_spec_version == "pareto-chart-spec-v1"
    assert [series.kind for series in spec.series] == ["bar", "line"]
    assert spec.series[0].name == "Category count"
    assert spec.series[0].x == ("Wrong label", "Smudged print", "Missing barcode")
    assert spec.series[0].y == (50, 30, 20)
    assert spec.series[1].name == "Cumulative percentage"
    assert spec.series[1].y == (50.0, 80.0, 100.0)
    assert spec.to_dict()["series"][1]["y_axis"] == "secondary"


def test_pareto_chart_spec_is_deterministic() -> None:
    result = calculate_pareto(
        [{"defect_type": "B", "count": 10}, {"defect_type": "A", "count": 10}],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )
    context = ChartInputContext(source_data="data/source.csv")

    assert build_pareto_chart_spec(result, input_context=context).to_dict() == (
        build_pareto_chart_spec(result, input_context=context).to_dict()
    )
