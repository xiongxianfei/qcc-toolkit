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


def test_markdown_first_surfaces_are_primary_and_optional_aids_are_labeled() -> None:
    readme = Path("README.md").read_text()
    project_map = Path("docs/project-map.md").read_text()
    catalog_payload = json.loads(Path("templates/ppt/catalog.yml").read_text())

    assert "method-kits/pareto-chart.md" in readme
    assert "Markdown-first" in readme
    assert (
        "PowerPoint templates and Python automation are optional execution aids"
        in readme
    )
    assert "GitHub Repository Template" not in readme
    assert "Use this template" not in readme

    assert "method-kits/" in project_map
    assert "optional execution aids" in project_map
    assert "README.md` still contains template repository content" not in project_map

    assert catalog_payload["product_identity"] == "markdown_first_method_guidance"
    assert catalog_payload["catalog_role"] == "optional_execution_aid"
    assert catalog_payload["official_method_kit_root"] == "method-kits"

    for entry in catalog_payload["templates"]:
        assert entry["product_role"] == "optional_execution_aid"
        assert entry["markdown_first_status"] == "secondary_to_method_kit"
        assert entry["method_kit_status"] in {"available", "pending"}
        if entry["method_kit_status"] == "available":
            assert entry["method_kit"].startswith("method-kits/")
            assert entry["method_kit"].endswith(".md")
            assert Path(entry["method_kit"]).exists()


def test_legacy_method_guides_do_not_override_markdown_first_method_kits() -> None:
    for path in Path("docs/methods").glob("*.md"):
        text = path.read_text()

        assert "Legacy optional-aid note" in text, f"{path} missing optional-aid note"
        assert "method-kits/" in text, f"{path} missing method-kit pointer"
        assert "PowerPoint template is the primary" not in text
        assert "PowerPoint remains the primary" not in text
        assert "authority for generated Pareto evidence" not in text

    package_text = "\n".join(
        path.read_text()
        for path in (
            Path("qcc_toolkit/evidence.py"),
            Path("qcc_toolkit/reports.py"),
        )
    )
    assert "optional" in package_text
    assert "method kit" in package_text
