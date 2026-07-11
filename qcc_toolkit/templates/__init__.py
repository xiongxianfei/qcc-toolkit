"""Template catalog validation for first-slice QCC assets."""

from __future__ import annotations

from dataclasses import dataclass
from json import JSONDecodeError, loads
from pathlib import Path
from typing import Any


class CatalogValidationError(ValueError):
    """Raised when the PowerPoint template catalog is inconsistent."""


@dataclass(frozen=True)
class ChartEditability:
    """PowerPoint chart editability metadata for chart method kits."""

    editable_powerpoint_chart: bool
    non_editable_reason: str | None = None


@dataclass(frozen=True)
class TemplateCatalogEntry:
    """A single first-slice template catalog entry."""

    template_id: str
    catalog_status: str
    method_id: str
    method_name: str
    template_type: str
    implementation_mode: str
    qcc_stages: tuple[str, ...]
    file: str
    markdown_guide: str
    python_assist_status: str
    python_assist_reasons: tuple[str, ...]
    supports_generated_chart: bool
    required_content: tuple[str, ...]
    evidence_levels: tuple[str, ...]
    expected_placeholders: tuple[str, ...]
    expected_assets: tuple[str, ...]
    method_kit_status: str | None = None
    method_kit: str | None = None
    chart_editability: ChartEditability | None = None
    python_generator: str | None = None
    example_project: str | None = None
    source_file: str | None = None
    sample_input: str | None = None
    runnable_assist: str | None = None
    generated_output_example: str | None = None
    reproducibility_note: str | None = None
    alternate_template: bool = False


@dataclass(frozen=True)
class TemplateCatalog:
    """Validated template catalog contents."""

    schema_version: int
    templates: tuple[TemplateCatalogEntry, ...]

    @property
    def official_templates(self) -> tuple[TemplateCatalogEntry, ...]:
        """Return entries classified as official method kits."""

        return tuple(
            entry for entry in self.templates if entry.catalog_status == "official"
        )

    def by_method_id(self, method_id: str) -> TemplateCatalogEntry:
        """Return the first official template entry for a method ID."""

        for entry in self.official_templates:
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

        if entry.catalog_status == "official" and not entry.alternate_template:
            if entry.method_id in method_owner_ids:
                raise CatalogValidationError(
                    f"duplicate method_id without alternate_template: {entry.method_id}"
                )
            method_owner_ids.add(entry.method_id)

        _validate_entry_contract(entry)
        _validate_path(root_path, entry.file, "file", entry.template_id)
        _validate_path(
            root_path,
            entry.markdown_guide,
            "markdown_guide",
            entry.template_id,
        )
        _validate_markdown_guide_method_id(root_path, entry)
        if entry.method_kit is not None:
            _validate_path(root_path, entry.method_kit, "method_kit", entry.template_id)
            if (
                entry.method_kit_status == "available"
                and entry.markdown_guide != entry.method_kit
            ):
                raise CatalogValidationError(
                    f"{entry.template_id} available method_kit must match "
                    "markdown_guide."
                )
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
        elif entry.catalog_status == "official":
            raise CatalogValidationError(
                f"{entry.template_id} official entry missing source_file."
            )
        if entry.sample_input is not None:
            _validate_path(
                root_path,
                entry.sample_input,
                "sample_input",
                entry.template_id,
            )
        if entry.runnable_assist is not None:
            _validate_path(
                root_path,
                entry.runnable_assist,
                "runnable_assist",
                entry.template_id,
            )
        if entry.generated_output_example is not None:
            _validate_path(
                root_path,
                entry.generated_output_example,
                "generated_output_example",
                entry.template_id,
            )
        if entry.reproducibility_note is not None:
            _validate_path(
                root_path,
                entry.reproducibility_note,
                "reproducibility_note",
                entry.template_id,
            )

    return catalog


