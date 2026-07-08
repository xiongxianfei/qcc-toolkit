"""Command-line entry point for template catalog validation."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

from qcc_toolkit.templates import CatalogValidationError, validate_template_catalog


def main() -> int:
    parser = ArgumentParser(prog="python -m qcc_toolkit.templates")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("catalog", type=Path)
    args = parser.parse_args()

    if args.command == "validate":
        try:
            catalog = validate_template_catalog(args.catalog)
        except CatalogValidationError as exc:
            parser.exit(
                status=1,
                message=f"Template catalog validation failed: {exc}\n",
            )
        print(f"validated {len(catalog.templates)} template catalog entries")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
