from pathlib import Path

PARETO_METHOD = Path("method-kits/pareto-chart.md")
PARETO_MEDIA_DIR = Path("media/pareto-chart")
METHOD_GUIDE_TEMPLATE = Path("docs/templates/method-guide.md")
IMAGE_PROMPT_TEMPLATE = Path("docs/templates/image-prompts.md")
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


def test_compact_guide_template_and_quality_standard_cover_manual_recipe() -> None:
    template_text = _read(METHOD_GUIDE_TEMPLATE)
    standard_text = _read(CHART_QUALITY_STANDARD)
    combined = f"{template_text}\n{standard_text}"

    for heading in (
        "## Manual chart or worksheet recipe",
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
        "## Evidence note for final charts",
    ):
        assert heading in template_text, f"compact guide template missing {heading}"

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

    for heading in (
        "## Concept visual prompt",
        "## Good/bad comparison prompt",
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


def test_evidence_levels_and_evidence_note_define_final_chart_support() -> None:
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


def test_tool_guidance_and_review_checklist_are_tool_class_based() -> None:
    tool_text = _read(TOOL_SELECTION_GUIDE)
    checklist_text = _read(METHOD_GUIDE_TEMPLATE)

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


def test_pareto_method_kit_contains_required_assets_and_prompts() -> None:
    required_paths = (
        PARETO_METHOD,
        PARETO_MEDIA_DIR / "prompts.md",
        PARETO_MEDIA_DIR / "pareto-chart-concept-v0.1.png",
        PARETO_MEDIA_DIR / "pareto-chart-good-bad-layout-v0.1.png",
    )

    for path in required_paths:
        assert path.exists(), f"missing Pareto kit asset: {path}"

    assert not Path("method-kits/pareto-chart").exists()

    method_text = _read(PARETO_METHOD)
    assert "method_id: pareto_chart" in method_text
    assert "Check Sheet" in method_text
    assert "Fishbone Diagram" in method_text
    assert "5 Whys" in method_text
    assert "chart-creation-guide.md" not in method_text
    assert "evidence-note-template.md" not in method_text

    for required_text in (
        "method purpose",
        "procedure",
        "interpretation",
        "common mistakes",
        "review checklist",
        "teaches application",
    ):
        assert required_text in method_text

    prompt = _read(PARETO_MEDIA_DIR / "prompts.md")
    for required_text in (
        "conceptual only",
        "training and explanation only",
        "not final project evidence",
        "Do not include exact data values",
        "Do not include fake percentages",
        "Keep detailed method instructions in Markdown",
    ):
        assert required_text in prompt

    for visual_name in (
        "![Pareto concept visual](../media/pareto-chart/pareto-chart-concept-v0.1.png)",
        "![Good and weak Pareto layout comparison]"
        "(../media/pareto-chart/pareto-chart-good-bad-layout-v0.1.png)",
    ):
        assert visual_name in method_text

    for visual_name in (
        "pareto-chart-concept-v0.1.png",
        "pareto-chart-good-bad-layout-v0.1.png",
    ):
        assert visual_name in prompt


def test_pareto_chart_creation_guide_defines_required_manual_rules() -> None:
    text = _read(PARETO_METHOD)

    for required_text in (
        "Chart construction steps",
        "categories and counts",
        "one consistent period and scope",
        "sort categories from largest to smallest",
        "descending count",
        "column bars",
        "optional cumulative percentage line",
        "capped at 100 percent",
        "source data",
        "date range",
        "scope or filters",
        "defensible interpretation",
    ):
        assert required_text in text

    for forbidden_named_tool in (
        "Excel",
        "PowerPoint",
        "Google Sheets",
        "Minitab",
    ):
        assert forbidden_named_tool not in text


def test_pareto_worked_example_is_synthetic_and_inline() -> None:
    worked = _read(PARETO_METHOD)
    for required_text in (
        "Synthetic sample data",
        "not project evidence",
        "Total count: 100",
        "Top category:",
        "Top three categories:",
        "next action",
        "Evidence level: E1",
    ):
        assert required_text in worked


def test_pareto_review_notes_distinguish_good_bad_and_evidence_readiness() -> None:
    combined = _read(PARETO_METHOD)
    checklist = _read(PARETO_METHOD)
    evidence_note = _read(PARETO_METHOD)

    for required_text in (
        "Reviewed teaching example",
        "conceptual only",
        "not final project evidence",
        "good example",
        "bad example",
        "clear title",
        "source note",
        "descending count",
        "missing source data",
        "mixed date ranges",
    ):
        assert required_text in combined

    for required_text in (
        "Pass",
        "Fail",
        "categories and counts",
        "one consistent period and scope",
        "source data",
        "review status",
    ):
        assert required_text in checklist

    for field in (
        "- Method: Pareto Chart",
        "- QCC stage:",
        "- Chart title:",
        "- Source data:",
        "- Date range:",
        "- Scope / filters:",
        "- Total sample or count:",
        "- Tool used:",
        "- Reviewer:",
        "- Review status:",
    ):
        assert field in evidence_note
