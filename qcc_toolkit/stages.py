"""Canonical QCC Story stage identifiers."""

from dataclasses import dataclass
from enum import StrEnum


class QccStage(StrEnum):
    """Stable machine-readable QCC Story stage IDs."""

    SELECT_THEME = "select_theme"
    DEFINE_PROBLEM = "define_problem"
    UNDERSTAND_CURRENT_CONDITION = "understand_current_condition"
    SET_TARGET = "set_target"
    ANALYZE_CAUSES = "analyze_causes"
    DEVELOP_COUNTERMEASURES = "develop_countermeasures"
    IMPLEMENT_COUNTERMEASURES = "implement_countermeasures"
    VERIFY_EFFECTS = "verify_effects"
    STANDARDIZE_CONTROL = "standardize_control"
    REFLECT_SHARE = "reflect_share"


@dataclass(frozen=True)
class StageDefinition:
    """Human-facing metadata for a stable QCC stage ID."""

    stage_id: str
    label: str
    aliases: tuple[str, ...] = ()


QCC_STORY_STAGES: tuple[StageDefinition, ...] = (
    StageDefinition(QccStage.SELECT_THEME.value, "Select Theme"),
    StageDefinition(QccStage.DEFINE_PROBLEM.value, "Define Problem"),
    StageDefinition(
        QccStage.UNDERSTAND_CURRENT_CONDITION.value,
        "Understand Current Condition",
        ("Current State Analysis", "Grasp Current Status", "Measure"),
    ),
    StageDefinition(QccStage.SET_TARGET.value, "Set Target"),
    StageDefinition(
        QccStage.ANALYZE_CAUSES.value,
        "Analyze Causes",
        ("Root Cause Analysis", "Analyze"),
    ),
    StageDefinition(QccStage.DEVELOP_COUNTERMEASURES.value, "Develop Countermeasures"),
    StageDefinition(
        QccStage.IMPLEMENT_COUNTERMEASURES.value,
        "Implement Countermeasures",
    ),
    StageDefinition(
        QccStage.VERIFY_EFFECTS.value,
        "Verify Effects",
        ("Check Results", "Effect Confirmation"),
    ),
    StageDefinition(
        QccStage.STANDARDIZE_CONTROL.value,
        "Standardize and Control",
        ("Control", "Standardization"),
    ),
    StageDefinition(QccStage.REFLECT_SHARE.value, "Reflect and Share"),
)


__all__ = ["QCC_STORY_STAGES", "QccStage", "StageDefinition"]
