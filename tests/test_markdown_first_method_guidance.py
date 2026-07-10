from pathlib import Path

PARETO_METHOD = Path("method-kits/pareto-chart.md")
PARETO_METADATA = Path("method-kits/metadata/pareto-chart.yml")
PARETO_MEDIA_DIR = Path("docs/media/pareto-chart")
PARETO_PROMPT_DIR = Path("docs/media/prompts/pareto-chart")
NEXT_METHOD_KITS = {
    "flowchart": {
        "title": "Flowchart / Process Map",
        "media": ("current-state-process-flow", "good-vs-weak-process-map"),
        "required_terms": (
            "start and end boundaries",
            "decision points",
            "handoffs",
            "queues",
            "rework loops",
            "failure or defect locations",
            "current state",
            "future state",
        ),
    },
    "histogram": {
        "title": "Histogram",
        "media": ("conceptual-distribution", "good-vs-weak-histogram"),
        "required_terms": (
            "numeric observations",
            "sample size",
            "bin width",
            "outliers",
            "distribution shape",
            "before/after",
            "does not prove process stability",
        ),
    },
    "scatter-diagram": {
        "title": "Scatter Diagram",
        "media": ("paired-variable-pattern", "good-vs-weak-scatter"),
        "required_terms": (
            "paired numeric observations",
            "x variable",
            "y variable",
            "axis labels",
            "units",
            "outlier",
            "correlation",
            "does not prove root cause",
        ),
    },
}
METHOD_GUIDE_TEMPLATE = Path("docs/templates/method-guide.md")
METHOD_METADATA_TEMPLATE = Path("docs/templates/method-metadata.yml")
IMAGE_PROMPT_TEMPLATE = Path("docs/templates/image-prompts.md")
EVIDENCE_LEVELS = Path("docs/evidence/evidence-levels.md")
EVIDENCE_NOTE_TEMPLATE = Path("docs/evidence/evidence-note-template.md")
CHART_QUALITY_STANDARD = Path("docs/chart-creation/chart-quality-standard.md")
TOOL_SELECTION_GUIDE = Path("docs/tool-guidance/tool-selection.md")
QCC_PROJECT_STORY = Path("docs/qcc-project-story.md")


def _read(path: Path) -> str:
    assert path.exists(), f"missing required M1 artifact: {path}"
    return path.read_text()


def _metadata(path: Path) -> dict[str, str]:
    text = _read(path)
    parsed: dict[str, str] = {}
    for line in text.splitlines():
        if not line or line.startswith("  "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key] = value.strip()
    return parsed


def test_method_guide_template_defines_readable_opening_metadata_and_sections() -> None:
    metadata = _metadata(METHOD_METADATA_TEMPLATE)
    text = _read(METHOD_GUIDE_TEMPLATE)

    assert text.startswith("# Method Name\n")
    assert not text.startswith("---\n")
    for visible_text in (
        "Status: draft",
        "Guide version: 0.1.0",
        "Evidence risk: medium",
        "Metadata:",
    ):
        assert visible_text in text

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
        assert key in metadata, f"method metadata template missing {key}"

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
        "## Prompt record path",
        "## Output file",
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


def test_qcc_project_story_guide_connects_methods_across_project_flow() -> None:
    text = _read(QCC_PROJECT_STORY)
    readme = _read(Path("README.md"))

    assert "# QCC Project Story" in text
    assert "[QCC Project Story](docs/qcc-project-story.md)" in readme

    for heading in (
        "## Purpose",
        "## Project story map",
        "## Problem selection",
        "## Current-state grasp",
        "## Cause analysis",
        "## Countermeasure planning",
        "## Verification",
        "## Standardization and control",
        "## Evidence handoff",
        "## Review checklist",
        "## Method links",
    ):
        assert heading in text, f"project-story guide missing {heading}"

    for stage in (
        "problem selection",
        "current-state grasp",
        "cause analysis",
        "countermeasure planning",
        "verification",
        "standardization",
    ):
        assert stage in text.lower()

    for method in (
        "Pareto Chart",
        "Check Sheet",
        "Fishbone Diagram",
        "5 Whys",
        "5W2H",
    ):
        assert method in text

    for required_boundary in (
        "Markdown method guides govern method knowledge",
        "Generated or teaching images are conceptual aids only",
        (
            "Final charts need source data, scope, assumptions, interpretation, "
            "and review status"
        ),
        "Do not start with a chart type before the project question is clear",
        "Do not treat the tallest Pareto bar as root cause",
        "Do not treat an action list as verified improvement",
    ):
        assert required_boundary in text


