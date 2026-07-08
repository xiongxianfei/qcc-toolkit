from pathlib import Path

import pytest

from qcc_toolkit.templates import CatalogValidationError, validate_template_catalog


def test_catalog_validation_fails_for_missing_referenced_path(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.yml"
    catalog.write_text(
        """
{
  "schema_version": 1,
  "templates": [
    {
      "template_id": "missing_template",
      "method_id": "pareto_chart",
      "template_type": "method_template",
      "qcc_stages": ["understand_current_condition"],
      "file": "missing/template.pptx.md",
      "markdown_guide": "docs/methods/pareto_chart.md",
      "supports_generated_chart": true,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    }
  ]
}
""".strip()
    )

    with pytest.raises(CatalogValidationError, match="missing/template.pptx.md"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_duplicate_template_id(tmp_path: Path) -> None:
    catalog = tmp_path / "catalog.yml"
    catalog.write_text(
        """
{
  "schema_version": 1,
  "templates": [
    {
      "template_id": "duplicate_template",
      "method_id": "check_sheet",
      "template_type": "method_template",
      "qcc_stages": ["understand_current_condition"],
      "file": "docs/methods/check_sheet.md",
      "markdown_guide": "docs/methods/check_sheet.md",
      "supports_generated_chart": false,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    },
    {
      "template_id": "duplicate_template",
      "method_id": "5w2h",
      "template_type": "method_template",
      "qcc_stages": ["define_problem"],
      "file": "docs/methods/5w2h.md",
      "markdown_guide": "docs/methods/5w2h.md",
      "supports_generated_chart": false,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    }
  ]
}
""".strip()
    )

    with pytest.raises(CatalogValidationError, match="duplicate_template"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_unclassified_duplicate_method(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    catalog.write_text(
        """
{
  "schema_version": 1,
  "templates": [
    {
      "template_id": "check_sheet_template_a",
      "method_id": "check_sheet",
      "template_type": "method_template",
      "qcc_stages": ["understand_current_condition"],
      "file": "docs/methods/check_sheet.md",
      "markdown_guide": "docs/methods/check_sheet.md",
      "supports_generated_chart": false,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    },
    {
      "template_id": "check_sheet_template_b",
      "method_id": "check_sheet",
      "template_type": "method_template",
      "qcc_stages": ["understand_current_condition"],
      "file": "docs/methods/check_sheet.md",
      "markdown_guide": "docs/methods/check_sheet.md",
      "supports_generated_chart": false,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    }
  ]
}
""".strip()
    )

    with pytest.raises(CatalogValidationError, match="duplicate method_id"):
        validate_template_catalog(catalog)


def test_catalog_validation_fails_for_mismatched_guide_method_id(
    tmp_path: Path,
) -> None:
    catalog = tmp_path / "catalog.yml"
    catalog.write_text(
        """
{
  "schema_version": 1,
  "templates": [
    {
      "template_id": "pareto_chart_template",
      "method_id": "pareto_chart",
      "template_type": "method_template",
      "qcc_stages": ["understand_current_condition", "analyze_causes"],
      "file": "templates/ppt/methods/pareto-chart-template.pptx.md",
      "markdown_guide": "docs/methods/check_sheet.md",
      "python_generator": "examples/scripts/generate_pareto.py",
      "example_project": "examples/projects/reduce-packing-label-errors",
      "supports_generated_chart": true,
      "expected_placeholders": ["method_name", "demo_label"],
      "expected_assets": ["template_metadata"]
    }
  ]
}
""".strip()
    )

    with pytest.raises(CatalogValidationError, match="pareto_chart_template"):
        validate_template_catalog(catalog)
