from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS, get_method

CANONICAL_METHOD_KITS = {
    "pareto_chart": Path("method-kits/pareto-chart.md"),
    "check_sheet": Path("method-kits/check-sheet.md"),
    "5w2h": Path("method-kits/five-w-two-h.md"),
    "fishbone_diagram": Path("method-kits/fishbone-diagram.md"),
    "5_whys": Path("method-kits/five-whys.md"),
}


def test_legacy_method_guide_directory_has_no_active_guides() -> None:
    assert not any(Path("docs/methods").glob("*.md"))


def test_first_slice_methods_have_canonical_method_kits() -> None:
    for method in FIRST_SLICE_METHODS:
        path = CANONICAL_METHOD_KITS[method.method_id]
        assert path.exists()
        text = path.read_text()
        assert method.name in text
        assert get_method(method.method_id) == method


def test_template_native_method_kits_state_manual_guidance_first() -> None:
    for method_id in ("5w2h", "5_whys", "check_sheet", "fishbone_diagram"):
        text = CANONICAL_METHOD_KITS[method_id].read_text()

        assert "Automation policy:" in text
        assert "manual" in text
        assert "## Evidence note" in text
        assert "review checklist" in text.lower()
