import json
from pathlib import Path

import pytest

from qcc_toolkit.analysis import calculate_pareto
from qcc_toolkit.charts import ChartInputContext
from qcc_toolkit.contracts import ParetoParameters, WarningCategory
from qcc_toolkit.evidence import EvidencePackageError, write_pareto_evidence_package


def _pareto_result() -> object:
    return calculate_pareto(
        [
            {"defect_type": "Wrong label", "count": 50},
            {"defect_type": "Smudged print", "count": 30},
            {"defect_type": "Missing barcode", "count": 20},
        ],
        ParetoParameters(category_column="defect_type", count_column="count"),
    )


def test_evidence_package_contains_required_files_and_metadata(tmp_path: Path) -> None:
    package = write_pareto_evidence_package(
        _pareto_result(),
        tmp_path,
        input_context=ChartInputContext(
            source_data="data/packing_label_defects.csv",
            filters={"period": "baseline"},
        ),
        include_png=True,
    )

    expected_files = {
        "chart.html",
        "chart-spec.json",
        "calculated-table.csv",
        "caption.md",
        "warnings.json",
        "metadata.json",
        "README.md",
        "report.md",
    }
    assert expected_files.issubset({path.name for path in tmp_path.iterdir()})
    assert "chart.png" not in {path.name for path in tmp_path.iterdir()}
    assert package.files["chart_spec"] == "chart-spec.json"
    assert package.files["report_markdown"] == "report.md"

    metadata = json.loads((tmp_path / "metadata.json").read_text())
    assert metadata["method_id"] == "pareto_chart"
    assert metadata["qcc_stage"] == "understand_current_condition"
    assert metadata["source_data"] == "data/packing_label_defects.csv"
    assert metadata["filters"] == {"period": "baseline"}
    assert metadata["selected_columns"] == {
        "category": "defect_type",
        "count": "count",
    }
    assert metadata["toolkit_version"] == "0.0.0"
    assert metadata["authoritative_record"] == "evidence_package"
    assert metadata["slide_edit_authority"] == "presentation_only"

    warnings = json.loads((tmp_path / "warnings.json").read_text())
    assert warnings[0]["category"] == WarningCategory.EXPORT_SKIPPED.value
    assert warnings[0]["code"] == "png_export_skipped"
    assert "chart.html" in (tmp_path / "README.md").read_text()
    assert "calculated-table.csv" in (tmp_path / "report.md").read_text()


def test_existing_output_folder_requires_explicit_overwrite(tmp_path: Path) -> None:
    def exporter(_spec: object) -> bytes:
        return b"png-bytes"

    write_pareto_evidence_package(
        _pareto_result(),
        tmp_path,
        include_png=True,
        png_exporter=exporter,
    )
    assert (tmp_path / "chart.png").exists()

    with pytest.raises(EvidencePackageError, match="already contains files"):
        write_pareto_evidence_package(_pareto_result(), tmp_path)

    assert json.loads((tmp_path / "metadata.json").read_text())["status"] == "success"

    write_pareto_evidence_package(_pareto_result(), tmp_path, overwrite=True)
    assert json.loads((tmp_path / "metadata.json").read_text())["status"] == "success"
    assert not (tmp_path / "chart.png").exists()


def test_evidence_outputs_are_reproducible_for_same_inputs(tmp_path: Path) -> None:
    first = tmp_path / "first"
    second = tmp_path / "second"
    result = _pareto_result()
    context = ChartInputContext(source_data="data/packing_label_defects.csv")

    write_pareto_evidence_package(result, first, input_context=context)
    write_pareto_evidence_package(result, second, input_context=context)

    assert (first / "chart-spec.json").read_text() == (
        second / "chart-spec.json"
    ).read_text()
    assert (first / "calculated-table.csv").read_text() == (
        second / "calculated-table.csv"
    ).read_text()
