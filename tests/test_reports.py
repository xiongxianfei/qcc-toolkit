import json
from pathlib import Path

from qcc_toolkit.reports import build_qcc_project_report


def _write_evidence_package(evidence_dir: Path) -> None:
    evidence_dir.mkdir(parents=True)
    (evidence_dir / "chart.html").write_text("<html>chart</html>")
    (evidence_dir / "chart-spec.json").write_text("{}\n")
    (evidence_dir / "calculated-table.csv").write_text("rank,category,count\n")
    (evidence_dir / "caption.md").write_text(
        "Wrong label is the largest contributor.\n"
    )
    (evidence_dir / "warnings.json").write_text(
        json.dumps(
            [
                {
                    "category": "export_skipped",
                    "code": "png_export_skipped",
                    "message": (
                        "PNG export was skipped: PNG exporter is not configured."
                    ),
                }
            ]
        )
        + "\n"
    )
    (evidence_dir / "metadata.json").write_text(
        json.dumps(
            {
                "method_id": "pareto_chart",
                "authoritative_record": "evidence_package",
                "slide_edit_authority": "presentation_only",
            }
        )
        + "\n"
    )
    (evidence_dir / "README.md").write_text("# Pareto Evidence Package\n")


def test_project_report_references_evidence_artifacts_and_warnings(
    tmp_path: Path,
) -> None:
    project = tmp_path / "project"
    evidence_dir = project / "evidence" / "pareto"
    report_dir = project / "report"
    _write_evidence_package(evidence_dir)

    report = build_qcc_project_report(evidence_dir, report_dir)

    assert report.markdown_path == report_dir / "report.md"
    assert report.html_path == report_dir / "report.html"

    markdown = (report_dir / "report.md").read_text()
    assert "../evidence/pareto/chart.html" in markdown
    assert "../evidence/pareto/calculated-table.csv" in markdown
    assert "../evidence/pareto/caption.md" in markdown
    assert "../evidence/pareto/warnings.json" in markdown
    assert "../evidence/pareto/metadata.json" in markdown
    assert "../evidence/pareto/README.md" in markdown
    assert "PNG export was skipped" in markdown
    assert "authoritative calculation record" in markdown
    assert "presentation artifacts" in markdown

    html = (report_dir / "report.html").read_text()
    assert "<!doctype html>" in html
    assert "../evidence/pareto/chart.html" in html
    assert "PNG export was skipped" in html
