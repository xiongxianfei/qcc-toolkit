from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS
from qcc_toolkit.templates import load_template_catalog, validate_template_catalog

CATALOG_PATH = Path("templates/ppt/catalog.yml")


def test_template_catalog_covers_first_slice_methods() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)
    methods_by_id = {method.method_id: method for method in FIRST_SLICE_METHODS}

    official_entries = catalog.official_templates

    assert CATALOG_PATH.exists()
    assert {entry.method_id for entry in official_entries} == set(methods_by_id)
    assert len(official_entries) == len(FIRST_SLICE_METHODS)

    for entry in official_entries:
        method = methods_by_id[entry.method_id]

        assert entry.template_id
        assert entry.catalog_status == "official"
        assert entry.method_name == method.name
        assert entry.template_type == "method_template"
        assert tuple(entry.qcc_stages) == method.qcc_stages
        assert Path(entry.file).exists()
        assert Path(entry.file).suffix == ".pptx"
        assert Path(entry.markdown_guide).exists()
        assert entry.source_file is not None
        source_path = Path(entry.source_file)
        assert source_path.exists()
        assert source_path.parent == Path("templates/ppt/sources")
        assert source_path.suffix == ".md"
        assert ".pptx" not in source_path.name
        assert entry.supports_generated_chart is method.supports_generated_chart
        assert "method_name" in entry.expected_placeholders
        assert "demo_label" in entry.expected_placeholders
        assert "template_metadata" in entry.expected_assets
        assert "catalog_entry" in entry.required_content
        assert set(entry.evidence_levels) == {
            "teaching_draft",
            "normal_qcc_project",
            "competition_management_review",
            "audit_high_risk",
        }


def test_template_catalog_declares_method_kit_modes_and_assist_status() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)

    expected_modes = {
        "pareto_chart": "powerpoint_native_chart",
        "5w2h": "template_native_worksheet",
        "5_whys": "template_native_worksheet",
        "check_sheet": "template_native_worksheet",
        "fishbone_diagram": "template_native_diagram",
    }
    expected_assist = {
        "pareto_chart": "optional",
        "5w2h": "unavailable",
        "5_whys": "unavailable",
        "check_sheet": "unavailable",
        "fishbone_diagram": "unavailable",
    }

    for method_id, mode in expected_modes.items():
        entry = catalog.by_method_id(method_id)
        assert entry.implementation_mode == mode
        assert entry.python_assist_status == expected_assist[method_id]
        if entry.python_assist_status == "optional":
            assert entry.python_assist_reasons
        else:
            assert entry.python_assist_reasons == ()


def test_pareto_catalog_entry_declares_generated_evidence_slots() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)
    pareto = catalog.by_method_id("pareto_chart")

    assert pareto.python_generator == "examples/scripts/generate_pareto.py"
    assert pareto.example_project == "examples/projects/reduce-packing-label-errors"
    assert pareto.implementation_mode == "powerpoint_native_chart"
    assert pareto.python_assist_status == "optional"
    assert pareto.chart_editability is not None
    assert pareto.chart_editability.editable_powerpoint_chart is True
    assert pareto.supports_generated_chart is True
    assert "chart_image" in pareto.expected_placeholders
    assert "caption" in pareto.expected_placeholders
    assert "metadata" in pareto.expected_assets
    assert "chart_image" in pareto.expected_assets


def test_load_template_catalog_preserves_schema_version() -> None:
    catalog = load_template_catalog(CATALOG_PATH)

    assert catalog.schema_version == 1


def test_template_catalog_has_no_incoming_entries_registered_as_official() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)

    incoming_or_source = {
        entry.template_id
        for entry in catalog.templates
        if entry.catalog_status in {"incoming", "source"}
    }
    official_ids = {entry.template_id for entry in catalog.official_templates}

    assert incoming_or_source.isdisjoint(official_ids)
    assert Path("templates/incoming/README.md").exists()
