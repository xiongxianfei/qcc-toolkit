from pathlib import Path

from qcc_toolkit.templates import validate_template_catalog

CATALOG_PATH = Path("templates/ppt/catalog.yml")
EVIDENCE_LEVELS_PATH = Path("docs/template-standards/evidence-levels.md")
INCOMING_TEMPLATES_PATH = Path("docs/template-standards/incoming-templates.md")
REVIEW_CHECKLIST_PATH = Path("docs/template-standards/method-kit-review-checklist.md")
INCOMING_README_PATH = Path("templates/incoming/README.md")


def test_evidence_level_standard_defines_all_required_levels() -> None:
    text = EVIDENCE_LEVELS_PATH.read_text()

    for required_text in (
        "Level 1",
        "teaching/draft",
        "PowerPoint template edits are sufficient",
        "Level 2",
        "normal QCC project",
        "source data",
        "date range",
        "checklist evidence",
        "Level 3",
        "competition or management review",
        "calculation table",
        "versioned template",
        "Python assist is recommended for raw-data or repeated chart methods",
        "Level 4",
        "audit or high-risk evidence",
        "reproducible evidence package",
        "validated analysis path",
        "manual PowerPoint chart is not authoritative final evidence",
    ):
        assert required_text in text


def test_incoming_template_guidance_keeps_source_assets_unofficial() -> None:
    combined_text = "\n".join(
        (
            INCOMING_TEMPLATES_PATH.read_text(),
            INCOMING_README_PATH.read_text(),
        )
    )

    for required_text in (
        "templates/incoming/",
        "not official",
        "official method kit",
        "method-kit quality standard",
        "unknown method",
        "unknown QCC stage",
        "unknown owner",
        "unsupported formulas",
        "real customer names",
        "employee names",
        "supplier names",
        "patient data",
        "credentials",
        "hidden notes",
        "private data",
        "catalog entry",
    ):
        assert required_text in combined_text


def test_method_kit_review_checklist_covers_demo_source_and_scope_failures() -> None:
    text = REVIEW_CHECKLIST_PATH.read_text()

    for required_text in (
        "demo data presented as project evidence",
        "missing data source",
        "missing date range",
        "QCC stage fit",
        "method logic",
        "generic template assets",
        "common mistakes",
        "facilitator checklist",
        "Python assist decision",
        "Evidence/source note",
    ):
        assert required_text in text


def test_official_method_kits_are_cross_artifact_consistent() -> None:
    catalog = validate_template_catalog(CATALOG_PATH)

    for entry in catalog.official_templates:
        guide_text = Path(entry.markdown_guide).read_text()
        assert entry.source_file is not None
        source_text = Path(entry.source_file).read_text()
        combined = f"{guide_text}\n{source_text}"

        assert f"method_id: {entry.method_id}" in guide_text
        assert f"method_id: {entry.method_id}" in source_text
        assert f"template_id: {entry.template_id}" in source_text
        assert entry.method_name in guide_text
        assert "DEMO EXAMPLE - not project evidence" in source_text
        assert "Python assist decision" in combined
        assert (
            "Evidence/source note" in combined
            or "Evidence levels and source notes" in combined
        )
        assert "Common mistakes" in combined
        assert "Review checklist" in combined or "Facilitator checklist" in combined
        assert "manual PowerPoint chart is authoritative" not in combined
