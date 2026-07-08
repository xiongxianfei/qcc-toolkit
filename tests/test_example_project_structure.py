from pathlib import Path

PROJECT = Path("examples/projects/reduce-packing-label-errors")


def test_reduce_packing_label_errors_project_has_expected_structure() -> None:
    assert PROJECT.exists()
    assert (PROJECT / "README.md").exists()
    assert (PROJECT / "data" / "packing_label_defects.csv").exists()
    assert (PROJECT / "evidence").exists()
    assert Path("examples/scripts/generate_pareto.py").exists()

    readme = (PROJECT / "README.md").read_text()
    assert "reduce-packing-label-errors" in readme
    assert "generate_pareto.py" in readme
    assert "evidence/pareto" in readme
