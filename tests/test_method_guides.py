from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS, get_method

GUIDE_DIR = Path("docs/methods")

REQUIRED_SECTIONS = (
    "## Summary",
    "## QCC stage fit",
    "## When to use",
    "## When not to use",
    "## Inputs required",
    "## Outputs produced",
    "## Procedure",
    "## Interpretation guidance",
    "## Common mistakes",
    "## Example",
    "## Related methods",
    "## Formula or logic notes",
    "## Review checklist",
)

TEMPLATE_NATIVE_METHODS = (
    "5w2h",
    "5_whys",
    "check_sheet",
    "fishbone_diagram",
)


def _front_matter(path: Path) -> dict[str, object]:
    text = path.read_text()
    assert text.startswith("---\n")
    _, front_matter, _body = text.split("---\n", 2)
    parsed: dict[str, object] = {}
    current_key: str | None = None
    for line in front_matter.splitlines():
        if line.startswith("  - "):
            assert current_key is not None
            value = parsed.setdefault(current_key, [])
            assert isinstance(value, list)
            value.append(line.removeprefix("  - "))
            continue
        key, value = line.split(":", 1)
        current_key = key
        parsed[key] = [] if not value.strip() else value.strip()
    return parsed


def test_first_slice_method_guides_have_contract_front_matter() -> None:
    for method in FIRST_SLICE_METHODS:
        path = GUIDE_DIR / f"{method.method_id}.md"
        front_matter = _front_matter(path)

        assert front_matter["method_id"] == method.method_id
        assert front_matter["method_name"] == method.name
        assert front_matter["method_type"] == method.method_type.value
        assert front_matter["supports_generated_chart"] == str(
            method.supports_generated_chart
        ).lower()
        assert front_matter["first_slice_status"] == method.first_slice_status
        assert tuple(front_matter["qcc_stages"]) == method.qcc_stages
        assert get_method(str(front_matter["method_id"])) == method


def test_first_slice_method_guides_include_required_sections() -> None:
    for method in FIRST_SLICE_METHODS:
        text = (GUIDE_DIR / f"{method.method_id}.md").read_text()

        for heading in REQUIRED_SECTIONS:
            assert heading in text, f"{method.method_id} missing {heading}"


def test_pareto_guide_documents_supported_input_shapes_and_formula() -> None:
    text = (GUIDE_DIR / "pareto_chart.md").read_text()

    for required_text in (
        "event-record data",
        "category-count data",
        "percentage",
        "cumulative_count",
        "cumulative_percentage",
        "sort order",
        "descending count",
        "case-insensitive category name",
    ):
        assert required_text in text


def test_pareto_guide_contains_powerpoint_first_method_kit_guidance() -> None:
    text = (GUIDE_DIR / "pareto_chart.md").read_text()

    for required_heading in (
        "## Purpose",
        "## PowerPoint template workflow",
        "## PowerPoint edit instructions",
        "## Blank copyable project slide",
        "## Interpretation patterns",
        "## Python assist decision",
        "## Evidence levels and source notes",
    ):
        assert required_heading in text

    for required_text in (
        "vital few",
        "non-overlapping",
        "consistent data period",
        "Right-click the chart",
        "Edit Data",
        "sort counts descending",
        "formula cells were not overwritten",
        "largest contributor",
        "top-three share",
        "next action",
        "Level 1",
        "Level 2",
        "Level 3",
        "Level 4",
    ):
        assert required_text in text


def test_template_native_guides_contain_method_kit_guidance() -> None:
    for method_id in TEMPLATE_NATIVE_METHODS:
        text = (GUIDE_DIR / f"{method_id}.md").read_text()

        for required_heading in (
            "## Purpose",
            "## PowerPoint template workflow",
            "## Blank working slide or worksheet",
            "## Interpretation patterns",
            "## Python assist decision",
            "## Evidence levels and source notes",
        ):
            assert required_heading in text, f"{method_id} missing {required_heading}"

        for required_text in (
            "DEMO EXAMPLE - not project evidence",
            "PowerPoint is enough",
            "source",
            "date range",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "facilitator checklist",
        ):
            assert required_text in text, f"{method_id} missing {required_text}"
