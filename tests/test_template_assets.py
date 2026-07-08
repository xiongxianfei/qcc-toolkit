from pathlib import Path

from qcc_toolkit.templates import validate_template_catalog


def test_template_assets_declare_demo_labels_and_placeholders() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))

    for entry in catalog.templates:
        text = Path(entry.file).read_text()

        assert "DEMO EXAMPLE - not project evidence" in text
        assert f"template_id: {entry.template_id}" in text
        assert f"method_id: {entry.method_id}" in text
        for placeholder in entry.expected_placeholders:
            assert f"{{{{{placeholder}}}}}" in text


def test_scope_exclusions_remain_absent_from_template_assets() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    combined_text = "\n".join(
        Path(entry.file).read_text() for entry in catalog.templates
    )

    assert "automated PPTX generation" not in combined_text
    assert "CAPA workflow" not in combined_text
    assert "Control Chart support" not in combined_text
