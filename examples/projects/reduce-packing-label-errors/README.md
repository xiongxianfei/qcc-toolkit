# Reduce Packing Label Errors

Project ID: `reduce-packing-label-errors`

This is a synthetic QCC example project for learning and testing QCC Toolkit.
It does not contain real customer, employee, supplier, production, or private operational data.

## Data

- `data/packing_label_defects.csv`

The dataset summarizes simulated baseline packing label defects by defect type.

## Regenerate Pareto Evidence

Run from the repository root:

```sh
python examples/scripts/generate_pareto.py \
  --input examples/projects/reduce-packing-label-errors/data/packing_label_defects.csv \
  --category-column defect_type \
  --count-column count \
  --project examples/projects/reduce-packing-label-errors \
  --output examples/projects/reduce-packing-label-errors/evidence/pareto
```

The generated `evidence/pareto` folder is the authoritative calculation record.
Use the generated chart, calculated table, caption, warnings, and metadata when filling the Pareto PowerPoint template.

The same command also writes report-ready project output to:

- `report/report.md`
- `report/report.html`

## Generate Fishbone SVG

Run from the repository root:

```sh
python examples/scripts/generate_fishbone.py \
  --output examples/projects/reduce-packing-label-errors/evidence/fishbone
```

The generated `evidence/fishbone/fishbone.svg` is a static presentation asset for the Fishbone method kit.
It is not root-cause proof; listed causes remain hypotheses until verified.
