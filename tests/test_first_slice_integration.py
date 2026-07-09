import json
import subprocess
import sys
from pathlib import Path


def test_script_generates_project_report_ready_outputs(tmp_path: Path) -> None:
    example = Path("examples/projects/reduce-packing-label-errors")
    project = tmp_path / "project"
    output = project / "evidence" / "pareto"

    result = subprocess.run(
        [
            sys.executable,
            "examples/scripts/generate_pareto.py",
            "--input",
            str(example / "data" / "packing_label_defects.csv"),
            "--category-column",
            "defect_type",
            "--count-column",
            "count",
            "--project",
            str(project),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    report_markdown = project / "report" / "report.md"
    report_html = project / "report" / "report.html"
    assert report_markdown.exists()
    assert report_html.exists()

    markdown = report_markdown.read_text()
    assert "evidence/pareto/chart.html" in markdown
    assert "evidence/pareto/calculated-table.csv" in markdown
    assert "evidence/pareto/warnings.json" in markdown
    assert "evidence/pareto/metadata.json" in markdown
    assert "optional aids alongside the method kit" in markdown
    assert "authoritative calculation record" in markdown

    metadata = json.loads((output / "metadata.json").read_text())
    assert metadata["authoritative_record"] == "evidence_package"
    assert metadata["slide_edit_authority"] == "presentation_only"
