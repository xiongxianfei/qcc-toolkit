import json
import subprocess
import sys
from pathlib import Path


def test_pareto_script_regenerates_synthetic_evidence(tmp_path: Path) -> None:
    project = Path("examples/projects/reduce-packing-label-errors")
    output = tmp_path / "project" / "evidence" / "pareto"

    result = subprocess.run(
        [
            sys.executable,
            "examples/scripts/generate_pareto.py",
            "--input",
            str(project / "data" / "packing_label_defects.csv"),
            "--category-column",
            "defect_type",
            "--count-column",
            "count",
            "--project",
            str(tmp_path / "project"),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert str(output) in result.stdout
    expected = {
        "chart.html",
        "chart-spec.json",
        "calculated-table.csv",
        "caption.md",
        "warnings.json",
        "metadata.json",
        "README.md",
        "report.md",
    }
    assert expected.issubset({path.name for path in output.iterdir()})

    metadata = json.loads((output / "metadata.json").read_text())
    assert metadata["method_id"] == "pareto_chart"
    assert metadata["status"] == "success"
    assert metadata["source_data"].endswith("packing_label_defects.csv")


def test_pareto_script_rejects_missing_required_column(tmp_path: Path) -> None:
    input_path = tmp_path / "bad.csv"
    output = tmp_path / "project" / "evidence" / "pareto"
    input_path.write_text("wrong_column,count\nWrong label,4\n")

    result = subprocess.run(
        [
            sys.executable,
            "examples/scripts/generate_pareto.py",
            "--input",
            str(input_path),
            "--category-column",
            "defect_type",
            "--count-column",
            "count",
            "--project",
            str(tmp_path / "project"),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "defect_type" in result.stderr
    assert not (output / "metadata.json").exists()
