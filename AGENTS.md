# Aurex Corp VTT Agent Instructions

## Project Summary

Aurex Corp VTT is a local-first, minimal virtual tabletop for Dungeons & Dragons.

The application has two major user-facing surfaces:

- **GM interface:** read/write controls for managing the session.
- **Player display:** read-only display of public projected state.

The project should remain intentionally small, understandable, and easy to run locally.
Do not turn this into a full Foundry/Roll20 replacement unless explicitly asked.

## Core Safety Rule

Player display views must receive only public projected state.
Never expose hidden GM notes, private state, unrevealed monsters, secret counters, GM-only scene data, keys, tokens, or local file paths through player routes, player API payloads, static files, or client-side JavaScript.

When in doubt, create an explicit public-state projection layer instead of sharing full state with the frontend.

## Development Mode

This repository is currently in early phased development.

- Prefer small, phase-based changes.
- Do not add application code unless explicitly requested.
- Do not skip ahead into later roadmap phases unless explicitly asked.
- Keep each change easy to review.
- Prefer boring, readable Python and simple frontend code over clever abstractions.
- Avoid adding dependencies unless they clearly reduce complexity.
- Ask before introducing frameworks, databases, authentication systems, build tools, or package managers not already present.

## Repository Layout

Expected top-level structure:

```text
app/                  Application package and server code
docs/                 Stable project documentation
.ai-context/          Stable AI-agent project guidance
.brainstorming/       Agent scratch work, audits, analysis, and temporary planning notes
.project-board/       Local markdown project-board tickets organized by phase
AGENTS.md             Instructions for AI coding agents
README.md             Human-facing project overview
requirements.txt      Python dependencies, if any
pyproject.toml        Python project metadata/configuration, if used
```

## AI Playbooks

Recurring AI-assisted workflows live under `.ai-context/playbooks/`.

Playbooks are standard operating procedures for Codex and other AI agents. They describe how to perform recurring project activities; they are not brainstorming notes, tickets, or human-facing documentation.

Before beginning a new work session, consult:

```text
.ai-context/playbooks/session-start.md
```

Use that playbook to establish current context, identify the active phase or ticket, and produce a short startup brief before making changes.

When a task materially changes architecture, terminology, coding conventions, testing strategy, UI conventions, or recurring workflows, mention whether the relevant `.ai-context/` file or playbook should be updated. Do not make broad documentation maintenance changes unless the user requested them or they are directly necessary for the task.

## Documentation Boundaries

Use the right location for each kind of writing:

### `.ai-context/`

Use `.ai-context/` for stable, concise AI-agent guidance that should be consulted before making changes.

For the current file list and maintenance guidance, see `.ai-context/README.md`.

Before changing code, tests, UI, routes, docs, or tickets, read the relevant `.ai-context/` file(s) along with `AGENTS.md` and the source docs or tickets for the task.

Keep `.ai-context/` practical and derived from maintained project knowledge. Do not use it for speculative brainstorming; use `.brainstorming/` for that.

### `docs/`

Use `docs/` only for stable, intentional project documentation that should be treated as part of the maintained project knowledge base.

Examples:

- Architecture decisions
- API design
- State model
- Roadmap
- UI concepts
- Changelog
- Developer setup instructions

Do not place speculative audits, brainstorming, rough notes, or temporary analysis in `docs/`.

### `.brainstorming/`

Use `.brainstorming/` for unstructured working documents that are not code, not formal docs, and not direct project-board tickets.

Codex should place project analysis here when asked to audit, review, assess, compare, plan broadly, or brainstorm.

Examples:

- Codebase audits
- Architecture review notes
- Feature brainstorming
- Refactor analysis
- Risk assessments
- Scratch implementation plans
- Comparison notes
- Temporary design explorations

Suggested filename style:

```text
.brainstorming/YYYY-MM-DD-short-topic.md
```

Examples:

```text
.brainstorming/2026-06-29-phase-1-skeleton-audit.md
.brainstorming/2026-06-29-state-model-notes.md
```

Do not treat `.brainstorming/` files as binding requirements unless the user explicitly promotes them into `docs/` or `.project-board/`.

