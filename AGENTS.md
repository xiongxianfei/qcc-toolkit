# Agent Operating Rules

This repository is governed by [CONSTITUTION.md](CONSTITUTION.md). Agents MUST read it before making substantive changes.

## Project Identity

QCC Toolkit is a Python-first, stage-aware evidence toolkit for Quality Control Circle projects. Changes MUST preserve the vision that charts, calculations, interpretations, and report artifacts are traceable QCC project evidence, not isolated utilities.

## Required Workflow

- Use [VISION.md](VISION.md) to check project fit before proposing new scope.
- Use `CONSTITUTION.md` as the highest operational rule source.
- For behavior changes, write or update a spec before implementation unless the change is trivial and fully described by an existing artifact.
- For cross-component or durable design decisions, write or update architecture documentation before implementation planning.
- Write tests or proof before production code when behavior is implemented or fixed.
- Run the relevant local verification commands before claiming completion. If no commands exist yet, state that clearly.

## Change Discipline

- MUST NOT make unrelated refactors, formatting churn, or broad template cleanup while doing a scoped task.
- MUST NOT silently invent QCC terminology, statistical assumptions, report semantics, or compatibility promises.
- MUST NOT claim CI, tests, package checks, or generated outputs passed without command evidence.
- MUST preserve user changes in the working tree unless the user explicitly asks to revert them.

## Documentation

Update docs when behavior, public API, QCC stage semantics, chart evidence metadata, compatibility, security, or workflow expectations change. Keep durable decisions in repository artifacts, not only in chat.
