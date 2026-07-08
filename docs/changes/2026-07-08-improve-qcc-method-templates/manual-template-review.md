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

## Review Scope

This manual note covers MP1 for the Pareto Chart template only.
MP2 and MP3 remain pending for later milestones.
