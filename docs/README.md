# Documentation Index

Purpose: help humans and AI agents find the right maintained project documentation without overloading the main README.

Use `docs/` for stable, intentional project documentation. Do not place speculative audits, scratch plans, or temporary analysis here.

## Project Direction

- `roadmap.md` - phase names, phase status, current development position, and next planned work.
- `changelog.md` - durable summary of completed work by phase.
- `philosophy.md` - product philosophy and scope guardrails.

## Technical Design

- `architecture.md` - system shape, state ownership, player projection boundary, runtime shape.
- `state-model.md` - canonical session state, public/private fields, assets, scenes, trackers, initiative, save metadata.
- `api.md` - route conventions, public API, GM APIs, validation expectations, autosave response conventions.

## Development Workflow

- `developer-setup.md` - Python version, virtual environment, install, test, run, and runtime data guidance.
- `testing.md` - test strategy, current test layout, safety regression expectations.
- `project-maintenance-playbook.md` - human-facing maintenance workflows, audit prompts, and phase closeout procedures.

## Related Non-Docs Areas

- `../AGENTS.md` - global instructions for AI coding agents.
- `../.ai-context/` - stable AI-agent guidance and playbooks.
- `../.project-board/` - local markdown tickets organized by phase.
- `../.brainstorming/` - temporary audits, analysis, and scratch planning.

## Source Of Truth Notes

- Phase names and phase status: `roadmap.md`.
- Current actionable ticket: `../.project-board/active.md`.
- Public/player safety boundary: `architecture.md`, `state-model.md`, and `api.md`.
- Test command and test organization: `developer-setup.md` and `testing.md`.
