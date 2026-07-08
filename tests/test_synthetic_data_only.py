from pathlib import Path


def test_examples_are_marked_synthetic_and_exclude_private_data_markers() -> None:
    example_root = Path("examples/projects/reduce-packing-label-errors")
    text = "\n".join(
        path.read_text() for path in example_root.rglob("*") if path.is_file()
    )

    assert "synthetic" in text.lower()
    banned_markers = [
        "customer name",
        "employee id",
        "patient",
        "supplier confidential",
        "real production",
    ]
    for marker in banned_markers:
        assert marker not in text.lower()
