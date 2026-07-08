from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS
from qcc_toolkit.templates import load_template_catalog, validate_template_catalog

CATALOG_PATH = Path("templates/ppt/catalog.yml")


def test_template_catalog_covers_first_slice_methods() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)
    methods_by_id = {method.method_id: method for method in FIRST_SLICE_METHODS}

    assert CATALOG_PATH.exists()
    assert {entry.method_id for entry in catalog.templates} == set(methods_by_id)
    assert len(catalog.templates) == len(FIRST_SLICE_METHODS)

    for entry in catalog.templates:
        method = methods_by_id[entry.method_id]

        assert entry.template_id
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


def test_pareto_catalog_entry_declares_generated_evidence_slots() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)
    pareto = catalog.by_method_id("pareto_chart")

    assert pareto.python_generator == "examples/scripts/generate_pareto.py"
    assert pareto.example_project == "examples/projects/reduce-packing-label-errors"
    assert pareto.supports_generated_chart is True
    assert "chart_image" in pareto.expected_placeholders
    assert "caption" in pareto.expected_placeholders
    assert "metadata" in pareto.expected_assets
    assert "chart_image" in pareto.expected_assets


def test_load_template_catalog_preserves_schema_version() -> None:
    catalog = load_template_catalog(CATALOG_PATH)

    assert catalog.schema_version == 1
