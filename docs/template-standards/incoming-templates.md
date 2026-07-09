# Incoming Template Handling

## Purpose

Incoming templates are user-created or legacy source assets.
They can preserve useful practice, layouts, examples, and wording, but they are not official method kits until reviewed and migrated.

## Storage

Place incoming source assets under `templates/incoming/`.
Do not place reviewed official method kits in this folder.
Do not register an incoming template as an official method kit in `templates/ppt/catalog.yml`.

## Intake Metadata

Record what is known before review:

- source or owner;
- method name and method ID if known;
- QCC stage if known;
- date received;
- intended user or training context;
- whether formulas, hidden notes, embedded files, linked files, or macros are present;
- whether the asset contains real or private data.

If the template has unknown method, unknown QCC stage, unknown owner, or unsupported formulas, it remains a source asset.

## Privacy Review

Incoming templates must be treated as untrusted until reviewed.
Before migration, check for:

- real customer names;
- employee names;
- supplier names;
- patient data;
- credentials;
- hidden notes;
- private data;
- internal comments;
- unsupported formulas;
- undocumented assumptions;
- stale examples.

Do not publish or catalog an incoming template as an official method kit until these risks are removed or documented as approved non-sensitive content.

## Migration to Official Kit

An incoming template can become part of an official method kit only after the useful content is migrated into reviewed assets:

- Markdown method guide;
- PowerPoint method template;
- PowerPoint source notes;
- completed demo example labeled as demo;
- blank working slide or worksheet;
- interpretation patterns;
- common mistakes;
- facilitator checklist;
- Python assist decision;
- Evidence/source note;
- catalog entry.

The original incoming file remains source reference material unless the team explicitly removes it after migration.
