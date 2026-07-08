import json
from pathlib import Path

import pytest

from examples.scripts import generate_pareto


def test_generate_pareto_script_delegates_to_public_api(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    input_path = tmp_path / "defects.csv"
    output_path = tmp_path / "project" / "evidence" / "pareto"
    input_path.write_text("defect_type,count\nWrong label,4\nSmudged print,2\n")

    calls: list[tuple[str, object]] = []

    def fake_calculate_pareto(records: object, parameters: object) -> object:
        calls.append(("calculate", parameters))
        assert list(records) == [
            {"defect_type": "Wrong label", "count": 4.0},
            {"defect_type": "Smudged print", "count": 2.0},
        ]
        return object()

    def fake_write_pareto_evidence_package(
        result: object,
        output_dir: Path,
        *,
        input_context: object,
        overwrite: bool,
    ) -> object:
        calls.append(("write", input_context))
        assert output_dir == output_path
        assert overwrite is True
        output_dir.mkdir(parents=True)
        (output_dir / "metadata.json").write_text(json.dumps({"status": "success"}))
        return result

    monkeypatch.setattr(generate_pareto, "calculate_pareto", fake_calculate_pareto)
    monkeypatch.setattr(
        generate_pareto,
        "write_pareto_evidence_package",
        fake_write_pareto_evidence_package,
    )

    exit_code = generate_pareto.main(
        [
            "--input",
            str(input_path),
            "--category-column",
            "defect_type",
            "--count-column",
            "count",
            "--project",
            str(tmp_path / "project"),
            "--output",
            str(output_path),
        ]
    )

    assert exit_code == 0
    assert [name for name, _payload in calls] == ["calculate", "write"]


def test_generate_pareto_script_rejects_missing_input_file(tmp_path: Path) -> None:
    output_path = tmp_path / "project" / "evidence" / "pareto"

    exit_code = generate_pareto.main(
        [
            "--input",
            str(tmp_path / "missing.csv"),
            "--category-column",
            "defect_type",
            "--count-column",
            "count",
            "--project",
            str(tmp_path / "project"),
            "--output",
            str(output_path),
        ]
    )

    assert exit_code != 0
    assert not output_path.exists()
