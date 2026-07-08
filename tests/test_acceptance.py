import json
import re
from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS, MethodType

CHANGE_ROOT = Path("docs/changes/2026-07-07-create-qcc-toolkit")
PLAN_PATH = Path("docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md")
CATALOG_PATH = Path("templates/ppt/catalog.yml")


def test_first_slice_acceptance_surfaces_are_ready_for_m7_review() -> None:
    change_text = (CHANGE_ROOT / "change.yaml").read_text()
    plan_text = PLAN_PATH.read_text()
    catalog = json.loads(CATALOG_PATH.read_text())

    assert "status: m7-review-requested" in change_text
    assert "current_stage: code-review" in change_text
    assert "Current milestone: M7" in plan_text
    assert "Current milestone state: review-requested" in plan_text
    assert "Next stage: code-review" in plan_text

    for milestone in range(1, 7):
        assert f"code-review-m{milestone}-" in change_text
        assert re.search(rf"M{milestone} .*closed by code-review", plan_text)

    method_ids = {method.method_id for method in FIRST_SLICE_METHODS}
    catalog_entries = {entry["method_id"]: entry for entry in catalog["templates"]}
    assert set(catalog_entries) == method_ids

    pareto = catalog_entries["pareto_chart"]
    assert Path(pareto["python_generator"]).exists()
    assert Path(pareto["example_project"]).exists()
    assert Path(pareto["example_project"], "data", "packing_label_defects.csv").exists()
    assert pareto["supports_generated_chart"] is True

    for method in FIRST_SLICE_METHODS:
        entry = catalog_entries[method.method_id]
        assert Path(entry["file"]).exists()
        assert Path(entry["markdown_guide"]).exists()
        assert f"method_id: {method.method_id}" in Path(entry["file"]).read_text()
        assert "DEMO EXAMPLE - not project evidence" in Path(entry["file"]).read_text()
        if method.method_type is MethodType.TEMPLATE_GUIDED:
            assert method.first_slice_status == "template_guided"
            assert entry["supports_generated_chart"] is False
