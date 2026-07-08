import json
from pathlib import Path


def test_lifecycle_and_first_slice_paths_are_consistent() -> None:
    change = Path("docs/changes/2026-07-07-create-qcc-toolkit/change.yaml")
    plan = Path("docs/plans/2026-07-08-create-qcc-toolkit-first-slice.md")
    catalog = Path("templates/ppt/catalog.yml")

    assert change.exists()
    assert plan.exists()
    assert catalog.exists()
    assert str(plan) in change.read_text()

    payload = json.loads(catalog.read_text())
    for entry in payload["templates"]:
        assert Path(entry["file"]).exists()
        assert Path(entry["markdown_guide"]).exists()
        if "python_generator" in entry:
            assert Path(entry["python_generator"]).exists()
        if "example_project" in entry:
            assert Path(entry["example_project"]).exists()
