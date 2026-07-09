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
    assert 'data-architecture="four-layer"' in svg
    assert 'data-visible-causes-per-branch="2"' in svg
    assert 'data-lane="top"' in svg
    assert 'data-lane="bottom"' in svg
    assert 'class="cause-box"' in svg
    assert len(svg) > 4000


def test_render_fishbone_svg_exposes_four_layer_architecture() -> None:
    svg = render_fishbone_svg(
        effect="Packing label defects increased on Line 2",
        branches=(
            FishboneBranch(
                name="Method",
                causes=(FishboneCause("Late label check", status="S"),),
            ),
            FishboneBranch(
                name="Machine",
                causes=(FishboneCause("Scanner warning hidden", status="V?"),),
            ),
        ),
        source_note="Synthetic QCC demo",
    )

    for required_text in (
        "Four-layer architecture",
        "Layer 1: effect",
        "Layer 2: branch category",
        "Layer 3: short visible cause",
        "Layer 4: verification detail",
        "Keep Layer 4 out of the diagram body",
    ):
        assert required_text in svg

    assert 'data-layer="1-effect"' in svg
    assert 'data-layer="2-branch-category"' in svg
    assert 'data-layer="3-short-visible-cause"' in svg
    assert 'data-layer="4-verification-detail"' in svg


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
            r'data-box="(\d+),(\d+),(\d+),(\d+)"[^>]*class="cause-box"',
            svg,
        )
    ]
    labels = [
        tuple(map(int, match))
        for match in re.findall(
            r'data-label-box="(\d+),(\d+),(\d+),(\d+)"[^>]*class="branch-label"',
            svg,
        )
    ]
    assert len(boxes) == 12
    assert len(labels) == 6
    assert "Hidden third cause" not in svg
    assert all(x + width <= 1010 for x, _y, width, _height in boxes)
    assert all(y < 330 or y > 430 for _x, y, _width, _height in boxes)
    assert all(y < 430 or y > 540 for _x, y, _width, _height in labels)

    for index, first in enumerate(boxes):
        for second in boxes[index + 1 :]:
            assert not _overlaps(first, second)
    for label in labels:
        for box in boxes:
            assert not _overlaps(label, box)


def test_render_fishbone_svg_keeps_connectors_outside_text_boxes() -> None:
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
            r'data-box="(\d+),(\d+),(\d+),(\d+)"[^>]*class="cause-box"',
            svg,
        )
    ]
    labels = [
        tuple(map(int, match))
        for match in re.findall(
            r'data-label-box="(\d+),(\d+),(\d+),(\d+)"[^>]*class="branch-label"',
            svg,
        )
    ]
    connectors = [
        tuple(map(int, match))
        for match in re.findall(
            r'data-connector="[^"]+" x1="(\d+)" y1="(\d+)" x2="(\d+)" y2="(\d+)"',
            svg,
        )
    ]

    assert len(connectors) >= 19
    text_regions = boxes + labels
    for connector in connectors:
        for region in text_regions:
            assert not _line_crosses_rect(connector, region)


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


def _line_crosses_rect(
    line: tuple[int, int, int, int],
    rect: tuple[int, int, int, int],
) -> bool:
    x1, y1, x2, y2 = line
    rect_x, rect_y, width, height = rect
    left = rect_x
    right = rect_x + width
    top = rect_y
    bottom = rect_y + height

    if _point_inside_rect(x1, y1, rect) or _point_inside_rect(x2, y2, rect):
        return True
    edges = (
        (left, top, right, top),
        (right, top, right, bottom),
        (right, bottom, left, bottom),
        (left, bottom, left, top),
    )
    return any(_segments_intersect(line, edge) for edge in edges)


def _point_inside_rect(x: int, y: int, rect: tuple[int, int, int, int]) -> bool:
    rect_x, rect_y, width, height = rect
    return rect_x < x < rect_x + width and rect_y < y < rect_y + height


def _segments_intersect(
    first: tuple[int, int, int, int],
    second: tuple[int, int, int, int],
) -> bool:
    a_x, a_y, b_x, b_y = first
    c_x, c_y, d_x, d_y = second

    def orientation(p_x: int, p_y: int, q_x: int, q_y: int, r_x: int, r_y: int) -> int:
        value = (q_y - p_y) * (r_x - q_x) - (q_x - p_x) * (r_y - q_y)
        if value == 0:
            return 0
        return 1 if value > 0 else 2

    def on_segment(p_x: int, p_y: int, q_x: int, q_y: int, r_x: int, r_y: int) -> bool:
        return (
            min(p_x, r_x) <= q_x <= max(p_x, r_x)
            and min(p_y, r_y) <= q_y <= max(p_y, r_y)
        )

    first_orientation = orientation(a_x, a_y, b_x, b_y, c_x, c_y)
    second_orientation = orientation(a_x, a_y, b_x, b_y, d_x, d_y)
    third_orientation = orientation(c_x, c_y, d_x, d_y, a_x, a_y)
    fourth_orientation = orientation(c_x, c_y, d_x, d_y, b_x, b_y)

    if (
        first_orientation != second_orientation
        and third_orientation != fourth_orientation
    ):
        return True
    if first_orientation == 0 and on_segment(a_x, a_y, c_x, c_y, b_x, b_y):
        return True
    if second_orientation == 0 and on_segment(a_x, a_y, d_x, d_y, b_x, b_y):
        return True
    if third_orientation == 0 and on_segment(c_x, c_y, a_x, a_y, d_x, d_y):
        return True
    if fourth_orientation == 0 and on_segment(c_x, c_y, b_x, b_y, d_x, d_y):
        return True
    return False
