"""Report-ready artifacts for generated QCC evidence."""

from collections.abc import Mapping
from dataclasses import dataclass
from html import escape
from json import loads
from os.path import relpath
from pathlib import Path


def build_pareto_markdown_report(files: Mapping[str, str], caption: str) -> str:
    """Build a small report-ready Markdown summary for a Pareto package."""

    lines = [
        "# Pareto Evidence Report",
        "",
        caption,
        "",
        "## Generated assets",
        "",
    ]
    for label, path in sorted(files.items()):
        lines.append(f"- {label}: `{path}`")
    lines.extend(
        [
            "",
            "The evidence package is the authoritative calculation record.",
            "Slides created from these assets are presentation artifacts.",
            "",
        ]
    )
    return "\n".join(lines)


@dataclass(frozen=True)
class QccProjectReport:
    """Generated project-level report artifacts."""

    markdown_path: Path
    html_path: Path


def build_qcc_project_report(evidence_dir: Path, report_dir: Path) -> QccProjectReport:
    """Build report-ready project Markdown and HTML from an evidence package."""

    report_dir.mkdir(parents=True, exist_ok=True)
    markdown = _project_report_markdown(evidence_dir, report_dir)
    markdown_path = report_dir / "report.md"
    html_path = report_dir / "report.html"
    markdown_path.write_text(markdown)
    html_path.write_text(_simple_html_report(markdown))
    return QccProjectReport(markdown_path=markdown_path, html_path=html_path)


def _project_report_markdown(evidence_dir: Path, report_dir: Path) -> str:
    caption = _read_optional_text(evidence_dir / "caption.md").strip()
    warnings = _read_warnings(evidence_dir / "warnings.json")
    metadata = _read_metadata(evidence_dir / "metadata.json")
    method_id = str(metadata.get("method_id", "unknown_method"))

    artifact_paths = {
        "interactive chart": "chart.html",
        "chart specification": "chart-spec.json",
        "calculated table": "calculated-table.csv",
        "caption": "caption.md",
        "warnings": "warnings.json",
        "metadata": "metadata.json",
        "evidence README": "README.md",
    }

    lines = [
        "# QCC Project Report",
        "",
        f"Method: `{method_id}`",
        "",
        "## Evidence Summary",
        "",
        caption or "No caption was generated.",
        "",
        "## Evidence Artifacts",
        "",
    ]
    for label, filename in artifact_paths.items():
        relative_path = _relative_link(report_dir, evidence_dir / filename)
        lines.append(f"- {label}: `{relative_path}`")

    lines.extend(
        [
            "",
            "## Warnings",
            "",
        ]
    )
    if warnings:
        for warning in warnings:
            code = warning.get("code", "unknown_warning")
            message = warning.get("message", "")
            lines.append(f"- `{code}`: {message}")
    else:
        lines.append("- No warnings recorded.")

    lines.extend(
        [
            "",
            "## Slide Use",
            "",
            "Use the linked chart, table, caption, warnings, and metadata when "
            "filling the PowerPoint template.",
            "The evidence package is the authoritative calculation record.",
            "Slides created or edited from these assets are presentation artifacts.",
            "",
        ]
    )
    return "\n".join(lines)


def _simple_html_report(markdown: str) -> str:
    body = "\n".join(
        f"<p>{escape(line)}</p>" if line else "" for line in markdown.splitlines()
    )
    return f"<!doctype html>\n<html><body>\n{body}\n</body></html>\n"


def _relative_link(base_dir: Path, target: Path) -> str:
    return relpath(target, start=base_dir).replace("\\", "/")


def _read_optional_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def _read_warnings(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    payload = loads(path.read_text())
    if not isinstance(payload, list):
        return []
    return [item for item in payload if isinstance(item, dict)]


def _read_metadata(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    payload = loads(path.read_text())
    return payload if isinstance(payload, dict) else {}


__all__ = [
    "QccProjectReport",
    "build_pareto_markdown_report",
    "build_qcc_project_report",
]
