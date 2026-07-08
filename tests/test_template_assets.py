from pathlib import Path
from zipfile import ZipFile

from qcc_toolkit.templates import validate_template_catalog


def test_template_assets_declare_demo_labels_and_placeholders() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))

    for entry in catalog.templates:
        assert entry.source_file is not None
        text = Path(entry.source_file).read_text()

        assert "DEMO EXAMPLE - not project evidence" in text
        assert f"template_id: {entry.template_id}" in text
        assert f"method_id: {entry.method_id}" in text
        for placeholder in entry.expected_placeholders:
            assert f"{{{{{placeholder}}}}}" in text


def test_template_catalog_points_to_real_pptx_files() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))

    for entry in catalog.templates:
        path = Path(entry.file)

        assert path.suffix == ".pptx"
        assert path.exists()
        assert path.read_bytes().startswith(b"PK")
        with ZipFile(path) as archive:
            names = set(archive.namelist())
            assert all(
                archive.getinfo(name).date_time == (2026, 7, 8, 0, 0, 0)
                for name in names
            )
            slide_names = sorted(
                name
                for name in names
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            )
            combined_xml = "\n".join(
                archive.read(name).decode("utf-8") for name in slide_names
            )

        assert len(slide_names) >= 3
        assert "DEMO EXAMPLE - not project evidence" in combined_xml
        assert f"template_id: {entry.template_id}" in combined_xml
        assert f"method_id: {entry.method_id}" in combined_xml
        for placeholder in entry.expected_placeholders:
            assert f"{{{{{placeholder}}}}}" in combined_xml


def test_scope_exclusions_remain_absent_from_template_assets() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    combined_text = "\n".join(
        Path(entry.source_file or entry.file).read_text() for entry in catalog.templates
    )

    assert "automated PPTX generation" not in combined_text
    assert "CAPA workflow" not in combined_text
    assert "Control Chart support" not in combined_text
