from pathlib import Path
from zipfile import ZipFile

from qcc_toolkit.templates import validate_template_catalog

TEMPLATE_NATIVE_METHODS = (
    "5w2h",
    "5_whys",
    "check_sheet",
    "fishbone_diagram",
)


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

        assert len(slide_names) >= 4
        assert "DEMO EXAMPLE - not project evidence" in combined_xml
        assert "DATA ENTRY" in combined_xml
        assert "Change data only" in combined_xml
        assert f"template_id: {entry.template_id}" in combined_xml
        assert f"method_id: {entry.method_id}" in combined_xml
        for placeholder in entry.expected_placeholders:
            assert f"{{{{{placeholder}}}}}" in combined_xml


def test_pareto_template_contains_editable_chart_data() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    pareto = catalog.by_method_id("pareto_chart")

    with ZipFile(pareto.file) as archive:
        names = set(archive.namelist())
        chart_names = sorted(
            name for name in names if name.startswith("ppt/charts/chart")
        )
        embedded_workbooks = sorted(
            name for name in names if name.startswith("ppt/embeddings/")
        )
        combined_chart_xml = "\n".join(
            archive.read(name).decode("utf-8") for name in chart_names
        )

    assert chart_names
    assert embedded_workbooks
    assert "Wrong label" in combined_chart_xml
    assert "Missing label" in combined_chart_xml
    assert "Count" in combined_chart_xml


def test_pareto_source_notes_declare_complete_method_kit_sections() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    pareto = catalog.by_method_id("pareto_chart")
    assert pareto.source_file is not None
    text = Path(pareto.source_file).read_text()

    for required_text in (
        "Purpose",
        "QCC stage fit",
        "When to use",
        "When not to use",
        "Required inputs",
        "PowerPoint edit instructions",
        "Completed demo example",
        "Blank copyable project slide",
        "Interpretation patterns",
        "Common mistakes",
        "Facilitator checklist",
        "Python assist decision",
        "Evidence/source note",
        "formula cells were not overwritten",
        "source",
        "date range",
    ):
        assert required_text in text


def test_pareto_pptx_exposes_complete_method_kit_surfaces() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    pareto = catalog.by_method_id("pareto_chart")

    with ZipFile(pareto.file) as archive:
        slide_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        combined_xml = "\n".join(
            archive.read(name).decode("utf-8") for name in slide_names
        )

    assert len(slide_names) >= 8
    for required_text in (
        "Purpose",
        "QCC stage fit",
        "When to use",
        "When not to use",
        "Required inputs",
        "PowerPoint Edit Data",
        "Completed demo example",
        "Blank copyable project slide",
        "Interpretation patterns",
        "Common mistakes",
        "Facilitator checklist",
        "Python assist decision",
        "Evidence/source note",
        "Key finding",
        "Next action",
    ):
        assert required_text in combined_xml


def test_pareto_source_notes_declare_chart_quality_standard() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    pareto = catalog.by_method_id("pareto_chart")
    assert pareto.source_file is not None
    text = Path(pareto.source_file).read_text()

    for required_text in (
        "Chart decision guide",
        "Decision supported",
        "Pattern to look for",
        "Safe conclusion",
        "Overclaim to avoid",
        "Chart variant library",
        "Cumulative Pareto",
        "Before/after Pareto comparison",
        "Focus annotation",
        "Chart quality checklist",
        "Percent",
        "Cumulative percent",
        "Formula check",
    ):
        assert required_text in text


def test_pareto_pptx_exposes_chart_quality_surfaces() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    pareto = catalog.by_method_id("pareto_chart")

    with ZipFile(pareto.file) as archive:
        slide_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        combined_xml = "\n".join(
            archive.read(name).decode("utf-8") for name in slide_names
        )

    assert len(slide_names) >= 13
    for required_text in (
        "Chart decision guide",
        "Decision supported",
        "Pattern to look for",
        "Safe conclusion",
        "Overclaim to avoid",
        "Chart variant library",
        "Cumulative Pareto",
        "Before/after Pareto comparison",
        "Focus annotation",
        "Chart quality checklist",
        "Source",
        "Date range",
        "Filters",
        "Percent",
        "Cumulative percent",
        "Formula check",
    ):
        assert required_text in combined_xml


