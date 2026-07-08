from pathlib import Path

from qcc_toolkit.methods import FIRST_SLICE_METHODS


def test_first_slice_excludes_deferred_product_surfaces() -> None:
    repo_text = "\n".join(
        path.read_text(errors="ignore")
        for root in [Path("qcc_toolkit"), Path("examples"), Path("docs/methods")]
        for path in root.rglob("*")
        if path.is_file()
    ).lower()

    forbidden_phrases = [
        "fastapi",
        "django",
        "flask",
        "streamlit",
        "capa workflow",
        "eqms workflow",
        "automated pptx generation",
        "ai-generated conclusion",
    ]
    for phrase in forbidden_phrases:
        assert phrase not in repo_text

    assert all(method.method_id != "control_chart" for method in FIRST_SLICE_METHODS)
