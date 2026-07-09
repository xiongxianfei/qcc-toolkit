from pathlib import Path


METHOD_TEMPLATE_DIR = Path("method-kits/_template")
METHOD_GUIDE_TEMPLATE = METHOD_TEMPLATE_DIR / "method-guide.md"
CHART_GUIDE_TEMPLATE = METHOD_TEMPLATE_DIR / "chart-creation-guide.md"
REVIEW_CHECKLIST_TEMPLATE = METHOD_TEMPLATE_DIR / "review-checklist.md"
IMAGE_PROMPT_TEMPLATE = METHOD_TEMPLATE_DIR / "image-prompts" / "concept-visual.md"
TEACHING_VISUAL_DIR = METHOD_TEMPLATE_DIR / "assets" / "teaching-visuals"
EVIDENCE_LEVELS = Path("docs/evidence/evidence-levels.md")
EVIDENCE_NOTE_TEMPLATE = Path("docs/evidence/evidence-note-template.md")
CHART_QUALITY_STANDARD = Path("docs/chart-creation/chart-quality-standard.md")
TOOL_SELECTION_GUIDE = Path("docs/tool-guidance/tool-selection.md")


def _read(path: Path) -> str:
    assert path.exists(), f"missing required M1 artifact: {path}"
    return path.read_text()


def _front_matter(path: Path) -> dict[str, str]:
    text = _read(path)
    assert text.startswith("---\n"), f"{path} missing YAML front matter"
    _prefix, front_matter, _body = text.split("---\n", 2)
    parsed: dict[str, str] = {}
    for line in front_matter.splitlines():
        if not line or line.startswith("  "):
            continue
        key, value = line.split(":", 1)
        parsed[key] = value.strip()
    return parsed


def test_method_guide_template_defines_required_front_matter_and_sections() -> None:
    front_matter = _front_matter(METHOD_GUIDE_TEMPLATE)
    text = _read(METHOD_GUIDE_TEMPLATE)

    for key in (
        "method_id",
        "method_name",
        "qcc_stages",
        "method_type",
        "primary_output",
        "evidence_risk",
        "imagegen_allowed",
        "final_chart_generation",
        "related_methods",
        "guide_version",
        "review_status",
    ):
        assert key in front_matter, f"method-guide template missing {key}"

    for heading in (
        "## Summary",
        "## QCC stage fit",
        "## What question this method answers",
        "## When to use",
        "## When not to use",
        "## Required inputs",
        "## Output",
        "## Manual chart or worksheet recipe",
        "## Quality standards",
        "## Interpretation guide",
        "## Example conclusion wording",
        "## Common mistakes",
        "## Review checklist",
        "## Evidence note for final charts",
        "## Image-assisted demonstration notes",
        "## Related methods",
    ):
        assert heading in text, f"method-guide template missing {heading}"

    assert "teach application" in text
    assert "not only define the method" in text


def test_chart_creation_template_and_quality_standard_cover_manual_chart_recipe() -> None:
    template_text = _read(CHART_GUIDE_TEMPLATE)
    standard_text = _read(CHART_QUALITY_STANDARD)
    combined = f"{template_text}\n{standard_text}"

    for heading in (
        "## Chart purpose",
        "## Required data structure",
        "## Data preparation",
        "## Tool-selection guidance",
        "## Chart construction steps",
        "## Formatting standard",
        "## Required annotations",
        "## Interpretation rules",
        "## Common chart defects",
        "## Review checklist",
        "## Evidence note",
    ):
        assert heading in template_text, f"chart template missing {heading}"

    for required_text in (
        "clear title",
        "correct chart type",
        "readable labels",
        "source note",
        "correct scale",
        "appropriate annotations",
        "defensible interpretation",
    ):
        assert required_text in combined


def test_image_prompt_template_is_conceptual_only_and_reviewable() -> None:
    text = _read(IMAGE_PROMPT_TEMPLATE)
    assert TEACHING_VISUAL_DIR.exists()

    for heading in (
        "## Purpose",
        "## Use",
        "## Prompt",
        "## Negative constraints",
        "## Review checklist",
    ):
        assert heading in text, f"image prompt template missing {heading}"

    for required_text in (
        "conceptual only",
        "training and explanation only",
        "not final project evidence",
        "not a quantitative chart",
        "Do not include exact data values",
        "Do not include fake percentages",
        "Do not include misleading axes",
        "Keep detailed method instructions in Markdown",
    ):
        assert required_text in text


def test_evidence_levels_and_evidence_note_template_define_final_chart_support() -> None:
    levels = _read(EVIDENCE_LEVELS)
    note = _read(EVIDENCE_NOTE_TEMPLATE)

    for level in (
        "E0 - Concept",
        "E1 - Draft",
        "E2 - Project presentation",
        "E3 - Formal review",
        "E4 - Audit or high-risk",
    ):
        assert level in levels

    for required_text in (
        "conceptual only",
        "source data",
        "date range",
        "scope or filters",
        "reviewer checklist",
        "calculation table",
        "method guide version",
        "validated analysis path",
        "independent verification",
        "full reproducibility record",
    ):
        assert required_text in levels

    for field in (
        "- Method:",
        "- QCC stage:",
        "- Chart title:",
        "- Source data:",
        "- Data owner:",
        "- Date range:",
        "- Scope / filters:",
        "- Total sample or count:",
        "- Tool used:",
        "- Calculation table location:",
        "- Assumptions:",
        "- Exclusions:",
        "- Reviewer:",
        "- Review date:",
        "- Review status:",
    ):
        assert field in note


def test_tool_guidance_stays_tool_class_based_and_review_checklist_is_pass_fail() -> None:
    tool_text = _read(TOOL_SELECTION_GUIDE)
    checklist_text = _read(REVIEW_CHECKLIST_TEMPLATE)

    for tool_class in (
        "spreadsheet tools",
        "charting tools",
        "presentation tools",
        "statistical tools",
        "data-analysis tools",
        "diagramming tools",
    ):
        assert tool_class in tool_text

    for forbidden_named_tool in (
        "Excel",
        "PowerPoint",
        "Google Sheets",
        "Minitab",
        "Python",
    ):
        assert forbidden_named_tool not in tool_text

    for required_text in (
        "Pass",
        "Fail",
        "method purpose",
        "QCC stage fit",
        "source data",
        "review status",
        "conceptual only",
        "final quantitative evidence",
    ):
        assert required_text in checklist_text