def test_pareto_method_kit_contains_required_assets_and_prompts() -> None:
    required_paths = (
        PARETO_METHOD,
        PARETO_METADATA,
        PARETO_PROMPT_DIR / "pareto-chart-concept-v0.1.md",
        PARETO_PROMPT_DIR / "pareto-chart-good-bad-layout-v0.1.md",
        PARETO_MEDIA_DIR / "pareto-chart-concept-v0.1.png",
        PARETO_MEDIA_DIR / "pareto-chart-good-bad-layout-v0.1.png",
    )

    for path in required_paths:
        assert path.exists(), f"missing Pareto kit asset: {path}"

    assert not Path("method-kits/pareto-chart").exists()

    method_text = _read(PARETO_METHOD)
    metadata_text = _read(PARETO_METADATA)
    assert method_text.startswith("# Pareto Chart\n")
    assert not method_text.startswith("---\n")
    assert "method_id: pareto_chart" not in method_text
    assert "method_id: pareto_chart" in metadata_text
    assert "Metadata: [method-kits/metadata/pareto-chart.yml]" in method_text
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

    prompt = "\n".join(
        _read(path)
        for path in (
            PARETO_PROMPT_DIR / "pareto-chart-concept-v0.1.md",
            PARETO_PROMPT_DIR / "pareto-chart-good-bad-layout-v0.1.md",
        )
    )
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
        "![Pareto concept visual]"
        "(../docs/media/pareto-chart/pareto-chart-concept-v0.1.png)",
        "![Good and weak Pareto layout comparison]"
        "(../docs/media/pareto-chart/pareto-chart-good-bad-layout-v0.1.png)",
    ):
        assert visual_name in method_text

    for visual_name in (
        "pareto-chart-concept-v0.1.png",
        "pareto-chart-good-bad-layout-v0.1.png",
    ):
        assert visual_name in prompt


def test_media_assets_have_matching_per_image_prompt_records() -> None:
    method_text = _read(PARETO_METHOD)
    image_paths = sorted(PARETO_MEDIA_DIR.glob("*.png"))
    prompt_paths = sorted(PARETO_PROMPT_DIR.glob("*.md"))

    assert image_paths, "Pareto media directory should contain teaching images"
    assert {path.stem for path in image_paths} == {path.stem for path in prompt_paths}

    for image_path in image_paths:
        prompt_path = PARETO_PROMPT_DIR / f"{image_path.stem}.md"
        prompt_text = _read(prompt_path)

        output_reference = image_path.as_posix()
        prompt_reference = prompt_path.as_posix()
        guide_image_reference = f"../{output_reference}"
        guide_prompt_reference = f"../{prompt_reference}"

        assert output_reference in prompt_text
        assert prompt_reference in prompt_text
        assert guide_image_reference in method_text
        assert guide_prompt_reference in method_text


