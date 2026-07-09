"""Generate a readable static Fishbone SVG from synthetic demo content."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from qcc_toolkit import FishboneBranch, FishboneCause, render_fishbone_svg


def main(argv: Sequence[str] | None = None) -> int:
    """Run the Fishbone SVG starter script."""

    parser = argparse.ArgumentParser(
        description="Generate a clean local Fishbone SVG presentation asset.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output folder for fishbone.svg and README.md.",
    )
    args = parser.parse_args(argv)
    output_dir = Path(args.output)

    try:
        if output_dir.exists() and not output_dir.is_dir():
            raise ValueError(f"Output path must be a folder: {output_dir}")
        output_dir.mkdir(parents=True, exist_ok=True)
        svg_path = output_dir / "fishbone.svg"
        render_fishbone_svg(
            effect="Packing label defects increased on Line 2",
            branches=_demo_branches(),
            source_note="Synthetic QCC demo; not project evidence.",
            output_path=svg_path,
        )
        (output_dir / "README.md").write_text(_readme(svg_path.name))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"Fishbone SVG written to {svg_path}")
    return 0


def _demo_branches() -> tuple[FishboneBranch, ...]:
    return (
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
    )


def _readme(svg_filename: str) -> str:
    return "\n".join(
        (
            "# Python-Generated Fishbone Diagram",
            "",
            f"- Asset: `{svg_filename}`",
            "- Method: `fishbone_diagram`",
            "- Asset type: Clean static SVG presentation asset.",
            "",
            "This is synthetic demo content, not project evidence.",
            "Use it when the editable PowerPoint fishbone diagram is too hard to read.",
            "Listed causes remain hypotheses until verified.",
            "",
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
