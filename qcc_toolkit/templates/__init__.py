"""Template catalog validation for first-slice QCC assets."""

from __future__ import annotations

from dataclasses import dataclass
from json import JSONDecodeError, loads
from pathlib import Path
from typing import Any


class CatalogValidationError(ValueError):
    """Raised when the PowerPoint template catalog is inconsistent."""


@dataclass(frozen=True)
class TemplateCatalogEntry:
    """A single first-slice template catalog entry."""

    template_id: str
    method_id: str
    template_type: str
    qcc_stages: tuple[str, ...]
    file: str
    markdown_guide: str
    supports_generated_chart: bool
    expected_placeholders: tuple[str, ...]
    expected_assets: tuple[str, ...]
    python_generator: str | None = None
    example_project: str | None = None
    source_file: str | None = None
    alternate_template: bool = False


@dataclass(frozen=True)
class TemplateCatalog:
    """Validated template catalog contents."""

    schema_version: int
    templates: tuple[TemplateCatalogEntry, ...]

    def by_method_id(self, method_id: str) -> TemplateCatalogEntry:
        """Return the first template entry for a method ID."""

        for entry in self.templates:
            if entry.method_id == method_id:
                return entry
        raise KeyError(f"Unknown method_id in template catalog: {method_id}")


def load_template_catalog(path: Path | str) -> TemplateCatalog:
    """Load the catalog from JSON-compatible YAML syntax."""

    catalog_path = Path(path)
    try:
        payload = loads(catalog_path.read_text())
    except JSONDecodeError as exc:
        raise CatalogValidationError(
            f"{catalog_path} must use JSON-compatible YAML syntax."
        ) from exc
    if not isinstance(payload, dict):
        raise CatalogValidationError(f"{catalog_path} must contain a mapping.")

    schema_version = payload.get("schema_version")
    if schema_version != 1:
        raise CatalogValidationError("Template catalog schema_version must be 1.")

    templates = payload.get("templates")
    if not isinstance(templates, list):
        raise CatalogValidationError("Template catalog must contain templates list.")

    return TemplateCatalog(
        schema_version=schema_version,
        templates=tuple(_entry_from_payload(entry) for entry in templates),
    )


def validate_template_catalog(
    path: Path | str,
    *,
    root: Path | str = ".",
) -> TemplateCatalog:
    """Validate catalog uniqueness, path references, and ownership rules."""

    catalog = load_template_catalog(path)
    root_path = Path(root)
    template_ids: set[str] = set()
    method_owner_ids: set[str] = set()

    for entry in catalog.templates:
        if entry.template_id in template_ids:
            raise CatalogValidationError(
                f"Duplicate template_id in template catalog: {entry.template_id}"
            )
        template_ids.add(entry.template_id)

        if not entry.alternate_template:
            if entry.method_id in method_owner_ids:
                raise CatalogValidationError(
                    f"duplicate method_id without alternate_template: {entry.method_id}"
                )
            method_owner_ids.add(entry.method_id)

        _validate_path(root_path, entry.file, "file", entry.template_id)
        _validate_path(
            root_path,
            entry.markdown_guide,
            "markdown_guide",
            entry.template_id,
        )
        _validate_markdown_guide_method_id(root_path, entry)
        if entry.python_generator is not None:
            _validate_path(
                root_path,
                entry.python_generator,
                "python_generator",
                entry.template_id,
            )
        if entry.example_project is not None:
            _validate_path(
                root_path,
                entry.example_project,
                "example_project",
                entry.template_id,
            )
        if entry.source_file is not None:
            _validate_path(
                root_path,
                entry.source_file,
                "source_file",
                entry.template_id,
            )

    return catalog


def _entry_from_payload(payload: object) -> TemplateCatalogEntry:
    if not isinstance(payload, dict):
        raise CatalogValidationError("Template catalog entries must be mappings.")

    required = (
        "template_id",
        "method_id",
        "template_type",
        "qcc_stages",
        "file",
        "markdown_guide",
        "supports_generated_chart",
        "expected_placeholders",
        "expected_assets",
    )
    for field in required:
        if field not in payload:
            raise CatalogValidationError(
                f"Catalog entry missing required field: {field}"
            )

    return TemplateCatalogEntry(
        template_id=_required_string(payload, "template_id"),
        method_id=_required_string(payload, "method_id"),
        template_type=_required_string(payload, "template_type"),
        qcc_stages=_string_tuple(payload, "qcc_stages"),
        file=_required_string(payload, "file"),
        markdown_guide=_required_string(payload, "markdown_guide"),
        supports_generated_chart=_required_bool(payload, "supports_generated_chart"),
        expected_placeholders=_string_tuple(payload, "expected_placeholders"),
        expected_assets=_string_tuple(payload, "expected_assets"),
        python_generator=_optional_string(payload, "python_generator"),
        example_project=_optional_string(payload, "example_project"),
        source_file=_optional_string(payload, "source_file"),
        alternate_template=bool(payload.get("alternate_template", False)),
    )


def _required_string(payload: dict[str, Any], field: str) -> str:
    value = payload[field]
    if not isinstance(value, str) or not value:
        raise CatalogValidationError(
            f"Catalog field {field} must be a non-empty string."
        )
    return value


def _optional_string(payload: dict[str, Any], field: str) -> str | None:
    value = payload.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise CatalogValidationError(
            f"Catalog field {field} must be a non-empty string."
        )
    return value


def _required_bool(payload: dict[str, Any], field: str) -> bool:
    value = payload[field]
    if not isinstance(value, bool):
        raise CatalogValidationError(f"Catalog field {field} must be a boolean.")
    return value


def _string_tuple(payload: dict[str, Any], field: str) -> tuple[str, ...]:
    value = payload[field]
    if not isinstance(value, list) or not value:
        raise CatalogValidationError(f"Catalog field {field} must be a non-empty list.")
    if not all(isinstance(item, str) and item for item in value):
        raise CatalogValidationError(f"Catalog field {field} must contain strings.")
    return tuple(value)


def _validate_path(root: Path, value: str, field: str, template_id: str) -> None:
    path = root / value
    if not path.exists():
        raise CatalogValidationError(
            f"{template_id} field {field} references missing path: {value}"
        )


def _validate_markdown_guide_method_id(
    root: Path,
    entry: TemplateCatalogEntry,
) -> None:
    path = root / entry.markdown_guide
    guide_method_id = _markdown_front_matter_value(path, "method_id")
    if guide_method_id != entry.method_id:
        raise CatalogValidationError(
            f"{entry.template_id} markdown_guide {entry.markdown_guide} "
            f"declares method_id {guide_method_id!r}, expected {entry.method_id!r}."
        )


def _markdown_front_matter_value(path: Path, field: str) -> str:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise CatalogValidationError(f"{path} is missing Markdown front matter.")
    _leading, front_matter, _body = text.split("---\n", 2)
    for line in front_matter.splitlines():
        if line.startswith(f"{field}:"):
            value = line.split(":", 1)[1].strip()
            if not value:
                raise CatalogValidationError(f"{path} has empty {field}.")
            return value
    raise CatalogValidationError(f"{path} is missing {field}.")


__all__ = [
    "CatalogValidationError",
    "TemplateCatalog",
    "TemplateCatalogEntry",
    "load_template_catalog",
    "validate_template_catalog",
]
