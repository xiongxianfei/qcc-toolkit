import subprocess
import sys
from pathlib import Path


def test_pareto_script_regeneration_is_reproducible(tmp_path: Path) -> None:
    project = Path("examples/projects/reduce-packing-label-errors")
    outputs = [tmp_path / "first" / "pareto", tmp_path / "second" / "pareto"]

    for output in outputs:
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
                str(tmp_path),
                "--output",
                str(output),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr

    assert (outputs[0] / "calculated-table.csv").read_text() == (
        outputs[1] / "calculated-table.csv"
    ).read_text()
    assert (outputs[0] / "chart-spec.json").read_text() == (
        outputs[1] / "chart-spec.json"
    ).read_text()
