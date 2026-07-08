from qcc_toolkit.methods import FIRST_SLICE_METHODS
from qcc_toolkit.stages import QCC_STORY_STAGES, QccStage


def test_stage_ids_are_stable() -> None:
    assert [stage.stage_id for stage in QCC_STORY_STAGES] == [
        QccStage.SELECT_THEME.value,
        QccStage.DEFINE_PROBLEM.value,
        QccStage.UNDERSTAND_CURRENT_CONDITION.value,
        QccStage.SET_TARGET.value,
        QccStage.ANALYZE_CAUSES.value,
        QccStage.DEVELOP_COUNTERMEASURES.value,
        QccStage.IMPLEMENT_COUNTERMEASURES.value,
        QccStage.VERIFY_EFFECTS.value,
        QccStage.STANDARDIZE_CONTROL.value,
        QccStage.REFLECT_SHARE.value,
    ]


def test_first_slice_method_ids_are_present_and_unique() -> None:
    method_ids = [method.method_id for method in FIRST_SLICE_METHODS]

    assert method_ids == [
        "pareto_chart",
        "check_sheet",
        "5w2h",
        "fishbone_diagram",
        "5_whys",
    ]
    assert len(method_ids) == len(set(method_ids))
