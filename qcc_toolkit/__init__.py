"""QCC Toolkit public package surface."""

from qcc_toolkit._version import __version__
from qcc_toolkit.analysis import ParetoResult, ParetoRow, calculate_pareto
from qcc_toolkit.charts import (
    ChartInputContext,
    ChartRunMetadata,
    ChartSeries,
    ParetoChartSpec,
    build_pareto_chart_spec,
)
from qcc_toolkit.contracts import (
    ParetoParameters,
    ParetoValidationError,
    QccWarning,
    WarningCategory,
)
from qcc_toolkit.evidence import (
    EvidencePackage,
    EvidencePackageError,
    RenderedChartArtifacts,
    render_pareto_chart_artifacts,
    warnings_to_jsonable,
    write_pareto_evidence_package,
)
from qcc_toolkit.interpretation import (
    ParetoInterpretation,
    build_pareto_interpretation,
)
from qcc_toolkit.methods import FIRST_SLICE_METHODS, MethodDefinition, MethodType
from qcc_toolkit.reports import build_pareto_markdown_report
from qcc_toolkit.stages import QCC_STORY_STAGES, QccStage, StageDefinition

__all__ = [
    "__version__",
    "FIRST_SLICE_METHODS",
    "QCC_STORY_STAGES",
    "ChartInputContext",
    "ChartRunMetadata",
    "ChartSeries",
    "EvidencePackage",
    "EvidencePackageError",
    "MethodDefinition",
    "MethodType",
    "ParetoChartSpec",
    "ParetoInterpretation",
    "ParetoParameters",
    "ParetoResult",
    "ParetoRow",
    "ParetoValidationError",
    "QccStage",
    "QccWarning",
    "RenderedChartArtifacts",
    "StageDefinition",
    "WarningCategory",
    "build_pareto_interpretation",
    "build_pareto_chart_spec",
    "build_pareto_markdown_report",
    "calculate_pareto",
    "render_pareto_chart_artifacts",
    "warnings_to_jsonable",
    "write_pareto_evidence_package",
]
