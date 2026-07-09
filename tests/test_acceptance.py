import json
import re
from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS, MethodType

CHANGE_ROOT = Path("docs/changes/2026-07-07-create-qcc-toolkit")
PLAN_PATH = Path("docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md")
CATALOG_PATH = Path("templates/ppt/catalog.yml")


def test_first_slice_acceptance_surfaces_have_stable_lifecycle_evidence() -> None:
    change_text = (CHANGE_ROOT / "change.yaml").read_text()
    plan_text = PLAN_PATH.read_text()
    catalog = json.loads(CATALOG_PATH.read_text())
    status = _metadata_value(change_text, "status")
    current_stage = _metadata_value(change_text, "current_stage")

    assert status != "m7-ready"
    assert current_stage in {
        "code-review",
        "review-resolution",
        "explain-change",
        "verify",
        "pr",
        "done",
    }
    assert re.search(r"Current milestone: (M7|none)", plan_text)
    assert re.search(
        (
            r"Current milestone state: "
            r"(review-requested|resolution-needed|closed|not-applicable)"
        ),
        plan_text,
    )
    assert re.search(
        r"Next stage: (code-review|review-resolution|explain-change|verify|pr|none)",
        plan_text,
    )

    for milestone in range(1, 7):
        assert f"code-review-m{milestone}-" in change_text
        assert re.search(rf"M{milestone} .*closed by code-review", plan_text)

    method_ids = {method.method_id for method in FIRST_SLICE_METHODS}
    catalog_entries = {entry["method_id"]: entry for entry in catalog["templates"]}
    assert set(catalog_entries) == method_ids

    pareto = catalog_entries["pareto_chart"]
    assert "python_generator" not in pareto
    assert "example_project" not in pareto
    assert pareto["supports_generated_chart"] is True

    for method in FIRST_SLICE_METHODS:
        entry = catalog_entries[method.method_id]
        assert Path(entry["file"]).exists()
        assert Path(entry["file"]).suffix == ".pptx"
        source_path = Path(entry["source_file"])
        assert source_path.exists()
        assert source_path.parent == Path("templates/ppt/sources")
        assert ".pptx" not in source_path.name
        assert Path(entry["markdown_guide"]).exists()
        assert f"method_id: {method.method_id}" in source_path.read_text()
        assert "DEMO EXAMPLE - not project evidence" in source_path.read_text()
        if method.method_type is MethodType.TEMPLATE_GUIDED:
            assert method.first_slice_status == "template_guided"
            assert entry["supports_generated_chart"] is False


def _metadata_value(text: str, key: str) -> str:
    match = re.search(rf"^{key}: (.+)$", text, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)