def test_template_native_source_notes_declare_complete_method_kit_sections() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))

    for method_id in TEMPLATE_NATIVE_METHODS:
        entry = catalog.by_method_id(method_id)
        assert entry.source_file is not None
        text = Path(entry.source_file).read_text()

        for required_text in (
            "Purpose",
            "QCC stage fit",
            "When to use",
            "When not to use",
            "Required inputs",
            "Completed demo example",
            "Blank working slide or worksheet",
            "Interpretation patterns",
            "Common mistakes",
            "Facilitator checklist",
            "Python assist decision",
            "Evidence/source note",
            "source",
            "date range",
        ):
            assert required_text in text, f"{method_id} missing {required_text}"


def test_template_native_pptx_exposes_complete_method_kit_surfaces() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))

    for method_id in TEMPLATE_NATIVE_METHODS:
        entry = catalog.by_method_id(method_id)
        with ZipFile(entry.file) as archive:
            slide_names = sorted(
                name
                for name in archive.namelist()
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            )
            combined_xml = "\n".join(
                archive.read(name).decode("utf-8") for name in slide_names
            )

        assert len(slide_names) >= 8, method_id
        for required_text in (
            "Purpose",
            "QCC stage fit",
            "When to use",
            "When not to use",
            "Required inputs",
            "Completed demo example",
            "Blank working slide or worksheet",
            "Interpretation patterns",
            "Common mistakes",
            "Facilitator checklist",
            "Python assist decision",
            "Evidence/source note",
            "Key conclusion",
            "Next action",
        ):
            assert required_text in combined_xml, f"{method_id} missing {required_text}"


def test_fishbone_source_notes_declare_diagram_quality_standard() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    fishbone = catalog.by_method_id("fishbone_diagram")
    assert fishbone.source_file is not None
    text = Path(fishbone.source_file).read_text()

    for required_text in (
        "Diagram quality guide",
        "Diagram decision",
        "Good structure",
        "Overclaim to avoid",
        "Verification marker legend",
        "Cause wording guide",
        "Weak wording",
        "Testable wording",
        "Editable fishbone diagram",
        "Cause verification plan",
        "Verification method",
        "Owner",
        "Due date",
        "Status",
        "Visual design rule",
        "Centered fishbone composition",
        "Short cause labels",
        "Details stay in verification plan",
        "Branch label capsules",
        "Status badges",
        "Four-layer architecture",
        "Layer 1: effect",
        "Layer 2: branch category",
        "Layer 3: short visible cause",
        "Layer 4: verification detail",
        "Keep Layer 4 out of the diagram body",
    ):
        assert required_text in text


def test_fishbone_pptx_exposes_diagram_quality_surfaces() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    fishbone = catalog.by_method_id("fishbone_diagram")

    with ZipFile(fishbone.file) as archive:
        slide_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        combined_xml = "\n".join(
            archive.read(name).decode("utf-8") for name in slide_names
        )

    assert len(slide_names) >= 14
    for required_text in (
        "Diagram quality guide",
        "Diagram decision",
        "Good structure",
        "Overclaim to avoid",
        "Verification marker legend",
        "[S] Suspected",
        "[V?] Selected for verification",
        "[V] Verified",
        "[X] Rejected",
        "Cause wording guide",
        "Weak wording",
        "Testable wording",
        "Editable fishbone diagram",
        "Effect statement",
        "Selected causes to verify",
        "Evidence/source fields",
        "Cause verification plan",
        "Verification method",
        "Owner",
        "Due date",
        "Status",
        "Clean editable fishbone",
        "Centered fishbone composition",
        "Short cause labels",
        "Details stay in verification plan",
        "Branch label capsules",
        "Status badges",
        "Four-layer architecture",
        "Layer 1: effect",
        "Layer 2: branch category",
        "Layer 3: short visible cause",
        "Layer 4: verification detail",
        "Keep Layer 4 out of the diagram body",
    ):
        assert required_text in combined_xml


def test_scope_exclusions_remain_absent_from_template_assets() -> None:
    catalog = validate_template_catalog(Path("templates/ppt/catalog.yml"))
    combined_text = "\n".join(
        Path(entry.source_file or entry.file).read_text() for entry in catalog.templates
    )

    assert "automated PPTX generation" not in combined_text
    assert "CAPA workflow" not in combined_text
    assert "Control Chart support" not in combined_text
    assert "manual chart is authoritative" not in combined_text
