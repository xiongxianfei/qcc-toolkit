# Manual Template Review: Improve QCC Method Templates

## Status

active

## MP1. Pareto Template Review

| Check | Result | Evidence |
|---|---|---|
| Pareto template is readable at the package/text level | pass | `python-pptx` inspection found 10 slides with clear section titles for purpose, data entry, stage fit, use/not-use, edit instructions, interpretation, checklist, evidence/source note, demo, and blank project slide. |
| Demo content is labeled as demo, not project evidence | pass | Slide 9 title and badge include `Completed demo example - DEMO EXAMPLE - not project evidence`; source notes also include `DEMO EXAMPLE - not project evidence`. |
| Blank slide is copyable | pass | Slide 10 is titled `Blank copyable project slide` and contains project title, chart area, source, date range, key finding, next action, and prepared-by/date fields. |
| Chart/table editing guidance is usable | pass | Slide 2 contains editable chart data; Slide 5 says to right-click the chart, choose Edit Data, replace demo categories/counts, sort descending, and verify formula cells. |
| Evidence/source notes are visible | pass | Slide 8 covers evidence levels and source/date/filter/calculation notes; source notes define the same evidence/source note contract. |
| Visual renderer limitation | noted | No PowerPoint or LibreOffice renderer is available in this environment. Review used deterministic PPTX generation, ZIP/package inspection, and `python-pptx` text/layout extraction. |

## Evidence Command

```text
.venv/bin/python - <<'PY'
from pathlib import Path
from pptx import Presentation

path = Path('templates/ppt/methods/pareto-chart-template.pptx')
prs = Presentation(path)
print(f'slides={len(prs.slides)} width={prs.slide_width} height={prs.slide_height}')
for index, slide in enumerate(prs.slides, start=1):
    texts = []
    for shape in slide.shapes:
        text = getattr(shape, 'text', '')
        if text:
            texts.append(' '.join(text.split())[:120])
    print(f'slide {index}: ' + ' | '.join(texts[:6]))
PY
```

## MP2. Template-Native Method Review

| Method | Result | Evidence |
|---|---|---|
| 5W2H | pass | Package/text inspection found 10 slides with demo labeling, blank working slide or worksheet, interpretation patterns, common mistakes, facilitator checklist, Python assist decision, evidence/source note, key conclusion, and next action surfaces. |
| 5 Whys | pass | Package/text inspection found 10 slides with demo labeling, blank working slide or worksheet, interpretation patterns, common mistakes, facilitator checklist, Python assist decision, evidence/source note, key conclusion, and next action surfaces. |
| Check Sheet | pass | Package/text inspection found 10 slides with demo labeling, blank working slide or worksheet, interpretation patterns, common mistakes, facilitator checklist, Python assist decision, evidence/source note, key conclusion, and next action surfaces. |
| Fishbone Diagram | pass | Package/text inspection found 10 slides with demo labeling, blank working slide or worksheet, interpretation patterns, common mistakes, facilitator checklist, Python assist decision, evidence/source note, key conclusion, and next action surfaces. |
| Readability and crowding | pass with limitation | Each deck uses the same two-column guidance slide pattern used by the reviewed Pareto kit and splits dense guidance across separate slides. No PowerPoint or LibreOffice renderer is available in this environment, so review used deterministic PPTX generation and ZIP/package text inspection rather than rendered screenshots. |

## MP2 Evidence Command

```text
.venv/bin/python - <<'PY'
from pathlib import Path
from zipfile import ZipFile
from qcc_toolkit.templates import validate_template_catalog

methods = ('5w2h', '5_whys', 'check_sheet', 'fishbone_diagram')
catalog = validate_template_catalog(Path('templates/ppt/catalog.yml'))
for method_id in methods:
    entry = catalog.by_method_id(method_id)
    with ZipFile(entry.file) as archive:
        slide_names = sorted(
            name for name in archive.namelist()
            if name.startswith('ppt/slides/slide') and name.endswith('.xml')
        )
        combined = '\n'.join(
            archive.read(name).decode('utf-8') for name in slide_names
        )
    print(f'{method_id}: slides={len(slide_names)}')
    for term in (
        'DEMO EXAMPLE - not project evidence',
        'Blank working slide or worksheet',
        'Facilitator checklist',
        'Python assist decision',
        'Evidence/source note',
        'Key conclusion',
        'Next action',
    ):
        print(f'  {term}: {term in combined}')
PY
```

Observed result: each M3 template reported `slides=10`, and every checked term returned `True`.

## Review Scope

## MP3. Final Method-Kit Set Review

| Method kit | Result | Evidence |
|---|---|---|
| Pareto Chart | pass | Package/text inspection found 10 slides with demo labeling, Evidence/source note, source, date range, and Python assist decision surfaces. |
| Check Sheet | pass | Package/text inspection found 10 slides with demo labeling, Evidence/source note, source, date range, and Python assist decision surfaces. |
| 5W2H | pass | Package/text inspection found 10 slides with demo labeling, Evidence/source note, source, date range, and Python assist decision surfaces. |
| Fishbone Diagram | pass | Package/text inspection found 10 slides with demo labeling, Evidence/source note, source, date range, and Python assist decision surfaces. |
| 5 Whys | pass | Package/text inspection found 10 slides with demo labeling, Evidence/source note, source, date range, and Python assist decision surfaces. |
| Final set consistency | pass with limitation | All official method kits expose the checked review terms at the package/text level. No PowerPoint or LibreOffice renderer is available in this environment, so MP3 does not claim rendered screenshot proof. |

## MP3 Evidence Command

```text
.venv/bin/python - <<'PY'
from pathlib import Path
from zipfile import ZipFile
from qcc_toolkit.templates import validate_template_catalog

catalog = validate_template_catalog(Path('templates/ppt/catalog.yml'))
terms = (
    'DEMO EXAMPLE - not project evidence',
    'Evidence/source note',
    'Source',
    'Date range',
    'Python assist decision',
)
for entry in catalog.official_templates:
    with ZipFile(entry.file) as archive:
        slides = sorted(
            name for name in archive.namelist()
            if name.startswith('ppt/slides/slide') and name.endswith('.xml')
        )
        combined = '\n'.join(
            archive.read(name).decode('utf-8') for name in slides
        )
    print(f'{entry.method_id}: slides={len(slides)}')
    for term in terms:
        print(f'  {term}: {term in combined}')
PY
```

Observed result: each official method kit reported `slides=10`, and every checked term returned `True`.

## Review Scope

This manual note covers MP1, MP2, and MP3.
