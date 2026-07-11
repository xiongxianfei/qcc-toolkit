import json
from pathlib import Path

LEGACY_METHOD_GUIDE_PATHS = {
    "docs/methods/5_whys.md",
    "docs/methods/5w2h.md",
    "docs/methods/check_sheet.md",
    "docs/methods/fishbone_diagram.md",
    "docs/methods/pareto_chart.md",
}
CANONICAL_METHOD_KITS = {
    "method-kits/check-sheet.md",
    "method-kits/fishbone-diagram.md",
    "method-kits/five-whys.md",
    "method-kits/five-w-two-h.md",
    "method-kits/pareto-chart.md",
}


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
        assert "python_generator" not in entry
        assert "example_project" not in entry


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
    assert not any(Path("docs/methods").glob("*.md"))

    package_text = "\n".join(
        path.read_text()
        for path in (
            Path("qcc_toolkit/evidence.py"),
            Path("qcc_toolkit/reports.py"),
        )
    )
    assert "optional" in package_text
    assert "method kit" in package_text


def test_deleted_legacy_method_paths_are_not_live_dependencies() -> None:
    live_paths = (
        Path("README.md"),
        Path("docs/qcc-project-story.md"),
        Path("docs/project-map.md"),
        Path("templates/ppt/catalog.yml"),
        Path("tests/test_markdown_first_method_guidance.py"),
        Path("tests/test_template_catalog.py"),
        Path("tests/test_method_kit_closeout.py"),
        Path("tests/test_acceptance.py"),
    )

    for path in live_paths:
        text = path.read_text()
        for legacy_path in LEGACY_METHOD_GUIDE_PATHS:
            assert legacy_path not in text, f"{path} still references {legacy_path}"
        assert "methods/check_sheet.md" not in text
        assert "methods/fishbone_diagram.md" not in text
        assert "methods/5_whys.md" not in text
        assert "methods/5w2h.md" not in text


def test_catalog_points_official_entries_to_canonical_method_kits() -> None:
    payload = json.loads(Path("templates/ppt/catalog.yml").read_text())

    for entry in payload["templates"]:
        assert entry["method_kit_status"] == "available"
        assert entry["method_kit"] in CANONICAL_METHOD_KITS
        assert entry["markdown_guide"] == entry["method_kit"]
        assert Path(entry["markdown_guide"]).exists()
