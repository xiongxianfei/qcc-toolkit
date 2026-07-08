"""Build first-slice QCC PowerPoint method templates.

The Markdown files next to the generated decks remain the reviewable source notes.
This script creates static, editable PPTX decks from the catalog contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from qcc_toolkit.templates import TemplateCatalogEntry, load_template_catalog

CATALOG_PATH = Path("templates/ppt/catalog.yml")
OUTPUT_ROOT = Path("templates/ppt/methods")
GENERATED_AT = datetime(2026, 7, 8, 0, 0, 0)
ZIP_TIMESTAMP = (2026, 7, 8, 0, 0, 0)


@dataclass(frozen=True)
class TemplateContent:
    """Human-facing static content for one template deck."""

    title: str
    stage_label: str
    purpose: str
    demo_title: str
    demo_points: tuple[str, ...]
    project_title: str
    project_points: tuple[str, ...]


CONTENT: dict[str, TemplateContent] = {
    "pareto_chart": TemplateContent(
        title="Pareto Chart",
        stage_label="Understand Current Condition / Analyze Causes",
        purpose=(
            "Identify the vital few defect categories from validated project data."
        ),
        demo_title="DEMO EXAMPLE - not project evidence",
        demo_points=(
            "Generated chart image slot: {{chart_image}}",
            "Calculated table reference: {{calculated_table}}",
            "Caption from evidence package: {{caption}}",
            "Data context and filters: {{data_context}}",
            "Warnings and cautions: {{warnings}}",
        ),
        project_title="Project Pareto Evidence",
        project_points=(
            "Insert generated chart image in {{chart_image}}.",
            "Link table artifact in {{calculated_table}}.",
            "Paste deterministic caption in {{caption}}.",
            "Preserve source and filters in {{data_context}}.",
            "Carry warning state in {{warnings}}.",
        ),
    ),
    "check_sheet": TemplateContent(
        title="Check Sheet",
        stage_label="Understand Current Condition",
        purpose="Collect defects or events consistently before analysis.",
        demo_title="DEMO EXAMPLE - not project evidence",
        demo_points=(
            "Check item: {{check_item}}",
            "Tally area: {{tally_area}}",
            "Collection notes: {{review_notes}}",
        ),
        project_title="Project Check Sheet",
        project_points=(
            "Define the item being counted in {{check_item}}.",
            "Record counts or tallies in {{tally_area}}.",
            "Capture collection limits in {{review_notes}}.",
        ),
    ),
    "5w2h": TemplateContent(
        title="5W2H",
        stage_label="Define Problem",
        purpose="Turn a broad issue into a concrete problem statement.",
        demo_title="DEMO EXAMPLE - not project evidence",
        demo_points=(
            "What: {{what}}",
            "Why: {{why}}",
            "Where: {{where}}",
            "When: {{when}}",
            "Who: {{who}}",
            "How: {{how}}",
            "How much: {{how_much}}",
        ),
        project_title="Project 5W2H Statement",
        project_points=(
            "Fill the 5W2H fields from project facts.",
            "Use the result as the problem statement source.",
            "Avoid unsupported causes or solutions in this slide.",
        ),
    ),
    "fishbone_diagram": TemplateContent(
        title="Fishbone Diagram",
        stage_label="Analyze Causes",
        purpose="Organize suspected causes before verification.",
        demo_title="DEMO EXAMPLE - not project evidence",
        demo_points=(
            "Effect statement: {{effect_statement}}",
            "Cause branches: {{cause_branches}}",
            "Verified causes: {{verified_causes}}",
        ),
        project_title="Project Cause Structure",
        project_points=(
            "Place the effect in {{effect_statement}}.",
            "Group suspected causes in {{cause_branches}}.",
            "Separate verified causes in {{verified_causes}}.",
        ),
    ),
    "5_whys": TemplateContent(
        title="5 Whys",
        stage_label="Analyze Causes",
        purpose="Trace a problem through evidence-backed why links.",
        demo_title="DEMO EXAMPLE - not project evidence",
        demo_points=(
            "Problem: {{problem}}",
            "Why chain: {{why_chain}}",
            "Root cause: {{root_cause}}",
            "Verification: {{verification}}",
        ),
        project_title="Project Why Chain",
        project_points=(
            "Start with the specific problem in {{problem}}.",
            "Build the cause chain in {{why_chain}}.",
            "State the candidate root cause in {{root_cause}}.",
            "Record evidence status in {{verification}}.",
        ),
    ),
}


def main() -> None:
    catalog = load_template_catalog(CATALOG_PATH)
    for entry in catalog.templates:
        if entry.source_file is None:
            raise ValueError(f"{entry.template_id} is missing source_file.")
        if not Path(entry.source_file).exists():
            raise FileNotFoundError(entry.source_file)
        if not Path(entry.markdown_guide).exists():
            raise FileNotFoundError(entry.markdown_guide)
        _build_template(entry)


def _build_template(entry: TemplateCatalogEntry) -> None:
    content = CONTENT[entry.method_id]
    output_path = Path(entry.file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    prs = Presentation()
    prs.slide_width = Inches(13.333333)
    prs.slide_height = Inches(7.5)
    prs.core_properties.title = f"{content.title} QCC Method Template"
    prs.core_properties.subject = "QCC Toolkit method template"
    prs.core_properties.keywords = (
        f"qcc, {entry.method_id}, {entry.template_id}, DEMO EXAMPLE"
    )
    prs.core_properties.created = GENERATED_AT
    prs.core_properties.modified = GENERATED_AT
    prs.core_properties.last_modified_by = "QCC Toolkit"
    prs.core_properties.comments = (
        "Generated by tools/build_ppt_templates.py from template catalog and "
        "reviewable Markdown source notes."
    )

    _add_overview_slide(prs, entry, content)
    _add_demo_slide(prs, entry, content)
    _add_project_slide(prs, entry, content)

    prs.save(output_path)
    _normalize_pptx_package(output_path)


def _normalize_pptx_package(path: Path) -> None:
    """Rewrite the zip package with stable entry order and timestamps."""

    with ZipFile(path) as source:
        entries = [(name, source.read(name)) for name in sorted(source.namelist())]

    with ZipFile(path, "w", compression=ZIP_DEFLATED) as target:
        for name, data in entries:
            info = ZipInfo(name, ZIP_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            target.writestr(info, data)


def _add_overview_slide(
    prs: Presentation,
    entry: TemplateCatalogEntry,
    content: TemplateContent,
) -> None:
    slide = _blank_slide(prs)
    _add_header(slide, content.title, "QCC method template")
    _add_meta_bar(slide, entry, content)
    _add_text_box(
        slide,
        left=0.7,
        top=1.75,
        width=5.6,
        height=1.25,
        text=content.purpose,
        font_size=24,
        bold=True,
        color=RGBColor(35, 45, 55),
    )
    _add_section_box(
        slide,
        left=0.7,
        top=3.35,
        width=5.8,
        height=2.6,
        title="Template rules",
        items=(
            "PowerPoint teaches and presents.",
            "Markdown governs method knowledge.",
            "Python generates data-dependent evidence.",
            "Final project slides must preserve evidence references.",
        ),
    )
    _add_section_box(
        slide,
        left=6.85,
        top=3.35,
        width=5.8,
        height=2.6,
        title="Placeholders",
        items=tuple(f"{{{{{name}}}}}" for name in entry.expected_placeholders),
    )
    _add_footer(slide, entry)


def _add_demo_slide(
    prs: Presentation,
    entry: TemplateCatalogEntry,
    content: TemplateContent,
) -> None:
    slide = _blank_slide(prs)
    _add_header(slide, content.demo_title, content.title)
    _add_badge(slide, "DEMO EXAMPLE - not project evidence", 0.7, 1.15, 4.2)
    _add_section_box(
        slide,
        left=0.7,
        top=1.85,
        width=5.9,
        height=4.6,
        title="Demo structure",
        items=content.demo_points,
    )
    _add_placeholder_panel(slide, entry, left=6.95, top=1.85)
    _add_footer(slide, entry)


def _add_project_slide(
    prs: Presentation,
    entry: TemplateCatalogEntry,
    content: TemplateContent,
) -> None:
    slide = _blank_slide(prs)
    _add_header(slide, content.project_title, content.title)
    _add_badge(slide, "Replace demo content with project evidence", 0.7, 1.15, 5.2)
    _add_section_box(
        slide,
        left=0.7,
        top=1.85,
        width=5.9,
        height=4.6,
        title="Project slide checklist",
        items=content.project_points,
    )
    _add_placeholder_panel(slide, entry, left=6.95, top=1.85)
    _add_footer(slide, entry)


def _blank_slide(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _add_header(slide, title: str, subtitle: str) -> None:
    _add_text_box(
        slide,
        left=0.55,
        top=0.28,
        width=9.1,
        height=0.46,
        text=title,
        font_size=24,
        bold=True,
        color=RGBColor(27, 39, 51),
    )
    _add_text_box(
        slide,
        left=0.57,
        top=0.78,
        width=8.5,
        height=0.26,
        text=subtitle,
        font_size=11,
        color=RGBColor(90, 99, 108),
    )
    line = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.RECTANGLE,
        Inches(0.55),
        Inches(1.03),
        Inches(12.2),
        Inches(0.03),
    )
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(66, 126, 120)
    line.line.fill.background()


def _add_meta_bar(
    slide,
    entry: TemplateCatalogEntry,
    content: TemplateContent,
) -> None:
    text = (
        f"template_id: {entry.template_id}\n"
        f"method_id: {entry.method_id}\n"
        f"qcc_stage: {content.stage_label}\n"
        f"{{{{method_name}}}} | {{{{qcc_stage}}}} | {{{{demo_label}}}}"
    )
    _add_text_box(
        slide,
        left=7.05,
        top=1.45,
        width=5.15,
        height=1.25,
        text=text,
        font_size=12,
        color=RGBColor(45, 55, 65),
        fill=RGBColor(238, 244, 243),
        border=RGBColor(170, 195, 190),
    )


def _add_section_box(
    slide,
    *,
    left: float,
    top: float,
    width: float,
    height: float,
    title: str,
    items: tuple[str, ...],
) -> None:
    shape = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE,
        Inches(left),
        Inches(top),
        Inches(width),
        Inches(height),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(248, 249, 247)
    shape.line.color.rgb = RGBColor(190, 196, 191)
    frame = shape.text_frame
    frame.clear()
    frame.margin_left = Inches(0.18)
    frame.margin_right = Inches(0.18)
    frame.margin_top = Inches(0.14)
    frame.vertical_anchor = MSO_ANCHOR.TOP
    paragraph = frame.paragraphs[0]
    run = paragraph.add_run()
    run.text = title
    run.font.bold = True
    run.font.size = Pt(15)
    run.font.color.rgb = RGBColor(27, 39, 51)
    for item in items:
        p = frame.add_paragraph()
        p.text = item
        p.level = 0
        p.font.size = Pt(11)
        p.font.color.rgb = RGBColor(45, 55, 65)


def _add_placeholder_panel(
    slide,
    entry: TemplateCatalogEntry,
    *,
    left: float,
    top: float,
) -> None:
    _add_section_box(
        slide,
        left=left,
        top=top,
        width=5.35,
        height=4.6,
        title="Reserved placeholders",
        items=tuple(f"{{{{{name}}}}}" for name in entry.expected_placeholders),
    )


def _add_badge(slide, text: str, left: float, top: float, width: float) -> None:
    shape = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE,
        Inches(left),
        Inches(top),
        Inches(width),
        Inches(0.36),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(255, 242, 204)
    shape.line.color.rgb = RGBColor(214, 159, 46)
    frame = shape.text_frame
    frame.clear()
    frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    paragraph = frame.paragraphs[0]
    paragraph.alignment = PP_ALIGN.CENTER
    run = paragraph.add_run()
    run.text = text
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(102, 75, 17)


def _add_footer(slide, entry: TemplateCatalogEntry) -> None:
    _add_text_box(
        slide,
        left=0.6,
        top=6.95,
        width=11.9,
        height=0.25,
        text=(
            f"{entry.template_id} | {entry.method_id} | "
            "Final data-dependent evidence belongs in the evidence package."
        ),
        font_size=8,
        color=RGBColor(105, 112, 119),
    )


def _add_text_box(
    slide,
    *,
    left: float,
    top: float,
    width: float,
    height: float,
    text: str,
    font_size: int,
    color: RGBColor,
    bold: bool = False,
    fill: RGBColor | None = None,
    border: RGBColor | None = None,
) -> None:
    box = slide.shapes.add_textbox(
        Inches(left),
        Inches(top),
        Inches(width),
        Inches(height),
    )
    if fill is not None:
        box.fill.solid()
        box.fill.fore_color.rgb = fill
    if border is not None:
        box.line.color.rgb = border
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0.08)
    frame.margin_right = Inches(0.08)
    paragraph = frame.paragraphs[0]
    run = paragraph.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color


if __name__ == "__main__":
    main()
