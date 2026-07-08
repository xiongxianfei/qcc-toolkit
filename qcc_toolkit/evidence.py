"""Evidence package writing for QCC method outputs."""

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from json import dumps
from pathlib import Path

import plotly.graph_objects as go  # type: ignore[import-untyped]

from qcc_toolkit.analysis import ParetoResult
from qcc_toolkit.charts import (
    ChartInputContext,
    ParetoChartSpec,
    build_pareto_chart_spec,
)
from qcc_toolkit.contracts import QccWarning, WarningCategory
from qcc_toolkit.interpretation import build_pareto_interpretation
from qcc_toolkit.reports import build_pareto_markdown_report

PngExporter = Callable[[ParetoChartSpec], bytes]

_METHOD_OWNED_FILES = (
    "chart.html",
    "chart.png",
    "chart-spec.json",
    "calculated-table.csv",
    "caption.md",
    "warnings.json",
    "metadata.json",
    "README.md",
    "report.md",
)


class EvidencePackageError(RuntimeError):
    """Raised when an evidence package cannot be written safely."""


@dataclass(frozen=True)
class RenderedChartArtifacts:
    """Files and warnings produced by chart rendering."""

    files: dict[str, str]
    warnings: tuple[QccWarning, ...] = ()


@dataclass(frozen=True)
class EvidencePackage:
    """Method-scoped evidence package manifest."""

    method_id: str
    output_path: str
    files: dict[str, str]
    warnings: tuple[QccWarning, ...]
    metadata: dict[str, object]


def render_pareto_chart_artifacts(
    spec: ParetoChartSpec,
    output_dir: Path,
    *,
    include_png: bool = False,
    png_exporter: PngExporter | None = None,
) -> RenderedChartArtifacts:
    """Render Pareto chart artifacts from a chart spec."""

    output_dir.mkdir(parents=True, exist_ok=True)
    html = _render_plotly_html(spec)
    (output_dir / "chart.html").write_text(html)

    files = {"interactive_html": "chart.html"}
    warnings: list[QccWarning] = []
    if include_png:
        if png_exporter is None:
            warnings.append(_png_skipped_warning("PNG exporter is not configured."))
        else:
            try:
                (output_dir / "chart.png").write_bytes(png_exporter(spec))
                files["static_png"] = "chart.png"
            except Exception as exc:  # pragma: no cover - defensive integration path
                warnings.append(_png_skipped_warning(str(exc)))

    return RenderedChartArtifacts(files=files, warnings=tuple(warnings))


