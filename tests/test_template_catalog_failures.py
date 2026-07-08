import json
from pathlib import Path

import pytest

from qcc_toolkit.templates import CatalogValidationError, validate_template_catalog


def _valid_entry(**overrides: object) -> dict[str, object]:
    entry: dict[str, object] = {
        "template_id": "pareto_chart_template",
        "catalog_status": "official",
        "method_id": "pareto_chart",
        "method_name": "Pareto Chart",
        "template_type": "method_template",
        "implementation_mode": "powerpoint_native_chart",
        "qcc_stages": ["understand_current_condition", "analyze_causes"],
        "file": "templates/ppt/methods/pareto-chart-template.pptx",
        "source_file": "templates/ppt/sources/pareto-chart.md",
        "markdown_guide": "docs/methods/pareto_chart.md",
        "python_assist_status": "optional",
        "python_assist_reasons": ["large_raw_data"],
        "python_generator": "examples/scripts/generate_pareto.py",
        "example_project": "examples/projects/reduce-packing-label-errors",
        "supports_generated_chart": True,
        "required_content": [
            "markdown_guide",
            "powerpoint_template",
            "completed_demo_example",
            "blank_copyable_slide",
            "interpretation_patterns",
            "common_mistakes",
            "facilitator_checklist",
            "python_assist_decision",
            "evidence_source_note",
            "catalog_entry",
            "sample_data_table",
            "chart_editing_instructions",
        ],
        "evidence_levels": [
            "teaching_draft",
            "normal_qcc_project",
            "competition_management_review",
            "audit_high_risk",
        ],
        "chart_editability": {
            "editable_powerpoint_chart": True,
        },
        "expected_placeholders": ["method_name", "demo_label"],
        "expected_assets": ["template_metadata"],
    }
    entry.update(overrides)
    return entry


def _write_catalog(catalog: Path, *entries: dict[str, object]) -> None:
    catalog.write_text(
        json.dumps({"schema_version": 1, "templates": list(entries)}, indent=2)
    )


def _write_valid_catalog(catalog: Path, **entry_overrides: object) -> None:
    _write_catalog(catalog, _valid_entry(**entry_overrides))


def test_catalog_validation_fails_for_missing_referenced_path(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_valid_catalog(
        catalog,
        template_id="missing_template",
        file="missing/template.pptx.md",
    )

    with pytest.raises(CatalogValidationError, match="missing/template.pptx.md"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_without_required_method_kit_metadata(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_valid_catalog(catalog, required_content=["catalog_entry"])

    with pytest.raises(CatalogValidationError, match="required_content"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_without_chart_editability_metadata(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_valid_catalog(catalog, chart_editability=None)

    with pytest.raises(CatalogValidationError, match="chart_editability"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_incomplete_python_assist_metadata(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_valid_catalog(
        catalog,
        implementation_mode="python_assisted_chart",
        python_assist_status="recommended",
    )

    with pytest.raises(CatalogValidationError, match="sample_input"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_duplicate_template_id(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_catalog(
        catalog,
        _valid_entry(
            template_id="duplicate_template",
            method_id="check_sheet",
            method_name="Check Sheet",
            implementation_mode="template_native_worksheet",
            qcc_stages=["understand_current_condition"],
            file="docs/methods/check_sheet.md",
            source_file="templates/ppt/sources/check-sheet.md",
            markdown_guide="docs/methods/check_sheet.md",
            python_assist_status="unavailable",
            python_assist_reasons=[],
            supports_generated_chart=False,
            chart_editability=None,
        ),
        _valid_entry(
            template_id="duplicate_template",
            method_id="5w2h",
            method_name="5W2H",
            implementation_mode="template_native_worksheet",
            qcc_stages=["define_problem"],
            file="docs/methods/5w2h.md",
            source_file="templates/ppt/sources/5w2h.md",
            markdown_guide="docs/methods/5w2h.md",
            python_assist_status="unavailable",
            python_assist_reasons=[],
            supports_generated_chart=False,
            chart_editability=None,
        ),
    )

    with pytest.raises(CatalogValidationError, match="duplicate_template"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_unclassified_duplicate_method(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_catalog(
        catalog,
        _valid_entry(
            template_id="check_sheet_template_a",
            method_id="check_sheet",
            method_name="Check Sheet",
            implementation_mode="template_native_worksheet",
            qcc_stages=["understand_current_condition"],
            file="docs/methods/check_sheet.md",
            source_file="templates/ppt/sources/check-sheet.md",
            markdown_guide="docs/methods/check_sheet.md",
            python_assist_status="unavailable",
            python_assist_reasons=[],
            supports_generated_chart=False,
            chart_editability=None,
        ),
        _valid_entry(
            template_id="check_sheet_template_b",
            method_id="check_sheet",
            method_name="Check Sheet",
            implementation_mode="template_native_worksheet",
            qcc_stages=["understand_current_condition"],
            file="docs/methods/check_sheet.md",
            source_file="templates/ppt/sources/check-sheet.md",
            markdown_guide="docs/methods/check_sheet.md",
            python_assist_status="unavailable",
            python_assist_reasons=[],
            supports_generated_chart=False,
            chart_editability=None,
        ),
    )

    with pytest.raises(CatalogValidationError, match="duplicate method_id"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_mismatched_guide_method_id(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    _write_valid_catalog(catalog, markdown_guide="docs/methods/check_sheet.md")

    with pytest.raises(CatalogValidationError, match="pareto_chart_template"):
        validate_template_catalog(catalog)
