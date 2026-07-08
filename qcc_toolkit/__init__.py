"""QCC Toolkit public package surface."""

from qcc_toolkit.analysis import ParetoResult, ParetoRow, calculate_pareto
from qcc_toolkit.contracts import (
    ParetoParameters,
    ParetoValidationError,
    QccWarning,
    WarningCategory,
)
from qcc_toolkit.interpretation import (
    ParetoInterpretation,
    build_pareto_interpretation,
)
from qcc_toolkit.methods import FIRST_SLICE_METHODS, MethodDefinition, MethodType
from qcc_toolkit.stages import QCC_STORY_STAGES, QccStage, StageDefinition

__version__ = "0.0.0"

__all__ = [
    "__version__",
    "FIRST_SLICE_METHODS",
    "QCC_STORY_STAGES",
    "MethodDefinition",
    "MethodType",
    "ParetoInterpretation",
    "ParetoParameters",
    "ParetoResult",
    "ParetoRow",
    "ParetoValidationError",
    "QccStage",
    "QccWarning",
    "StageDefinition",
    "WarningCategory",
    "build_pareto_interpretation",
    "calculate_pareto",
]
