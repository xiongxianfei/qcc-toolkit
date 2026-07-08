import json

from qcc_toolkit.contracts import QccWarning, WarningCategory
from qcc_toolkit.evidence import warnings_to_jsonable


def test_warnings_serialize_with_machine_readable_categories() -> None:
    warnings = (
        QccWarning(
            category=WarningCategory.VALIDATION_ERROR,
            code="missing_category",
            message="Category is required.",
        ),
        QccWarning(
            category=WarningCategory.DATA_CAUTION,
            code="many_categories",
            message="Review category grouping.",
        ),
        QccWarning(
            category=WarningCategory.EXPORT_SKIPPED,
            code="png_export_skipped",
            message="PNG export was skipped.",
        ),
        QccWarning(
            category=WarningCategory.INTERPRETATION_CAUTION,
            code="one_category",
            message="Avoid vital-few comparison.",
        ),
    )

    payload = warnings_to_jsonable(warnings)

    assert [item["category"] for item in payload] == [
        "validation_error",
        "data_caution",
        "export_skipped",
        "interpretation_caution",
    ]
    assert json.loads(json.dumps(payload)) == payload
