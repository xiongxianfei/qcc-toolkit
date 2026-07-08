"""First-slice QCC method registry."""

from dataclasses import dataclass
from enum import StrEnum

from qcc_toolkit.stages import QccStage

PARETO_CHART = "pareto_chart"
CHECK_SHEET = "check_sheet"
FIVE_W_TWO_H = "5w2h"
FISHBONE_DIAGRAM = "fishbone_diagram"
FIVE_WHYS = "5_whys"


class MethodType(StrEnum):
    """Supported first-slice method implementation styles."""

    DATA_CHART = "data_chart"
    TEMPLATE_GUIDED = "template_guided"


@dataclass(frozen=True)
class MethodDefinition:
    """Stable method metadata shared by docs, templates, and Python."""

    method_id: str
    name: str
    method_type: MethodType
    qcc_stages: tuple[str, ...]
    supports_generated_chart: bool
    first_slice_status: str


FIRST_SLICE_METHODS: tuple[MethodDefinition, ...] = (
    MethodDefinition(
        method_id=PARETO_CHART,
        name="Pareto Chart",
        method_type=MethodType.DATA_CHART,
        qcc_stages=(
            QccStage.UNDERSTAND_CURRENT_CONDITION.value,
            QccStage.ANALYZE_CAUSES.value,
        ),
        supports_generated_chart=True,
        first_slice_status="supported",
    ),
    MethodDefinition(
        method_id=CHECK_SHEET,
        name="Check Sheet",
        method_type=MethodType.TEMPLATE_GUIDED,
        qcc_stages=(QccStage.UNDERSTAND_CURRENT_CONDITION.value,),
        supports_generated_chart=False,
        first_slice_status="template_guided",
    ),
    MethodDefinition(
        method_id=FIVE_W_TWO_H,
        name="5W2H",
        method_type=MethodType.TEMPLATE_GUIDED,
        qcc_stages=(QccStage.DEFINE_PROBLEM.value,),
        supports_generated_chart=False,
        first_slice_status="template_guided",
    ),
    MethodDefinition(
        method_id=FISHBONE_DIAGRAM,
        name="Fishbone Diagram",
        method_type=MethodType.TEMPLATE_GUIDED,
        qcc_stages=(QccStage.ANALYZE_CAUSES.value,),
        supports_generated_chart=False,
        first_slice_status="template_guided",
    ),
    MethodDefinition(
        method_id=FIVE_WHYS,
        name="5 Whys",
        method_type=MethodType.TEMPLATE_GUIDED,
        qcc_stages=(QccStage.ANALYZE_CAUSES.value,),
        supports_generated_chart=False,
        first_slice_status="template_guided",
    ),
)

_METHODS_BY_ID = {method.method_id: method for method in FIRST_SLICE_METHODS}


def get_method(method_id: str) -> MethodDefinition:
    """Return a first-slice method definition by stable method ID."""

    try:
        return _METHODS_BY_ID[method_id]
    except KeyError as exc:
        raise KeyError(f"Unknown QCC method_id: {method_id}") from exc


__all__ = [
    "CHECK_SHEET",
    "FISHBONE_DIAGRAM",
    "FIRST_SLICE_METHODS",
    "FIVE_WHYS",
    "FIVE_W_TWO_H",
    "PARETO_CHART",
    "MethodDefinition",
    "MethodType",
    "get_method",
]
