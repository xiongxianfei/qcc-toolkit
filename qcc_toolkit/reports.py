"""Markdown report fragments for generated QCC evidence."""

from collections.abc import Mapping


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


__all__ = ["build_pareto_markdown_report"]
