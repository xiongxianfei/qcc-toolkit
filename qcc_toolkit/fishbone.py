"""Python-generated Fishbone diagram assets."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import wrap

_STATUS_LABELS = {
    "S": ("suspected", "#eceff1", "#737d82", "#394247"),
    "V?": ("selected", "#fff2cc", "#d69f2e", "#664b11"),
    "V": ("verified", "#e2f1e8", "#4a9160", "#215c32"),
    "X": ("rejected", "#f6e6e2", "#ad5b4d", "#75342a"),
}


@dataclass(frozen=True)
class FishboneCause:
    """A short cause label and verification status for a Fishbone branch."""

    label: str
    status: str = "S"


@dataclass(frozen=True)
class FishboneBranch:
    """A major Fishbone branch with short cause labels."""

    name: str
    causes: tuple[FishboneCause, ...]


@dataclass(frozen=True)
class _BranchSlot:
    branch: FishboneBranch
    upper: bool
    spine_x: int
    tip_x: int
    tip_y: int
    lane: str
    lane_x: int
    lane_y: int


def render_fishbone_svg(
    *,
    effect: str,
    branches: tuple[FishboneBranch, ...],
    source_note: str = "",
    output_path: Path | None = None,
) -> str:
    """Render a clean static SVG Fishbone diagram.

    The SVG is a presentation asset for readability. It is not root-cause proof;
    listed causes remain hypotheses until verified.
    """

    _validate_fishbone(effect=effect, branches=branches)
    svg = _build_svg(effect=effect, branches=branches, source_note=source_note)
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(svg)
    return svg


def _validate_fishbone(*, effect: str, branches: tuple[FishboneBranch, ...]) -> None:
    if not effect.strip():
        raise ValueError("effect must be non-empty.")
    if not branches:
        raise ValueError("branches must include at least one branch.")
    for branch in branches:
        if not branch.name.strip():
            raise ValueError("branch name must be non-empty.")
        if not branch.causes:
            raise ValueError(f"branch {branch.name!r} must include at least one cause.")
        for cause in branch.causes:
            if not cause.label.strip():
                raise ValueError("cause label must be non-empty.")
            if cause.status not in _STATUS_LABELS:
                allowed = ", ".join(sorted(_STATUS_LABELS))
                raise ValueError(f"status must be one of: {allowed}.")


def _build_svg(
    *,
    effect: str,
    branches: tuple[FishboneBranch, ...],
    source_note: str,
) -> str:
    width = 1600
    height = 1120
    spine_y = 520
    spine_start = 150
    spine_end = 1120
    branch_slots = _branch_slots(branches, spine_start=spine_start)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}" role="img" '
        'aria-label="QCC Toolkit Python-generated Fishbone Diagram" '
        'data-layout="fixed-lanes" data-visible-causes-per-branch="2">',
        "<title>QCC Toolkit Python-generated Fishbone Diagram</title>",
        "<desc>Clean static SVG Fishbone diagram with short cause labels; "
        "causes remain hypotheses until verified.</desc>",
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#23313a}",
        ".title{font-size:28px;font-weight:700}",
        ".subtitle{font-size:14px;fill:#667178}",
        ".branch{font-size:13px;font-weight:700;fill:#fff}",
        ".cause{font-size:15px}",
        ".small{font-size:12px;fill:#5f6b72}",
        ".status{font-size:11px;font-weight:700;text-anchor:middle}",
        "</style>",
        '<rect x="0" y="0" width="1600" height="1120" fill="#ffffff"/>',
        '<text x="72" y="64" class="title">Python-generated Fishbone Diagram</text>',
        '<text x="72" y="92" class="subtitle">Clean static SVG: centered '
        "fishbone composition, short cause labels, and details in the "
        'verification plan.</text>',
        f'<line x1="{spine_start}" y1="{spine_y}" x2="{spine_end}" '
        f'y2="{spine_y}" stroke="#2f6f69" stroke-width="5" '
        'stroke-linecap="round"/>',
        _effect_box(spine_end + 42, spine_y - 70, effect),
    ]

    for slot in branch_slots:
        parts.extend(_branch_svg(slot, spine_y=spine_y))

    parts.extend(
        [
            _legend_svg(76, 960),
            _note_panel_svg(900, 940, source_note),
            "</svg>",
        ]
    )
    return "\n".join(parts)


def _branch_slots(
    branches: tuple[FishboneBranch, ...],
    *,
    spine_start: int,
) -> list[_BranchSlot]:
    max_branches = 6
    selected = branches[:max_branches]
    top_lanes = ((110, 130), (420, 130), (730, 130))
    bottom_lanes = ((110, 700), (420, 700), (730, 700))
    slots: list[_BranchSlot] = []
    for index, branch in enumerate(selected):
        upper = index % 2 == 0
        lane_index = index // 2
        lane_x, lane_y = (top_lanes if upper else bottom_lanes)[lane_index]
        spine_x = spine_start + 125 + lane_index * 310
        tip_y = 355 if upper else 655
        tip_x = lane_x + 190
        slots.append(
            _BranchSlot(
                branch=branch,
                upper=upper,
                spine_x=spine_x,
                tip_x=tip_x,
                tip_y=tip_y,
                lane="top" if upper else "bottom",
                lane_x=lane_x,
                lane_y=lane_y,
            )
        )
    return slots


def _branch_svg(slot: _BranchSlot, *, spine_y: int) -> list[str]:
    branch = slot.branch
    upper = slot.upper
    spine_x = slot.spine_x
    tip_x = slot.tip_x
    tip_y = slot.tip_y
    lane_x = slot.lane_x
    lane_y = slot.lane_y
    label_y = 338 if upper else 638

    parts = [
        f'<line x1="{spine_x}" y1="{spine_y}" x2="{tip_x}" y2="{tip_y}" '
        'stroke="#6f8580" stroke-width="3" stroke-linecap="round"/>',
        _branch_label(tip_x - 68, label_y, branch.name),
        f'<g data-lane="{slot.lane}" data-branch="{escape(branch.name)}">',
    ]
    for cause_index, cause in enumerate(branch.causes[:2]):
        parts.append(
            _cause_box(
                x=lane_x,
                y=lane_y + cause_index * 88,
                cause=cause,
            )
        )
    parts.append("</g>")
    return parts


def _cause_box(*, x: int, y: int, cause: FishboneCause) -> str:
    width = 260
    height = 66
    lines = _wrapped_text(cause.label, width=22, max_lines=2)
    text = "".join(
        f'<tspan x="{x + 68}" dy="{20 if index else 0}">{escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    return (
        f'<g data-box="{x},{y},{width},{height}" class="cause-box">'
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="12" '
        'fill="#f8f9f7" stroke="#c5ccc7"/>'
        f"{_status_badge(x + 16, y + 20, cause.status)}"
        f'<text x="{x + 68}" y="{y + 27}" class="cause">{text}</text>'
        "</g>"
    )


def _effect_box(x: int, y: int, effect: str) -> str:
    lines = _wrapped_text(effect, width=24, max_lines=3)
    text = "".join(
        f'<tspan x="{x + 26}" dy="{24 if index else 0}">{escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    return (
        f'<g data-effect="{escape(effect)}">'
        f'<rect x="{x}" y="{y}" width="300" height="138" rx="14" '
        'fill="#e8f1ef" stroke="#2f6f69" stroke-width="2"/>'
        f'<text x="{x + 26}" y="{y + 42}" font-size="18" '
        f'font-weight="700">{text}</text>'
        "</g>"
    )


def _branch_label(x: int, y: int, label: str) -> str:
    width = 136
    height = 34
    return (
        f'<g data-label-box="{x},{y},{width},{height}" class="branch-label">'
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="17" '
        'fill="#427e78" stroke="#427e78"/>'
        f'<text x="{x + 68}" y="{y + 22}" class="branch" '
        f'text-anchor="middle">{escape(label)}</text>'
        "</g>"
    )


def _status_badge(x: int, y: int, status: str) -> str:
    css_class, fill, stroke, color = _STATUS_LABELS[status]
    width = 42 if status != "V?" else 52
    label = f"[{status}]"
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="26" rx="13" '
        f'fill="{fill}" stroke="{stroke}"/>'
        f'<text x="{x + width / 2:.1f}" y="{y + 18}" '
        f'class="status status-badge {css_class}" fill="{color}">'
        f"{escape(label)}</text>"
    )


def _legend_svg(x: int, y: int) -> str:
    items = (
        ("S", "Suspected"),
        ("V?", "Selected for verification"),
        ("V", "Verified"),
        ("X", "Rejected"),
    )
    parts = [
        f'<rect x="{x}" y="{y}" width="705" height="92" rx="12" '
        'fill="#f8f9f7" stroke="#c5ccc7"/>',
        f'<text x="{x + 22}" y="{y + 28}" font-size="15" '
        'font-weight="700">Status badges</text>',
    ]
    item_x = x + 24
    for status, label in items:
        parts.append(_status_badge(item_x, y + 47, status))
        parts.append(
            f'<text x="{item_x + 62}" y="{y + 65}" '
            f'class="small">{escape(label)}</text>'
        )
        item_x += 162
    return "\n".join(parts)


def _note_panel_svg(x: int, y: int, source_note: str) -> str:
    source = source_note or "Source/session/date: [record on project slide]"
    return (
        f'<rect x="{x}" y="{y}" width="500" height="92" rx="12" '
        'fill="#f8f9f7" stroke="#c5ccc7"/>'
        f'<text x="{x + 22}" y="{y + 30}" font-size="15" '
        'font-weight="700">Review note</text>'
        f'<text x="{x + 22}" y="{y + 56}" class="small">'
        "Use short cause labels on the diagram; details stay in the "
        "verification plan.</text>"
        f'<text x="{x + 22}" y="{y + 76}" class="small">'
        f"{escape(source)}</text>"
    )


def _wrapped_text(text: str, *, width: int, max_lines: int) -> tuple[str, ...]:
    lines = wrap(" ".join(text.split()), width=width) or [text]
    if len(lines) <= max_lines:
        return tuple(lines)
    shortened = lines[:max_lines]
    shortened[-1] = shortened[-1].rstrip(".") + "..."
    return tuple(shortened)


__all__ = [
    "FishboneBranch",
    "FishboneCause",
    "render_fishbone_svg",
]
