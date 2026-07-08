from qcc_toolkit.methods import MethodType, get_method


def test_pareto_is_first_complete_data_chart_method() -> None:
    pareto = get_method("pareto_chart")

    assert pareto.method_type is MethodType.DATA_CHART
    assert pareto.supports_generated_chart is True
    assert pareto.first_slice_status == "supported"


def test_template_guided_methods_have_first_slice_metadata() -> None:
    for method_id in ("check_sheet", "5w2h", "fishbone_diagram", "5_whys"):
        method = get_method(method_id)

        assert method.method_type is MethodType.TEMPLATE_GUIDED
        assert method.supports_generated_chart is False
        assert method.first_slice_status == "template_guided"
        assert method.qcc_stages
