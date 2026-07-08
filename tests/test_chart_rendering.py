from pathlib import Path

from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.charts import ChartInputContext, build_pareto_chart_spec
from qcc_toolkit.contracts import ParetoParameters, WarningCategory
from qcc_toolkit.evidence import render_pareto_chart_artifacts


def _chart_spec() -> object:
    result = calculate_pareto(
        [{"defect_type": "Wrong label", "count": 2}],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )
    return build_pareto_chart_spec(
        result,
        input_context=ChartInputContext(source_data="data/source.csv"),
    )


def test_chart_rendering_writes_html_without_png(tmp_path: Path) -> None:
    output = render_pareto_chart_artifacts(_chart_spec(), tmp_path, include_png=False)

    assert (tmp_path / "chart.html").exists()
    assert "Plotly.newPlot" in (tmp_path / "chart.html").read_text()
    assert output.files["interactive_html"] == "chart.html"
    assert "static_png" not in output.files
    assert output.warnings == ()


def test_chart_rendering_records_png_skip_warning(tmp_path: Path) -> None:
    output = render_pareto_chart_artifacts(_chart_spec(), tmp_path, include_png=True)

    assert (tmp_path / "chart.html").exists()
    assert not (tmp_path / "chart.png").exists()
    assert output.files["interactive_html"] == "chart.html"
    assert output.warnings[0].category is WarningCategory.EXPORT_SKIPPED
    assert output.warnings[0].code == "png_export_skipped"


def test_chart_rendering_writes_png_when_exporter_is_available(tmp_path: Path) -> None:
    def exporter(_spec: object) -> bytes:
        return b"png-bytes"

    output = render_pareto_chart_artifacts(
        _chart_spec(),
        tmp_path,
        include_png=True,
        png_exporter=exporter,
    )

    assert (tmp_path / "chart.png").read_bytes() == b"png-bytes"
    assert output.files["static_png"] == "chart.png"
    assert output.warnings == ()
