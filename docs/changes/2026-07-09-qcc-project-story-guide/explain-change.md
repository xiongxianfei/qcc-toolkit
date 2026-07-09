# Explain Change: QCC Project Story Guide

## Summary

This change adds a small Markdown guide that explains how QCC methods connect across a project story.
It is intentionally placed before adding new method guides so users do not treat methods as disconnected tool pages.

## Governing direction

The guide is scoped under the approved Markdown-first method-guidance spec, especially R26: official guidance preserves QCC stage workflow and related-method links.

## What changed

| Surface | Change | Reason |
|---|---|---|
| `docs/qcc-project-story.md` | Added the project-story guide. | Users need a stage-level map before choosing more methods. |
| `README.md` | Linked the guide from the current guide surface. | The guide should be discoverable before individual method kits. |
| `docs/project-map.md` | Recorded the new guide in the observed repository layout. | Future agents need the current documentation surface. |
| `tests/test_markdown_first_method_guidance.py` | Added a focused structure and boundary test. | The guide needs proof for stage coverage, method links, and evidence boundaries. |

## Validation

| Command | Result |
|---|---|
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py::test_qcc_project_story_guide_connects_methods_across_project_flow -q` | 1 passed |
| `.venv/bin/python -m pytest tests/test_markdown_first_method_guidance.py tests/test_artifact_consistency.py -q` | 14 passed |
| `.venv/bin/python -m ruff check tests/test_markdown_first_method_guidance.py` | all checks passed |
| `git diff --check` | passed |

## Scope control

This change does not add new QCC methods, statistical calculations, chart rendering, PowerPoint templates, generated images, named-tool recipes, CI, or release automation.

## Handoff

Implementation is ready for code-review.
This artifact does not claim branch readiness, PR readiness, hosted CI success, or release readiness.