For project maintenance audits, use this filename unless the user requests a different name:

```text
.brainstorming/project-audit-YYYY-MM-DD.md
```

Audit reports should separate findings from proposed changes, list verification commands run, and clearly state whether any files were modified beyond the report itself.

### `.project-board/`

Use `.project-board/` for local markdown tickets, similar to a minimalist Jira board.
Tickets should be organized by development phase using `pNN` folder names.

Expected phase folders:

```text
.project-board/p00/   Phase 0 — Project planning and architecture
.project-board/p01/   Phase 1 — Application skeleton
.project-board/p02/   Phase 2 — Scene display
.project-board/p03/   Phase 3 — Generic trackers
.project-board/p04/   Phase 4 — Initiative tracker
```

Create additional `pNN` folders only when the roadmap adds new phases.

Suggested ticket filename style:

```text
.project-board/p01/p01-001-short-title.md
```

Ticket files should be concise and structured. Use this template unless told otherwise:

```markdown
# P01-001 Short Ticket Title

## Status

Backlog

## Phase

Phase 1 — Application Skeleton

## Goal

One or two sentences describing the intended outcome.

## Acceptance Criteria

- [ ] Specific, testable outcome
- [ ] Specific, testable outcome

## Notes

Optional context, constraints, or links to related docs.
```

Valid ticket statuses:

- Backlog
- Ready
- In Progress
- Blocked
- Done

When asked to create tickets, place them in `.project-board/pNN/`, not in `docs/` and not in `.brainstorming/`.

## Roadmap Discipline

Current roadmap phases are defined in `docs/roadmap.md`.
Use that file as the source of truth for phase names and goals.

Before implementing work, identify which phase the work belongs to.
If the requested work does not match the current phase, mention that briefly and proceed only if the user clearly asked for it.

## Coding Rules

- Keep the app local-first.
- Keep the player display passive/read-only.
- Backend owns canonical state.
- GM actions should update state through clear server-side routes or APIs.
- Player display routes should consume filtered public state only.
- Avoid global hidden state leaking into templates or JSON responses.
- Prefer explicit functions for state projection and validation.
- Keep routes small and easy to test.
- Prefer simple file/module organization until the project needs more structure.

## Python Rules

- Use clear standard-library Python where practical.
- Add dependencies to `requirements.txt` only when needed.
- If `pyproject.toml` is used, keep it minimal and consistent with the actual tooling.
- Do not assume a database exists unless one is introduced deliberately.
- Do not introduce async, WebSockets, or background workers unless explicitly requested.

## Frontend Rules

- Keep the player display readable from across a room.
- Keep the GM UI fast and practical over decorative.
- Avoid frontend frameworks unless explicitly requested.
- Avoid complex build steps while the app is still small.
- Prefer simple templates, static CSS, and small JavaScript files.

## Command and Permission Rules

- Explain planned changes before editing files when working interactively.
- Do not run destructive commands without explicit approval.
- Do not install packages without explicit approval.
- Do not modify files outside the repository.
- Do not commit, push, or create branches unless explicitly asked.
- If tests or run commands exist, use them after changes and summarize the result.
- If no test command exists, state that clearly and perform lightweight verification when possible.

## Git Hygiene

- Keep generated caches, virtual environments, and local runtime files out of version control.
- Do not commit `.venv/`, `__pycache__/`, build artifacts, local logs, or secrets.
- Use small commits grouped by purpose when the user asks for commits.
- Prefer phase-oriented commit messages, for example:

```text
p01: add basic GM and player routes
p01: define public state projection
p02: add scene image controls
```

## Secrets and Local Data

Never commit secrets, session keys, private game notes, real tokens, API keys, environment files, or local save data.

If sample data is needed, use clearly fake data and keep it minimal.

## Agent Output Expectations

When completing a task, summarize:

1. What changed.
2. Where the files are.
3. How to run or verify it.
4. Any limitations or follow-up tickets that should be created.

For broad audits or planning tasks, write the working document to `.brainstorming/` when asked to save it.
For ticket breakdowns, write ticket markdown files to `.project-board/pNN/`.
