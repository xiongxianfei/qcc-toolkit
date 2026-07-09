import re
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
    assert 'data-layout="fixed-lanes"' in svg
    assert 'data-visible-causes-per-branch="2"' in svg
    assert 'data-lane="top"' in svg
    assert 'data-lane="bottom"' in svg
    assert 'class="cause-box"' in svg
    assert len(svg) > 4000


def test_render_fishbone_svg_uses_non_overlapping_lane_boxes() -> None:
    svg = render_fishbone_svg(
        effect="Packing label defects increased on Line 2",
        branches=(
            FishboneBranch(
                name="Method",
                causes=(
                    FishboneCause("Late label check", status="S"),
                    FishboneCause("Missing check step", status="V?"),
                    FishboneCause("Hidden third cause", status="S"),
                ),
            ),
            FishboneBranch(
                name="Machine",
                causes=(
                    FishboneCause("Scanner warning hidden", status="V?"),
                    FishboneCause("Printer alert unclear", status="S"),
                ),
            ),
            FishboneBranch(
                name="Material",
                causes=(
                    FishboneCause("Similar roll colors", status="S"),
                    FishboneCause("Mixed label stock", status="S"),
                ),
            ),
            FishboneBranch(
                name="People",
                causes=(
                    FishboneCause("New operators rotate in", status="S"),
                    FishboneCause("Training check missing", status="V?"),
                ),
            ),
            FishboneBranch(
                name="Environment",
                causes=(
                    FishboneCause("Mixed SKU paperwork", status="V?"),
                    FishboneCause("Crowded pack table", status="S"),
                ),
            ),
            FishboneBranch(
                name="Measurement",
                causes=(
                    FishboneCause("Audit form mismatch", status="X"),
                    FishboneCause("Defect codes unclear", status="S"),
                ),
            ),
        ),
    )

    boxes = [
        tuple(map(int, match))
        for match in re.findall(
            r'data-box="(\d+),(\d+),(\d+),(\d+)" class="cause-box"',
            svg,
        )
    ]
    assert len(boxes) == 12
    assert "Hidden third cause" not in svg
    assert all(x + width <= 1010 for x, _y, width, _height in boxes)
    assert all(y < 330 or y > 430 for _x, y, _width, _height in boxes)

    for index, first in enumerate(boxes):
        for second in boxes[index + 1 :]:
            assert not _overlaps(first, second)


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


def _overlaps(
    first: tuple[int, int, int, int],
    second: tuple[int, int, int, int],
) -> bool:
    first_x, first_y, first_width, first_height = first
    second_x, second_y, second_width, second_height = second
    return not (
        first_x + first_width <= second_x
        or second_x + second_width <= first_x
        or first_y + first_height <= second_y
        or second_y + second_height <= first_y
    )
