from pathlib import Path

from examples.scripts import generate_fishbone


def test_generate_fishbone_script_writes_svg_and_readme(tmp_path: Path) -> None:
    output_dir = tmp_path / "fishbone"

    exit_code = generate_fishbone.main(["--output", str(output_dir)])

    assert exit_code == 0
    svg = output_dir / "fishbone.svg"
    readme = output_dir / "README.md"
    assert svg.exists()
    assert readme.exists()

    svg_text = svg.read_text()
    assert "QCC Toolkit Python-generated Fishbone Diagram" in svg_text
    assert "Packing label defects increased on Line 2" in svg_text
    assert "Clean static SVG" in readme.read_text()


def test_generate_fishbone_script_rejects_existing_file_output(tmp_path: Path) -> None:
    output = tmp_path / "not-a-folder"
    output.write_text("x")

    exit_code = generate_fishbone.main(["--output", str(output)])

    assert exit_code != 0
    assert output.read_text() == "x"
