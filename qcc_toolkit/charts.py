"""Renderer-independent chart specifications for QCC methods."""

from dataclasses import dataclass
from typing import Any

from qcc_toolkit._version import __version__
from qcc_toolkit.analysis import ParetoResult


@dataclass(frozen=True)
class ChartInputContext:
    """Source-data context preserved with generated chart specifications."""

    source_data: str | None = None
    filters: dict[str, str] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_data": self.source_data,
            "filters": self.filters or {},
        }


@dataclass(frozen=True)
class ChartRunMetadata:
    """Deterministic run metadata needed for reproducibility."""

    toolkit_version: str = __version__
    chart_spec_version: str = "pareto-chart-spec-v1"
    calculation_version: str = "pareto-calculation-v1"

    def to_dict(self) -> dict[str, str]:
        return {
            "toolkit_version": self.toolkit_version,
            "chart_spec_version": self.chart_spec_version,
            "calculation_version": self.calculation_version,
        }


@dataclass(frozen=True)
class ChartSeries:
    """A renderer-independent chart data series."""

    kind: str
    name: str
    x: tuple[str, ...]
    y: tuple[float, ...]
    y_axis: str = "primary"

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "name": self.name,
            "x": list(self.x),
            "y": list(self.y),
            "y_axis": self.y_axis,
        }


@dataclass(frozen=True)
class ParetoChartSpec:
    """Renderer-independent Pareto chart specification."""

    method_id: str
    qcc_stage: str
    title: str
    input_context: ChartInputContext
    selected_columns: dict[str, str | None]
    parameters: dict[str, str | None]
    run_metadata: ChartRunMetadata
    series: tuple[ChartSeries, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "method_id": self.method_id,
            "qcc_stage": self.qcc_stage,
            "title": self.title,
            "input_context": self.input_context.to_dict(),
            "selected_columns": self.selected_columns,
            "parameters": self.parameters,
            "run_metadata": self.run_metadata.to_dict(),
            "series": [series.to_dict() for series in self.series],
        }


def build_pareto_chart_spec(
    result: ParetoResult,
    *,
    input_context: ChartInputContext | None = None,
) -> ParetoChartSpec:
    """Build a deterministic Pareto chart spec from a calculation result."""

    context = input_context or ChartInputContext()
    categories = tuple(row.category for row in result.rows)
    counts = tuple(row.count for row in result.rows)
    cumulative_percentages = tuple(row.cumulative_percentage for row in result.rows)
    selected_columns = {
        "category": result.category_column,
        "count": result.count_column,
    }

    return ParetoChartSpec(
        method_id=result.method_id,
        qcc_stage=result.qcc_stage,
        title="Pareto Chart",
        input_context=context,
        selected_columns=selected_columns,
        parameters=selected_columns.copy(),
        run_metadata=ChartRunMetadata(),
        series=(
            ChartSeries(
                kind="bar",
                name="Category count",
                x=categories,
                y=counts,
                y_axis="primary",
            ),
            ChartSeries(
                kind="line",
                name="Cumulative percentage",
                x=categories,
                y=cumulative_percentages,
                y_axis="secondary",
            ),
        ),
    )


__all__ = [
    "ChartInputContext",
    "ChartRunMetadata",
    "ChartSeries",
    "ParetoChartSpec",
    "build_pareto_chart_spec",
]