def test_next_basic_quality_tool_method_kits_have_required_sections() -> None:
    shared_headings = (
        "## Summary",
        "## QCC stage fit",
        "## What question this method answers",
        "## When to use",
        "## When not to use",
        "## Required inputs",
        "## Output",
        "## Manual chart or diagram recipe",
        "## Quality standards",
        "## Interpretation limits",
        "## Common mistakes",
        "## Evidence note",
        "## Review checklist",
        "## Image-assisted demonstration notes",
        "## Related methods",
    )

    for method_id, config in NEXT_METHOD_KITS.items():
        text = _read(Path(f"method-kits/{method_id}.md"))

        for heading in shared_headings:
            assert heading in text, f"{method_id} missing {heading}"

        for metadata_key in (
            "Method ID:",
            "Method name:",
            "Method type:",
            "QCC stages:",
            "Status:",
            "Guide version:",
            "Image policy:",
            "Automation policy:",
        ):
            assert metadata_key in text, f"{method_id} missing {metadata_key}"

        lowered = text.lower()
        for required_term in config["required_terms"]:
            assert required_term.lower() in lowered, (
                f"{method_id} missing {required_term}"
            )

        assert "Generated visuals are not final evidence" in text
        assert "Control Chart" not in text
        assert "control limit" not in lowered
        assert "process capability" not in lowered


def test_next_basic_quality_tool_prompt_records_and_media_are_linked() -> None:
    for method_id, config in NEXT_METHOD_KITS.items():
        kit_text = _read(Path(f"method-kits/{method_id}.md"))

        for image_id in config["media"]:
            media_path = Path(f"docs/media/{method_id}/{image_id}.png")
            prompt_path = Path(f"docs/media/prompts/{method_id}/{image_id}.md")
            media_ref = media_path.as_posix()
            prompt_ref = prompt_path.as_posix()

            assert media_path.exists(), f"missing media asset: {media_path}"
            assert prompt_path.exists(), f"missing prompt record: {prompt_path}"
            assert media_path.stat().st_size > 100_000, (
                f"media asset looks unexpectedly small: {media_path}"
            )

            prompt_text = _read(prompt_path)
            prompt_lower = prompt_text.lower()
            for heading in (
                "## Purpose",
                "## Intended use",
                "## Final prompt",
                "## Negative constraints",
                "## Conceptual-only policy",
                "## Manual review",
            ):
                assert heading in prompt_text, f"{prompt_path} missing {heading}"

            assert "not final project evidence" in prompt_lower, (
                f"{prompt_path} missing final-evidence boundary"
            )
            assert "review status: passed" in prompt_lower, (
                f"{prompt_path} missing passed review status"
            )
            for required_phrase in (media_ref, prompt_ref):
                assert required_phrase in prompt_text, (
                    f"{prompt_path} missing {required_phrase}"
                )

            for forbidden_phrase in (
                "fake percentages",
                "private",
                "credentials",
                "final-evidence appearance",
            ):
                assert forbidden_phrase in prompt_lower

            assert f"../{media_ref}" in kit_text
            assert f"../{prompt_ref}" in kit_text


def test_next_basic_quality_tool_navigation_links_story_fit_and_scope_guards() -> None:
    readme = _read(Path("README.md"))
    story = _read(QCC_PROJECT_STORY)
    story_lower = story.lower()
    combined_nav = f"{readme}\n{story}"

    expected_links = {
        "Flowchart / Process Map": "method-kits/flowchart.md",
        "Histogram": "method-kits/histogram.md",
        "Scatter Diagram": "method-kits/scatter-diagram.md",
    }
    for title, readme_link in expected_links.items():
        story_link = f"../{readme_link}"
        assert f"[{title}]({readme_link})" in readme
        assert f"[{title}]({story_link})" in story

    for required_story_text in (
        "process sequence, handoff, queue, rework, or decision flow",
        "numeric spread, shape, or outlier behavior",
        "paired numeric variables appear related",
        "does not prove root cause",
        "does not prove process stability",
        "generated visuals remain conceptual teaching aids",
    ):
        assert required_story_text in story_lower

    forbidden_scope_terms = (
        "SPC rules",
        "control-limit",
        "control limits",
        "process capability",
        "run-rule automation",
        "Histogram renderer",
        "Scatter renderer",
    )
    for forbidden in forbidden_scope_terms:
        assert forbidden not in combined_nav

    assert "Control Chart" not in readme
    assert "Control Chart" not in story


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
