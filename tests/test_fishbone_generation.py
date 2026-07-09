from pathlib import Path

from qcc_toolkit.fishbone import FishboneBranch, FishboneCause, render_fishbone_svg


def test_render_fishbone_svg_creates_readable_static_diagram() -> None:
    svg = render_fishbone_svg(
        effect="Packing label defects increased on Line 2",
        branches=(
            FishboneBranch(
                name="Method",
                causes=(
                    FishboneCause("Late label check", status="S"),
                    FishboneCause("Missing check step", status="V?"),
                ),
            ),
            FishboneBranch(
                name="Machine",
                causes=(FishboneCause("Scanner warning hidden", status="V?"),),
            ),
            FishboneBranch(
                name="People",
                causes=(FishboneCause("New operators rotate in", status="S"),),
            ),
        ),
        source_note="Synthetic QCC demo",
    )

    assert svg.startswith("<svg ")
    assert "QCC Toolkit Python-generated Fishbone Diagram" in svg
    assert "Packing label defects increased on Line 2" in svg
    assert "Late label check" in svg
    assert "Scanner warning hidden" in svg
    assert "status-badge selected" in svg
    assert "short cause labels" in svg
    assert "hypotheses until verified" in svg
    assert "Synthetic QCC demo" in svg
    assert len(svg) > 4000


def test_render_fishbone_svg_rejects_invalid_status() -> None:
    try:
        render_fishbone_svg(
            effect="Effect",
            branches=(
                FishboneBranch(
                    name="Method",
                    causes=(FishboneCause("Cause", status="unknown"),),
                ),
            ),
        )
    except ValueError as exc:
        assert "status must be one of" in str(exc)
    else:
        raise AssertionError("Expected invalid status to fail.")


def test_render_fishbone_svg_writes_file(tmp_path: Path) -> None:
    output = tmp_path / "fishbone.svg"
    svg = render_fishbone_svg(
        effect="Effect",
        branches=(
            FishboneBranch(
                name="Method",
                causes=(FishboneCause("Short cause", status="S"),),
            ),
        ),
        output_path=output,
    )

    assert output.read_text() == svg