def _entry_from_payload(payload: object) -> TemplateCatalogEntry:
    if not isinstance(payload, dict):
        raise CatalogValidationError("Template catalog entries must be mappings.")

    required = (
        "template_id",
        "catalog_status",
        "method_id",
        "method_name",
        "template_type",
        "implementation_mode",
        "qcc_stages",
        "file",
        "markdown_guide",
        "python_assist_status",
        "supports_generated_chart",
        "required_content",
        "evidence_levels",
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
        catalog_status=_enum_value(
            payload,
            "catalog_status",
            {"official", "incoming", "source"},
        ),
        method_id=_required_string(payload, "method_id"),
        method_name=_required_string(payload, "method_name"),
        template_type=_required_string(payload, "template_type"),
        implementation_mode=_enum_value(
            payload,
            "implementation_mode",
            {
                "template_native_worksheet",
                "template_native_diagram",
                "powerpoint_native_chart",
                "python_assisted_chart",
                "python_first_analysis",
            },
        ),
        qcc_stages=_string_tuple(payload, "qcc_stages"),
        file=_required_string(payload, "file"),
        markdown_guide=_required_string(payload, "markdown_guide"),
        python_assist_status=_enum_value(
            payload,
            "python_assist_status",
            {"unavailable", "optional", "recommended", "required"},
        ),
        python_assist_reasons=_optional_string_tuple(payload, "python_assist_reasons"),
        supports_generated_chart=_required_bool(payload, "supports_generated_chart"),
        required_content=_string_tuple(payload, "required_content"),
        evidence_levels=_string_tuple(payload, "evidence_levels"),
        expected_placeholders=_string_tuple(payload, "expected_placeholders"),
        expected_assets=_string_tuple(payload, "expected_assets"),
        method_kit_status=_optional_string(payload, "method_kit_status"),
        method_kit=_optional_string(payload, "method_kit"),
        chart_editability=_chart_editability(payload.get("chart_editability")),
        python_generator=_optional_string(payload, "python_generator"),
        example_project=_optional_string(payload, "example_project"),
        source_file=_optional_string(payload, "source_file"),
        sample_input=_optional_string(payload, "sample_input"),
        runnable_assist=_optional_string(payload, "runnable_assist"),
        generated_output_example=_optional_string(payload, "generated_output_example"),
        reproducibility_note=_optional_string(payload, "reproducibility_note"),
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


def _enum_value(payload: dict[str, Any], field: str, allowed: set[str]) -> str:
    value = _required_string(payload, field)
    if value not in allowed:
        allowed_values = ", ".join(sorted(allowed))
        raise CatalogValidationError(
            f"Catalog field {field} must be one of: {allowed_values}."
        )
    return value


def _string_tuple(payload: dict[str, Any], field: str) -> tuple[str, ...]:
    value = payload[field]
    if not isinstance(value, list) or not value:
        raise CatalogValidationError(f"Catalog field {field} must be a non-empty list.")
    if not all(isinstance(item, str) and item for item in value):
        raise CatalogValidationError(f"Catalog field {field} must contain strings.")
    return tuple(value)


def _optional_string_tuple(payload: dict[str, Any], field: str) -> tuple[str, ...]:
    value = payload.get(field)
    if value is None:
        return ()
    if not isinstance(value, list):
        raise CatalogValidationError(f"Catalog field {field} must be a list.")
    if not all(isinstance(item, str) and item for item in value):
        raise CatalogValidationError(f"Catalog field {field} must contain strings.")
    return tuple(value)


def _chart_editability(value: object) -> ChartEditability | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise CatalogValidationError(
            "Catalog field chart_editability must be a mapping."
        )

    editable = value.get("editable_powerpoint_chart")
    if not isinstance(editable, bool):
        raise CatalogValidationError(
            "Catalog field chart_editability.editable_powerpoint_chart "
            "must be a boolean."
        )

    reason = value.get("non_editable_reason")
    if reason is not None and (not isinstance(reason, str) or not reason):
        raise CatalogValidationError(
            "Catalog field chart_editability.non_editable_reason must be a "
            "non-empty string."
        )
    if editable is False and reason is None:
        raise CatalogValidationError(
            "Catalog field chart_editability.non_editable_reason is required "
            "when editable_powerpoint_chart is false."
        )
    return ChartEditability(
        editable_powerpoint_chart=editable,
        non_editable_reason=reason,
    )


def _validate_entry_contract(entry: TemplateCatalogEntry) -> None:
    if entry.catalog_status != "official":
        return

    missing_required_content = _MINIMUM_REQUIRED_CONTENT.difference(
        entry.required_content
    )
    if missing_required_content:
        missing = ", ".join(sorted(missing_required_content))
        raise CatalogValidationError(
            f"{entry.template_id} required_content missing: {missing}"
        )

    missing_evidence_levels = _REQUIRED_EVIDENCE_LEVELS.difference(
        entry.evidence_levels
    )
    if missing_evidence_levels:
        missing = ", ".join(sorted(missing_evidence_levels))
        raise CatalogValidationError(
            f"{entry.template_id} evidence_levels missing: {missing}"
        )

    if entry.python_assist_status == "unavailable":
        if entry.python_assist_reasons:
            raise CatalogValidationError(
                f"{entry.template_id} python_assist_reasons must be empty "
                "when python_assist_status is unavailable."
            )
    elif not entry.python_assist_reasons:
        raise CatalogValidationError(
            f"{entry.template_id} python_assist_reasons required for "
            f"python_assist_status {entry.python_assist_status}."
        )

    if entry.implementation_mode in _CHART_IMPLEMENTATION_MODES:
        if entry.chart_editability is None:
            raise CatalogValidationError(
                f"{entry.template_id} chart_editability is required for "
                f"implementation_mode {entry.implementation_mode}."
            )
        missing_chart_content = _CHART_REQUIRED_CONTENT.difference(
            entry.required_content
        )
        if missing_chart_content:
            missing = ", ".join(sorted(missing_chart_content))
            raise CatalogValidationError(
                f"{entry.template_id} required_content missing chart items: {missing}"
            )

    if _requires_python_assist_artifacts(entry):
        required_paths = {
            "sample_input": entry.sample_input,
            "runnable_assist": entry.runnable_assist,
            "generated_output_example": entry.generated_output_example,
            "reproducibility_note": entry.reproducibility_note,
        }
        for field, value in required_paths.items():
            if value is None:
                raise CatalogValidationError(
                    f"{entry.template_id} {field} is required for "
                    f"implementation_mode {entry.implementation_mode} and "
                    f"python_assist_status {entry.python_assist_status}."
                )


def _requires_python_assist_artifacts(entry: TemplateCatalogEntry) -> bool:
    return (
        entry.implementation_mode in {"python_assisted_chart", "python_first_analysis"}
        or entry.python_assist_status in {"recommended", "required"}
    )


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
    guide_method_id = _markdown_method_id(path)
    if not _method_ids_match(guide_method_id, entry.method_id):
        raise CatalogValidationError(
            f"{entry.template_id} markdown_guide {entry.markdown_guide} "
            f"declares method_id {guide_method_id!r}, expected {entry.method_id!r}."
        )


def _markdown_method_id(path: Path) -> str:
    text = path.read_text()
    if text.startswith("---\n"):
        return _markdown_front_matter_value(path, "method_id")

    for line in text.splitlines():
        if line.startswith("Method ID:"):
            value = line.split(":", 1)[1].strip()
            if not value:
                raise CatalogValidationError(f"{path} has empty Method ID.")
            return value
        if line.startswith("Metadata:") and "](" in line and line.endswith(")"):
            metadata_link = line.rsplit("(", 1)[1].removesuffix(")")
            return _metadata_field_value(path.parent / metadata_link, "method_id")

    raise CatalogValidationError(f"{path} is missing method_id.")


def _metadata_field_value(path: Path, field: str) -> str:
    for line in path.read_text().splitlines():
        if line.startswith(f"{field}:"):
            value = line.split(":", 1)[1].strip()
            if not value:
                raise CatalogValidationError(f"{path} has empty {field}.")
            return value
    raise CatalogValidationError(f"{path} is missing {field}.")


def _method_ids_match(guide_method_id: str, catalog_method_id: str) -> bool:
    aliases = {
        "check-sheet": "check_sheet",
        "fishbone-diagram": "fishbone_diagram",
        "five-whys": "5_whys",
        "five-w-two-h": "5w2h",
        "pareto-chart": "pareto_chart",
    }
    return aliases.get(guide_method_id, guide_method_id) == catalog_method_id


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
    "ChartEditability",
    "CatalogValidationError",
    "TemplateCatalog",
    "TemplateCatalogEntry",
    "load_template_catalog",
    "validate_template_catalog",
]


_MINIMUM_REQUIRED_CONTENT = {
    "markdown_guide",
    "powerpoint_template",
    "completed_demo_example",
    "blank_copyable_slide",
    "interpretation_patterns",
    "common_mistakes",
    "facilitator_checklist",
    "python_assist_decision",
    "evidence_source_note",
    "catalog_entry",
}

_CHART_REQUIRED_CONTENT = {
    "sample_data_table",
    "chart_editing_instructions",
}

_CHART_IMPLEMENTATION_MODES = {
    "powerpoint_native_chart",
    "python_assisted_chart",
}

_REQUIRED_EVIDENCE_LEVELS = {
    "teaching_draft",
    "normal_qcc_project",
    "competition_management_review",
    "audit_high_risk",
}
