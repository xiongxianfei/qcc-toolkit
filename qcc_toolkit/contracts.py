"""Shared first-slice contracts for validation, parameters, and warnings."""

from dataclasses import dataclass
from enum import StrEnum

from qcc_toolkit.stages import QccStage


class WarningCategory(StrEnum):
    """Warning categories required by the first-slice evidence contract."""

    VALIDATION_ERROR = "validation_error"
    DATA_CAUTION = "data_caution"
    EXPORT_SKIPPED = "export_skipped"
    INTERPRETATION_CAUTION = "interpretation_caution"


@dataclass(frozen=True)
class QccWarning:
    """Structured warning emitted by validation, interpretation, or export code."""

    category: WarningCategory
    code: str
    message: str


@dataclass(frozen=True)
class ParetoParameters:
    """Column and context settings for Pareto validation and calculation."""

    category_column: str
    count_column: str | None = None
    qcc_stage: str = QccStage.UNDERSTAND_CURRENT_CONDITION.value


class ParetoValidationError(ValueError):
    """Raised when Pareto input data cannot produce valid evidence."""

    def __init__(self, message: str, code: str = "pareto_validation_error") -> None:
        super().__init__(message)
        self.warning = QccWarning(
            category=WarningCategory.VALIDATION_ERROR,
            code=code,
            message=message,
        )


__all__ = [
    "ParetoParameters",
    "ParetoValidationError",
    "QccWarning",
    "WarningCategory",
]