def write_pareto_evidence_package(
    result: ParetoResult,
    output_dir: Path,
    *,
    input_context: ChartInputContext | None = None,
    include_png: bool = False,
    png_exporter: PngExporter | None = None,
    overwrite: bool = False,
) -> EvidencePackage:
    """Write a method-scoped Pareto evidence package."""

    if output_dir.exists() and any(output_dir.iterdir()):
        if not overwrite:
            raise EvidencePackageError(
                f"Output folder '{output_dir}' already contains files; pass "
                "overwrite=True to replace method-owned generated files."
            )
        _remove_method_owned_files(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    spec = build_pareto_chart_spec(result, input_context=input_context)
    interpretation = build_pareto_interpretation(result)
    rendered = render_pareto_chart_artifacts(
        spec,
        output_dir,
        include_png=include_png,
        png_exporter=png_exporter,
    )
    warnings = tuple(result.warnings) + interpretation.warnings + rendered.warnings

    files = {
        **rendered.files,
        "chart_spec": "chart-spec.json",
        "calculated_table": "calculated-table.csv",
        "caption": "caption.md",
        "warnings": "warnings.json",
        "metadata": "metadata.json",
        "readme": "README.md",
        "report_markdown": "report.md",
    }
    metadata = _metadata_for(result, spec, output_dir)

    _write_json(output_dir / "chart-spec.json", spec.to_dict())
    (output_dir / "calculated-table.csv").write_text(_calculated_table_csv(result))
    (output_dir / "caption.md").write_text(interpretation.caption + "\n")
    _write_json(output_dir / "warnings.json", warnings_to_jsonable(warnings))
    _write_json(output_dir / "metadata.json", metadata)
    (output_dir / "README.md").write_text(_readme_for(files))
    (output_dir / "report.md").write_text(
        build_pareto_markdown_report(files, interpretation.caption)
    )

    return EvidencePackage(
        method_id=result.method_id,
        output_path=str(output_dir),
        files=files,
        warnings=warnings,
        metadata=metadata,
    )


def warnings_to_jsonable(warnings: Iterable[QccWarning]) -> list[dict[str, str]]:
    """Serialize warnings with machine-readable categories."""

    return [
        {
            "category": warning.category.value,
            "code": warning.code,
            "message": warning.message,
        }
        for warning in warnings
    ]


def _render_plotly_html(spec: ParetoChartSpec) -> str:
    bar = spec.series[0]
    line = spec.series[1]
    figure = go.Figure()
    figure.add_bar(x=list(bar.x), y=list(bar.y), name=bar.name)
    figure.add_scatter(
        x=list(line.x),
        y=list(line.y),
        name=line.name,
        yaxis="y2",
        mode="lines+markers",
    )
    figure.update_layout(
        title=spec.title,
        yaxis={"title": "Count"},
        yaxis2={
            "title": "Cumulative %",
            "overlaying": "y",
            "side": "right",
            "range": [0, 100],
        },
    )
    return _remove_plotly_cdn_urls(
        str(figure.to_html(full_html=True, include_plotlyjs=True))
    )


def _png_skipped_warning(reason: str) -> QccWarning:
    return QccWarning(
        category=WarningCategory.EXPORT_SKIPPED,
        code="png_export_skipped",
        message=f"PNG export was skipped: {reason}",
    )


def _remove_plotly_cdn_urls(html: str) -> str:
    return html.replace("https://cdn.plot.ly", "plotly-local")


def _metadata_for(
    result: ParetoResult, spec: ParetoChartSpec, output_dir: Path
) -> dict[str, object]:
    return {
        "status": "success",
        "method_id": result.method_id,
        "qcc_stage": result.qcc_stage,
        "source_data": spec.input_context.source_data,
        "filters": spec.input_context.filters or {},
        "selected_columns": spec.selected_columns,
        "parameters": spec.parameters,
        "toolkit_version": spec.run_metadata.toolkit_version,
        "chart_spec_version": spec.run_metadata.chart_spec_version,
        "calculation_version": spec.run_metadata.calculation_version,
        "output_path": str(output_dir),
        "authoritative_record": "evidence_package",
        "slide_edit_authority": "presentation_only",
    }


def _remove_method_owned_files(output_dir: Path) -> None:
    for filename in _METHOD_OWNED_FILES:
        path = output_dir / filename
        if path.exists() and path.is_file():
            path.unlink()


def _calculated_table_csv(result: ParetoResult) -> str:
    lines = [
        "rank,category,count,percentage,cumulative_count,cumulative_percentage",
    ]
    for row in result.rows:
        lines.append(
            ",".join(
                [
                    str(row.rank),
                    _csv_cell(row.category),
                    f"{row.count:g}",
                    f"{row.percentage:g}",
                    f"{row.cumulative_count:g}",
                    f"{row.cumulative_percentage:g}",
                ]
            )
        )
    return "\n".join(lines) + "\n"


def _csv_cell(value: str) -> str:
    if any(character in value for character in (",", '"', "\n")):
        return '"' + value.replace('"', '""') + '"'
    return value


def _readme_for(files: Mapping[str, str]) -> str:
    lines = [
        "# Pareto Evidence Package",
        "",
        "Use the generated assets below when filling QCC templates.",
        "The evidence package remains the authoritative calculation record.",
        "",
    ]
    for label, path in sorted(files.items()):
        lines.append(f"- {label}: `{path}`")
    lines.append("")
    return "\n".join(lines)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(dumps(payload, indent=2, sort_keys=True) + "\n")


__all__ = [
    "EvidencePackage",
    "EvidencePackageError",
    "PngExporter",
    "RenderedChartArtifacts",
    "render_pareto_chart_artifacts",
    "warnings_to_jsonable",
    "write_pareto_evidence_package",
]
